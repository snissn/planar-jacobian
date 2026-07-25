#!/usr/bin/env python3
"""Run all issue-owned checks for the OBLF packet."""
from __future__ import annotations

import argparse
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

# Bind the harness to stable packet identifiers and exact source/version labels,
# not to incidental prose that can be copy-edited without changing scope.
MARKERS = {
    "README.md": [
        "scientific_status: SUBCLASS_EXCLUSION_WITH_EXACT_REDUCTION",
        "`OBLF-05`",
        "`OBLF-09`",
    ],
    "BOUNDARY_HYPOTHESES.md": ["`OBLF-H3`", "`OBLF-H8`"],
    "LOGARITHMIC_MODULE.md": ["`OBLF-01`", "Syz_B(g_P,g_Q,-g)"],
    "SEMISIMPLE_CLASSIFICATION.md": [
        "`OBLF-04`",
        "`OBLF-05`",
        "arXiv:2607.20210v1, Theorem 3.3",
    ],
    "PRINCIPAL_PARTS.md": ["`OBLF-07`", "`OBLF-09`"],
    "SOURCE_OPEN_INVARIANCE.md": ["`OBLF-05`", "`OBLF-06`", "Tag 0BMB"],
    "REVIEW.md": ["ACCEPT_FOR_CANDIDATE_INTEGRATION", "BLOCK_PROMOTION"],
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
    print(f"OBLF packet structure: PASS ({len(REQUIRED)} files)")


def run_symbolic() -> None:
    subprocess.run([sys.executable, str(HERE / "verify_oblf.py")], check=True)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--structure-only", action="store_true")
    mode.add_argument("--symbolic-only", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.structure_only:
        check_files_and_markers()
        return 0
    if args.symbolic_only:
        run_symbolic()
        return 0
    check_files_and_markers()
    run_symbolic()
    print("OBLF aggregate checks: PASS")
    print("review authority: candidate integration only")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
