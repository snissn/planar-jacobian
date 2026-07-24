# Track M — Filtered Equivariance and the Weighted Rees Staircase

> **Authority:** `MUTABLE_NONAUTHORITATIVE`  
> **Active issue:** [#17](https://github.com/snissn/planar-jacobian/issues/17)  
> **Scientific inference:** none

## Purpose

Exact nontrivial `G_m`-equivariance is a literature-backed rigidity class for planar Keller maps: T. Shaska proves that a `G_m`-equivariant planar Keller map is an automorphism for every sign pattern of the weights (arXiv:2607.20210, submitted 2026-07-22).

This track asks whether an arbitrary Keller pair can be reduced to that exact graded case through its weighted Rees filtration. The conversation-derived low-defect calculations are retained as theorem candidates, not as accepted results.

## 1. Weighted layers

Fix a primitive positive weight

```text
w=(p,q),  p,q>0.
```

For a polynomial `H`, let `deg_w H` be its weighted degree. Put

```text
d_P = deg_w P,
d_Q = deg_w Q,
kappa_w = d_P+d_Q-p-q.
```

Write the weighted layer expansions

```text
P = P_0+P_1+...,
Q = Q_0+Q_1+...,
```

where

```text
deg_w P_i = d_P-i,
deg_w Q_j = d_Q-j.
```

Define the weighted Rees deformation

```text
Pcal(t,x,y) = t^(d_P) P(t^(-p)x,t^(-q)y)
            = sum_i t^i P_i,
Qcal(t,x,y) = t^(d_Q) Q(t^(-p)x,t^(-q)y)
            = sum_j t^j Q_j.
```

A chain-rule computation gives the candidate identity

```text
J_x,y(Pcal,Qcal) = t^(kappa_w) J(P,Q) = t^(kappa_w).
```

Consequently the layer equations are

```text
sum_(i+j=n) J(P_i,Q_j) = 0,  n<kappa_w,
sum_(i+j=kappa_w) J(P_i,Q_j) = 1.
```

This algebra is elementary but remains subject to independent claim-and-revision audit before promotion; exact-byte hashes are optional provenance.

## 2. Resonant layers

For `i+j=kappa_w`, the bracket `J(P_i,Q_j)` has weighted degree zero. Positive source weights imply that every such bracket is a scalar. Since their sum is `1`, at least one resonant pair has nonzero constant bracket.

Conditional on the exact graded theorem, such a pair is a weighted-homogeneous coordinate pair. This gives a graded automorphism hidden among the layers of every Keller pair, but it does not by itself imply that the full filtered map is invertible.

## 3. Top-layer cancellation criterion

A useful candidate lemma is:

> If a nonzero resonant pair uses a top layer, for example
> `J(P_0,Q_j) in C*` or `J(P_i,Q_0) in C*`, then a graded source change makes the top component a coordinate. Weight positivity then forces the lower layers of that component to be triangular, so the full Keller map is an automorphism.

This needs an audit of every allowed source change and of the claim that the lower layers cannot contain a mixed monomial of smaller weight.

## 4. Candidate low-defect reduction

The conversation contains a proposed case analysis yielding

```text
kappa_w <= 3  =>  F is an automorphism.
```

The proposed mechanisms are:

- `kappa=0`: exact graded rigidity;
- `kappa=1`: every resonant position touches a top layer;
- `kappa=2`: after excluding top-layer resonance, the middle pair is a graded coordinate pair and the preceding staircase equation forces a parallel-line/common-factor reduction;
- `kappa=3`: an arithmetic exhaustion of the interior resonance positions and weights is claimed to force either a contradiction or a defect-lowering target operation.

This result is recorded as `CANDIDATE`, not `FROZEN_ACCEPTED`. It has not yet received an independent complete case audit, and no downstream claim may use it as theorem authority.

## 5. Defect 4

Defect `4` is the first level at which the central resonance can contain a genuine middle Wronskian. In the `(2,2)` pattern, after normalizing the resonant pair, the earlier equation has the form

```text
J(P_0,Q_2) + J(P_1,Q_1) + J(P_2,Q_0) = 0.
```

The term

```text
J(P_1,Q_1)
```

is absent from the defect-2 line-pencil calculation and may bend the leading common-factor fibers. It is the first explicit filtered term capable of carrying the cusp/monodromy correction seen in the normalization tracks.

The other resonance positions are `(1,3)` and `(3,1)`. All three must be treated with unequal positive weights, vanishing intermediate layers, and the full class of filtration-compatible transformations.

## 6. Allowed transformations

Any proposed reduction must state exactly which operations are used and prove both properties below:

1. the operation preserves the Keller equation `J(P,Q)=1`;
2. the operation strictly lowers the declared weighted defect or a separately declared well-founded refinement.

Relevant operations may include:

- determinant-one affine target changes;
- triangular target automorphisms `(P,Q)->(P,Q-h(P))` and their transpose;
- polynomial source automorphisms whose action on the filtration is controlled;
- filtered Hamiltonian/source changes, only after proving polynomiality and termination.

A formal cancellation of one layer that creates a larger layer elsewhere is not a reduction.

## 7. Falsification program

Before strengthening the staircase theorem, construct the most general finite layer systems satisfying the equations through defect `4` and test whether:

- a nonzero middle Wronskian survives all permitted normalizations;
- formal solutions fail to lift to actual polynomials;
- the claimed low-defect proof omitted a resonance or weight case;
- the obstruction is equivalent to a known Newton inner-polynomial condition;
- a boundary valuation or Puiseux invariant supplies a monotone termination measure.

A formal counterexample to staircase reduction is a useful scientific disposition even though it is not a Keller counterexample.

## 8. Relation to other tracks

- **Track G:** exact grading in the Wright one-boundary ring; this track supplies a filtered neighborhood of that problem.
- **Track J:** closed-orbit/no-escape degeneration; the Rees parameter is an explicit degeneration, but it may lose function-field degree or boundary valuations.
- **Track H:** the middle Wronskian may encode cusp braid monodromy.
- **Track A:** any successful defect reduction should have an interpretation on the finite-normalization boundary.
- **Track L:** all external theorem statements and exact hypotheses require primary-source audit.

## Exit

This track advances only through an exact disposition of the defect-4 packet:

1. complete reduction to smaller defect;
2. a declared subclass theorem;
3. a formal counterexample to the reduction ansatz;
4. or a strictly smaller invariant obstruction with a proved reduction to it.

Do not generalize to arbitrary defect merely by naming the unresolved middle-Wronskian problem.