# Formal models and realization levels

> Authority: `MUTABLE_NONAUTHORITATIVE`  
> Primary label: `NTLC-08`

## 1. Realization ladder

Every model is tagged at the strongest level it actually reaches.

```text
L0  coefficient identities only
L1  all-orders Laurent solution in a completed two-dimensional field
L2  algebraic formal neighborhood / finite local cover
L3  conductor and puncture gluing on a finite normalization
L4  global polynomial P,Q and polynomial primitive H in C[x,y]
L5  actual Keller pair and its one-boundary normalization
```

No model below reaches `L5`. This prevents a formal survivor from being called
a Keller counterexample.

## 2. Arbitrary-index toric control

Fix integers

```text
e>1, m>0, r>=0
```

and `B in C`. In the formal field `C(z)((t))`, set

```text
P=t^e,
Q=z,
x=z t^(-m),
y=B x^r-e/(m+e) t^(m+e).                         (2.1)
```

Then direct differentiation gives

```text
dx wedge dy=e t^e dt/t wedge dz=dP wedge dQ.       (2.2)
```

Moreover

```text
H=B/(r+1) x^(r+1)-(m/e)x(y-Bx^r)                  (2.3)
```

is polynomial in the displayed source variables and satisfies

```text
P dQ+y dx=dH.                                      (2.4)
```

Thus higher principal parts survive for arbitrary `e,m`, and the unique
resonant coefficient still vanishes. The reduced target branch is `P=0`, so
the model is toric and is already outside the surviving geometric class.
Also `P,Q` are generally not polynomials in `x,y`; (2.1) is an `L1` formal
control, not a Keller map. Its purpose is to falsify any claim that the local
differential equations alone bound `e,m` or kill every higher coefficient.

## 3. Non-toric Liouville-exact near-model

Let `R(z)` be rational and put

```text
U=t^e,
Q=z,
P=U+R'(z).                                         (3.1)
```

The branch `U=0` has parametrization `(P,Q)=(R'(z),z)` and

```text
P dQ|_(U=0)=dR.
```

Use the same `x,y` as in (2.1). Since

```text
dP wedge dQ=dU wedge dz=dx wedge dy,
```

the full primitive is

```text
H_near=B/(r+1)x^(r+1)-(m/e)x(y-Bx^r)+R(z).         (3.2)
```

For

```text
R(z)=1/z+1/(z-1),
```

the branch is the smooth non-toric three-puncture curve of
`LOGARITHMIC_FIELDS.md`. Equations (3.1)-(3.2) survive to every Laurent order
for arbitrary `e,m` and have trivial curve conductor.

The exact failure is visible: `R(z)` and the target functions in (3.1) retain
rational denominators when expressed through the displayed source data. The
model reaches `L1` and the smooth-branch part of `L3`, but not `L4`. It is a
formal all-orders non-toric survivor, not an algebraized or polynomial Keller
counterexample.

## 4. Nonexact mutation killed at order zero

Replace the branch in (3.1) by

```text
g_ne=P(P-1)Q-1.
```

Its normalized `P dQ` has nonzero residues. The order-zero equation

```text
D_0=d h_0
```

has no rational solution, so the recursion stops before any higher coefficient
or conductor calculation. This mutation verifies that the Liouville test is a
genuine finite-order obstruction.

## 5. Conductor mutation

For a singular normalized branch `A_C subset Abar`, choose an exact primitive
`R in Abar`. Mutating `R` by a semigroup-gap term changes its class in
`Abar/A_C` without changing `dR` as a rational exactness statement. The class
therefore records target-primitive descent, but the present Keller derivation
does not assert that every model requires `R in A_C`. The symbolic engine
reports the class separately rather than converting it automatically into a
contradiction.

## 6. Search status

The validator searches exact and sign-mutated instances of these families. It
classifies each result as:

- `formal_consistent`;
- `conductor_obstructed_if_descent_required`;
- `liouville_obstructed`;
- `polynomial_realization_unproved`;
- or `keller_realization_unproved`.

No searched model is labeled a polynomial or Keller realization without an
explicit polynomial inverse substitution and a verified constant Jacobian.

## 7. Field-generating rational control

A stronger toric control reaches the full source function field. For arbitrary
`e>1`, set

```text
x=t^(-1),
y=-e z t^(e+1),
P=t^e=x^(-e),
Q=z=-(1/e)y x^(e+1).                               (7.1)
```

Then `C(t,z)=C(x,y)`, and as rational functions of the genuine source
coordinates,

```text
J(P,Q)=1,
P dQ+y dx=d(-x y/e).                               (7.2)
```

Thus the source field and a polynomial primitive are both present for every
ramification index. The exact missing condition is polynomiality of `P`:
`P=x^(-e)` has a denominator. This control is stronger than a bare coefficient
model but still stops below `L4`.

Replacing `P` by

```text
P=x^(-e)+R'(Q)
```

produces the non-toric exact branch `P=R'(Q)` and changes the primitive to

```text
-x y/e+R(Q).
```

For the three-puncture `R`, both `P` and the added primitive term are rational,
not polynomial. This identifies polynomial realization, rather than the formal
Jacobian or exactness equations, as the first failed Keller condition.
