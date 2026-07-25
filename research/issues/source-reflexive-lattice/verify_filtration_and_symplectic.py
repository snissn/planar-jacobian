#!/usr/bin/env python3
"""Verify pole-shift and exact-symplectic countercontrol formulas."""
from __future__ import annotations

import sympy as sp

checks = 0


def require(condition: bool, message: str) -> None:
    global checks
    checks += 1
    if not condition:
        raise AssertionError(message)


def main() -> int:
    x, y = sp.symbols("x y", nonzero=True)
    for e in range(2, 9):
        P = x**e
        Q = y / (e * x ** (e - 1))
        jac = sp.simplify(sp.diff(P, x) * sp.diff(Q, y) - sp.diff(P, y) * sp.diff(Q, x))
        require(jac == 1, f"Laurent Keller Jacobian failed: e={e}")

        # Coefficients of dx and dy in x dy - P dQ.
        coeff_dx = sp.simplify(-P * sp.diff(Q, x))
        coeff_dy = sp.simplify(x - P * sp.diff(Q, y))
        target_dx = sp.Rational(e - 1, e) * y
        target_dy = sp.Rational(e - 1, e) * x
        require(sp.simplify(coeff_dx - target_dx) == 0, f"primitive dx failed: e={e}")
        require(sp.simplify(coeff_dy - target_dy) == 0, f"primitive dy failed: e={e}")

        s = sp.symbols(f"s{e}", nonzero=True)
        t = s**e
        D = lambda expr: sp.simplify(sp.diff(expr, s) / (e * s ** (e - 1)))
        for m in range(1, 6):
            actual = D(s ** (-m))
            expected = -sp.Rational(m, e) * s ** (-m - e)
            require(sp.simplify(actual - expected) == 0, f"ramified pole shift failed: e={e}, m={m}")

    t, u = sp.symbols("t u", nonzero=True)
    for m in range(1, 8):
        require(sp.diff(t ** (-m), t) == -m * t ** (-m - 1), f"unramified shift failed: m={m}")
        require(sp.simplify(t * sp.diff(t ** (-m), t) + m * t ** (-m)) == 0, f"log stability failed: m={m}")

    print("source-reflexive-lattice filtration/symplectic checks: PASS")
    print(f"exact assertions: {checks}")
    print("planar polynomial Keller counterexample constructed: NO")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
