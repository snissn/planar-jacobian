#!/usr/bin/env python3
"""Exact checks for inertia cycles, localization growth, multiplier logic, and symplectic controls."""
from __future__ import annotations

import argparse
import json
from fractions import Fraction
from math import factorial

import sympy as sp


def cycle_classes(length: int) -> tuple[Fraction, ...]:
    """Return the fractional residue classes of one inertia cycle."""
    return tuple(Fraction(j, length) for j in range(length))


def verify_inertia(max_degree: int) -> dict[str, int]:
    """Check that ordinary coherence detects only trivial cycle partitions."""
    checks = 0
    for degree in range(1, max_degree + 1):
        for split in integer_partitions(degree):
            classes = tuple(c for e in split for c in cycle_classes(e))
            assert len(classes) == degree
            ordinary_coherent = all(c.denominator == 1 for c in classes)
            trivial_inertia = all(e == 1 for e in split)
            assert ordinary_coherent == trivial_inertia
            checks += 1
    return {"inertia_partition_checks": checks}


def integer_partitions(n: int, minimum: int = 1):
    """Yield nondecreasing integer partitions of ``n``."""
    if n == 0:
        yield ()
        return
    for first in range(minimum, n + 1):
        for rest in integer_partitions(n - first, first):
            yield (first,) + rest


def verify_localization(max_n: int) -> dict[str, int]:
    """Check repeated transverse derivatives of ordinary pole terms."""
    checks = 0
    for m in range(1, 6):
        for n in range(max_n + 1):
            coefficient = (-1) ** n
            for r in range(n):
                coefficient *= m + r
            expected = (-1) ** n * factorial(m + n - 1) // factorial(m - 1)
            assert coefficient == expected
            pole_order = m + n
            assert pole_order >= m
            checks += 1
    return {"localization_checks": checks}


def verify_multiplier_converse(max_degree: int) -> dict[str, int]:
    """Check the unstable-seed/stable-multiplier control M=P*B."""
    P, Q, b = sp.symbols("P Q b")
    checks = 0

    # M=P*B is not partial_P-stable because partial_P(P)=1 is not in (P).
    derivative = sp.diff(P, P)
    assert derivative == 1
    assert derivative.subs(P, 0) != 0
    checks += 2

    # In the domain B, zP=Pb implies z=b by cancellation, so (PB:PB)=B.
    assert sp.cancel(P * b / P) == b
    checks += 1

    # The multiplier B is stable under both target translations.
    for a in range(max_degree + 1):
        for c in range(max_degree + 1 - a):
            monomial = P**a * Q**c
            assert sp.diff(monomial, P).is_polynomial(P, Q)
            assert sp.diff(monomial, Q).is_polynomial(P, Q)
            checks += 2
    return {"multiplier_converse_checks": checks}


def verify_exact_symplectic(max_e: int) -> dict[str, int]:
    """Check the Laurent exact-symplectic countercontrol through ``max_e``."""
    x, y = sp.symbols("x y", nonzero=True)
    checks = 0
    for e in range(2, max_e + 1):
        P = x**e
        Q = y / (e * x ** (e - 1))
        jac = sp.simplify(
            sp.diff(P, x) * sp.diff(Q, y)
            - sp.diff(P, y) * sp.diff(Q, x)
        )
        assert jac == 1

        # Compare coefficients of x dy - P dQ and ((e-1)/e) d(xy).
        lhs_dx = sp.simplify(-P * sp.diff(Q, x))
        lhs_dy = sp.simplify(x - P * sp.diff(Q, y))
        rhs_dx = sp.Rational(e - 1, e) * y
        rhs_dy = sp.Rational(e - 1, e) * x
        assert sp.simplify(lhs_dx - rhs_dx) == 0
        assert sp.simplify(lhs_dy - rhs_dy) == 0
        checks += 3
    return {"exact_symplectic_checks": checks}


def main() -> int:
    """Parse bounds, run all exact checks, and print a stable report."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-degree", type=int, default=12)
    parser.add_argument("--max-n", type=int, default=12)
    parser.add_argument("--max-e", type=int, default=10)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    if args.max_degree < 1 or args.max_n < 1 or args.max_e < 2:
        raise SystemExit(
            "bounds must satisfy max-degree >= 1, max-n >= 1, and max-e >= 2"
        )

    result = {}
    result.update(verify_inertia(args.max_degree))
    result.update(verify_localization(args.max_n))
    result.update(verify_multiplier_converse(args.max_degree))
    result.update(verify_exact_symplectic(args.max_e))
    result["total_checks"] = sum(result.values())

    if args.json:
        print(json.dumps(result, sort_keys=True))
    else:
        print("global bridge validation: PASS")
        for key, value in sorted(result.items()):
            print(f"{key}: {value}")
        print("mathematical truth beyond encoded identities: NOT EVALUATED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
