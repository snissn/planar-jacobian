#!/usr/bin/env python3
"""Run the issue #4 synchronization and apply governance-mode corrections.

This transport wrapper and its implementation delete themselves before the
resulting synchronization commit is created.  Repository writes remain on the
issue branch and are performed by the repository workflow.
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
IMPL = ROOT / "scripts/sync_issue4_source_reflexive_impl.py"
WORKFLOW = ROOT / ".github/workflows/repository-python-validators.yml"


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected exactly one source occurrence, found {count}")
    return text.replace(old, new, 1)


def edit(path: Path, replacements: list[tuple[str, str, str]]) -> None:
    text = path.read_text(encoding="utf-8")
    for old, new, label in replacements:
        text = replace_once(text, old, new, label)
    path.write_text(text, encoding="utf-8")


def main() -> int:
    subprocess.run([sys.executable, str(IMPL)], cwd=ROOT, check=True)

    # The GitHub App token can write repository contents but cannot push a
    # workflow-file mutation.  Restore the exact event workflow; a later
    # adapter commit installs the permanent read-only workflow.
    workflow = subprocess.check_output(
        ["git", "show", "HEAD:.github/workflows/repository-python-validators.yml"],
        cwd=ROOT,
        text=True,
    )
    WORKFLOW.write_text(workflow, encoding="utf-8")

    edit(
        ROOT / "research/issues/source-reflexive-lattice/README.md",
        [
            (
                "> **Review status:** constructor adversarial review required before integration  ",
                "> **Review status:** declared `local-adversarial-review`; promotion blocked",
                "packet README review mode",
            )
        ],
    )
    edit(
        ROOT / "research/issues/source-reflexive-lattice/REVIEW.md",
        [
            (
                "> **Review mode:** `constructor-adversarial-review`  ",
                "> **Review mode:** `local-adversarial-review`",
                "review mode",
            ),
            (
                "The same assistant constructed and adversarially reviewed the candidate.\n"
                "Repository governance permits this as a declared fallback, but it is not an\n"
                "independent scientific acceptance and cannot promote any claim to\n"
                "`reviewed_scoped`.",
                "The same assistant constructed and adversarially reviewed the candidate in declared\n"
                "`local-adversarial-review` mode. Repository governance permits this fallback\n"
                "when no distinct reviewer is available, but it is not independent scientific\n"
                "acceptance and cannot promote any claim to `reviewed_scoped`. The mode-name\n"
                "correction in packet metadata is editorial and does not alter the pinned\n"
                "candidate theorem bytes.",
                "review independence wording",
            ),
        ],
    )
    edit(
        ROOT / "research/issues/source-reflexive-lattice/HANDOFF.md",
        [
            (
                "The packet reaches a class-level obstruction, not an unconditional planar\n"
                "Jacobian theorem.  The constructor adversarial review permits mutable\n"
                "mainline preservation but blocks promotion to reviewed authority.",
                "The packet reaches a class-level obstruction, not an unconditional planar\n"
                "Jacobian theorem. The declared `local-adversarial-review` permits mutable\n"
                "mainline preservation but blocks promotion to reviewed authority.",
                "handoff review mode",
            )
        ],
    )
    edit(
        ROOT / "research/leaf-packets/L02-stable-order.md",
        [
            (
                "The integrated packet reaches a constructor-reviewed class-level obstruction for divisorial source-pole constructions. Promotion remains blocked because the review is not independent. The leaf remains open.",
                "The integrated packet reaches a class-level obstruction for divisorial source-pole constructions under a declared `local-adversarial-review`. Promotion remains blocked because the review is not independent. The leaf remains open.",
                "L02 review mode",
            )
        ],
    )
    edit(
        ROOT / "research/tracks/d-stable-differential-lattice.md",
        [
            (
                "The successor's declared constructor adversarial review passes mutable integration but blocks promotion. No finite pair-stable lattice is constructed.",
                "The successor's declared `local-adversarial-review` passes mutable integration but blocks promotion. No finite pair-stable lattice is constructed.",
                "track D review mode",
            )
        ],
    )

    validator = ROOT / "scripts/validate_repository.py"
    validator_text = validator.read_text(encoding="utf-8")
    anchor = (
        '        if "Promotion disposition:** `BLOCK`" not in review_text:\n'
        '            error("source-reflexive-lattice review: promotion BLOCK is missing")\n'
    )
    addition = anchor + (
        '        if "Review mode:** `local-adversarial-review`" not in review_text:\n'
        '            error("source-reflexive-lattice review: permitted local-adversarial-review mode is missing")\n'
        '        if "constructor-adversarial-review" in review_text:\n'
        '            error("source-reflexive-lattice review: unsupported constructor review mode remains")\n'
    )
    validator.write_text(
        replace_once(validator_text, anchor, addition, "validator review-mode anchor"),
        encoding="utf-8",
    )

    Path(__file__).unlink()
    print("issue #4 shared synchronization and local review-mode correction prepared")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
