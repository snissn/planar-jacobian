# Exact-symplectic principal parts in the one-boundary model

> Authority: `MUTABLE_NONAUTHORITATIVE`  
> Labels: `OBLF-07` and `OBLF-09`

This file retains every negative Laurent coefficient. It does not repeat the
invalid inference from zero residue to regularity.

## 1. Generic boundary expansions

Assume `OBLF-H0` through `OBLF-H3`. At the generic point of the unique boundary
divisor `D0`, choose a uniformizer `pi` and write `k=C(D0)` for the tangential
coefficient field. Let prime denote a fixed nonzero `C`-derivation of `k`.
Write Laurent series with finite negative parts

```text
P = sum_i p_i pi^i,    Q = sum_j q_j pi^j,
x = sum_i x_i pi^i,    y = sum_j y_j pi^j,
H = sum_r h_r pi^r.
```

Because `P,Q in O`, `p_i=q_i=0` for negative `i`. The source functions `x,y`
and the polynomial primitive `H in C[x,y]` can have poles on `Y` because they
are required to be regular only on `U`. For each fixed coefficient order, the
sums below are finite because every series has a lower exponent bound.

The equality

```text
dP wedge dQ = dx wedge dy
```

gives, for every integer `r`,

```text
sum_(i+j=r) (i p_i q'_j - j p'_i q_j)
 =
sum_(i+j=r) (i x_i y'_j - j x'_i y_j).       (2.1)
```

The primitive

```text
P dQ + y dx = dH
```

gives

```text
r h_r = sum_(i+j=r) j (p_i q_j + y_i x_j),    (2.2)

h'_r = sum_(i+j=r) (p_i q'_j + y_i x'_j).     (2.3)
```

These are the complete coefficient equations. Equation (2.3) is compatible
with the tangential derivative of (2.2) precisely because of (2.1); it is not
an independent pole-elimination identity.

## 2. What exactness kills

At `r=0`, (2.2) is the zero-residue equation

```text
0 = sum_(i+j=0) j(p_iq_j+y_ix_j).              (2.4)
```

For every `r<0`, however, division by the nonzero integer `r` gives

```text
h_r = (1/r) sum_(i+j=r) j(p_iq_j+y_ix_j).      (2.5)
```

Thus the negative coefficient of the one-form is absorbed by a negative
coefficient of `H`. One-boundary support does not change this algebraic fact.
For example, `x=pi^(-1)` and `H=x^m` give

```text
dH=-m pi^(-m-1)dpi
```

with zero logarithmic residue and a nonzero higher pole.

## 3. The first additional one-boundary equation

One-boundary geometry does add a common valuation. Let

```text
x = a pi^(-m) + higher powers,
y = b pi^(-n) + higher powers,
```

where `a,b in k*`, `m,n>=0`, and `m+n>0`. Since the left side of (2.1) is zero
for negative `r`, its lowest equation, at `r=-(m+n)`, is

```text
n a' b - m a b' = 0.                           (2.6)
```

This is `OBLF-07`. Equivalently,

```text
(a^n/b^m)'=0                                   (2.7)
```

when `m,n>0`. If `d=gcd(m,n)`, there are constants `alpha,beta in C*` and a
function `c in k*` such that, after adjusting constants,

```text
a = alpha c^(m/d),   b = beta c^(n/d).          (2.8)
```

The statement is in the function field; it does not assert that `c` is regular
on the boundary curve or that a corresponding divisor is principal on a
compactification.

At the same lowest order, (2.2) determines the leading negative coefficient of
the primitive:

```text
h_(-(m+n)) = m a b/(m+n).                       (2.9)
```

Equation (2.9) is determination, not vanishing. Once the pole orders are fixed,
the remaining negative orders through order zero form a finite coupled
coefficient system; no triangular solvability is claimed.

If `n=0`, (2.6) says `a b'=0`, so the leading regular coefficient of `y` is
constant along `D0`; the symmetric statement holds if `m=0`. This is a genuine
one-boundary restriction but still does not force absence of the pole.

## 4. Interaction with a semisimple field

Suppose an integral-weight target field has been linearized to

```text
E=m_0 u partial_u+n_0 v partial_v
```

and the reduced branch equation is a semi-invariant of weight `d`. The local
system then includes

```text
m_0 u g_u+n_0 v g_v=d g,                        (2.10)
```

in addition to (2.1)-(2.3). In a one-boundary Keller model satisfying the
ramified hypotheses, any solution of (2.10) produces an actual target torus
action and is excluded by `OBLF-05`. Therefore the remaining branch equations
must have no nonzero integral semisimple solution.

The exact-symplectic identities do not themselves imply (2.10). Their first
new one-boundary consequence is (2.6), which involves the leading source pole
coefficients rather than the target branch polynomial.

## 5. Fixed-type finite compatibility system

For fixed data

```text
(m,n), ramification index e, branch equation g,
normalization of D0, conductor algebra, and puncture set,
```

the negative and zero-order compatibility conditions are finite:

1. logarithmic lifting:

   ```text
   A g_P+B g_Q = c g;
   ```

2. semisimple/integral test, if sought: the semisimple part preserves `(g)`
   and the selected cocharacter has integral weights on `B`;
3. Laurent equations (2.1)-(2.3) from the lowest pole through order zero;
4. the leading relation (2.6) and primitive coefficient (2.9);
5. conductor descent modulo the finite conductor quotient;
6. source-open tangency at the boundary prime.

This is `OBLF-09`. It is finite after the valuation and conductor type are
fixed. No uniform bound on those types is proved here, so the general
one-boundary class is not declared solved.

## 6. No weighted-homogeneity conclusion from exactness

The logical implications established are

```text
one boundary + exact symplectic
=> common pole support + (2.1)-(2.9),
```

not

```text
one boundary + exact symplectic
=> weighted-homogeneous branch.
```

A proof of the latter would require a new bridge from the source pole
coefficients and conductor data to a target semi-invariance equation. If such
a bridge is found, `OBLF-05` immediately excludes the ramified model.