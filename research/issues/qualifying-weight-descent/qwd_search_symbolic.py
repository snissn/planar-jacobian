#!/usr/bin/env python3
"""Affine, binomial-chain, and formal symbolic campaigns for issue #41."""
from qwd_search_core import *  # noqa: F401,F403


def campaign_affine_obstruction(weight_bound: int, max_n: int) -> None:
    weights = primitive_weights(weight_bound)
    COUNTS.primitive_weights = len(weights)
    for n in range(2, max_n + 1):
        COUNTS.affine_family_instances += 1
        best: int | None = None
        for p, q in weights:
            r, s = sorted((p, q))
            d_low = max(s, n * r)
            d_high = n * s
            for d in (d_low, d_high):
                value = (n + 1) * d - p - q
                COUNTS.affine_weight_evaluations += 1
                best = value if best is None else min(best, value)
        expected = n * n - 1
        check(best == expected, f"A_{n}: affine minimum {best}, expected {expected}")
        p_support = frozenset({(1, 0), (0, n)})
        q_support = frozenset({(0, 1)} | {(k, n * (n - k)) for k in range(n + 1)})
        check(kappa(p_support, q_support, (n, 1)) == expected, "affine bound not achieved")
        check(kappa(p_support, frozenset({(0, 1)}), (n, 1)) == 0, "target shear failed")
    n = max(3, min(max_n, 7))
    p_support = frozenset({(1, 0), (0, n)})
    q_support = frozenset({(0, 1)} | {(k, n * (n - k)) for k in range(n + 1)})
    exact = n * n - 1
    omitted = min(
        kappa(p_support, q_support, w)
        for w in weights
        if w not in {(n, 1), (1, n)}
    )
    check(omitted > exact, "omitted-weight mutation was not detected")
    COUNTS.mutation_controls += 1


def campaign_binomial_chain(max_n: int) -> None:
    x, y = sp.symbols("x y")
    for n in range(2, max_n + 1):
        COUNTS.binomial_chain_instances += 1
        a, b, c = sp.symbols(f"a{n} b{n} c{n}")
        qs = sp.symbols(" ".join(f"q{n}_{k}" for k in range(n + 1)))
        p = a * x + b * y**n
        q = c * y + sum(qs[k] * x**k * y ** (n * (n - k)) for k in range(n + 1))
        equations = [sp.factor(coeff) for coeff in sp.Poly(jacobian(p, q, x, y) - 1, x, y).coeffs()]
        COUNTS.binomial_chain_equations += len(equations)
        check(len(equations) == n + 1, f"B_{n}: wrong number of equations")
        check(any(sp.expand(e) == a * c - 1 for e in equations), f"B_{n}: no constant equation")
        for k in range(n):
            expected = n * (a * (n - k) * qs[k] - b * (k + 1) * qs[k + 1])
            check(any(sp.expand(e - expected) == 0 for e in equations), f"B_{n}: missing recurrence {k}")
        lam = qs[n] / a**n
        target = sp.expand(c * y + lam * p**n)
        substitutions: dict[sp.Symbol, sp.Expr] = {c: 1 / a}
        for k in range(n):
            substitutions[qs[k]] = sp.simplify(lam * math.comb(n, k) * a**k * b ** (n - k))
        check(sp.simplify(sp.expand(q - target).subs(substitutions)) == 0, f"B_{n}: recurrence failure")
        check(sp.simplify(jacobian(p, target, x, y).subs(c, 1 / a)) == 1, f"B_{n}: not Keller")
        for mask in range(1 << max(0, n - 1)):
            present = {0, n}
            for k in range(1, n):
                if mask & (1 << (k - 1)):
                    present.add(k)
            COUNTS.missing_support_patterns += 1
            if len(present) < n + 1:
                # Since a,b and the retained endpoint coefficients are nonzero,
                # each recurrence has nonzero scalar multipliers and therefore
                # q_k=0 iff q_(k+1)=0.  The zero/nonzero support pattern must be
                # constant along the entire chain; endpoints present with any
                # interior hole are exactly incompatible.
                recurrence_compatible = all(
                    (k in present) == (k + 1 in present) for k in range(n)
                )
                check(
                    not recurrence_compatible,
                    f"B_{n}: missing support pattern survived recurrence closure",
                )
        p_w = x + y**n
        q_w = y + p_w**n
        u, v = sp.symbols("u v")
        check(sp.expand((v - u**n).subs({u: p_w, v: q_w})) == y, "target shear failed")
        check(jacobian(p_w, q_w, x, y) == 1, f"A_{n}: not Keller")
    p = x + y**3
    q = y + p**3
    check(jacobian(q, p, x, y) == -1, "unsigned swap mutation not detected")
    COUNTS.mutation_controls += 1


def campaign_formal_23() -> None:
    x, y, z = sp.symbols("x y z")
    a, b = sp.symbols("a b")
    p10, p01, p00 = sp.symbols("p10 p01 p00")
    q20, q11, q02, q10, q01, q00 = sp.symbols("q20 q11 q02 q10 q01 q00")
    p = a * x**2 + p10 * x + p01 * y + p00
    q = b * x**3 + q20 * x**2 + q11 * x * y + q02 * y**2 + q10 * x + q01 * y + q00
    coeffs = sp.Poly(jacobian(p, q, x, y) - 1, x, y).coeffs()
    equations = coeffs + [z * a * b - 1]
    variables = [z, a, b, p10, p01, q20, q11, q02, q10, q01]
    COUNTS.formal_ideals += 1
    COUNTS.formal_variables_max = max(COUNTS.formal_variables_max, len(variables))
    gb = sp.groebner(equations, *variables, order="grevlex")
    check(any(poly.as_expr() == 1 for poly in gb.polys), "formal (2,3) template survived")
    gb_unsat = sp.groebner(coeffs, *variables[1:], order="grevlex")
    check(not any(poly.as_expr() == 1 for poly in gb_unsat.polys), "saturation mutation not detected")
    COUNTS.mutation_controls += 1
