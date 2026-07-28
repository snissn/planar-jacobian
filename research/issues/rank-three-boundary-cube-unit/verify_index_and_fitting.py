#!/usr/bin/env python3
"""Verify the rank-three index determinant, Fitting presentation, and index-square identity."""
from __future__ import annotations

import sympy as sp


def assert_zero(expr: sp.Expr, label: str) -> None:
    value = sp.factor(sp.expand(expr))
    if value != 0:
        raise AssertionError(f"{label}: expected 0, got {value}")


def main() -> int:
    p, q, X, Y = sp.symbols("p q X Y")

    # Algebra O = B[t]/(t^3+p t+q), represented in the basis 1,t,t^2.
    def multiply(lhs: sp.Matrix, rhs: sp.Matrix) -> sp.Matrix:
        coeff = [sp.Integer(0)] * 5
        for i in range(3):
            for j in range(3):
                coeff[i + j] += lhs[i] * rhs[j]
        # t^4 = -p t^2-q t and t^3=-p t-q.
        coeff[2] += -p * coeff[4]
        coeff[1] += -q * coeff[4]
        coeff[1] += -p * coeff[3]
        coeff[0] += -q * coeff[3]
        return sp.Matrix([sp.expand(coeff[0]), sp.expand(coeff[1]), sp.expand(coeff[2])])

    one = sp.Matrix([1, 0, 0])
    tvec = sp.Matrix([0, 1, 0])
    t2vec = sp.Matrix([0, 0, 1])
    e1 = tvec
    e2 = sp.Matrix([sp.Rational(2, 3) * p, 0, 1])  # trace zero
    section = X * e1 + Y * e2
    section2 = multiply(section, section)
    inclusion = sp.Matrix.hstack(one, section, section2)
    phi = sp.factor(inclusion.det())

    # Trace by the companion algebra's Newton sums.
    def trace(element: sp.Matrix) -> sp.Expr:
        return sp.expand(3 * element[0] - 2 * p * element[2])

    basis = [one, tvec, t2vec]
    gram_o = sp.Matrix([[trace(multiply(x, y)) for y in basis] for x in basis])
    power_basis = [one, section, section2]
    gram_s = sp.Matrix([[trace(multiply(x, y)) for y in power_basis] for x in power_basis])

    disc_o = sp.factor(gram_o.det())
    assert_zero(disc_o - (-4 * p**3 - 27 * q**2), "normal-basis discriminant")
    assert_zero(gram_s.det() - phi**2 * gram_o.det(), "index-square discriminant identity")

    # The square presentation B^3 --inclusion--> O has Fitt_0(coker)=det(inclusion).
    # Verify that the determinant is a genuine cubic and that t is a unit-index section.
    if sp.Poly(phi, X, Y).total_degree() != 3:
        raise AssertionError(f"index determinant is not cubic: {phi}")
    assert_zero(phi.subs({X: 1, Y: 0}) - 1, "monogenic coordinate direction")

    # Trace-free check for the selected frame.
    assert_zero(trace(e1), "trace(e1)")
    assert_zero(trace(e2), "trace(e2)")

    print("index, Fitting, and discriminant-square verification: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
