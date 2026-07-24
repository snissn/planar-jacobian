#!/usr/bin/env python3
"""Exact symbolic checks for the rank-three intrinsic index cubic."""
from __future__ import annotations

import sympy as sp


def check_generic_binary_cubic() -> None:
    X, Y = sp.symbols("X Y")
    a1, a2, b1, b2, c1, c2 = sp.symbols("a1 a2 b1 b2 c1 c2")

    # Only the trace-free coordinates of s^2 enter 1 wedge s wedge s^2.
    s = sp.Matrix([X, Y])
    s2 = sp.Matrix([
        a1 * X**2 + 2 * b1 * X * Y + c1 * Y**2,
        a2 * X**2 + 2 * b2 * X * Y + c2 * Y**2,
    ])
    phi = sp.expand(sp.det(sp.Matrix.hstack(s, s2)))
    expected = sp.expand(
        a2 * X**3
        + (2 * b2 - a1) * X**2 * Y
        + (c2 - 2 * b1) * X * Y**2
        - c1 * Y**3
    )
    assert sp.expand(phi - expected) == 0

    # Over C, evaluations recover every coefficient.  Hence the ideal of all
    # integral values equals the coefficient/content ideal.
    A, B, C, D = sp.symbols("A B C D")
    f = A * X**3 + B * X**2 * Y + C * X * Y**2 + D * Y**3
    f10 = f.subs({X: 1, Y: 0})
    f01 = f.subs({X: 0, Y: 1})
    f11 = f.subs({X: 1, Y: 1})
    f1m = f.subs({X: 1, Y: -1})
    recovered_B = sp.expand((f11 - f1m - 2 * f01) / 2)
    recovered_C = sp.expand((f11 + f1m - 2 * f10) / 2)
    assert sp.expand(recovered_B - B) == 0
    assert sp.expand(recovered_C - C) == 0


def check_issue3_countermodel() -> None:
    u, v, X, Y, T = sp.symbols("u v X Y T")

    # Basis: (1,w,e).  Columns are multiplication by alpha=X*w+Y*e.
    m_alpha = sp.Matrix(
        [
            [0, -u * v * Y, -u * v * X - v * Y],
            [X, X, v * Y],
            [Y, -u * X, 0],
        ]
    )
    one = sp.Matrix([1, 0, 0])
    alpha = sp.Matrix([0, X, Y])
    alpha2 = sp.expand(m_alpha * alpha)
    power_matrix = sp.Matrix.hstack(one, alpha, alpha2)
    phi = sp.factor(power_matrix.det())
    expected_phi = -(u * X**3 + X**2 * Y + v * Y**3)
    assert sp.expand(phi - expected_phi) == 0

    # The coefficient ideal is the unit ideal because the X^2 Y coefficient is
    # 1, although the issue #3 proof shows that no value is a nonzero constant.
    assert sp.Poly(-expected_phi, X, Y).coeff_monomial(X**2 * Y) == 1

    # Trace Gram determinant from the multiplication table.
    gram = sp.Matrix([[3, 1, 0], [1, 1, -3 * u * v], [0, -3 * u * v, -2 * v]])
    disc_o = sp.factor(gram.det())
    assert sp.expand(disc_o + v * (4 + 27 * u**2 * v)) == 0

    # Characteristic polynomial of multiplication by alpha is the generic
    # minimal polynomial.  Its discriminant equals Phi(alpha)^2 Disc(O/B).
    charpoly = sp.Poly(m_alpha.charpoly(T).as_expr(), T)
    disc_power = sp.factor(sp.discriminant(charpoly.as_expr(), T))
    assert sp.factor(disc_power - phi**2 * disc_o) == 0


def main() -> int:
    check_generic_binary_cubic()
    check_issue3_countermodel()
    print("rank-three index checks: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
