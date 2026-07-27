# Exhaustive Resonance, Weight, and Coefficient Audit

## 1. Orientation and universal cases

Select a nonzero resonant bracket, arrange `p<=q`, apply a signed component swap
when necessary, and perform the scalar-retaining graded normalization:

```text
P_a=x,  Q_b=c y,  a+b=5,  c in C*.
```

The six positions are the two endpoints `(0,5)`, `(5,0)` and four interiors
`(1,4)`, `(2,3)`, `(3,2)`, `(4,1)`. Endpoints are coordinates and are already
invertible. In an interior case,

```text
d_P=p+a,  d_Q=q+b,
rho=gcd(d_P,d_Q),
m=d_P/rho,  n=d_Q/rho.
```

If `m=1` or `n=1`, a determinant-one complete-top shear strictly lowers the
actual defect. The table below concerns only `m,n>=2`.

## 2. Unbounded family table

| Position | Exact unequal-weight no-descent families | Root/top data |
|---|---|---|
| `(1,4)` | `p=1`, odd `q>=3` | `rho=1`, `P_0=A x^2`, `Q_0=B x^(q+4)` |
| `(2,3)` | `p=1`, `q>=2`, `3∤q`; or `p=2`, `q≡3 mod4` | `rho=1` in the first family; `rho=2` in the second |
| `(3,2)` | `p=1`, `q>=3`, `q≠2 mod4`; or `p=3`, `q≡1 mod6`, `q>=7` | `rho=gcd(4,q+2)` for `p=1`; `rho=3` for `p=3` |
| `(4,1)` | `p=1`, `q>=2`, `q≠4 mod5`; or `p=2`, odd `q`, `q≠2 mod3`; or `p=4`, `q≡3 mod8`, `q>=11` | pure-`x` maximal root in every row |
| every interior | `(p,q)=(1,1)` | linear maximal root `H` |

The derivation is arithmetic, not enumerative: `p<=a`, a `y`-monomial in the
root would force `2q<=p+a`, and the remaining pure-`x` root forces `p|a` and
`p|(q+b)`.

## 3. Position `(1,4)`

### 3.1 Unequal weights

Here `p=1`, `q` is odd and at least three,

```text
P_0=A x^2,  P_1=x,
Q_0=B x^(q+4),  Q_4=c y.
```

Let `f_r` be the coefficient of `x^(4-r)y` in `Q_r`, for `r=1,2,3`.
The pure-`x` coefficients of `S_1,...,S_4` are

```text
2Af_1=0,
2Af_2+f_1=0,
2Af_3+f_2=0,
2Ac+f_3=0.
```

They successively force `f_1=f_2=f_3=c=0`, impossible. At `q=3`, `Q_1` also
supports `g y^2`; its independent coefficient equation is `4Ag=0` and does not
alter the pure-`x` chain. Missing lower layers are constants or zero.

### 3.2 Equal weight

Set `X=H` and choose `Y` with `J(X,Y)=1`. Write

```text
P_0=A X^2,  Q_0=B X^5,
P_1=L=ell X+sY,
Q_4=M=mu X+nY,
c=ell*n-s*mu !=0.
```

Use complete supports

```text
Q_1=sum_(i=0)^4 a_i X^(4-i)Y^i,
Q_2=sum_(i=0)^3 b_i X^(3-i)Y^i,
Q_3=sum_(i=0)^2 d_i X^(2-i)Y^i.
```

The independently expanded coefficients include

```text
S_1: 2A a_1-5B s=0,  4A a_2=0,  6A a_3=0,  8A a_4=0,
S_2: 4A b_2-3a_1 s+2a_2 ell=0,
     6A b_3-2a_2 s+3a_3 ell=0,
S_3: -b_2 s+3b_3 ell=0.
```

Thus `a_2=a_3=a_4=b_3=0`,

```text
a_1=(5B/(2A))s,
b_2=(3a_1/(4A))s,
b_2s=0.
```

Since `A,B` are nonzero, `s=0`, then `a_1=b_2=0`. The remaining pure-`X`
chain is

```text
2A b_1=0,
2A d_1=0,
2A n=0.
```

Hence `n=0`, and `c=ell*n-s*mu=0`, contradiction. This is a genuine
defect-five chain, not a defect-four middle-Wronskian argument. The signed target
swap gives `(4,1)` at equal weight.

## 4. Position `(2,3)`

### 4.1 Family `p=1`, `q>2`

The relevant layers are

```text
P_0=A x^3,  P_1=u x^2,  P_2=x,
Q_3=c y.
```

Let `f_1` and `f_2` be the coefficients of `x^2y` in `Q_1` and `xy` in `Q_2`.
Then

```text
3Af_1=0,
3Af_2+2u f_1=0,
3Ac+2u f_2+f_1=0,
```

which is impossible.

### 4.2 Exception `w=(1,2)`

Complete relevant supports are

```text
P_0=A x^3,
P_1=u x^2+v y,
P_2=x,
Q_0=B x^5,
Q_1=e x^4+f x^2y+g y^2,
Q_2=r x^3+s xy,
Q_3=c y,
Q_4=kx.
```

The full nontrivial coefficient equations are

```text
3Af-5Bv=0,          6Ag=0,
3As-4ve+2uf=0,      -2vf+4ug=0,
3Ac-3vr+2us+f=0,   -vs+2g=0,
2uc+s=0,
c-vk=1.
```

The last equation retains the simultaneous resonance `J(vy,kx)=-vk`. From
`g=0`, `vs=0`. If `v=0`, then `f=s=u=0` and `3Ac=0`. If `s=0`, then `u=0`;
either `v=0`, or `f=0` and the first equation forces `v=0`. Contradiction.

### 4.3 Family `p=2`, `q>3`

No descent gives `q≡3 mod4`, hence `q>=7`. Here `P_1=0`; if `f` is the
coefficient of `xy` in `Q_1`,

```text
2Af=0,
2Ac+f=0.
```

### 4.4 Exception `w=(2,3)`

The correct top degrees are essential:

```text
P_0=A x^2,
P_1=v y,
P_2=x,
Q_0=B x^3,
Q_1=fxy,
Q_2=r x^2,
Q_3=c y,
Q_4=kx.
```

The equations are

```text
2Af-3Bv=0,
-vf=0,
2Ac-2vr+f=0,
c-vk=1.
```

The first two force `v=f=0`; the third then contradicts `A,c!=0`.

## 5. Position `(3,2)`

### 5.1 Family `p=1`, `q>3`

Write

```text
P_0=A x^4,  P_1=u x^3,  P_3=x,
Q_1=...+fxy,  Q_2=c y.
```

The decisive coefficients are

```text
4Af=0,
4Ac+3uf=0.
```

### 5.2 Highlighted infinite family: `q` divisible by four

Let `q=4r`. Then

```text
rho=gcd(4,q+2)=2,
m=2,
n=(q+2)/2=2r+1,
H=x^2.
```

This is precisely where the maximal common root must be used consistently: one
may not replace `H=x^2` by `x` while retaining coprime exponents. Nevertheless
the same `S_1,S_2` equations above force `f=0` and then `4Ac=0`. Every member of
this infinite support family is excluded.

### 5.3 Exception `w=(1,3)`

Use

```text
P_0=A x^4,
P_1=u x^3+v y,
P_2=r x^2,
P_3=x,
Q_0=B x^5,
Q_1=e x^4+fxy,
Q_2=c y,
Q_3=sx^2,
Q_4=kx.
```

The equations are

```text
4Af-5Bv=0,
4Ac-4ve+3uf=0,  -vf=0,
3uc+2rf=0,
-2vs+2rc+f=0,
c-vk=1.
```

The product equation and the first equation force `v=f=0`; then the second
forces `4Ac=0`.

### 5.4 Family `p=3`

No descent gives `q≡1 mod6`, `q>=7`. The degree-five and degree-four pieces of
`P` vanish, and the coefficient of `x` in `S_2` is simply

```text
2Ac=0.
```

The signed target swap of the equal-weight `(2,3)` audit covers equal-weight
`(3,2)`.

## 6. Position `(4,1)`

Let `M=1+4/p`, so `P_0=A x^M` and `Q_1=c y`. The coefficient
`J(P_0,Q_1)=M A c x^(M-1)` can be cancelled by `J(P_1,Q_0)` only if `P_1`
contains a `y`-monomial, which requires `q<=p+3`. In the no-descent families,
this leaves exactly `(1,2)`, `(1,3)`, and `(2,3)`. Outside those exceptions,
`S_1` gives respectively `5Ac=0`, `3Ac=0`, or `2Ac=0`.

### 6.1 Exception `w=(1,2)`

```text
P_1=u x^4+v x^2y+w y^2,
P_2=r x^3+sxy,
P_3=z x^2+t y,
Q_2=kx.
```

The equations are

```text
5Ac-3Bv=0,       -6Bw=0,
-3Bs+4uc=0,       2vc=0,
-3Bt-vk+3rc=0,   -2wk+sc=0,
-sk+2zc=0,
-tk+c=1.
```

Since `c!=0`, `2vc=0` forces `v=0`, contradicting the first equation.

### 6.2 Exception `w=(1,3)`

```text
P_1=u x^4+vxy,
P_2=r x^3+t y,
P_3=z x^2,
Q_2=kx^2,
Q_3=ell x.
```

The equations are

```text
5Ac-4Bv=0,
-4Bt+4uc=0,  vc=0,
-2vk+3rc=0,
-v ell-2tk+2zc=0,
-t ell+c=1.
```

Again `vc=0` contradicts the first equation.

### 6.3 Exception `w=(2,3)`

```text
P_1=vxy,  P_2=r x^2,  P_3=t y,  Q_2=kx.
```

The equations include

```text
3Ac-2Bv=0,
vc=0,
-2Bt-vk+2rc=0,
-tk+c=1.
```

The first two are incompatible.

## 7. Equal-weight position `(2,3)`

Set `X=H`, choose `Y` with `J(X,Y)=1`, and write

```text
P_0=A X^3,  Q_0=B X^4,
P_2=L=ell X+sY,
Q_3=M=mu X+nY.
```

Initially let

```text
P_1=aX^2+bXY+gY^2.
```

The complete `S_1=0` equation integrates to

```text
Q_1=(4B/(3A)) X P_1+E X^3.
```

The `Y^3` coefficient of `J(P_1,Q_1)` in `S_2` is

```text
-8B g^2/(3A).
```

Since `A,B` are nonzero and the field has characteristic zero, `g=0`. Write

```text
P_1=aX^2+bXY,
Q_1=dX^3+eX^2Y,
Q_2=uX^2+vXY+wY^2.
```

The complete equations are

```text
S_1: 3Ae-4Bb=0,
S_2: 3Av-4Bs+2ae-3bd=0,  6Aw-be=0,
S_3: 3An+2av-2bu-3ds+e ell=0,
     4aw-2es=0,  2bw=0,
S_4: 2an-b mu+ell v-2su=0,
     bn+2ell w-sv=0,
S_5: ell*n-s*mu=1.
```

The first equation and `6Aw=be` give

```text
e=(4B/(3A))b,
w=(2B/(9A^2))b^2.
```

Then `2bw=0` forces `b=0`, so `e=w=0`. The first `S_2` equation gives
`3Av=4Bs`, while the second `S_4` equation gives `sv=0`; hence `s=v=0`.
The first `S_3` equation gives `n=0`, contradicting `ell*n-s*mu=1`.
The signed target swap gives equal-weight `(3,2)`.

## 8. Zero layers and simultaneous resonances

All layers used above are complete weighted-homogeneous supports. Unsupported
degrees are literal zero. The six unequal systems with a second possible
resonant bracket have exact `S_5` equations:

| Position / weight | Retained equation |
|---|---|
| `(2,3)`, `(1,2)` | `c-vk=1` |
| `(2,3)`, `(2,3)` | `c-vk=1` |
| `(3,2)`, `(1,3)` | `c-vk=1` |
| `(4,1)`, `(1,2)` | `c-tk=1` |
| `(4,1)`, `(1,3)` | `c-t ell=1` |
| `(4,1)`, `(2,3)` | `c-tk=1` |

Each contradiction occurs in an earlier stair with `c!=0`; no simultaneous
resonance can repair it.

## 9. Logical levels

The audit distinguishes:

1. **support compatibility** — weighted degrees have monomial support;
2. **coefficient-ideal compatibility** — all coefficients of `S_0,...,S_5`
   satisfy their exact equations with required nonzero data;
3. **actual polynomial pair** — choose the finitely many layers and set deeper
   layers to zero; above-resonance brackets vanish individually;
4. **actual Keller pair in original coordinates** — invert the proved graded
   normalization and orientation maps.

No no-descent system reaches level 2. Consequently none reaches levels 3 or 4.
