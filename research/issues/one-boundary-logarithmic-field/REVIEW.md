# Adversarial review

```text
review_mode: local-adversarial-review
candidate_revision: 02547f9a1c8c72486ad2bb07a06a10fde1351af4
disposition: ACCEPT_FOR_CANDIDATE_INTEGRATION
promotion_disposition: BLOCK_PROMOTION
reviewer_independence: NOT_INDEPENDENT_SAME_ASSISTANT
```

## 1. Scope of review

The review is bound to the issue-owned packet at the pinned candidate revision,
excluding this review file and later generated synchronization views. It tests
whether the packet may be preserved on `main` as mutable candidate work. It
does not confer authority, freeze a theorem, or independently validate the
recent external equivariant Keller theorem.

Critical files reviewed:

- `LOGARITHMIC_MODULE.md`;
- `SEMISIMPLE_CLASSIFICATION.md`;
- `PRINCIPAL_PARTS.md`;
- `CONDUCTOR_AND_PUNCTURES.md`;
- `SOURCE_OPEN_INVARIANCE.md`;
- `SUBCLASS_TABLE.md`;
- `COUNTERMODELS.md`.

## 2. Corrections made before the pinned revision

Three substantive scope defects were found during the adversarial pass and
corrected before the original candidate `ad7abee8370146e40f41cb2d108cf07dc129df03`
was pinned.

1. The finite-isogeny lifting lemma had been stated for a general normal
   complex variety while its extension proof was affine. It is now stated for
   a normal affine complex variety, exactly the Keller setting.
2. The boundary expansions were called finite Laurent expansions and the
   follow-on equations were called triangular. They are now Laurent series
   with finite negative parts, and only a finite coupled negative/zero-order
   system is claimed after pole orders are fixed.
3. The elliptic control initially used only finiteness of the automorphism group
   fixing the puncture; that left open an ambient torus acting trivially on the
   curve. The final version also uses affine-plane torus linearization, whose
   fixed locus is a coordinate linear subspace.

After that pass, one notation-only change prefixed the displayed power-isogeny
line with `power map` so the repository Markdown validator would not parse
`[N]:G_m->G_m` as a reference link. No mathematical assertion changed. The
packet was reread after that edit and is therefore rebound to exact candidate
revision `02547f9a1c8c72486ad2bb07a06a10fde1351af4`.

## 3. Attack: logarithmic module

The presentation

```text
0 -> M_g -> B^2 -> (g_P,g_Q)B/(g) -> 0
```

is correct for irreducible `g`. At a maximal ideal on the curve, the Jacobian
ideal is a nonzero torsion-free module over a one-dimensional local domain and
has depth one. The depth lemma and Auslander-Buchsbaum make `M_g` locally free;
Quillen-Suslin makes it globally free. The rank and Saito determinant are
consistent in the line, graph, and cusp controls.

**Disposition:** no blocking defect. The theorem is deliberately restricted to
an irreducible reduced branch, although the plane-curve freeness phenomenon can
be stated more generally.

## 4. Attack: locally finite and semisimple decomposition

The Jordan parts are constructed on compatible finite-dimensional invariant
subspaces. Generalized eigenspaces multiply with added eigenvalues, so the
semisimple part remains a derivation and the nilpotent part is locally
nilpotent. A stable ideal remains stable because its intersection with each
finite invariant subspace is preserved by polynomial functions of the
endomorphism.

The packet correctly distinguishes three operations:

- scalar rescaling of a rank-one rational weight system;
- passage to the torus closure of a semisimple locally finite field;
- selection of a possibly different integral cocharacter.

It does not claim that irrational weight ratios become integral by scaling.

**Disposition:** no blocking defect.

## 5. Attack: classification of invariant irreducible curves

After Gutwirth linearization, a generator of an invariant principal prime is a
semi-invariant because all polynomial units are constants. The monomial support
lies on one affine lattice line. Factoring the induced one-variable polynomial
over `C` gives exactly axes, same-sign binomials, opposite-sign hyperbolic
binomials, or coordinate lines in the one-zero-weight case. Smoothness and
Abhyankar-Moh are not conflated.

**Disposition:** no blocking defect.

## 6. Attack: finite-isogeny lift

This is the highest-risk new lemma.

- On `X-C`, the cover is finite etale.
- Pulling the target action to the universal cover of `C*`, the covering-homotopy
  property produces the normalized lift.
- The additive group law follows from uniqueness.
- A period acts through the finite deck-automorphism group, so a finite-index
  period lattice acts trivially.
- Riemann existence algebraizes the resulting isomorphism of finite covers.
- Normality of `G_m x Y` extends transformed integral elements across the
  omitted divisor.

The non-Galois case is covered because only the finite automorphism group of
the given cover is used; regularity of a derivation is never substituted for
this action-level construction.

**Disposition:** acceptable for mutable candidate integration. Independent
review should recheck the covering-homotopy coherence and algebraization before
promotion.

## 7. Attack: source-open invariance

Generic logarithmic tangency gives

```text
e epsilon delta(pi)=pi(epsilon h-delta(epsilon)),
```

so the lifted field is tangent to a ramified divisor. At action level, the
relative ramification support is intrinsic. Under the explicit hypotheses that
`D` has one reduced component and that component is generically ramified, the
lifted connected torus preserves `D` and its complement `U`. The packet does
not extend this conclusion to an unramified boundary component.

**Disposition:** no blocking defect.

## 8. Attack: terminal equivariant implication

The cited statement was checked against arXiv:2607.20210v1, Theorem 3.3: a
planar Keller map equivariant for nontrivial algebraic `G_m` actions on source
and target is an automorphism. The packet invokes it only after constructing
both actions, proving source-open invariance, and proving equivariance. An
automorphism makes the normalization boundary empty, contradicting the
nontrivial one-boundary hypothesis.

**Disposition:** logically correct conditional on the exact cited theorem.
Because the source is a very recent preprint and is not independently reviewed
inside this repository, the claim remains candidate-scoped.

## 9. Attack: principal parts and conductor

Direct coefficient comparison confirms equations (2.1)-(2.3). At the lowest
source pole order, the symplectic equation is

```text
n a' b-m a b'=0,
```

and the primitive coefficient is

```text
h_(-(m+n))=mab/(m+n).
```

These identities determine compatibility but do not kill the pole. The cusp
normalization calculation gives conductor exponent `(a-1)(b-1)`, Euler field
`t partial_t`, and Hamiltonian field
`-t^((a-1)(b-1)) partial_t`. The one-puncture discussion correctly limits the
conclusion to residue vanishing.

**Disposition:** no blocking defect. The general finite reduction is only
finite after valuation and conductor type are fixed; the packet says so.

## 10. Countermodel audit

Every control names its absent Keller hypothesis. Cyclic and monomial covers
are ramified or have nonconstant units; the mixed-boundary model fails source
invariance; the exact Laurent pole is local only; the elliptic branch supplies
a logarithmic field without a target torus. None is mislabeled as a Keller
counterexample.

**Disposition:** no blocking defect.

## 11. Final review disposition

`ACCEPT_FOR_CANDIDATE_INTEGRATION` means the packet is coherent, scoped, and
suitable for preservation on current `main` with candidate claim statuses. It
establishes a substantial named subclass exclusion and a fixed-type finite
compatibility system.

`BLOCK_PROMOTION` remains mandatory because:

1. the same assistant constructed and reviewed the packet;
2. `OBLF-04` is a new action-lifting lemma needing independent scrutiny;
3. the terminal implication depends on arXiv:2607.20210v1;
4. the general smooth/generically smooth one-boundary class remains open.

The correct mainline status is mutable candidate work, not reviewed theorem and
not a proof of `JC_2`.