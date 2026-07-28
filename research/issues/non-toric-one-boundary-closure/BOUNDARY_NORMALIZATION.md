# Boundary normalization and the leading equation

> Authority: `MUTABLE_NONAUTHORITATIVE`  
> Primary label: `NTLC-02`

## 1. Coefficient functions and changes of parameter

At the generic point of `E`, choose a uniformizer `t` and write

```text
x=t^(-m)(a+O(t)),
y=t^(-n)(b+O(t)),
```

where `a,b in ell*`, `m,n>=0`, and `m+n>0`. If `t` is replaced by
`t_new=u t` with `u in ell*`, then

```text
a_new=u^m a,  b_new=u^n b.
```

Thus `a^n/b^m` is independent of the chosen normalized parameter. Globally,
`a` and `b` are rational sections of powers of the conormal line at the smooth
generic locus; the ratio is a rational function on the normalization of `E`.

## 2. Independent sign derivation

Using `dt/t` and a nonzero derivation prime on `ell`, the leading contribution
to `dx wedge dy` is

```text
(n a' b-m a b') t^(-(m+n)) dt/t wedge dz.          (2.1)
```

The target form has positive `t`-order at a ramified divisor, hence (2.1)
vanishes:

```text
n a' b-m a b'=0.                                   (2.2)
```

The sign is fixed by

```text
dx=(-m a dt/t+d a)t^(-m)+...,
dy=(-n b dt/t+d b)t^(-n)+...,
```

so the coefficient of `dt/t wedge dz` is `n b d a-m a d b`.

## 3. Divisor-safe common-power theorem

Assume `m,n>0`. Equation (2.2) gives

```text
d(a^n/b^m)=0.
```

Because the constant field of `ell` is `C`,

```text
a^n/b^m=lambda in C*.                              (3.1)
```

Let `d=gcd(m,n)`, `m=d m0`, `n=d n0`, and
`gcd(m0,n0)=1`. Since `C` is algebraically closed, (3.1) implies
`a^n0/b^m0 in C*`. Choose integers `r,s` with

```text
r m0+s n0=1
```

and set the rational conormal section

```text
h=a^r b^s.
```

Then constants `alpha,beta in C*` satisfy

```text
a=alpha h^m0,  b=beta h^n0.                        (3.2)
```

This construction never divides by `a` or `b` at a zero on the compactified
curve; it takes place in the function field. Divisors satisfy

```text
n0 div(a)=m0 div(b),
div(a)=m0 div(h),  div(b)=n0 div(h).                (3.3)
```

Hence common zeros, poles, and puncture orders occur in the exact proportions
`m0:n0`. The statement does not assert that `h` is a regular unit on the
affine normalization.

## 4. Zeros, units, and punctures

Let `Ebar` be a smooth projective completion of the normalization of `E` and
`S=Ebar-Etilde` its puncture set.

- As a rational section of the relevant conormal power, `h` has a divisor on
  `Ebar`; its affine zeros are precisely the points where the displayed generic
  pole orders of both source coordinates drop in the proportions (3.3).
- If that conormal power has been separately trivialized and the resulting
  function is a unit on `Etilde`, its divisor is supported on `S`.
- Only in this honest-function situation does `|S|=1` force the unit to be
  constant: a degree-zero principal divisor supported at one point is zero.
- Without a trivialization, a rational section may have nonzero line-bundle
  degree concentrated at the unique puncture. One puncture therefore does not
  make the leading section constant.
- Positive genus does not invalidate (3.2); it affects whether prescribed
  differential recursions have rational primitives.

Generic leading coefficients may vanish at special affine points, and no
conormal trivialization or principal divisor is inferred from one-boundary
support.

## 5. Edge cases

If `n=0` and `m>0`, (2.2) becomes `m a b'=0`, so the leading regular coefficient
`b` is constant. If `m=0<n`, the symmetric statement holds. If the coordinate
with a pole is `y` rather than `x`, replace

```text
(X,Y)=(y,-x).
```

Then `dX wedge dY=dx wedge dy` and

```text
Y dX=y dx-d(xy),
```

so the exact-symplectic primitive changes only by an exact polynomial.

## 6. Relation to the normalized recursion

The proof in `LAURENT_RECURSION.md` is stronger. After a finite extension and
setting `s=x^(-1/m)`, the leading coefficient of `y` becomes a complex
constant. Translating back to `t` yields (3.1)-(3.3), while all coefficients
through the pre-ramification range become constant as well.
