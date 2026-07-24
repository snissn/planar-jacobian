# Multiplier Ring of a Full Finite Lattice

> **Authority:** `MUTABLE_NONAUTHORITATIVE`  
> **Claim:** `SRL-006`

## 1. Definition

Let `B` be a noetherian normal domain with fraction field `K`, let `L/K` be a finite field extension, and let

```text
M subset L
```

be a full finite torsion-free `B`-module:

```text
M tensor_B K = L.
```

Define its multiplier ring

```text
O_M = (M:M) = { z in L : zM subset M }.
```

This definition uses the common field `L`; it does not assume that `M` is an algebra.

## 2. Finite order theorem

### Theorem 2.1

`O_M` is a finite commutative `B`-algebra containing `B`, it is a domain, and its total quotient field is `L`.

### Proof

Multiplication gives an injective `B`-linear map

```text
O_M -> End_B(M).
```

The endomorphism module is finite over the noetherian ring `B`, so `O_M` is finite. It contains `B` because scalar multiplication preserves `M`; closure under sums, products, and negatives is immediate; and it is a domain because it is a subring of `L`.

To identify the generic field, fix `z in L` and finite generators `m_1,...,m_r` of `M`. Each `zm_i` lies in

```text
M tensor_B K.
```

One nonzero `b in B` clears all denominators, so

```text
bzM subset M.
```

Thus `bz in O_M`, and `z` lies in `Frac(O_M)`. Therefore

```text
Frac(O_M)=L.
```

So `O_M` is a finite `B`-order in the exact sense required by issue #4.

## 3. Exact derivation stability

### Theorem 3.1

Let `delta:B->B` be a derivation, let `D:L->L` be its extension, and assume

```text
D(M) subset M.
```

Then

```text
D(O_M) subset O_M.
```

### Proof

For `z in O_M` and `m in M`,

```text
D(z)m = D(zm)-zD(m).
```

Both terms on the right lie in `M`: the first by stability of `M`, the second because `D(m) in M` and `z` is a multiplier. Hence `D(z)M subset M`, so `D(z) in O_M`.

The proof applies simultaneously to `D_P,D_Q`.

## 4. Reflexivity and local freeness

A finite order need not be locally free merely because it is torsion-free. The exact surface argument is as follows.

Assume `B` is regular of dimension two and `M` is reflexive. Inside `L`,

```text
M = intersection_(ht(p)=1) M_p.
```

Therefore

```text
O_M
 = {z : zM_p subset M_p for every ht-one p}
 = intersection_(ht(p)=1) O_(M_p).
```

The finite module `O_M` is consequently reflexive. Every reflexive finite module over a regular surface is locally free. Thus `O_M` is a finite locally free order, and its trace/discriminant is defined in the exact form used by the predecessor packet.

If the original full finite stable lattice is not reflexive, replace it by

```text
M** = intersection_(ht(p)=1) M_p.
```

Derivation stability localizes, and every base localization `B_p` is preserved by a base derivation. Hence `M**` is again stable. Applying the construction to `M**` produces the required locally free stable order.

## 5. What local freeness of `M` does and does not give

Local freeness of `M` gives finite connection matrices for the derivations and embeds the multiplier ring into a locally free endomorphism algebra. It does **not** by itself give a trace-discriminant argument on `M`, because multiplication by an arbitrary element of `M` need not preserve `M`.

The trace/discriminant bridge becomes valid only after passing to the algebra `O_M` and proving that `O_M` is locally free. Once this is done, the predecessor implication applies:

```text
full finite stable lattice
  => stable locally free multiplier order
  => unit discriminant
  => finite etale
  => degree one over C.
```

This derived bridge removes any distinction between a successful finite stable module and a successful finite stable order in the present regular-surface setting.

## 6. Rank-one reflexive `O`-fractional ideals

Let `O` be a normal domain and let `I subset L` be a full rank-one reflexive `O`-module. Then

```text
(I:I)=O.
```

Indeed, at every height-one prime `q` of `O`, the DVR module `I_q` is principal, so

```text
(I_q:I_q)=O_q.
```

Intersecting all height-one localizations gives `O` by normality.

Consequences:

- for every divisorial source-pole module `O_Y(sum m_iE_i)`, the multiplier ring is `O`;
- for the inverse different, canonical fractional module, and any divisorial ideal, the multiplier ring is `O`;
- taking multiplier rings cannot turn a pole-bearing rank-one source module into a new intermediate order;
- if `O` is ramified, the multiplier ring is the same unstable normalization;
- if `O` is unramified, it is already the canonical stable order.

## 7. Relation to commensurability

Because `O_M` is finite and has generic fiber `L`, it is commensurable with both `M` and the normalization `O`. Explicitly, after clearing denominators there are nonzero `b,c in B` with

```text
bO subset O_M subset c^(-1)O.
```

This is useful for valuations but does not imply equality. Equality follows for the rank-one reflexive `O`-modules of the previous section, not for an arbitrary `B`-lattice.

## 8. Exact boundary of the theorem

The theorem requires:

- a finite full lattice inside `L`;
- exact derivation stability, not stability up to a larger stage;
- reflexive hull or an equivalent codimension-one saturation to obtain local freeness of the order;
- the regular two-dimensional base for the reflexive-implies-locally-free step.

It does not apply to the infinite union `j_*O_U`, to a module lacking a common lower valuation bound, or to a logarithmic lattice stable only under `hD` rather than `D`.
