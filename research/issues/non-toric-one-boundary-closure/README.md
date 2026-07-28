# Non-Toric One-Boundary Laurent–Conductor Closure

```text
authority: MUTABLE_NONAUTHORITATIVE
scientific_status: SUBCLASS_EXCLUSION_WITH_LIOUVILLE_EXACTNESS_REDUCTION
review_mode: local-adversarial-review
role: research-worker
task_issue: 5
supporting_issue: 13
owned_path: research/issues/non-toric-one-boundary-closure/
base_commit: 652a5e252626fa5816445651245e8a8946cee53e
issue_local_labels: NTLC-*
```

## Disposition

This packet does **not** exclude every non-toric one-boundary Keller
normalization and does not produce a qualifying weight. It proves a new exact
subclass obstruction and reduces the fixed-type recursion to explicit
one-dimensional differential equations.

Let `E` be a generically ramified boundary divisor, let `C` be its reduced
target branch, and assume at least one source coordinate has a pole at `E`.
Then:

1. after a finite extension of the boundary coefficient field and a formal
   change of uniformizer, one may set `x=s^(-m)`;
2. if the ramification order is `e>0`, every coefficient of `y` below the
   first ramification order is constant in the boundary function field;
3. the unique logarithmic-resonant coefficient is zero by the exact
   zero-residue equation;
4. consequently the pullback of `P dQ` to the normalization of `C` is an exact
   rational differential;
5. for a singular branch, its primitive is regular on the normalized affine
   curve and leaves one finite conductor-descent class;
6. every branch for which `[P dQ]` is nonzero in rational de Rham cohomology is
   impossible in this ramified pole-supported class.

The new excluded class is called the **Liouville-nonexact non-toric class**.
It includes the smooth non-toric curve

```text
P(P-1)Q-1=0,
```

whose normalization is `P1-{0,1,infinity}` and for which `P dQ` has residues
`+1` and `-1` at two punctures.

The condition is not equivalent to toricity. The smooth non-toric curve

```text
P Q^2(Q-1)^2 + (Q-1)^2 + Q^2 = 0
```

has normalization `Q=z` and satisfies

```text
P dQ = d(1/z + 1/(z-1)).
```

It survives the new obstruction. A complete formal-neighborhood near-model is
recorded, but it does not yield a polynomial Keller pair: its primitive and
source realization retain rational denominators. Thus algebraization and
polynomial realization remain essential.

## Candidate results

- `NTLC-01` — Puiseux–Laurent coefficient normal form.
- `NTLC-02` — divisor-safe common-power conclusion from
  `n a' b-m a b'=0`.
- `NTLC-03` — triangular all-order Laurent recursion in `s=x^(-1/m)`.
- `NTLC-04` — normalized branch Liouville exactness: `P dQ=dR`.
- `NTLC-05` — conductor primitive and finite descent class.
- `NTLC-06` — exclusion of the Liouville-nonexact non-toric subclass.
- `NTLC-07` — exact explanation why local pole data do not produce a
  defect-`<=4` or defect-`5` weight.
- `NTLC-08` — all-orders toric control model and non-toric exact near-model.
- `NTLC-09` — remaining global bridge: polynomial algebraization plus support
  control, or a proof that one of its differential/conductor classes cannot
  vanish.

## Artifact map

- [`FOUNDATIONS.md`](FOUNDATIONS.md) — conventions, signs, authority, and exact
  hypotheses.
- [`BOUNDARY_NORMALIZATION.md`](BOUNDARY_NORMALIZATION.md) — normalized
  boundary, divisors, punctures, and common-power theorem.
- [`LAURENT_RECURSION.md`](LAURENT_RECURSION.md) — normalized coordinate and
  full recursive system.
- [`CONDUCTOR_GLUING.md`](CONDUCTOR_GLUING.md) — Liouville exactness, trace,
  conductor quotient, and singular gluing.
- [`LOGARITHMIC_FIELDS.md`](LOGARITHMIC_FIELDS.md) — logarithmic derivations and
  the exact/nonexact non-toric examples.
- [`WEIGHT_EXTRACTION.md`](WEIGHT_EXTRACTION.md) — candidate weights, defect
  calculations, and the missing global support input.
- [`CASE_TABLE.md`](CASE_TABLE.md) — exact case dispositions.
- [`FORMAL_MODELS.md`](FORMAL_MODELS.md) — symbolic models and realization
  levels.
- [`SOURCE_AUDIT.md`](SOURCE_AUDIT.md) — internal and primary-source bindings.
- [`REVIEW.md`](REVIEW.md) — pinned local adversarial review.
- [`HANDOFF.md`](HANDOFF.md) — issue #5 / issue #13 handoff.
- [`validate_laurent_conductor.py`](validate_laurent_conductor.py) — exact
  symbolic identities and mutations.
- [`verify_all.py`](verify_all.py) — packet and manifest checks.
- [`INTEGRATION.json`](INTEGRATION.json) — worker integration contract and
  proposed shared deltas.

## Scientific nonclaims

This packet does not prove that every boundary divisor has a source-coordinate
pole, that every Liouville-exact branch algebraizes to a Keller normalization,
that conductor descent is automatic, that a locally finite logarithmic field
exists, that a primitive positive weight of bounded defect exists, that the
fixed-weight defect-five candidate is independently accepted, or that the
planar Jacobian conjecture is true.
