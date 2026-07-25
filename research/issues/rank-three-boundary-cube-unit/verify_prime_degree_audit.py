#!/usr/bin/env python3
"""Falsification controls for the claimed rare-property degree-two classification."""
from __future__ import annotations

import sympy as sp


def reduced_mod_cyclotomic(expr: sp.Expr, zeta: sp.Symbol) -> sp.Expr:
    poly = sp.Poly(sp.expand(expr), zeta)
    modulus = sp.Poly(zeta**2 + zeta + 1, zeta)
    return sp.expand(poly.rem(modulus).as_expr())


def main() -> int:
    s, v, zeta = sp.symbols("s v zeta")
    x = s + v
    y = s + 2 * v

    # Exact bounded mutation control: no tested nonconstant monomial is fixed by s -> zeta*s.
    for i in range(0, 9):
        for j in range(0, 9):
            if i == 0 and j == 0:
                continue
            monomial = sp.expand(x**i * y**j)
            conjugate = sp.expand((zeta * s + v) ** i * (zeta * s + 2 * v) ** j)
            difference = reduced_mod_cyclotomic(conjugate - monomial, zeta)
            if difference == 0:
                raise AssertionError(f"unexpected invariant monomial at {(i, j)}")

    # Finite-field falsification control only: zeta=2 has order three in F_7.
    modulus = 7
    for i in range(0, 6):
        for j in range(0, 6):
            if i == 0 and j == 0:
                continue
            original = sp.Poly(sp.expand(x**i * y**j), s, v, modulus=modulus)
            conjugate = sp.Poly(sp.expand((2 * s + v) ** i * (2 * s + 2 * v) ** j), s, v, modulus=modulus)
            if original == conjugate:
                raise AssertionError(f"finite-field control became invariant at {(i, j)}")

    T, U = sp.symbols("T U")
    if sp.factor(T**3 - U) != T**3 - U:
        raise AssertionError("T^3-U unexpectedly factored symbolically")

    print("prime-degree literature-audit controls: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
