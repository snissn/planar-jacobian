# Primary-source literature audit

> Authority: `MUTABLE_NONAUTHORITATIVE`  
> Label: `TPPR-03`

## Load-bearing source

Zbigniew Jelonek and Michał Lasoń, **Quantitative properties of the
non-properness set of a polynomial map**, *manuscripta mathematica* **156**
(2018), 383--397, DOI `10.1007/s00229-017-0965-0`; preprint
`arXiv:1411.5011`.

The journal article is open access. The preprint and journal abstract state the
same complex theorem used here.

## Exact items bound

### Definition 1.1

For a generically finite polynomial map `f:X->Y`, the source defines `S_f` as
the set of target points having no open neighborhood over which `f` is finite
(proper). This is exactly the definition used in
`SOURCE_COMPACTIFICATION.md`.

### Definition 2.1

An irreducible affine curve is parametric of degree at most `d` when it is the
image of a **nonconstant polynomial map** from the affine line of degree at
most `d`.

This is stronger and more relevant here than merely having a rational
parametrization from `P1`.

### Proposition 2.2 and Definition 2.3

The uniruledness condition is componentwise. For every point of each
irreducible component, a bounded-degree parametric curve passes through that
point. The proof may equivalently use a nonempty open set, but the stated
equivalence supplies every point.

### Theorem 3.2

If

```text
f:C^n->C^m
```

is a generically finite polynomial map of algebraic degree `d`, then `S_f` has
degree of `C`-uniruledness at most `d-1`.

## Hypothesis binding

| primary-source hypothesis | packet verification |
|---|---|
| base field `C` | source and target are complex affine planes |
| source `C^n` | `n=2`, actual source `A2_(x,y)` |
| target `C^m` | `m=2`, target `A2_(P,Q)` |
| polynomial coordinate map | exactly the `L4` hypothesis |
| generically finite | assumed in theorem; automatic for a Keller pair |
| finite algebraic degree `d` | every polynomial map has finite degree |
| componentwise conclusion | Definition 2.3 |
| nonconstant polynomial `A1` curves | Definition 2.1 |

No part of the proof uses the real theorem, positive-characteristic
generalization, an asymptotic sequence as a substitute for algebraic
nonproperness, or projective rational uniruledness.

## Cross-checks, not additional dependencies

- Proposition 3.1 gives the familiar sequence characterization over `C`.
- The 2019 positive-characteristic sequel explicitly describes the 2018 result
  as coverage of `S_f` by polynomial curves of degree at most `d-1`.
- Jelonek's earlier nonproperness work gives hypersurface/uniruledness results,
  but the 2018 theorem is retained because its definition is explicitly
  polynomial and componentwise.

## Theorems deliberately not invoked

This packet does not invoke Abhyankar--Moh, one-place-at-infinity
classification, semigroup classification, valuation-tree theorems, or
simultaneous monomialization. Their hypotheses therefore require no hidden
binding here.
