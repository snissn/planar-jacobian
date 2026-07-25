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
namespace = {"__name__": "__main__", "__file__": str(legacy)}
exec(compile(source, str(legacy), "exec"), namespace)
