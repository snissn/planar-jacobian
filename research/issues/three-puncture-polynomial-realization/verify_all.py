#!/usr/bin/env python3
"""Packet aggregator for the exact scientific candidate."""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent
REQUIRED = {
    "README.md",
    "BRANCH_GEOMETRY.md",
    "SOURCE_COMPACTIFICATION.md",
    "POLE_AND_DIVISOR_TABLE.md",
    "CONDUCTOR_DESCENT.md",
    "POLYNOMIAL_REALIZATION.md",
    "FINITE_CASES.md",
    "COUNTERMODEL_LADDER.md",
    "LITERATURE_AUDIT.md",
    "verify_three_puncture.py",
    "verify_all.py",
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def run_checker(max_degree: int) -> dict:
    proc = subprocess.run(
        [
            sys.executable,
            str(ROOT / "verify_three_puncture.py"),
            "--max-degree",
            str(max_degree),
            "--json",
        ],
        check=True,
        text=True,
        capture_output=True,
    )
    return json.loads(proc.stdout)


def main() -> int:
    try:
        missing = sorted(name for name in REQUIRED if not (ROOT / name).is_file())
        require(not missing, f"missing candidate artifacts: {missing}")
        text = "\n".join((ROOT / name).read_text() for name in sorted(REQUIRED) if name.endswith(".md"))
        for phrase in (
            "Jelonek--Lasoń",
            "generically finite",
            "nonproperness",
            "no nonconstant polynomial",
            "MUTABLE_NONAUTHORITATIVE",
            "does not prove a general one-boundary theorem",
        ):
            require(phrase in text, f"missing scope/source guard: {phrase}")
        require("simultaneous monomialization" in text, "missing nonmonomial valuation guard")
        default = run_checker(12)
        enlarged = run_checker(32)
        require(default["status"] == enlarged["status"] == "PASS", "checker status")
        require(enlarged["total_checks"] > default["total_checks"], "enlarged campaign did not grow")
    except Exception as exc:
        print(f"three-puncture packet verification: FAIL: {exc}")
        return 1
    print(f"default exact assertions: {default['total_checks']}")
    print(f"enlarged exact assertions: {enlarged['total_checks']}")
    print("three-puncture packet verification: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
