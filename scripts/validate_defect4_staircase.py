#!/usr/bin/env python3
"""Exact regression checks for the positive-weight defect-four audit.

This script is process evidence only.  The unbounded case proof is the Markdown
artifact in research/audits/defect-4-staircase-audit.md.
"""

from __future__ import annotations

import json
import math
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
x, y = sp.symbols("x y")
checks = 0


def jac(f: sp.Expr, g: sp.Expr) -> sp.Expr:
    return sp.expand(sp.diff(f, x) * sp.diff(g, y) - sp.diff(f, y) * sp.diff(g, x))


def require(condition: bool, message: str) -> None:
    global checks
    checks += 1
    if not condition:
        raise AssertionError(message)


def require_zero(expr: sp.Expr, message: str) -> None:
    require(sp.expand(expr) == 0, f"{message}: got {sp.expand(expr)}")


def require_equal(expr: sp.Expr, expected: sp.Expr, message: str) -> None:
    require_zero(sp.expand(expr - expected), message)


def monomials_of_weight(p: int, q: int, degree: int) -> list[tuple[int, int]]:
    if degree < 0:
        return []
    out: list[tuple[int, int]] = []
    for b in range(degree // q + 1):
        rest = degree - q * b
        if rest >= 0 and rest % p == 0:
            out.append((rest // p, b))
    return out


# 1. Chain-rule exponent bookkeeping.
dp, dq, p_sym, q_sym = sp.symbols("d_P d_Q p q", integer=True)
rees_exponent = (dp - p_sym) + (dq - q_sym)
require_equal(rees_exponent, dp + dq - p_sym - q_sym, "Rees exponent")
require((dp - p_sym) + (dq - q_sym) == (dp - q_sym) + (dq - p_sym),
        "both determinant products must have the same t exponent")

# 2. Jacobian signs and triangular target preservation.
P = x**3 + 2 * x * y + y
Q = x**2 - y**2 + 3 * y
z = sp.symbols("z")
h = z**4 - 2 * z
require_zero(jac(P, Q - h.subs(z, P)) - jac(P, Q), "target triangular Jacobian")
wrong_jac = sp.diff(P, x) * sp.diff(Q, y) + sp.diff(P, y) * sp.diff(Q, x)
require(sp.expand(wrong_jac - jac(P, Q)) != 0, "Jacobian sign mutation must be detected")

# 3. Defect-four central exceptional weight (1,2).
a, b, c, u, v, e, f = sp.symbols("a b c u v e f")
P0 = a * x**3
Q0 = b * x**4
P1 = u * x**2 + v * y
Q1 = e * x**3 + f * x * y
S1 = jac(P0, Q1) + jac(P1, Q0)
W = jac(P1, Q1)
S2 = jac(P0, c * y) + W + jac(x, Q0)
require_equal(S1, (3 * a * f - 4 * b * v) * x**3, "central (1,2) S1")
require_equal(W, (2 * u * f - 3 * v * e) * x**2 - v * f * y,
              "central (1,2) middle Wronskian")
require_equal(S2, (3 * a * c + 2 * u * f - 3 * v * e) * x**2 - v * f * y,
              "central (1,2) S2")
require(sp.Poly(S2, x, y).coeff_monomial(y) == -v * f,
        "central y coefficient must be -vf")

# A sign reversal of the middle Wronskian changes the decisive coefficients.
S2_mutated = jac(P0, c * y) - W + jac(x, Q0)
require(sp.expand(S2_mutated - S2) == sp.expand(-2 * W),
        "middle-Wronskian sign mutation must be detected")

# A central-only formal cancellation is rejected by the preceding stair.
formal_P0 = x**3
formal_Q0 = x**4
formal_P1 = y
formal_Q1 = x**3
formal_S0 = jac(formal_P0, formal_Q0)
formal_S1 = jac(formal_P0, formal_Q1) + jac(formal_P1, formal_Q0)
formal_S2 = jac(formal_P0, y) + jac(formal_P1, formal_Q1) + jac(x, formal_Q0)
require_zero(formal_S0, "central-only model S0")
require_zero(formal_S2, "central-only model S2")
require_equal(formal_S1, -4 * x**3, "preceding stair rejects central-only model")

# 4. Defect-four (3,1) exceptional weight (1,2).
P0_31 = a * x**4
Q0_31 = b * x**3
P1_31 = u * x**3 + v * x * y
r, s, g = sp.symbols("r s g")
P2_31 = r * x**2 + s * y
Q2_31 = g * x
S1_31 = jac(P0_31, c * y) + jac(P1_31, Q0_31)
S2_31 = jac(P0_31, Q2_31) + jac(P1_31, c * y) + jac(P2_31, Q0_31)
require_equal(S1_31, (4 * a * c - 3 * b * v) * x**3, "(3,1), weight (1,2), S1")
require_equal(S2_31, (-3 * b * s + 3 * c * u) * x**2 + c * v * y,
              "(3,1), weight (1,2), S2")

# 5. Equal-weight defect-three exceptional equations.
A, B, C, U, V, K = sp.symbols("A B C U V K")
H = U * x + V * y
Q1_12 = -2 * A * C * U**2 * x * y - A * C * U * V * y**2 + K * x**2
require_zero(jac(A * H**2, C * y) + jac(x, Q1_12), "kappa=3 (1,2) second stair")
E1_12 = sp.Poly(jac(A * H**2, Q1_12) + jac(x, B * H**3), x, y)
require(E1_12.coeff_monomial(y**2) == 3 * B * V**3,
        "kappa=3 (1,2) y^2 coefficient")
require(E1_12.coeff_monomial(x**2).subs(V, 0) == -4 * A**2 * C * U**4,
        "kappa=3 (1,2) residual x^2 coefficient")

P1_21 = -(B * V * U / C) * x**2 - (2 * B * V**2 / C) * x * y + K * y**2
require_zero(jac(P1_21, C * y) + jac(x, B * H**2), "kappa=3 (2,1) second stair")
E1_21 = sp.Poly(jac(A * H**3, C * y) + jac(P1_21, B * H**2), x, y)
require(E1_21.coeff_monomial(x**2) == 3 * A * C * U**3,
        "kappa=3 (2,1) x^2 coefficient")
require(sp.simplify(E1_21.coeff_monomial(y**2).subs(U, 0)) == -4 * B**2 * V**4 / C,
        "kappa=3 (2,1) residual y^2 coefficient")

# 6. Bounded support enumeration as an adversarial regression control.
primitive_pairs = 0
for p in range(1, 81):
    for q in range(p, 81):
        if math.gcd(p, q) != 1:
            continue
        primitive_pairs += 1

        # Central p>1: simultaneous P1 and Q1 support forces (2,3).
        if p > 1 and p < q:
            p1_nonzero = bool(monomials_of_weight(p, q, p + 1))
            q1_nonzero = bool(monomials_of_weight(p, q, q + 1))
            if p1_nonzero and q1_nonzero:
                require((p, q) == (2, 3),
                        f"unexpected central support pair {(p, q)}")

        # (1,3), p>1: P0 support forces q=p+1.
        if p > 1 and p < q and monomials_of_weight(p, q, p + 1):
            require(q == p + 1, f"unexpected (1,3) P0 support at {(p, q)}")

        # (3,1), p>1: pure-x top dependence requires p=3.
        if p > 1 and p < q and (q + 1) % p == 0 and (p + 3) % p == 0:
            require(p == 3, f"unexpected (3,1) pure-x pair {(p, q)}")

        # Top-common-factor compatibility after exponent-one descent is removed.
        for position in ((1, 3), (2, 2), (3, 1)):
            a_index, b_index = position
            alpha = p + a_index
            beta = q + b_index
            r = math.gcd(alpha, beta)
            exponent_one = alpha // r == 1 or beta // r == 1
            common_factor_supported = bool(monomials_of_weight(p, q, r))
            if not exponent_one and common_factor_supported:
                if position == (1, 3):
                    require(p == 1, f"unexpected no-descent (1,3) weight {(p, q)}")
                elif position == (2, 2):
                    require(p == 1, f"unexpected no-descent central weight {(p, q)}")
                else:
                    require(p in (1, 3), f"unexpected no-descent (3,1) weight {(p, q)}")
                    if p == 3:
                        require(q >= 8, f"unexpected small p=3 no-descent weight {(p, q)}")

        # Negative weighted degrees have no monomial support.
        require(not monomials_of_weight(p, q, -1), "negative weight piece must vanish")

# 7. Compensated source/target normalization keeps the resonant scalar.
alpha0, beta0, gamma0 = sp.symbols("alpha0 beta0 gamma0", nonzero=True)
A0 = alpha0 * x
B0 = beta0 * y + gamma0 * x**2
c0 = alpha0 * beta0
# The explicit inverse is x -> x/alpha0, y -> (y-gamma0*(x/alpha0)**2)/beta0.
phi_x = x / alpha0
phi_y = (y - gamma0 * (x / alpha0) ** 2) / beta0
require_equal(A0.subs({x: phi_x, y: phi_y}, simultaneous=True), x,
              "graded normalization first coordinate")
require_equal(B0.subs({x: phi_x, y: phi_y}, simultaneous=True), y,
              "graded normalization second coordinate")
require_equal(jac(phi_x, phi_y), 1 / c0, "inverse source Jacobian")
require_equal(c0 * jac(phi_x, phi_y), 1, "compensating target determinant")

# 8. Maintained artifact synchronization when run in the repository.
claims_path = ROOT / "research" / "claim_ledger.json"
graph_path = ROOT / "research" / "proof_graph.json"
if claims_path.exists() and graph_path.exists():
    claims = json.loads(claims_path.read_text())
    claim_by_id = {item["id"]: item for item in claims["claims"]}
    require(claim_by_id["CLM-049"]["status"] == "candidate_proved", "CLM-049 status")
    require(claim_by_id["CLM-050"]["status"] == "candidate_proved", "CLM-050 status")
    require(claim_by_id["CLM-051"]["status"] == "candidate_proved", "CLM-051 status")
    require(claim_by_id["CLM-052"]["status"] == "candidate_proved", "CLM-052 status")

    all_claim_ids = set(claim_by_id)
    for item in claims["claims"]:
        for dependency in item.get("depends_on", []):
            require(dependency in all_claim_ids,
                    f"claim {item['id']} missing dependency {dependency}")

    graph = json.loads(graph_path.read_text())
    node_by_id = {item["id"]: item for item in graph["nodes"]}
    require(node_by_id["OPEN-DEFECT-4"]["status"] == "candidate_proved",
            "OPEN-DEFECT-4 graph status")
    all_node_ids = set(node_by_id)
    for edge in graph["edges"]:
        require(edge["from"] in all_node_ids, f"missing graph source {edge['from']}")
        require(edge["to"] in all_node_ids, f"missing graph target {edge['to']}")
    require(len(graph["nodes"]) == 34, "proof graph node count")
    require(len(graph["edges"]) == 50, "proof graph edge count")

    required_paths = [
        ROOT / "research" / "audits" / "defect-4-staircase-audit.md",
        ROOT / "research" / "audits" / "defect-4-case-table.md",
        ROOT / "research" / "audits" / "filtered-transformation-catalogue.md",
        ROOT / "research" / "audits" / "defect-4-primary-source-audit.md",
    ]
    for path in required_paths:
        require(path.exists(), f"missing candidate artifact {path.relative_to(ROOT)}")

print(f"symbolic/support checks: {checks}")
print(f"primitive weights enumerated: {primitive_pairs}")
print("defect-four regression validation: PASS")
print("mathematical authority: NOT CONFERRED")
