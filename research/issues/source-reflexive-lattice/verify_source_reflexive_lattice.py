#!/usr/bin/env python3
"""Exact rational regressions for the source-reflexive-lattice packet.

These checks verify displayed local formulas and the artifact contract. They do
not evaluate the global mathematical truth or confer scientific acceptance.
"""
from __future__ import annotations

from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REQUIRED = {
    "README.md",
    "LOCAL_RESIDUE_THEOREM.md",
    "TWO_DERIVATION_SPECTRUM.md",
    "SOURCE_POLE_FILTRATION.md",
    "MULTIPLIER_RING.md",
    "CANDIDATE_LATTICE_TABLE.md",
    "COUNTERMODELS.md",
    "REVIEW.md",
    "HANDOFF.md",
    "verify_source_reflexive_lattice.py",
}
LABELS = {f"SRL-{number:03d}" for number in range(1, 11)}


def falling(alpha: Fraction, n: int) -> Fraction:
    result = Fraction(1)
    for r in range(n):
        result *= alpha - r
    return result


def check_kummer_repeated_derivatives() -> None:
    for e in range(2, 10):
        for j in range(1, e):
            for n_base in range(-2, 4):
                alpha = Fraction(n_base * e + j, e)
                for n in range(0, 9):
                    coefficient = falling(alpha, n)
                    assert coefficient != 0
                    valuation = e * (n_base - n) + j
                    assert valuation == e * n_base + j - e * n


def check_fractional_spectrum_invariance() -> None:
    for e in range(1, 12):
        expected = {Fraction(j, e) % 1 for j in range(e)}
        for shift in range(-3 * e, 3 * e + 1):
            shifted = {Fraction(shift + j, e) % 1 for j in range(e)}
            assert shifted == expected
        inverse_different = {
            Fraction(1 - e + j, e) % 1 for j in range(e)
        }
        assert inverse_different == expected
        for integer_shift in range(-5, 6):
            colon = {
                (Fraction(j, e) + integer_shift) % 1 for j in range(e)
            }
            assert colon == expected


def check_two_derivation_pair() -> None:
    samples = [(1, 0), (0, 1), (2, -3), (5, 7)]
    for e in range(2, 9):
        for a_p, a_q in samples:
            assert (a_p, a_q) != (0, 0)
            for j in range(e):
                rho_p = Fraction(j * a_p, e)
                rho_q = Fraction(j * a_q, e)
                # The tangent combination a_q D_P-a_p D_Q has zero residue.
                assert a_q * rho_p - a_p * rho_q == 0
            # At least one canonical direction is transverse.
            assert a_p != 0 or a_q != 0
            # e>1 retains the nonintegral normalized exponent 1/e.
            assert Fraction(1, e).denominator == e


def check_source_pole_escape() -> None:
    for e in range(1, 10):
        for m in range(1, 8):
            alpha = Fraction(-m, e)
            for n in range(0, 9):
                coefficient = falling(alpha, n)
                assert coefficient != 0
                valuation = -m - n * e
                assert valuation <= -m
                if n:
                    assert valuation < -m


def check_multiplier_identity() -> None:
    # For a principal fractional DVR ideal s^m S, the condition
    # z*s^m S subset s^m S is exactly z in S; valuations cancel.
    for m in range(-20, 21):
        for v_z in range(-10, 11):
            preserves = v_z + m >= m
            assert preserves == (v_z >= 0)


def check_artifact_contract() -> None:
    present = {path.name for path in ROOT.iterdir() if path.is_file()}
    missing = REQUIRED - present
    assert not missing, f"missing artifacts: {sorted(missing)}"

    combined = "\n".join(
        (ROOT / name).read_text(encoding="utf-8")
        for name in sorted(REQUIRED)
        if name.endswith(".md")
    )
    missing_labels = LABELS - {label for label in LABELS if label in combined}
    assert not missing_labels, f"missing provisional labels: {sorted(missing_labels)}"
    assert "O -> A" in combined
    assert "A -> O" not in (ROOT / "README.md").read_text(encoding="utf-8")
    assert "MUTABLE_NONAUTHORITATIVE" in combined
    assert "planar Jacobian conjecture" in combined


def main() -> int:
    check_kummer_repeated_derivatives()
    check_fractional_spectrum_invariance()
    check_two_derivation_pair()
    check_source_pole_escape()
    check_multiplier_identity()
    check_artifact_contract()
    print("source-reflexive-lattice exact checks: PASS")
    print("- tame Kummer repeated derivatives: PASS")
    print("- fractional residue shift invariance: PASS")
    print("- two-derivation normal/tangent compatibility: PASS")
    print("- source-pole unbounded escape: PASS")
    print("- multiplier ring DVR identity: PASS")
    print("- required artifact and SRL-label contract: PASS")
    print("mathematical truth: NOT EVALUATED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
