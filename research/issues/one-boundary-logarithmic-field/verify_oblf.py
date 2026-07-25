#!/usr/bin/env python3
"""Exact symbolic controls for the one-boundary logarithmic-field packet.

These checks verify displayed algebraic identities only.  They do not validate
classification theorems, source bindings, or the planar Jacobian conjecture.
"""
from __future__ import annotations

import sympy as sp


P, Q, t, pi, s = sp.symbols("P Q t pi s", nonzero=True)


def assert_zero(expr: sp.Expr, label: str) -> None:
    value = sp.factor(sp.simplify(expr))
    if value != 0:
        raise AssertionError(f"{label}: expected zero, got {value}")


def check_saito_determinants() -> None:
    # Coordinate line g=P, with generators P*dP and dQ.
    g_line = P
    determinant_line = P * 1 - 0 * 0
    assert_zero(determinant_line - g_line, "coordinate-line determinant")

    # Polynomial graph g=P-Q^4.
    h = Q**4
    g_graph = P - h
    # Columns are delta_1=(g,0), delta_2=(h',1).
    determinant_graph = g_graph * 1 - sp.diff(h, Q) * 0
    assert_zero(determinant_graph - g_graph, "graph determinant")
    assert_zero(
        sp.diff(g_graph, P) * sp.diff(h, Q) + sp.diff(g_graph, Q),
        "graph tangency",
    )

    # Weighted cusp g=P^2-Q^3.
    g_cusp = P**2 - Q**3
    euler = (3 * P, 2 * Q)
    hamiltonian = (-3 * Q**2, -2 * P)
    determinant_cusp = euler[0] * hamiltonian[1] - euler[1] * hamiltonian[0]
    assert_zero(determinant_cusp + 6 * g_cusp, "cusp Saito determinant")
    assert_zero(
        euler[0] * sp.diff(g_cusp, P)
        + euler[1] * sp.diff(g_cusp, Q)
        - 6 * g_cusp,
        "cusp Euler weight",
    )
    assert_zero(
        hamiltonian[0] * sp.diff(g_cusp, P)
        + hamiltonian[1] * sp.diff(g_cusp, Q),
        "cusp Hamiltonian tangency",
    )


def check_cusp_conductor_field() -> None:
    # P=t^3, Q=t^2 for P^2-Q^3.  The conductor exponent is (2-1)(3-1)=2.
    p_t = t**3
    q_t = t**2
    delta_p = -3 * q_t**2
    delta_t = sp.cancel(delta_p / sp.diff(p_t, t))
    assert_zero(delta_t + t**2, "cusp Hamiltonian on normalization")

    euler_p = 3 * p_t
    euler_t = sp.cancel(euler_p / sp.diff(p_t, t))
    assert_zero(euler_t - t, "cusp Euler on normalization")


def check_cyclic_cover_lift() -> None:
    # For g=P^2-Q^3, E(g)=6g.  On s^5=g, set E(s)=6s/5.
    g = P**2 - Q**3
    relation = s**5 - g
    delta_relation = 5 * s**4 * (sp.Rational(6, 5) * s) - (
        3 * P * sp.diff(g, P) + 2 * Q * sp.diff(g, Q)
    )
    assert_zero(delta_relation - 6 * relation, "cyclic-cover lifted Euler field")


def check_leading_laurent_equations() -> None:
    m, n = sp.symbols("m n", positive=True, integer=True)
    A = sp.Function("A")(t)
    B = sp.Function("B")(t)
    x = A * pi ** (-m)
    y = B * pi ** (-n)

    wedge_coefficient = sp.diff(x, pi) * sp.diff(y, t) - sp.diff(x, t) * sp.diff(y, pi)
    expected = (n * sp.diff(A, t) * B - m * A * sp.diff(B, t)) * pi ** (
        -m - n - 1
    )
    assert_zero(wedge_coefficient - expected, "leading symplectic coefficient")

    ratio_derivative = sp.diff(A**n / B**m, t)
    factored_ratio = A ** (n - 1) * B ** (-m - 1) * (
        n * sp.diff(A, t) * B - m * A * sp.diff(B, t)
    )
    assert_zero(ratio_derivative - factored_ratio, "common-power ratio identity")

    h_lead = m * A * B / (m + n)
    radial_y_dx = sp.diff(x, pi) * y
    radial_dh = sp.diff(h_lead * pi ** (-(m + n)), pi)
    assert_zero(radial_y_dx - radial_dh, "leading primitive coefficient")


def main() -> int:
    check_saito_determinants()
    check_cusp_conductor_field()
    check_cyclic_cover_lift()
    check_leading_laurent_equations()
    print("OBLF symbolic identities: PASS")
    print("mathematical classification and source theorems: NOT EVALUATED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
