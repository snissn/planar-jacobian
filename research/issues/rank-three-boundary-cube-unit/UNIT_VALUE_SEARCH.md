# Unit-Value Search and a Boundary-Stable Moving-Divisor Family

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

## 2. Boundary-first restricted search

Let `H` be the square-free product of all target height-one primes under the
normalization boundary. Choose `theta in E` primitive at every prime dividing
`H`, as in `BOUNDARY_VALUATIONS.md`. For an arbitrary second section `eta in E`,
consider the affine pencil

```text
s_T=theta+H T eta,
T in B.
```

Every member remains primitive at every boundary prime. This is a useful
**restricted** search, not an exhaustion of `E`: all its members have the same
class as `theta` in `E/H E`. A hypothetical unit-index section can have a
different primitive residue class at one or more boundary components. The
finite-prime adaptation theorem supplies at least one boundary-primitive class,
but it does not show that a unit-valued section can be moved into that chosen
class while preserving its index value.

Let

```text
D=Phi(theta),
C=3 C_Phi(theta,theta,eta),
B_2=3 C_Phi(theta,eta,eta),
A=Phi(eta).
```

Then the exact index polynomial for this pencil is

```text
G_{theta,eta}(T)
 = Phi(s_T)
 = D+H C T+H^2 B_2 T^2+H^3 A T^3.         (2.1)
```

Consequently,

```text
G_{theta,eta}(T)=lambda,
eta in E,
T in C[P,Q],
lambda in C*                              (2.2)
```

is a sufficient unit-search subproblem inside the single congruence class
`theta+H E`. It is not equivalent to the unrestricted unit problem for one
fixed `theta`.

At each boundary prime `p|H`, equation (2.1) reduces to `D`, a unit. Hence every
irreducible factor of `G_{theta,eta}(T)` is a nonboundary collision component.

## 3. Exact residue-class decomposition

Define the set of boundary-primitive residue classes

```text
R_H={bar(theta) in E/H E :
     bar(theta) generates O_p/p O_p for every p|H}.
```

The predecessor's finite-prime adaptation theorem proves `R_H` is nonempty.
For any `bar(theta) in R_H` and any lift `theta in E`, the integral sections with
that residue class are exactly

```text
theta+H eta,  eta in E.
```

Therefore the unrestricted conditional unit question is exactly

```text
find bar(theta) in R_H, a lift theta, eta in E, and lambda in C*
such that Phi(theta+H eta)=lambda.          (3.1)
```

Equation (3.1) is a union over all boundary-primitive residue classes. The
fixed-`theta` pencil (2.1) studies one class and one direction at a time. No
finite list of classes, canonical class, or descent from an arbitrary unit
section to the initially chosen `theta` is proved.

## 4. Sheetwise meaning of the affine pencil

On a split étale chart, let `z_i` be the sheet values of `theta` and `w_i` the
sheet values of `eta`. Then

```text
G_{theta,eta}(T)
 = product_{i<j} ((z_j-z_i)+H T(w_j-w_i)).  (4.1)
```

A zero of `G_{theta,eta}(T)` is therefore one of the three equations

```text
(z_j-z_i)+H T(w_j-w_i)=0.                  (4.2)
```

Equation (4.2) identifies two scalar values but not two source points. Since the
cover is étale there, it is an excess index divisor, not a branch divisor.

## 5. Why Chinese remainder arguments stop

For a finite set of height-one primes, one may prescribe `T mod p` to avoid the
finitely many bad residue classes at those primes. The resulting polynomial
`T(P,Q)` generally has positive degree. Substitution into (2.1) then produces a
new nonconstant polynomial whose irreducible factors were absent from the finite
list.

The obstruction is not lack of local choices. It is the absence of a theorem
that the entire divisor of `G_{theta,eta}(T)` is supported on the
already-controlled finite set. Equation (2.1) proves the opposite boundary
statement: any new factor is automatically *outside* that set.

Thus a CRT construction is valid only if supplemented by a global theorem such
as

```text
all zeros of G_{theta,eta}(T) lie over H=0,
```

but no such theorem follows from source étaleness or the different.

## 6. Constant and affine target choices

### 6.1 Constant `T`

Taking `T=c in C` gives a one-dimensional pencil of sections. Even if the three
linear sheet-difference equations in (4.2) avoid every boundary component, their
eliminants in `P,Q` can define nonempty curves. A generic constant avoids
identical vanishing, not pointwise vanishing over the entire target.

### 6.2 Affine-linear `T`

An affine-linear polynomial can satisfy more interpolation conditions but also
raises the degree of `G_{theta,eta}(T)`. There is no monotonicity of collision
support: removing one component can create another. This is the exact “moving
divisor” phenomenon already observed in the predecessor packet.

### 6.3 Iteration

Replacing a bad section by another affine combination and repeating does not
give a descending invariant. Neither total degree, number of components, nor
intersection multiplicity is known to decrease. Without such a well-founded
measure, iteration is not a proof.

## 7. Fixed-section geometry does not force a global point

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

## 8. Norm-form and resolvent attempts

The binary index cubic is a Vandermonde-type alternating product, not the norm
of a canonical element of the cubic field. A norm representation after choosing
coordinates would still require a global element of prescribed norm and would
not control integral index.

The quadratic resolvent records the square class of the cubic discriminant. It
can distinguish `S_3` from `A_3` monodromy but cannot select one of the three
sheets in either transitive case. A distinguished resolvent point therefore does
not yield a distinguished integral primitive section.

## 9. Differential attempts

No nonconstant divisor can be invariant under both target translations, but the
fixed-section ideal `(G_{theta,eta}(T))` is not known to be stable under either
one. The canonical derivations move the section coefficients and the parameter
`T`. Consequently, the minimal-degree argument for translation-stable ideals
cannot be applied to `G_{theta,eta}(T)`.

The exact primitive-coordinate congruence controls denominators and the relative
different. It leaves the three scalar-collision factors in (4.1) unconstrained
at unramified points.

## 10. Strongest internal search statement

Without invoking Orevkov, the exact conclusions are:

1. the unrestricted unit problem decomposes as (3.1) over all
   boundary-primitive classes in `E/H E`;
2. for each chosen class and direction, the exact pencil equation is

   ```text
   D+H C T+H^2 B_2 T^2+H^3 A T^3=lambda in C*;
   ```

3. `D` is a unit at every boundary prime and all higher coefficients carry the
   powers `H,H^2,H^3`;
4. every divisor produced inside the pencil is a nonboundary scalar collision;
5. failure of one chosen class or pencil does not exclude a unit section in a
   different boundary residue class;
6. no finite-prime patch controls all newly created nonboundary divisors.

Thus the packet isolates a boundary-stable restricted moving-divisor equation
and the exact extra residue-class choice that an exhaustive argument would have
to control.

## 11. Terminal rank-three disposition

For an actual planar Keller map, Orevkov's theorem makes the conditional search
empty: field degree three cannot occur. The residue-class decomposition and
pencil equation are retained as useful algebra for neighboring finite covers and
for auditing proposed internal proofs, but they are no longer a necessary bridge
for the rank-three Keller leaf.
