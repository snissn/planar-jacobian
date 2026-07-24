# Rank-Three Theorem or Exact Obstruction

```text
status: BLOCKED
accepted_disposition: exact differential/divisor reduction plus correction
```

## 1. Conditional rank-three terminal theorem

### Theorem 1.1

Assume:

1. `B=C[P,Q]`, `L=C(x,y)`, and `O` is the normalization of `B` in `L`;
2. `O` is finite locally free of rank three over `B`;
3. `U=Spec(C[x,y])->Y=Spec(O)` is the specified open immersion, with ring map
   `O->C[x,y]`, and `J(P,Q)=1` on `U`;
4. there exists `s in E=ker Tr_{O/B}` such that `Phi(s) in C*`.

Then

```text
O=B[s] and [L:K]=1.
```

Proof. The unit determinant makes `B^3 -> O`, `(a,b,c)->a+bs+cs^2`, an
isomorphism, so `O=B[s]`. The issue #3 minimal-polynomial derivative argument
then forces degree one.

This theorem isolates the only missing implication; it does not assert (4).

## 2. Proved rank-three support theorem

### Theorem 2.1 — finite Keller source/boundary certificate

Under hypotheses 1-3 above, there exist five integral trace-free sections

```text
theta,s_0,s_1,s_2,s_3 in E
```

such that their fixed-section index values have no common height-one factor.

Proof. Choose four distinct constants `lambda_i` and clear the boundary poles
of `x+lambda_i y` by a common base multiplier. Away from the finite image of
the boundary, one of the four directions separates every geometric cubic
fiber. Apply issue #3 finite-prime adaptation to one section `theta` at all
height-one components of the boundary/denominator image. The five localized
values generate at every height-one base prime.

Equivalently,

```text
gcd(Phi(theta),Phi(s_0),Phi(s_1),Phi(s_2),Phi(s_3))=1             (2.1)
```

in the UFD `C[P,Q]`, although the ideal they generate can remain supported at
finitely many closed points.

Theorem 2.1 is not a global primitive-element theorem: a nonlinear cubic value
of a combination need not be a combination of the five values, and a generic
combination can create a new divisor.

## 3. Exact correction to the universal-index formulation

### Proposition 3.1

The following implications are false in general, even for the issue #3 smooth
rational cubic algebra:

```text
J_Phi=B  =>  exists s with Phi(s) in C*,
fiberwise local monogenicity  =>  global monogenicity.            (3.1)
```

The countermodel polynomial `uX^3+X^2Y+vY^3` has content one and no unit value.
Thus the phrase “universal index ideal is the unit ideal” must mean the
fixed-section ideal `Fitt_0(O/B[s])=B` for one named section, not merely the
coefficient ideal of the universal cubic.

## 4. Keller-specific different exclusion

### Proposition 4.1

For a Keller normalization, the ramification/different divisor of `O/B` is
supported in `Y-U`.

Proof. Pullback along `O->A` identifies the relative differential module with
`Omega_{A/B}`, which vanishes by the Jacobian criterion. The Fitting support of
`Omega_{O/B}` therefore misses `U`.

This excludes the issue #3 model's invariant failure but leaves unramified
index collisions untouched.

## 5. Exact differential reduction

### Proposition 5.1

For any primitive cubic coordinate `t`, minimal polynomial `F`, and quadratic
representatives `x=X(t), y=Y(t)`, the Keller condition is equivalent to the
congruence

```text
F_T
 = F_T(X_PY_Q-X_QY_P)
   +F_P(X_QY_T-X_TY_Q)
   +F_Q(X_TY_P-X_PY_T) mod F.                                    (5.1)
```

This is proved directly in `DIFFERENTIAL_IDENTITIES.md`. It is a finite system
of three rational coefficient equations after reduction modulo the monic
cubic. Every denominator comes from the coefficients of `F,X,Y` and hence from
boundary valuations.

## 6. Smallest surviving divisor identity

Let `r=a(P,Q)x+b(P,Q)y` be a primitive source-linear function and let
`m in B\{0}` clear its boundary poles, so the trace-free part

```text
s=(m r)^0 in E.
```

Then

```text
Phi(s)=m^3 Phi_K(r).                                               (6.1)
```

The rank-three theorem follows if one proves, for one such pair `(r,m)`,

```text
div_B(Phi_K(r)) = -3 div_B(m).                                   (6.2)
```

Equivalently, all nonboundary pair-collision factors of the Vandermonde of `r`
are absent, and every boundary valuation is exactly canceled by the cube of the
integrality multiplier.

The four-direction lemma proves only the pointwise finite-family version of
“no nonboundary collision”; it does not select one global `r`. Equation (5.1)
provides the additional differential constraint, but this packet does not yet
derive (6.2) from it.

## 7. Final disposition

The primary theorem remains `BLOCKED`. The exact successor is:

> Use the cubic congruence (5.1), the boundary-only support of the different,
> and the four-direction finite certificate to prove the boundary-cube equality
> (6.2) for one source-derived primitive coordinate, or construct a genuine
> rank-three Keller-compatible model violating it.

This is strictly smaller than the generic issue #3 problem: the universal
content route is retired, interior ramification is excluded, the obstruction is
localized to boundary denominators and moving scalar collisions, and the
Keller differential constraint is an explicit three-coefficient congruence.
