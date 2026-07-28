#!/usr/bin/env python3
"""Verify the boundary-adapted affine-family identity and moving-collision expansion."""
from __future__ import annotations

import sympy as sp


def assert_zero(expr: sp.Expr, label: str) -> None:
    value = sp.factor(sp.expand(expr))
    if value != 0:
        raise AssertionError(f"{label}: expected 0, got {value}")


def assert_divisible_in_H(coefficient: sp.Expr, H: sp.Symbol, exponent: int, label: str) -> None:
    """Require polynomial divisibility by H**exponent, without rational cancellation."""
    dividend = sp.Poly(sp.expand(coefficient), H, domain=sp.EX)
    divisor = sp.Poly(H**exponent, H, domain=sp.EX)
    quotient, remainder = dividend.div(divisor)
    if not remainder.is_zero:
        raise AssertionError(
            f"{label}: expected divisibility by H^{exponent}, remainder={remainder.as_expr()}"
        )
    assert_zero(
        coefficient - H**exponent * quotient.as_expr(),
        f"{label} reconstruction",
    )


def main() -> int:
    U, V, T, H = sp.symbols("U V T H")
    a, b, c, d = sp.symbols("a b c d")
    u0, v0, u1, v1 = sp.symbols("u0 v0 u1 v1")
    f = a * U**3 + b * U**2 * V + c * U * V**2 + d * V**3

    theta = {U: u0, V: v0}
    eta_u, eta_v = u1, v1
    family = sp.expand(f.subs({U: u0 + H * T * u1, V: v0 + H * T * v1}))
    D = sp.expand(f.subs(theta))
    directional = eta_u * sp.diff(f, U) + eta_v * sp.diff(f, V)
    C = sp.expand(directional.subs(theta))
    B2 = sp.expand(
        (eta_u * sp.diff(directional, U) + eta_v * sp.diff(directional, V)).subs(theta)
        / 2
    )
    A = sp.expand(f.subs({U: u1, V: v1}))
    expected = D + H * T * C + H**2 * T**2 * B2 + H**3 * T**3 * A
    assert_zero(family - expected, "boundary-adapted cubic expansion")
    assert_zero(sp.rem(family - D, H), "congruence modulo H")

    # On a split etale chart, the same family is the product of three affine sheet differences.
    z1, z2, z3, w1, w2, w3 = sp.symbols("z1 z2 z3 w1 w2 w3")
    vandermonde_family = sp.prod(
        [
            (z2 - z1) + H * T * (w2 - w1),
            (z3 - z1) + H * T * (w3 - w1),
            (z3 - z2) + H * T * (w3 - w2),
        ]
    )
    vandermonde_constant = (z2 - z1) * (z3 - z1) * (z3 - z2)
    poly_t = sp.Poly(sp.expand(vandermonde_family), T)
    if poly_t.degree() != 3:
        raise AssertionError("moving-collision Vandermonde is not cubic in T")
    for exponent in range(1, 4):
        coefficient = poly_t.coeff_monomial(T**exponent)
        assert_divisible_in_H(
            coefficient,
            H,
            exponent,
            f"H^{exponent} divisibility",
        )

        # Falsification control: a coefficient with a nonzero H-adic remainder must fail.
        try:
            assert_divisible_in_H(
                coefficient + 1,
                H,
                exponent,
                f"H^{exponent} negative control",
            )
        except AssertionError:
            pass
        else:
            raise AssertionError(
                f"H^{exponent} divisibility check accepted a nondivisible mutation"
            )
    assert_zero(poly_t.coeff_monomial(1) - vandermonde_constant, "Vandermonde constant term")

    print("boundary-adapted affine-family verification: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
