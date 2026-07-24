# Issue #3 — Unramified Moving Index Divisor

```text
authority: MUTABLE_NONAUTHORITATIVE
engineering_status: DEVELOPMENT
execution_validity: NOT_A_SCIENTIFIC_EXECUTION
protocol_verdict: null
scientific_inference: scoped algebraic obstruction plus Keller-specific successor
base_commit: 296867d82d09d51ef2386de2a62067408b7f949c
base_ref: agent/bootstrap-proof-graph
branch: issue-3/unramified-index-gpt56
```

## Exact disposition

The moving-index route separates into three proved-candidate statements and
one open Keller-specific bridge.

### 1. Ramified height-one adaptation is valid

For every prescribed finite set `S` of height-one primes of
`B=C[P,Q]`, there is one integral primitive element `theta in Cbar` such that

```text
B_p[theta]=Cbar_p  for every p in S.
```

Here `Cbar_p=Cbar tensor_B B_p` is the entire finite semilocal algebra over
the DVR `B_p`; separate generation of the factors `Cbar_q` is insufficient.
Taking `S` to be the finite ramification support proves the content of
`CLM-029` at mutable candidate scope.

### 2. Exact codimension-one generation globalizes

If one integral primitive element generates `Cbar_p` at every height-one base
prime, then `B[theta]` is a hypersurface and therefore `S2`, while its
height-one local rings agree with the DVR localizations of `Cbar`, so it is
`R1`. Hence

```text
B[theta]=Cbar.
```

After this equality is proved, restriction to the Keller source gives
`f_theta'(theta) in C*`; minimality of `f_theta` then forces degree one. The
globalization and degree-one arguments are noncircular.

### 3. Purely algebraic unramified elimination is false

A rank-three algebra over `C[u,v]` is constructed with all of the following
properties:

```text
connected, smooth, normal, finite flat, rational function field,
locally monogenic on all of Spec(B), squarefree tame branch,
one unramified sheet over every generic branch point,
and an open subset isomorphic to A2.
```

Its universal index form is

```text
Phi(X,Y)=-(uX^3+X^2Y+vY^3),
```

and it never represents a nonzero constant. Thus the algebra is not globally
monogenic. Every element generating all ramified height-one
semilocalizations has a nonempty index divisor whose height-one generic
points are unramified. The family `w+lambda e` has moving collision line

```text
u+lambda+lambda^3v=0.
```

The displayed open affine plane maps to the base by

```text
(u,s) |-> (u,us^3-s^2)
```

with Jacobian `s(3us-2)`. Therefore this example is not a Keller map: the
precise missing property is etaleness on the specified open affine plane.

### 4. Surviving bridge

The only surviving version of the route is Keller-specific:

> Use the simultaneous package `L=C(x,y)`, the open immersion
> `A2_source -> Y`, and etaleness on that source to construct an integral
> primitive element whose index ideal is a unit.

Rationality, smoothness, local monogenicity, squarefree branch, fixed-sheet
monodromy, an open affine plane, factoriality of the base, generic fiber
separation, and finite-dimensional parameter counts are insufficient without
that etaleness input.

## Artifact map

- [`THEOREM-PACKET.md`](THEOREM-PACKET.md): precise quantifiers, local
  criterion, index/discriminant/different formulas, finite-prime adaptation,
  `R1/S2` globalization, and the degree-one proof.
- [`COLLISION-DIVISORS.md`](COLLISION-DIVISORS.md): Galois-closure
  Vandermonde formulas, intrinsic versus accidental contact, mutation
  criteria, primitive-element schemes, monodromy, and divisor-class limits.
- [`KELLER-NEAR-COUNTERMODEL.md`](KELLER-NEAR-COUNTERMODEL.md): the smooth
  rational non-Galois rank-three model with squarefree fixed-sheet branch and
  an explicit non-etale open affine plane.
- [`COUNTERMODELS.md`](COUNTERMODELS.md): additional diagonal, corank-two,
  Galois, and local tame controls.
- [`SOURCE-AUDIT.md`](SOURCE-AUDIT.md): exact primary-source locators and the
  boundary between imported infrastructure and self-contained proofs.
- [`ADVERSARIAL-REVIEW.md`](ADVERSARIAL-REVIEW.md): separate constructor
  adversarial audit; it is not an independent scientific acceptance.
- [`PROPOSED-SYNC.md`](PROPOSED-SYNC.md): claim-ledger, leaf, track,
  work-queue, and proof-graph synchronization plan.
- [`HANDOFF.md`](HANDOFF.md): exact surviving bridge and smallest next
  calculation.
- [`verify_index_models.py`](verify_index_models.py): optional exact SymPy
  recomputation of multiplication, index, discriminant, Vandermonde, and
  open-plane Jacobian identities.
- [`ARTIFACT-MANIFEST.sha256`](ARTIFACT-MANIFEST.sha256): SHA-256 manifest of
  the issue-scoped candidate bytes, excluding the manifest itself.

## Scientific boundary

No proof or disproof of the planar Jacobian conjecture is asserted. The
finite-normalization/open-immersion baseline remains the repository's
`CLM-003` dependency and retains the separate `L12` audit. Every new theorem
or countermodel here is `MUTABLE_NONAUTHORITATIVE` pending independent
review.
