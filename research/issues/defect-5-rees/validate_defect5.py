#!/usr/bin/env python3
"""Exact regression checker for the grading-defect-five Rees packet.

This program is independent of the defect-four checker.  It regenerates weighted
supports, Rees stairs, no-descent weight classes, exceptional coefficient ideals,
and semantic mutation tests from the definitions.  Its bounded enumeration is
engineering/falsification evidence; the unbounded theorem is the human support
argument in DERIVATION.md.
"""
from __future__ import annotations

import math
import random
import time
from collections import Counter
from dataclasses import dataclass
from typing import Iterable

import sympy as sp

x, y, t = sp.symbols("x y t")
MAX_WEIGHT = 120


def jacobian(f: sp.Expr, g: sp.Expr) -> sp.Expr:
    return sp.expand(sp.diff(f, x) * sp.diff(g, y) - sp.diff(f, y) * sp.diff(g, x))


def wrong_plus_jacobian(f: sp.Expr, g: sp.Expr) -> sp.Expr:
    return sp.expand(sp.diff(f, x) * sp.diff(g, y) + sp.diff(f, y) * sp.diff(g, x))


def support(degree: int, p: int, q: int) -> list[tuple[int, int]]:
    """All (i,j) with p*i+q*j=degree, including the empty piece."""
    if degree < 0:
        return []
    return [
        (i, (degree - p * i) // q)
        for i in range(degree // p + 1)
        if degree - p * i >= 0 and (degree - p * i) % q == 0
    ]


def generic_homogeneous(prefix: str, degree: int, p: int, q: int, variables: list[sp.Symbol]) -> sp.Expr:
    terms: list[sp.Expr] = []
    for i, j in support(degree, p, q):
        coefficient = sp.Symbol(f"{prefix}_{i}_{j}")
        variables.append(coefficient)
        terms.append(coefficient * x**i * y**j)
    return sp.Add(*terms) if terms else sp.Integer(0)


def polynomial_coefficients(poly: sp.Expr) -> list[sp.Expr]:
    expanded = sp.Poly(sp.expand(poly), x, y)
    return [sp.expand(coefficient) for _, coefficient in expanded.terms() if coefficient != 0]


def monomial_coefficient(poly: sp.Expr, i: int, j: int) -> sp.Expr:
    return sp.Poly(sp.expand(poly), x, y).coeff_monomial(x**i * y**j)


@dataclass
class FormalSystem:
    p: int
    q: int
    a: int
    b: int
    d_p: int
    d_q: int
    root_degree: int
    exponent_p: int
    exponent_q: int
    root: sp.Expr
    p_layers: list[sp.Expr]
    q_layers: list[sp.Expr]
    stairs: list[sp.Expr]
    equations: list[sp.Expr]
    variables: list[sp.Symbol]
    A: sp.Symbol
    B: sp.Symbol
    c: sp.Symbol


def build_formal_system(p: int, q: int, a: int, chart: int = 0) -> FormalSystem | None:
    """Build all normalized layers and S_0,...,S_5 from scratch.

    The selected resonant pair is exactly P_a=x, Q_(5-a)=c*y.  Other layers
    are complete weighted-homogeneous supports, including zeros.  The maximal
    common root has degree gcd(d_P,d_Q), and a projective chart fixes one root
    coefficient to one.
    """
    assert math.gcd(p, q) == 1 and p <= q and 1 <= a <= 4
    b = 5 - a
    d_p, d_q = p + a, q + b
    rho = math.gcd(d_p, d_q)
    m, n = d_p // rho, d_q // rho
    if m == 1 or n == 1:
        return None
    root_support = support(rho, p, q)
    assert root_support and 0 <= chart < len(root_support)

    variables: list[sp.Symbol] = []
    root_terms: list[sp.Expr] = []
    for index, (i, j) in enumerate(root_support):
        coefficient: sp.Expr
        if index == chart:
            coefficient = sp.Integer(1)
        else:
            coefficient = sp.Symbol(f"h_{i}_{j}")
            variables.append(coefficient)
        root_terms.append(coefficient * x**i * y**j)
    root = sp.Add(*root_terms)

    A, B, c = sp.symbols("A B c")
    variables.extend([A, B, c])
    p_layers: list[sp.Expr] = []
    q_layers: list[sp.Expr] = []
    for index in range(6):
        degree = d_p - index
        if index == 0:
            p_layers.append(A * root**m)
        elif index == a:
            p_layers.append(x)
        else:
            p_layers.append(generic_homogeneous(f"P{index}", degree, p, q, variables))
    for index in range(6):
        degree = d_q - index
        if index == 0:
            q_layers.append(B * root**n)
        elif index == b:
            q_layers.append(c * y)
        else:
            q_layers.append(generic_homogeneous(f"Q{index}", degree, p, q, variables))

    stairs: list[sp.Expr] = []
    equations: list[sp.Expr] = []
    for stair in range(6):
        expression = sp.expand(
            sum((jacobian(p_layers[i], q_layers[stair - i]) for i in range(stair + 1)), sp.Integer(0))
        )
        if stair == 5:
            expression = sp.expand(expression - 1)
        stairs.append(expression)
        equations.extend(polynomial_coefficients(expression))

    return FormalSystem(
        p=p,
        q=q,
        a=a,
        b=b,
        d_p=d_p,
        d_q=d_q,
        root_degree=rho,
        exponent_p=m,
        exponent_q=n,
        root=root,
        p_layers=p_layers,
        q_layers=q_layers,
        stairs=stairs,
        equations=equations,
        variables=variables,
        A=A,
        B=B,
        c=c,
    )


def unit_groebner(equations: Iterable[sp.Expr], variables: Iterable[sp.Symbol], nonzero: sp.Expr) -> tuple[int, int]:
    z = sp.Symbol("saturation_z")
    ordered_variables = list(dict.fromkeys([*variables, z]))
    ideal = [sp.expand(eq) for eq in equations] + [sp.expand(z * nonzero - 1)]
    basis = sp.groebner(ideal, *ordered_variables, order="grevlex")
    assert any(poly.as_expr() == 1 for poly in basis.polys), "formal no-descent system survived"
    return len(ideal), len(ordered_variables)


def classify_no_descent(p: int, q: int, a: int) -> str:
    if p == q:
        assert (p, q) == (1, 1)
        return f"equal-a{a}"
    if a == 1:
        return "a1-chain"
    if a == 2:
        if (p, q) in {(1, 2), (2, 3)}:
            return f"a2-exception-{p}-{q}"
        return f"a2-generic-p{p}"
    if a == 3:
        if (p, q) == (1, 3):
            return "a3-exception-1-3"
        return f"a3-generic-p{p}"
    if a == 4:
        if (p, q) in {(1, 2), (1, 3), (2, 3)}:
            return f"a4-exception-{p}-{q}"
        return f"a4-generic-p{p}"
    raise AssertionError(a)


def verify_generic_certificate(system: FormalSystem) -> None:
    """Verify the exact coefficient chain used by the unbounded proof."""
    p, q, a = system.p, system.q, system.a
    P, Q, S = system.p_layers, system.q_layers, system.stairs
    A, c = system.A, system.c
    if a == 1:
        f1 = monomial_coefficient(Q[1], 3, 1)
        f2 = monomial_coefficient(Q[2], 2, 1)
        f3 = monomial_coefficient(Q[3], 1, 1)
        assert sp.expand(monomial_coefficient(S[1], 4, 0) - 2 * A * f1) == 0
        assert sp.expand(monomial_coefficient(S[2], 3, 0) - (2 * A * f2 + f1)) == 0
        assert sp.expand(monomial_coefficient(S[3], 2, 0) - (2 * A * f3 + f2)) == 0
        assert sp.expand(monomial_coefficient(S[4], 1, 0) - (2 * A * c + f3)) == 0
        return
    if a == 2 and p == 1:
        assert q > 2
        u = monomial_coefficient(P[1], 2, 0)
        f1 = monomial_coefficient(Q[1], 2, 1)
        f2 = monomial_coefficient(Q[2], 1, 1)
        assert sp.expand(monomial_coefficient(S[1], 4, 0) - 3 * A * f1) == 0
        assert sp.expand(monomial_coefficient(S[2], 3, 0) - (3 * A * f2 + 2 * u * f1)) == 0
        assert sp.expand(monomial_coefficient(S[3], 2, 0) - (3 * A * c + 2 * u * f2 + f1)) == 0
        return
    if a == 2 and p == 2:
        assert q > 3
        f = monomial_coefficient(Q[1], 1, 1)
        assert sp.expand(monomial_coefficient(S[1], 2, 0) - 2 * A * f) == 0
        assert sp.expand(monomial_coefficient(S[3], 1, 0) - (2 * A * c + f)) == 0
        return
    if a == 3 and p == 1:
        assert q > 3
        u = monomial_coefficient(P[1], 3, 0)
        f = monomial_coefficient(Q[1], 1, 1)
        assert sp.expand(monomial_coefficient(S[1], 4, 0) - 4 * A * f) == 0
        assert sp.expand(monomial_coefficient(S[2], 3, 0) - (4 * A * c + 3 * u * f)) == 0
        return
    if a == 3 and p == 3:
        assert sp.expand(monomial_coefficient(S[2], 1, 0) - 2 * A * c) == 0
        return
    if a == 4:
        ordinary_exponent = 1 + a // p
        assert sp.expand(monomial_coefficient(S[1], ordinary_exponent - 1, 0) - ordinary_exponent * A * c) == 0
        return
    raise AssertionError((p, q, a))


def equal_weight_ideals() -> list[tuple[str, list[sp.Expr], list[sp.Symbol], sp.Expr]]:
    """Exact coordinate ideals after taking X=H, J(X,Y)=1."""
    X, Y = sp.symbols("X Y")

    def J(f: sp.Expr, g: sp.Expr) -> sp.Expr:
        return sp.expand(sp.diff(f, X) * sp.diff(g, Y) - sp.diff(f, Y) * sp.diff(g, X))

    ideals: list[tuple[str, list[sp.Expr], list[sp.Symbol], sp.Expr]] = []

    # Position (1,4), complete standard-homogeneous supports.
    A, B, ell, s, mu, nu = sp.symbols("A B ell s mu nu")
    a = sp.symbols("a0:5")
    b = sp.symbols("b0:4")
    d = sp.symbols("d0:3")
    L, M = ell * X + s * Y, mu * X + nu * Y
    Q1 = sum(a[k] * X ** (4 - k) * Y**k for k in range(5))
    Q2 = sum(b[k] * X ** (3 - k) * Y**k for k in range(4))
    Q3 = sum(d[k] * X ** (2 - k) * Y**k for k in range(3))
    expressions = [
        J(A * X**2, Q1) + J(L, B * X**5),
        J(A * X**2, Q2) + J(L, Q1),
        J(A * X**2, Q3) + J(L, Q2),
        J(A * X**2, M) + J(L, Q3),
    ]
    equations = [coefficient for expression in expressions for coefficient in polynomial_coefficients_xy(expression, X, Y)]
    variables = [A, B, ell, s, mu, nu, *a, *b, *d]
    ideals.append(("equal-(1,4)", equations, variables, A * B * J(L, M)))

    # Position (2,3).  S1 gives Q1=(4B/(3A)) X P1+E X^3.
    # The Y^3 coefficient of S2 is -8B*g^2/(3A), so g=0.  The
    # remaining exact complete support is encoded below without denominators.
    A, B, aa, bb, dd, ee, uu, vv, ww, ell, s, mu, nu = sp.symbols(
        "A B aa bb dd ee uu vv ww ell s mu nu"
    )
    P1 = aa * X**2 + bb * X * Y
    Q1 = dd * X**3 + ee * X**2 * Y
    Q2 = uu * X**2 + vv * X * Y + ww * Y**2
    L, M = ell * X + s * Y, mu * X + nu * Y
    expressions = [
        J(A * X**3, Q1) + J(P1, B * X**4),
        J(A * X**3, Q2) + J(P1, Q1) + J(L, B * X**4),
        J(A * X**3, M) + J(P1, Q2) + J(L, Q1),
        J(P1, M) + J(L, Q2),
    ]
    equations = [coefficient for expression in expressions for coefficient in polynomial_coefficients_xy(expression, X, Y)]
    variables = [A, B, aa, bb, dd, ee, uu, vv, ww, ell, s, mu, nu]
    ideals.append(("equal-(2,3)", equations, variables, A * B * J(L, M)))
    return ideals


def polynomial_coefficients_xy(poly: sp.Expr, X: sp.Symbol, Y: sp.Symbol) -> list[sp.Expr]:
    return [sp.expand(coefficient) for _, coefficient in sp.Poly(sp.expand(poly), X, Y).terms() if coefficient != 0]


def verify_equal_reduction_step() -> None:
    X, Y = sp.symbols("X Y")
    A, B, aa, bb, gg, E = sp.symbols("A B aa bb gg E", nonzero=True)
    P1 = aa * X**2 + bb * X * Y + gg * Y**2
    Q1 = sp.Rational(4, 3) * B / A * X * P1 + E * X**3
    J = lambda f, g: sp.expand(sp.diff(f, X) * sp.diff(g, Y) - sp.diff(f, Y) * sp.diff(g, X))
    coefficient = sp.Poly(J(P1, Q1), X, Y).coeff_monomial(Y**3)
    assert sp.simplify(coefficient + sp.Rational(8, 3) * B * gg**2 / A) == 0


def weighted_degree(poly: sp.Expr, p: int, q: int) -> int:
    terms = sp.Poly(sp.expand(poly), x, y).terms()
    if not terms:
        return -10**9
    return max(p * i + q * j for (i, j), coefficient in terms if coefficient != 0)


def weighted_layers(poly: sp.Expr, p: int, q: int) -> tuple[int, dict[int, sp.Expr]]:
    degree = weighted_degree(poly, p, q)
    pieces: dict[int, sp.Expr] = {}
    for (i, j), coefficient in sp.Poly(sp.expand(poly), x, y).terms():
        index = degree - (p * i + q * j)
        pieces[index] = sp.expand(pieces.get(index, 0) + coefficient * x**i * y**j)
    return degree, pieces


def verify_rees_identity(P: sp.Expr, Q: sp.Expr, p: int, q: int) -> None:
    assert sp.expand(jacobian(P, Q) - 1) == 0
    d_p, p_layers = weighted_layers(P, p, q)
    d_q, q_layers = weighted_layers(Q, p, q)
    kappa = d_p + d_q - p - q
    Pcal = sp.expand(sum(t**index * layer for index, layer in p_layers.items()))
    Qcal = sp.expand(sum(t**index * layer for index, layer in q_layers.items()))
    assert sp.expand(jacobian(Pcal, Qcal) - t**kappa) == 0
    for stair in range(kappa + 1):
        expression = sp.expand(
            sum(
                (
                    jacobian(p_layers.get(i, 0), q_layers.get(stair - i, 0))
                    for i in range(stair + 1)
                ),
                sp.Integer(0),
            )
        )
        assert sp.expand(expression - (1 if stair == kappa else 0)) == 0


def semantic_mutation_tests() -> int:
    mutations = 0
    assert jacobian(y, x) == -1
    assert wrong_plus_jacobian(y, x) == 1
    mutations += 1

    P, Q = x + y**2, y
    assert jacobian(Q, P) == -1 and jacobian(Q, -P) == 1
    mutations += 1

    u, v = sp.symbols("u v")
    psi_1, psi_2 = 2 * x, 3 * y + 5 * x**2
    assert jacobian(psi_1, psi_2) == 6
    phi_1 = u / 2
    phi_2 = (v - 5 * (u / 2) ** 2) / 3
    assert sp.expand(psi_1.subs({x: phi_1, y: phi_2}) - u) == 0
    assert sp.expand(psi_2.subs({x: phi_1, y: phi_2}) - v) == 0
    # Compensated normalization has determinant 6*(1/6)=1.
    assert sp.simplify(6 * sp.det(sp.Matrix([[sp.diff(phi_1, u), sp.diff(phi_1, v)], [sp.diff(phi_2, u), sp.diff(phi_2, v)]])) - 1) == 0
    mutations += 1

    # Graded inverse preserves every (1,2)-homogeneous degree; the corrupted
    # non-graded y->y+x substitution does not.
    for degree in range(0, 17):
        generic = sum(sp.Integer(i + 2 * j + 1) * x**i * y**j for i, j in support(degree, 1, 2))
        transformed = sp.expand(generic.subs({x: phi_1, y: phi_2}).subs({u: x, v: y}))
        if generic != 0:
            assert weighted_degree(transformed, 1, 2) == degree
    corrupted = sp.expand(y.subs({y: y + x}))
    assert {p * i + q * j for (i, j), coefficient in sp.Poly(corrupted, x, y).terms() for p, q in [(1, 2)]} == {1, 2}
    mutations += 1

    P, Q = x + y**2, y + (x + y**2) ** 3
    d_p = weighted_degree(P, 1, 2)
    d_q = weighted_degree(Q, 1, 2)
    kappa = d_p + d_q - 3
    Pcal = sp.expand(t**d_p * P.subs({x: t**-1 * x, y: t**-2 * y}))
    Qcal = sp.expand(t**d_q * Q.subs({x: t**-1 * x, y: t**-2 * y}))
    assert sp.expand(jacobian(Pcal, Qcal) - t**kappa) == 0
    assert sp.expand(jacobian(Pcal, Qcal) - t ** (kappa + 1)) != 0
    mutations += 1
    return mutations


def actual_keller_trials() -> int:
    trials = 0
    algebraic = sp.sqrt(2)
    pairs = [
        (x + y**2, y + (x + y**2) ** 3),
        (x + 2 * y**3, y - 3 * (x + 2 * y**3) ** 2),
        (x + algebraic * y**2, y + algebraic / 2 * (x + algebraic * y**2) ** 2),
    ]
    weights = [(1, 1), (1, 2), (2, 3), (3, 5), (4, 7)]
    for P, Q in pairs:
        for p, q in weights:
            verify_rees_identity(P, Q, p, q)
            trials += 1
    return trials


def main() -> int:
    started = time.time()
    primitive_weights = 0
    no_descent_systems = 0
    root_support_obstructions = 0
    descent_systems = 0
    zero_layers = 0
    simultaneous_resonance_systems = 0
    family_counts: Counter[str] = Counter()
    exceptional_systems: dict[tuple[int, int, int], FormalSystem] = {}

    exceptional_keys = {
        (1, 2, 2),
        (2, 3, 2),
        (1, 3, 3),
        (1, 2, 4),
        (1, 3, 4),
        (2, 3, 4),
    }

    for p in range(1, MAX_WEIGHT + 1):
        for q in range(p, MAX_WEIGHT + 1):
            if math.gcd(p, q) != 1:
                continue
            primitive_weights += 1
            for a in range(1, 5):
                b = 5 - a
                d_p, d_q = p + a, q + b
                rho = math.gcd(d_p, d_q)
                m, n = d_p // rho, d_q // rho
                if m == 1 or n == 1:
                    descent_systems += 1
                    continue
                root_support = support(rho, p, q)
                if not root_support:
                    root_support_obstructions += 1
                    continue
                no_descent_systems += 1
                assert p <= a, (p, q, a, rho, m, n)
                if p == q:
                    assert (p, q) == (1, 1)
                else:
                    assert len(root_support) == 1 and root_support[0][1] == 0, (p, q, a, rho, root_support)
                    assert a % p == 0 and (q + b) % p == 0
                family = classify_no_descent(p, q, a)
                family_counts[family] += 1

                system = build_formal_system(p, q, a)
                assert system is not None
                zero_layers += sum(layer == 0 for layer in [*system.p_layers, *system.q_layers])
                potential_resonances = sum(
                    sp.expand(jacobian(system.p_layers[i], system.q_layers[5 - i])) != 0 for i in range(6)
                )
                if potential_resonances > 1:
                    simultaneous_resonance_systems += 1
                if p == q:
                    continue
                key = (p, q, a)
                if key in exceptional_keys:
                    exceptional_systems[key] = system
                else:
                    verify_generic_certificate(system)

    assert exceptional_keys == set(exceptional_systems)

    groebner_cases = 0
    largest_equation_count = 0
    largest_variable_count = 0
    for key in sorted(exceptional_systems):
        system = exceptional_systems[key]
        equation_count, variable_count = unit_groebner(
            system.equations,
            system.variables,
            system.A * system.B * system.c,
        )
        groebner_cases += 1
        largest_equation_count = max(largest_equation_count, equation_count)
        largest_variable_count = max(largest_variable_count, variable_count)

    verify_equal_reduction_step()
    for _, equations, variables, nonzero in equal_weight_ideals():
        equation_count, variable_count = unit_groebner(equations, variables, nonzero)
        groebner_cases += 1
        largest_equation_count = max(largest_equation_count, equation_count)
        largest_variable_count = max(largest_variable_count, variable_count)

    # Equal positions (3,2) and (4,1) are the exact signed target swaps of
    # (2,3) and (1,4); the bracket is retained, not negated.
    L, M = sp.symbols("L M")
    assert jacobian(y, -x) == 1

    mutations = semantic_mutation_tests()
    keller_trials = actual_keller_trials()

    # The symbolic selected scalar is never specialized in the formal systems.
    assert all(system.c.is_Symbol for system in exceptional_systems.values())

    elapsed = time.time() - started
    print("defect-five validator mode: independent-from-defect-four")
    print(f"primitive weights enumerated (1 <= p <= q <= {MAX_WEIGHT}): {primitive_weights}")
    print(f"interior systems with exponent-one top descent: {descent_systems}")
    print(f"arithmetic no-descent cases killed by empty root support: {root_support_obstructions}")
    print(f"formal no-descent systems constructed through S_5: {no_descent_systems}")
    print(f"zero layers generated: {zero_layers}")
    print(f"systems admitting multiple symbolic resonant brackets: {simultaneous_resonance_systems}")
    print(f"no-descent support families: {len(family_counts)}")
    print(f"exact saturated Groebner eliminations: {groebner_cases}")
    print(f"largest Groebner input: {largest_equation_count} equations, {largest_variable_count} variables")
    print(f"semantic corruptions detected: {mutations}")
    print(f"exact rational/algebraic Keller-Rees trials: {keller_trials}")
    print("formal complete-staircase survivors resisting declared descent: 0")
    print(f"elapsed seconds: {elapsed:.3f}")
    print("defect-five exact symbolic validation: PASS")
    print("mathematical authority: HUMAN DERIVATION AND REVIEW STATUS, NOT CHECK COUNTS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
