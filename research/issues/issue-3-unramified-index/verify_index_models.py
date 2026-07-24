#!/usr/bin/env python3
"""Exact symbolic checks for the issue #3 countermodels.

This script is non-decisive process evidence.  The mathematical proofs are in the
Markdown artifacts; the script independently recomputes their finite algebra and
determinant identities.
"""

from __future__ import annotations

import sys

try:
    import sympy as sp
except ImportError as exc:  # pragma: no cover - explicit environment failure
    raise SystemExit("SymPy is required for this optional exact check") from exc


def coords_rank3(vec: sp.Matrix, x: sp.Expr, y: sp.Expr, c: sp.Expr = 0) -> sp.Matrix:
    """Coordinates of c + x*w + y*e in the basis (1,w,e)."""
    return sp.Matrix([c, x, y])


def rank3_multiply(
    a: sp.Matrix,
    b: sp.Matrix,
    r: sp.Expr,
    s: sp.Expr,
) -> sp.Matrix:
    """Multiply in w^2=-r e, e^2=s w, we=-r s."""
    a0, a1, a2 = a
    b0, b1, b2 = b
    return sp.Matrix(
        [
            sp.expand(a0 * b0 - r * s * (a1 * b2 + a2 * b1)),
            sp.expand(a0 * b1 + a1 * b0 + s * a2 * b2),
            sp.expand(a0 * b2 + a2 * b0 - r * a1 * b1),
        ]
    )


def check_rank3_model() -> None:
    t, x, y = sp.symbols("t x y")
    d = t**2 + 1
    one = sp.Matrix([1, 0, 0])
    w = sp.Matrix([0, 1, 0])
    e = sp.Matrix([0, 0, 1])

    # Associativity on basis triples is sufficient by bilinearity.
    basis = [one, w, e]
    for a in basis:
        for b in basis:
            for c in basis:
                left = rank3_multiply(rank3_multiply(a, b, t, d), c, t, d)
                right = rank3_multiply(a, rank3_multiply(b, c, t, d), t, d)
                assert all(sp.expand(z) == 0 for z in left - right)

    alpha = coords_rank3(one, x, y)
    alpha2 = rank3_multiply(alpha, alpha, t, d)
    power_matrix = sp.Matrix.hstack(one, alpha, alpha2)
    index_form = sp.factor(power_matrix.det())
    assert sp.expand(index_form + t * x**3 + d * y**3) == 0

    trace_gram = sp.Matrix(
        [
            [3, 0, 0],
            [0, 0, -3 * t * d],
            [0, -3 * t * d, 0],
        ]
    )
    normal_disc = sp.factor(trace_gram.det())
    assert sp.expand(normal_disc + 27 * t**2 * d**2) == 0

    power_gram = sp.simplify(power_matrix.T * trace_gram * power_matrix)
    power_disc = sp.factor(power_gram.det())
    expected = sp.factor(normal_disc * index_form**2)
    assert sp.expand(power_disc - expected) == 0

    print("rank-three local/global countermodel: PASS")
    print(f"  index form = {index_form}")
    print(f"  normal discriminant = {normal_disc}")


def check_rational_rank3_model() -> None:
    u, v, x, y = sp.symbols("u v x y")
    one = sp.Matrix([1, 0, 0])
    alpha = sp.Matrix([0, x, y])
    alpha2 = rank3_multiply(alpha, alpha, u, v)
    index_form = sp.factor(sp.Matrix.hstack(one, alpha, alpha2).det())
    assert sp.expand(index_form + u * x**3 + v * y**3) == 0
    print("rational corank-two rank-three model: PASS")
    print(f"  index form = {index_form}")


def reduce_biquadratic(expr: sp.Expr, a: sp.Symbol, b: sp.Symbol, u: sp.Symbol, v: sp.Symbol) -> sp.Matrix:
    """Reduce modulo a^2=u, b^2=v into the basis (1,a,b,ab)."""
    out = [sp.Integer(0)] * 4
    for term in sp.Add.make_args(sp.expand(expr)):
        powers = term.as_powers_dict()
        ea = int(powers.get(a, 0))
        eb = int(powers.get(b, 0))
        coeff = term / (a**ea * b**eb)
        coeff *= u ** (ea // 2) * v ** (eb // 2)
        idx = {(0, 0): 0, (1, 0): 1, (0, 1): 2, (1, 1): 3}[(ea % 2, eb % 2)]
        out[idx] = sp.expand(out[idx] + coeff)
    return sp.Matrix(out)


def check_biquadratic_model() -> None:
    a, b, c, u, v = sp.symbols("a b c u v")
    theta = a + c * b
    columns = [reduce_biquadratic(theta**j, a, b, u, v) for j in range(4)]
    power_matrix = sp.Matrix.hstack(*columns)
    index_form = sp.factor(power_matrix.det())
    assert sp.expand(index_form + 4 * c**2 * (u - c**2 * v)) == 0

    values = [a + c * b, a - c * b, -a + c * b, -a - c * b]
    vandermonde = sp.factor(
        sp.prod(values[j] - values[i] for i in range(4) for j in range(i + 1, 4))
    )
    expected_v = 64 * c**2 * u * v * (u - c**2 * v)
    reduced_v = sp.expand(vandermonde.subs({a**2: u, b**2: v}))
    # Direct factor substitution is not recursive in SymPy, so compare before replacement.
    assert sp.expand(vandermonde - 64 * c**2 * a**2 * b**2 * (a**2 - c**2 * b**2)) == 0

    normal_disc = 2**8 * u**2 * v**2
    assert sp.expand(expected_v**2 - normal_disc * index_form**2) == 0

    print("biquadratic Galois collision model: PASS")
    print(f"  index form = {index_form}")
    print(f"  Vandermonde = {sp.factor(expected_v)}")


def main() -> int:
    check_rank3_model()
    check_rational_rank3_model()
    check_biquadratic_model()
    print("all exact symbolic checks: PASS")
    print("scientific inference: process evidence only")
    return 0


if __name__ == "__main__":
    sys.exit(main())
