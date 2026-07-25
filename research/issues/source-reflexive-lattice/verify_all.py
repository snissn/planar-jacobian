#!/usr/bin/env python3
"""Run every exact check owned by the source-reflexive-lattice packet."""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent


def main() -> int:
    scripts = [
        HERE / "verify_local_residues.py",
        HERE / "verify_filtration_and_symplectic.py",
    ]
    for script in scripts:
        subprocess.run([sys.executable, str(script)], check=True)
    print("source-reflexive-lattice aggregate validation: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
