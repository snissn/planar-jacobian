# Independent Reconstruction A — Foundations and Defects Zero Through Three

> **Review mode:** `independent-review`
> **Reviewed candidate:** `96fc7ec34bd3b685a0edeae7ecd4404abab7e2f1`
> **Disposition:** `ACCEPT`

## 3. Independent reconstruction

The reconstruction below is organized by a common-root degree sieve, not by the
candidate's weight-regime table.

### 3.1 Exact Rees identity and staircase

Let `R=C[x,y]`, with `deg_w x=p`, `deg_w y=q`, and let `R_d` be the
weighted-homogeneous piece of degree `d`; set `R_d=0` for `d<0`. Put

```text
d_P=deg_w P,  d_Q=deg_w Q,  kappa=d_P+d_Q-p-q,
P=sum_(i>=0) P_i,  P_i in R_(d_P-i),
Q=sum_(j>=0) Q_j,  Q_j in R_(d_Q-j).
```

A missing weighted degree is represented by a zero layer. Define

```text
Pcal(t,x,y)=t^(d_P) P(t^(-p)x,t^(-q)y),
Qcal(t,x,y)=t^(d_Q) Q(t^(-p)x,t^(-q)y).
```

The chain rule gives

```text
(Pcal)_x=t^(d_P-p) P_x(t^(-p)x,t^(-q)y),
(Pcal)_y=t^(d_P-q) P_y(t^(-p)x,t^(-q)y),
```

and the analogous formulas for `Qcal`. Both determinant products therefore
carry the same exponent:

```text
(d_P-p)+(d_Q-q)=(d_P-q)+(d_Q-p)=d_P+d_Q-p-q.
```

With `J(f,g)=f_x g_y-f_y g_x`, no sign changes, and

```text
J(Pcal,Qcal)=t^kappa J(P,Q)(t^(-p)x,t^(-q)y)=t^kappa.
```

Since `Pcal=sum_i t^i P_i` and `Qcal=sum_j t^j Q_j`, comparison of
coefficients gives, for every `n>=0`,

```text
S_n := sum_(i+j=n) J(P_i,Q_j) = delta_(n,kappa).          (1)
```

Moreover,

```text
J(P_i,Q_j) in R_(kappa-i-j).                              (2)
```

The left side of the Rees identity is a polynomial in `t`; hence `kappa` cannot
be negative. Equation (2) makes every bracket with `i+j>kappa` vanish
individually. At resonance `i+j=kappa`, every bracket belongs to `R_0=C`, so
every resonant bracket is a scalar. Their sum is one by (1), so at least one is
nonzero. This proves all lower, resonant, and above-resonance staircase
statements, including absent layers.

### 3.2 Weighted-homogeneous constant-bracket pairs

Let `A in R_r` and `B in R_s` be nonzero and satisfy `J(A,B)=c in C*`.
Both degrees are positive. Evaluating the Jacobian at the origin shows that the
ordinary linear parts of `A,B` have determinant `c`, hence rank two. A
weighted-homogeneous polynomial can contain an `x` linear term only in degree
`p` and a `y` linear term only in degree `q`. Therefore

```text
{r,s}={p,q}.                                               (3)
```

After arranging `p<=q` and orienting the pair so `(r,s)=(p,q)`:

- if `p<q`, then

  ```text
  A=a x,
  B=b y+h(x),
  ab=c,
  deg_w h=q.
  ```

  In fact `h` can be nonzero only when `p=1`, in which case it is a scalar
  multiple of `x^q`;
- if `p=q`, primitivity gives `(p,q)=(1,1)`, and `(A,B)` is an invertible
  linear pair.

Thus `psi=(A,B)` is a graded polynomial automorphism. In the unequal-weight
case its inverse is explicit:

```text
x=u/a,
y=(v-h(u/a))/b.
```

Both the map and its inverse preserve the weighted grading, hence the complete
weighted filtration.

For a selected resonant pair `(P_a,Q_b)=(A,B)`, take
`phi=psi^(-1)` and `D(u,v)=(u,c v)`. Then

```text
J(D o F o phi)=c * 1 * (1/c)=1,
(P_a,Q_b) -> (x,c y).                                      (4)
```

The scalar `c` remains visible. Because `phi` is graded and `D` is diagonal,
all layer indices are preserved. Every other staircase term is transformed by
the same change of variables; normalization of the selected bracket cannot
invalidate or discard another term.

The other operations used are exact:

```text
(P,Q) -> (Q,-P)                         determinant 1,
(P,Q) -> (P,Q-lambda P)                 determinant 1,
(P,Q) -> (P,Q-h(P))                     determinant 1,
(P,Q) -> (P-h(Q),Q)                     determinant 1.
```

The source swap `(x,y)->(y,-x)`, together with relabeling `(p,q)->(q,p)`,
has Jacobian one and preserves `kappa`.

### 3.3 Common-power lemma in the weighted UFD

Let `f in R_alpha` and `g in R_beta` be nonzero, nonconstant, and satisfy
`J(f,g)=0`. Let

```text
E=p x partial_x+q y partial_y.
```

Since `df wedge dg=0`, contraction with `E` and weighted Euler's identities
give

```text
alpha f dg-beta g df=0.                                   (5)
```

Therefore `d(g^alpha/f^beta)=0` in `C(x,y)`. In characteristic zero the common
kernel of `partial_x` and `partial_y` in `C(x,y)` is `C`, so

```text
g^alpha=C f^beta,  C in C*.                               (6)
```

Write

```text
rho=gcd(alpha,beta),
alpha=rho m,  beta=rho n,  gcd(m,n)=1.
```

After taking a `rho`-th root of the scalar in `C`, unique factorization applied
to every irreducible valuation in (6) gives

```text
f=A H^m,
g=B H^n,                                                   (7)
```

with `A,B in C*`. A factor of a homogeneous element in a positively graded
domain is homogeneous: comparing the least and greatest nonzero weighted
components of a product forces each factor to have only one degree. Hence
`H in R_rho` is nonconstant. This proves the lemma without a closed-polynomial
theorem and covers common factors, equal degrees, coprime exponents, and all
zero intermediate layers.

If `m=1`, then `g=lambda f^n`, and

```text
(P,Q) -> (P,Q-lambda P^n)
```

cancels the **entire** top layer of `Q`. All other terms of `P^n` have smaller
weight, so no replacement term of the old top weight is created. Thus
`d'_Q<d_Q`, `d'_P=d_P`, and the actual integer defect strictly decreases. The
case `n=1` is transposed; when `m=n=1`, a determinant-one linear shear cancels
one proportional top layer. Partial cancellation is not counted as descent.

### 3.4 Endpoint resonance

Suppose a nonzero resonant bracket touches a top layer. After orientation and
normalization, one endpoint has `P_0=x` and `d_P=p`. If `p<q`, every lower term
of `P` has weight at most `p`, so `P=x+constant`; if `p=q=1`, `P` is affine
linear. Thus `P` is a polynomial coordinate. The transposed endpoint has a
component of the form `c y+h(x)` plus lower `x` terms and is likewise a
coordinate.

Choose a polynomial coordinate complement `R` with `J(P,R)=delta in C*` and
write source coordinates `(u,v)=(P,R)`. Then

```text
1=J(P,Q)=delta * partial_v(Q),
Q=delta^(-1) v+h(u).
```

The full map, including constants and all lower weighted terms, is triangular
and invertible. This settles every endpoint position.

### 3.5 The root-degree sieve

Assume a selected interior resonance has position `(a,b)` and is normalized as

```text
P_a=x,  Q_b=c y,
d_P=p+a,  d_Q=q+b.                                         (8)
```

After excluding exact top-power descent, (7) has exponents `m,n>=2`. If
`rho=deg_w H`, then `rho>=p`; hence

```text
p+a=d_P=m rho >= 2p,
so p<=a.                                                    (9)
```

For `kappa<=4`, (9) leaves only:

```text
a=1: p=1,
a=2: p in {1,2},
a=3: p in {1,2,3}.
```

Divisibility and support remove further values. This is the organizing sieve
for the independent case reconstruction.

## 4. Defects zero through three

The proof is by strong induction on the nonnegative integer `kappa`.

### 4.1 Defects zero and one

For `kappa=0`, `S_0=1`, so the resonant pair is an endpoint pair. For
`kappa=1`, both possible positions `(0,1)` and `(1,0)` are endpoints. The endpoint lemma above applies.

### 4.2 Defect two

The only interior position is `(1,1)`. Normalize

```text
P_1=x,  Q_1=c y.
```

After removing exponent-one descent, (9) gives `p=1`. Equal weights give a
linear top descent, so `q>1`. The common root has degree one, and

```text
P_0=A x^2,
Q_0=B x^(q+1).
```

The preceding stair is

```text
S_1=J(P_0,c y)+J(x,Q_0)=2A c x,
```

which is impossible.

### 4.3 Defect three, position `(1,2)`

Normalize `P_1=x`, `Q_2=c y`. No descent implies `p=1`.

For `q>1`,

```text
P_0=A x^2,
Q_0=B x^(q+2),
P_2 in C.
```

Then `S_1=0` gives `(Q_1)_y=0`, and `S_2=0` reduces to `2A c x=0`.

For `(p,q)=(1,1)`, write

```text
P_0=A H^2,
Q_0=B H^3,
H=u x+v y.
```

The second preceding stair gives

```text
(Q_1)_y=-2A c u H,
Q_1=-2A c u^2 x y-A c u v y^2+K x^2.
```

Substitution into the first preceding stair gives `y^2` coefficient `3B v^3`,
so `v=0`. Since `H` is nonzero, `u!=0`; the remaining `x^2` coefficient is
`-4A^2 c u^4`, a contradiction.

### 4.4 Defect three, position `(2,1)`

Normalize `P_2=x`, `Q_1=c y`. No descent implies `p in {1,2}`.

For `p=1`, `q>2`, the top layers are `A x^3` and `B x^(q+1)`, while
`P_1` is a multiple of `x^2`; hence `S_1=3A c x^2`, impossible. The weight
`(1,2)` is an equal-top-degree descent.

For `p=2`, the surviving no-descent weights have `q>=5`; the top first layer is
`A x^2`, and `P_1 in R_3=0`. Thus `S_1=2A c x`, impossible. Weight `(2,3)`
is a proportional-top descent.

For `(1,1)`, write

```text
P_0=A H^3,
Q_0=B H^2,
H=u x+v y.
```

The second preceding stair gives

```text
(P_1)_x=-(2Bv/c)H,
P_1=-(Buv/c)x^2-(2Bv^2/c)xy+K y^2.
```

The first preceding stair has `x^2` coefficient `3A c u^3`, so `u=0`; the
remaining `y^2` coefficient is `-4B^2 v^4/c`, a contradiction.

This completes the independent lower-defect induction in both orientations.
