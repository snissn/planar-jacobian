# Human Derivation: Defect Five

## 1. The theorem under construction

Fix a Keller pair `F=(P,Q)` over `C`, a primitive positive weight `w=(p,q)`,
and assume

```text
kappa=d_P+d_Q-p-q=5.
```

The Rees identity and the complete stairs `S_0,...,S_5` are derived in
`FOUNDATIONS.md`. At least one resonant bracket `J(P_a,Q_b)`, `a+b=5`, is a
nonzero scalar.

The proof is by exact resonance analysis. No assertion below assumes that only
one resonant bracket is nonzero.

## 2. Endpoint positions `(0,5)` and `(5,0)`

Suppose a nonzero resonant bracket touches a top layer. Apply the compensated
graded normalization from `TRANSFORMATIONS.md`.

If the normalized top component is `P_0=x`, then `d_P=p`. For `p<q`, every
monomial of `P` has weight at most `p`, so `P=x+constant`; for `(p,q)=(1,1)`,
`P` is affine linear. If the normalized top component has degree `q`, it has the
form `c y+g(x)` plus lower `x`-terms and is likewise a coordinate.

Let the coordinate be `U=P` and choose a polynomial complement `V=R` with
`J(P,R)=delta in C*`. In source coordinates `(u,v)=(P,R)`,

```text
1=J(P,Q)=delta * partial_v Q,
Q=delta^(-1) v+h(u).
```

The full map is triangular and invertible. The transposed endpoint is identical.
This uses all lower layers and proves the endpoint result directly.

Henceforth every nonzero resonant endpoint is excluded and an interior pair is
selected.

## 3. Interior normalization and all simultaneous resonances

After source-weight and target-component orientation, take `p<=q` and normalize
one selected interior pair to

```text
P_a=x,  Q_b=c y,  a+b=5,  c!=0.                    (3.1)
```

The graded inverse preserves every layer index. Equation (T4) shows that every
other bracket is pulled back covariantly. In particular, the full resonant stair
remains

```text
J(P_0,Q_5)+J(P_1,Q_4)+J(P_2,Q_3)
+J(P_3,Q_2)+J(P_4,Q_1)+J(P_5,Q_0)=1,              (3.2)
```

with the chosen term equal to `c` and all other terms still present.
From (3.1),

```text
d_P=p+a,  d_Q=q+b.                                  (3.3)
```

## 4. Common powers and exact descent

The top stair is `J(P_0,Q_0)=0`. Both top layers are nonzero, nonconstant, and
weighted homogeneous. Let their degrees be `alpha=d_P`, `beta=d_Q`, and let
`E=p x partial_x+q y partial_y`. Contracting `dP_0 wedge dQ_0=0` with `E` gives

```text
alpha P_0 dQ_0-beta Q_0 dP_0=0.
```

Thus `d(Q_0^alpha/P_0^beta)=0` in `C(x,y)`, whose common constant field for
`partial_x,partial_y` is `C`. Hence

```text
Q_0^alpha=C P_0^beta.                                (4.1)
```

Write `rho=gcd(alpha,beta)`, `alpha=rho m`, `beta=rho n`, with
`gcd(m,n)=1`. Unique factorization in `C[x,y]`, after absorbing a scalar root,
gives

```text
P_0=A H^m,  Q_0=B H^n,                              (4.2)
```

where `A,B in C*` and `H` is a nonconstant weighted-homogeneous polynomial of
degree `rho`. A factor of a homogeneous element in this positive grading is
homogeneous: least and greatest nonzero degrees in a product cannot cancel.

If `m=1` or `n=1`, the complete-top shear (T5) preserves `J=1`, cancels the
entire top layer, and strictly lowers the actual integer defect to a nonnegative
`kappa'<=4`. The independently accepted defect-at-most-four theorem then proves
invertibility.

It remains to show that a no-descent system `m,n>=2` cannot satisfy the complete
stairs.

## 5. Unbounded support sieve

Because `H` is nonconstant and `p<=q`, `rho>=p`. From (3.3) and `m>=2`,

```text
p+a=m rho>=2p,
so p<=a.                                             (5.1)
```

This already bounds `p` by four.

Assume first `p<q`. If `H` contains a monomial involving `y`, then
`rho>=q`, so

```text
2q<=2rho<=p+a.                                       (5.2)
```

For `a=1,2`, (5.2) has no solution. For `a=3`, it leaves only `(p,q)=(1,2)`,
but then `(d_P,d_Q)=(4,4)` and `m=n=1`, already a top descent. For `a=4`, it
leaves `(1,2)` and `(2,3)`; their root degrees are respectively `1` and `2`,
both strictly below `q`. Therefore every unequal-weight no-descent root is a
pure `x`-power.

Consequently

```text
H=x^r after scalar absorption,
p divides a,
p divides q+b,                                      (5.3)
P_0=A x^(1+a/p),
Q_0=B x^((q+b)/p).
```

Equations (5.1)–(5.3), primitivity, and the condition `m,n>=2` give exactly the
weight families in `CASE_TABLE.md`; no larger primitive weight is omitted.
Arithmetic cases for which `rho` is not in the weighted semigroup have no
nonzero `H` and are already impossible.

If `p=q`, primitivity gives the single standard weight `(1,1)`, treated in
Sections 10–11.

## 6. Position `(1,4)`

The no-descent unequal weights are `p=1`, odd `q>=3`. The top layers are

```text
P_0=A x^2,  Q_0=B x^(q+4),  P_1=x,  Q_4=c y.
```

For `r=1,2,3`, let `f_r` be the coefficient of `x^(4-r)y` in `Q_r`. Complete
support generation, including the extra `y^2` term when `q=3`, gives the pure
`x` coefficients

```text
S_1: 2A f_1=0,
S_2: 2A f_2+f_1=0,
S_3: 2A f_3+f_2=0,
S_4: 2A c+f_3=0.                                    (6.1)
```

Since `A,c!=0`, (6.1) is impossible. The extra `q=3` coefficient satisfies its
own equation `4A g=0` and cannot alter this chain. All other resonant terms in
`S_5` vanish by support, so `S_5` would give `c=1`; the contradiction occurs
earlier.

## 7. Position `(2,3)`

### 7.1 Weight `p=1`, `q>2`

Here `3` does not divide `q`,

```text
P_0=A x^3,
P_1=u x^2,
P_2=x,
Q_3=c y.
```

Let `f_1,f_2` be the coefficients of `x^2y` in `Q_1` and `xy` in `Q_2`.
Then

```text
S_1: 3A f_1=0,
S_2: 3A f_2+2u f_1=0,
S_3: 3A c+2u f_2+f_1=0,                             (7.1)
```

which is impossible.

### 7.2 Exceptional weight `(1,2)`

Complete supports are

```text
P_1=u x^2+v y,
Q_1=e x^4+f x^2y+g y^2,
Q_2=r x^3+s xy,
Q_4=kx.
```

The complete stairs give

```text
3Af-5Bv=0,          6Ag=0,
3As-4ve+2uf=0,     -2vf+4ug=0,
3Ac-3vr+2us+f=0,   -vs+2g=0,
2uc+s=0,
c-vk=1.                                             (7.2)
```

The final equation displays the simultaneously resonant bracket
`J(P_1,Q_4)=-vk`; the selected scalar is not silently set to one.
From `g=0`, equation `vs=0`. If `v=0`, then `f=s=u=0` successively, leaving
`3Ac=0`. If `s=0`, then `u=0`; either `v=0` or `f=0`, and the first equation
again forces `v=f=0`. Contradiction.

### 7.3 Weight `p=2`, `q>3`

The no-descent congruence is `q≡3 mod 4`; hence `q>=7`. Here `P_1=0` and
`Q_1=fxy`. Two coefficients suffice:

```text
S_1: 2Af=0,
S_3: 2Ac+f=0.                                       (7.3)
```

### 7.4 Exceptional weight `(2,3)`

With

```text
P_1=v y,  Q_1=fxy,  Q_2=r x^2,  Q_4=kx,
```

one obtains

```text
2Af-3Bv=0,
-vf=0,
2Ac-2vr+f=0,
c-vk=1.                                             (7.4)
```

If `v=0`, then `f=0` and the third equation is impossible. If `f=0`, the first
forces `v=0`. Thus no system survives.

## 8. Position `(3,2)`

This position is kept separate rather than inferred from a defect-four middle
case.

### 8.1 Weight `p=1`, `q>3`

The no-descent condition is `q not congruent to 2 mod 4`. Write

```text
P_0=A x^4,  P_1=u x^3,  P_3=x,
Q_1=...+fxy,  Q_2=c y.
```

Then

```text
S_1: 4Af=0,
S_2: 4Ac+3uf=0,                                     (8.1)
```

which is impossible.

### 8.2 Exceptional weight `(1,3)`

Complete relevant supports are

```text
P_1=u x^3+v y,
P_2=r x^2,
Q_1=e x^4+fxy,
Q_3=sx^2,
Q_4=kx.
```

The stairs are

```text
4Af-5Bv=0,
4Ac-4ve+3uf=0,   -vf=0,
3uc+2rf=0,
-2vs+2rc+f=0,
c-vk=1.                                             (8.2)
```

The product equation `vf=0` and the first equation force `v=f=0`; the second
then gives `4Ac=0`.

### 8.3 Weight `p=3`

No descent requires `q≡1 mod 6`, `q>=7`. The pieces of degrees five and four
are zero, so the coefficient of `x` in `S_2` is simply

```text
2Ac=0.                                               (8.3)
```

## 9. Position `(4,1)`

### 9.1 Generic unequal weights

For `p=1`, every no-descent `q>=5` has `P_1` pure in `x`; the coefficient of
`x^4` in `S_1` is `5Ac`. For `p=2`, every generic no-descent weight has
`q>=7`, `P_1=0`, and the coefficient of `x^2` is `3Ac`. For `p=4`, no descent
requires `q≡3 mod 8`, `q>=11`, `P_1=0`, and the coefficient of `x` is `2Ac`.
All are impossible.

### 9.2 Exceptional weight `(1,2)`

Use

```text
P_1=u x^4+v x^2y+w y^2,
P_2=r x^3+sxy,
P_3=z x^2+t y,
Q_2=kx.
```

The complete equations are

```text
5Ac-3Bv=0,       -6Bw=0,
-3Bs+4uc=0,       2vc=0,
-3Bt-vk+3rc=0,   -2wk+sc=0,
-sk+2zc=0,
-tk+c=1.                                             (9.1)
```

Since `c!=0`, `v=0`, contradicting the first equation.

### 9.3 Exceptional weight `(1,3)`

With

```text
P_1=u x^4+vxy,
P_2=r x^3+t y,
P_3=z x^2,
Q_2=kx^2,
Q_3=ell x,
```

one gets

```text
5Ac-4Bv=0,
-4Bt+4uc=0,  vc=0,
-2vk+3rc=0,
-v ell-2tk+2zc=0,
-t ell+c=1.                                          (9.2)
```

Again `v=0` contradicts the first equation.

### 9.4 Exceptional weight `(2,3)`

For

```text
P_1=vxy,  P_2=r x^2,  P_3=t y,  Q_2=kx,
```

the equations include

```text
3Ac-2Bv=0,
vc=0,
-2Bt-vk+2rc=0,
-tk+c=1.                                             (9.3)
```

The first two are incompatible.

## 10. Equal weight `(1,1)`, position `(1,4)`

This is the first genuinely new defect-five correction. Put `X=H` and choose a
linear `Y` with `J(X,Y)=1`. Write

```text
P_0=A X^2,  Q_0=B X^5,
P_1=L=ell X+sY,
Q_4=M=mu X+nY,
c=J(L,M)=ell*n-s*mu !=0.
```

Use complete homogeneous supports

```text
Q_1=sum_(i=0)^4 a_i X^(4-i)Y^i,
Q_2=sum_(i=0)^3 b_i X^(3-i)Y^i,
Q_3=sum_(i=0)^2 d_i X^(2-i)Y^i.
```

Selected coefficients of the complete stairs are

```text
S_1: 2A a_1-5B s=0,  4A a_2=0,  6A a_3=0,  8A a_4=0,
S_2: 4A b_2-3a_1 s+2a_2 ell=0,  6A b_3-2a_2 s+3a_3 ell=0,
S_3: -b_2 s+3b_3 ell=0.                              (10.1)
```

Thus `a_2=a_3=a_4=b_3=0`,

```text
a_1=(5B/(2A))s,
b_2=(3a_1/(4A))s,
b_2 s=0.
```

Since `A,B!=0`, this forces `s=0`, hence `a_1=b_2=0`. The remaining pure
`X` chain is

```text
S_2: 2A b_1=0,
S_3: 2A d_1=0,
S_4: 2A n=0.
```

Therefore `n=0`, while `s=0`, so `c=ell*n-s*mu=0`, contradiction. Here `S_5`
would give `c=1`; the contradiction uses only that it is nonzero.

The signed target swap gives the equal-weight `(4,1)` case with the same scalar.

## 11. Equal weight `(1,1)`, position `(2,3)`

This is the second new correction, and it contains the first nonlinear middle
term `J(P_1,Q_1)` not controlled by defect four. In coordinates `X=H,Y`, write

```text
P_0=A X^3,  Q_0=B X^4,
P_2=L=ell X+sY,
Q_3=M=mu X+nY.
```

Let initially

```text
P_1=aX^2+bXY+gY^2.
```

The equation `S_1=0` integrates exactly to

```text
Q_1=(4B/(3A)) X P_1+E X^3.                          (11.1)
```

All other terms of `S_2` are divisible by `X^2`; the `Y^3` coefficient of
`J(P_1,Q_1)` from (11.1) is

```text
-8B g^2/(3A).
```

Hence `g=0`. Write

```text
P_1=aX^2+bXY,
Q_1=dX^3+eX^2Y,
Q_2=uX^2+vXY+wY^2.
```

The complete coefficient equations are

```text
S_1: 3Ae-4Bb=0,
S_2: 3Av-4Bs+2ae-3bd=0,  6Aw-be=0,
S_3: 3An+2av-2bu-3ds+e ell=0,
     4aw-2es=0,  2bw=0,
S_4: 2an-b mu+ell v-2su=0,
     bn+2ell w-sv=0,
S_5: ell*n-s*mu=1.                                  (11.2)
```

The first equation and `6Aw=be` give

```text
e=(4B/(3A))b,
w=(2B/(9A^2))b^2.
```

Then `2bw=0` forces `b=0`, so `e=w=0`. The first `S_2` equation reduces to
`3Av=4Bs`, while the second `S_4` equation reduces to `sv=0`. Thus `s=v=0`.
The first `S_3` equation now gives `n=0`, contradicting
`ell*n-s*mu=1`.

The signed target swap gives the equal-weight `(3,2)` case.

## 12. Closure and orientations

Every interior no-descent system has now been contradicted. Therefore an actual
interior defect-five Keller pair must have `m=1` or `n=1`, so an allowed target
shear lowers its actual defect to at most four. The accepted defect-at-most-four
theorem proves the descended map invertible, and all normalizations are inverted.

The source swap covers the original orientation `p>q`; the signed target swap
covers either component-degree orientation and retains the resonant scalar. The
four canonical interior positions were treated separately, and missing layers
and simultaneous resonances were included in the displayed complete supports.

Thus every primitive-positive-weight Keller pair of defect five is a polynomial
automorphism, at candidate status pending independent review.
