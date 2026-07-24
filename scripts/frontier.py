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
    leaf_counts = Counter(item["priority"] for item in queue["leaves"] if item["status"] == "open")
    storage_counts = Counter(item.get("storage_mode", "unknown") for item in manifest["exports"])

    print("PLANAR JACOBIAN RESEARCH FRONTIER")
    print(f"claims={len(claims['claims'])} ({counts_text(claim_counts)})")
    print(f"graph_nodes={len(graph['nodes'])} graph_edges={len(graph['edges'])} ({counts_text(node_counts)})")
    print(f"open_leaves={sum(leaf_counts.values())} ({counts_text(leaf_counts)})")
    print(f"archive_exports={len(manifest['exports'])} ({counts_text(storage_counts)})")
    print("root_goal=ROOT-JC2:blocked")
    print()

    for priority in ["P0", "P1", "P2", "P3"]:
        leaves = [
            item
            for item in queue["leaves"]
            if item["status"] == "open" and item["priority"] == priority
        ]
        if not leaves:
            continue
        print(priority)
        for item in leaves:
            dependencies = ",".join(item["claim_dependencies"])
            print(
                f"  {item['id']} {item['graph_node']} issue=#{item['issue_number']} "
                f"claims={dependencies} artifact={item['artifact']}"
            )
    print()
    print("structural_validation_is_not_mathematical_review=true")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
