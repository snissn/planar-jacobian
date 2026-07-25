#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def load(path: str):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def save(path: str, value) -> None:
    (ROOT / path).write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


claim_path = "research/claim_ledger.json"
claims = load(claim_path)
ids = [item["id"] for item in claims["claims"]]
if "CLM-073" not in ids:
    assert ids[-1] == "CLM-072", ids[-5:]
    claims["claims"].append(
        {
            "id": "CLM-073",
            "status": "candidate_proved",
            "track": "filtered-equivariance",
            "statement": "For any primitive positive weight w, a planar Keller pair with grading defect kappa_w=5 admits a filtration-compatible polynomial source or target automorphism that strictly lowers the actual integer defect to at most four; hence it is a polynomial automorphism by the reviewed defect-at-most-four theorem.",
            "depends_on": ["CLM-047", "CLM-048", "CLM-049", "CLM-051", "CLM-060"],
            "note": "Issue #29 defect-five packet. A separate local-adversarial-review returned ACCEPT for candidate 2eeb36d232366d124b5a66774b29769ec1eba43d, but this is not independent review; the claim remains mutable candidate_proved. It does not prove that every Keller pair admits a qualifying primitive positive weight, does not treat defect six, and does not establish JC_2.",
        }
    )
save(claim_path, claims)

graph_path = "research/proof_graph.json"
graph = load(graph_path)
if not any(node["id"] == "OPEN-DEFECT-5" for node in graph["nodes"]):
    graph["nodes"].append(
        {
            "id": "OPEN-DEFECT-5",
            "title": "Fixed-weight defect-five closure at candidate scope",
            "type": "leaf",
            "status": "disposed",
            "artifact": "leaf-packets/L15-defect-5-staircase.md",
            "note": "Issue #29 is disposed at candidate_proved scope after local-adversarial-review ACCEPT. Independent scientific promotion is not conferred; no qualifying-weight existence, defect-six, or JC_2 inference is licensed.",
        }
    )
for edge in [
    {"from": "BR-FILTERED-EQUIVARIANCE", "to": "OPEN-DEFECT-5", "kind": "requires"},
    {"from": "OPEN-DEFECT-4", "to": "OPEN-DEFECT-5", "kind": "supports"},
    {"from": "OPEN-DEFECT-5", "to": "OPEN-GRADED-REDUCTION", "kind": "supports"},
]:
    if edge not in graph["edges"]:
        graph["edges"].append(edge)
save(graph_path, graph)

queue_path = "research/work_queue.json"
queue = load(queue_path)
if not any(item["id"] == "L15" for item in queue["leaves"] + queue["dispositions"]):
    queue["dispositions"].append(
        {
            "id": "L15",
            "graph_node": "OPEN-DEFECT-5",
            "title": "Fixed-Weight Defect-Five Closure",
            "status": "disposed",
            "disposition": "CANDIDATE_PROVED_LOCAL_REVIEW",
            "artifact": "research/leaf-packets/L15-defect-5-staircase.md",
            "track_artifact": "research/tracks/m-filtered-equivariance.md",
            "issue_number": 29,
            "claim_dependencies": ["CLM-047", "CLM-048", "CLM-049", "CLM-051", "CLM-060", "CLM-073"],
            "review_artifact": "research/issues/defect-5-rees/REVIEW.md",
            "note": "Every fixed-weight defect-five case reduces or contradicts the full staircase at candidate scope. The review is local-adversarial, not independent; qualifying-weight existence, defect six, and JC_2 remain unproved.",
        }
    )
save(queue_path, queue)

leaf = ROOT / "research/leaf-packets/L15-defect-5-staircase.md"
leaf.write_text(
    """# L15 — Fixed-Weight Defect-Five Candidate Disposition

> **Issue:** [#29](https://github.com/snissn/planar-jacobian/issues/29)  
> **Issue packet:** [`research/issues/defect-5-rees/`](../issues/defect-5-rees/)  
> **Canonical claim:** `CLM-073` (`candidate_proved`)  
> **Review mode:** `local-adversarial-review`; not independent acceptance

## Load-bearing question

For a planar Keller pair and a fixed primitive positive weight with actual grading defect five, must a filtration-compatible source or target automorphism lower the actual defect to at most four, or must the complete staircase be inconsistent?

## Forbidden shortcuts

- Do not infer that every Keller pair admits a primitive positive weight of defect at most five.
- Do not describe the local adversarial review as independent.
- Do not omit zero layers, simultaneous resonances, source-weight reversal, or target-component reversal.
- Do not extend this packet to defect six or attach a terminal `JC_2` edge.

## Required artifacts

- the exact issue-owned derivation, transformation catalogue, and exhaustive case table;
- a checker built from the defect-five definitions;
- a separate local adversarial checker and pinned review record;
- an explicit candidate disposition and scientific nonclaims.

## Candidate evidence

The packet proves at constructing-agent scope that every endpoint is invertible and every interior system either admits complete-top strict descent to defect at most four or contradicts the full stairs. Exact bounded support generation, saturated Groebner eliminations, mutation controls, and a separate local adversarial pass found no survivor. These checks are evidence, not independent theorem authority.

## Stop rule

This leaf is disposed when the complete candidate packet is integrated as `CLM-073`, the local review remains correctly labeled, all repository checks pass, and issue #29 records the exact candidate disposition. Independent promotion, if later requested, requires a new pinned independent review.

## Handoff

The next filtered-equivariance task is not defect six. It is either independent review of `CLM-073` or a separate theorem producing a qualifying primitive positive weight. Preserve the nonclaims about qualifying-weight existence, arbitrary termination, and `JC_2`.
""",
    encoding="utf-8",
)

track_path = ROOT / "research/tracks/m-filtered-equivariance.md"
track = track_path.read_text(encoding="utf-8")
header_anchor = "> **Scientific inference:** primitive positive weight and `kappa_w<=4` imply automorphism; no broader inference\n"
header_line = "> **Defect-five candidate:** issue [#29](https://github.com/snissn/planar-jacobian/issues/29), `CLM-073`; local-adversarial-review only  \n"
if header_line not in track:
    assert header_anchor in track
    track = track.replace(header_anchor, header_anchor + header_line, 1)
section = """## 9. Defect five candidate disposition

Issue #29 banks the fixed-weight defect-five theorem in [`../issues/defect-5-rees/README.md`](../issues/defect-5-rees/README.md) as `CLM-073` with status `candidate_proved`. The exact candidate `2eeb36d232366d124b5a66774b29769ec1eba43d` received a separate local-adversarial-review `ACCEPT`, not independent acceptance.

Every resonant endpoint is invertible; every interior system either admits complete-top strict descent to `kappa_w<=4` or contradicts the complete staircase. The coupled transverse chains in the standard-weight interior charts are the first genuinely new defect-five correction and are not imported from the defect-four middle-Wronskian row.

The task leaf [`L15-defect-5-staircase.md`](../leaf-packets/L15-defect-5-staircase.md) is disposed at candidate scope. Independent promotion or a theorem producing a qualifying weight would be a separate task. No defect-six, arbitrary-termination, qualifying-weight-existence, or `JC_2` claim is introduced.

"""
if "## 9. Defect five candidate disposition" not in track:
    assert "## Exit" in track
    track = track.replace("## Exit", section + "## Exit", 1)
old_exit = "Defect `5`, a theorem producing a qualifying weight, and `JC_2` remain outside this track's reviewed scope."
new_exit = "Defect `5` is banked only as mutable candidate `CLM-073`. Independent promotion, a qualifying-weight theorem, defect six, and `JC_2` remain outside this track's reviewed scope."
if old_exit in track:
    track = track.replace(old_exit, new_exit, 1)
track_path.write_text(track, encoding="utf-8")

render_path = ROOT / "scripts/render_views.py"
render = render_path.read_text(encoding="utf-8")
old_nonclaim = '        "- **Explicit nonclaims:** no defect-five theorem, no theorem producing a qualifying weight for every Keller pair, and no proof of `JC_2`.",\n'
new_nonclaim = '        "- **Explicit nonclaims:** no independently reviewed defect-five theorem, no theorem producing a qualifying weight for every Keller pair, no defect-six result, and no proof of `JC_2`.",\n'
if old_nonclaim in render:
    render = render.replace(old_nonclaim, new_nonclaim, 1)
issue17 = '        "- **Issue #17:** the exact positive-weight defect-at-most-four theorem is reviewed only at the pinned revision. It creates no terminal edge to `JC_2`.",\n'
issue29 = '        "- **Issue #29:** fixed primitive positive weight and actual defect five is banked as `CLM-073` at mutable `candidate_proved` scope after local-adversarial review. No independent promotion, qualifying-weight, defect-six, or `JC_2` claim is introduced.",\n'
if issue29 not in render:
    assert issue17 in render
    render = render.replace(issue17, issue17 + issue29, 1)
render_path.write_text(render, encoding="utf-8")

legacy_path = ROOT / "scripts/validate_repository_legacy.py"
legacy = legacy_path.read_text(encoding="utf-8")
claim_anchor = '    if "arXiv:2607.20210v1" not in by_id.get("CLM-070", {}).get("note", ""):\n        error("CLM-070: terminal subclass exclusion must retain exact external dependency")\n'
claim_checks = '    if by_id.get("CLM-073", {}).get("status") != "candidate_proved":\n        error("CLM-073: fixed-weight defect-five result must remain candidate_proved")\n    if "does not prove that every Keller pair admits" not in by_id.get("CLM-073", {}).get("note", ""):\n        error("CLM-073: qualifying-weight nonclaim is missing")\n    if "does not treat defect six" not in by_id.get("CLM-073", {}).get("note", ""):\n        error("CLM-073: defect-six nonclaim is missing")\n'
if claim_checks not in legacy:
    assert claim_anchor in legacy
    legacy = legacy.replace(claim_anchor, claim_anchor + claim_checks, 1)
graph_anchor = '    if node_by_id.get("OPEN-DEFECT-4", {}).get("status") != "reviewed":\n        error("OPEN-DEFECT-4 must retain reviewed status")\n'
graph_check = '    if node_by_id.get("OPEN-DEFECT-5", {}).get("status") != "disposed":\n        error("OPEN-DEFECT-5 must retain candidate-scope disposed status")\n'
if graph_check not in legacy:
    assert graph_anchor in legacy
    legacy = legacy.replace(graph_anchor, graph_anchor + graph_check, 1)
edge_anchor = '        if edge.get("from") == "OPEN-DEFECT-4" and edge.get("to") in forbidden_targets:\n            error("OPEN-DEFECT-4 must not acquire a terminal or JC_2 edge")\n'
edge_check = '        if edge.get("from") == "OPEN-DEFECT-5" and edge.get("to") in forbidden_targets:\n            error("OPEN-DEFECT-5 must not acquire a terminal or JC_2 edge")\n'
if edge_check not in legacy:
    assert edge_anchor in legacy
    legacy = legacy.replace(edge_anchor, edge_anchor + edge_check, 1)
legacy_path.write_text(legacy, encoding="utf-8")

manifest = {
    "schema_version": 1,
    "issue_number": 29,
    "leaf_id": "L15",
    "role": "integration-maintainer",
    "owned_paths": [
        "research/issues/defect-5-rees/",
        "research/leaf-packets/L15-defect-5-staircase.md",
        "research/tracks/m-filtered-equivariance.md",
    ],
    "base_sha": "4e26438c83d370be8fcddf14da88ef151cb3e841",
    "candidate_sha": "2eeb36d232366d124b5a66774b29769ec1eba43d",
    "scientific_status": "candidate_proved",
    "review_mode": "local-adversarial-review",
    "reviewed_revision": "2eeb36d232366d124b5a66774b29769ec1eba43d",
    "proposed_global_claims": [{"id": "CLM-073", "status": "candidate_proved", "scope": "fixed primitive positive weight with actual grading defect five"}],
    "proposed_graph_nodes": [{"id": "OPEN-DEFECT-5", "status": "disposed", "disposition": "CANDIDATE_PROVED_LOCAL_REVIEW"}],
    "shared_surfaces_requested": [
        "STATUS.md",
        "research/claim_ledger.json",
        "research/CLAIM_LEDGER.md",
        "research/proof_graph.json",
        "research/PROOF_GRAPH.md",
        "research/work_queue.json",
        "research/WORK_QUEUE.md",
        "research/ISSUE_INDEX.md",
        "scripts/render_views.py",
        "scripts/validate_repository_legacy.py",
    ],
    "supersedes_prs": [30, 36],
    "temporary_artifacts_absent": True,
    "integration_state": "integration-ready",
}
save("research/issues/defect-5-rees/INTEGRATION.json", manifest)

print("defect-five staging synchronization: PASS")
