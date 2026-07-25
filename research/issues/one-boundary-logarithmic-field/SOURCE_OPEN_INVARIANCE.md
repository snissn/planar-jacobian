# Preservation of the source open

> Authority: `MUTABLE_NONAUTHORITATIVE`  
> Primary labels: `OBLF-05` and `OBLF-06`

Regularity on the finite normalization and preservation of the specified source
open are different assertions. This file gives the exact bridge in the genuine
one-boundary ramified case and records why it fails in wider classes.

## 1. Height-one ideal criterion

Let `A` be a normal noetherian domain and let `p` be a height-one prime. For a
regular derivation `delta:A->A`, the following are equivalent:

```text
delta(p) subset p,
delta(p A_p) subset p A_p.                         (4.1)
```

The forward implication is immediate. Conversely, for `f in p`, regularity
gives `delta(f) in A`, while generic tangency gives `delta(f) in pA_p`.
Normality is not needed for the contraction identity
`p=A intersect pA_p`, but it is used elsewhere to extend a rational derivation
from all height-one localizations.

For a reduced divisor `D=sum D_i` on a normal affine surface, a regular field
preserves `D` exactly when it preserves every height-one prime `p_i`. An
algebraic connected group action preserves `D` when it preserves those finitely
many components; a connected group cannot act nontrivially on their finite set.

## 2. Tangency at a tame ramified component

At a generic ramified divisor in characteristic zero, after completion and an
unramified base change, write

```text
u = epsilon pi^e,
```

where `u=0` is a target branch parameter, `pi=0` is the divisor, `epsilon` is a
unit, and `e>1`. If a target field `V` is logarithmic,

```text
V(u)=u h,
```

then its regular lift satisfies

```text
e epsilon V_tilde(pi)
 = pi(epsilon h-V_tilde(epsilon)).               (4.2)
```

Thus `V_tilde(pi) in (pi)`. A regular logarithmic lift is tangent not only to
the target branch image but to every ramified divisor above it.

This calculation uses generic ramification. It gives no condition on an
unramified component of `Y-U`.

## 3. The genuine one-boundary bridge

Assume `OBLF-H0` through `OBLF-H5`. Let an actual target `G_m` action preserve
the unique reduced branch curve. By `OBLF-04`, after finite isogeny it extends
to an algebraic action on `Y`.

The relative ramification support is intrinsic and equivariant. The unique
boundary divisor `D0` is generically ramified, so it is the unique divisorial
ramification component. It follows that the lifted action preserves `D0` and
therefore

```text
U=Y-D0.                                           (4.3)
```

The restricted source action is algebraic. Equation (4.3), not regularity
alone, is what licenses the equivariant Keller theorem.

Infinitesimally, the same conclusion follows from (4.1)-(4.2): the lifted
field preserves the ideal of `D0`. Algebraic integration is still required to
turn that infinitesimal statement into a group action.

## 4. Conductor points

Suppose a boundary curve is singular and `A_C subset A_bar` is its
normalization with conductor `c`. A derivation regular on the normal surface
and tangent to the boundary prime is already regular at the ambient
codimension-two point. To induce a derivation on the singular curve image it
must additionally satisfy

```text
delta(A_C) subset A_C.
```

When it preserves both `A_C` and `A_bar`, it preserves `c` automatically. The
finite quotient `A_bar/c` therefore carries the complete curve-level descent
test. No extra ambient pole appears at the conductor point.

## 5. Failure with an unramified boundary component

If `D` has a component `E` at which `pi` is generically etale, logarithmic
tangency to the target branch does not imply

```text
V_tilde(I_E) subset I_E.
```

Such a component is not in the relative ramification support and is invisible
to the branch equation. A separate boundary ideal calculation is mandatory.
This is why `OBLF-05` assumes that the only boundary component is generically
ramified.

## 6. No-ramification one-boundary exclusion

### Theorem `OBLF-06`

Assume `OBLF-H0` through `OBLF-H3` and suppose the unique boundary divisor is
generically unramified. Then there is no nontrivial one-boundary model: the
function-field degree is one and the Keller map is an automorphism.

### Proof

Keller étaleness puts every divisorial ramification component inside `D`. Since
`D` has only one component and that component is generically unramified, the
finite map `pi:Y->A2` is unramified at every height-one point. Purity of branch
locus makes `pi` etale everywhere. We use the Stacks Project, Tag 0BMB, whose
hypotheses apply because `Y` is normal, the target is regular, and `pi` is
finite.

A connected finite etale cover of `A2_C` is trivial. This follows, for example,
from Riemann existence (SGA 1, Expose XII, Theorem 5.1) and the topological
simple connectedness of `C^2`. Hence `L=K` and `Y=A2`. The standard birational
Keller theorem then makes `F` an automorphism, so the specified open immersion
has empty boundary. `square`

The theorem rules out “one boundary component with no ramification but
nonproper sheet loss.” It does not rule out unramified components when several
other ramified boundary components are present.

## 7. Checklist before a terminal implication

A field/action may be passed to the equivariant Keller theorem only after all
of the following have been shown:

1. target logarithmic tangency;
2. regular lift to normal `Y`;
3. algebraic integration, possibly after a finite isogeny;
4. preservation of every component of `Y-U`;
5. nontrivial algebraic action on `U`;
6. equivariance of `F`.

`OBLF-04` and the unique ramified boundary supply steps 3-6 in the declared
subclass. Outside that subclass the checklist remains open.