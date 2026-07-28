# Three-Puncture Liouville-Exact Branch: Polynomial Realization Obstruction

```text
authority: MUTABLE_NONAUTHORITATIVE
scientific_status: DISPLAYED_BRANCH_EXCLUDED_AT_GLOBAL_POLYNOMIAL_LEVEL
review_mode: local-adversarial-review
role: research-worker
task_issue: 5
coordinating_issue: 13
owned_path: research/issues/three-puncture-polynomial-realization/
base_commit: b4545bd9ca395c023b0d452feee29b5e6f77f83e
issue_local_labels: TPPR-*
```

## Exact disposition

This packet proves requested disposition **A for the displayed branch only**.
Set

```text
g(P,Q)=P Q^2(Q-1)^2+(Q-1)^2+Q^2
```

and let `C=V(g)` in the target affine plane. There is no dominant quasi-finite
polynomial map

```text
F=(P,Q): A2_C -> A2_C
```

whose finite-normalization source boundary contains a divisor mapping onto
`C`. In particular, no polynomial Keller map can have the displayed normalized
boundary branch.

The contradiction occurs exactly at the `L3 -> L4` step:

1. `C[C]=C[z,z^(-1),(z-1)^(-1)]` with `Q=z`;
2. every morphism `A1 -> C` is constant, since `z` and `z-1` pull back to
   units of `C[t]`;
3. for a dominant quasi-finite polynomial map, the image of the omitted
   divisor in the finite normalization is an irreducible component of its
   nonproperness set `S_F`;
4. Jelonek--Lasoń, Theorem 3.2, makes every irreducible component of `S_F`
   polynomially uniruled, hence covered by nonconstant polynomial maps from
   `A1`;
5. these conclusions are incompatible.

The proof is independent of the source ramification index, pole orders,
Puiseux pairs, value semigroup, target conductor bound, number of source
boundary components, and simultaneous monomialization.

## Why exactness and conductor do not obstruct this branch

The normalization is

```text
Q=z,
P=-1/z^2-1/(z-1)^2,
R=1/z+1/(z-1),
P dQ=dR.
```

The rational-looking functions already lie in the affine branch ring.
Explicit representatives modulo `g` are

```text
Q^(-1) = -P Q^3+2P Q^2-P Q-2Q+2,
(Q-1)^(-1) = -P Q^2(Q-1)-2Q,
R = -2P Q^3+3P Q^2-P Q-4Q+2.
```

Thus `C` is smooth and normal, its conductor quotient is zero, and `[R]=0`.
The order-zero term of `P dQ+y dx=dH` is genuinely compatible. The new
obstruction is global polynomial realization of the map, not a concealed
residue or conductor failure.

## Candidate labels

- `TPPR-01`: exact branch ring, units, smooth normalization, punctures, and
  descended primitive.
- `TPPR-02`: finite-normalization boundary image equals the polynomial
  nonproperness set, componentwise.
- `TPPR-03`: primary-source binding to polynomial uniruledness of `S_F`.
- `TPPR-04`: exhaustive exclusion of nonconstant polynomial curves in `C`.
- `TPPR-05`: terminal exclusion of the displayed branch from polynomial
  Keller realization.
- `TPPR-06`: exact divisor and source-pole tables; no false local obstruction.
- `TPPR-07`: rational countermodel ladder and exact first failed condition.

## Artifact map

- [BRANCH_GEOMETRY.md](BRANCH_GEOMETRY.md)
- [SOURCE_COMPACTIFICATION.md](SOURCE_COMPACTIFICATION.md)
- [POLE_AND_DIVISOR_TABLE.md](POLE_AND_DIVISOR_TABLE.md)
- [CONDUCTOR_DESCENT.md](CONDUCTOR_DESCENT.md)
- [POLYNOMIAL_REALIZATION.md](POLYNOMIAL_REALIZATION.md)
- [FINITE_CASES.md](FINITE_CASES.md)
- [COUNTERMODEL_LADDER.md](COUNTERMODEL_LADDER.md)
- [LITERATURE_AUDIT.md](LITERATURE_AUDIT.md)
- [REVIEW.md](REVIEW.md)
- [HANDOFF.md](HANDOFF.md)
- [VALIDATION.md](VALIDATION.md)
- [verify_three_puncture.py](verify_three_puncture.py)
- [verify_all.py](verify_all.py)
- [INTEGRATION.json](INTEGRATION.json)

## Scientific nonclaims

This packet does not prove a general one-boundary theorem and does not treat
merely generically finite maps with positive-dimensional exceptional fibers.
It does not exclude all Liouville-exact branches, produce a qualifying weight,
identify a nonmonomial boundary valuation with a Newton weight, bound
ramification or conductor, classify all nonproperness curves, or establish
`JC_2`. Passing symbolic and repository checks establishes exact identities
and process consistency, not independent mathematical acceptance.
