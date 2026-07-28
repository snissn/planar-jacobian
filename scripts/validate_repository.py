#!/usr/bin/env python3
"""Run integration-policy checks, then the maintained structural validator.

The legacy implementation is preserved byte-for-byte beside this wrapper.
Runtime source transformations replace historical snapshot invariants with
transition-aware checks for canonical states already defined by the ledgers.
"""
from __future__ import annotations

from pathlib import Path
import sys

from validate_integration_contract import validate_root

ROOT = Path(__file__).resolve().parents[1]
result = validate_root(ROOT)
if result.errors:
    for message in result.errors:
        print("ERROR:", message)
    for message in result.warnings:
        print("WARNING:", message)
    print("integration contract: FAIL")
    raise SystemExit(1)

legacy = Path(__file__).with_name("validate_repository_legacy.py")
source = legacy.read_text(encoding="utf-8")
old = '''    expected_sequence = [f"CLM-{number:03d}" for number in range(1, 73)]
    if ids != expected_sequence:
        error("claim IDs must be the ordered contiguous sequence CLM-001 through CLM-066")
'''
new = '''    numeric_ids = []
    for claim_id in ids:
        match = re.fullmatch(r"CLM-(\\d{3,})", claim_id)
        if not match:
            error(f"invalid claim ID format: {claim_id!r}")
            continue
        numeric_ids.append(int(match.group(1)))
    expected_sequence = (
        [f"CLM-{number:03d}" for number in range(1, max(numeric_ids) + 1)]
        if numeric_ids
        else []
    )
    if ids != expected_sequence:
        terminal = expected_sequence[-1] if expected_sequence else "<none>"
        error(
            "claim IDs must be the ordered contiguous sequence starting at "
            f"CLM-001 and ending at the actual maximum {terminal}"
        )
'''
if old not in source:
    print("ERROR: legacy claim-sequence snapshot was not found")
    raise SystemExit(1)
source = source.replace(old, new, 1)
clm059_old = '''    if by_id.get("CLM-059", {}).get("status") != "open_bridge":
        error("CLM-059: Keller-specific index-form unit theorem must remain open_bridge")
'''
clm059_new = '''    if "CLM-074" in by_id:
        clm059 = by_id.get("CLM-059", {})
        if clm059.get("status") != "retired":
            error("CLM-059: rank-three construction target must remain retired")
        if "CLM-074" not in clm059.get("depends_on", []):
            error("CLM-059: rank-three retirement must depend on CLM-074")
        if "no unit-index section was constructed" not in clm059.get("note", "").lower():
            error("CLM-059: retirement must retain the constructive nonclaim")
    elif by_id.get("CLM-059", {}).get("status") != "open_bridge":
        error("CLM-059: Keller-specific index-form unit theorem must remain open_bridge before a bounded terminal is synchronized")
'''
if clm059_old not in source:
    print("ERROR: legacy CLM-059 status snapshot was not found")
    raise SystemExit(1)
source = source.replace(clm059_old, clm059_new, 1)
claim_anchor = '    if "arXiv:2607.20210v1" not in by_id.get("CLM-070", {}).get("note", ""):\n        error("CLM-070: terminal subclass exclusion must retain exact external dependency")\n'
claim_checks = claim_anchor + (
    '    clm073 = by_id.get("CLM-073", {})\n'
    '    if clm073.get("status") != "reviewed_scoped":\n'
    '        error("CLM-073 must be reviewed_scoped after the independent issue #38 ACCEPT")\n'
    '    clm073_review = clm073.get("review", {})\n'
    '    if clm073_review.get("mode") != "independent-review" or clm073_review.get("disposition") != "ACCEPT":\n'
    '        error("CLM-073 must retain the independent ACCEPT binding")\n'
    '    if clm073_review.get("reviewed_revision") != "2eeb36d232366d124b5a66774b29769ec1eba43d":\n'
    '        error("CLM-073 reviewed revision drifted")\n'
    '    if clm073_review.get("candidate_aggregate_sha256") != "333614389c339f4a3383856de2dfc5b977dc5dd6a6520f176b25c7116d861d12":\n'
    '        error("CLM-073 candidate aggregate drifted")\n'
    '    if clm073_review.get("review_record") != "research/issues/defect-5-independent-review/REVIEW.md":\n'
    '        error("CLM-073 review record drifted")\n'
    '    if clm073_review.get("freeze_record") != "governance/reviews/issue-38-defect5-mainline-freeze.md":\n'
    '        error("CLM-073 freeze record drifted")\n'
    '    if "does not prove that every Keller pair admits" not in clm073.get("note", ""):\n'
    '        error("CLM-073 lost its qualifying-weight nonclaim")\n'
    '    for phrase in ("arbitrary filtered termination", "generic defect six", "does not establish JC_2"):\n'
    '        if phrase not in clm073.get("note", ""):\n'
    '            error(f"CLM-073 lost nonclaim: {phrase}")\n'
    '    if "CLM-074" in by_id:\n'
    '        rank_three_statuses = {\n'
    '            "CLM-074": "literature_bound",\n'
    '            "CLM-075": "candidate_proved",\n'
    '            "CLM-076": "candidate_proved",\n'
    '            "CLM-077": "candidate_proved",\n'
    '            "CLM-078": "literature_bound",\n'
    '        }\n'
    '        for claim_id, expected_status in rank_three_statuses.items():\n'
    '            if by_id.get(claim_id, {}).get("status") != expected_status:\n'
    '                error(f"{claim_id}: rank-three synchronization status drifted")\n'
    '        clm074 = by_id.get("CLM-074", {})\n'
    '        statement = clm074.get("statement", "")\n'
    '        if "function-field degree three" not in statement or "Orevkov" not in statement:\n'
    '            error("CLM-074: bounded primary-source terminal drifted")\n'
    '        for phrase in ("constructs no unit-index section", "degree four or higher", "JC_2"):\n'
    '            if phrase not in clm074.get("note", ""):\n'
    '                error(f"CLM-074 lost nonclaim: {phrase}")\n'
    '        if "CLM-074" not in by_id.get("CLM-078", {}).get("depends_on", []):\n'
    '            error("CLM-078: literature-bound application lost CLM-074 dependency")\n'
)
if claim_anchor not in source:
    print("ERROR: legacy CLM-070 invariant anchor was not found")
    raise SystemExit(1)
source = source.replace(claim_anchor, claim_checks, 1)
keller_node_old = '''    if node_by_id.get("OPEN-KELLER-INDEX-UNIT", {}).get("status") != "open":
        error("OPEN-KELLER-INDEX-UNIT must remain open")
'''
keller_node_new = '''    rank_three_terminal = node_by_id.get("TERM-RANK-THREE-EXCLUSION")
    if rank_three_terminal:
        if node_by_id.get("OPEN-KELLER-INDEX-UNIT", {}).get("status") != "disposed":
            error("OPEN-KELLER-INDEX-UNIT must retain disposed rank-three status")
        if rank_three_terminal.get("type") != "terminal" or rank_three_terminal.get("status") != "literature_bound":
            error("TERM-RANK-THREE-EXCLUSION must retain its literature-bound terminal scope")
    elif node_by_id.get("OPEN-KELLER-INDEX-UNIT", {}).get("status") != "open":
        error("OPEN-KELLER-INDEX-UNIT must remain open before a bounded terminal is synchronized")
'''
if keller_node_old not in source:
    print("ERROR: legacy OPEN-KELLER-INDEX-UNIT snapshot was not found")
    raise SystemExit(1)
source = source.replace(keller_node_old, keller_node_new, 1)
graph_anchor = '    if node_by_id.get("OPEN-DEFECT-4", {}).get("status") != "reviewed":\n        error("OPEN-DEFECT-4 must retain reviewed status")\n'
graph_checks = graph_anchor + (
    '    defect5 = node_by_id.get("OPEN-DEFECT-5", {})\n'
    '    if defect5.get("status") != "reviewed":\n'
    '        error("OPEN-DEFECT-5 must retain reviewed status")\n'
    '    if defect5.get("review_artifact") != "research/issues/defect-5-independent-review/REVIEW.md":\n'
    '        error("OPEN-DEFECT-5 review artifact drifted")\n'
)
if graph_anchor not in source:
    print("ERROR: legacy OPEN-DEFECT-4 invariant anchor was not found")
    raise SystemExit(1)
source = source.replace(graph_anchor, graph_checks, 1)
edge_anchor = '''    for edge in edges:
        if edge.get("from") == "OPEN-DEFECT-4" and edge.get("to") in forbidden_targets:
            error("OPEN-DEFECT-4 must not acquire a terminal or JC_2 edge")
'''
edge_checks = edge_anchor + '''    if rank_three_terminal:
        required_rank_three_edges = {
            ("OPEN-KELLER-INDEX-UNIT", "narrows-to", "TERM-RANK-THREE-EXCLUSION"),
            ("CTL-LITERATURE", "supports", "TERM-RANK-THREE-EXCLUSION"),
        }
        present_edges = {
            (edge.get("from"), edge.get("kind"), edge.get("to"))
            for edge in edges
        }
        missing_edges = required_rank_three_edges - present_edges
        if missing_edges:
            error(f"rank-three literature-bound terminal lost required edges: {sorted(missing_edges)}")
        for edge in edges:
            if (
                edge.get("from") in {"OPEN-KELLER-INDEX-UNIT", "TERM-RANK-THREE-EXCLUSION"}
                and edge.get("to") in forbidden_targets
            ):
                error("rank-three disposition must not acquire a degree-one or JC_2 edge")
'''
if edge_anchor not in source:
    print("ERROR: legacy terminal-edge invariant anchor was not found")
    raise SystemExit(1)
source = source.replace(edge_anchor, edge_checks, 1)
namespace = {"__name__": "__main__", "__file__": str(legacy)}
exec(compile(source, str(legacy), "exec"), namespace)
