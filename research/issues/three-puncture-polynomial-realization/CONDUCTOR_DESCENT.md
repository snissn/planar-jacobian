# Conductor descent and the full primitive

> Authority: `MUTABLE_NONAUTHORITATIVE`  
> Labels: `TPPR-01`, `TPPR-06`

## 1. Target conductor class

For the displayed branch,

```text
A=C[P,Q]/(g)=C[z,z^(-1),(z-1)^(-1)]
```

is already normal. Therefore its normalization `Abar` equals `A`, its
conductor ideal is the unit ideal, and

```text
Abar/A=0.                                               (1.1)
```

The predecessor packet's finite conductor class vanishes automatically:

```text
[R]=0 in Abar/A.                                        (1.2)
```

More strongly, the primitive has the target-polynomial representative

```text
rho=-2P Q^3+3P Q^2-P Q-4Q+2,
rho|_C=R.                                               (1.3)
```

Hence neither value matching nor missing semigroup coefficients obstruct
descent on this branch.

## 2. Exact symplectic identity

For a Keller pair normalized by `dP wedge dQ=dx wedge dy`, the polynomial
one-form

```text
lambda=P dQ+y dx
```

is closed:

```text
d lambda=dP wedge dQ+dy wedge dx=0.
```

Polynomial de Rham exactness on `A2_C` gives a polynomial `H in C[x,y]` with

```text
P dQ+y dx=dH.                                           (2.1)
```

The predecessor Laurent recursion shows that the order-zero tangential
coefficient of `H` must be `R` up to a constant. Equations (1.2)-(1.3) verify
that this condition is satisfied, not contradicted.

The radial leading term is the compatible expression recorded in
`POLE_AND_DIVISOR_TABLE.md`:

```text
H=(m b/(m+n))s^(-(m+n))+... .                          (2.2)
```

## 3. Why higher Laurent classes are not needed here

The all-orders formal models already show that exactness determines many higher
coefficients without forcing them to vanish. Computing another Laurent class
without using polynomiality would therefore repeat the predecessor boundary.

The present packet uses a different implication:

```text
global polynomial P,Q
  => displayed branch is a component of S_F
  => that component must contain polynomial A1-curves
  => contradiction.                                    (3.1)
```

This implication acts at `L4` and does not assert that any higher differential
class is nonzero.

## 4. Conductor mutation

Trivial conductor is proved only for this smooth branch. It is not silently
assumed in general. For example,

```text
C[t^2,t^3] subset C[t]
```

has conductor quotient containing the gap class of `t`; a primitive involving
that class need not descend. The symbolic review includes this mutation to
prevent generalization of (1.1).

## 5. Puncture gluing

The affine branch has three punctures in its smooth projective completion.
Since `R in A`, no finite affine gluing remains. The puncture poles are genuine
projective principal parts:

```text
ord_0(R)=ord_1(R)=-1,
ord_infinity(R)=+1.
```

They are compatible with rational exactness and with the polynomial
representative (1.3) on the affine branch. The terminal obstruction is not that
one polynomial `H` cannot carry these principal parts; it is that no polynomial
map can have this curve as a nonproperness component at all.
