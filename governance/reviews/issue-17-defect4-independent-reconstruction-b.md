# Independent Reconstruction B — Defect Four and Inductive Closure

> **Review mode:** `independent-review`
> **Reviewed candidate:** `96fc7ec34bd3b685a0edeae7ecd4404abab7e2f1`
> **Disposition:** `ACCEPT`

## 5. Defect four

Assume no endpoint resonant term is nonzero and select any nonzero interior
resonant term. Multiple simultaneous resonant terms cause no problem: the
normalization preserves the entire staircase, and all unselected layers remain
generic in the following equations.

### 5.1 Offset `a=1`, position `(1,3)`

No descent forces `p=1`. Equal weights give top exponent one and descend. For
`q>1`,

```text
P_0=A x^2,
Q_0=B x^(q+3),
P_2 in C,
P_3=0.
```

Successive preceding stairs give

```text
S_1=0  => (Q_1)_y=0,
S_2=0  => (Q_2)_y=0,
S_3=J(Ax^2,c y)+J(x,Q_2)=2A c x,
```

contradiction. Missing `Q_1` or `Q_2` is included by setting that layer to zero.

### 5.2 Offset `a=2`, central position `(2,2)`

Normalize `P_2=x`, `Q_2=c y`. The central preceding equation is

```text
c(P_0)_x+J(P_1,Q_1)+(Q_0)_y=0.             (C)
```

For unequal weights and no top descent, write
`P_0=A H^m`, `Q_0=B H^n`. Since `d_Q>d_P`, `n>m>=2`. If
`J(P_1,Q_1)=0`, equation (C) becomes

```text
c A m H_x+B n H^(n-m) H_y=0
```

after dividing by `H^(m-1)`. Thus `H` divides `H_x`. If `H_x!=0`, ordinary
total degree makes this impossible; if `H_x=0`, the same equation forces
`H_y=0`, contradicting nonconstancy. Consequently a surviving central case
would require `P_1,Q_1` both nonzero.

For `p>1`, support of `P_1 in R_(p+1)` forces `q=p+1`, and support of
`Q_1 in R_(q+1)` forces `p|(q+1)`. Hence `(p,q)=(2,3)`. The complete top
supports are

```text
P_0=A x^2,
Q_0=B x y,
```

and `J(P_0,Q_0)=2AB x^2`, contradicting `S_0=0`.

For `p=1`, `q>2`, no descent gives

```text
P_0=A x^3,
Q_0=B x^(q+2),
P_1=u x^2,
Q_1=e x^(q+1)+f x y.
```

The earlier stair `S_1=0` is `3A f x^3=0`, so `f=0`; then the middle
Wronskian is zero and the preceding divisibility contradiction applies. Thus
the central equation alone is not being used.

For the exceptional weight `(1,2)`, the complete supports are

```text
P_1=u x^2+v y,
Q_1=e x^3+f x y.
```

The two required stairs are

```text
S_1=(3A f-4B v)x^3=0,                                      (E1)
J(P_1,Q_1)=(2u f-3v e)x^2-v f y,
S_2=(3A c+2u f-3v e)x^2-v f y=0.                           (E2)
```

Equation (E2) gives `vf=0`; equation (E1) then gives `v=f=0`; the `x^2`
coefficient of (E2) becomes `3A c`, impossible.

For equal weights `(1,1)`, the top degree-three forms are proportional and a
linear target shear descends.

### 5.3 Offset `a=3`, position `(3,1)`

No descent forces `p in {1,2,3}`.

For `p=2`, the common-root degree would have to be at least two and divide
`d_P=5`; the only positive divisors are one and five, and degree five gives
exponent one. Thus no no-descent system exists.

For `p=3`, no descent forces common-root degree three and
`P_0=A x^2`. At `q=5` the top layers are proportional and descend. Every
remaining no-descent weight has `q>=8`, while `P_1 in R_5=0`; hence
`S_1=2A c x`, impossible.

For `p=1`, equal weights and `q=3` descend at the top. For `q>3`, the top
layers are pure `x` powers and `P_1` is a multiple of `x^3`, so
`S_1=4A c x^3`, impossible.

The exceptional weight `(1,2)` has complete supports

```text
P_0=A x^4,
Q_0=B x^3,
P_1=u x^3+v x y,
P_2=r x^2+s y,
Q_2=g x.
```

The earlier stairs are

```text
S_1=(4A c-3B v)x^3=0,
S_2=(3c u-3B s)x^2+c v y=0.
```

The first equation forces `v=4A c/(3B)`, which is nonzero; the `y`
coefficient of the second is therefore impossible. Setting `P_2` or `Q_2` to
zero does not remove `c v y`.

The determinant-one target swap `(P,Q)->(Q,-P)` exchanges `(1,3)` and
`(3,1)` and fixes the central position, so reversed resonant degree orientation
is covered. The determinant-one source swap with weight relabeling covers
`p>q`.

## 6. Inductive closure

Each descent is a polynomial target automorphism, so the descended pair remains
a Keller pair. The weight is unchanged. A complete top layer is removed, so
one actual weighted degree decreases and the integer `kappa` strictly
decreases. The Rees identity, applied anew to the descended Keller pair, proves
the new defect is still nonnegative. Strong induction therefore applies
without assuming the theorem at the current defect.

If the descended normalized pair is an automorphism, inversion of the target
shear, the compensating target scaling, the graded source automorphism, and any
source/target swaps proves that the original pair is an automorphism. No
normalization is discarded at the conclusion.
