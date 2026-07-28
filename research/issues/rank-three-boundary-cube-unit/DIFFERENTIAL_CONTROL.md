# Differential Control of the Fixed-Section Collision Divisor

```text
authority: MUTABLE_NONAUTHORITATIVE
local_claim: R3BC-04
```

## 1. Canonical Keller derivations

For

```text
J(P,Q)=P_x Q_y-P_y Q_x=1
```

after the harmless constant normalization, define

```text
D_P = Q_y partial_x-Q_x partial_y,
D_Q = -P_y partial_x+P_x partial_y.
```

Then

```text
D_P(P)=1,   D_P(Q)=0,
D_Q(P)=0,   D_Q(Q)=1,
[D_P,D_Q]=0.
```

Thus their restrictions to `B=C[P,Q]` are `partial_P` and `partial_Q`.
The signs agree with `CLM-010` and the predecessor differential packet.

These derivations act regularly on the source algebra `A=C[x,y]`. Their
extension to the fraction field acts on any rational primitive coordinate, but
need not preserve the finite normalization order across ramified boundary
components. No stability of `O` or `E` is assumed here.

## 2. Split-sheet formula on the étale locus

Work étale-locally on a target open where the cubic cover splits:

```text
O_et = B_et e_1 x B_et e_2 x B_et e_3.
```

Idempotents are horizontal under any lifted derivation. Indeed, if `e^2=e`, then

```text
D(e)=D(e^2)=2eD(e),
(1-2e)D(e)=0,
```

and `(1-2e)^2=1`, so `D(e)=0`.

For a fixed section `s`, write its three sheet values `z_1,z_2,z_3`. With a
horizontal determinant frame,

```text
Phi(s)=(z_2-z_1)(z_3-z_1)(z_3-z_2).
```

Away from the collision divisor,

```text
D log Phi(s)
 = (D z_2-D z_1)/(z_2-z_1)
 + (D z_3-D z_1)/(z_3-z_1)
 + (D z_3-D z_2)/(z_3-z_2).                 (2.1)
```

Formula (2.1) shows what can happen at an accidental scalar collision. Along a
generic component where `z_j-z_i=0`, the corresponding summand has a pole when
the relative velocity

```text
D(z_j-z_i)=D z_j-D z_i
```

is nonzero modulo that collision divisor (equivalently, the derivation is
transverse at its generic point). If the relative velocity also vanishes there,
the collision is tangent in that direction and no pole is forced by this
summand. Source étaleness says the sheets themselves remain distinct as points;
it neither forces transversality nor says one scalar function takes distinct
values on them.

## 3. No divisor is stable under both target translations

### Lemma 3.1

Let `g in C[P,Q]` be irreducible and nonconstant. The principal ideal `(g)`
cannot be stable under both `partial_P` and `partial_Q`.

### Proof

Stability would imply

```text
g | partial_P g,
g | partial_Q g.
```

Each nonzero derivative has smaller total degree than `g`, so both derivatives
must vanish. In characteristic zero this makes `g` constant, contradiction. ∎

The same minimal-degree argument shows that a nonzero ideal stable under both
translations is the unit ideal (`CLM-012`).

### Corollary 3.2

If an irreducible component of a fixed-section collision divisor were invariant
under both canonical translations, it would be impossible. At least one
translation moves every nonconstant component.

This is a movement statement, not a vanishing theorem.

## 4. Why fixed-section ideals are not known to be stable

Let `s in E` and suppose a derivation acts where `s` is defined. Differentiating

```text
Phi(s)=1 wedge s wedge s^2
```

gives terms involving `D(s)`. Unless `D(s)` is constrained to the line spanned
by `s` modulo base scalars, there is no identity

```text
D(Phi(s)) in (Phi(s)).
```

The denominator-cleared differential identity from the predecessor controls the
universal coefficient/content ideal. It does not principalize the fixed value
and does not make `(Phi(s))` stable.

In the affine family

```text
s_T=theta+H T eta,
```

a target translation differentiates `T`, `H`, the coefficients of `theta` and
`eta`, and the cubic coefficients. Even if one specializes `T` to solve finitely
many local conditions, the derivative of the new collision polynomial is not
forced to be a multiple of that polynomial.

## 5. Primitive-coordinate differential congruence

Suppose a primitive cubic coordinate `t` has monic minimal polynomial

```text
F(T;P,Q)=0
```

and source coordinates have quadratic representatives

```text
x=X(T;P,Q),
y=Y(T;P,Q).
```

The predecessor proves that the Keller identity is equivalent modulo `F` to

```text
F_T
 = F_T (X_P Y_Q-X_Q Y_P)
 + F_P (X_Q Y_T-X_T Y_Q)
 + F_Q (X_T Y_P-X_P Y_T).                  (5.1)
```

All partial derivatives hold `T` fixed. Formula (5.1) is exact and detects the
boundary denominators needed to express `x,y` in the primitive coordinate.
It has two important negative consequences:

1. it does not imply `F_T` is a unit in the normalization unless the primitive
   coordinate already generates the integral order;
2. it does not imply a fixed binary-cubic value `Phi(s)` divides either of its
   target derivatives.

Thus (5.1) is compatible with moving unramified collision divisors.

## 6. Boundary support of the different versus collision support

Under `CLM-066`, the relative different/ramification support is contained in the
normalization boundary. The affine family of `BOUNDARY_VALUATIONS.md` is chosen
so that its index is a unit at every boundary prime. Therefore any divisor of
`Phi(s_T)` is disjoint from the ramified height-one support.

At such a divisor:

```text
Disc(O/B) is a unit,
Disc(B[s_T]/B)=Phi(s_T)^2 Disc(O/B),
```

so the discriminant zero is pure excess index: two values of `s_T` collide on
otherwise distinct étale sheets. Differential control must separate scalar
values, not merely prove absence of ramification.

## 7. Exact differential disposition

The strongest supported statement is:

```text
no nonconstant collision component is invariant under both translations,
but no theorem makes the whole fixed-section ideal translation-stable.
```

Accordingly, canonical derivations show that the collision divisor moves; they
do not supply a translation whose flow removes all components without creating
new ones. The Orevkov terminal theorem excludes the rank-three Keller case
before such a flow construction is needed.
