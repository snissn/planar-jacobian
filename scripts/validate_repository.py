#!/usr/bin/env python3
"""Validate repository structure, machine ledgers, provenance, and Markdown paths.

This validator intentionally does not evaluate mathematical truth or review quality.
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


def validate_claims(claims: dict[str, Any]) -> set[str]:
    items = claims.get("claims", [])
    vocabulary = claims.get("status_vocabulary", [])
    if claims.get("schema_version") != 1:
        error("research/claim_ledger.json: unsupported schema_version")
    if duplicates(vocabulary):
        error("research/claim_ledger.json: duplicate status vocabulary entries")

    ids = [item.get("id", "") for item in items]
    for item_id in sorted(duplicates(ids)):
        error(f"duplicate claim id: {item_id}")
    claim_ids = set(ids)

    for item in items:
        item_id = item.get("id", "<missing>")
        for field in ["id", "status", "track", "statement", "depends_on", "note"]:
            if field not in item:
                error(f"claim {item_id}: missing field {field}")
        if item.get("status") not in vocabulary:
            error(f"claim {item_id}: unknown status {item.get('status')!r}")
        dependencies = item.get("depends_on", [])
        if len(dependencies) != len(set(dependencies)):
            error(f"claim {item_id}: duplicate dependency")
        if item_id in dependencies:
            error(f"claim {item_id}: self dependency")
        for dependency in dependencies:
            if dependency not in claim_ids:
                error(f"claim {item_id}: missing dependency {dependency}")

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
    return claim_ids


def validate_graph(graph: dict[str, Any]) -> tuple[set[str], dict[str, dict[str, Any]]]:
    if graph.get("schema_version") != 1:
        error("research/proof_graph.json: unsupported schema_version")
    nodes = graph.get("nodes", [])
    edges = graph.get("edges", [])
    node_ids_list = [node.get("id", "") for node in nodes]
    for item_id in sorted(duplicates(node_ids_list)):
        error(f"duplicate proof-graph node id: {item_id}")
    node_ids = set(node_ids_list)
    node_by_id = {node["id"]: node for node in nodes if node.get("id")}
    allowed_types = {"goal", "foundation", "reduction", "control", "branch", "leaf", "context", "terminal"}
    allowed_statuses = {"blocked", "active", "literature_bound", "open", "speculative"}
    for node in nodes:
        item_id = node.get("id", "<missing>")
        if node.get("type") not in allowed_types:
            error(f"node {item_id}: unknown type {node.get('type')!r}")
        if node.get("status") not in allowed_statuses:
            error(f"node {item_id}: unknown status {node.get('status')!r}")
        artifact = node.get("artifact")
        if artifact:
            artifact_path = ROOT / "research" / artifact
            if not artifact_path.is_file():
                error(f"node {item_id}: artifact missing: research/{artifact}")

    edge_keys: list[tuple[str, str, str]] = []
    allowed_relations = {"requires", "supports", "sufficient-if-closed", "idea-input", "updates"}
    for edge in edges:
        source = edge.get("from", "")
        target = edge.get("to", "")
        kind = edge.get("kind", "")
        edge_keys.append((source, kind, target))
        if source not in node_ids:
            error(f"edge: missing source node {source}")
        if target not in node_ids:
            error(f"edge: missing target node {target}")
        if kind not in allowed_relations:
            error(f"edge {source}->{target}: unknown relation {kind!r}")
    for edge_key in sorted(duplicates(["\0".join(key) for key in edge_keys])):
        source, kind, target = edge_key.split("\0")
        error(f"duplicate graph edge: {source} -[{kind}]-> {target}")
    return node_ids, node_by_id


def validate_queue(
    queue: dict[str, Any], claim_ids: set[str], node_by_id: dict[str, dict[str, Any]]
) -> None:
    if queue.get("schema_version") != 1:
        error("research/work_queue.json: unsupported schema_version")
    leaves = queue.get("leaves", [])
    leaf_ids = [leaf.get("id", "") for leaf in leaves]
    graph_nodes = [leaf.get("graph_node", "") for leaf in leaves]
    artifacts = [leaf.get("artifact", "") for leaf in leaves]
    for item_id in sorted(duplicates(leaf_ids)):
        error(f"duplicate queue leaf id: {item_id}")
    for item_id in sorted(duplicates(graph_nodes)):
        error(f"queue graph node appears more than once: {item_id}")
    for artifact in sorted(duplicates(artifacts)):
        error(f"queue artifact appears more than once: {artifact}")

    for leaf in leaves:
        item_id = leaf.get("id", "<missing>")
        if leaf.get("priority") not in {"P0", "P1", "P2", "P3"}:
            error(f"queue {item_id}: invalid priority {leaf.get('priority')!r}")
        if leaf.get("status") != "open":
            error(f"queue {item_id}: only open canonical leaves belong in the active queue")
        graph_node = node_by_id.get(leaf.get("graph_node", ""))
        if not graph_node:
            error(f"queue {item_id}: missing graph node {leaf.get('graph_node')}")
        else:
            if graph_node.get("type") != "leaf":
                error(f"queue {item_id}: graph node is not a leaf")
            if graph_node.get("status") != leaf.get("status"):
                error(f"queue {item_id}: queue/graph status mismatch")
            expected_artifact = f"research/{graph_node.get('artifact')}"
            if expected_artifact != leaf.get("artifact"):
                error(
                    f"queue {item_id}: artifact {leaf.get('artifact')} does not match graph artifact {expected_artifact}"
                )
        for path_field in ["artifact", "track_artifact"]:
            value = leaf.get(path_field, "")
            if not (ROOT / value).is_file():
                error(f"queue {item_id}: missing {path_field} {value}")
        issue_number = leaf.get("issue_number")
        if not isinstance(issue_number, int) or issue_number <= 0:
            error(f"queue {item_id}: invalid issue_number {issue_number!r}")
        for dependency in leaf.get("claim_dependencies", []):
            if dependency not in claim_ids:
                error(f"queue {item_id}: missing claim dependency {dependency}")

    graph_leaf_nodes = {
        node_id for node_id, node in node_by_id.items() if node.get("type") == "leaf" and node.get("status") == "open"
    }
    if graph_leaf_nodes != set(graph_nodes):
        missing = graph_leaf_nodes - set(graph_nodes)
        extra = set(graph_nodes) - graph_leaf_nodes
        if missing:
            error("queue missing open graph leaves: " + ", ".join(sorted(missing)))
        if extra:
            error("queue contains non-open graph leaves: " + ", ".join(sorted(extra)))

    canonical_leaf_paths = {
        path.relative_to(ROOT).as_posix()
        for path in (ROOT / "research/leaf-packets").glob("L[0-9][0-9]-*.md")
    }
    if canonical_leaf_paths != set(artifacts):
        missing = canonical_leaf_paths - set(artifacts)
        extra = set(artifacts) - canonical_leaf_paths
        if missing:
            error("queue missing canonical leaf packets: " + ", ".join(sorted(missing)))
        if extra:
            error("queue references noncanonical leaf packets: " + ", ".join(sorted(extra)))


def validate_leaf_contracts() -> None:
    markers = [
        "## Load-bearing question",
        "## Accepted evidence",
        "## Forbidden shortcuts",
        "## Required artifacts",
        "## Stop rule",
        "## Handoff",
    ]
    for path in sorted((ROOT / "research/leaf-packets").glob("L[0-9][0-9]-*.md")):
        text = path.read_text(encoding="utf-8")
        for marker in markers:
            if marker not in text:
                error(f"{path.relative_to(ROOT)}: missing {marker}")


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
            error(f"legacy claim {item_id}: unknown status {item.get('legacy_status')!r}")
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
                error(f"archive {export_id}: metadata_only export must not declare reconstructing chunks")
            if export.get("verification_status") != "declared_not_reproducible_from_current_git_tree":
                error(f"archive {export_id}: inaccurate metadata_only verification_status")
            warning(
                f"archive {export_id} is metadata_only; declared raw/gzip hashes are not reproducible from this Git tree"
            )
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
        if missing:
            for path in missing:
                error(f"archive {export_id}: missing chunk {path}")
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
    note = index.get("note", "").lower()
    if "metadata_only" not in note:
        error("archive/conversations/index.json: note must state metadata_only")
    if "losslessly reconstructed" in note or "lossless reconstruction" in note:
        error("archive/conversations/index.json: falsely claims lossless reconstruction")
    index_items = {item.get("id"): item for item in index.get("conversations", [])}
    if set(index_items) != set(export_by_id):
        error("archive/conversations/index.json: export IDs do not match archive/manifest.json")
    for export_id, export in export_by_id.items():
        item = index_items.get(export_id, {})
        for key in ["original_filename", "messages"]:
            if item.get(key) != export.get(key):
                error(f"archive index {export_id}: {key} does not match manifest")
        if item.get("storage_mode") != export.get("storage_mode"):
            error(f"archive index {export_id}: storage_mode does not match manifest")


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
    canonical_navigation = [
        "README.md",
        "STATUS.md",
        "AGENTS.md",
        "AGENT_PROMPT.md",
        "research/PROGRAM.md",
        "research/WORK_QUEUE.md",
        "research/ISSUE_INDEX.md",
    ]
    issue_one_url = re.compile(
        r"github\.com/snissn/planar-jacobian/issues/1(?:[)#?\s]|$)"
    )
    for relative_path in canonical_navigation:
        text = (ROOT / relative_path).read_text(encoding="utf-8")
        if issue_one_url.search(text):
            error(f"{relative_path}: closed issue #1 remains linked as an operational surface")
        if "issue-1/" in text:
            error(f"{relative_path}: superseded issue-1 branch remains an operational surface")


def validate_reconciliation_inventory() -> None:
    inventory = load_json("governance/reconciliation-inventory.json")
    if inventory.get("schema_version") != 1:
        error("governance/reconciliation-inventory.json: unsupported schema_version")
    semantic = inventory.get("pinned_rich_semantic_hashes", {})
    fields = semantic.get("claim_projection_fields", [])
    claims = load_json("research/claim_ledger.json").get("claims", [])
    try:
        projection = [{field: claim[field] for field in fields} for claim in claims]
        payload = json.dumps(
            projection, sort_keys=True, separators=(",", ":"), ensure_ascii=False
        ).encode("utf-8")
        actual_projection = hashlib.sha256(payload).hexdigest()
        if actual_projection != semantic.get("claim_projection_sha256"):
            error(
                "reconciliation inventory: canonical claim statements/statuses/dependencies "
                "differ from the pinned rich baseline"
            )
    except Exception as exc:
        error(f"reconciliation inventory: cannot compute claim projection: {exc}")

    for relative_path, key in [
        ("research/proof_graph.json", "proof_graph_file_sha256"),
        ("archive/manifest.json", "archive_manifest_file_sha256"),
    ]:
        path = ROOT / relative_path
        actual = hashlib.sha256(path.read_bytes()).hexdigest() if path.is_file() else "<missing>"
        if actual != semantic.get(key):
            error(
                f"reconciliation inventory: {relative_path} differs from pinned rich-baseline hash "
                f"{semantic.get(key)}; observed {actual}"
            )

    for relative_path, expected_hash in inventory.get("retained_current_main_file_hashes", {}).items():
        path = ROOT / relative_path
        actual = hashlib.sha256(path.read_bytes()).hexdigest() if path.is_file() else "<missing>"
        if actual != expected_hash:
            error(
                f"reconciliation inventory: retained current-main file {relative_path} "
                f"changed from {expected_hash}; observed {actual}"
            )


def main() -> int:
    validate_all_json()
    claims = load_json("research/claim_ledger.json")
    graph = load_json("research/proof_graph.json")
    queue = load_json("research/work_queue.json")
    legacy = load_json("research/legacy_claim_ledger.json")
    manifest = load_json("archive/manifest.json")

    claim_ids = validate_claims(claims)
    _, node_by_id = validate_graph(graph)
    validate_queue(queue, claim_ids, node_by_id)
    validate_leaf_contracts()
    validate_legacy(legacy, claim_ids)
    validate_archive(manifest)
    validate_generated_views()
    validate_markdown_links()
    validate_operational_references()
    validate_reconciliation_inventory()

    print(f"claims: {len(claims.get('claims', []))}")
    print(f"graph nodes: {len(graph.get('nodes', []))}")
    print(f"graph edges: {len(graph.get('edges', []))}")
    print(f"queue leaves: {len(queue.get('leaves', []))}")
    print(f"errors: {len(ERRORS)}")
    print(f"warnings: {len(WARNINGS)}")
    for item in ERRORS:
        print("ERROR:", item)
    for item in WARNINGS:
        print("WARNING:", item)
    if ERRORS:
        return 1
    print("repository structure: PASS")
    print("mathematical truth: NOT EVALUATED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
