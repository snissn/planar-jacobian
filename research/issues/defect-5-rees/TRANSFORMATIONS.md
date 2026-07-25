# Filtration-Compatible Transformation Catalogue

Every transformation used in the defect-five proof appears here. Operations not
listed here are not descent certificates.

## 1. Graded source normalization with scalar retention

Let a selected resonant pair be

```text
A=P_a,  B=Q_b,  a+b=5,  J(A,B)=c in C*.
```

The weighted degrees of `A,B` sum to `p+q`. Their ordinary linear parts have
Jacobian `c` at the origin, so both are nonzero and independent. A weighted
homogeneous polynomial has an `x`-linear term only in degree `p` and a
`y`-linear term only in degree `q`; hence

```text
{deg_w A,deg_w B}={p,q}.                          (T1)
```

After a signed target swap if necessary, take `deg_w A=p`, `deg_w B=q`.
If `p<q`, then

```text
A=a_0 x,
B=b_0 y+h(x),
a_0 b_0=c,
deg_w h=q.
```

The term `h` can occur only when `p=1`. If `p=q`, primitivity gives
`(p,q)=(1,1)` and `(A,B)` is an invertible linear pair. Thus
`psi=(A,B)` is a graded polynomial automorphism. In the unequal case,

```text
psi^(-1)(u,v)=
(u/a_0, (v-h(u/a_0))/b_0).
```

Every monomial in the inverse has the same weighted degree as the coordinate it
replaces. Consequently, for every `d`,

```text
psi^(-1)* R_d = R_d,
psi^(-1)* (sum_(e<=d) R_e) = sum_(e<=d) R_e.        (T2)
```

Let `phi=psi^(-1)` and let `D(u,v)=(u,c v)`. Then

```text
J(D o F o phi)=c * 1 * (1/c)=1,
(P_a,Q_b) -> (x,c y).                               (T3)
```

The scaling `D` alone does not preserve `J=1`; only the compensated composition
(T3) is allowed. The nonzero scalar `c` is retained.

For every layer pair,

```text
J(P_i o phi, c Q_j o phi)
=c (J(P_i,Q_j) o phi) J(phi)
=J(P_i,Q_j) o phi.                                  (T4)
```

Thus all layer indices and every simultaneously nonzero resonant bracket survive
normalization. Scalar resonant brackets are literally unchanged.

## 2. Source-weight orientation

The source automorphism

```text
sigma(x,y)=(y,-x),  J(sigma)=1
```

with weight relabeling `(p,q)->(q,p)` preserves weighted degrees, all layer
indices, and `kappa`. It is used only to arrange `p<=q`; the reverse orientation
is recovered by `sigma^(-1)`.

## 3. Target-component orientation

The signed target swap

```text
tau(P,Q)=(Q,-P),  det(tau)=1
```

preserves `J=1` and changes a resonant position `(a,b)` to `(b,a)`. It also
retains the selected scalar:

```text
J(Q_b,-P_a)=J(P_a,Q_b)=c.
```

The unsigned swap `(Q,P)` is forbidden because it changes the Jacobian to `-1`.
All four interior positions are nevertheless proved in the canonical orientation
where the selected first layer has weighted degree `p`.

## 4. Equal-weight root coordinates

At `(p,q)=(1,1)`, a nonzero linear common root `H` can be completed to a
linear form `K` with `J(H,K)=1`. The coordinate change `(x,y)->(H,K)` is graded
and preserves standard homogeneous layers. It is used to expose the new equal-
weight equations; it does not discard the normalized resonant scalar.

## 5. Complete-top target descent

If the top layers have common-power form

```text
P_0=A H^m,  Q_0=B H^n,
```

and `m=1`, then `Q_0=lambda P_0^n` with `lambda=B/A^n`. The target shear

```text
(P,Q) -> (P,Q-lambda P^n)                         (T5)
```

has determinant one and preserves `J=1`. It cancels the complete top layer of
`Q`, not merely one monomial. Every other term of `P^n` has weight strictly below
`n d_P=d_Q`; hence no replacement of the cancelled top weight is created.
Thus

```text
d'_Q<d_Q,  d'_P=d_P,  kappa'<kappa.                (T6)
```

The case `n=1` uses `(P-lambda Q^m,Q)`. If `m=n=1`, a determinant-one linear
shear cancels one proportional top layer. The transformed pair is Keller, so its
Rees identity gives `kappa'>=0`; from `kappa=5`, (T6) gives `kappa'<=4`.

## 6. Endpoint coordinate changes

For a resonant endpoint, the top component is proved to be a full polynomial
coordinate. Completing it to source coordinates and triangularizing the other
component proves invertibility directly. This coordinate change need not
preserve the original filtration, and it is **not** used as a filtered descent.

## 7. Inversion at the conclusion

Every normalization above is a polynomial automorphism with an explicit inverse.
If the normalized or descended map is an automorphism, composition with the
inverse target shear, compensation, graded source map, and any source/target
swaps proves that the original map is an automorphism.
