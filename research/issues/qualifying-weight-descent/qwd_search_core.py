#!/usr/bin/env python3
"""Exact symbolic/combinatorial checks for issue #41 qualifying-weight descent.

The executable separates support, formal-layer, polynomial, and Keller levels.
Bounded searches are falsification evidence; the unbounded statements are proved
in the accompanying Markdown files.
"""
from __future__ import annotations

import argparse
import json
import math
import random
from dataclasses import asdict, dataclass
from fractions import Fraction
from itertools import combinations, product
from typing import Iterable

import sympy as sp

Point = tuple[int, int]
Ray = tuple[int, int]
Support = frozenset[Point]


@dataclass
class Counts:
    primitive_weights: int = 0
    affine_family_instances: int = 0
    affine_weight_evaluations: int = 0
    fan_instances: int = 0
    fan_rays: int = 0
    fan_bruteforce_comparisons: int = 0
    binomial_chain_instances: int = 0
    binomial_chain_equations: int = 0
    missing_support_patterns: int = 0
    formal_ideals: int = 0
    formal_variables_max: int = 0
    adjacent_edge_solutions: int = 0
    adjacent_edge_zero_vertex_controls: int = 0
    exhaustive_support_points: int = 0
    exhaustive_binomial_supports: int = 0
    exhaustive_support_pairs: int = 0
    exhaustive_axis_admissible_pairs: int = 0
    exhaustive_high_defect_pairs: int = 0
    exhaustive_face_compatible_pairs: int = 0
    exhaustive_formal_systems: int = 0
    exhaustive_formal_survivors: int = 0
    mutation_controls: int = 0
    exact_assertions: int = 0


COUNTS = Counts()


def check(condition: bool, message: str) -> None:
    COUNTS.exact_assertions += 1
    if not condition:
        raise AssertionError(message)


def gcd2(a: int, b: int) -> int:
    return math.gcd(abs(a), abs(b))


def primitive(v: Point) -> Point:
    if v == (0, 0):
        raise ValueError("zero vector has no primitive direction")
    g = gcd2(*v)
    a, b = v[0] // g, v[1] // g
    if a < 0 or (a == 0 and b < 0):
        a, b = -a, -b
    return (a, b)


def det(u: Point, v: Point) -> int:
    return u[0] * v[1] - u[1] * v[0]


def dot(u: Point, v: Point) -> int:
    return u[0] * v[0] + u[1] * v[1]


def primitive_weights(bound: int) -> list[Ray]:
    return [
        (p, q)
        for p in range(1, bound + 1)
        for q in range(1, bound + 1)
        if math.gcd(p, q) == 1
    ]


def weighted_degree(support: Support, w: Ray) -> int:
    if not support:
        raise ValueError("zero polynomial is outside this packet")
    return max(dot(a, w) for a in support)


def kappa(support_p: Support, support_q: Support, w: Ray) -> int:
    return weighted_degree(support_p, w) + weighted_degree(support_q, w) - sum(w)


def face_support(support: Support, w: Ray) -> Support:
    d = weighted_degree(support, w)
    return frozenset(a for a in support if dot(a, w) == d)


def convex_hull(points: Iterable[Point]) -> list[Point]:
    pts = sorted(set(points))
    if len(pts) <= 1:
        return pts

    def cross(o: Point, a: Point, b: Point) -> int:
        return det((a[0] - o[0], a[1] - o[1]), (b[0] - o[0], b[1] - o[1]))

    lower: list[Point] = []
    for point in pts:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], point) <= 0:
            lower.pop()
        lower.append(point)
    upper: list[Point] = []
    for point in reversed(pts):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], point) <= 0:
            upper.pop()
        upper.append(point)
    return lower[:-1] + upper[:-1]


def minkowski_support(s: Support, t: Support) -> Support:
    return frozenset((a[0] + b[0], a[1] + b[1]) for a in s for b in t)


def positive_normal_rays(support_p: Support, support_q: Support) -> list[Ray]:
    """Rays of the common normal fan in the closed first quadrant."""
    hull = convex_hull(minkowski_support(support_p, support_q))
    rays: set[Ray] = {(1, 0), (0, 1)}
    if len(hull) >= 2:
        for a, b in zip(hull, hull[1:] + hull[:1]):
            edge = (b[0] - a[0], b[1] - a[1])
            normal = (edge[1], -edge[0])
            if normal[0] >= 0 and normal[1] >= 0 and normal != (0, 0):
                rays.add(primitive(normal))
    return sorted(
        rays,
        key=lambda r: (r[0] == 0, Fraction(r[1], r[0]) if r[0] else 0),
    )


def extended_gcd(a: int, b: int) -> tuple[int, int, int]:
    if b == 0:
        return (abs(a), 1 if a >= 0 else -1, 0)
    g, x1, y1 = extended_gcd(b, a % b)
    return (g, y1, x1 - (a // b) * y1)


def regular_subdivision(u: Ray, v: Ray) -> list[Ray]:
    """Primitive rays u=h0,...,hr=v with det(hi,hi+1)=1."""
    d = det(u, v)
    if d <= 0:
        raise ValueError(f"rays not counterclockwise: {u}, {v}")
    if d == 1:
        return [u, v]
    g, s, t = extended_gcd(u[0], u[1])
    if g != 1:
        raise AssertionError("ray not primitive")
    w0 = (-t, s)
    raw = det(w0, v)
    remainder = raw % d
    if remainder == 0:
        raise AssertionError("primitive endpoint produced zero Euclidean remainder")
    shift = (remainder - raw) // d
    w = (w0[0] + shift * u[0], w0[1] + shift * u[1])
    if det(u, w) != 1 or not (0 < det(w, v) < d):
        raise AssertionError("Euclidean insertion failed")
    return [u] + regular_subdivision(w, v)


def finite_weight_test_set(
    support_p: Support, support_q: Support, *, count_rays: bool = True
) -> list[Ray]:
    coarse = positive_normal_rays(support_p, support_q)
    regular: list[Ray] = [coarse[0]]
    for u, v in zip(coarse, coarse[1:]):
        regular.extend(regular_subdivision(u, v)[1:])
    if not all(det(u, v) == 1 for u, v in zip(regular, regular[1:])):
        raise AssertionError("fan not regular")
    candidates = {r for r in regular if r[0] > 0 and r[1] > 0}
    if not candidates:
        candidates.add((1, 1))
    if count_rays:
        COUNTS.fan_rays += len(regular)
    return sorted(candidates)


def polynomial_support(expr: sp.Expr, x: sp.Symbol, y: sp.Symbol) -> Support:
    poly = sp.Poly(sp.expand(expr), x, y)
    return frozenset(tuple(map(int, mon)) for mon, coeff in poly.terms() if coeff != 0)


def jacobian(p: sp.Expr, q: sp.Expr, x: sp.Symbol, y: sp.Symbol) -> sp.Expr:
    return sp.expand(sp.diff(p, x) * sp.diff(q, y) - sp.diff(p, y) * sp.diff(q, x))
