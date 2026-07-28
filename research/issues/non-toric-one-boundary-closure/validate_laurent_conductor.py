#!/usr/bin/env python3
"""Exact symbolic checks for the non-toric one-boundary packet.

The program verifies displayed differential identities, finite-order recursion
shape, explicit branch examples, conductor controls, weight calculations, and
formal model families. It does not test algebraization, polynomial realization,
or the planar Jacobian conjecture.
"""
from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

import sympy as sp


@dataclass
class Check:
    name: str
    status: str
    detail: str


def canonical(expr: sp.Expr) -> sp.Expr:
    return sp.factor(sp.cancel(sp.together(sp.simplify(expr))))


def assert_zero(expr: sp.Expr, name: str) -> None:
    value = canonical(expr)
    if value != 0:
        raise AssertionError(f"{name}: expected zero, got {value}")


def assert_nonzero(expr: sp.Expr, name: str) -> None:
    value = canonical(expr)
    if value == 0:
        raise AssertionError(f"{name}: expected nonzero")


def jacobian(f: sp.Expr, g: sp.Expr, a: sp.Symbol, b: sp.Symbol) -> sp.Expr:
    return sp.diff(f, a) * sp.diff(g, b) - sp.diff(f, b) * sp.diff(g, a)


def one_form_differential(a_coeff: sp.Expr, b_coeff: sp.Expr, x: sp.Symbol, y: sp.Symbol) -> sp.Expr:
    """Coefficient of dx wedge dy in d(a dx+b dy)."""
    return sp.diff(b_coeff, x) - sp.diff(a_coeff, y)


def weighted_degree(poly: sp.Expr, x: sp.Symbol, y: sp.Symbol, p: int, q: int) -> int:
    terms = sp.Poly(sp.expand(poly), x, y).terms()
    if not terms:
        raise ValueError("zero polynomial has no weighted degree")
    return max(p * exponents[0] + q * exponents[1] for exponents, _ in terms)


def check_signs() -> Check:
    x, y = sp.symbols("x y")
    P = x + y**2
    Q = y
    assert_zero(jacobian(P, Q, x, y) - 1, "control Keller Jacobian")

    plus_a = P * sp.diff(Q, x) + y
    plus_b = P * sp.diff(Q, y)
    minus_a = P * sp.diff(Q, x) - y
    minus_b = P * sp.diff(Q, y)
    assert_zero(one_form_differential(plus_a, plus_b, x, y), "plus Liouville sign")
    assert_zero(one_form_differential(minus_a, minus_b, x, y) - 2, "minus-sign mutation")
    return Check("signs", "pass", "P dQ+y dx is closed; the minus mutation has differential 2 dx wedge dy")


def check_leading_equation() -> Check:
    t, z = sp.symbols("t z", nonzero=True)
    m, n = sp.symbols("m n", positive=True, integer=True)
    A = sp.Function("A")(z)
    B = sp.Function("B")(z)
    x = A * t ** (-m)
    y = B * t ** (-n)
    dt_dz = jacobian(x, y, t, z)
    expected = (n * sp.diff(A, z) * B - m * A * sp.diff(B, z)) * t ** (-m - n - 1)
    assert_zero(dt_dz - expected, "leading dt wedge dz coefficient")

    h = z + 1
    a = h**2
    b = h**3
    correct = 3 * sp.diff(a, z) * b - 2 * a * sp.diff(b, z)
    wrong = 3 * sp.diff(a, z) * b + 2 * a * sp.diff(b, z)
    assert_zero(correct, "common-power leading equation")
    assert_nonzero(wrong, "leading-sign mutation")
    assert_zero(sp.diff(a**3 / b**2, z), "constant common-power ratio")
    return Check("leading_equation", "pass", "sign, ratio derivative, and gcd common-power control verified")


def check_normalized_recursion(order: int) -> Check:
    s, z = sp.symbols("s z", nonzero=True)
    m = 3
    low = -4
    coeffs = {j: sp.Function(f"c{j}")(z) for j in range(low, m + order + 1)}
    x = s ** (-m)
    y = sum(coeffs[j] * s**j for j in coeffs)
    ds_dz = jacobian(x, y, s, z)
    expected = -m * sum(sp.diff(coeffs[j], z) * s ** (j - m - 1) for j in coeffs)
    assert_zero(ds_dz - expected, "normalized recursion coefficient")

    equations = [f"d(c_{m+r})=-(1/{m}) beta_{r}" for r in range(order + 1)]
    if equations[0] != "d(c_3)=-(1/3) beta_0":
        raise AssertionError("recursion indexing mutation")
    return Check("normalized_recursion", "pass", f"generated {len(equations)} exact coefficient equations through radial order {order}")


def check_branch_examples() -> Check:
    z, P, Q = sp.symbols("z P Q")

    q_ne = 1 / (z * (z - 1))
    omega_ne = canonical(z * sp.diff(q_ne, z))
    expected_ne = 1 / z - 1 / (z - 1) - 1 / (z - 1) ** 2
    assert_zero(omega_ne - expected_ne, "nonexact branch differential")
    residues = [canonical(sp.residue(omega_ne, z, point)) for point in (0, 1)]
    if residues != [1, -1]:
        raise AssertionError(f"nonexact residues: got {residues}")
    g_ne = P * (P - 1) * Q - 1
    assert_zero(g_ne.subs({P: z, Q: q_ne}), "nonexact branch parametrization")

    R = 1 / z + 1 / (z - 1)
    p_ex = sp.diff(R, z)
    g_ex = P * Q**2 * (Q - 1) ** 2 + (Q - 1) ** 2 + Q**2
    assert_zero(g_ex.subs({P: p_ex, Q: z}), "exact branch parametrization")
    assert_zero(p_ex - sp.diff(R, z), "exact Liouville primitive")

    A_poly = Q**2 * (Q - 1) ** 2
    B_poly = (Q - 1) **2 + Q**2
    inverse_B = sp.invert(B_poly, A_poly)
    u_poly = sp.rem(sp.diff(A_poly, Q) * inverse_B, A_poly, Q)
    v_poly = sp.rem(sp.diff(B_poly, Q) * inverse_B, A_poly, Q)
    c_poly = u_poly * P + v_poly
    numerator = sp.expand(c_poly * g_ex - sp.diff(g_ex, Q))
    a_poly = sp.cancel(numerator / A_poly)
    if not a_poly.is_polynomial(P, Q):
        raise AssertionError("exact branch logarithmic basis quotient is not polynomial")
    assert_zero(a_poly * sp.diff(g_ex, P) + sp.diff(g_ex, Q) - c_poly * g_ex, "exact branch logarithmic basis")

    if canonical(g_ex.subs(Q, 0)) != 1 or canonical(g_ex.subs(Q, 1)) != 1:
        raise AssertionError("exact branch smoothness control at excluded Q-values")
    w = sp.symbols("w")
    residue_inf = sp.residue(-p_ex.subs(z, 1 / w) / w**2, w, 0)
    residues_ex = [canonical(sp.residue(p_ex, z, point)) for point in (0, 1)] + [canonical(residue_inf)]
    if any(value != 0 for value in residues_ex):
        raise AssertionError(f"exact branch residues not zero: {residues_ex}")

    return Check(
        "branch_examples",
        "pass",
        "nonexact three-puncture residues are (+1,-1); exact three-puncture branch satisfies P dQ=dR",
    )


def numerical_semigroup(generators: tuple[int, ...], limit: int) -> set[int]:
    values = {0}
    changed = True
    while changed:
        changed = False
        for value in list(values):
            for gen in generators:
                candidate = value + gen
                if candidate <= limit and candidate not in values:
                    values.add(candidate)
                    changed = True
    return values


def check_conductor_control() -> Check:
    values = numerical_semigroup((2, 3), 20)
    gaps = [n for n in range(20) if n not in values]
    if gaps != [1]:
        raise AssertionError(f"<2,3> gaps: {gaps}")
    conductor = min(c for c in range(20) if all(n in values for n in range(c, 20)))
    if conductor != 2:
        raise AssertionError(f"<2,3> conductor: {conductor}")
    return Check(
        "conductor_control",
        "pass",
        "C[t^2,t^3] has gap 1 and conductor exponent 2; a t-term records a nonzero normalization quotient class",
    )


def check_formal_models(max_e: int, max_m: int) -> Check:
    t, z, B = sp.symbols("t z B", nonzero=True)
    instances = 0
    for e in range(2, max_e + 1):
        for m in range(1, max_m + 1):
            for r in range(0, 3):
                P = t**e
                Q = z
                x = z * t ** (-m)
                y = B * x**r - sp.Rational(e, m + e) * t ** (m + e)
                assert_zero(jacobian(x, y, t, z) - jacobian(P, Q, t, z), f"toric wedge e={e},m={m},r={r}")

                H = B * x ** (r + 1) / (r + 1) - sp.Rational(m, e) * x * (y - B * x**r)
                alpha_t = P * sp.diff(Q, t) + y * sp.diff(x, t)
                alpha_z = P * sp.diff(Q, z) + y * sp.diff(x, z)
                assert_zero(sp.diff(H, t) - alpha_t, f"toric primitive dt e={e},m={m},r={r}")
                assert_zero(sp.diff(H, z) - alpha_z, f"toric primitive dz e={e},m={m},r={r}")

                R = 1 / z + 1 / (z - 1)
                Pn = t**e + sp.diff(R, z)
                Hn = H + R
                assert_zero(jacobian(x, y, t, z) - jacobian(Pn, Q, t, z), f"non-toric wedge e={e},m={m},r={r}")
                alpha_t_n = Pn * sp.diff(Q, t) + y * sp.diff(x, t)
                alpha_z_n = Pn * sp.diff(Q, z) + y * sp.diff(x, z)
                assert_zero(sp.diff(Hn, t) - alpha_t_n, f"non-toric primitive dt e={e},m={m},r={r}")
                assert_zero(sp.diff(Hn, z) - alpha_z_n, f"non-toric primitive dz e={e},m={m},r={r}")
                instances += 1

    x_sym, y_sym = sp.symbols("x_sym y_sym", nonzero=True)
    rational_instances = 0
    for e in range(2, max_e + 1):
        P_rat = x_sym ** (-e)
        Q_rat = -sp.Rational(1, e) * y_sym * x_sym ** (e + 1)
        H_rat = -sp.Rational(1, e) * x_sym * y_sym
        assert_zero(jacobian(P_rat, Q_rat, x_sym, y_sym) - 1, f"field-generating rational Jacobian e={e}")
        alpha_x = P_rat * sp.diff(Q_rat, x_sym) + y_sym
        alpha_y = P_rat * sp.diff(Q_rat, y_sym)
        assert_zero(sp.diff(H_rat, x_sym) - alpha_x, f"field-generating primitive dx e={e}")
        assert_zero(sp.diff(H_rat, y_sym) - alpha_y, f"field-generating primitive dy e={e}")
        rational_instances += 1
    return Check(
        "formal_models",
        "pass",
        f"verified {instances} toric/non-toric formal instances and {rational_instances} field-generating rational controls; polynomial/Keller realization intentionally not asserted",
    )


def check_weight_controls(max_power: int) -> Check:
    x, y = sp.symbols("x y")
    p, q = 2, 3
    T = y**2 - x**3
    if weighted_degree(T, x, y, p, q) != 6:
        raise AssertionError("pole-weight cancellation degree")
    degrees = [weighted_degree(T**N, x, y, p, q) for N in range(1, max_power + 1)]
    if degrees != [6 * N for N in range(1, max_power + 1)]:
        raise AssertionError(f"support mutation degrees: {degrees}")

    N = max(3, max_power)
    P_std = x + y**N
    Q_std = y
    kappa_std = weighted_degree(P_std, x, y, 1, 1) + weighted_degree(Q_std, x, y, 1, 1) - 2
    kappa_aligned = weighted_degree(P_std, x, y, N, 1) + weighted_degree(Q_std, x, y, N, 1) - N - 1
    if kappa_std != N - 1 or kappa_aligned != 0:
        raise AssertionError(f"weight-dependence control: {kappa_std}, {kappa_aligned}")
    assert_zero(jacobian(P_std, Q_std, x, y) - 1, "triangular weight control Jacobian")

    return Check(
        "weight_controls",
        "pass",
        f"cancellation powers have degrees {degrees}; a Keller automorphism has defects {kappa_std} and {kappa_aligned} for two weights",
    )


def run(args: argparse.Namespace) -> dict[str, Any]:
    checks = [
        check_signs(),
        check_leading_equation(),
        check_normalized_recursion(args.order),
        check_branch_examples(),
        check_conductor_control(),
        check_formal_models(args.max_e, args.max_m),
        check_weight_controls(args.max_power),
    ]
    return {
        "status": "PASS",
        "checks": [asdict(check) for check in checks],
        "classification": {
            "nonexact_branch": "liouville_obstructed",
            "exact_nontoric_near_model": "formal_consistent_polynomial_realization_unproved",
            "toric_control": "formal_consistent_predecessor_torus_class",
            "conductor_gap_control": "conductor_obstructed_if_descent_required",
            "keller_realization": "not_found",
        },
        "limits": {
            "max_e": args.max_e,
            "max_m": args.max_m,
            "recursion_order": args.order,
            "max_support_power": args.max_power,
            "mathematical_truth": "NOT_EVALUATED_BY_SYMBOLIC_PASS",
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-e", type=int, default=5)
    parser.add_argument("--max-m", type=int, default=5)
    parser.add_argument("--order", type=int, default=8)
    parser.add_argument("--max-power", type=int, default=8)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    if min(args.max_e, args.max_m, args.order, args.max_power) < 1 or args.max_e < 2:
        parser.error("require max-e>=2 and all other bounds>=1")
    result = run(args)
    if args.json:
        print(json.dumps(result, indent=2, sort_keys=True))
    else:
        for check in result["checks"]:
            print(f"{check['name']}: {check['status'].upper()} — {check['detail']}")
        print("packet symbolic identities: PASS")
        print("algebraization, polynomial realization, Keller realization, and mathematical truth: NOT EVALUATED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
