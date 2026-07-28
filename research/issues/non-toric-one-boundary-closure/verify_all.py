#!/usr/bin/env python3
"""Packet-level verification for non-toric one-boundary closure."""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REQUIRED = {
    "README.md",
    "FOUNDATIONS.md",
    "BOUNDARY_NORMALIZATION.md",
    "LAURENT_RECURSION.md",
    "CONDUCTOR_GLUING.md",
    "LOGARITHMIC_FIELDS.md",
    "WEIGHT_EXTRACTION.md",
    "CASE_TABLE.md",
    "FORMAL_MODELS.md",
    "SOURCE_AUDIT.md",
    "REVIEW.md",
    "HANDOFF.md",
    "validate_laurent_conductor.py",
    "verify_all.py",
    "INTEGRATION.json",
}


def fail(message: str) -> None:
    raise AssertionError(message)


def check_files() -> None:
    present = {path.name for path in ROOT.iterdir() if path.is_file()}
    missing = sorted(REQUIRED - present)
    if missing:
        fail(f"missing required artifacts: {missing}")
    forbidden = [
        path.name
        for path in ROOT.iterdir()
        if path.is_file()
        and (path.suffix == ".b64" or path.name.startswith("sync_") or path.name == "SYNC_REPORT.md")
    ]
    if forbidden:
        fail(f"forbidden temporary artifacts: {forbidden}")


def check_manifest() -> None:
    manifest = json.loads((ROOT / "INTEGRATION.json").read_text())
    expected = {
        "schema_version": 1,
        "issue_number": 5,
        "leaf_id": "L03",
        "role": "integration-maintainer",
        "owned_paths": ["research/issues/non-toric-one-boundary-closure/"],
        "base_sha": "72e09753d1a1523ff22b44093cc65e21384613fc",
        "review_mode": "local-adversarial-review",
        "integration_state": "integration-ready",
        "pr_number": 57,
        "temporary_artifacts_absent": True,
    }
    for key, value in expected.items():
        if manifest.get(key) != value:
            fail(f"manifest {key}: expected {value!r}, got {manifest.get(key)!r}")
    for field in ("candidate_sha", "reviewed_revision"):
        value = manifest.get(field)
        if not isinstance(value, str) or len(value) != 40 or any(ch not in "0123456789abcdef" for ch in value):
            fail(f"manifest {field} is not a 40-character lowercase SHA")
    if manifest["candidate_sha"] != manifest["reviewed_revision"]:
        fail("review must bind the exact candidate SHA")
    expected_ids = [f"CLM-{number:03d}" for number in range(86, 95)]
    actual_ids = [
        str(item.get("id", ""))
        for item in manifest.get("proposed_global_claims", [])
        if isinstance(item, dict)
    ]
    if actual_ids != expected_ids:
        fail(f"canonical claim mapping: expected {expected_ids!r}, got {actual_ids!r}")


def check_markers() -> None:
    readme = (ROOT / "README.md").read_text()
    review = (ROOT / "REVIEW.md").read_text()
    handoff = (ROOT / "HANDOFF.md").read_text()
    required_markers = {
        "README.md": ["NTLC-04", "Liouville-nonexact", "does **not** exclude every"],
        "REVIEW.md": ["local-adversarial-review", "BLOCK_PROMOTION", "candidate_revision"],
        "HANDOFF.md": ["issue #13", "Mainline completion", "CLM-094"],
    }
    texts = {"README.md": readme, "REVIEW.md": review, "HANDOFF.md": handoff}
    for name, markers in required_markers.items():
        for marker in markers:
            if marker not in texts[name]:
                fail(f"{name}: missing marker {marker!r}")


def check_symbolics() -> None:
    subprocess.run(
        [
            sys.executable,
            str(ROOT / "validate_laurent_conductor.py"),
            "--max-e",
            "6",
            "--max-m",
            "6",
            "--order",
            "10",
            "--max-power",
            "10",
            "--json",
        ],
        cwd=ROOT,
        check=True,
    )


def main() -> int:
    check_files()
    check_manifest()
    check_markers()
    check_symbolics()
    print("non-toric one-boundary packet: PASS")
    print("mathematical truth and promotion authority: NOT EVALUATED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
