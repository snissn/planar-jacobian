# Transformation Audit

## 1. Catalogue and disposition

Every transformation used in the proof was recomputed. No arbitrary formal
change of layers is accepted as a descent certificate.

| Operation | Formula | Jacobian | Filtration role | Result |
|---|---|---:|---|---|
| Graded source map | `psi=(A,B)` for a selected constant-bracket pair | `c` | graded automorphism | verified |
| Graded source inverse | `phi=psi^(-1)` | `1/c` | preserves every `R_d` | verified |
| Target compensation | `D(u,v)=(u,c v)` | `c` | used only with `phi` | verified |
| Source orientation | `sigma(x,y)=(y,-x)` | `1` | swaps source weights after relabeling | verified |
| Target orientation | `tau(P,Q)=(Q,-P)` | `1` | swaps component positions | verified |
| Complete-top shear | `(P,Q-lambda P^n)` or symmetric | `1` | strict defect descent | verified |
| Endpoint coordinate change | complete a polynomial coordinate | nonzero constant | need not preserve filtration | verified |

## 2. Constant-bracket graded automorphism

For a selected pair `A=P_a`, `B=Q_b` with `J(A,B)=c!=0`, weighted homogeneity
and the nonzero ordinary linear determinant force the degree multiset `{p,q}`.
After a signed target swap, `deg_w A=p`, `deg_w B=q`.

If `p<q`,

```text
A=a_0 x,
B=b_0 y+h(x),
a_0b_0=c,
```

with `h=0` unless `p=1`. Its polynomial inverse is

```text
psi^(-1)(u,v)=(u/a_0, (v-h(u/a_0))/b_0).
```

Every monomial in the inverse has the weight of the coordinate replaced. If
`p=q`, primitivity gives `(1,1)` and the pair is invertible linear. There is no
completion-valued or rational substitution in this step.

## 3. Determinant compensation and scalar retention

Set `phi=psi^(-1)` and `D(u,v)=(u,c v)`. Then

```text
J(D o F o phi)=c*1*(1/c)=1.
```

The selected pair becomes `(x,c y)`, not `(x,y)`. For all layer indices,

```text
J(P_i o phi,c Q_j o phi)=J(P_i,Q_j) o phi.
```

Thus:

- each individual layer remains at its original drop index;
- each zero layer remains zero;
- every unselected resonant bracket survives;
- each scalar resonant bracket retains its exact scalar and sign;
- the full equations `S_0,...,S_5` remain equivalent.

An uncompensated target scaling has Jacobian `c` and is invalid. The independent
checker explicitly detects that corruption.

## 4. Source-weight order

For original `p>q`, precompose with

```text
sigma(x,y)=(y,-x).
```

A monomial `x^i y^j` becomes `(-1)^j x^j y^i`; under relabeled weight `(q,p)`
its degree is `qj+pi`, equal to the original `pi+qj`. Hence `d_P,d_Q`, every
layer index, and `kappa` are preserved. Because `J(sigma)=1`, the Keller
condition is preserved. The inverse recovers the original map.

## 5. Component order

Use only the signed swap

```text
tau(P,Q)=(Q,-P).
```

It has determinant one and

```text
J(Q_b,-P_a)=J(P_a,Q_b)=c.
```

It sends position `(a,b)` to `(b,a)` without negating the selected scalar. The
unsigned swap has determinant `-1` and is rejected. Programmatic stair expansion
confirms that each entire `S_n` is unchanged after the signed swap.

## 6. Equal-weight root coordinates

At `(p,q)=(1,1)`, the maximal common root has degree one. Choose a linear `Y`
with `J(H,Y)=1` and set `X=H`. This is a graded determinant-one source
coordinate change, so standard homogeneous layers remain standard homogeneous
layers and every stair is pulled back exactly. The transverse coefficients in
`CASE_AUDIT.md` are therefore intrinsic to the normalized system, not artifacts
of a non-graded chart.

## 7. Complete-top cancellation

Suppose

```text
P_0=A H,  Q_0=B H^n.
```

With `lambda=B/A^n`, the shear

```text
(P,Q)->(P,Q-lambda P^n)
```

cancels `Q_0` as a whole. It does not merely delete one supported monomial. Any
other term in `P^n` contains a lower layer and has weight less than `n d_P`, so
the old top weight is absent after cancellation. Therefore `d'_Q<d_Q`, the same
positive weight is retained, and the actual integer `kappa` strictly decreases.
The Rees identity of the transformed Keller pair prevents negative defect.

A deliberately partial subtraction, such as deleting one monomial from a
multi-term top form, leaves the old weighted degree and is rejected by the
checker.

## 8. Endpoint coordinate and inversion

The endpoint argument proves that a full component is a polynomial coordinate,
not merely that its top form is one. Completing it to a source coordinate makes
the second component affine in the complementary variable. This operation is
used to prove direct invertibility, not as a filtered descent.

All transformations used in an interior proof have explicit polynomial inverses:
`phi^(-1)=psi`, `D^(-1)`, `sigma^(-1)`, `tau^(-1)`, and the inverse target
shear. Automorphy of the normalized or descended map therefore implies
automorphy of the original pair.

## 9. Mutation controls

The reviewer checker detects nine intentional corruptions:

1. plus-sign in place of the Jacobian determinant;
2. unsigned target component swap;
3. uncompensated determinant scaling;
4. a non-graded source substitution that mixes layer degrees;
5. a shifted Rees exponent;
6. partial rather than complete top cancellation;
7. an incorrect source-weight orientation rule;
8. premature deletion of a simultaneous resonance;
9. the wrong top common-power degree `Q_0=B x^2` in the `(2,3)`-weight exception.
