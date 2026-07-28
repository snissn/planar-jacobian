#!/usr/bin/env python3
"""Exact binary-cubic, boundary-fiber, discriminant, and resolvent checks."""
from __future__ import annotations

import sympy as sp


def assert_zero(expr: sp.Expr, label: str) -> None:
    value = sp.factor(sp.expand(expr))
    if value != 0:
        raise AssertionError(f"{label}: expected 0, got {value}")


def assert_unit_ideal(polys: list[sp.Expr], vars_: tuple[sp.Symbol, ...], label: str) -> None:
    basis = sp.groebner(polys, *vars_, order="lex")
    remainder = basis.reduce(sp.Integer(1))[1]
    if remainder != 0:
        raise AssertionError(f"{label}: singularity ideal is not the unit ideal: {basis}")


def main() -> int:
    U, V, T = sp.symbols("U V T")
    a, b, c, d = sp.symbols("a b c d")
    f = a * U**3 + b * U**2 * V + c * U * V**2 + d * V**3

    # Standard binary-cubic discriminant, checked against the univariate cubic.
    delta = b**2 * c**2 - 4 * a * c**3 - 4 * b**3 * d - 27 * a**2 * d**2 + 18 * a * b * c * d
    assert_zero(sp.discriminant(f.subs({U: T, V: 1}), T) - delta, "binary discriminant")

    # GL_2 covariance: Disc(f o M) = det(M)^6 Disc(f).
    r, s, t, w = sp.symbols("r s t w")
    transformed = sp.expand(f.subs({U: r * U + s * V, V: t * U + w * V}, simultaneous=True))
    poly = sp.Poly(transformed, U, V)
    aa = poly.coeff_monomial(U**3)
    bb = poly.coeff_monomial(U**2 * V)
    cc = poly.coeff_monomial(U * V**2)
    dd = poly.coeff_monomial(V**3)
    delta_transformed = bb**2 * cc**2 - 4 * aa * cc**3 - 4 * bb**3 * dd - 27 * aa**2 * dd**2 + 18 * aa * bb * cc * dd
    assert_zero(delta_transformed - (r * w - s * t) ** 6 * delta, "GL2 discriminant covariance")

    # Split length-three special fiber: k^3.
    z1, z2, z3 = sp.symbols("z1 z2 z3")
    split_matrix = sp.Matrix([[1, z1, z1**2], [1, z2, z2**2], [1, z3, z3**2]])
    split_phi = (z2 - z1) * (z3 - z1) * (z3 - z2)
    assert_zero(split_matrix.det() - split_phi, "split Vandermonde")

    # Simple tame ramification: k[eps]/eps^2 x k.
    aa0, bb0, cc0 = sp.symbols("aa0 bb0 cc0")
    simple_matrix = sp.Matrix(
        [
            [1, aa0, aa0**2],
            [0, bb0, 2 * aa0 * bb0],
            [0, cc0 - aa0, cc0**2 - aa0**2],
        ]
    )
    simple_phi = bb0 * (cc0 - aa0) ** 2
    assert_zero(simple_matrix.det() - simple_phi, "simple-ramification index form")
    assert_zero(simple_phi.subs(cc0, -2 * aa0) - 9 * bb0 * aa0**2, "simple trace-zero form")

    # Total tame ramification: k[eps]/eps^3.
    aaa, bbb, ccc = sp.symbols("aaa bbb ccc")
    total_matrix = sp.Matrix(
        [
            [1, aaa, aaa**2],
            [0, bbb, 2 * aaa * bbb],
            [0, ccc, bbb**2 + 2 * aaa * ccc],
        ]
    )
    assert_zero(total_matrix.det() - bbb**3, "total-ramification index form")

    # The three geometric lambda-level fibers are smooth for lambda=1.
    split_level = U * V * (U + V) - 1
    simple_level = U * V**2 - 1
    total_level = U**3 - 1
    for label, level in (
        ("split lambda-level", split_level),
        ("simple lambda-level", simple_level),
        ("total lambda-level", total_level),
    ):
        assert_unit_ideal([level, sp.diff(level, U), sp.diff(level, V)], (U, V), label)

    # A Cardano quadratic resolvent: its discriminant is -Disc/27.
    p, q, Z = sp.symbols("p q Z")
    cubic_delta = sp.discriminant(T**3 + p * T + q, T)
    resolvent = Z**2 + q * Z - p**3 / 27
    assert_zero(sp.discriminant(resolvent, Z) + cubic_delta / 27, "quadratic resolvent discriminant")

    print("binary cubic and boundary-fiber verification: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
