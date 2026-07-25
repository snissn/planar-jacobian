#!/usr/bin/env python3
"""Exact symbolic checks for the source-reflexive-lattice residue packet.

The checks are regression evidence for displayed formulas.  They do not prove
existence of a stable lattice or confer scientific authority.
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
    s = sp.symbols("s", nonzero=True)
    for e in range(2, 10):
        t = s**e
        D = lambda expr: sp.simplify(sp.diff(expr, s) / (e * s ** (e - 1)))
        for N in range(-2, 5):
            for j in range(1, e):
                expr = t**N * s**j
                current = expr
                coefficient = sp.Integer(1)
                for n in range(1, 7):
                    current = D(current)
                    coefficient *= sp.Rational(N * e + j, e) - (n - 1)
                    expected = sp.simplify(coefficient * t ** (N - n) * s**j)
                    require(
                        sp.simplify(current - expected) == 0,
                        f"Kummer iterate failed: e={e}, N={N}, j={j}, n={n}",
                    )

        residues = [sp.Rational(j, e) for j in range(e)]
        require(
            sp.simplify(sum(residues) - sp.Rational(e - 1, 2)) == 0,
            f"determinant residue sum failed: e={e}",
        )
        shifted = [sp.Mod(j + e, e) for j in range(e)]
        require(shifted == list(range(e)), f"integer shift changed classes: e={e}")

    P, Q = sp.symbols("P Q")
    examples = [P, Q, P**2 - Q**3, P * Q - 1, P**3 + P * Q + Q**2]
    for h in examples:
        hp, hq = sp.diff(h, P), sp.diff(h, Q)
        require(not (hp == 0 and hq == 0), f"gradient vanished identically: {h}")
        tangent = sp.expand(-hq * hp + hp * hq)
        require(tangent == 0, f"tangent combination failed: {h}")

    print("source-reflexive-lattice residue checks: PASS")
    print(f"exact assertions: {checks}")
    print("scientific authority: NOT INFERRED FROM CHECK COUNT")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
