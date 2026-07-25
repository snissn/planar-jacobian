# Qualifying Positive Weight or Minimal-Counterexample Obstruction

```text
authority: MUTABLE_NONAUTHORITATIVE
role: research-worker
issue: 41
owned_path: research/issues/qualifying-weight-descent/
base_main: 652a5e252626fa5816445651245e8a8946cee53e
review_mode: local-adversarial-review
```

## Exact disposition

This packet does **not** prove that every planar Keller pair has a primitive
positive weight of grading defect at most five. It reaches two exact bounded
results, one finite reduction, and one exact diagnosis.

1. **Named-class theorem (requested disposition 3).** The complete
   binomial-chain class `B_N` is solved for every `N>=2`. Its full Jacobian
   coefficient equations force

   ```text
   Q=c y+lambda P^N.
   ```

   One determinant-one target shear gives actual defect zero at a primitive
   positive weight. This is an actual polynomial/Keller theorem, not a
   support-only search.
2. **Fixed-representative finite reduction.** For any fixed planar Keller pair,
   the minimum of `kappa_w` over all primitive positive weights is attained on
   a finite, exactly computable set from a regular subdivision of the positive
   normal fan of `N(P)+N(Q)`.
3. **Actual affine-orbit countermodel.** For

   ```text
   A_N=(x+y^N, y+(x+y^N)^N),  N>=2,
   ```

   the determinant-one-linear and affine source/target orbit minima are exactly
   `N^2-1`, although one nonlinear target shear lowers the same actual Keller
   automorphism to defect zero. Thus no affine-only universal bound of five is
   possible, even on automorphisms.
4. **Invariant diagnosis (requested disposition 7).** The scalar written as
   `mu(F)` is inadequate until the transformation class is declared. The
   affine value is unbounded on `A_N`. At the other extreme, tame and full
   plane orbit classes coincide, and the reviewed defect-four theorem gives

   ```text
   F is an automorphism  <=>  mu_full(F)<=4.
   ```

   Conditional on independent acceptance of the exact fixed-weight defect-five
   candidate, the same equivalence holds with bound five. The full-orbit scalar
   therefore repackages the terminal invertibility question rather than
   supplying a constructive bridge. The useful replacement is a directed,
   certificate-bearing descent relation plus a lexicographic Newton core.

The global qualifying-weight problem remains open at the exact no-escape step:
force a certified complete-top descent or a bounded terminal common-power core
for an arbitrary Keller pair, while relating positive monomial weights to the
actual normalization boundary.

## Main issue-local statements

### `QWD-MIN` — class-indexed minima exist

For an explicitly declared nonempty class `C` of compensated source/target
polynomial automorphisms, define

```text
mu_C(F)=min kappa_w(beta o F o alpha),
```

where `w` is primitive positive and the transformed Jacobian remains one. Every
achieved value is a nonnegative integer by the exact Rees identity. The
identity transformation and `w=(1,1)` make the value set nonempty. The
well-ordering of `N` therefore gives an **achieved** minimum. No compactness or
finite generation of the automorphism group is used.

For the full/tame class, existence of the minimum is exact but not constructive:
a value at most four is equivalent to invertibility by the reviewed
fixed-weight theorem. This is why the directed replacement records explicit
forward certificates rather than an arbitrary orbit representative.

### `QWD-AFFINE` — exact affine-orbit obstruction

For every `N>=2`,

```text
mu_aff(A_N)=mu_SL-linear(A_N)=N^2-1.
```

For `N>=3` this exceeds five. The proof treats arbitrary affine source
coordinates, arbitrary invertible affine target mixing, translations, both
weight orientations, and possible cancellation. See
[`TRANSFORMATION_ORBIT.md`](TRANSFORMATION_ORBIT.md).

### `QWD-FAN` — finite positive-weight test

For a fixed Keller representative `G=(P,Q)`,

```text
kappa_w(G)=h_(N(P)+N(Q)-(1,1))(w).
```

This is integral linear on each cone of the common normal fan. After a finite
unimodular subdivision of the closed positive quadrant, the minimum on
primitive positive lattice vectors occurs on one of the finite positive rays,
with `(1,1)` added when the coordinate quadrant is the sole cone. See
[`NEWTON_WEIGHT_DICTIONARY.md`](NEWTON_WEIGHT_DICTIONARY.md).

### `QWD-BINOMIAL` — exact sparse Keller subclass

Let

```text
P=a x+b y^N,
Q=c y+sum_(k=0)^N q_k x^k y^(N(N-k)),
a b c q_N !=0.
```

Then `J(P,Q)=1` if and only if

```text
a c=1,
a(N-k)q_k=b(k+1)q_(k+1),  0<=k<N.
```

Consequently, with `lambda=q_N/a^N`,

```text
Q=c y+lambda P^N.
```

The target shear `Q->Q-lambda P^N` gives `(P,c y)`, and weight `(N,1)` has
`kappa=0`. Missing interior chain monomials are incompatible with nonzero
endpoints; they are not silently filled.

### `QWD-EDGE` — exact Newton/common-power interface

Whenever `kappa_w>0`, the top Rees equation gives

```text
J(in_w P,in_w Q)=0.
```

Weighted Euler identities and unique factorization then give

```text
in_w P=a H^m,  in_w Q=b H^n,  gcd(m,n)=1.
```

If the faces are edges, their lattice lengths are `m ell_H,n ell_H`; if either
face is a vertex, both are vertices. Adjacent positive edges sharing nonzero
vertices in both component polygons carry the same coprime pair. The origin is
an exact exception.

### `QWD-CORE` — corrected minimal-counterexample core

Assume a noninvertible planar Keller pair exists and minimize the six-coordinate
integer tuple in
[`MINIMAL_COUNTEREXAMPLE.md`](MINIMAL_COUNTEREXAMPLE.md) over **all** normalized
noninvertible Keller pairs and primitive positive weights. Then:

- every positive weight has defect at least five by the reviewed fixed-weight
  defect-at-most-four theorem;
- at every weight attaining the global minimum defect, no complete-top
  exponent-one shear is available;
- every positive face has common-power leading forms;
- adjacent nonzero face vertices impose the exact coprime-ratio compatibility;
- no declared source/target transformation exposes a lexicographically smaller
  pair/weight record.

The exponent-one exclusion is deliberately limited to defect-minimizing
weights. A strict descent at a nonminimizing weight may remain above the global
minimum and is not ruled out merely by minimality.

## Exact bounded search

`validate_qualifying_weight.py` performs exact integer and symbolic checks. The
default campaign includes:

- 5,611 primitive positive weights;
- the affine theorem for `A_N`, `2<=N<=10`;
- 24 fixed Keller representatives checked against the finite-fan theorem;
- all complete `B_N` Jacobian systems for `2<=N<=8`;
- every ordered pair of two-term supports in the total-degree-five triangle
  (44,100 support pairs);
- 387 saturated formal coefficient systems surviving the support and face
  filters, with no Keller survivor;
- a saturated complete `(2,3)` no-shear template;
- adjacent-edge compatibility and four semantic mutation controls.

The bounded campaign is regression/falsification evidence. It is not theorem
authority for unbounded supports.

## Dependency boundary

The only accepted low-defect theorem consumed is the independently reviewed
fixed-weight statement

```text
primitive positive w and kappa_w<=4  =>  polynomial automorphism.
```

It is bound to candidate `96fc7ec34bd3b685a0edeae7ecd4404abab7e2f1` and the
mainline freeze record. The fixed-weight defect-five theorem is **not** used as
unconditional authority. Any improvement from `kappa>=5` to `kappa>=6`, or the
full-orbit threshold-five equivalence, is stated only conditionally on
independent acceptance of the exact issue #29 candidate or on a future
independent rederivation.

## Artifact map

- [`DEFINITIONS.md`](DEFINITIONS.md) — transformation classes, minima, and the
  directed replacement invariant;
- [`TRANSFORMATION_ORBIT.md`](TRANSFORMATION_ORBIT.md) — affine theorem,
  triangular collapse, tame/full comparison, and `B_N` proof;
- [`MINIMAL_COUNTEREXAMPLE.md`](MINIMAL_COUNTEREXAMPLE.md) — well-order and
  exact consequences of minimality;
- [`NEWTON_WEIGHT_DICTIONARY.md`](NEWTON_WEIGHT_DICTIONARY.md) — support
  functions, finite fan, common powers, edge lengths, adjacency, mixed area,
  and valuations;
- [`LITERATURE_AUDIT.md`](LITERATURE_AUDIT.md) — primary-source audit and
  conflicting degree frontiers;
- [`CASE_TABLE.md`](CASE_TABLE.md) — transformation and obstruction table;
- [`COUNTERMODEL_SEARCH.md`](COUNTERMODEL_SEARCH.md) — exact bounded
  falsification design and level separation;
- [`validate_qualifying_weight.py`](validate_qualifying_weight.py) — symbolic,
  polyhedral, formal-ideal, and mutation checks;
- [`VALIDATION.md`](VALIDATION.md) — observed validation and authority limits;
- [`REVIEW.md`](REVIEW.md) — separate local-adversarial review bound to the
  construction revision;
- [`HANDOFF.md`](HANDOFF.md) — proposed shared deltas and next exact bridge;
- [`INTEGRATION.json`](INTEGRATION.json) — worker-owned integration contract.

## Issue-local labels

- `QWD-MIN`: existence and class dependence of the minimum;
- `QWD-AFFINE`: exact affine-orbit obstruction family;
- `QWD-FAN`: finite positive-weight fan theorem;
- `QWD-BINOMIAL`: exact binomial-chain Keller subclass;
- `QWD-EDGE`: common-power edge and adjacency dictionary;
- `QWD-CORE`: certified minimal-counterexample core;
- `QWD-SEARCH`: bounded exact falsification campaign.

No global `CLM-*` identifier is allocated in this worker packet.

## Scientific nonclaims

This packet does not prove `mu_C(F)<=5` for tame or full polynomial
automorphism classes, does not prove termination of complete-top descent, does
not monomialize arbitrary normalization-boundary valuations, does not consume
the candidate defect-five theorem as reviewed authority, and does not prove
`JC_2`. Merge or green CI would preserve candidate bytes; neither would promote
mathematical authority.
