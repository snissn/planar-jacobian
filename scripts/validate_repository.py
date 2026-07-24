#!/usr/bin/env python3
from pathlib import Path
import base64
import gzip
import hashlib
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
errors = []
warnings = []


def load(path):
    try:
        return json.loads((ROOT / path).read_text())
    except Exception as exc:
        errors.append(f"{path}: {exc}")
        return {}


claims = load("research/claim_ledger.json")
graph = load("research/proof_graph.json")
manifest = load("archive/manifest.json")

claim_ids = {claim["id"] for claim in claims.get("claims", [])}
for claim in claims.get("claims", []):
    for dependency in claim.get("depends_on", []):
        if dependency not in claim_ids:
            errors.append(f"claim {claim['id']} missing dependency {dependency}")

node_ids = {node["id"] for node in graph.get("nodes", [])}
for edge in graph.get("edges", []):
    if edge["from"] not in node_ids:
        errors.append(f"edge missing from {edge['from']}")
    if edge["to"] not in node_ids:
        errors.append(f"edge missing to {edge['to']}")

for node in graph.get("nodes", []):
    artifact = node.get("artifact")
    if artifact:
        path = (ROOT / "research" / artifact).resolve()
        if not path.exists():
            errors.append(f"node {node['id']} artifact missing: {artifact}")

for export in manifest.get("exports", []):
    export_id = export.get("id", "<unknown>")
    storage_mode = export.get("storage_mode", "embedded")

    if storage_mode == "metadata_only":
        if not manifest.get("archive_completion_issue"):
            errors.append(
                f"archive {export_id} is metadata-only without an archive_completion_issue"
            )
        warnings.append(
            f"archive {export_id} is metadata-only; raw/gzip hashes are recorded "
            "but not reproducible from the current Git tree"
        )
        for partial_path in export.get("historical_partial_chunk_paths", []):
            if not (ROOT / partial_path).exists():
                warnings.append(
                    f"archive {export_id} historical partial chunk missing: {partial_path}"
                )
        continue

    if storage_mode != "embedded":
        errors.append(f"archive {export_id} has unknown storage_mode {storage_mode!r}")
        continue

    chunk_paths = export.get("base64_chunk_paths", [])
    if not chunk_paths:
        errors.append(f"archive {export_id} is embedded but has no chunk paths")
        continue

    missing = [path for path in chunk_paths if not (ROOT / path).exists()]
    if missing:
        for path in missing:
            errors.append(f"archive {export_id} chunk missing: {path}")
        continue

    try:
        encoded = "".join((ROOT / path).read_text().strip() for path in chunk_paths)
        compressed = base64.b64decode(encoded, validate=True)
        if hashlib.sha256(compressed).hexdigest() != export["gzip_sha256"]:
            errors.append(f"gzip hash mismatch: {export_id}")
        raw = gzip.decompress(compressed)
        if hashlib.sha256(raw).hexdigest() != export["raw_sha256"]:
            errors.append(f"raw hash mismatch: {export_id}")
        if len(raw) != export.get("raw_bytes"):
            errors.append(f"raw byte count mismatch: {export_id}")
    except Exception as exc:
        errors.append(f"archive error {export_id}: {exc}")

for path in (ROOT / "research/leaf-packets").glob("*.md"):
    text = path.read_text()
    for marker in [
        "## Load-bearing question",
        "## Accepted evidence",
        "## Forbidden shortcuts",
        "## Required artifacts",
        "## Stop rule",
        "## Handoff",
    ]:
        if marker not in text:
            errors.append(f"{path.relative_to(ROOT)} missing {marker}")

print(f"claims: {len(claim_ids)}")
print(f"graph nodes: {len(node_ids)}")
print(f"graph edges: {len(graph.get('edges', []))}")
print(f"errors: {len(errors)}")
print(f"warnings: {len(warnings)}")
for error in errors:
    print("ERROR:", error)
for warning in warnings:
    print("WARNING:", warning)
if errors:
    sys.exit(1)
print("repository structure: PASS")
print("mathematical truth: NOT EVALUATED")
