# Pole and divisor table

> Authority: `MUTABLE_NONAUTHORITATIVE`  
> Label: `TPPR-06`

Let `Cbar=P1_z` be the smooth projective completion of the displayed affine
branch. Put

```text
alpha_+=(1+i)/2,
alpha_-=(1-i)/2.
```

## 1. Target functions on `Cbar`

| object | expression | divisor on `P1_z` |
|---|---|---|
| `Q` | `z` | `[0]-[infinity]` |
| `Q-1` | `z-1` | `[1]-[infinity]` |
| `R` | `(2z-1)/(z(z-1))` | `[1/2]+[infinity]-[0]-[1]` |
| `P` | `-(2z^2-2z+1)/(z^2(z-1)^2)` | `[alpha_+]+[alpha_-]+2[infinity]-2[0]-2[1]` |
| `P dQ` | `P dz` | `[alpha_+]+[alpha_-]-2[0]-2[1]` |

The differential divisor has degree `-2`, as required for a rational
differential on `P1`. The two zeros of `P` at infinity cancel the double pole of
`dz`.

On the affine curve `C=P1-{0,1,infinity}`, all five displayed objects are
regular. In particular `R` is regular on the affine normalization even though
it has puncture poles on `Cbar`.

## 2. Pullback to the source-boundary normalization

Let `phi:Etilde->Cbar` be the finite map induced by a source-boundary divisor
after normalizing its projective closure. For a function `f` and a point
`p in Etilde` over `a in Cbar`,

```text
ord_p(phi^*f)=e(p/a) ord_a(f).                         (2.1)
```

For a differential,

```text
div(phi^*(P dQ))=phi^*div(P dQ)+Ram(phi).              (2.2)
```

Thus the three puncture fibers and their ramification indices determine the
tangential pole orders. They do not create a radial pole of `P` or `Q` at the
generic point of `E`: as residue functions there, both have radial valuation
zero.

## 3. Source coordinates and the polynomial primitive

After the standard symplectic swap if necessary, normalize the generic
transverse parameter so that

```text
x=s^(-m),                    m>0,
y=b s^(-n)+higher terms,     n>=0, b in C*.            (3.1)
```

The radial part of the exact identity is

```text
y dx=-m b s^(-(m+n)) ds/s+... .
```

Therefore a polynomial primitive `H in C[x,y]`, viewed as a rational function
on a source compactification, must begin

```text
H=(m b/(m+n)) s^(-(m+n))+... .                         (3.2)
```

The pole order table at the generic point of `E` is:

| object | radial valuation |
|---|---:|
| `x` | `-m` |
| `y` | `-n` |
| `P` | `0` |
| `Q` | `0` |
| order-zero branch coefficient of `H` | `R` in the residue field |
| full `H` | `-(m+n)` |
| `R(Q)` | `0` radially; puncture poles tangentially |

Equation (3.2) is compatible for every `m>0,n>=0`; it is not an obstruction.
The terminal contradiction comes instead from the global polynomial map
`F=(P,Q)` and its nonproperness component.

## 4. No monomial-weight inference

The pair `(m,n)` records one divisorial valuation after a formal normalization.
It does not prove simultaneous monomialization in the original polynomial
coordinates and is not identified here with a primitive positive Newton weight.
