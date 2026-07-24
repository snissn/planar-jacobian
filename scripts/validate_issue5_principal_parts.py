#!/usr/bin/env python3
"""Exact regression checks for the issue #5 principal-parts packet.

These checks exercise displayed examples and obstructions only. They do not
prove the Keller branch radial or produce an algebraic group action.
"""
from __future__ import annotations

import sympy as sp

checks = 0


def require(condition: bool, message: str) -> None:
    global checks
    checks += 1
    if not condition:
        raise AssertionError(message)


def main() -> int:
    P, Q, pi = sp.symbols("P Q pi", nonzero=True)

    # Exact Laurent primitives can have zero logarithmic residue and higher poles.
    for m in range(1, 9):
        derivative = sp.diff(pi ** (-m), pi)
        require(sp.expand(derivative + m * pi ** (-m - 1)) == 0, f"Laurent derivative failed m={m}")
        require(-m - 1 != -1, f"unexpected logarithmic term m={m}")

    def apply_field(a: sp.Expr, b: sp.Expr, f: sp.Expr) -> sp.Expr:
        return sp.expand(a * sp.diff(f, P) + b * sp.diff(f, Q))

    # Standard radial field: radial line tangent, translated line not tangent.
    radial_a, radial_b = P, Q
    require(sp.rem(apply_field(radial_a, radial_b, P), P, P) == 0, "radial line tangency failed")
    shift = sp.symbols("shift", nonzero=True)
    translated = P - shift
    translated_remainder = sp.expand(apply_field(radial_a, radial_b, translated).subs(P, shift))
    require(translated_remainder == shift, "translated-line obstruction failed")

    # Cusp: standard radial field is not logarithmic, weighted Euler field is.
    cusp = P**2 - Q**3
    standard = apply_field(P, Q, cusp)
    standard_on_cusp = sp.expand(standard.subs(P**2, Q**3))
    require(standard_on_cusp == -Q**3, "standard radial cusp remainder failed")
    weighted = apply_field(3 * P, 2 * Q, cusp)
    require(sp.expand(weighted - 6 * cusp) == 0, "weighted cusp tangency failed")

    # Branch Hamiltonian is tangent but not locally finite on the cusp normalization.
    ham_a = sp.diff(cusp, Q)
    ham_b = -sp.diff(cusp, P)
    require(apply_field(ham_a, ham_b, cusp) == 0, "Hamiltonian tangency failed")
    t = sp.symbols("t")
    induced_from_P = sp.simplify(ham_a.subs({P: t**3, Q: t**2}) / sp.diff(t**3, t))
    induced_from_Q = sp.simplify(ham_b.subs({P: t**3, Q: t**2}) / sp.diff(t**2, t))
    require(induced_from_P == -t**2 and induced_from_Q == -t**2, "cusp normalization field failed")
    current = t
    for n in range(1, 9):
        current = sp.expand(-t**2 * sp.diff(current, t))
        expected = (-1) ** n * sp.factorial(n) * t ** (n + 1)
        require(sp.expand(current - expected) == 0, f"non-local-finiteness iterate failed n={n}")

    # No nonzero affine-linear field is tangent to P, P-Q^2, and P-Q^3 simultaneously.
    a0, a1, a2, b0, b1, b2 = sp.symbols("a0 a1 a2 b0 b1 b2")
    A = a0 + a1 * P + a2 * Q
    B = b0 + b1 * P + b2 * Q
    equations = [a0, a2]  # tangency to P=0
    for power in [2, 3]:
        restriction = sp.Poly(sp.expand((A - power * Q ** (power - 1) * B).subs(P, Q**power)), Q)
        equations.extend(restriction.all_coeffs())
    solution = sp.linsolve(equations, [a0, a1, a2, b0, b1, b2])
    require(solution == {(0, 0, 0, 0, 0, 0)}, f"affine compatibility obstruction failed: {solution}")

    print("issue #5 validation mode: principal-part-regression-evidence")
    print(f"exact assertions: {checks}")
    print("Laurent residue/higher-pole control: PASS")
    print("radial and logarithmic tangency examples: PASS")
    print("regularity-to-integration countercontrol: PASS")
    print("Keller branch proved radial: NO")
    print("algebraic action constructed: NO")
    print("mathematical authority: HUMAN-READABLE PACKET AND REVIEW, NOT CHECK COUNT")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
