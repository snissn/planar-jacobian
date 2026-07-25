# Boundary Valuations and the Exact Local Cubic

```text
authority: MUTABLE_NONAUTHORITATIVE
local_claims: R3BC-02, R3BC-03
```

## 1. Height-one setup

Temporarily retain a finite locally free rank-three normal `B`-algebra `O`, and
let `p` be a height-one prime of

```text
B=C[P,Q].
```

Put

```text
R=B_p,
S=O tensor_B R,
k=kappa(p).
```

The ring `R` is a DVR and `S` is the entire finite semilocal normalization
algebra over it. Generation must be tested on `S`, not separately on each DVR
factor. For `s in E`, the predecessor's local criterion says

```text
R[s]=S
iff
k[bar(s)]=S/pS
iff
v_p(Phi(s))=0.
```

For a generically primitive `s`, the exact valuation is

```text
v_p(Phi(s))=length_R(S/R[s]).
```

## 2. Why there are exactly three special-fiber types

Pass faithfully flatly to a strict henselization and then to an algebraic closure
of the residue field. This does not change whether the index determinant is a
unit. Every height-one factor of the normalization is a DVR. In characteristic
zero the ramification is tame at the generic point, so a factor with ramification
index `e` has special fiber `k[epsilon]/(epsilon^e)`. The total rank is three.

The partitions of three give only:

```text
1+1+1,
2+1,
3.
```

Thus the geometric special fiber is respectively

```text
k x k x k,
(k[epsilon]/epsilon^2) x k,
k[epsilon]/epsilon^3.
```

This classifies the reduction of the binary index cubic up to `GL_2(k)`.

## 3. Split fiber: three distinct linear factors

Let

```text
S_0=k x k x k,
s=(z1,z2,z3).
```

In the standard basis, the determinant of `1,s,s^2` is the Vandermonde

```text
Phi_0(s)
 = det [[1,z1,z1^2],
        [1,z2,z2^2],
        [1,z3,z3^2]]
 = (z2-z1)(z3-z1)(z3-z2).
```

On trace zero, `z1+z2+z3=0`, so the three collision equations are three distinct
linear forms on the two-dimensional trace-zero plane. Therefore

```text
Phi mod p ~ L1 L2 L3.
```

The section generates the special fiber exactly when the three sheet values are
pairwise distinct.

## 4. Simple ramification: one linear factor times a square

Let

```text
S_0=(k[epsilon]/epsilon^2) x k,
s=(a+b epsilon,c).
```

Use the basis

```text
1=(1,1),
epsilon_1=(epsilon,0),
e_2=(0,1).
```

The coordinate matrix of `1,s,s^2` is

```text
[1   a       a^2          ]
[0   b       2ab          ]
[0   c-a     c^2-a^2      ].
```

Its determinant is

```text
Phi_0(s)=b(c-a)^2.
```

The trace is `2a+c`. On the trace-zero plane, `c=-2a`, hence

```text
Phi_0=9 b a^2.
```

Therefore

```text
Phi mod p ~ L M^2,
```

not a cube. The two conditions have different meanings:

- `b != 0` supplies the nilpotent/uniformizer direction in the ramified factor;
- `c-a != 0` separates the reduced ramified point from the unramified sheet.

Failure of the second condition is a residual sheet collision; its square
multiplicity is intrinsic to the two coincident values in the Vandermonde.

## 5. Total ramification: a cube

Let

```text
S_0=k[epsilon]/epsilon^3,
s=a+b epsilon+c epsilon^2.
```

In the basis `1,epsilon,epsilon^2`, the coordinate matrix is

```text
[1   a   a^2       ]
[0   b   2ab       ]
[0   c   b^2+2ac   ].
```

Its determinant is

```text
Phi_0(s)=b^3.
```

The trace is `3a`, so trace zero imposes `a=0` and does not alter the formula.
Thus

```text
Phi mod p ~ L^3.
```

Here the “boundary cube” description is exact: the special fiber is generated
precisely when the coefficient of the first uniformizer direction is nonzero.

## 6. Exact boundary-cubic trichotomy

Combining the preceding calculations:

### Proposition 6.1

At every height-one base prime of a finite locally free normal rank-three algebra,
the reduced binary index cubic is geometrically `GL_2`-equivalent to exactly one
of

```text
L1 L2 L3,   L M^2,   L^3.
```

The cases correspond respectively to ramification partitions `1+1+1`, `2+1`,
and `3`.

### Consequences

1. A blanket “boundary cube” assumption is false.
2. The different/discriminant distinguishes the repeated-factor cases but does
   not select one global integral direction across all divisors.
3. In each case, `p` divides `Phi(s)` exactly when the reduction of `s` fails
   the displayed generation criterion.
4. Higher valuation of `Phi(s)` measures excess integral index beyond the
   special-fiber failure; the mod-`p` shape alone does not determine that
   higher length.

## 7. Simultaneous boundary adaptation

Let

```text
U=Spec(A) -> Y=Spec(O)
```

be the specified source open. The complement `Y-U` has finitely many irreducible
height-one components. Because `Y -> Spec(B)` is finite, each maps to a
height-one target prime. Let

```text
S_boundary={p_1,...,p_r}
```

be the finite set of distinct target primes so obtained, and choose a square-free
product

```text
H=h_1 ... h_r,
(p_i)=(h_i).
```

By the predecessor's finite-prime adaptation theorem (`CLM-029`), there is an
integral primitive `theta in O` such that

```text
B_{p_i}[theta]=O_{p_i}
```

for every `i`. Replacing `theta` by its trace-zero part changes it by a base
scalar and therefore does not change sheet differences or the generated algebra.
Thus take `theta in E` with

```text
v_{p_i}(Phi(theta))=0
```

for all boundary primes.

### Proposition 7.1 — boundary-stable affine family

For every `eta in E` and `T in B`, set

```text
s_T=theta+H T eta.
```

Then

```text
B_{p_i}[s_T]=O_{p_i}
```

for every `i` and every `T`.

### Proof

Modulo `p_i`, `H=0`, so `bar(s_T)=bar(theta)`. Since `bar(theta)` generates the
whole special fiber, the local generation criterion gives the result. ∎

Therefore

```text
v_{p_i}(Phi(s_T))=0
```

uniformly in `T`. All positive boundary valuations have been cancelled
simultaneously before the global unit search begins.

## 8. Exact affine-family identity

Let `C(-,-,-)` be the symmetric trilinear polarization of `Phi`. Homogeneity
gives

```text
Phi(theta+z eta)
 = Phi(theta)
 + 3 C(theta,theta,eta) z
 + 3 C(theta,eta,eta) z^2
 + Phi(eta) z^3.
```

With `z=HT`, write

```text
D=Phi(theta),
C_1=3 C(theta,theta,eta),
B_2=3 C(theta,eta,eta),
A=Phi(eta).
```

Then

```text
Phi(s_T)
 = D + H C_1 T + H^2 B_2 T^2 + H^3 A T^3.      (8.1)
```

Equation (8.1) is checked symbolically in `verify_boundary_family.py`.
At every `p_i|H`, it reduces to `D`, a unit. Hence every irreducible factor of
`Phi(s_T)` lies outside the chosen boundary set.

## 9. Exact remaining counterfactual bridge

If Orevkov's rank-three theorem is set aside, the entire unit problem becomes:

> Find `eta in E`, `T in B`, and `lambda in C*` such that
>
> ```text
> D + H C_1 T + H^2 B_2 T^2 + H^3 A T^3 = lambda.   (9.1)
> ```

All boundary primes are already excluded. Any failure of (9.1) is a newly
created height-one divisor in the source-étale target locus, where it represents
an accidental equality of two scalar sheet values of `s_T`. This is not
ramification and is not detected by the different.

Thus the predecessor phrase “boundary-cube unit” can be sharpened:

```text
boundary local shape: completely classified;
boundary valuations: simultaneously removable;
remaining divisor: nonboundary moving scalar collision.
```

## 10. Relation to source denominators

For a source function `r in A` viewed in `E_K`, clearing a denominator by
`m in B` gives the predecessor identity

```text
Phi((m r)^0)=m^3 Phi_K(r).
```

The boundary-adapted construction above is stronger for the unit search: rather
than accepting a cubic boundary contribution from one denominator, it first
chooses an integral section primitive at all boundary primes and then varies it
by a multiple of `H`. No denominator or valuation compensation remains at the
boundary.
