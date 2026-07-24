#!/usr/bin/env python3
"""Exact symbolic checks for issue #3 countermodels.

These computations are process evidence only. The analytic proofs and exact
scientific scope are in the issue-specific Markdown artifacts.
"""
from __future__ import annotations

import sys

try:
    import sympy as sp
except ImportError as exc:  # pragma: no cover
    raise SystemExit("SymPy is required for this optional exact check") from exc


def rank3_multiply(
    a: sp.Matrix,
    b: sp.Matrix,
    r: sp.Expr,
    s: sp.Expr,
    linear_w: sp.Expr = 0,
    cross_x2y: sp.Expr = 0,
) -> sp.Matrix:
    """Multiply in the two rank-three families used below.

    For ``linear_w=cross_x2y=0`` the relations are
        w^2=-r e, e^2=s w, we=-rs.

    For ``linear_w=cross_x2y=1`` and ``r=u,s=v`` the relations are
        w^2=w-u e, e^2=v(w-1), we=-uv.
    """
    a0, a1, a2 = a
    b0, b1, b2 = b
    return sp.Matrix(
        [
            sp.expand(
                a0 * b0
                - r * s * (a1 * b2 + a2 * b1)
                - cross_x2y * s * a2 * b2
            ),
            sp.expand(
                a0 * b1
                + a1 * b0
                + linear_w * a1 * b1
                + s * a2 * b2
            ),
            sp.expand(a0 * b2 + a2 * b0 - r * a1 * b1),
        ]
    )


def multiplication_matrix(
    x: sp.Matrix,
    basis: list[sp.Matrix],
    multiply,
) -> sp.Matrix:
    return sp.Matrix.hstack(*(multiply(x, b) for b in basis))


def check_keller_near_model() -> None:
    u, v, x, y, lam, T = sp.symbols("u v x y lambda T")
    one = sp.Matrix([1, 0, 0])
    w = sp.Matrix([0, 1, 0])
    e = sp.Matrix([0, 0, 1])
    basis = [one, w, e]

    def mul(a: sp.Matrix, b: sp.Matrix) -> sp.Matrix:
        return rank3_multiply(a, b, u, v, linear_w=1, cross_x2y=1)

    for a in basis:
        for b in basis:
            for c in basis:
                left = mul(mul(a, b), c)
                right = mul(a, mul(b, c))
                assert all(sp.expand(z) == 0 for z in left - right)

    alpha = sp.Matrix([0, x, y])
    alpha2 = mul(alpha, alpha)
    power = sp.Matrix.hstack(one, alpha, alpha2)
    index_form = sp.factor(power.det())
    assert sp.expand(index_form + u * x**3 + x**2 * y + v * y**3) == 0

    gram = sp.Matrix(
        [
            [sp.trace(multiplication_matrix(mul(a, b), basis, mul)) for b in basis]
            for a in basis
        ]
    )
    normal_disc = sp.factor(gram.det())
    assert sp.expand(normal_disc + v * (4 + 27 * u**2 * v)) == 0

    alpha_we = w + e
    char_we = sp.factor(multiplication_matrix(alpha_we, basis, mul).charpoly(T).as_expr())
    expected_char = (
        T**3
        - T**2
        + v * (3 * u + 1) * T
        - v * (u**2 - u * v + 2 * u + 1)
    )
    assert sp.expand(char_we - expected_char) == 0

    mutation_index = sp.factor(index_form.subs({x: 1, y: lam}))
    assert sp.expand(mutation_index + u + lam + lam**3 * v) == 0

    source_s = sp.symbols("s")
    source_v = u * source_s**3 - source_s**2
    source_jacobian = sp.diff(source_v, source_s)
    assert sp.factor(source_jacobian) == source_s * (3 * u * source_s - 2)

    print("smooth rational fixed-sheet countermodel: PASS")
    print(f"  index form = {index_form}")
    print(f"  normal discriminant = {normal_disc}")
    print(f"  mutation index = {mutation_index}")
    print(f"  open-plane Jacobian = {sp.factor(source_jacobian)}")


def check_diagonal_rank3_model() -> None:
    t, x, y = sp.symbols("t x y")
    d = t**2 + 1
    one = sp.Matrix([1, 0, 0])
    w = sp.Matrix([0, 1, 0])
    e = sp.Matrix([0, 0, 1])
    basis = [one, w, e]

    def mul(a: sp.Matrix, b: sp.Matrix) -> sp.Matrix:
        return rank3_multiply(a, b, t, d)

    for a in basis:
        for b in basis:
            for c in basis:
                left = mul(mul(a, b), c)
                right = mul(a, mul(b, c))
                assert all(sp.expand(z) == 0 for z in left - right)

    alpha = sp.Matrix([0, x, y])
    power = sp.Matrix.hstack(one, alpha, mul(alpha, alpha))
    index_form = sp.factor(power.det())
    assert sp.expand(index_form + t * x**3 + d * y**3) == 0

    trace_gram = sp.Matrix(
        [[3, 0, 0], [0, 0, -3 * t * d], [0, -3 * t * d, 0]]
    )
    normal_disc = sp.factor(trace_gram.det())
    assert sp.expand(normal_disc + 27 * t**2 * d**2) == 0
    power_disc = sp.expand((power.T * trace_gram * power).det())
    assert sp.expand(power_disc - normal_disc * index_form**2) == 0

    print("diagonal rank-three countermodel: PASS")
    print(f"  index form = {index_form}")
    print(f"  normal discriminant = {normal_disc}")


def check_rational_corank_two_model() -> None:
    u, v, x, y = sp.symbols("u v x y")
    one = sp.Matrix([1, 0, 0])
    alpha = sp.Matrix([0, x, y])
    alpha2 = rank3_multiply(alpha, alpha, u, v)
    index_form = sp.factor(sp.Matrix.hstack(one, alpha, alpha2).det())
    assert sp.expand(index_form + u * x**3 + v * y**3) == 0
    print("rational corank-two model: PASS")
    print(f"  index form = {index_form}")


def reduce_biquadratic(
    expr: sp.Expr,
    a: sp.Symbol,
    b: sp.Symbol,
    u: sp.Symbol,
    v: sp.Symbol,
) -> sp.Matrix:
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
    power = sp.Matrix.hstack(*columns)
    index_form = sp.factor(power.det())
    assert sp.expand(index_form + 4 * c**2 * (u - c**2 * v)) == 0

    values = [a + c * b, a - c * b, -a + c * b, -a - c * b]
    vandermonde = sp.factor(
        sp.prod(values[j] - values[i] for i in range(4) for j in range(i + 1, 4))
    )
    expected_raw = 64 * c**2 * a**2 * b**2 * (a**2 - c**2 * b**2)
    assert sp.expand(vandermonde - expected_raw) == 0

    expected_v = 64 * c**2 * u * v * (u - c**2 * v)
    normal_disc = 2**8 * u**2 * v**2
    assert sp.expand(expected_v**2 - normal_disc * index_form**2) == 0

    print("biquadratic Galois collision model: PASS")
    print(f"  index form = {index_form}")
    print(f"  Vandermonde = {sp.factor(expected_v)}")


def main() -> int:
    check_keller_near_model()
    check_diagonal_rank3_model()
    check_rational_corank_two_model()
    check_biquadratic_model()
    print("all exact symbolic checks: PASS")
    print("scientific inference: process evidence only")
    return 0


if __name__ == "__main__":
    sys.exit(main())
