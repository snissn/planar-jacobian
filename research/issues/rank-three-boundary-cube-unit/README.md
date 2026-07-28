# Issue #3 — Rank-Three Keller Boundary-Cube Unit

```text
authority: MUTABLE_NONAUTHORITATIVE
role: research-worker
task_issue: #3
owned_path: research/issues/rank-three-boundary-cube-unit/
base_commit: def93d34174cb87a1d59573bcae395a79b635040
scientific_disposition: RANK_THREE_KELLER_CASE_EXCLUDED_BY_PRIMARY_LITERATURE
review_state: local-adversarial-review ACCEPT at 3a0ba94eecd723295a4148814300242dba8ddae1
```

This worker packet uses issue-local labels `R3BC-01` through `R3BC-05`;
`R3BC-07` remains packet-local. A future integration maintainer must allocate
any global claim identifiers dynamically against then-current `main`. This
worker does not edit or preallocate shared claim, graph, queue, or generated
surfaces.

## Exact disposition

### R3BC-01 — rank-three exclusion (`literature_bound`)

Let

```text
F=(P,Q): A2_C -> A2_C,
J(P,Q) in C*,
K=C(P,Q),
L=C(x,y).
```

If `[L:K]=3`, then after localizing the target `C[x,y]` is finite étale of rank
three over `C[P,Q]`, so the polynomial map is generically three-sheeted.
Orevkov's theorem states that the Jacobian of a three-sheeted polynomial map
`C2 -> C2` cannot be constant. Thus no planar Keller map has function-field
degree three.

Primary source:

> S. Yu. Orevkov, “On three-sheeted polynomial mappings of C²,”
> *Math. USSR-Izv.* **29** (1987), 587–596,
> DOI `10.1070/IM1987v029n03ABEH000984`.

The English primary full text defines multiplicity as the number of preimages of
a generic point, states the degree-three exclusion in Theorem 1.1, and closes all
three multiplicity-three cases in the final proof. The degree-to-sheet bridge is
proved in [`FOUNDATIONS.md`](FOUNDATIONS.md).

Consequently, the simultaneous hypotheses

```text
J(P,Q) in C*,
O = normalization of C[P,Q] in C(x,y),
rank_B(O)=3
```

are inconsistent. This packet does **not** construct a section `s` with
`Phi(s) in C*`; no actual rank-three Keller normalization exists on which that
construction would have to be performed.

### R3BC-02 — boundary-cubic trichotomy (`candidate_proved`)

Conditionally retaining the predecessor's finite-flat rank-three algebra, pass
to the strict henselization of a height-one DVR and then to its geometric special
fiber. In a trace-zero frame, the reduced index cubic is exactly one of

```text
unramified split:       L1 L2 L3,
simple ramification:    L M^2,
total ramification:     L^3.
```

Thus “boundary cube” is correct only at total ramification. This is a geometric
local classification, not one simultaneous global `GL_2(B)` normal form. The
determinant calculations are in
[`BOUNDARY_VALUATIONS.md`](BOUNDARY_VALUATIONS.md).

### R3BC-03 — exact boundary classes and affine pencils (`candidate_proved`)

Let `H` be the square-free product of target height-one primes under the
normalization boundary. Finite-prime adaptation supplies a section `theta in E`
primitive at all primes dividing `H`. For every `eta in E` and `T in B`,

```text
s_T=theta+H T eta
```

remains primitive at those primes and satisfies

```text
Phi(s_T)=D+H C T+H^2 B_2 T^2+H^3 A T^3.
```

Every factor created in that pencil is therefore a nonboundary scalar-collision
divisor.

This pencil lies in one class of `E/H E`; it does **not** exhaust all integral
sections. If

```text
R_H={bar(theta) in E/H E : bar(theta) is primitive at every p|H},
```

then the unrestricted conditional unit problem is exactly the union over
`bar(theta) in R_H` of the classes `theta+H E`. The predecessor proves `R_H` is
nonempty, but does not choose a class containing a unit-index section. This
residue-class choice is the additional internal obstruction that was missing
from the first draft of the packet.

### R3BC-04 — differential control (`candidate_proved`)

No nonconstant divisor in `C[P,Q]` is invariant under both target translations.
However, the primitive-coordinate differential congruence does not make a fixed
value ideal `(Phi(s))` translation-stable because differentiating changes the
section. On a split étale chart, accidental scalar collisions remain visible as
relative sheet-value collisions rather than ramification.

### R3BC-05 — countermodel ladder terminal (`literature_bound`)

The integrated no-unit model reaches finite locally free rank three, normality,
connectedness, rational total space, a displayed open `A2`, and no nonzero
constant represented by `Phi`. It fails at the first genuine Keller condition.
In the audited finite-normalization factorization

```text
U=Spec(C[x,y]) -> Y=Spec(O) -> Spec(C[P,Q]),
```

`U` is the specified displayed source open. If the relative different has no
support on this `U`, then `Omega_{C[x,y]/C[P,Q]}=0`; the Jacobian determinant is
a unit of `C[x,y]`, hence a nonzero constant. The induced polynomial map still
has function-field degree three and is excluded by Orevkov. An arbitrary
abstract open `A2` in a rational surface is not enough. Stages 5–9 of the
requested ladder are incompatible specifically at this source-étale wall.

## Exact scope

Established at mutable packet scope:

1. the full-text-audited bridge from degree three to Orevkov's theorem;
2. the geometric local forms `L1L2L3`, `LM^2`, and `L^3` after strict
   henselization;
3. the boundary-primitive residue-class decomposition;
4. the exact affine-pencil polynomial inside each chosen class;
5. the nonboundary moving-collision interpretation;
6. the literature-bound incompatibility of the countermodel ladder with
   étaleness on the specified displayed source open at degree three.

Not claimed:

- a new proof of Orevkov's theorem;
- a constructed unit-index section;
- that one adapted boundary class exhausts all candidates;
- a theorem for rank four or higher;
- a proof of the planar Jacobian conjecture;
- scientific promotion from this construction/review round.

## Artifacts

- [`FOUNDATIONS.md`](FOUNDATIONS.md): exact setup and Orevkov application.
- [`BINARY_CUBIC_GEOMETRY.md`](BINARY_CUBIC_GEOMETRY.md): intrinsic cubic,
  covariance, Fitting/discriminant identities, levels, and resolvent limits.
- [`BOUNDARY_VALUATIONS.md`](BOUNDARY_VALUATIONS.md): local trichotomy,
  boundary classes, and affine-pencil identity.
- [`DIFFERENTIAL_CONTROL.md`](DIFFERENTIAL_CONTROL.md): canonical derivations and
  collision movement.
- [`UNIT_VALUE_SEARCH.md`](UNIT_VALUE_SEARCH.md): exact residue-class
  decomposition and restricted moving-divisor searches.
- [`COUNTERMODEL_LADDER.md`](COUNTERMODEL_LADDER.md): stage-by-stage terminal.
- [`LITERATURE_AUDIT.md`](LITERATURE_AUDIT.md): primary-source audit and rejected
  broader shortcut.
- [`REVIEW.md`](REVIEW.md): revision-bound local adversarial review.
- [`HANDOFF.md`](HANDOFF.md): proposed serialized integration deltas.
- [`INTEGRATION.json`](INTEGRATION.json): machine-readable manifest.
- `verify_*.py`: exact SymPy checks.

## Verification

```bash
python3 -m compileall -q scripts research/issues
python3 research/issues/rank-three-boundary-cube-unit/verify_all.py
python3 research/issues/issue-3-unramified-index/verify_index_models.py
python3 research/issues/rank-three-index-form-unit/verify_all.py
python3 scripts/render_views.py --check
python3 scripts/validate_repository.py
python3 scripts/validate_integration_contract.py
python3 -m unittest discover -s scripts/tests -p 'test_*.py'
python3 scripts/frontier.py
git diff --check
```

The guarded packet-local suite is run with SymPy 1.14.0. The renewed review
record pins the exact candidate and records pass/fail results for this complete
command set. Passing structural or symbolic validation does not evaluate
mathematical truth.
