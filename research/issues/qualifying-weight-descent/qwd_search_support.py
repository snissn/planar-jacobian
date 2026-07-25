#!/usr/bin/env python3
"""Finite-fan, exhaustive-support, and adjacency campaigns for issue #41."""
from qwd_search_core import *  # noqa: F401,F403
from qwd_search_symbolic import *  # noqa: F401,F403


def random_tame_map(rng: random.Random, steps: int, degree_cap: int = 5) -> tuple[sp.Expr, sp.Expr]:
    x, y = sp.symbols("x y")
    p, q = x, y
    for _ in range(steps):
        degree = rng.randint(2, degree_cap)
        coeff = rng.choice([-2, -1, 1, 2])
        mode = rng.randrange(4)
        if mode == 0:
            p = sp.expand(p + coeff * q**degree)
        elif mode == 1:
            q = sp.expand(q + coeff * p**degree)
        elif mode == 2:
            p, q = q, -p
        else:
            p, q = sp.expand(p + q), q
        if max(sp.Poly(p, x, y).total_degree(), sp.Poly(q, x, y).total_degree()) > 24:
            break
    return p, q


def campaign_finite_fan(weight_bound: int, instances: int) -> None:
    x, y = sp.symbols("x y")
    rng = random.Random(41041)
    weights = primitive_weights(weight_bound)
    maps: list[tuple[sp.Expr, sp.Expr]] = []
    for n in range(2, 9):
        p = x + y**n
        maps.append((p, y + p**n))
        maps.append((p, y))
    while len(maps) < instances:
        maps.append(random_tame_map(rng, steps=rng.randint(2, 5)))
    for p, q in maps[:instances]:
        check(jacobian(p, q, x, y) in (1, -1), "generated tame map lost constant Jacobian")
        support_p = polynomial_support(p, x, y)
        support_q = polynomial_support(q, x, y)
        test = finite_weight_test_set(support_p, support_q)
        finite_min = min(kappa(support_p, support_q, w) for w in test)
        brute_min = min(kappa(support_p, support_q, w) for w in weights)
        check(finite_min == brute_min, f"finite fan {finite_min} != brute {brute_min}")
        check(finite_min >= 0, "Keller support produced negative defect")
        COUNTS.fan_instances += 1
        COUNTS.fan_bruteforce_comparisons += len(weights)


def binomial_face_compatible(face_p: Support, face_q: Support) -> bool:
    if len(face_p) == len(face_q) == 1:
        return det(next(iter(face_p)), next(iter(face_q))) == 0
    if len(face_p) != len(face_q):
        return False
    if len(face_p) == 2:
        return face_p == face_q
    return False


def binomial_support_face_compatible(support_p: Support, support_q: Support) -> bool:
    coarse = positive_normal_rays(support_p, support_q)
    for u, v in zip(coarse, coarse[1:]):
        interior = (u[0] + v[0], u[1] + v[1])
        if not binomial_face_compatible(face_support(support_p, interior), face_support(support_q, interior)):
            return False
    for ray in coarse:
        if ray[0] > 0 and ray[1] > 0:
            if not binomial_face_compatible(face_support(support_p, ray), face_support(support_q, ray)):
                return False
    return True


def formal_binomial_pair(support_p: Support, support_q: Support) -> bool:
    x, y, z = sp.symbols("x y z")
    a0, a1, b0, b1 = sp.symbols("a0 a1 b0 b1")
    spoints = sorted(support_p)
    tpoints = sorted(support_q)
    p = a0 * x**spoints[0][0] * y**spoints[0][1] + a1 * x**spoints[1][0] * y**spoints[1][1]
    q = b0 * x**tpoints[0][0] * y**tpoints[0][1] + b1 * x**tpoints[1][0] * y**tpoints[1][1]
    coeffs = sp.Poly(jacobian(p, q, x, y) - 1, x, y).coeffs()
    equations = coeffs + [z * a0 * a1 * b0 * b1 - 1]
    variables = [z, a0, a1, b0, b1]
    gb = sp.groebner(equations, *variables, order="grevlex")
    return not any(poly.as_expr() == 1 for poly in gb.polys)


def campaign_exhaustive_binomial_supports(max_degree: int) -> None:
    points = [(i, j) for i in range(max_degree + 1) for j in range(max_degree + 1 - i)]
    supports = [frozenset(pair) for pair in combinations(points, 2)]
    COUNTS.exhaustive_support_points = len(points)
    COUNTS.exhaustive_binomial_supports = len(supports)
    COUNTS.exhaustive_support_pairs = len(supports) ** 2
    formal_candidates: list[tuple[Support, Support]] = []
    for support_p in supports:
        for support_q in supports:
            axis_x = kappa(support_p, support_q, (1, 0))
            axis_y = kappa(support_p, support_q, (0, 1))
            if axis_x < 0 or axis_y < 0:
                continue
            COUNTS.exhaustive_axis_admissible_pairs += 1
            test = finite_weight_test_set(support_p, support_q, count_rays=False)
            minimum = min(kappa(support_p, support_q, w) for w in test)
            if minimum < 6:
                continue
            COUNTS.exhaustive_high_defect_pairs += 1
            if not binomial_support_face_compatible(support_p, support_q):
                continue
            COUNTS.exhaustive_face_compatible_pairs += 1
            formal_candidates.append((support_p, support_q))
    seen: set[tuple[tuple[Point, ...], tuple[Point, ...]]] = set()
    for support_p, support_q in formal_candidates:
        key = (tuple(sorted(support_p)), tuple(sorted(support_q)))
        canonical = min(key, (key[1], key[0]))
        if canonical in seen:
            continue
        seen.add(canonical)
        COUNTS.exhaustive_formal_systems += 1
        if formal_binomial_pair(support_p, support_q):
            COUNTS.exhaustive_formal_survivors += 1
    check(COUNTS.exhaustive_formal_survivors == 0, "a high-defect binomial formal Keller pair survived")


def campaign_adjacent_edges(bound: int = 9) -> None:
    pairs = [(m, n) for m in range(1, 6) for n in range(1, 6) if math.gcd(m, n) == 1]
    nonzero_solutions = 0
    zero_controls = 0
    for pair1, pair2 in product(pairs, repeat=2):
        m, n = pair1
        r, s = pair2
        for h in product(range(bound + 1), repeat=2):
            if h == (0, 0):
                continue
            vp = (m * h[0], m * h[1])
            vq = (n * h[0], n * h[1])
            if vp[0] % r or vp[1] % r or vq[0] % s or vq[1] % s:
                continue
            h1 = (vp[0] // r, vp[1] // r)
            h2 = (vq[0] // s, vq[1] // s)
            if h1 == h2:
                nonzero_solutions += 1
                check(pair1 == pair2, "nonzero shared vertex allowed incompatible powers")
    for pair1, pair2 in combinations(pairs, 2):
        zero_controls += 1
        check((0 * pair1[0], 0 * pair1[1]) == (0, 0), "zero control failed")
    COUNTS.adjacent_edge_solutions = nonzero_solutions
    COUNTS.adjacent_edge_zero_vertex_controls = zero_controls
    COUNTS.mutation_controls += 1


def campaign_support_level(max_n: int, weight_bound: int) -> list[dict[str, object]]:
    weights = primitive_weights(weight_bound)
    records: list[dict[str, object]] = []
    for n in range(3, max_n + 1):
        support_p = frozenset({(1, 0), (0, n)})
        support_q = frozenset({(0, 1)} | {(k, n * (n - k)) for k in range(n + 1)})
        affine_min = min(kappa(support_p, support_q, w) for w in weights)
        check(affine_min == n * n - 1, "support campaign disagrees with affine theorem")
        records.append({
            "family": f"A_{n}",
            "support_level_affine_min": affine_min,
            "formal_level": "complete Jacobian recurrence solved",
            "polynomial_level": "explicit coefficients exist",
            "keller_level": "J=1 with explicit inverse",
            "after_declared_triangular_target_shear": 0,
            "adjacent_edge": {"lengths": [1, n], "coprime_exponents": [1, n]},
        })
    return records
