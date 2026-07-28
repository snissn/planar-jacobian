# Countermodel Ladder and the Source-Étale Wall

```text
authority: MUTABLE_NONAUTHORITATIVE
local_claims: R3BC-05, R3BC-07
R3BC-05_status: LITERATURE_BOUND_APPLICATION
```

## 1. Starting no-unit model

The integrated predecessor constructs a smooth rational finite-flat rank-three
cover with binary cubic

```text
Phi(U,V)=u U^3+U^2 V+v V^3
```

over `B=C[u,v]`. Its coefficient ideal is the unit ideal, but it represents no
nonzero constant. The total space is connected, normal, rational, and contains a
displayed open affine plane.

On that affine plane with coordinates `(u,s)`, the target map is

```text
P=u,
Q=u s^3-s^2,
```

and

```text
J(P,Q)=s(3us-2).
```

Hence the relative different meets the displayed source open. This model
correctly refutes the generic inference

```text
unit content or local monogenicity => one unit value,
```

but it is not a Keller normalization.

## 2. Stage table

| Stage | Added condition | Disposition |
|---|---|---|
| 1 | finite locally free rank three | achieved by the integrated no-unit model |
| 2 | normal and connected | achieved |
| 3 | rational total space | achieved |
| 4 | an open `A2` | achieved |
| 5 | relative different supported outside the displayed open | impossible for a rank-three polynomial source by Proposition 3.1 below |
| 6 | étaleness on the displayed open | equivalent to the relevant part of stage 5; impossible |
| 7 | exact-symplectic or primitive-coordinate differential congruence | not reached: stage 5 already contradicts Orevkov |
| 8 | canonical derivations with Keller signs | not reached for the same reason |
| 9 | no unit value of `Phi` | retained through stage 4, but no stage-5 model exists |

Thus the predecessor countermodel is maximal on this ladder: every condition up
to an abstract open affine plane is compatible with no unit value, while the
first genuine Keller condition is terminally incompatible with degree three.

## 3. Stage 5 already implies a rank-three Keller map

### Proposition 3.1

Let `Y=Spec(O)` be a finite normal connected rank-three cover of
`Spec(B)=A2_C`. Suppose `U subset Y` is the specified open source with

```text
U isomorphic to A2_C,
```

and the relative different of `O/B` has no support on `U`. Then the induced
polynomial map

```text
F:U=A2_C -> A2_C
```

is étale. If its function-field degree is three, this contradicts Orevkov's
theorem.

### Proof

The support of the relative different is the height-one ramification support.
Its absence on `U`, together with the finite-normalization/source-open setup,
gives `Omega_{U/B}=0`. Under coordinates `U=Spec C[x,y]`, this module is
presented by the Jacobian matrix of `P,Q`; vanishing means the determinant is a
unit of `C[x,y]`, hence a nonzero constant. The function field of `U` is the
function field of `Y`, so its degree over `C(P,Q)` is three. By
`FOUNDATIONS.md`, the map is generically three-sheeted. Orevkov excludes a
constant Jacobian. ∎

### Scope caution

An arbitrary abstract open `A2` in a rational surface is not enough. The
proposition uses the displayed open in the finite-normalization factorization,
so the target coordinates restrict to polynomials on that `A2` and the different
controls the restricted morphism.

## 4. Fixed-first-coordinate repairs are triangular

For the predecessor chart, retain `P=u` and ask for a polynomial `Q(u,s)` with
constant Jacobian `k`. Since

```text
J(P,Q)=partial_s Q,
```

one must have

```text
Q=k s+H(u).
```

This is triangular and has degree one. It cannot preserve the cubic cover or the
no-unit phenomenon. The symbolic control is in `verify_countermodel_ladder.py`.

This does not classify all deformations of both target coordinates; the stronger
stage-5 obstruction comes from Orevkov and does not depend on that restricted
deformation audit.

## 5. Exact-symplectic near-models do not save no-unit behavior

One can write rational constant-Jacobian cubic parametrizations, for example

```text
P=x^3,
Q=y/(3x^2),
```

on `x != 0`. They display the local symplectic mechanism, but `Q` is not a
polynomial on the full source affine plane. Moreover, the cubic algebra is
monogenic in the obvious coordinate and therefore does not preserve the
no-unit-value obstruction.

This shows why satisfying an isolated differential identity is weaker than
satisfying the actual polynomial-source and boundary-support conditions.

## 6. Cubic rare-property model used only as a literature audit

A separate exact model exposes an unsupported field-theoretic shortcut in a
2024 prime-degree preprint. Let

```text
L=C(s,v),
R=C(s^3,v),
x=s+v,
y=s+2v.
```

Then `L=C(x,y)` because

```text
s=2x-y,
v=y-x,
```

and `[L:R]=3`. For every `(i,j)!=(0,0)`, the monomial

```text
x^i y^j=(s+v)^i(s+2v)^j
```

is not fixed by `s -> zeta s` for a primitive cube root `zeta`. Indeed, after
setting `t=s/v`, invariance would make the root multiset of

```text
(t+1)^i(t+2)^j
```

stable under multiplication by `zeta^{-1}`. Every nonzero orbit has length
three, whereas the multiset is supported only at `-1` and `-2`, which are not in
the same cube-root orbit. Hence every nonconstant monomial lies outside `R` and,
because the extension degree is prime, generates `L` over `R`.

Thus the “rare property” does not force extension degree two.

In polynomial coordinates the base map is

```text
u=(2x-y)^3,
v_0=y-x,
J(u,v_0)=3(2x-y)^2.
```

It is a normal connected finite-free cubic polynomial cover of `A2` by `A2`, but
it ramifies on the source line `2x-y=0`. It is globally monogenic and is **not**
a no-unit countermodel. Its sole purpose here is to audit the broader literature
claim; see `LITERATURE_AUDIT.md`.

## 7. Ladder conclusion

The exact dividing line is:

```text
rank-three finite/rational/open-A2/no-unit algebra: possible;
rank-three polynomial source étale on that A2: impossible.
```

Therefore no Keller-near no-unit model can survive “all but one” condition beyond
source étaleness. The named missing condition in the integrated countermodel is
precisely the Keller source condition, and at degree three that condition is
already terminal by Orevkov.
