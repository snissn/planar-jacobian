# Issue #3 — Rank-Three Keller Boundary-Cube Unit

```text
authority: MUTABLE_NONAUTHORITATIVE
role: research-worker
task_issue: #3
owned_path: research/issues/rank-three-boundary-cube-unit/
base_commit: 652a5e252626fa5816445651245e8a8946cee53e
scientific_disposition: RANK_THREE_KELLER_CASE_EXCLUDED_BY_PRIMARY_LITERATURE
review_state: local-adversarial-review required before integration
```

## Exact disposition

The rank-three Keller branch closes more strongly than the requested unit-value
construction.

### R3BC-01 — rank-three exclusion (`literature_bound`)

Let

```text
F=(P,Q): A2_C -> A2_C,
J(P,Q) in C*,
K=C(P,Q),
L=C(x,y).
```

If `[L:K]=3`, then `F` is generically three-sheeted: after localizing the target,
`C[x,y]` is finite étale of rank three over `C[P,Q]`, so every geometric fiber
on a dense open has exactly three reduced points. Orevkov's theorem states that
the Jacobian of a three-sheeted polynomial map `C2 -> C2` cannot be constant.
Thus a planar Keller map cannot have function-field degree three.

The primary source is:

> S. Yu. Orevkov, “On three-sheeted polynomial mappings of C²,”
> *Math. USSR-Izv.* **29** (1987), 587–596,
> DOI `10.1070/IM1987v029n03ABEH000984`.

The publisher's primary record gives the theorem in exactly that form. The
application from field degree to sheet number is proved in
[`FOUNDATIONS.md`](FOUNDATIONS.md), without importing an additional theorem.

Consequently, the simultaneous hypotheses

```text
J(P,Q) in C*,
O = normalization of C[P,Q] in C(x,y),
rank_B(O)=3
```

are inconsistent. This packet does **not** construct a section `s` with
`Phi(s) in C*`; it shows that no actual rank-three Keller normalization exists
on which that construction would have to be performed.

### R3BC-02 — exact boundary-cubic trichotomy (`candidate_proved`)

Conditionally retaining the predecessor's finite-flat rank-three algebra, the
special-fiber index cubic at a height-one base prime has, after strict
henselization and a trace-zero frame, exactly one of the following shapes:

```text
unramified split:       L1 L2 L3,
simple ramification:    L M^2,
total ramification:     L^3.
```

Thus “boundary cube” is correct only in the totally ramified case. Simple
ramification gives a distinguished simple factor times a square. The determinant
calculations and unit criteria are in
[`BOUNDARY_VALUATIONS.md`](BOUNDARY_VALUATIONS.md).

### R3BC-03 — boundary valuations are simultaneously removable (`candidate_proved`)

Let `H` be a square-free equation for the finite union of height-one target
primes under the normalization boundary. By the predecessor's finite-prime
adaptation theorem, choose `theta in E` with `Phi(theta)` a unit at every prime
dividing `H`. Then for every `eta in E` and `T in B`,

```text
s_T = theta + H T eta
```

has the same special-fiber class as `theta` at each boundary prime, hence stays
primitive there. Homogeneity gives the exact identity

```text
Phi(s_T) = D + H C T + H^2 B_2 T^2 + H^3 A T^3,
```

where `D=Phi(theta)` and `A=Phi(eta)`. Therefore no boundary prime divides any
`Phi(s_T)`. Every remaining factor is a nonboundary scalar-collision divisor.
This is the smallest exact internal reduction left if Orevkov's terminal theorem
is deliberately set aside.

### R3BC-04 — differential control does not remove the moving divisor (`candidate_proved`)

No nonconstant principal divisor in `C[P,Q]` can be invariant under both target
translations `partial_P` and `partial_Q`. However, the exact primitive-coordinate
differential congruence does not imply that the fixed-section ideal
`(Phi(s))` is translation-stable: differentiating `s` changes the section. On a
split étale chart, the logarithmic derivative is the sum of the three relative
sheet-velocity quotients, so accidental scalar collisions remain visible rather
than contradictory.

### R3BC-05 — countermodel ladder stops exactly at source étaleness (`candidate_proved`)

The integrated issue #3 no-unit model reaches:

```text
finite locally free rank three,
normal and connected,
rational total space,
an open A2,
no nonzero constant represented by Phi.
```

It fails because the displayed `A2` is not étale over the target. More strongly,
no rank-three model can add “different supported outside the displayed source
open”: that condition makes the restricted polynomial map étale, hence Keller,
and Orevkov then excludes degree three. Stages 5–9 of the requested ladder are
therefore incompatible already at stage 5.

## What is and is not proved

Proved at the stated packet scope:

1. the exact bridge from rank-three normalization degree to Orevkov's
   three-sheeted hypothesis;
2. the three local boundary forms `L1L2L3`, `LM^2`, and `L^3`;
3. simultaneous elimination of all boundary valuations in one affine family;
4. the exact remaining moving-collision polynomial;
5. incompatibility of the countermodel ladder with source étaleness at degree
   three.

Not claimed:

- a new proof of Orevkov's theorem;
- a constructed unit-index section for a hypothetical rank-three Keller
  normalization;
- a theorem for rank four or higher;
- a proof of the planar Jacobian conjecture;
- scientific promotion from this local construction/review round.

## Artifact map

- [`FOUNDATIONS.md`](FOUNDATIONS.md): exact setup, degree-to-sheet bridge, and
  Orevkov application.
- [`BINARY_CUBIC_GEOMETRY.md`](BINARY_CUBIC_GEOMETRY.md): intrinsic cubic,
  `GL_2` covariance, Fitting/discriminant identities, level schemes, and
  resolvent limits.
- [`BOUNDARY_VALUATIONS.md`](BOUNDARY_VALUATIONS.md): DVR trichotomy, valuation
  criteria, and boundary-adapted family.
- [`DIFFERENTIAL_CONTROL.md`](DIFFERENTIAL_CONTROL.md): canonical derivations,
  sheet-difference derivatives, and the non-invariance result.
- [`UNIT_VALUE_SEARCH.md`](UNIT_VALUE_SEARCH.md): exact affine search equation
  and failure of content, CRT, monodromy, and rational-section shortcuts.
- [`COUNTERMODEL_LADDER.md`](COUNTERMODEL_LADDER.md): stage-by-stage mutation
  disposition and the precise source-étale wall.
- [`LITERATURE_AUDIT.md`](LITERATURE_AUDIT.md): primary-source binding for
  Orevkov and rejection of an unsupported broader prime-degree shortcut.
- [`REVIEW.md`](REVIEW.md): revision-bound local adversarial audit.
- [`HANDOFF.md`](HANDOFF.md): proposed global deltas and integration boundary.
- `verify_*.py`: exact SymPy checks.
- [`INTEGRATION.json`](INTEGRATION.json): machine-readable ownership and
  proposed integration deltas.

## Verification

```bash
python3 research/issues/rank-three-boundary-cube-unit/verify_all.py
python3 research/issues/issue-3-unramified-index/verify_index_models.py
python3 research/issues/rank-three-index-form-unit/verify_all.py
python3 scripts/validate_repository.py
python3 scripts/validate_integration_contract.py
python3 scripts/render_views.py --check
```

The first command is the packet-local exact suite. The remaining commands are
predecessor and repository checks; exact-head GitHub Actions is the authoritative
full-tree execution in this connector-only run.
