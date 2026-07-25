# Semisimple classification and the one-boundary obstruction

> Authority: `MUTABLE_NONAUTHORITATIVE`  
> Labels: `OBLF-02` through `OBLF-05`

This file starts with a locally finite derivation and ends with an algebraic
action only when the exact integrality hypotheses are present. The two notions
are not conflated.

## 1. Algebraic Jordan decomposition

Let `R` be a finitely generated `C`-algebra and let `delta` be a locally finite
derivation: every element of `R` lies in a finite-dimensional
`delta`-invariant vector space.

### Proposition `OBLF-02`

There are unique commuting derivations

```text
delta = delta_s + delta_n
```

such that `delta_s` is semisimple and locally finite and `delta_n` is locally
nilpotent. If an ideal `I` is stable under `delta`, then it is stable under
both `delta_s` and `delta_n`.

### Proof

On every finite-dimensional invariant subspace, take the ordinary additive
Jordan-Chevalley decomposition. The decompositions agree on nested invariant
subspaces by uniqueness. Generalized eigenspaces multiply according to

```text
R_lambda R_mu subset R_(lambda+mu),
```

so the semisimple part satisfies Leibniz; the nilpotent part is the difference
of two derivations. It is nilpotent on every finite invariant subspace and is
therefore locally nilpotent. If `f in I`, choose a finite invariant subspace
`W` containing `f`. The subspace `I intersect W` is `delta`-stable, and both
Jordan parts of `delta|W`, being polynomials in that endomorphism, preserve it.
`square`

Applied to `R=B=C[P,Q]` and `I=(g)`, the semisimple part of a locally finite
logarithmic field is again logarithmic.

## 2. What “integral weights” means

A semisimple locally finite derivation gives an eigenspace decomposition

```text
B = direct_sum_(lambda in Gamma) B_lambda.
```

It is the infinitesimal generator of an algebraic `G_m` action exactly when,
after the chosen normalization of the parameter, all occurring eigenvalues are
integers. Multiplying the derivation by one scalar only works when the
nonzero eigenvalues are rationally commensurable. Irrational weight ratios
cannot be made integral by rescaling.

There is nevertheless an algebraic torus attached to any semisimple locally
finite derivation. Decompose a finite set of algebra generators into
`delta_s`-eigenvectors and take the Zariski closure of the analytic one-parameter
subgroup on their finite-dimensional span. This closure is a diagonalizable
algebraic torus `T` acting on `B`. If `(g)` is `delta_s`-stable, it is stable
under the dense one-parameter subgroup and hence under `T`. Since the only
units of `B` are constants, `g` is a `T`-semi-invariant. A nonzero integral
cocharacter `G_m->T` then supplies a possibly different integral-weight
logarithmic field. This replacement is recorded explicitly; it is not called
a rescaling of `delta_s`.

## 3. Linearization and semi-invariant branch equations

An actual nontrivial algebraic `G_m` action on `A2_C` is polynomially
linearizable. We use A. Gutwirth, *The action of an algebraic torus on the
affine plane*, Trans. Amer. Math. Soc. 105 (1962), 407-414. Thus, after a
polynomial target automorphism, the action has the form

```text
t.(u,v) = (t^m u, t^n v),  (m,n) in Z^2, (m,n)!=(0,0).     (3.1)
```

If the irreducible curve `g=0` is invariant, its principal prime ideal is
stable. The connected torus sends each generator to another generator, and the
only units of `C[u,v]` are constants. Hence `g` is a semi-invariant:

```text
g(t^m u,t^n v)=t^d g(u,v).                                 (3.2)
```

Every monomial in `g` lies on the affine lattice line `mi+nj=d`.

### Irreducible forms

Factoring the resulting one-variable polynomial over `C` gives the following
complete list, up to constants and interchange of `u,v`.

1. If `m,n` have the same nonzero sign, an irreducible semi-invariant is an
   axis or

   ```text
   u^a-c v^b,  c in C*, gcd(a,b)=1.                         (3.3)
   ```

2. If `m,n` have opposite signs, an irreducible semi-invariant is an axis or

   ```text
   u^a v^b-c,  c in C*, gcd(a,b)=1.                         (3.4)
   ```

3. If exactly one weight is zero, an irreducible invariant curve is a
   coordinate line.

The smooth curves in (3.3) are coordinate `A1` curves: at least one of `a,b`
is one. The curves in (3.4) are smooth copies of `G_m`. If both exponents in
(3.3) exceed one, the origin is a cusp-type singular point.

The coordinate change in this classification is not silently discarded. It
replaces `(P,Q)` by a polynomial coordinate pair `(u,v)`. It induces an
abstract automorphism of `B`, carries the finite normalization and branch data
along, and multiplies the displayed Keller determinant by the nonzero constant
Jacobian of the target automorphism.

For a smooth branch already known to be abstractly `A1`, the stronger
coordinate conclusion can also be obtained from S. S. Abhyankar and T. T. Moh,
*Embeddings of the line in the plane*, J. Reine Angew. Math. 276 (1975),
148-166, DOI 10.1515/crll.1975.276.148. Smoothness or rationality alone is not
sufficient for that theorem.

## 4. Finite-isogeny lifting lemma

The central new step begins with an actual target action.

### Theorem `OBLF-04`

Let `X` be a normal affine complex variety, let `pi:Y->X` be a finite morphism
with `Y` normal and integral, and let `C subset X` be a reduced divisor such
that

```text
pi:Y^o=pi^(-1)(X-C) -> X^o=X-C
```

is finite etale. Suppose an algebraic `G_m` action on `X` preserves `C`. Then
there is an integer `N>0` such that the action precomposed with

```text
power map [N]: G_m -> G_m,  t |-> t^N,
```

lifts to an algebraic `G_m` action on `Y`, and `pi` is equivariant.

### Proof

**Topological lift on the etale locus.** Analytify. Pull the target action back
to the universal cover `exp:C_add->C*`. The covering-homotopy property, applied
to the contraction of `C_add`, gives a unique holomorphic map

```text
a_tilde:C x Y^o -> Y^o
```

lifting the target action and equal to the identity at parameter zero. The
additive group law holds by uniqueness of the lift. A period `2 pi i k` acts
as an automorphism of the finite cover `Y^o->X^o`. Its image lies in the finite
group `Aut_(X^o)(Y^o)`, so some positive multiple `N` of the period acts
trivially. The lifted action therefore descends to `C/(2 pi i N Z)`, which is
`G_m`, while its action on `X^o` is the original action precomposed with
`t|->t^N`.

**Algebraization.** The preceding lift is an isomorphism between the two finite
topological covers of `G_m x X^o` obtained by pulling `Y^o` back along the
action and the second projection. Riemann existence for finite etale covers
algebraizes this isomorphism. We use SGA 1, Expose XII, Theorem 5.1. The cocycle
identity holds analytically and hence algebraically.

**Extension across `C`.** Work on coordinate rings. The action on `Y^o` acts on
the function field of `Y`. If `z in O_Y` is integral over `O_X`, its transformed
element satisfies the transformed monic equation and is integral over the
coordinate ring of `G_m x X`, hence also integral over the coordinate ring of
`G_m x Y`. The product `G_m x Y` is normal, so the transformed element belongs
to that coordinate ring. Thus the action morphism extends across `Y-Y^o`. The
group law and equivariance extend from the dense open subset. `square`

The isogeny is necessary in general: an orbit loop can act by a nontrivial
finite deck transformation. The theorem does not say that an arbitrary
regular derivation on `Y` is complete.

## 5. Preservation of the unique ramified boundary

Return to the Keller normalization and assume `OBLF-H0` through `OBLF-H5`.
The finite map is etale over `X-C`; purity excludes an additional isolated
non-etale locus. A target action preserving `C` therefore lifts after the
isogeny of `OBLF-04`.

The ramification support on `Y` is intrinsic and is preserved by every
equivariant automorphism. Because `D0` is the only boundary divisor and is
generically ramified, it is the unique divisorial ramification component.
The connected lifted torus preserves it. Hence

```text
U=Y-D0
```

is invariant. The restricted action on `U` is algebraic and nontrivial: if it
were trivial, equivariance and dominance of `F` would make the target action
trivial.

## 6. One-boundary semisimple obstruction

### Theorem `OBLF-05`

Under `OBLF-H0` through `OBLF-H5`, the reduced branch curve cannot be preserved
by a nontrivial target `G_m` action unless the boundary is empty. Equivalently,
a nontrivial one-boundary model satisfying those hypotheses contains no
nonzero semisimple locally finite integral-weight target field in
`Der_C(B)(-log g)`.

### Proof

The target action lifts after finite isogeny by `OBLF-04`. Section 5 proves
that it preserves `U`, and `F:U->X` is equivariant for nontrivial algebraic
`G_m` actions on source and target. T. Shaska, *Graded Keller maps and the
Jacobian Conjecture*, arXiv:2607.20210v1, Theorem 3.3, states that a planar
Keller map equivariant for nontrivial algebraic `G_m` actions on source and
target is an automorphism. Therefore `L=K`, `O=B`, `Y=X`, and the specified
open immersion has empty boundary. This contradicts `OBLF-H3`. `square`

The theorem is conditional on the exact cited equivariant Keller result,
which is currently recorded in the repository as a literature-bound input. It
is not a proof of that external theorem.

## 7. Consequences for named branch classes

The obstruction immediately excludes the following as reduced branch curves
of a nontrivial generically ramified one-boundary Keller normalization:

- a coordinate line;
- any irreducible weighted-homogeneous plane curve;
- a weighted cusp `u^a-cv^b=0`;
- a hyperbolic monomial curve `u^a v^b=c`;
- any smooth `A1` branch, after Abhyankar-Moh;
- any branch preserved by a higher-dimensional target torus, after choosing a
  cocharacter acting nontrivially on the target.

It does **not** prove that an arbitrary smooth or one-place branch has a torus
symmetry. The remaining class is exactly the non-semi-invariant class addressed
by the principal-part and conductor system.