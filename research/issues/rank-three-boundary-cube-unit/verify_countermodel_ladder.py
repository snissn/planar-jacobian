#!/usr/bin/env python3
"""Exact controls for the no-unit countermodel boundary and a cubic rare-property audit model."""
from __future__ import annotations

import sympy as sp


def assert_zero(expr: sp.Expr, label: str) -> None:
    value = sp.factor(sp.expand(expr))
    if value != 0:
        raise AssertionError(f"{label}: expected 0, got {value}")


def main() -> int:
    # Existing issue #3 no-unit model: its displayed A^2 source is not etale.
    u, s = sp.symbols("u s")
    P = u
    Q = u * s**3 - s**2
    jac = sp.det(sp.Matrix([[sp.diff(P, u), sp.diff(P, s)], [sp.diff(Q, u), sp.diff(Q, s)]]))
    assert_zero(jac - s * (3 * u * s - 2), "issue #3 source Jacobian")

    # Fixed first-coordinate Keller repair forces the second coordinate to be affine in s.
    k = sp.symbols("k", nonzero=True)
    h0, h1, h2, h3 = sp.symbols("h0 h1 h2 h3")
    Hpoly = h0 + h1 * u + h2 * u**2 + h3 * u**3
    repaired_Q = k * s + Hpoly
    repaired_jac = sp.det(
        sp.Matrix([[sp.diff(P, u), sp.diff(P, s)], [sp.diff(repaired_Q, u), sp.diff(repaired_Q, s)]])
    )
    assert_zero(repaired_jac - k, "triangular constant-Jacobian repair")

    # Cubic rare-property audit model: x=s+v, y=s+2v, R=C(s^3,v).
    source_s, v = sp.symbols("source_s v")
    x_from_sv = source_s + v
    y_from_sv = source_s + 2 * v
    assert_zero(2 * x_from_sv - y_from_sv - source_s, "rare model inverse s")
    assert_zero(y_from_sv - x_from_sv - v, "rare model inverse v")

    # Re-express the polynomial base map in the independent source coordinates x,y.
    x, y = sp.symbols("x y")
    sigma = 2 * x - y
    base_v = y - x
    assert_zero((sigma + base_v) - x, "rare model inverse x")
    assert_zero((sigma + 2 * base_v) - y, "rare model inverse y")
    base_u = sigma**3
    rare_jac = sp.det(
        sp.Matrix([[sp.diff(base_u, x), sp.diff(base_u, y)], [sp.diff(base_v, x), sp.diff(base_v, y)]])
    )
    assert_zero(rare_jac - 3 * sigma**2, "cubic rare-model Jacobian")

    print("countermodel-ladder verification: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
