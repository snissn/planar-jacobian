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

For a generically primitive `s`,

```text
v_p(Phi(s))=length_R(S/R[s]).
```

## 2. The three geometric special fibers

Pass faithfully flatly to a strict henselization and then to an algebraic closure
of the residue field. This preserves whether the index determinant is a unit.
In residue characteristic zero the height-one ramification is tame. Total rank
three leaves only the partitions

```text
1+1+1,  2+1,  3,
```

and the corresponding geometric special-fiber algebras

```text
k x k x k,
(k[epsilon]/epsilon^2) x k,
k[epsilon]/epsilon^3.
```

These determine the binary index cubic up to `GL_2(k)`.

## 3. Split fiber: three distinct linear factors

For

```text
S_0=k x k x k,
s=(z1,z2,z3),
```

the determinant of `1,s,s^2` is the Vandermonde

```text
Phi_0(s)
 = (z2-z1)(z3-z1)(z3-z2).
```

On trace zero, `z1+z2+z3=0`; the three collision equations are distinct linear
forms on the two-dimensional trace-zero plane. Hence

```text
Phi mod p ~ L1 L2 L3.
```

The reduction of `s` generates exactly when its three sheet values are pairwise
distinct.

## 4. Simple ramification: one linear factor times a square

For

```text
S_0=(k[epsilon]/epsilon^2) x k,
s=(a+b epsilon,c),
```

use the basis

```text
1=(1,1),
epsilon_1=(epsilon,0),
e_2=(0,1).
```

The coordinate matrix of `1,s,s^2` is

```text
[1   a       a^2          ]
[0   b       2ab          ]
[0   c-a     c^2-a^2      ],
```

so

```text
Phi_0(s)=b(c-a)^2.
```

Trace zero gives `2a+c=0`, hence `Phi_0=9ba^2`. Therefore

```text
Phi mod p ~ L M^2,
```

not a cube. The simple factor supplies the nilpotent direction; the squared
factor separates the reduced ramified point from the unramified sheet.

## 5. Total ramification: a cube

For

```text
S_0=k[epsilon]/epsilon^3,
s=a+b epsilon+c epsilon^2,
```

the coordinate matrix is

```text
[1   a   a^2       ]
[0   b   2ab       ]
[0   c   b^2+2ac   ],
```

with determinant

```text
Phi_0(s)=b^3.
```

Trace zero imposes `a=0` and does not change the formula. Thus

```text
Phi mod p ~ L^3.
```

The “boundary cube” description is exact only in this totally ramified case.

## 6. Boundary-cubic trichotomy

### Proposition 6.1

At every height-one base prime of a finite locally free normal rank-three algebra,
the reduced binary index cubic is geometrically `GL_2`-equivalent to exactly one
of

```text
L1 L2 L3,   L M^2,   L^3,
```

corresponding to ramification partitions `1+1+1`, `2+1`, and `3`.

Consequently:

1. a blanket boundary-cube assumption is false;
2. the different distinguishes repeated-factor cases but does not choose one
   global integral direction;
3. `p` divides `Phi(s)` exactly when the reduction of `s` fails the displayed
   generation criterion;
4. the mod-`p` shape does not determine higher index length.

The determinant identities are checked in `verify_binary_cubic.py`.

## 7. Simultaneous boundary adaptation

Let

```text
U=Spec(A) -> Y=Spec(O)
```

be the specified source open. Its finitely many height-one boundary components
map, under the finite normalization morphism, to finitely many target
height-one primes

```text
S_boundary={p_1,...,p_r}.
```

Choose a square-free product

```text
H=h_1 ... h_r,
(p_i)=(h_i).
```

By the predecessor's finite-prime adaptation theorem (`CLM-029`), there is an
integral primitive `theta in O` with

```text
B_{p_i}[theta]=O_{p_i}
```

for every `i`. Subtracting the trace scalar does not change the generated algebra
or sheet differences, so take `theta in E` with

```text
v_{p_i}(Phi(theta))=0
```

at all boundary primes.

### Proposition 7.1 — one boundary-stable congruence class

For every `eta in E` and `T in B`, set

```text
s_T=theta+H T eta.
```

Then

```text
B_{p_i}[s_T]=O_{p_i}
```

for all `i` and all `T`.

### Proof

Modulo `p_i`, `H=0`, so `bar(s_T)=bar(theta)`. Since `bar(theta)` generates the
whole semilocal special fiber, the local generation criterion gives the result.
∎

Thus

```text
v_{p_i}(Phi(s_T))=0
```

uniformly in this congruence class. This simultaneously removes every boundary
valuation for the chosen family. It does **not** show that every possible unit
section is congruent to this `theta` modulo `H E`.

## 8. Exact affine-pencil identity

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

Equation (8.1) is checked symbolically in `verify_boundary_family.py`. At every
`p_i|H`, it reduces to `D`, a unit. Hence every irreducible factor created in
this pencil lies outside the chosen boundary set and is a nonboundary scalar
collision.

## 9. Exact residue-class decomposition of the conditional search

Define

```text
R_H={bar(theta) in E/H E :
     bar(theta) generates O_p/pO_p for every p|H}.
```

Finite-prime adaptation proves only that `R_H` is nonempty. For each
`bar(theta) in R_H` and any lift `theta`, the integral sections with that residue
class are exactly

```text
theta+H eta,  eta in E.
```

Therefore, if Orevkov's terminal theorem is deliberately set aside, the full
conditional unit problem is

```text
find bar(theta) in R_H, a lift theta, eta in E, and lambda in C*
such that Phi(theta+H eta)=lambda.               (9.1)
```

For a fixed class and direction, (8.1) is an exact one-parameter subproblem.
Choosing the initial `theta` does not prove that a hypothetical unit section lies
in its class. Failure of one pencil—or even one full class—does not exclude a
unit section with different boundary residues.

The sharpened boundary statement is therefore:

```text
boundary local shape: completely classified;
within each chosen primitive class: all boundary valuations vanish;
remaining factors in a pencil: nonboundary moving scalar collisions;
additional exhaustive choice: the boundary-primitive class in E/H E.
```

## 10. Relation to source denominators

For a source function `r in A` viewed in `E_K`, clearing a denominator by
`m in B` gives the predecessor identity

```text
Phi((m r)^0)=m^3 Phi_K(r).
```

The boundary-adapted family avoids that denominator contribution inside a chosen
primitive congruence class: it fixes one integral section primitive at all
boundary primes and varies it by multiples of `H`. No boundary valuation is
created inside that class, but no canonical or exhaustive class is selected.
