# Liouville exactness, conductor, and gluing

> Authority: `MUTABLE_NONAUTHORITATIVE`  
> Labels: `NTLC-04`, `NTLC-05`, and `NTLC-06`

## 1. Normalized branch Liouville theorem

Let `C=V(g)` be the reduced target branch dominated by the generically ramified
boundary divisor `E`. Let

```text
k=C(C),  ell=C(E).
```

Assume the pole-supported hypotheses of `FOUNDATIONS.md`.

### Theorem `NTLC-04`

There exists `R in k` such that

```text
dR=P dQ in Omega^1_(k/C).                          (1.1)
```

Equivalently, the pullback of `P dQ` to the normalization of the target branch
is an exact rational differential.

### Proof

Choose the completed ramified normal form and, after a finite coefficient
extension `ell'/ell`, the normalized source parameter `s=x^(-1/m)` from
`NTLC-01`. The target functions are regular power series in `s`, so the radial
coefficient `C_0` of `P dQ` is zero and its tangential coefficient is the
pullback of `P dQ` on the residue curve.

By `NTLC-01`, the coefficient `c_m` is zero. Equation (3.4) of
`LAURENT_RECURSION.md` therefore gives

```text
pullback(P dQ)=d h_0 in Omega^1_(ell'/C).          (1.2)
```

Trace (1.2) first from `ell'` to `ell`, and then from the finite separable
extension `ell/k`. Trace commutes with the universal derivation in
characteristic zero, while a form from `k` has trace equal to the field degree
times itself. Dividing by the nonzero degrees yields (1.1). `square`

The same proof applies when `y`, rather than `x`, is the coordinate with a pole,
using `(X,Y)=(y,-x)` and changing the primitive by `d(xy)`.

## 2. Residue and period consequences

An exact rational differential has:

- zero residue at every point of a smooth projective completion;
- zero class in rational/algebraic de Rham cohomology;
- no nonzero period under the complex comparison map.

Therefore any nonzero residue or de Rham class of `P dQ` excludes the ramified
pole-supported boundary type at finite order zero. This is not a residue-only
argument about `P dQ+y dx`; it follows after the full pre-ramification
Puiseux recursion proves that the source contribution is exact at order zero.

For a rational normalized branch, zero residues at all punctures are also
sufficient for rational exactness, because a residue-free rational one-form on
`P1` is the derivative of a rational function.

## 3. Regularity of the primitive on the affine normalization

Let `A_C=C[P,Q]/(g)` and let `Abar` be its finite normalization. If `R in k`
satisfies (1.1), then `R` is regular at every point of `Spec(Abar)`.
Indeed `P dQ` is regular there. If `R` had a pole of order `r>0` in a local
parameter `z`, then `dR` would have a pole of order `r+1`, contradiction.
Thus

```text
R in Abar.                                          (3.1)
```

## 4. Conductor descent class

Let

```text
c={a in A_C: a Abar subset A_C}
```

be the conductor. The normalized primitive is an exact differential already in
`Abar`. It is the differential of an element of the singular coordinate ring
exactly when

```text
[R]=0 in Abar/A_C.                                  (4.1)
```

This quotient is finite-dimensional. Equivalently, (4.1) is a finite set of
jet-matching conditions modulo the conductor:

- at a node, values on the two normalized branches must agree;
- at a cusp, the semigroup-gap coefficients must vanish;
- at a general singular point, the finite conductor quotient prescribes the
  matching jets.

Changing `R` by a constant does not alter (4.1), because constants already lie
in `A_C`.

`NTLC-05` is the exact reduction:

```text
ramified pole-supported Keller boundary
 => P dQ=dR on normalization
 => one finite target-descent class [R].            (4.2)
```

The packet does not prove that the source primitive forces `R` itself to lie in
`A_C`. A nonzero class excludes a fixed type only when its separately declared
conductor/gluing data require a primitive on the singular target branch. Without
that additional requirement, `[R]` is a finite invariant and a precise remaining
question, not an automatic contradiction.

## 5. Explicit non-toric exclusion

Consider

```text
g_ne=P(P-1)Q-1.
```

Its normalization is

```text
P=z,  Q=1/(z(z-1)),
```

so the affine curve is `P1-{0,1,infinity}` and is smooth. Direct calculation
gives

```text
P dQ=(1/z-1/(z-1)-1/(z-1)^2) dz.                  (5.1)
```

The residues at `z=0` and `z=1` are `+1` and `-1`. Hence (5.1) is not exact,
and `NTLC-04` excludes this non-toric branch from the remaining one-boundary
class. This is `NTLC-06`.

More generally, every smooth or singular branch whose normalized Liouville
class `[P dQ]` is nonzero is excluded before logarithmic-field integration,
weight extraction, or higher conductor calculations.

## 6. What remains after exactness

The exactness condition is not a torus criterion. A non-toric exact example is
recorded in `LOGARITHMIC_FIELDS.md`. Surviving types still require:

1. resolution of the finite target-descent class `[R]` when the declared gluing problem requires it;
2. vanishing of the higher twisted differential classes `beta_r` in the
   normalized Laurent recursion;
3. algebraization of the formal coefficients on the finite normalization;
4. realization of `H` as one polynomial in the actual source coordinates;
5. global Newton-support control sufficient for a qualifying weight or another
   degree-one theorem.

## 7. Boundary normalization algebra and sheet gluing

Let `A_E` be the coordinate ring of the normalization of the affine boundary
curve and let `Abar` be the normalization of the target branch. The finite map
of curves gives

```text
A_C subset Abar subset A_E,
Frac(A_C)=k subset ell=Frac(A_E).                   (7.1)
```

At a singular target point, the first inclusion is controlled by the branch
conductor. At a singular point of the boundary image or after a coefficient
extension, the second inclusion has its own finite normalization quotient.
For every fixed pole bound, a Laurent coefficient is a rational section with a
finite principal part. Its gluing conditions are therefore finite linear
conditions in the corresponding conductor quotients and finite jet spaces.

At punctures of a smooth projective completion, the equations

```text
d c_(m+r)=-beta_r/m
```

have a rational solution exactly when the differential class of `beta_r`
vanishes. This includes all residue conditions and, in positive genus, the
remaining de Rham/period conditions. The order-zero instance is `P dQ=dR`.

## 8. Connectedness, purity, and missing sheets

The local algebra does not contradict a single irreducible ramified boundary.
Over the generic branch point, the ramified valuation has an index and residue
degree, while additional unramified points of the finite fibre may lie inside
`U`. Connectedness of `Y` does not make the ramified contribution equal to the
whole generic degree, and purity has already done its available work by placing
the non-étale locus in codimension one.

Accordingly this packet proves no topological impossibility for one component
supporting the missing affine locus. A terminal argument would need a new
global statement controlling the generic fibre decomposition, monodromy, or the
way the single boundary component meets the source-open complement. That input
is not contained in the Laurent recursion.
