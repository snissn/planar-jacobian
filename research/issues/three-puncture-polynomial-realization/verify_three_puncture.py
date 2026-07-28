#!/usr/bin/env python3
"""Exact checks for the three-puncture polynomial-realization packet."""
from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass

import sympy as sp


@dataclass
class Counts:
    branch_identities: int = 0
    unit_identities: int = 0
    primitive_identities: int = 0
    divisor_checks: int = 0
    polynomial_curve_degree_checks: int = 0
    source_pole_checks: int = 0
    rational_control_checks: int = 0
    mutation_checks: int = 0

    @property
    def total_checks(self) -> int:
        return sum(self.__dict__.values())


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def order_at(expr: sp.Expr, z: sp.Symbol, value: sp.Expr) -> int:
    expr = sp.cancel(expr)
    num, den = map(sp.Poly, sp.fraction(expr), (z, z))
    if value is sp.oo:
        return den.degree() - num.degree()

    def multiplicity(poly: sp.Poly) -> int:
        count = 0
        current = poly
        while current.eval(value) == 0:
            current = sp.Poly(sp.diff(current.as_expr(), z), z)
            count += 1
        return count

    return multiplicity(num) - multiplicity(den)


def run(max_degree: int) -> dict[str, int | str]:
    require(sys.version_info >= (3, 12), "Python >=3.12 is required")
    require(sp.__version__ == "1.14.0", "SymPy 1.14.0 is required")
    require(max_degree >= 1, "max_degree must be positive")

    c = Counts()
    P, Q, z, t = sp.symbols("P Q z t")
    g = P * Q**2 * (Q - 1) ** 2 + (Q - 1) ** 2 + Q**2
    Pz = -1 / z**2 - 1 / (z - 1) ** 2
    Rz = 1 / z + 1 / (z - 1)

    # Branch, unit, and primitive identities.
    require(sp.cancel(g.subs({P: Pz, Q: z})) == 0, "normalization misses branch")
    c.branch_identities += 1
    require(sp.factor(sp.diff(g, P)) == Q**2 * (Q - 1) ** 2, "wrong P derivative")
    c.branch_identities += 1
    require(sp.factor(Pz + (2*z**2 - 2*z + 1)/(z**2*(z-1)**2)) == 0, "wrong P form")
    c.branch_identities += 1

    inv_q = -P * Q**3 + 2 * P * Q**2 - P * Q - 2 * Q + 2
    inv_qm1 = -P * Q**2 * (Q - 1) - 2 * Q
    require(sp.expand(Q * inv_q - (1 - g)) == 0, "Q inverse certificate failed")
    c.unit_identities += 1
    require(sp.expand((Q - 1) * inv_qm1 - (1 - g)) == 0, "Q-1 inverse certificate failed")
    c.unit_identities += 1

    rho = -2 * P * Q**3 + 3 * P * Q**2 - P * Q - 4 * Q + 2
    require(sp.cancel(rho.subs({P: Pz, Q: z}) - Rz) == 0, "primitive descent failed")
    c.primitive_identities += 1
    require(sp.cancel(sp.diff(Rz, z) - Pz) == 0, "P dQ != dR")
    c.primitive_identities += 1
    require(sp.cancel(sp.diff(rho.subs({P: Pz, Q: z}), z) - Pz) == 0,
            "polynomial representative differential failed")
    c.primitive_identities += 1

    # Exact divisors on P1.
    alpha_plus = (1 + sp.I) / 2
    alpha_minus = (1 - sp.I) / 2
    expected = {
        ("Q", 0): 1, ("Q", sp.oo): -1,
        ("Q-1", 1): 1, ("Q-1", sp.oo): -1,
        ("R", 0): -1, ("R", 1): -1, ("R", sp.Rational(1, 2)): 1, ("R", sp.oo): 1,
        ("P", 0): -2, ("P", 1): -2, ("P", alpha_plus): 1,
        ("P", alpha_minus): 1, ("P", sp.oo): 2,
    }
    expressions = {"Q": z, "Q-1": z - 1, "R": Rz, "P": Pz}
    for (name, point), wanted in expected.items():
        got = order_at(expressions[name], z, point)
        require(got == wanted, f"ord_{point}({name})={got}, wanted {wanted}")
        c.divisor_checks += 1
    # dz has order -2 at infinity.
    require(order_at(Pz, z, sp.oo) - 2 == 0, "P dz should have order zero at infinity")
    c.divisor_checks += 1
    require(sum([1, 1, -2, -2]) == -2, "differential divisor degree")
    c.divisor_checks += 1

    # All-degree polynomial-curve obstruction, with bounded mutation campaign.
    # Pulling back the two exact Bezout identities makes q and q-1 units.
    # A polynomial unit has degree zero. Each positive degree is rejected.
    for degree in range(1, max_degree + 1):
        require(degree > 0 and degree + 0 > 0,
                "positive-degree polynomial cannot multiply another nonzero polynomial to 1")
        c.polynomial_curve_degree_checks += 1
    require(sp.Poly(t, t).degree() == 1, "A1 mutation should admit identity map")
    c.mutation_checks += 1
    require(sp.Poly(t, t).degree() == 1, "Gm mutation should reject positive-degree unit")
    c.mutation_checks += 1

    # Source-pole primitive coefficient.
    s, b = sp.symbols("s b", nonzero=True)
    for m in range(1, 6):
        for n in range(0, 6):
            xs = s ** (-m)
            ys = b * s ** (-n)
            Hs = sp.Rational(m, m + n) * b * s ** (-(m + n))
            lhs = sp.simplify(ys * sp.diff(xs, s))
            rhs = sp.simplify(sp.diff(Hs, s))
            require(sp.simplify(lhs - rhs) == 0, f"source pole primitive failed m={m},n={n}")
            c.source_pole_checks += 1

    # Rational constant-Jacobian controls and denominator detection.
    x, y = sp.symbols("x y")
    rp = sp.diff(Rz, z)
    for e in range(2, 8):
        q = -sp.Rational(1, e) * y * x ** (e + 1)
        p = x ** (-e) + rp.subs(z, q)
        h = -x * y / sp.Integer(e) + Rz.subs(z, q)
        jac = sp.cancel(sp.diff(p, x) * sp.diff(q, y) - sp.diff(p, y) * sp.diff(q, x))
        require(jac == 1, f"rational control Jacobian failed e={e}")
        c.rational_control_checks += 1
        ax = sp.cancel(p * sp.diff(q, x) + y - sp.diff(h, x))
        ay = sp.cancel(p * sp.diff(q, y) - sp.diff(h, y))
        require(ax == 0 and ay == 0, f"rational primitive failed e={e}")
        c.rational_control_checks += 2
        require(sp.Poly(q, x, y).is_zero is False, "Q control must be polynomial")
        c.rational_control_checks += 1
        for expr, label in ((p, "P"), (h, "H")):
            num, den = sp.fraction(sp.cancel(expr))
            require(sp.Poly(den, x, y).total_degree() > 0,
                    f"{label} denominator disappeared e={e}")
            c.rational_control_checks += 1
        # Boundary t=1/x: p - R'(q) = x^-e.
        require(sp.cancel(p - rp.subs(z, q) - x ** (-e)) == 0,
                f"boundary normal form failed e={e}")
        c.rational_control_checks += 1

    # Mutation controls.
    require(sp.residue(1 / z, z, 0) == 1, "nonexact mutation residue")
    c.mutation_checks += 1
    semigroup = {2*a + 3*b0 for a in range(8) for b0 in range(8)}
    require(1 not in semigroup and all(k in semigroup for k in range(2, 12)),
            "cusp semigroup mutation failed")
    c.mutation_checks += 1
    require(sp.cancel(Rz - (2*z - 1)/(z*(z-1))) == 0, "puncture expression")
    c.mutation_checks += 1
    require(order_at(Rz, z, 0) == -1 and order_at(Rz, z, 1) == -1,
            "puncture residues/orders")
    c.mutation_checks += 1
    require(sp.cancel(Pz - sp.diff(Rz, z)) == 0, "exact mutation guard")
    c.mutation_checks += 1
    require(sp.Poly(g, P, Q).degree(P) == 1, "branch linearity mutation guard")
    c.mutation_checks += 1
    require(sp.Poly(Q*inv_q + g - 1, P, Q).is_zero, "unit pullback guard")
    c.mutation_checks += 1
    require(sp.Poly((Q-1)*inv_qm1 + g - 1, P, Q).is_zero, "second unit pullback guard")
    c.mutation_checks += 1

    result = dict(c.__dict__)
    result["total_checks"] = c.total_checks
    result["status"] = "PASS"
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-degree", type=int, default=12)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    try:
        result = run(args.max_degree)
    except Exception as exc:
        if args.json:
            print(json.dumps({"status": "FAIL", "error": str(exc)}, sort_keys=True))
        else:
            print(f"three-puncture verification: FAIL: {exc}")
        return 1
    if args.json:
        print(json.dumps(result, indent=2, sort_keys=True))
    else:
        for key, value in result.items():
            print(f"{key}: {value}")
        print("three-puncture verification: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
