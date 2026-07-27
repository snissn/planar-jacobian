# Countermodels and Deliberate Near-Misses

## 1. No surviving model

The exact classification has no residual coefficient ideal. Therefore this
packet does not produce a formal, support-only, polynomial, or Keller
countermodel satisfying the complete local transition equations. Every one of
the 16 raw systems saturates to the unit ideal after imposing `A B c!=0`.

The constructions below are deliberate near-misses used to identify which
condition blocks apparent survivors.

## 2. Top-only common-power model

For normal form I,

```text
P_0=A x^4,  Q_0=B x^6
```

satisfies `J(P_0,Q_0)=0` and exhibits the `{2,3}` common-power top with
`H=x^2`. By itself it is only an `S_0` model. Adding the required selected
layers `P_3=x`, `Q_3=c y` and all supported intervening layers forces the
contradiction in `S_1,S_2,S_3`.

**Failed condition:** complete defect-six Rees sequence.

## 3. Shared-axis face near-miss

At the first wall `(1,4)` in normal form I, take

```text
P^u=A x^4+v y,
Q^u=B x^6+f x^2 y,
A B v f!=0.
```

The two Jacobian exponent classes are

```text
(4Af-6Bv)x^5,
-2vf x y.
```

The second coefficient cannot vanish under `v f!=0`, even if the first is
tuned to cancel.

**Failed condition:** adjacent positive-face equation. This also demonstrates
why cancellation at one exponent vector cannot repair a different exponent
vector.

## 4. One-component axis near-misses

The `Q`-only normal-form-I wall

```text
P^u=A x^4,
Q^u=B x^6+f x^2 y
```

has Jacobian `4Af x^5`. The `P`-only wall has Jacobian `-6Bv x^5`.
Normal forms II and III similarly give `6Ac x^5` and `2Ac x`.

**Failed condition:** zero top bracket at the adjacent positive weight.

## 5. Scalar-erased pseudo-solution

Replacing `Q_b=c y` by `y` before constructing the equations may obscure the
compensating Jacobian factor. The determinant-one normalization leaves the
selected pair `(x,c y)`, and `c` participates both in early stairs and in
`S_6`. Setting `c=0` can make early equations look soluble but destroys the
chosen nonzero constant bracket and makes `S_6=1` impossible.

**Failed condition:** scalar retention and constant-bracket nonvanishing.

## 6. Deleted selected monomial

Deleting the required `c y` term eliminates the wall that exposes the low
defect. It also deletes the selected nonzero bracket used to obtain the normal
form and cannot satisfy the complete scalar equation.

**Failed condition:** actual support and `S_6=1`.

## 7. Added forbidden top monomial

Adding, for example, `x y` to `A x^4` in normal form I changes the top support.
It is not a lower-layer mutation at weight `(1,3)` unless its weighted degree is
strictly below four; here its degree is four. The common root is no longer the
exhaustively derived monomial `x^2`.

**Failed condition:** declared `{2,3}` top normal form and weighted degree.

## 8. Wrong `{2,3}` weighted degree

Changing one top degree without recomputing `rho`, `m`, and `n` can leave a
visual pair of powers while the coprime degree ratio is not `(2,3)` or `(3,2)`.
The checker deliberately mutates a top degree and confirms that the maximal
common-root convention rejects it.

**Failed condition:** exact coprime common-power degree data.

## 9. Dropped constant-bracket equation

Keeping only `S_0,...,S_5` changes a Keller staircase into a zero-Jacobian
formal system. Even though the four canonical contradictions happen earlier,
removing `S_6` invalidates the derivation of the selected nonzero bracket and is
caught as a semantic mutation.

**Failed condition:** complete Rees identity.

## 10. False origin sharing

The exhaustive arithmetic gives `H=x`, `x^2`, or `x^3` after normalization.
The shared top vertices are positive multiples of `(1,0)`, never `(0,0)`.
Relabeling this axis vertex as the origin manufactures a transition absent from
the actual Newton support.

**Failed condition:** exact exponent-vector geometry.

## 11. Partial top cancellation

For a top polynomial such as

```text
x^4+2x^2 y+y^2
```

at weight `(1,2)`, deleting only `x^4` leaves terms of the same top degree.
The actual defect has not decreased. A valid complete-top shear must cancel all
coefficients on the exposed face after collection.

**Failed condition:** actual strict descent.

## 12. Omitted zero layer

Normal form III has multiple semigroup gaps. Compressing the index sequence by
removing a zero layer changes which brackets contribute to `S_6`; it is not a
notational simplification.

**Failed condition:** literal Rees indexing.
