# Minimal-Counterexample Program

## 1. Two minimization universes

This packet does not conflate the following constructions.

1. `mu_C(F)` and `nu_D(F)` are quantities attached to one starting pair and an
   explicitly declared transformation class or directed descent relation.
2. The contradiction program below assumes that at least one noninvertible
   normalized planar Keller pair exists and minimizes over the set of **all**
   such pairs and all primitive positive weights.

Polynomial source and target automorphisms preserve invertibility, so every
transformed noninvertible pair remains in the global contradiction universe.

## 2. The well-order

For a normalized noninvertible Keller pair `G=(R,S)` and primitive positive
weight `w`, define

```text
Lambda(G,w)=(
  kappa_w(G),
  deg(R)+deg(S),
  |Supp(R)|+|Supp(S)|,
  e_+(R)+e_+(S),
  2 Area(N(R)+N(S)),
  d_R(w)+d_S(w)
).                                                        (2.1)
```

Every coordinate is a nonnegative integer:

- `kappa_w` is nonnegative by the exact Rees identity;
- ordinary and weighted degrees and support cardinalities are integers;
- a polygon has finitely many compact positive-normal edges;
- twice the area of a lattice polygon is an integer, with zero used for a
  segment or point.

Lexicographic order on `N^6` is a well-order. If the counterexample set is
nonempty, the set of values (2.1) has a least element, achieved by at least one
pair/weight record. Fix a minimizer `(F,w)` and write

```text
F=(R,S),
kappa_min=kappa_w(F).
```

The following proposed coordinates are omitted deliberately:

- a count of transformations preserving a minimum can be infinite because of
  stabilizers;
- normalization-boundary valuation count depends on a chosen finite model and
  is not determined by Newton support;
- maximal common-power exponent is recoverable after a support is fixed but is
  not required before degree, support count, edge count, and area.

## 3. Immediate low-defect consequence

The independently reviewed fixed-weight theorem says

```text
kappa_u(F)<=4  =>  F is a polynomial automorphism.
```

Since `F` is assumed noninvertible,

```text
kappa_u(F)>=5 for every primitive positive u.            (3.1)
```

No defect-five theorem is used in (3.1). Conditional on independent acceptance
of the exact issue #29 fixed-weight candidate, (3.1) improves to
`kappa_u(F)>=6`.

In particular, for every positive weight, the top Rees equation is a
zero-bracket equation.

## 4. No complete-top exponent-one shear at a minimizing weight

Let a primitive positive `u` satisfy

```text
kappa_u(F)=kappa_min
```

and suppose its top layers have

```text
R_0=A H,
S_0=B H^n,
```

with `A,B in C*`; the transposed case is identical. The determinant-one target
shear

```text
(R,S)->(R,S-(B/A^n)R^n)                                 (4.1)
```

cancels the complete top layer of `S`. Every other term of `R^n` has strictly
smaller `u`-weight. Hence the recomputed actual defect is a nonnegative integer
strictly below `kappa_min`. The transformed pair remains normalized Keller and
noninvertible, contradicting global minimality.

Therefore:

```text
at every defect-minimizing positive weight,
the coprime common-power exponents satisfy m,n>=2.       (4.2)
```

The smallest possible unordered pair at such a face is `{2,3}`.

This conclusion is intentionally not asserted for every nonminimizing weight.
A strict decrease from `kappa_u>kappa_min` can remain at or above
`kappa_min`; minimality alone does not exclude that local descent. It is still
a valid directed descent certificate, but not a contradiction to the selected
global minimum.

## 5. No named transformation exposes a smaller record

Let `alpha,beta` be any explicitly considered compensated source and target
automorphisms: determinant-one linear, affine, fixed-weight graded source,
triangular target, tame, or full. Put

```text
F'=beta o F o alpha.
```

Then `F'` is normalized Keller and noninvertible. If some primitive positive
`u` satisfied

```text
Lambda(F',u)<_lex Lambda(F,w),                           (5.1)
```

then `(F,w)` would not be a global minimum. Thus no declared coordinate
orientation, target combination, or polynomial automorphism hides a smaller
pair/weight record.

This is not a claim that `Lambda` is invariant. It is a consequence of
minimizing over all counterexamples after all such transformations.

## 6. Every positive Newton face has common-power leading forms

Let `u` be any primitive positive weight. By (3.1), `kappa_u(F)>0`, so

```text
J(in_u R,in_u S)=0.                                     (6.1)
```

Both initial forms are nonconstant. The internal weighted common-power lemma
in [`NEWTON_WEIGHT_DICTIONARY.md`](NEWTON_WEIGHT_DICTIONARY.md) gives

```text
in_u R=a_u H_u^m(u),
in_u S=b_u H_u^n(u),
gcd(m(u),n(u))=1.                                       (6.2)
```

If either exposed face is a vertex, both are vertices and `H_u` is a monomial.
If either is an edge, both are parallel edges and their lattice lengths satisfy

```text
ell_R=m(u) ell_H,
ell_S=n(u) ell_H.
```

At a weight attaining `kappa_min`, (4.2) says `m(u),n(u)>=2`. Other positive
faces have exact common-power data but may retain an exponent-one local descent
that does not lower the global minimum.

## 7. Adjacent supporting weights

Suppose adjacent positive edge normals `u,u'` share nonzero vertices in both
component polygons. The common-root endpoint equations are

```text
v_R=m(u) h=m(u') h',
v_S=n(u) h=n(u') h'.                                      (7.1)
```

Because the shared vertices are nonzero, (7.1) gives equal rational ratios.
Coprimality gives

```text
(m(u),n(u))=(m(u'),n(u')).                               (7.2)
```

Thus the coprime pair is constant along an adjacent-edge chain connected
through nonzero shared vertices in both polygons.

The origin is an exact exception: every positive multiple of zero is zero, so
different coprime pairs can meet there. Axis vertices and transitions that do
not share both component vertices remain separate cases. No global common
composite is inferred merely by walking around the polygons.

## 8. Jacobian constraints at transitions

For each positive supporting weight `u`, write the actual layers

```text
R=sum_i R_i,
S=sum_j S_j.
```

The first two equations are

```text
J(R_0,S_0)=0,                                            (8.1)
J(R_0,S_1)+J(R_1,S_0)=0.                                (8.2)
```

Inside a normal-fan chamber, both faces are vertices and (8.1) forces the two
exponent vectors to be parallel. On a wall, (8.1) is the common-power edge
equation. Equation (8.2) is the first exact correction compatibility between
adjacent faces.

A proposed transition is invalid unless every actual monomial in `R_1,S_1` is
included. Conversely, an absent lattice point contributes zero. Cross-edge
cancellation is handled only after collecting coefficients at the same
exponent.

## 9. No hidden orientation or lower-defect representative

Because (2.1) ranges over every primitive positive weight of every normalized
noninvertible Keller pair:

- swapping source axes and relabeling weights cannot expose a smaller record;
- the signed target swap `(R,S)->(S,-R)` cannot expose one;
- affine source orientation, target linear mixing, triangular target shears,
  or tame transformations cannot expose one;
- a fixed-weight graded source normalization cannot discard a simultaneous
  resonant term and then claim a smaller record.

Any transformed support is recomputed from actual nonzero coefficients before
comparison.

## 10. Missing monomials and cancellation

After every transformation, recompute

```text
Supp(R), Supp(S), N(R), N(S), d_R(u), d_S(u), kappa_u.
```

Different polynomial contributions can land on the same exponent and cancel.
Such cancellation lowers a weighted degree only if **every** coefficient on the
former exposed face cancels. Partial cancellation is not descent.

The binomial-chain theorem is the exact model: the full Jacobian recurrence
forces the entire top polynomial to be `lambda P^N`; only then does the target
shear strictly lower the actual defect. Omitting one chain monomial destroys
the coefficient equations rather than creating a generic hole.

## 11. The surviving exact core

The deductions reduce a global minimal counterexample to the following
support/face obstruction.

1. Every positive weight has defect at least five, conditionally six only after
   independent defect-five acceptance.
2. Every positive initial pair has common-power form.
3. At every defect-minimizing face, both coprime exponents are at least two.
4. The coprime pair is constant along nonzero adjacent-edge chains.
5. Changes of pair can occur only through zero/axis vertices or through failure
   to share both component vertices.
6. Every transition satisfies the complete Rees correction equations.
7. No named polynomial source/target transformation exposes a smaller
   lexicographic record.

This is not a finite global list. The finite-fan theorem makes the weight set
finite for one fixed support, but no theorem here bounds all possible
minimizing supports or turns all positive-face chains into one global composite.

## 12. Relation to normalization and one-boundary work

A positive Newton weight is a toric monomial valuation in chosen polynomial
source coordinates. A divisor on the finite normalization may be nonmonomial
and may carry key-polynomial, Puiseux, Laurent, or conductor data. The
one-boundary packet excludes the unramified and target-toric subclasses but
leaves a non-toric Laurent--conductor system.

No argument here identifies that system with the Newton core. A simultaneous
monomialization/no-escape theorem remains necessary before this support
reduction can control every normalization-boundary valuation.
