# Independent Human Reconstruction

## 1. Setup and layer convention

Let `R=C[x,y]`, let `w=(p,q)` be primitive and positive, and define
`deg_w(x)=p`, `deg_w(y)=q`. Write `R_d` for the weighted-homogeneous piece of
degree `d`, with `R_d=0` for `d<0`.

For a Keller pair `F=(P,Q)` with `J(P,Q)=1`, write

```text
P=sum_(i>=0) P_i,  P_i in R_(d_P-i),
Q=sum_(j>=0) Q_j,  Q_j in R_(d_Q-j),
```

where `d_P=deg_w(P)` and `d_Q=deg_w(Q)`. A missing semigroup degree is a
literal zero layer. Throughout this review

```text
kappa=d_P+d_Q-p-q=5.
```

## 2. Rees identity and the complete staircase

Define

```text
Pcal(t,x,y)=t^(d_P) P(t^(-p)x,t^(-q)y),
Qcal(t,x,y)=t^(d_Q) Q(t^(-p)x,t^(-q)y).
```

The chain rule gives

```text
(Pcal)_x=t^(d_P-p) P_x(t^(-p)x,t^(-q)y),
(Pcal)_y=t^(d_P-q) P_y(t^(-p)x,t^(-q)y),
```

and similarly for `Qcal`. Both determinant products therefore carry exponent
`d_P+d_Q-p-q`. With `J(f,g)=f_xg_y-f_yg_x`,

```text
J(Pcal,Qcal)=t^kappa J(P,Q)(t^(-p)x,t^(-q)y)=t^kappa.
```

Because `Pcal=sum_i t^iP_i` and `Qcal=sum_j t^jQ_j`, coefficient comparison
gives

```text
S_n:=sum_(i+j=n) J(P_i,Q_j)=delta_(n,5).
```

Explicitly,

```text
S_0 = J(P_0,Q_0)                                                   = 0,
S_1 = J(P_0,Q_1)+J(P_1,Q_0)                                      = 0,
S_2 = J(P_0,Q_2)+J(P_1,Q_1)+J(P_2,Q_0)                           = 0,
S_3 = J(P_0,Q_3)+J(P_1,Q_2)+J(P_2,Q_1)+J(P_3,Q_0)                = 0,
S_4 = J(P_0,Q_4)+J(P_1,Q_3)+J(P_2,Q_2)+J(P_3,Q_1)+J(P_4,Q_0)   = 0,
S_5 = J(P_0,Q_5)+J(P_1,Q_4)+J(P_2,Q_3)+J(P_3,Q_2)
      +J(P_4,Q_1)+J(P_5,Q_0)                                     = 1.
```

Moreover,

```text
J(P_i,Q_j) in R_(5-i-j).
```

Thus every bracket with `i+j>5` vanishes individually, not merely after
summation. At `i+j=5` every bracket is a scalar, and their sum is one. At least
one resonant bracket is nonzero.

The same identity also proves `kappa>=0` for every Keller pair: its left side is
a polynomial in `t`, whereas `t^kappa` cannot have a negative exponent.

## 3. Classification of a nonzero constant-bracket pair

Choose a resonant pair

```text
A=P_a,  B=Q_b,  a+b=5,  J(A,B)=c in C*.
```

Let `r=deg_w A` and `s=deg_w B`. Since `J(A,B)` is a nonzero constant,
`r+s=p+q`. More strongly, evaluating the Jacobian at the origin shows that the
ordinary linear parts of `A` and `B` have determinant `c`. A weighted-homogeneous
polynomial can contain an `x`-linear term only in degree `p`, and a `y`-linear
term only in degree `q`. Hence

```text
{r,s}={p,q}.
```

After a determinant-one signed target swap if necessary, take `r=p`, `s=q`.
If `p<q`, complete support enumeration gives

```text
A=a_0 x,
B=b_0 y+h(x),
a_0b_0=c,
```

where `h` can be nonzero only when `p=1`; then it is a scalar multiple of
`x^q`. If `p=q`, primitivity gives `(p,q)=(1,1)` and `(A,B)` is an invertible
linear pair. Thus `psi=(A,B)` is a graded polynomial automorphism in every case.

## 4. Scalar-retaining graded normalization

Let `phi=psi^(-1)` and let `D(u,v)=(u,c v)`. The normalized map is

```text
F'=D o F o phi.
```

Because `J(psi)=c` and `J(phi)=1/c`,

```text
J(F')=c*1*(1/c)=1.
```

The selected layers become `(x,c y)` after renaming normalized coordinates. The
inverse `phi` is graded: for `p<q`,

```text
phi(u,v)=(u/a_0, (v-h(u/a_0))/b_0),
```

and every monomial replacing a coordinate has exactly that coordinate's weight.
Therefore `phi^*(R_d)=R_d` for every `d`, and every layer index is preserved.
For every pair of layers,

```text
J(P_i o phi, c Q_j o phi)
 =c (J(P_i,Q_j) o phi) J(phi)
 =J(P_i,Q_j) o phi.
```

All unselected simultaneous resonances remain present. Scalar resonant brackets
are unchanged, not normalized to one. The scaling `D` alone would change the
Jacobian; only the compensated composition is used.

The source map `sigma(x,y)=(y,-x)`, together with relabeling `(p,q)` to `(q,p)`,
has determinant one and reduces `p>q` to `p<=q`. The target map
`tau(P,Q)=(Q,-P)` also has determinant one, sends position `(a,b)` to `(b,a)`,
and retains the scalar because `J(Q_b,-P_a)=J(P_a,Q_b)`.

## 5. Common powers from `S_0=0`

The top forms `P_0,Q_0` are nonzero, nonconstant, weighted homogeneous. Let

```text
alpha=d_P,  beta=d_Q,
E=p x partial_x+q y partial_y.
```

From `dP_0 wedge dQ_0=0`, contraction with `E` gives

```text
alpha P_0 dQ_0-beta Q_0 dP_0=0.
```

In the rational function field,

```text
d(Q_0^alpha/P_0^beta)=0.
```

The common constant field of `partial_x` and `partial_y` in `C(x,y)` is `C` in
characteristic zero, so

```text
Q_0^alpha=C_0 P_0^beta,  C_0 in C*.
```

Set `rho=gcd(alpha,beta)`, `alpha=rho m`, `beta=rho n`, with `gcd(m,n)=1`.
Unique factorization in `C[x,y]` implies, after absorbing scalar roots,

```text
P_0=A_0 H^m,  Q_0=B_0 H^n,
```

for `A_0,B_0 in C*` and nonconstant `H in C[x,y]`. The coprime exponent
convention is the maximal common-root convention: `H` itself may be a proper
polynomial power. Positive-grading extremal-degree arguments show that `H` is
weighted homogeneous, and `deg_w H=rho`.

This is stronger than mere proportionality of top forms. Proportionality is the
special case `m=n=1`; exponent-one descent means either `m=1` or `n=1`.

## 6. Complete-top descent

If `m=1`, then

```text
Q_0=lambda P_0^n,  lambda=B_0/A_0^n.
```

Apply the target shear

```text
(P,Q) -> (P,Q-lambda P^n).
```

Its determinant is one, so `J=1` is preserved. Its top contribution
`lambda P_0^n` cancels the entire top layer of `Q`. Every other term of `P^n`
contains at least one layer below `P_0`, hence has weight strictly below
`n d_P=d_Q`; no replacement term occurs at the old top weight. Therefore

```text
d'_P=d_P,  d'_Q<d_Q,  kappa'<5.
```

The transformed pair is Keller, so its Rees identity gives `kappa'>=0`; hence
`kappa'<=4`. The case `n=1` uses the symmetric shear in `P`. Both shears have
polynomial inverses. The independently reviewed defect-at-most-four theorem now
gives automorphy, and all normalizations can be inverted.

## 7. Endpoint resonance

Suppose a selected nonzero resonance has `a=0` or `b=0`. After graded
normalization, the complete component whose top layer is selected has weighted
degree `p` or `q`.

- At degree `p` with `p<=q`, lower positive-weight layers contain no nonconstant
  monomial, so the full component is `x+constant` after scaling.
- At degree `q>p`, its top layer is `c y+h(x)` and every lower layer contains
  only `x`-terms; the full component is `c y+g(x)`.
- At `(1,1)`, it is affine linear.

In every case the full component is a polynomial coordinate. If it is `P`, take
a polynomial complement `R` with `J(P,R)=delta in C*`. In coordinates
`(u,v)=(P,R)`,

```text
1=J(P,Q)=delta * partial_v Q,
Q=delta^(-1)v+h(u).
```

The map is triangular and invertible. The transposed endpoint is identical.
This argument covers both source-weight orders and component orientations.

## 8. Unbounded no-descent support sieve

It remains to exclude an interior normalized system

```text
P_a=x,  Q_b=c y,  a+b=5,  c!=0,
```

with `p<=q` and common-power exponents `m,n>=2`. The selected degrees give

```text
d_P=p+a,  d_Q=q+b.
```

Because `H` is nonconstant, `rho=deg_w H>=p`. Since `d_P=m rho>=2rho`,

```text
p+a>=2p,  so p<=a<=4.
```

Assume `p<q`. If any monomial of `H` contains `y`, then `rho>=q`, so

```text
2q<=2rho<=p+a.
```

For `a=1,2` this is impossible. For `a=3` it leaves only `(p,q)=(1,2)`, where
`d_P=d_Q=4` and `m=n=1`. For `a=4` it leaves `(1,2)` or `(2,3)`, but their
actual root degrees are respectively `1` and `2`, both below `q`. Thus every
unequal-weight no-descent root is a pure `x`-power.

Consequently `H` is a scalar multiple of `x^r`,

```text
p divides a,
p divides q+b,
P_0=A_0 x^(1+a/p),
Q_0=B_0 x^((q+b)/p).
```

Combining these divisibilities with primitivity and `m,n>=2` yields exactly:

```text
(a,b)=(1,4): p=1, q odd, q>=3.
(a,b)=(2,3): p=1, q>=2, 3 does not divide q;
             or p=2, q congruent 3 mod 4.
(a,b)=(3,2): p=1, q>=3, q not congruent 2 mod 4;
             or p=3, q congruent 1 mod 6, q>=7.
(a,b)=(4,1): p=1, q>=2, q not congruent 4 mod 5;
             or p=2, q odd and q not congruent 2 mod 3;
             or p=4, q congruent 3 mod 8, q>=11.
```

This derivation is unbounded. It does not infer completeness from a finite scan.
Equal weights reduce by primitivity to `(1,1)`.

## 9. Staircase contradictions

For every unequal family, selected coefficients in earlier stairs force the
nonzero selected scalar to vanish. Complete equations, finite exceptions, and
the two equal-weight systems are reconstructed in `CASE_AUDIT.md`.

The generic contradictions are:

```text
(1,4), p=1:
2Af_1=0,
2Af_2+f_1=0,
2Af_3+f_2=0,
2Ac+f_3=0.

(2,3), p=1, q>2:
3Af_1=0,
3Af_2+2u f_1=0,
3Ac+2u f_2+f_1=0.

(2,3), p=2, q>=7:
2Af=0,
2Ac+f=0.

(3,2), p=1, q>3:
4Af=0,
4Ac+3u f=0.

(3,2), p=3, q>=7:
2Ac=0.

(4,1), outside its three finite exceptions:
M A c=0,  M=1+4/p in {5,3,2}.
```

All top coefficients and `c` are required nonzero, so no generic system exists.
The six finite unequal systems are inconsistent after retaining every supported
layer and every simultaneous resonance. At `(1,1)`, the new `(1,4)` chain and
the coupled `(2,3)` quadratic/cubic system are inconsistent; their signed target
swaps cover `(4,1)` and `(3,2)`.

## 10. Closure

Every resonant endpoint is invertible. Every interior system either has
`m=1` or `n=1`, giving exact complete-top descent to a nonnegative defect at most
four, or belongs to a no-descent support family contradicted by the complete
stairs. The defect-at-most-four theorem proves the descended pair invertible.
Every source map, target map, compensation, and shear used above has an explicit
polynomial inverse. Therefore the original defect-five Keller pair is a
polynomial automorphism.
