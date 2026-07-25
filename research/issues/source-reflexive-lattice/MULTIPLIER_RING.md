# Multiplier Ring: From a Stable Module to a Stable Order

> **Authority:** `MUTABLE_NONAUTHORITATIVE`  
> **Claim:** `SRL-008`

## 1. Definition

Let `B` be a Noetherian normal domain with fraction field `K`, let `L/K` be a
finite field extension, and let `M subset L` be a full finite `B`-lattice.
Define

\[
O_M=(M:M)=\{z\in L:zM\subset M\}.
\]

No `O`-module structure, local freeness, or multiplication on `M` is assumed.

## 2. Finiteness and generic field

Multiplication embeds `O_M` into `End_B(M)`.  Since `M` is finite over the
Noetherian ring `B`, it is finitely presented, `End_B(M)` is finite, and its
submodule `O_M` is finite.  It is a commutative `B`-subalgebra of the field
`L`, contains `B`, and is a domain.

Its total quotient field is `L`.  For any `z in L`, multiplication by `z` on
`M_K=L` has a matrix with entries in `K`.  Clearing denominators gives a
nonzero `b in B` with

\[
bzM\subset M,
\]

so `bz in O_M` and `z=(bz)/b` belongs to `Frac(O_M)`.

Thus `O_M` is a finite `B`-order in the generic sense, although it need not be
locally free.

## 3. Derivation stability

Let `D` extend a derivation of `B` and suppose `D(M) subset M`.  For
`z in O_M` and `m in M`,

\[
D(z)m=D(zm)-zD(m).
\]

Both terms on the right lie in `M`; hence

\[
D(O_M)\subset O_M.
\]

The argument applies separately to `D_P,D_Q`.  No trace or discriminant is
used here.

## 4. Reflexive closure remains an order

Set

\[
O_M^{\mathrm{ref}}=(O_M)^{**}_B.
\]

Inside `L`, normality of `B` identifies it with

\[
O_M^{\mathrm{ref}}
 =\bigcap_{\operatorname{ht}p=1}(O_M)_p.
\]

Each localization is a ring, so the intersection is a ring.  It remains
finite over `B`, contains `B`, and has total quotient field `L`.  Since
localization commutes with the extended derivation,

\[
D(O_M^{\mathrm{ref}})\subset O_M^{\mathrm{ref}}.
\]

When `B=C[P,Q]`, every finite reflexive `B`-module is locally free.  Therefore
`O_M^{ref}` is a finite locally free order stable under every derivation that
stabilizes `M`.

## 5. Consequence for the Keller route

If one finite full `B`-module `M subset L` is stable under both canonical
translations, then `O_M^{ref}` satisfies the predecessor packet's
stable-order theorem.  Its trace discriminant is stable under both base
translations, hence is the unit ideal; the order is finite etale and
connected, so

\[
[L:K]=1.
\]

This removes a former apparent gap:

> A source-derived module need not itself be multiplicatively closed.  Its
> stable reflexive multiplier ring supplies the required order.

The remaining load-bearing problem is exact stability of one finite full
module.

## 6. Divisorial modules yield no new order

Let `I` be a nonzero rank-one reflexive fractional `O`-module.  At every
height-one point `q` of the normal domain `O`,

\[
I_q=s_q^{n_q}O_q,
\qquad
(I_q:I_q)=O_q.
\]

Intersecting gives

\[
(I:I)=O.
\]

Consequently the multiplier rings of

- inverse differents and trace duals,
- canonical modules,
- divisorial source-pole modules,
- reflexive hulls of `(O:h^mO)`, and
- finite divisorial intersections

are all the normalization `O`.  The multiplier construction cannot hide
ramification in a different rank-one order; it simply returns the order whose
instability was already detected.

## 7. Trace and discriminant hypotheses

A module `M` without multiplication has no intrinsic multiplication-trace
discriminant.  Local freeness of `M` alone does not change that.  Trace
control begins only after passing to the multiplier order.

For the predecessor determinant argument, it is enough that
`O_M^{ref}` be:

1. finite locally free over `B`;
2. a commutative algebra contained in the field `L`;
3. generically the separable field `L`;
4. stable under both canonical derivations.

All four conditions follow from the construction above in the planar
characteristic-zero setting.

## 8. Limits

- If `M` is not finite, `End_B(M)` need not be finite and the bridge fails.
- If `M` is not full, the multiplier ring can have a smaller generic field.
- Reflexive closure is essential for the locally free discriminant argument;
  an arbitrary suborder may fail `S2` or flatness.
- The construction proves no existence theorem for `M`.
