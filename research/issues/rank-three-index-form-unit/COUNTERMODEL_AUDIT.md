# Countermodel Audit and Keller-Specific Exclusion

```text
claims: IDX3U-07
status: CANDIDATE_PROVED_FOR_STATED_EXCLUSION; COUNTEREXAMPLE_SEARCH_NEGATIVE
```

## 1. Issue #3 model

The banked free cubic algebra over `B=C[u,v]` has basis `1,w,e` and

```text
w^2=w-u e,
we=-uv,
e^2=v(w-1).
```

Its index cubic is

```text
Phi(X,Y)=-(uX^3+X^2Y+vY^3),                                      (1.1)
```

and its open plane has coordinates `(u,s)` with

```text
w=us,
e=s(1-us),
v=us^3-s^2.                                                      (1.2)
```

The restricted finite map is

```text
(u,s) |-> (u,us^3-s^2),
J=s(3us-2).                                                       (1.3)
```

The moving collision lines are

```text
u+lambda+lambda^3v=0.                                             (1.4)
```

## 2. Invariant Keller failure

The failure is not merely that one displayed Jacobian polynomial happens to
vanish. The invariant statement is:

> The relative ramification/different divisor of the finite cubic map meets the
> displayed open affine plane.

Indeed, both curves `s=0` and `3us-2=0` in (1.3) are contained in that plane.

For an actual Keller normalization, restriction along `O -> A` gives

```text
Omega_{O/B} tensor_O A = Omega_{A/B}=0.                           (2.1)
```

Therefore the Kähler different/Fitting ramification support of `O/B` is
disjoint from `U`; every ramified prime divisor of `Y` lies in `Y-U`.

This proves a structural exclusion theorem:

```text
A rank-three finite normalization whose different meets the specified source
open cannot be a Keller normalization.                             (2.2)
```

It excludes the issue #3 model and every deformation retaining its interior
different pattern. It does not exclude unramified value-collision divisors,
which are not part of the different.

## 3. Boundary chart and canonical warning

Let `z=1-w`; the removed boundary curve is `E=V(u,z)`. At its generic point,
`(e,v)` are rational parameters and

```text
z=-e^2/v,
u=-e/v-e^3/v^2,
s=-v/e.                                                          (3.1)
```

Direct calculation gives

```text
det(partial(u,s)/partial(e,v)) = e/v^2.                           (3.2)
```

Thus the source volume form has a simple zero along `E` in this chart. This is
an explicit countercontrol to the tempting argument “the trace-free module is
free, therefore the canonical/different divisor is trivial.” Freeness of the
Tschirnhausen/trace-free bundle does not trivialize the inverse different as an
`O`-ideal.

The arbitrary-base binary-form context and associated inverse-different ideal
are treated in M. M. Wood, *JLMS* **83** (2011), 208-231, DOI
10.1112/jlms/jdq074. No canonical-class vanishing is imported from that
correspondence.

## 4. Triangular and affine-coordinate repairs

### Fixed first coordinate

For a polynomial deformation

```text
P=u,
Q=q(u,s),
```

one has `J=q_s`. If `J=k in C*`, then

```text
q(u,s)=k s+h(u),                                                   (4.1)
```

so `(P,Q)` is a polynomial automorphism. In particular no deformation retaining
a nonlinear `s`-term, including `us^3-s^2`, can repair the Jacobian while the
first target coordinate remains `u`.

### Affine-linear first coordinate

More generally, let

```text
P=u+alpha s.
```

The equation `J(P,Q)=k` is

```text
Q_s-alpha Q_u=k.
```

Its polynomial solutions are

```text
Q=k s+H(u+alpha s).                                                (4.2)
```

Hence `(P,Q)` is triangular after the affine source coordinate change
`(u,s)->(P,s)` and is again an automorphism. Degree-three field behavior cannot
survive this repair class.

Composing the issue #3 map with source or target polynomial automorphisms only
pulls back or multiplies its Jacobian by a nonzero constant, so it cannot erase
the interior ramification divisor.

These statements are exact, but they do not exhaust arbitrary simultaneous
nonlinear deformations of both target coordinates.

## 5. Counterexample search controls

The following models/families were checked.

1. **Issue #3 cubic.** Satisfies smoothness, normality, rationality, finite
   flatness, local monogenicity, and an open affine plane; fails source
   étaleness by (1.3).
2. **Fixed/affine first-coordinate repairs.** Constant Jacobian forces an
   automorphism by (4.1)-(4.2); no rank-three example remains.
3. **Rational symplectic cubic.** `P=x^3`, `Q=y/(3x^2)` has constant Jacobian and
   cubic field degree, but `Q` is not polynomial and the finite model does not
   contain the required whole affine source as the specified open.
4. **Target/source automorphic mutations.** Preserve the nonempty Jacobian zero
   divisor of the issue #3 source map.

No rank-three finite normal algebra containing a specified open affine plane on
which the finite map is polynomial Keller was found. The search is a set of
symbolically verified controls, not an exhaustive moduli classification.

## 6. Moving-collision pattern after exclusion

Equation (2.2) removes the model's interior **ramification**, but it does not
remove the mechanism in (1.4): two distinct étale points can have equal value
under one integral function. Therefore the invariant obstruction extracted
from the model is necessary but not sufficient for the primary theorem.

The surviving structural task is to combine boundary-only different support
with the joint source coordinates `(x,y)` and the cubic identity in
`DIFFERENTIAL_IDENTITIES.md` to exclude all such scalar collisions for one
integral section.
