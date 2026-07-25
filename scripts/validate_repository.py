#!/usr/bin/env python3
"""Validate repository structure, ledgers, generated views, provenance, and links.

This validator deliberately does not evaluate mathematical truth or review quality.
"""
from __future__ import annotations

import base64
import gzip
import hashlib
import json
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any, Iterable
from urllib.parse import unquote, urlsplit

import render_views

ROOT = Path(__file__).resolve().parents[1]
ERRORS: list[str] = []
WARNINGS: list[str] = []
HEX40 = re.compile(r"^[0-9a-f]{40}$")
HEX64 = re.compile(r"^[0-9a-f]{64}$")


def error(message: str) -> None:
    ERRORS.append(message)


def warning(message: str) -> None:
    WARNINGS.append(message)


def load_json(path: str) -> dict[str, Any]:
    try:
        return json.loads((ROOT / path).read_text(encoding="utf-8"))
    except Exception as exc:  # pragma: no cover - diagnostic path
        error(f"{path}: {exc}")
        return {}


def duplicates(values: Iterable[str]) -> set[str]:
    counts = Counter(values)
    return {value for value, count in counts.items() if count > 1}


def validate_all_json() -> None:
    for path in sorted(ROOT.rglob("*.json")):
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except Exception as exc:
            error(f"invalid JSON {path.relative_to(ROOT)}: {exc}")


def validate_claims(claims: dict[str, Any]) -> tuple[set[str], dict[str, dict[str, Any]]]:
    if claims.get("schema_version") != 1:
        error("research/claim_ledger.json: unsupported schema_version")
    vocabulary = claims.get("status_vocabulary", [])
    required_vocabulary = {
        "reviewed_scoped",
        "verified_internal",
        "verified_conceptual",
        "candidate_proved",
        "candidate",
        "literature_bound",
        "source_audit_required",
        "open_bridge",
        "speculative",
        "retired",
    }
    if set(vocabulary) != required_vocabulary:
        error("research/claim_ledger.json: unexpected status vocabulary")
    for value in sorted(duplicates(vocabulary)):
        error(f"research/claim_ledger.json: duplicate status {value}")

    items = claims.get("claims", [])
    ids = [item.get("id", "") for item in items]
    for item_id in sorted(duplicates(ids)):
        error(f"duplicate claim id: {item_id}")
    claim_ids = set(ids)
    by_id = {item.get("id", ""): item for item in items if item.get("id")}

    expected_sequence = [f"CLM-{number:03d}" for number in range(1, 73)]
    if ids != expected_sequence:
        error("claim IDs must be the ordered contiguous sequence CLM-001 through CLM-066")

    for item in items:
        item_id = item.get("id", "<missing>")
        for field in ["id", "status", "track", "statement", "depends_on", "note"]:
            if field not in item:
                error(f"claim {item_id}: missing field {field}")
        if item.get("status") not in vocabulary:
            error(f"claim {item_id}: unknown status {item.get('status')!r}")
        dependencies = item.get("depends_on", [])
        if not isinstance(dependencies, list):
            error(f"claim {item_id}: depends_on is not a list")
            dependencies = []
        if len(dependencies) != len(set(dependencies)):
            error(f"claim {item_id}: duplicate dependency")
        if item_id in dependencies:
            error(f"claim {item_id}: self dependency")
        for dependency in dependencies:
            if dependency not in claim_ids:
                error(f"claim {item_id}: missing dependency {dependency}")

        review = item.get("review")
        if item.get("status") == "reviewed_scoped":
            if not isinstance(review, dict):
                error(f"claim {item_id}: reviewed_scoped requires review metadata")
                continue
            expected_fields = {
                "mode",
                "disposition",
                "reviewed_revision",
                "candidate_aggregate_sha256",
                "review_record",
                "freeze_record",
            }
            missing = expected_fields - set(review)
            if missing:
                error(f"claim {item_id}: missing review fields {sorted(missing)}")
            if review.get("mode") != "independent-review":
                error(f"claim {item_id}: reviewed_scoped currently requires independent-review")
            if review.get("disposition") != "ACCEPT":
                error(f"claim {item_id}: reviewed_scoped requires ACCEPT")
            if not HEX40.fullmatch(str(review.get("reviewed_revision", ""))):
                error(f"claim {item_id}: invalid reviewed revision")
            if not HEX64.fullmatch(str(review.get("candidate_aggregate_sha256", ""))):
                error(f"claim {item_id}: invalid candidate aggregate SHA-256")
            for field in ["review_record", "freeze_record"]:
                relative = review.get(field, "")
                path = ROOT / relative
                if not path.is_file():
                    error(f"claim {item_id}: missing {field} {relative}")
                else:
                    text = path.read_text(encoding="utf-8")
                    if review.get("reviewed_revision", "") not in text:
                        error(f"claim {item_id}: {field} does not bind reviewed revision")
            if review.get("disposition") not in (ROOT / review.get("review_record", "missing")).read_text(
                encoding="utf-8"
            ) if (ROOT / review.get("review_record", "missing")).is_file() else "":
                error(f"claim {item_id}: review record does not contain disposition")
        elif review is not None:
            error(f"claim {item_id}: review metadata is reserved for reviewed_scoped status")

    adjacency = {item["id"]: list(item.get("depends_on", [])) for item in items if item.get("id")}
    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(node: str, trail: list[str]) -> None:
        if node in visiting:
            cycle_start = trail.index(node) if node in trail else 0
            error("claim dependency cycle: " + " -> ".join(trail[cycle_start:] + [node]))
            return
        if node in visited:
            return
        visiting.add(node)
        for dependency in adjacency.get(node, []):
            visit(dependency, trail + [node])
        visiting.remove(node)
        visited.add(node)

    for item_id in adjacency:
        visit(item_id, [])

    # Scientific-boundary invariants for the integrated packets.
    if by_id.get("CLM-060", {}).get("status") != "reviewed_scoped":
        error("CLM-060: defect-at-most-four theorem must be reviewed_scoped")
    if "primitive positive weight" not in by_id.get("CLM-060", {}).get("statement", ""):
        error("CLM-060: reviewed theorem lost its positive-weight scope")
    if "does not cover defect at least 5" not in by_id.get("CLM-060", {}).get("note", ""):
        error("CLM-060: missing explicit defect-five nonclaim")
    if by_id.get("CLM-061", {}).get("status") != "open_bridge":
        error("CLM-061: stable-order existence must remain open_bridge")
    if "no stable order is constructed" not in by_id.get("CLM-013", {}).get("note", "").lower():
        error("CLM-013: conditional stable-order implication must state that existence is open")
    if by_id.get("CLM-057", {}).get("status") != "open_bridge":
        error("CLM-057: radial/logarithmic integration step must remain open_bridge")
    if "does not prove the actual Keller branch is radial" not in by_id.get("CLM-054", {}).get("note", ""):
        error("CLM-054: radial tangency criterion must not assert the Keller branch is radial")
    if by_id.get("CLM-059", {}).get("status") != "open_bridge":
        error("CLM-059: Keller-specific index-form unit theorem must remain open_bridge")
    for claim_id in ["CLM-062", "CLM-063", "CLM-064", "CLM-065", "CLM-066"]:
        if by_id.get(claim_id, {}).get("status") != "candidate_proved":
            error(f"{claim_id}: rank-three successor result must remain candidate_proved")
    if "universal coefficient/content ideal" not in by_id.get("CLM-059", {}).get("statement", ""):
        error("CLM-059: fixed-section bridge must retain the universal-content correction")
    for claim_id in ["CLM-067", "CLM-068", "CLM-069", "CLM-070", "CLM-071"]:
        if by_id.get(claim_id, {}).get("status") != "candidate_proved":
            error(f"{claim_id}: one-boundary successor result must remain candidate_proved")
    if by_id.get("CLM-072", {}).get("status") != "open_bridge":
        error("CLM-072: non-toric one-boundary compatibility system must remain open_bridge")
    if "no uniform bound" not in by_id.get("CLM-072", {}).get("note", ""):
        error("CLM-072: fixed-type reduction must retain its no-uniform-bound nonclaim")
    if "arXiv:2607.20210v1" not in by_id.get("CLM-070", {}).get("note", ""):
        error("CLM-070: terminal subclass exclusion must retain exact external dependency")

    return claim_ids, by_id


def validate_graph(graph: dict[str, Any]) -> tuple[set[str], dict[str, dict[str, Any]]]:
    if graph.get("schema_version") != 2:
        error("research/proof_graph.json: unsupported schema_version")
    nodes = graph.get("nodes", [])
    edges = graph.get("edges", [])
    node_ids_list = [node.get("id", "") for node in nodes]
    for item_id in sorted(duplicates(node_ids_list)):
        error(f"duplicate proof-graph node id: {item_id}")
    node_ids = set(node_ids_list)
    node_by_id = {node["id"]: node for node in nodes if node.get("id")}
    allowed_types = {"goal", "foundation", "reduction", "control", "branch", "leaf", "context", "terminal"}
    allowed_statuses = {"blocked", "active", "literature_bound", "open", "speculative", "reviewed", "disposed"}
    for node in nodes:
        item_id = node.get("id", "<missing>")
        if node.get("type") not in allowed_types:
            error(f"node {item_id}: unknown type {node.get('type')!r}")
        if node.get("status") not in allowed_statuses:
            error(f"node {item_id}: unknown status {node.get('status')!r}")
        artifact = node.get("artifact")
        if artifact and not (ROOT / "research" / artifact).is_file():
            error(f"node {item_id}: artifact missing: research/{artifact}")
        review_artifact = node.get("review_artifact")
        if review_artifact and not (ROOT / review_artifact).is_file():
            error(f"node {item_id}: missing review artifact {review_artifact}")
        if node.get("status") == "reviewed" and not review_artifact:
            error(f"node {item_id}: reviewed node lacks review_artifact")

    edge_keys: list[str] = []
    allowed_relations = {"requires", "supports", "sufficient-if-closed", "idea-input", "updates", "narrows-to"}
    for edge in edges:
        source = edge.get("from", "")
        target = edge.get("to", "")
        kind = edge.get("kind", "")
        edge_keys.append("\0".join([source, kind, target]))
        if source not in node_ids:
            error(f"edge: missing source node {source}")
        if target not in node_ids:
            error(f"edge: missing target node {target}")
        if kind not in allowed_relations:
            error(f"edge {source}->{target}: unknown relation {kind!r}")
    for key in sorted(duplicates(edge_keys)):
        source, kind, target = key.split("\0")
        error(f"duplicate graph edge: {source} -[{kind}]-> {target}")

    if node_by_id.get("ROOT-JC2", {}).get("status") != "blocked":
        error("ROOT-JC2 must remain blocked")
    if node_by_id.get("OPEN-STABLE-ORDER", {}).get("status") != "open":
        error("OPEN-STABLE-ORDER must remain open")
    if node_by_id.get("OPEN-BOUNDARY-POLE", {}).get("status") != "open":
        error("OPEN-BOUNDARY-POLE must remain open")
    if node_by_id.get("OPEN-KELLER-INDEX-UNIT", {}).get("status") != "open":
        error("OPEN-KELLER-INDEX-UNIT must remain open")
    if node_by_id.get("OPEN-UNRAMIFIED-INDEX", {}).get("status") != "disposed":
        error("OPEN-UNRAMIFIED-INDEX must retain disposed status")
    if node_by_id.get("OPEN-DEFECT-4", {}).get("status") != "reviewed":
        error("OPEN-DEFECT-4 must retain reviewed status")

    forbidden_targets = {"TERM-FINITE-ETALE", "TERM-DEGREE-ONE", "TERM-AUTOMORPHISM", "ROOT-JC2"}
    for edge in edges:
        if edge.get("from") == "OPEN-DEFECT-4" and edge.get("to") in forbidden_targets:
            error("OPEN-DEFECT-4 must not acquire a terminal or JC_2 edge")
    return node_ids, node_by_id


def validate_queue(
    queue: dict[str, Any], claim_ids: set[str], node_by_id: dict[str, dict[str, Any]]
) -> None:
    if queue.get("schema_version") != 2:
        error("research/work_queue.json: unsupported schema_version")
    leaves = queue.get("leaves", [])
    dispositions = queue.get("dispositions", [])
    all_items = leaves + dispositions

    for field, label in [("id", "leaf id"), ("graph_node", "graph node"), ("artifact", "artifact")]:
        values = [item.get(field, "") for item in all_items]
        for value in sorted(duplicates(values)):
            error(f"queue duplicate {label}: {value}")

    for leaf in leaves:
        item_id = leaf.get("id", "<missing>")
        if leaf.get("priority") not in {"P0", "P1", "P2", "P3"}:
            error(f"queue {item_id}: invalid priority {leaf.get('priority')!r}")
        if leaf.get("status") != "open":
            error(f"queue {item_id}: active queue contains non-open status")
        graph_node = node_by_id.get(leaf.get("graph_node", ""))
        if not graph_node:
            error(f"queue {item_id}: missing graph node {leaf.get('graph_node')}")
        else:
            if graph_node.get("type") != "leaf" or graph_node.get("status") != "open":
                error(f"queue {item_id}: graph node must be an open leaf")
            expected = f"research/{graph_node.get('artifact')}"
            if leaf.get("artifact") != expected:
                error(f"queue {item_id}: artifact does not match graph node")
        validate_queue_paths_and_claims(leaf, claim_ids, item_id)

    for item in dispositions:
        item_id = item.get("id", "<missing>")
        if item.get("status") not in {"disposed", "reviewed"}:
            error(f"queue disposition {item_id}: invalid status")
        graph_node = node_by_id.get(item.get("graph_node", ""))
        if not graph_node:
            error(f"queue disposition {item_id}: missing graph node")
        else:
            if graph_node.get("type") != "leaf" or graph_node.get("status") != item.get("status"):
                error(f"queue disposition {item_id}: queue/graph status mismatch")
            expected = f"research/{graph_node.get('artifact')}"
            if item.get("artifact") != expected:
                error(f"queue disposition {item_id}: artifact does not match graph node")
        if not item.get("disposition"):
            error(f"queue disposition {item_id}: missing disposition label")
        if item.get("review_artifact") and not (ROOT / item["review_artifact"]).is_file():
            error(f"queue disposition {item_id}: missing review artifact")
        if item.get("successor_graph_node") and item["successor_graph_node"] not in node_by_id:
            error(f"queue disposition {item_id}: missing successor graph node")
        validate_queue_paths_and_claims(item, claim_ids, item_id)

    graph_open = {
        node_id for node_id, node in node_by_id.items() if node.get("type") == "leaf" and node.get("status") == "open"
    }
    graph_dispositions = {
        node_id
        for node_id, node in node_by_id.items()
        if node.get("type") == "leaf" and node.get("status") in {"disposed", "reviewed"}
    }
    if graph_open != {item["graph_node"] for item in leaves}:
        error("active queue does not exactly match open proof-graph leaves")
    if graph_dispositions != {item["graph_node"] for item in dispositions}:
        error("queue dispositions do not exactly match disposed/reviewed proof-graph leaves")

    canonical_leaf_paths = {
        path.relative_to(ROOT).as_posix() for path in (ROOT / "research/leaf-packets").glob("L[0-9][0-9]-*.md")
    }
    queued_paths = {item["artifact"] for item in all_items}
    if canonical_leaf_paths != queued_paths:
        missing = canonical_leaf_paths - queued_paths
        extra = queued_paths - canonical_leaf_paths
        if missing:
            error("queue missing canonical leaf packets: " + ", ".join(sorted(missing)))
        if extra:
            error("queue references noncanonical leaf packets: " + ", ".join(sorted(extra)))


def validate_queue_paths_and_claims(item: dict[str, Any], claim_ids: set[str], item_id: str) -> None:
    for path_field in ["artifact", "track_artifact"]:
        value = item.get(path_field, "")
        if not (ROOT / value).is_file():
            error(f"queue {item_id}: missing {path_field} {value}")
    issue_number = item.get("issue_number")
    if not isinstance(issue_number, int) or issue_number <= 0:
        error(f"queue {item_id}: invalid issue_number {issue_number!r}")
    dependencies = item.get("claim_dependencies", [])
    if len(dependencies) != len(set(dependencies)):
        error(f"queue {item_id}: duplicate claim dependency")
    for dependency in dependencies:
        if dependency not in claim_ids:
            error(f"queue {item_id}: missing claim dependency {dependency}")


def validate_leaf_contracts() -> None:
    fixed_markers = [
        "## Load-bearing question",
        "## Forbidden shortcuts",
        "## Required artifacts",
        "## Stop rule",
        "## Handoff",
    ]
    for path in sorted((ROOT / "research/leaf-packets").glob("L[0-9][0-9]-*.md")):
        text = path.read_text(encoding="utf-8")
        for marker in fixed_markers:
            if marker not in text:
                error(f"{path.relative_to(ROOT)}: missing {marker}")
        if "## Accepted evidence" not in text and "## Candidate evidence" not in text:
            error(f"{path.relative_to(ROOT)}: missing accepted/candidate evidence section")


def validate_legacy(legacy: dict[str, Any], claim_ids: set[str]) -> None:
    if legacy.get("schema_version") != 1:
        error("research/legacy_claim_ledger.json: unsupported schema_version")
    vocabulary = set(legacy.get("legacy_status_vocabulary", []))
    items = legacy.get("claims", [])
    ids = [item.get("id", "") for item in items]
    for item_id in sorted(duplicates(ids)):
        error(f"duplicate legacy claim id: {item_id}")
    for item in items:
        item_id = item.get("id", "<missing>")
        if item.get("legacy_status") not in vocabulary:
            error(f"legacy claim {item_id}: unknown status")
        for link in item.get("canonical_links", []):
            if link.get("claim_id") not in claim_ids:
                error(f"legacy claim {item_id}: missing canonical claim {link.get('claim_id')}")
            if not link.get("relation"):
                error(f"legacy claim {item_id}: canonical link lacks relation")


def validate_archive(manifest: dict[str, Any]) -> None:
    if manifest.get("schema_version") != 2:
        error("archive/manifest.json: unsupported schema_version")
    if "issues/22" not in manifest.get("archive_completion_issue", ""):
        error("archive/manifest.json: archive_completion_issue must retain issue #22")

    export_by_id: dict[str, dict[str, Any]] = {}
    for export in manifest.get("exports", []):
        export_id = export.get("id", "<unknown>")
        if export_id in export_by_id:
            error(f"archive: duplicate export id {export_id}")
        export_by_id[export_id] = export
        storage_mode = export.get("storage_mode")
        if storage_mode == "metadata_only":
            if export.get("base64_chunk_paths"):
                error(f"archive {export_id}: metadata_only export declares reconstruction chunks")
            if export.get("verification_status") != "declared_not_reproducible_from_current_git_tree":
                error(f"archive {export_id}: inaccurate metadata_only verification_status")
            warning(f"archive {export_id} is metadata_only; declared source hashes are not reproducible")
            for partial_path in export.get("historical_partial_chunk_paths", []):
                if not (ROOT / partial_path).is_file():
                    warning(f"archive {export_id}: historical partial chunk missing: {partial_path}")
            continue
        if storage_mode != "embedded":
            error(f"archive {export_id}: unknown storage_mode {storage_mode!r}")
            continue
        chunk_paths = export.get("base64_chunk_paths", [])
        if not chunk_paths:
            error(f"archive {export_id}: embedded export has no chunk paths")
            continue
        missing = [path for path in chunk_paths if not (ROOT / path).is_file()]
        for path in missing:
            error(f"archive {export_id}: missing chunk {path}")
        if missing:
            continue
        try:
            encoded = "".join((ROOT / path).read_text(encoding="utf-8").strip() for path in chunk_paths)
            compressed = base64.b64decode(encoded, validate=True)
            if hashlib.sha256(compressed).hexdigest() != export.get("gzip_sha256"):
                error(f"archive {export_id}: gzip hash mismatch")
            if len(compressed) != export.get("gzip_bytes"):
                error(f"archive {export_id}: gzip byte count mismatch")
            raw = gzip.decompress(compressed)
            if hashlib.sha256(raw).hexdigest() != export.get("raw_sha256"):
                error(f"archive {export_id}: raw hash mismatch")
            if len(raw) != export.get("raw_bytes"):
                error(f"archive {export_id}: raw byte count mismatch")
        except Exception as exc:
            error(f"archive {export_id}: reconstruction error: {exc}")

    index = load_json("archive/conversations/index.json")
    if index.get("schema_version") != 1:
        error("archive/conversations/index.json: unsupported schema_version")
    note = index.get("note", "").lower()
    if "metadata_only" not in note:
        error("archive/conversations/index.json: note must state metadata_only")
    if "losslessly reconstructed" in note or "lossless reconstruction" in note:
        error("archive/conversations/index.json: falsely claims lossless reconstruction")
    index_items = {item.get("id"): item for item in index.get("conversations", [])}
    if set(index_items) != set(export_by_id):
        error("archive/conversations/index.json: export IDs do not match manifest")
    for export_id, export in export_by_id.items():
        item = index_items.get(export_id, {})
        for key in ["original_filename", "messages", "storage_mode"]:
            if item.get(key) != export.get(key):
                error(f"archive index {export_id}: {key} does not match manifest")
        topic_summary = item.get("topic_summary", "")
        if not (ROOT / topic_summary).is_file():
            error(f"archive index {export_id}: missing topic summary {topic_summary}")


def validate_generated_views() -> None:
    for relative_path, expected in render_views.expected_outputs().items():
        path = ROOT / relative_path
        expected_bytes = (expected.rstrip() + "\n").encode("utf-8")
        actual = path.read_bytes() if path.exists() else b""
        if actual != expected_bytes:
            error(f"generated view stale: {relative_path}; run scripts/render_views.py --write")


INLINE_LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)\n]+)\)")
REFERENCE_LINK_RE = re.compile(r"^\s*\[[^\]]+\]:\s*(\S+)", re.MULTILINE)
SCHEME_RE = re.compile(r"^[A-Za-z][A-Za-z0-9+.-]*:")


def normalize_link_target(raw_target: str) -> str | None:
    target = raw_target.strip()
    if target.startswith("<") and ">" in target:
        target = target[1 : target.index(">")]
    else:
        target = target.split()[0]
    target = target.strip("<>")
    if not target or target.startswith("#") or target.startswith("//"):
        return None
    if SCHEME_RE.match(target):
        return None
    split = urlsplit(target)
    path = unquote(split.path)
    return path or None


def validate_markdown_links() -> None:
    for markdown in sorted(ROOT.rglob("*.md")):
        text = markdown.read_text(encoding="utf-8")
        targets = [match.group(1) for match in INLINE_LINK_RE.finditer(text)]
        targets += [match.group(1) for match in REFERENCE_LINK_RE.finditer(text)]
        for raw_target in targets:
            target = normalize_link_target(raw_target)
            if target is None:
                continue
            candidate = ROOT / target.lstrip("/") if target.startswith("/") else markdown.parent / target
            try:
                resolved = candidate.resolve()
                resolved.relative_to(ROOT.resolve())
            except Exception:
                error(f"{markdown.relative_to(ROOT)}: internal link escapes repository: {raw_target}")
                continue
            if not resolved.exists():
                error(f"{markdown.relative_to(ROOT)}: broken internal link: {raw_target}")


def validate_operational_references() -> None:
    operational = [
        "README.md",
        "STATUS.md",
        "AGENTS.md",
        "AGENT_PROMPT.md",
        "CONTRIBUTING.md",
        "governance/SCIENTIFIC-WORKFLOW.md",
        "governance/PARALLEL-AGENT-POLICY.md",
        "governance/REPOSITORY-MAP.md",
        "research/PROGRAM.md",
        "research/WORK_QUEUE.md",
        "research/ISSUE_INDEX.md",
    ]
    forbidden = {
        "PR #15": "historical PR #15 presented in an operational surface",
        "PR #24": "historical PR #24 presented in an operational surface",
        "pull/15": "historical PR #15 link presented in an operational surface",
        "pull/24": "historical PR #24 link presented in an operational surface",
        "issue-1/": "historical issue-1 branch presented in an operational surface",
        "agent/bootstrap-proof-graph": "historical bootstrap branch presented in an operational surface",
        "maintenance/reconcile-rich-baseline": "historical reconciliation branch presented in an operational surface",
    }
    issue_one_url = re.compile(r"github\.com/snissn/planar-jacobian/issues/1(?:[)#?\s]|$)")
    for relative in operational:
        text = (ROOT / relative).read_text(encoding="utf-8")
        for token, message in forbidden.items():
            if token in text:
                error(f"{relative}: {message}")
        if issue_one_url.search(text):
            error(f"{relative}: closed issue #1 presented in an operational surface")
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    if "issues/2" not in readme:
        error("README.md: issue #2 must be the durable coordination surface")
    if "latest `main`" not in readme:
        error("README.md: navigation must start from latest main")


def validate_reconciliation_inventory() -> None:
    inventory = load_json("governance/reconciliation-inventory.json")
    if inventory.get("schema_version") != 2:
        error("governance/reconciliation-inventory.json: unsupported schema_version")
    if inventory.get("initial_main_sha") != "e542948a6d645569518437c6c0634a059415cfc4":
        error("reconciliation inventory: initial main SHA changed unexpectedly")
    policy = inventory.get("history_policy", {})
    required_true = [
        "single_parent_from_live_main",
        "shared_files_reconciled_manually",
    ]
    required_false = [
        "force_push",
        "published_history_rewritten",
        "unrelated_branch_history_imported",
    ]
    for key in required_true:
        if policy.get(key) is not True:
            error(f"reconciliation inventory: {key} must be true")
    for key in required_false:
        if policy.get(key) is not False:
            error(f"reconciliation inventory: {key} must be false")
    for source in inventory.get("source_revisions", []):
        if not source.get("role") or not HEX40.fullmatch(str(source.get("sha", ""))):
            error("reconciliation inventory: invalid source revision")
    for relative in inventory.get("owned_packet_roots", []):
        if not (ROOT / relative).exists():
            error(f"reconciliation inventory: missing owned packet root {relative}")
    for relative in inventory.get("shared_reconciliation_paths", []):
        if not (ROOT / relative).is_file():
            error(f"reconciliation inventory: missing shared path {relative}")
    nonclaims = " ".join(inventory.get("scientific_nonclaims", [])).lower()
    for phrase in ["defect five", "stable differential order", "not proved radial", "does not claim jc_2"]:
        if phrase not in nonclaims:
            error(f"reconciliation inventory: missing scientific nonclaim containing {phrase!r}")


def validate_integration_policy() -> None:
    policy = (ROOT / "governance/SCIENTIFIC-WORKFLOW.md").read_text(encoding="utf-8")
    required_phrases = [
        "latest `main`",
        "unique issue-specific artifact path",
        "issue-local claim labels",
        "Global claim IDs",
        "final synchronization",
        "re-resolve `main`",
        "Unrelated branch histories",
        "speculative work",
        "small, non-draft",
        "transport and preservation",
        "Exact-byte manifests",
        "local-adversarial-review",
        "Material changes",
        "Editorial-only changes",
    ]
    for phrase in required_phrases:
        if phrase not in policy:
            error(f"governance/SCIENTIFIC-WORKFLOW.md: missing integration policy phrase {phrase!r}")


def main() -> int:
    validate_all_json()
    claims = load_json("research/claim_ledger.json")
    graph = load_json("research/proof_graph.json")
    queue = load_json("research/work_queue.json")
    legacy = load_json("research/legacy_claim_ledger.json")
    manifest = load_json("archive/manifest.json")

    claim_ids, _ = validate_claims(claims)
    _, node_by_id = validate_graph(graph)
    validate_queue(queue, claim_ids, node_by_id)
    validate_leaf_contracts()
    validate_legacy(legacy, claim_ids)
    validate_archive(manifest)
    validate_generated_views()
    validate_markdown_links()
    validate_operational_references()
    validate_reconciliation_inventory()
    validate_integration_policy()

    print(f"claims: {len(claims.get('claims', []))}")
    print(f"reviewed-scoped claims: {sum(1 for item in claims.get('claims', []) if item.get('status') == 'reviewed_scoped')}")
    print(f"graph nodes: {len(graph.get('nodes', []))}")
    print(f"graph edges: {len(graph.get('edges', []))}")
    print(f"open queue leaves: {len(queue.get('leaves', []))}")
    print(f"recorded leaf dispositions: {len(queue.get('dispositions', []))}")
    print(f"errors: {len(ERRORS)}")
    print(f"warnings: {len(WARNINGS)}")
    for item in ERRORS:
        print("ERROR:", item)
    for item in WARNINGS:
        print("WARNING:", item)
    if ERRORS:
        return 1
    print("repository structure: PASS")
    print("prose/JSON generated-view consistency: PASS")
    print("proof-graph dependency and artifact closure: PASS")
    print("internal Markdown links: PASS")
    print("mathematical truth: NOT EVALUATED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
