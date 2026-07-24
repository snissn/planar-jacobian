# Handoff: Rank-Three Boundary-Cube Elimination

```text
issue: 3
leaf: L14
packet_status: BLOCKED_WITH_EXACT_REDUCTION
next_claim: CLM-059 after wording correction
```

## 1. Banked results to reuse

1. `O=B*1 direct_sum E`, with `E` free rank two under finite local freeness.
2. Intrinsic binary cubic `Phi:E->det(E)` and exact fixed-section Fitting test.
3. Universal content ideal is frame-independent but does not imply a unit
   value.
4. Weighted derivative stability with explicit denominators `h_P,h_Q`.
5. Boundary clearing `Phi((mr)^0)=m^3 Phi_K(r)`.
6. Four fixed source directions cover every cubic fiber away from the boundary
   image.
7. One issue #3 section handles all boundary height-one primes, yielding a
   finite gcd-one index certificate.
8. Exact primitive-coordinate congruence

```text
F_T
 = F_T(X_PY_Q-X_QY_P)
   +F_P(X_QY_T-X_TY_Q)
   +F_Q(X_TY_P-X_PY_T) mod F.
```

9. The different of an actual Keller normalization is supported in `Y-U`.
10. The issue #3 interior-different model and all affine-coordinate constant-J
    repairs are excluded.

## 2. Smallest next calculation

Choose a primitive cubic coordinate `t` and quadratic representatives
`x=X(t), y=Y(t)`. For every boundary height-one valuation, write the valuations
of:

```text
F_T, F_P, F_Q,
X_T,X_P,X_Q,
Y_T,Y_P,Y_Q.
```

Use the congruence to prove one of the following exact statements.

### Preferred target

There exist `a,b,m in B`, with `r=ax+by` primitive and `(mr)^0 in E`, such that

```text
div_B(Phi_K(r)) = -3 div_B(m).
```

Then `Phi((mr)^0) in C*`, so issue #3 globalization and the minimal-polynomial
argument give degree one.

### Equivalent support target

Find one integral section adapted at the boundary primes and prove that every
unramified factor of its index would force a common collision of both source
coordinates, not merely of one scalar projection.

### Falsification target

Construct a finite normal rank-three algebra with an open `A2` whose finite map
is polynomial étale with constant Jacobian, while the binary cubic has no unit
value. Every hypothesis, normalization computation, boundary component, and
Jacobian must be checked exactly.

## 3. Do not repeat these failed routes

- Do not identify the universal content ideal with a fixed-section index ideal.
- Do not invoke derivative simplicity without proving `D_P(O),D_Q(O) subset O`.
- Do not infer a critical point from equality of one sheet value.
- Do not infer trivial different/canonical class from freeness of `E`.
- Do not use exactness of `P dQ+y dx` as principalization.
- Do not treat the triangular deformation audit as an exhaustive moduli search.
- Do not reverse `O -> C[x,y]`.

## 4. Validation

Run the packet checks:

```text
python3 -m compileall -q research/issues/rank-three-index-form-unit
python3 research/issues/rank-three-index-form-unit/verify_all.py
```

Run the repository and predecessor regressions:

```text
python3 -m compileall -q scripts research/issues/issue-3-unramified-index research/issues/rank-three-index-form-unit
python3 scripts/render_views.py --check
python3 scripts/validate_repository.py
python3 scripts/frontier.py
python3 research/issues/issue-3-unramified-index/verify_index_models.py
python3 scripts/validate_defect4_staircase.py
python3 scripts/review_validate_defect4_independent.py
python3 scripts/validate_issue4_stable_order.py
python3 scripts/validate_issue5_principal_parts.py
```

Passing validation does not alter scientific status.
