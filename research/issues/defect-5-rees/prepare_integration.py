#!/usr/bin/env python3
"""Prepare a clean issue #29 integration overlay for artifact extraction.

This helper never commits or pushes. It is deleted before the integration PR is
opened; only its generated durable files are retained.
"""
from __future__ import annotations

import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PACKET = "research/issues/defect-5-rees/README.md"


def load(path: str):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def save(path: str, value) -> None:
    (ROOT / path).write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def replace_once(path: str, old: str, new: str) -> None:
    target = ROOT / path
    text = target.read_text(encoding="utf-8")
    if new in text:
        return
    if old not in text:
        raise RuntimeError(f"{path}: anchor not found")
    target.write_text(text.replace(old, new, 1), encoding="utf-8")


claims = load("research/claim_ledger.json")
ids = [item["id"] for item in claims["claims"]]
if ids[-1] == "CLM-072":
    claims["claims"].append(
        {
            "id": "CLM-073",
            "status": "candidate_proved",
            "track": "filtered-equivariance",
            "statement": "For any primitive positive weight w, a planar Keller pair with grading defect kappa_w=5 admits a filtration-compatible polynomial source or target automorphism that strictly lowers the actual integer defect to at most four; hence it is a polynomial automorphism by the reviewed defect-at-most-four theorem.",
            "depends_on": ["CLM-047", "CLM-048", "CLM-049", "CLM-051", "CLM-060"],
            "note": "Issue #29 defect-five packet. A separate local-adversarial-review returned ACCEPT for candidate 2eeb36d232366d124b5a66774b29769ec1eba43d, but this is not independent review and the claim remains mutable candidate_proved. It does not prove that every Keller pair admits a qualifying primitive positive weight, does not treat defect six, and does not establish JC_2.",
        }
    )
elif ids[-1] != "CLM-073":
    raise RuntimeError(f"unexpected terminal claim {ids[-1]}")
save("research/claim_ledger.json", claims)

graph = load("research/proof_graph.json")
if not any(node["id"] == "OPEN-DEFECT-5" for node in graph["nodes"]):
    graph["nodes"].append(
        {
            "id": "OPEN-DEFECT-5",
            "title": "Independently review the fixed-weight defect-five closure",
            "type": "leaf",
            "status": "open",
            "artifact": "leaf-packets/L15-defect-5-staircase.md",
            "note": "Issue #29 banks CLM-073 at candidate_proved after local-adversarial-review ACCEPT. Independent review is issue #38; no qualifying-weight existence, defect-six, or JC_2 inference is licensed.",
        }
    )
for edge in [
    {"from": "BR-FILTERED-EQUIVARIANCE", "to": "OPEN-DEFECT-5", "kind": "requires"},
    {"from": "OPEN-DEFECT-4", "to": "OPEN-DEFECT-5", "kind": "supports"},
    {"from": "OPEN-DEFECT-5", "to": "OPEN-GRADED-REDUCTION", "kind": "supports"},
]:
    if edge not in graph["edges"]:
        graph["edges"].append(edge)
save("research/proof_graph.json", graph)

queue = load("research/work_queue.json")
if not any(item["id"] == "L15" for item in queue["leaves"] + queue.get("dispositions", [])):
    leaf = {
        "id": "L15",
        "graph_node": "OPEN-DEFECT-5",
        "title": "Independent Review of Fixed-Weight Defect Five",
        "priority": "P0",
        "status": "open",
        "artifact": "research/leaf-packets/L15-defect-5-staircase.md",
        "track_artifact": "research/tracks/m-filtered-equivariance.md",
        "issue_number": 38,
        "claim_dependencies": ["CLM-047", "CLM-048", "CLM-049", "CLM-051", "CLM-060", "CLM-073"],
    }
    index = next((i + 1 for i, item in enumerate(queue["leaves"]) if item["id"] == "L14"), 0)
    queue["leaves"].insert(index, leaf)
save("research/work_queue.json", queue)

(ROOT / "research/leaf-packets/L15-defect-5-staircase.md").write_text(
    """# L15 — Independent Review of Fixed-Weight Defect Five

> **Construction issue:** [#29](https://github.com/snissn/planar-jacobian/issues/29)  
> **Review issue:** [#38](https://github.com/snissn/planar-jacobian/issues/38)  
> **Issue packet:** [`../issues/defect-5-rees/`](../issues/defect-5-rees/)  
> **Banked claim:** `CLM-073` (`candidate_proved`)  
> **Required review mode:** `independent-review`

## Load-bearing question

Independently review the exact issue #29 candidate at `2eeb36d232366d124b5a66774b29769ec1eba43d`: for a fixed primitive positive weight and actual grading defect five, does every Keller pair have a resonant endpoint or a filtration-compatible strict descent to defect at most four?

## Forbidden shortcuts

- Do not treat the local adversarial review as independent acceptance.
- Do not infer existence of a defect-at-most-five weight for every Keller pair.
- Do not omit zero layers, simultaneous resonances, either source-weight order, or either target-component order.
- Do not begin defect six or attach a terminal `JC_2` edge.

## Required artifacts

- independent reconstruction of normalization, complete-top descent, support sieve, equal-weight chains, and finite exceptional systems;
- an independently implemented checker or exact hand calculations;
- a pinned `ACCEPT` or `BLOCK` review record;
- a synchronization proposal limited to `CLM-073` and `OPEN-DEFECT-5`.

## Candidate evidence

The issue packet contains a complete derivation, exact case table, from-definitions checker, mutation controls, saturated Gröbner eliminations, and a separate local-adversarial-review checker. These are falsification evidence, not independent theorem authority.

## Stop rule

Return `ACCEPT` only after every load-bearing case and transformation is independently reconstructed at the pinned bytes. Otherwise return the smallest exact `BLOCK`, correction, or formal countermodel.

## Handoff

On independent `ACCEPT`, promote only the fixed-weight defect-five statement. Preserve the nonclaims about qualifying-weight existence, defect six, arbitrary termination, and `JC_2`.
""",
    encoding="utf-8",
)

track = ROOT / "research/tracks/m-filtered-equivariance.md"
text = track.read_text(encoding="utf-8")
header_anchor = "> **Scientific inference:** primitive positive weight and `kappa_w<=4` imply automorphism; no broader inference\n"
header = "> **Defect-five candidate:** issue [#29](https://github.com/snissn/planar-jacobian/issues/29), `CLM-073`; local-adversarial-review only  \n"
if header not in text:
    if header_anchor not in text:
        raise RuntimeError("track header anchor missing")
    text = text.replace(header_anchor, header_anchor + header, 1)
section = """## 9. Defect five candidate and successor review

Issue #29 banks the fixed-weight defect-five theorem in [`../issues/defect-5-rees/README.md`](../issues/defect-5-rees/README.md) as `CLM-073` with status `candidate_proved`. The exact candidate `2eeb36d232366d124b5a66774b29769ec1eba43d` received a separate local-adversarial-review `ACCEPT`, not independent acceptance.

Every resonant endpoint is invertible; every interior system either admits complete-top strict descent to `kappa_w<=4` or contradicts the complete staircase. The standard-weight coupled transverse chains are the first new defect-five correction and are not imported from the defect-four middle-Wronskian row.

The successor leaf [`L15-defect-5-staircase.md`](../leaf-packets/L15-defect-5-staircase.md) and issue [#38](https://github.com/snissn/planar-jacobian/issues/38) request independent review. No qualifying-weight existence, defect-six, arbitrary-termination, or `JC_2` claim is introduced.

"""
if section not in text:
    if "## Exit" not in text:
        raise RuntimeError("track exit anchor missing")
    text = text.replace("## Exit", section + "## Exit", 1)
text = text.replace(
    "Defect `5`, a theorem producing a qualifying weight, and `JC_2` remain outside this track's reviewed scope.",
    "Defect `5` is banked only as mutable candidate `CLM-073`; independent review remains open as `L15`. A qualifying-weight theorem, defect six, and `JC_2` remain outside this track's reviewed scope.",
)
track.write_text(text, encoding="utf-8")

replace_once(
    "README.md",
    "- **Defect at most four:** `CLM-047–051` and `CLM-060` are `reviewed_scoped`, bound to independent `ACCEPT` at candidate revision `96fc7ec34bd3b685a0edeae7ecd4404abab7e2f1`. The theorem applies only to primitive positive weights with grading defect at most four. It does not cover defect five, prove that an arbitrary Keller pair has such a weight, or establish `JC_2`.",
    "- **Filtered defects:** `CLM-047–051` and `CLM-060` are `reviewed_scoped` only through defect four, bound to independent `ACCEPT` at candidate revision `96fc7ec34bd3b685a0edeae7ecd4404abab7e2f1`. The [defect-five packet](research/issues/defect-5-rees/README.md) is separately banked as mutable `CLM-073` after local-adversarial-review `ACCEPT`; independent review remains issue #38. Neither scope proves that an arbitrary Keller pair has a qualifying weight or establishes `JC_2`.",
)
replace_once(
    "README.md",
    "python3 -m compileall -q scripts research/issues/issue-3-unramified-index research/issues/rank-three-index-form-unit research/issues/source-reflexive-lattice research/issues/one-boundary-logarithmic-field",
    "python3 -m compileall -q scripts research/issues",
)
replace_once(
    "README.md",
    "python3 research/issues/one-boundary-logarithmic-field/verify_all.py\n",
    "python3 research/issues/one-boundary-logarithmic-field/verify_all.py\npython3 research/issues/defect-5-rees/validate_defect5.py --max-weight 64 --json\npython3 research/issues/defect-5-rees/review_validate_defect5_adversarial.py\n",
)

render = ROOT / "scripts/render_views.py"
render_text = render.read_text(encoding="utf-8")
render_text = render_text.replace(
    '        "- **Explicit nonclaims:** no defect-five theorem, no theorem producing a qualifying weight for every Keller pair, and no proof of `JC_2`.",',
    '        "- **Candidate-only defect five:** fixed primitive positive weight and actual defect five is `CLM-073` at mutable `candidate_proved` scope after local-adversarial review; no independent acceptance.",\n        "- **Explicit nonclaims:** no theorem producing a qualifying weight for every Keller pair, no defect-six or arbitrary-termination theorem, and no proof of `JC_2`.",',
)
issue17 = '        "- **Issue #17:** the exact positive-weight defect-at-most-four theorem is reviewed only at the pinned revision. It creates no terminal edge to `JC_2`.",\n'
issue29 = '        "- **Issue #29:** fixed primitive positive weight and actual defect five is banked as `CLM-073` at mutable `candidate_proved` scope. Independent review is issue #38; no qualifying-weight, defect-six, or `JC_2` claim is introduced.",\n'
if issue29 not in render_text:
    if issue17 not in render_text:
        raise RuntimeError("render status issue anchor missing")
    render_text = render_text.replace(issue17, issue17 + issue29, 1)
render.write_text(render_text, encoding="utf-8")

validator = ROOT / "scripts/validate_repository.py"
validator_text = validator.read_text(encoding="utf-8")
anchor = 'source = source.replace(old, new, 1)\n'
extra = '''source = source.replace(old, new, 1)
claim_anchor = ''' + repr('''    if "arXiv:2607.20210v1" not in by_id.get("CLM-070", {}).get("note", ""):
        error("CLM-070: terminal subclass exclusion must retain exact external dependency")
''') + '''
claim_checks = claim_anchor + ''' + repr('''    if by_id.get("CLM-073", {}).get("status") != "candidate_proved":
        error("CLM-073 must remain candidate_proved pending independent review")
    if "does not prove that every Keller pair admits" not in by_id.get("CLM-073", {}).get("note", ""):
        error("CLM-073 lost its qualifying-weight nonclaim")
''') + '''
if claim_anchor not in source:
    print("ERROR: legacy CLM-070 invariant anchor was not found")
    raise SystemExit(1)
source = source.replace(claim_anchor, claim_checks, 1)
graph_anchor = ''' + repr('''    if node_by_id.get("OPEN-DEFECT-4", {}).get("status") != "reviewed":
        error("OPEN-DEFECT-4 must retain reviewed status")
''') + '''
graph_checks = graph_anchor + ''' + repr('''    if node_by_id.get("OPEN-DEFECT-5", {}).get("status") != "open":
        error("OPEN-DEFECT-5 must remain open pending independent review")
''') + '''
if graph_anchor not in source:
    print("ERROR: legacy OPEN-DEFECT-4 invariant anchor was not found")
    raise SystemExit(1)
source = source.replace(graph_anchor, graph_checks, 1)
'''
if "CLM-073 must remain candidate_proved" not in validator_text:
    if anchor not in validator_text:
        raise RuntimeError("validator wrapper anchor missing")
    validator_text = validator_text.replace(anchor, extra, 1)
validator.write_text(validator_text, encoding="utf-8")

manifest = {
    "schema_version": 1,
    "issue_number": 29,
    "leaf_id": "L15",
    "role": "integration-maintainer",
    "owned_paths": ["research/issues/defect-5-rees/"],
    "base_sha": "4e26438c83d370be8fcddf14da88ef151cb3e841",
    "candidate_sha": "99d502ffb965d84b4046a625a6f83c3a03f9328c",
    "scientific_status": "candidate_proved / MUTABLE_NONAUTHORITATIVE",
    "review_mode": "local-adversarial-review",
    "reviewed_revision": "2eeb36d232366d124b5a66774b29769ec1eba43d",
    "proposed_global_claims": [{"id": "CLM-073", "status": "candidate_proved"}],
    "proposed_graph_nodes": [{"id": "OPEN-DEFECT-5", "status": "open"}],
    "shared_surfaces_requested": [
        "README.md",
        "STATUS.md",
        "research/claim_ledger.json",
        "research/proof_graph.json",
        "research/work_queue.json",
        "research/ISSUE_INDEX.md",
    ],
    "supersedes_prs": [30],
    "temporary_artifacts_absent": True,
    "integration_state": "integration-ready",
    "pr_number": None,
    "completion_receipt": None,
}
save("research/issues/defect-5-rees/INTEGRATION.json", manifest)

subprocess.run(["python3", "scripts/render_views.py", "--write"], cwd=ROOT, check=True)
print("defect-five integration overlay prepared")
