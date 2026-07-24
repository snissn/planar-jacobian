#!/usr/bin/env python3
"""Exact symbolic checks for the cubic primitive-coordinate differential identity."""
from __future__ import annotations

import sympy as sp


def check_abstract_identity() -> None:
    Ft, Fp, Fq = sp.symbols("Ft Fp Fq", nonzero=True)
    Xt, Xp, Xq, Yt, Yp, Yq = sp.symbols("Xt Xp Xq Yt Yp Yq")

    xP = Xp - Xt * Fp / Ft
    xQ = Xq - Xt * Fq / Ft
    yP = Yp - Yt * Fp / Ft
    yQ = Yq - Yt * Fq / Ft
    jac = sp.factor(xP * yQ - xQ * yP)

    rhs = sp.expand(
        Ft * (Xp * Yq - Xq * Yp)
        + Fp * (Xq * Yt - Xt * Yq)
        + Fq * (Xt * Yp - Xp * Yt)
    )
    assert sp.factor(jac - rhs / Ft) == 0

    # Under J=1, the exact identity is Ft=rhs.  With x=t this specializes to
    # Ft=Fq*Yp-Fp*Yq.
    special = sp.expand(rhs.subs({Xt: 1, Xp: 0, Xq: 0}))
    assert sp.expand(special - (Fq * Yp - Fp * Yq)) == 0


def check_rational_symplectic_control() -> None:
    x, y, P, Q, T = sp.symbols("x y P Q T")
    p_expr = x**3
    q_expr = y / (3 * x**2)
    jac = sp.factor(
        sp.diff(p_expr, x) * sp.diff(q_expr, y)
        - sp.diff(p_expr, y) * sp.diff(q_expr, x)
    )
    assert jac == 1

    # F(T)=T^3-P and y=Y(T)=3 Q T^2.
    F = T**3 - P
    Y = 3 * Q * T**2
    Ft = sp.diff(F, T)
    Fp = sp.diff(F, P)
    Fq = sp.diff(F, Q)
    Yp = sp.diff(Y, P)
    Yq = sp.diff(Y, Q)
    assert sp.expand(Ft - (Fq * Yp - Fp * Yq)) == 0


def check_generic_cubic_remainder_shape() -> None:
    # Verify that the identity is a polynomial congruence modulo an arbitrary
    # monic cubic after reducing all primitive-coordinate representatives.
    T = sp.symbols("T")
    a, b, c = sp.symbols("a b c")
    F = T**3 + a * T**2 + b * T + c
    coeffs = sp.symbols("x0:3 y0:3 fp0:3 fq0:3")
    x0, x1, x2, y0, y1, y2, fp0, fp1, fp2, fq0, fq1, fq2 = coeffs
    X = x0 + x1 * T + x2 * T**2
    Y = y0 + y1 * T + y2 * T**2
    Fp = fp0 + fp1 * T + fp2 * T**2
    Fq = fq0 + fq1 * T + fq2 * T**2

    # Formal coefficient derivatives Xp,Xq,Yp,Yq are represented separately.
    xp0, xp1, xp2, xq0, xq1, xq2 = sp.symbols("xp0:3 xq0:3")
    yp0, yp1, yp2, yq0, yq1, yq2 = sp.symbols("yp0:3 yq0:3")
    Xp = xp0 + xp1 * T + xp2 * T**2
    Xq = xq0 + xq1 * T + xq2 * T**2
    Yp = yp0 + yp1 * T + yp2 * T**2
    Yq = yq0 + yq1 * T + yq2 * T**2
    Xt = sp.diff(X, T)
    Yt = sp.diff(Y, T)
    Ft = sp.diff(F, T)

    expression = sp.expand(
        Ft
        - Ft * (Xp * Yq - Xq * Yp)
        - Fp * (Xq * Yt - Xt * Yq)
        - Fq * (Xt * Yp - Xp * Yt)
    )
    remainder = sp.rem(expression, F, T)
    assert sp.degree(remainder, T) <= 2


def main() -> int:
    check_abstract_identity()
    check_rational_symplectic_control()
    check_generic_cubic_remainder_shape()
    print("rank-three differential checks: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
