# Local Adversarial Review — Qualifying-Weight Descent

```text
review_mode: local-adversarial-review
reviewed_revision: 3de516d76c8defd14a66b8727a6ae22618d368de
reviewed_base: 652a5e252626fa5816445651245e8a8946cee53e
reviewer: constructing agent in a separate review pass
disposition: ACCEPT at mutable candidate scope
```

## 1. Exact binding

This review treats the construction commit
`3de516d76c8defd14a66b8727a6ae22618d368de` as immutable. The comparison with
its base reports thirteen added files, all under
`research/issues/qualifying-weight-descent/`, and no shared scientific or
governance surface edits.

The reviewed claims are only:

1. existence of the class-indexed achieved minimum `mu_C`;
2. the exact affine-orbit formula `mu_aff(A_N)=mu_SL(A_N)=N^2-1`;
3. collapse of `A_N` by one declared nonlinear target shear;
4. the finite regular-fan test for a fixed Keller representative;
5. the weighted common-power and adjacent nonzero-vertex lemmas;
6. the complete binomial-chain theorem `Q=c y+lambda P^N`;
7. the corrected global minimal-counterexample core; and
8. the exact bounded search at the four declared realizability levels.

The review does not accept a universal tame/full bound, termination, a global
finite support list, monomialization of normalization-boundary valuations, the
fixed-weight defect-five candidate, or `JC_2`.

## 2. Disposition

`ACCEPT` at `local-adversarial-review / MUTABLE_NONAUTHORITATIVE` scope.

No mathematical blocker was found in the exact scoped statements. This is not
independent review because the same agent constructed and reviewed the packet.
The packet is integration-ready as a candidate/obstruction record only.

## 3. Critical correction made before binding

An earlier draft overclaimed that a global minimal counterexample has no
exponent-one complete-top shear at every positive weight. That is false as a
minimality inference: a strict decrease from a nonminimal defect can remain at
or above the selected global minimum.

The bound revision states the exact consequence:

```text
if kappa_u(F)=kappa_min,
then a complete-top exponent-one shear is impossible.
```

At nonminimizing weights such a shear remains a valid directed descent, but is
not itself a contradiction. The README, definitions, minimal-counterexample
record, and case table consistently use this corrected scope.

## 4. Reconstruction and adversarial checks

### 4.1 Well-order and transformation classes

The review verified that `mu_C` is an achieved minimum because its value set is
a nonempty subset of `N`; no finite generation or compactness is asserted. It
also checked that every transformation class is separately declared and that
uncompensated scalings are excluded.

The full-orbit value zero on an automorphism uses the inverse and is therefore
identified as circular as a search detector, not as a qualifying-weight
reduction.

### 4.2 Affine obstruction family

For

```text
A_N=(x+y^N, y+(x+y^N)^N),
```

the proof was recomputed after arbitrary affine source coordinates `M,L` and
arbitrary invertible affine target mixing. If

```text
D=max(deg_w M,N deg_w L),
```

then the transformed component-degree sum is at least `(N+1)D`; target
cancellation cannot remove the degree-`ND` term with a degree-`D` component.
The two source-orientation cases give the lower bound `N^2-1`, achieved at
weight `(N,1)`. Translations do not alter positive top degrees.

The signed/unsigned target-swap distinction and the exact shear
`(u,v)->(u,v-u^N)` were checked directly.

### 4.3 Finite regular-fan theorem

The review checked the support-function identity

```text
kappa_w=h_(N(P)+N(Q)-(1,1))(w),
```

linearity on common-normal-fan cones, nonnegativity on the axes by positive-ray
limits, and the unimodular-cone decomposition `w=a u+b v`. The coordinate
quadrant exception is correctly handled by adding `(1,1)` when there is no
strictly positive fan ray.

The theorem is fixed-representative only. The packet consistently requires a
support/fan rebuild after coefficient cancellation or an automorphism.

### 4.4 Common powers and adjacency

Weighted Euler identities were checked with signs:

```text
d_B B A_x-d_A A B_x=q y J(A,B),
d_B B A_y-d_A A B_y=-p x J(A,B).
```

They imply a constant rational ratio in characteristic zero, and UFD
factorization yields coprime common powers. Lattice edge lengths multiply by
the exponents. The adjacent-edge proof uses nonzero shared vertices; the
origin exception is explicitly retained and tested.

### 4.5 Complete binomial-chain theorem

For

```text
P=a x+b y^N,
Q=c y+sum q_k x^k y^(N(N-k)),
```

the complete Jacobian coefficient calculation was regenerated. The only
contributions at exponent `x^k y^(N(N-k)-1)` give

```text
a(N-k)q_k=b(k+1)q_(k+1).
```

Together with `ac=1`, the recurrence gives the complete binomial expansion
`Q=c y+lambda P^N`. No missing chain monomial can survive on the nonzero
endpoint chart, and partial cancellation does not lower the weighted degree.

### 4.6 Minimal-counterexample universe

The lexicographic tuple has six nonnegative integer coordinates, so the global
counterexample universe is well-ordered if nonempty. The independently reviewed
defect-at-most-four theorem is used only to obtain `kappa_u>=5` for every
positive weight of a noninvertible pair. Defect five is never promoted; the
improvement to six is stated conditionally.

The review confirmed the distinction between minimization over all
counterexamples and the directed invariant attached to one starting pair.

### 4.7 Search levels, saturation, and mutations

The default exact campaign was rerun and returned:

```text
primitive weights: 5611
ordered two-term support pairs: 44100
face-compatible high-defect pairs: 639
saturated formal systems: 387
formal Keller survivors: 0
adjacent nonzero-vertex solutions: 1881
mutation controls: 4
exact assertions: 2488
```

The larger JSON run with weight bound 128, `N<=12`, and 32 fan instances also
passed. The search distinguishes support, formal-layer, polynomial, and Keller
levels; saturated nonzero charts are imposed. Mutations detect omission of the
exact minimizing rays, the unsigned target swap, omission of saturation, and
the zero-vertex exception.

The bounded search is not used as unbounded theorem authority.

## 5. Literature challenge

Every load-bearing algebraic result except plane automorphism tameness is
proved internally. The audit does not consume remembered Razar/Formanek
statements whose exact primary theorem text was not available. Stable
higher-dimensional degree reductions are not treated as planar orbit
reductions. Conflicting low-degree frontiers are recorded separately.

## 6. Residual risks and next review target

The substantive open risks are not hidden cases in the scoped proofs. They are:

- whether arbitrary Keller support admits a terminating sequence of certified
  complete-top descents;
- whether a terminal coprime-power core with both exponents at least two can be
  bounded or excluded;
- whether positive monomial weights can be related to all non-toric
  normalization-boundary valuations without losing degree or sheets.

A future independent reviewer should focus on the arbitrary affine-source lower
bound, axis handling in the finite-fan theorem, and the exact boundary between
defect-minimizing and nonminimizing weights.

## 7. Authority statement

This local review supports integration of the issue-owned packet at mutable
candidate scope. It does not authorize `reviewed_scoped`, allocate a global
claim identifier, edit shared surfaces, close the qualifying-weight bridge, or
claim `JC_2`.
