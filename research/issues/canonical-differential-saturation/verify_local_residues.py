#!/usr/bin/env python3
"""Exact arithmetic checks for the local residue and escape formulas."""
from __future__ import annotations

import argparse
import json
from fractions import Fraction

import sympy as sp


def falling(alpha: Fraction, n: int) -> Fraction:
    """Return the falling factorial alpha(alpha-1)...(alpha-n+1)."""
    value = Fraction(1)
    for r in range(n):
        value *= alpha - r
    return value


def verify_kummer(max_e: int, max_n: int) -> dict[str, int]:
    """Check residue classes, lattice shifts, and repeated derivatives."""
    checks = 0
    twist_checks = 0
    for e in range(2, max_e + 1):
        classes = {Fraction(j, e) % 1 for j in range(e)}
        assert len(classes) == e
        assert Fraction(0) in classes
        for shift in range(-4, 5):
            shifted = {(Fraction(j, e) + shift) % 1 for j in range(e)}
            assert shifted == classes
            checks += 1
        # Multiplication by s^k may permute tame characters rather than
        # shift every fixed eigenspace by one common integer.
        for parameter_shift in range(-2 * e, 2 * e + 1):
            twisted = {
                Fraction(j + parameter_shift, e) % 1 for j in range(e)
            }
            assert twisted == classes
            twist_checks += 1
        for j in range(1, e):
            for N in range(-3, 4):
                alpha = Fraction(N * e + j, e)
                for n in range(1, max_n + 1):
                    coeff = falling(alpha, n)
                    assert coeff != 0
                    valuation = alpha - n
                    assert valuation == Fraction(N * e + j, e) - n
                    checks += 1
        determinant_residue = sum((Fraction(j, e) for j in range(e)), Fraction())
        assert determinant_residue == Fraction(e - 1, 2)
        if e % 2 == 1:
            assert determinant_residue.denominator == 1
            assert any(Fraction(j, e).denominator != 1 for j in range(1, e))
        checks += 1
    return {"kummer_checks": checks, "fractional_twist_checks": twist_checks}


def verify_pair_spectrum(max_e: int) -> dict[str, int]:
    """Check the normal/tangent change of frame for both derivations."""
    checks = 0
    hp, hq, a, b = sp.symbols("hp hq a b")
    constraint = a * hp + b * hq - 1
    normal_frame_ideal = sp.groebner(
        [constraint], a, b, hp, hq, order="lex", domain=sp.QQ
    )
    for e in range(2, max_e + 1):
        for j in range(e):
            r = sp.Rational(j, e)
            normal = sp.expand(r * (a * hp + b * hq))
            tangent = sp.expand(r * (-hq * hp + hp * hq))
            assert tangent == 0
            # The normal coefficient equals r on the locus
            # a*hp+b*hq=1; reduce modulo that defining relation.
            _, remainder = normal_frame_ideal.reduce(normal - r)
            assert remainder == 0
            checks += 1
    return {"pair_spectrum_checks": checks}


def verify_non_galois_cubic() -> dict[str, int]:
    """Check the discriminant and ramified local equation of the cubic control."""
    z, t, s, tau = sp.symbols("z t s tau")
    polynomial = z**3 - 3 * z - t
    discriminant = sp.discriminant(polynomial, z)
    assert sp.expand(discriminant) == 27 * (4 - t**2)
    local = sp.expand(polynomial.subs({z: -1 + s, t: 2 + tau}))
    assert sp.expand(local - (s**3 - 3 * s**2 - tau)) == 0
    # tau = s^2(s-3), hence dt/ds = 3s(s-2).
    assert sp.simplify(sp.diff(s**2 * (s - 3), s) - 3 * s * (s - 2)) == 0
    return {"non_galois_checks": 3}


def main() -> int:
    """Parse bounds, run all exact checks, and print a stable report."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-e", type=int, default=12)
    parser.add_argument("--max-n", type=int, default=16)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    if args.max_e < 2 or args.max_n < 1:
        raise SystemExit("bounds must satisfy max-e >= 2 and max-n >= 1")

    result = {}
    result.update(verify_kummer(args.max_e, args.max_n))
    result.update(verify_pair_spectrum(args.max_e))
    result.update(verify_non_galois_cubic())
    result["total_checks"] = sum(result.values())

    if args.json:
        print(json.dumps(result, sort_keys=True))
    else:
        print("local residue validation: PASS")
        for key, value in sorted(result.items()):
            print(f"{key}: {value}")
        print("mathematical truth beyond encoded identities: NOT EVALUATED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
