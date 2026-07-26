#!/usr/bin/env python3
"""Run every exact symbolic check in the rank-three boundary-cube packet."""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parent
SCRIPTS = [
    "verify_binary_cubic.py",
    "verify_index_and_fitting.py",
    "verify_boundary_family.py",
    "verify_countermodel_ladder.py",
    "verify_prime_degree_audit.py",
]
MIN_PYTHON = (3, 12)
EXPECTED_SYMPY = "1.14.0"


def check_environment() -> None:
    """Guard the canonical packet suite's symbolic runtime."""
    if sys.version_info < MIN_PYTHON:
        found = f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
        required = ".".join(map(str, MIN_PYTHON))
        raise SystemExit(f"Python {required} or newer is required; found {found}")
    if sp.__version__ != EXPECTED_SYMPY:
        raise SystemExit(
            f"SymPy {EXPECTED_SYMPY} is required; found {sp.__version__}"
        )


def main() -> int:
    check_environment()
    for script in SCRIPTS:
        subprocess.run([sys.executable, str(ROOT / script)], check=True)
    print("rank-three boundary-cube packet verification: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
