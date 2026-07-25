#!/usr/bin/env python3
"""Run all issue-owned checks for the OBLF packet."""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path


HERE = Path(__file__).resolve().parent
REQUIRED = [
    "README.md",
    "BOUNDARY_HYPOTHESES.md",
    "LOGARITHMIC_MODULE.md",
    "SEMISIMPLE_CLASSIFICATION.md",
    "PRINCIPAL_PARTS.md",
    "CONDUCTOR_AND_PUNCTURES.md",
    "SOURCE_OPEN_INVARIANCE.md",
    "SUBCLASS_TABLE.md",
    "COUNTERMODELS.md",
    "REVIEW.md",
    "HANDOFF.md",
    "verify_oblf.py",
    "verify_all.py",
]

MARKERS = {
    "README.md": [
        "SUBCLASS_EXCLUSION_WITH_EXACT_REDUCTION",
        "OBLF-05",
        "does **not** prove the planar Jacobian conjecture",
    ],
    "BOUNDARY_HYPOTHESES.md": [
        "the branch divisor equals the boundary",
        "actual nontrivial algebraic `G_m` action",
    ],
    "LOGARITHMIC_MODULE.md": [
        "Syz_B(g_P,g_Q,-g)",
        "Quillen-Suslin",
        "Hamiltonian field",
    ],
    "SEMISIMPLE_CLASSIFICATION.md": [
        "finite-isogeny",
        "arXiv:2607.20210v1, Theorem 3.3",
        "regular derivation on `Y` is complete",
    ],
    "PRINCIPAL_PARTS.md": [
        "n a' b - m a b' = 0",
        "does not eliminate higher principal parts",
    ],
    "SOURCE_OPEN_INVARIANCE.md": [
        "delta(p) subset p",
        "Tag 0BMB",
        "OBLF-06",
    ],
    "REVIEW.md": [
        "local-adversarial-review",
        "BLOCK_PROMOTION",
    ],
}


def fail(message: str) -> None:
    raise AssertionError(message)


def check_files_and_markers() -> None:
    for name in REQUIRED:
        path = HERE / name
        if not path.is_file():
            fail(f"missing required packet file: {name}")
    for name, markers in MARKERS.items():
        text = (HERE / name).read_text(encoding="utf-8")
        for marker in markers:
            if marker not in text:
                fail(f"{name}: missing marker {marker!r}")


def run_symbolic() -> None:
    subprocess.run([sys.executable, str(HERE / "verify_oblf.py")], check=True)


def main() -> int:
    check_files_and_markers()
    run_symbolic()
    print(f"OBLF packet files: PASS ({len(REQUIRED)} files)")
    print("review authority: candidate integration only")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
