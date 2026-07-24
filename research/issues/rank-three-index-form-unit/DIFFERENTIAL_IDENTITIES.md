# Differential and Symplectic Identities

```text
claims: IDX3U-04, IDX3U-06
status: CANDIDATE_PROVED_WITH_EXPLICIT_DENOMINATORS
```

## 1. Canonical source derivations

With `J(P,Q)=1`, the target coordinate derivations act on `A=C[x,y]` by

```text
D_P = Q_y partial_x - Q_x partial_y,
D_Q = -P_y partial_x + P_x partial_y.                              (1.1)
```

They satisfy

```text
D_P(P)=1, D_P(Q)=0,
D_Q(P)=0, D_Q(Q)=1,
[D_P,D_Q]=0.                                                       (1.2)
```

They extend uniquely from `K` to the finite separable field `L`. Equations
(1.1)-(1.2) hold on `A`, but they do not imply `D_P(O),D_Q(O) subset O`.

## 2. Exact differential of the index section

For `s in E`, in `det(O) tensor K`,

```text
D Phi(s)
 = D(1 wedge s wedge s^2)
 = 1 wedge D(s) wedge s^2
   + 2(1 wedge s wedge sD(s)).                                    (2.1)
```

Let `e=(1,e_1,e_2)` be a global `B`-frame of `O` and write

```text
D(e_j)=sum_i A_ij e_i,  A_ij in K.
```

If `omega=1 wedge e_1 wedge e_2`, then

```text
D(omega)=Tr(A) omega.                                              (2.2)
```

Writing `Phi(s)=phi(s)omega`, equations (2.1)-(2.2) give

```text
D(phi(s)) + Tr(A) phi(s)
 = coefficient of
   1 wedge D(s) wedge s^2 + 2(1 wedge s wedge sD(s)).              (2.3)
```

All entries of `A` and `D(s)` are rational. A common denominator `h_D` makes
`h_D A` and `h_D D(s)` integral and yields the weighted stability recorded in
`UNIVERSAL_INDEX_IDEAL.md`. Dropping `A`, `Tr(A)`, or `h_D` reverses the logical
direction and assumes the result sought by the stable-order track.

## 3. Different formula on a monogenic chart

Suppose locally `O=B[s]` with monic cubic

```text
f(T)=T^3+aT^2+bT+c.
```

For either target derivation,

```text
f'(s)D(s) = -(D a)s^2-(D b)s-D c.                                (3.1)
```

The denominator `f'(s)` generates the Kähler different in the monogenic chart.
It is a unit precisely on the étale locus. Formula (3.1) makes every pole term
visible and explains why the canonical derivations are regular on the Keller
source yet may have poles along the boundary ramification divisor.

## 4. Primitive-coordinate cubic identity

Choose any primitive element `t in L` for the separable cubic extension
`L/K`. Let

```text
F(T)=T^3+aT^2+bT+c in K[T]
```

be its monic minimal polynomial. Every element of `L` has a unique quadratic
representative, so write

```text
x=X(t),  y=Y(t),
X,Y in K[T],  degree_T < 3.                                       (4.1)
```

Subscripts `P,Q` below differentiate the coefficients while holding `T` fixed;
subscript `T` differentiates in `T`. From `F(t)=0`,

```text
dt = -(F_P(t)dP+F_Q(t)dQ)/F_T(t).                                (4.2)
```

Substitute (4.2) into `dx=dX(t)` and `dy=dY(t)`. The coefficient determinant of
`dP,dQ` is

```text
J(P,Q)^(-1)
 = [ F_T(X_PY_Q-X_QY_P)
     +F_P(X_QY_T-X_TY_Q)
     +F_Q(X_TY_P-X_PY_T) ] / F_T                                 (4.3)
```

inside `L`. Since `J(P,Q)=1`, the exact identity is

```text
F_T
 = F_T(X_PY_Q-X_QY_P)
   +F_P(X_QY_T-X_TY_Q)
   +F_Q(X_TY_P-X_PY_T)                 in K[T]/(F).                (4.4)
```

This is the promised rank-three Keller-specific coefficient identity. It is a
quadratic congruence after reduction modulo `F`; clearing the denominators of
`a,b,c` and the coefficients of `X,Y` gives a finite explicit polynomial
system in `C[P,Q]`.

If the source coordinate `x` itself is primitive, take `t=x` and `X=T`.
Equation (4.4) simplifies to

```text
F_T = F_Q Y_P - F_P Y_Q             in K[T]/(F).                  (4.5)
```

No theorem that `x` must be primitive is consumed; (4.4) works for an arbitrary
primitive `t`.

## 5. Relation to the different and index

The element `F_T(t)` is the monogenic trace-dual/Jacobian denominator. After
localizing at a place where an integral primitive `t` generates an order, it
generates that order's different. Equation (4.4) expresses it as a
target-coefficient Jacobian of the
quadratic representatives of the source coordinates. It therefore links:

- the monogenic different denominator (`F_T`);
- boundary denominators of the primitive coordinate and of `X,Y`;
- the symplectic identity;
- the source coordinate pair that jointly separates points.

What remains missing is an integrality/divisor estimate converting (4.4) into

```text
m^3 Phi_K(t) in C*                                                 (5.1)
```

for a base multiplier `m` making the trace-free part of `mt` integral.
Equation (4.4) itself permits denominators and does not principalize the index.

## 6. Rational symplectic control

The rational functions

```text
P=x^3,
Q=y/(3x^2)
```

satisfy

```text
dP wedge dQ = dx wedge dy,
[L:K]=3.
```

Here `F(T)=T^3-P` and `Y(T)=3QT^2`, and (4.5) becomes the identity
`3T^2=3T^2`. This control has the desired differential identity but fails the
polynomial Keller-source hypotheses: `Q` is not in `C[x,y]`, and the relevant
finite model only matches the source after inverting `x`.

Thus exact symplecticity alone does not imply a unit index value.

## 7. Exact primitive and principalization warning

The equality

```text
dP wedge dQ = dx wedge dy
```

implies that `P dQ + y dx` is polynomially exact on the source. This produces
coefficient equations for boundary Laurent expansions and zero logarithmic
residue, as recorded in issue #5. Exactness does not force a regular top form
or an index determinant to be nowhere zero; no principalization conclusion is
drawn from it here.

## 8. Outcome of attack C

Proved:

- the exact differential (2.1);
- all frame and denominator terms (2.3);
- the local different formula (3.1);
- the rank-three primitive-coordinate identity (4.4).

Open:

- a valuation consequence of (4.4) strong enough to establish (5.1);
- a proof that its denominator divisor is exactly a removable boundary cube.
