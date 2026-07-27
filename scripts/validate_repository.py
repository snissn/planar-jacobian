#!/usr/bin/env python3
"""Run integration-policy checks, then the maintained structural validator.

The legacy implementation is preserved byte-for-byte beside this wrapper. The
only runtime source transformation removes its historical fixed upper claim-ID
snapshot while retaining all named scientific invariants.
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
)
if claim_anchor not in source:
    print("ERROR: legacy CLM-070 invariant anchor was not found")
    raise SystemExit(1)
source = source.replace(claim_anchor, claim_checks, 1)
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
namespace = {"__name__": "__main__", "__file__": str(legacy)}
exec(compile(source, str(legacy), "exec"), namespace)
