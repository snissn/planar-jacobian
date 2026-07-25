#!/usr/bin/env python3
"""Run every exact symbolic check in the rank-three boundary-cube packet."""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SCRIPTS = [
    "verify_binary_cubic.py",
    "verify_index_and_fitting.py",
    "verify_boundary_family.py",
    "verify_countermodel_ladder.py",
    "verify_prime_degree_audit.py",
]


def main() -> int:
    for script in SCRIPTS:
        subprocess.run([sys.executable, str(ROOT / script)], check=True)
    print("rank-three boundary-cube packet verification: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
