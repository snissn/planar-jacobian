from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

import sys

SCRIPT_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SCRIPT_DIR))

from validate_integration_contract import PullRequestContext, validate_root  # noqa: E402

VALID_SHA_A = "a" * 40
VALID_SHA_B = "b" * 40


def write(path: Path, content: str = "x\n") -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def manifest(
    role: str = "research-worker",
    review_mode: str = "none",
    *,
    issue_number: int = 99,
    leaf_id: str = "L99",
    owned_path: str = "research/issues/example/",
) -> dict:
    return {
        "schema_version": 1,
        "issue_number": issue_number,
        "leaf_id": leaf_id,
        "role": role,
        "owned_paths": [owned_path],
        "base_sha": VALID_SHA_A,
        "candidate_sha": VALID_SHA_B,
        "scientific_status": "MUTABLE_NONAUTHORITATIVE",
        "review_mode": review_mode,
        "reviewed_revision": VALID_SHA_B if review_mode != "none" else None,
        "proposed_global_claims": [],
        "proposed_graph_nodes": [],
        "shared_surfaces_requested": [],
        "supersedes_prs": [],
        "temporary_artifacts_absent": True,
        "integration_state": "integration-ready",
    }


class IntegrationContractTests(unittest.TestCase):
    def make_repo(self, data: dict | None = None) -> Path:
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        root = Path(temp.name)
        write(root / ".github/workflows/repository-python-validators.yml", "permissions:\n  contents: read\n")
        write(root / "research/issues/example/README.md")
        write(root / "research/issues/example/INTEGRATION.json", json.dumps(data or manifest(), indent=2) + "\n")
        return root

    def test_valid_worker_packet(self) -> None:
        self.assertEqual([], validate_root(self.make_repo()).errors)

    def test_forbidden_base64_payload(self) -> None:
        root = self.make_repo(); write(root / "research/issues/example/payload.b64")
        self.assertTrue(any("base64" in e for e in validate_root(root).errors))

    def test_workflow_contents_write_is_rejected(self) -> None:
        root = self.make_repo(); write(root / ".github/workflows/repository-python-validators.yml", "permissions:\n  contents: write\n")
        self.assertTrue(any("contents: write" in e for e in validate_root(root).errors))

    def test_worker_cannot_change_shared_ledger(self) -> None:
        root = self.make_repo()
        context = PullRequestContext(1, False, "main", VALID_SHA_A, VALID_SHA_B, "- Role: research-worker\n- Task-Issue: #99\n- Owned-Path: research/issues/example/\n", "o/r")
        result = validate_root(root, context=context, changed_files=["research/issues/example/README.md", "research/claim_ledger.json"], remote_prs=[])
        self.assertTrue(any("shared surface" in e or "outside ownership" in e for e in result.errors))

    def test_review_requires_revision(self) -> None:
        data = manifest(review_mode="local-adversarial-review"); data["reviewed_revision"] = None
        self.assertTrue(any("reviewed_revision" in e for e in validate_root(self.make_repo(data)).errors))

    def test_duplicate_open_pr_is_rejected(self) -> None:
        root = self.make_repo(); body = "- Role: research-worker\n- Task-Issue: #99\n- Owned-Path: research/issues/example/\n"
        context = PullRequestContext(2, False, "main", VALID_SHA_A, VALID_SHA_B, body, "o/r")
        result = validate_root(root, context=context, changed_files=["research/issues/example/README.md"], remote_prs=[{"number": 3, "body": body}])
        self.assertTrue(any("duplicate open PR" in e for e in result.errors))

    def test_pure_governance_can_add_historical_manifests(self) -> None:
        data = manifest(role="integration-maintainer"); data["integration_state"] = "merged"
        root = self.make_repo(data)
        context = PullRequestContext(2, False, "main", VALID_SHA_A, VALID_SHA_B, "- Role: governance-maintainer\n- Task-Issue: #2\n- Owned-Path: governance/\n", "o/r")
        result = validate_root(root, context=context, changed_files=["governance/EXECUTION-LIFECYCLE.md", "research/issues/example/INTEGRATION.json", "scripts/validate_integration_contract.py"], remote_prs=[])
        self.assertEqual([], result.errors)

    def test_governance_pr_requires_exactly_one_metadata_marker(self) -> None:
        root = self.make_repo()
        context = PullRequestContext(
            2,
            False,
            "main",
            VALID_SHA_A,
            VALID_SHA_B,
            "- Role: governance-maintainer\n- Task-Issue: #99\n",
            "o/r",
        )
        result = validate_root(
            root,
            context=context,
            changed_files=["scripts/validate_integration_contract.py"],
            remote_prs=[],
        )
        self.assertTrue(any("exactly one Owned-Path" in e for e in result.errors))

    def test_duplicate_governance_pr_is_rejected(self) -> None:
        root = self.make_repo()
        body = "- Role: governance-maintainer\n- Task-Issue: #99\n- Owned-Path: governance/\n"
        context = PullRequestContext(2, False, "main", VALID_SHA_A, VALID_SHA_B, body, "o/r")
        result = validate_root(
            root,
            context=context,
            changed_files=["scripts/validate_integration_contract.py"],
            remote_prs=[{"number": 3, "body": body}],
        )
        self.assertTrue(any("duplicate open PR" in e for e in result.errors))

    def test_integration_maintainer_must_use_current_base(self) -> None:
        data = manifest(role="integration-maintainer"); data["base_sha"] = "c" * 40
        root = self.make_repo(data); body = "- Role: integration-maintainer\n- Task-Issue: #99\n- Owned-Path: research/issues/example/\n"
        context = PullRequestContext(2, False, "main", VALID_SHA_A, VALID_SHA_B, body, "o/r")
        result = validate_root(root, context=context, changed_files=["research/issues/example/README.md"], remote_prs=[])
        self.assertTrue(any("does not match current PR base" in e for e in result.errors))

    def test_manifest_requires_exactly_one_owned_packet_root(self) -> None:
        data = manifest()
        data["owned_paths"].append("research/claim_ledger.json")
        result = validate_root(self.make_repo(data))
        self.assertTrue(any("exactly one issue-owned path" in e for e in result.errors))

    def test_unselected_manifest_cannot_authorize_changed_files(self) -> None:
        selected = manifest(role="integration-maintainer")
        root = self.make_repo(selected)
        other = manifest(
            role="integration-maintainer",
            issue_number=100,
            leaf_id="L100",
            owned_path="research/issues/other/",
        )
        write(root / "research/issues/other/README.md")
        write(root / "research/issues/other/INTEGRATION.json", json.dumps(other, indent=2) + "\n")
        body = "- Role: integration-maintainer\n- Task-Issue: #99\n- Owned-Path: research/issues/example/\n"
        context = PullRequestContext(2, False, "main", VALID_SHA_A, VALID_SHA_B, body, "o/r")
        result = validate_root(
            root,
            context=context,
            changed_files=[
                "research/issues/example/README.md",
                "research/issues/other/README.md",
            ],
            remote_prs=[],
        )
        self.assertTrue(any("selected manifest" in e for e in result.errors))

    def test_integration_maintainer_must_declare_shared_surface(self) -> None:
        data = manifest(role="integration-maintainer")
        root = self.make_repo(data)
        body = "- Role: integration-maintainer\n- Task-Issue: #99\n- Owned-Path: research/issues/example/\n"
        context = PullRequestContext(2, False, "main", VALID_SHA_A, VALID_SHA_B, body, "o/r")
        result = validate_root(
            root,
            context=context,
            changed_files=[
                "research/issues/example/README.md",
                "research/claim_ledger.json",
            ],
            remote_prs=[],
        )
        self.assertTrue(any("not requested by selected manifest" in e for e in result.errors))

    def test_integration_maintainer_cannot_change_governance_surface(self) -> None:
        data = manifest(role="integration-maintainer")
        data["shared_surfaces_requested"] = ["scripts/validate_repository.py"]
        root = self.make_repo(data)
        body = "- Role: integration-maintainer\n- Task-Issue: #99\n- Owned-Path: research/issues/example/\n"
        context = PullRequestContext(2, False, "main", VALID_SHA_A, VALID_SHA_B, body, "o/r")
        result = validate_root(
            root,
            context=context,
            changed_files=[
                "research/issues/example/README.md",
                "scripts/validate_repository.py",
            ],
            remote_prs=[],
        )
        self.assertTrue(any("may not edit governance surface" in e for e in result.errors))

    def test_integration_maintainer_can_change_declared_shared_surface(self) -> None:
        data = manifest(role="integration-maintainer")
        data["shared_surfaces_requested"] = ["research/claim_ledger.json"]
        root = self.make_repo(data)
        body = "- Role: integration-maintainer\n- Task-Issue: #99\n- Owned-Path: research/issues/example/\n"
        context = PullRequestContext(2, False, "main", VALID_SHA_A, VALID_SHA_B, body, "o/r")
        result = validate_root(
            root,
            context=context,
            changed_files=[
                "research/issues/example/README.md",
                "research/claim_ledger.json",
            ],
            remote_prs=[],
        )
        self.assertEqual([], result.errors)

    def test_integration_maintainer_can_add_declared_freeze_record(self) -> None:
        data = manifest(role="integration-maintainer")
        freeze = "governance/reviews/issue-99-freeze.md"
        data["shared_surfaces_requested"] = [freeze]
        root = self.make_repo(data)
        body = "- Role: integration-maintainer\n- Task-Issue: #99\n- Owned-Path: research/issues/example/\n"
        context = PullRequestContext(2, False, "main", VALID_SHA_A, VALID_SHA_B, body, "o/r")
        result = validate_root(
            root,
            context=context,
            changed_files=["research/issues/example/README.md", freeze],
            remote_prs=[],
        )
        self.assertEqual([], result.errors)

    def test_integration_maintainer_cannot_request_another_packet(self) -> None:
        data = manifest(role="integration-maintainer")
        data["shared_surfaces_requested"] = ["research/issues/other/PROOF.md"]
        result = validate_root(self.make_repo(data))
        self.assertTrue(any("noncanonical shared surfaces" in e for e in result.errors))


if __name__ == "__main__":
    unittest.main()
