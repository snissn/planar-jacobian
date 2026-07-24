#!/usr/bin/env python3
"""Exact regression checks for the issue #4 stable-order packet.

These checks verify displayed algebraic identities and bounded examples only.
They do not construct a stable order or confer mathematical authority.
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
    a, b, c, d = sp.symbols("a b c d")
    g11, g12, g22 = sp.symbols("g11 g12 g22")
    A = sp.Matrix([[a, b], [c, d]])
    G = sp.Matrix([[g11, g12], [g12, g22]])
    delta_G = A.T * G + G * A
    determinant = sp.expand(G.det())
    determinant_derivative = sp.expand(
        sp.diff(determinant, g11) * delta_G[0, 0]
        + sp.diff(determinant, g12) * delta_G[0, 1]
        + sp.diff(determinant, g22) * delta_G[1, 1]
    )
    require(
        sp.expand(determinant_derivative - 2 * sp.trace(A) * determinant) == 0,
        "trace-discriminant determinant identity failed",
    )

    u11, u12, u21, u22 = sp.symbols("u11 u12 u21 u22")
    U = sp.Matrix([[u11, u12], [u21, u22]])
    transformed = sp.expand((U.T * G * U).det())
    require(
        sp.expand(transformed - U.det() ** 2 * G.det()) == 0,
        "basis-change discriminant identity failed",
    )

    # Kummer escape formula D(t^N s)=(N+1/e)t^(N-1)s when t=s^e and D(t)=1.
    s = sp.symbols("s", nonzero=True)
    for e in range(2, 8):
        for N in range(0, 5):
            expr = s ** (e * N + 1)
            derivation = sp.diff(expr, s) / (e * s ** (e - 1))
            expected = sp.Rational(e * N + 1, e) * s ** (e * (N - 1) + 1)
            require(sp.simplify(derivation - expected) == 0, f"Kummer first derivative failed e={e}, N={N}")

            current = expr
            coefficient = sp.Integer(1)
            for n in range(1, 7):
                current = sp.simplify(sp.diff(current, s) / (e * s ** (e - 1)))
                coefficient *= sp.Rational(e * N + 1, e) - (n - 1)
                expected_n = sp.simplify(coefficient * s ** (e * (N - n) + 1))
                require(sp.simplify(current - expected_n) == 0, f"Kummer iterate failed e={e}, N={N}, n={n}")
                require(e * (N - n) + 1 == (e * N + 1) - n * e, "valuation escape arithmetic failed")

    # Minimal-degree control for bi-translation-stable ideals: a polynomial
    # annihilated by both partials in characteristic zero is constant.
    P, Q = sp.symbols("P Q")
    polynomial = 7 + 0 * P + 0 * Q
    require(sp.diff(polynomial, P) == 0 and sp.diff(polynomial, Q) == 0, "constant control failed")
    for sample in [P, Q, P * Q, P**3 + Q**2, (P + Q) ** 4]:
        require(
            sp.diff(sample, P) != 0 or sp.diff(sample, Q) != 0,
            f"nonconstant derivative control failed for {sample}",
        )

    print("issue #4 validation mode: algebraic-regression-evidence")
    print(f"exact assertions: {checks}")
    print("trace-discriminant identities: PASS")
    print("ramified-DVR escape formulas: PASS")
    print("stable order constructed: NO")
    print("mathematical authority: HUMAN-READABLE PACKET AND REVIEW, NOT CHECK COUNT")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
