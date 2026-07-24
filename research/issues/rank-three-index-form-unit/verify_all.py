#!/usr/bin/env python3
"""Run every exact symbolic check in this packet."""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SCRIPTS = [
    "verify_rank_three_index.py",
    "verify_differential_identity.py",
    "verify_countermodel_boundary.py",
]


def main() -> int:
    for script in SCRIPTS:
        subprocess.run([sys.executable, str(ROOT / script)], check=True)
    print("rank-three packet verification: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
