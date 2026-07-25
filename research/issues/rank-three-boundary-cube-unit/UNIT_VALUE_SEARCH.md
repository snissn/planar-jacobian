# Unit-Value Search and the Exact Moving-Divisor Equation

```text
authority: MUTABLE_NONAUTHORITATIVE
local_claims: R3BC-03, R3BC-04
terminal_context: R3BC-01 excludes the actual rank-three Keller case
```

## 1. The exact integral question

Conditionally retain the rank-three algebra

```text
B=C[P,Q],
O=B direct_sum E,
Phi:E -> B.
```

The desired fixed section is

```text
s=U e1+V e2,
Phi(U,V)=lambda in C*.
```

By homogeneity, a unit value automatically makes `(U,V)` unimodular. The
following substitutes are insufficient and are not used:

```text
content(Phi)=B,
gcd(Phi(s_1),...,Phi(s_m))=1,
local monogenicity,
generic or rational primitivity,
a formal primitive element.
```

The predecessor supplied the first two integral certificates and explicitly
showed why they do not imply one unit value.

## 2. Boundary-first normalization of the search

Let `H` be the square-free product of all target height-one primes under the
normalization boundary. Choose `theta in E` primitive at every prime dividing
`H`, as in `BOUNDARY_VALUATIONS.md`. For an arbitrary second section `eta in E`,
search only in

```text
s_T=theta+H T eta,
T in B.
```

This loses no boundary flexibility relevant to the unit problem: every `s_T`
remains primitive at every boundary prime.

Let

```text
D=Phi(theta),
C=3 C_Phi(theta,theta,eta),
B_2=3 C_Phi(theta,eta,eta),
A=Phi(eta).
```

Then the exact one-parameter index polynomial is

```text
G_eta(T)
 = Phi(s_T)
 = D+H C T+H^2 B_2 T^2+H^3 A T^3.         (2.1)
```

The unit problem is exactly

```text
G_eta(T)=lambda,
eta in E,
T in C[P,Q],
lambda in C*.                              (2.2)
```

At each boundary prime `p|H`, equation (2.1) reduces to `D`, a unit. Hence every
irreducible factor of `G_eta(T)` is a nonboundary collision component.

## 3. Sheetwise meaning of the affine family

On a split étale chart, let `z_i` be the sheet values of `theta` and `w_i` the
sheet values of `eta`. Then

```text
G_eta(T)
 = product_{i<j} ((z_j-z_i)+H T(w_j-w_i)).  (3.1)
```

A zero of `G_eta(T)` is therefore one of the three equations

```text
(z_j-z_i)+H T(w_j-w_i)=0.                  (3.2)
```

Equation (3.2) identifies two scalar values but not two source points. Since the
cover is étale there, it is an excess index divisor, not a branch divisor.

## 4. Why Chinese remainder arguments stop

For a finite set of height-one primes, one may prescribe `T mod p` to avoid the
finitely many bad residue classes at those primes. The resulting polynomial
`T(P,Q)` generally has positive degree. Substitution into (2.1) then produces a
new nonconstant polynomial whose irreducible factors were absent from the finite
list.

The obstruction is not lack of local choices. It is the absence of a theorem
that the entire divisor of `G_eta(T)` is supported on the already-controlled
finite set. Equation (2.1) proves the opposite boundary statement: any new factor
is automatically *outside* that set.

Thus a CRT construction is valid only if supplemented by a global theorem such
as

```text
all zeros of G_eta(T) lie over H=0,
```

but no such theorem follows from source étaleness or the different.

## 5. Constant and affine target choices

### 5.1 Constant `T`

Taking `T=c in C` gives a one-dimensional pencil of sections. Even if the three
linear sheet-difference equations in (3.2) avoid every boundary component, their
eliminants in `P,Q` can define nonempty curves. A generic constant avoids
identical vanishing, not pointwise vanishing over the entire target.

### 5.2 Affine-linear `T`

An affine-linear polynomial can satisfy more interpolation conditions but also
raises the degree of `G_eta(T)`. There is no monotonicity of collision support:
removing one component can create another. This is the exact “moving divisor”
phenomenon already observed in the predecessor packet.

### 5.3 Iteration

Replacing a bad section by another affine combination and repeating does not
give a descending invariant. Neither total degree, number of components, nor
intersection multiplicity is known to decrease. Without such a well-founded
measure, iteration is not a proof.

## 6. Fixed-section geometry does not force a global point

The scheme

```text
X_lambda: Phi(U,V)=lambda
```

has the following geometric fibers:

```text
split etale:         a three-punctured genus-one curve,
simple ramification: G_m,
total ramification:  three disjoint A1 components.
```

This variation prevents a uniform torsor interpretation. In particular:

- the split fibers are not affine spaces;
- `Pic(B)=0` and `H^1(B,O_B)=0` do not force a section;
- a rational primitive direction lies only in `Phi != 0`, and scaling it to a
  constant level requires a cube root in `K`;
- the source open supplies many rational functions but no canonical integral
  point on one fixed level.

## 7. Norm-form and resolvent attempts

The binary index cubic is a Vandermonde-type alternating product, not the norm
of a canonical element of the cubic field. A norm representation after choosing
coordinates would still require a global element of prescribed norm and would
not control integral index.

The quadratic resolvent records the square class of the cubic discriminant. It
can distinguish `S_3` from `A_3` monodromy but cannot select one of the three
sheets in either transitive case. A distinguished resolvent point therefore does
not yield a distinguished integral primitive section.

## 8. Differential attempts

No nonconstant divisor can be invariant under both target translations, but the
fixed-section ideal `(G_eta(T))` is not known to be stable under either one. The
canonical derivations move the section coefficients and the parameter `T`.
Consequently, the minimal-degree argument for translation-stable ideals cannot
be applied to `G_eta(T)`.

The exact primitive-coordinate congruence controls denominators and the relative
different. It leaves the three scalar-collision factors in (3.1) unconstrained
at unramified points.

## 9. Strongest internal reduction

Without invoking Orevkov, the smallest exact remaining equation is (2.2):

```text
D+H C T+H^2 B_2 T^2+H^3 A T^3=lambda in C*.
```

Its defining properties are:

1. `D` is a unit at every boundary prime;
2. all higher coefficients carry the corresponding powers `H,H^2,H^3`;
3. every divisor of the left side is a nonboundary scalar collision;
4. no finite-prime patch controls all such divisors;
5. neither the different nor source étaleness forbids them.

This is stronger and more precise than saying only that “one moving divisor
remains.”

## 10. Terminal rank-three disposition

For an actual planar Keller map, Orevkov's theorem makes the conditional search
empty: field degree three cannot occur. The unit-value equation is retained as
useful algebra for neighboring finite covers and for auditing proposed internal
proofs, but it is no longer a necessary bridge for the rank-three Keller leaf.
