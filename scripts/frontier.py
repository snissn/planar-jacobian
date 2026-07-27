#!/usr/bin/env python3
"""Render the current proof frontier from machine-readable repository data."""
from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load(path: str):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def counts_text(counter: Counter[str]) -> str:
    return ", ".join(f"{key}={value}" for key, value in sorted(counter.items()))


def main() -> int:
    claims = load("research/claim_ledger.json")
    graph = load("research/proof_graph.json")
    queue = load("research/work_queue.json")
    manifest = load("archive/manifest.json")

    claim_counts = Counter(item["status"] for item in claims["claims"])
    node_counts = Counter(item["status"] for item in graph["nodes"])
    leaf_counts = Counter(item["priority"] for item in queue["leaves"])
    disposition_counts = Counter(item["status"] for item in queue.get("dispositions", []))
    storage_counts = Counter(item.get("storage_mode", "unknown") for item in manifest["exports"])
    claim_by_id = {item["id"]: item for item in claims["claims"]}
    defect_five_reviewed = claim_by_id.get("CLM-073", {}).get("status") == "reviewed_scoped"

    print("PLANAR JACOBIAN RESEARCH FRONTIER")
    print(f"claims={len(claims['claims'])} ({counts_text(claim_counts)})")
    print(f"graph_nodes={len(graph['nodes'])} graph_edges={len(graph['edges'])} ({counts_text(node_counts)})")
    print(f"open_leaves={len(queue['leaves'])} ({counts_text(leaf_counts)})")
    print(f"leaf_dispositions={len(queue.get('dispositions', []))} ({counts_text(disposition_counts)})")
    print(f"archive_exports={len(manifest['exports'])} ({counts_text(storage_counts)})")
    print("root_goal=ROOT-JC2:blocked")
    print("merge_is_scientific_acceptance=false")
    print()

    for priority in ["P0", "P1", "P2", "P3"]:
        leaves = [item for item in queue["leaves"] if item["priority"] == priority]
        if not leaves:
            continue
        print(priority)
        for item in leaves:
            dependencies = ",".join(item["claim_dependencies"])
            print(
                f"  {item['id']} {item['graph_node']} issue=#{item['issue_number']} "
                f"claims={dependencies} artifact={item['artifact']}"
            )

    if queue.get("dispositions"):
        print()
        print("DISPOSITIONS")
        for item in queue["dispositions"]:
            extra = item.get("successor_graph_node") or item.get("review_artifact") or "none"
            print(
                f"  {item['id']} {item['graph_node']} status={item['status']} "
                f"disposition={item['disposition']} next={extra}"
            )

    print()
    print("reviewed_defect_at_most_four_scope=primitive_positive_weight_only")
    print(f"defect_five_covered={str(defect_five_reviewed).lower()}")
    if defect_five_reviewed:
        print("reviewed_defect_five_scope=fixed_primitive_positive_weight_actual_defect_five_only")
    print("qualifying_weight_existence_proved=false")
    print("structural_validation_is_not_mathematical_review=true")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
