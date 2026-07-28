# Finite cases and exhaustive scope

> Authority: `MUTABLE_NONAUTHORITATIVE`

The terminal theorem makes a conductor-by-conductor enumeration unnecessary
for the displayed branch. This file records precisely which finite data are
absorbed and which mutations escape.

## 1. Cases absorbed by the theorem

| datum | allowed range | disposition |
|---|---:|---|
| target branch conductor | unique: trivial | excluded |
| source ramification index over branch | every finite `e>=1` | excluded |
| residue-field degree | every finite degree | excluded |
| source pole orders `(m,n)` | every `m>0,n>=0` after symplectic swap | excluded |
| Puiseux pairs of source boundary | arbitrary finite data | excluded |
| source value semigroup | arbitrary | excluded |
| number of source boundary divisors | one or more | excluded |
| gluing at other target components | arbitrary finite data | excluded |
| generic polynomial degree of `F` | every finite degree | excluded |

The reason is uniform: none of these data alters the two facts that `C` is a
component of `S_F` and that `C` has no nonconstant polynomial `A1` curve.

## 2. Exact branch-level finite list

The smooth completion has exactly three punctures:

```text
0, 1, infinity.
```

The relevant target functions have no other poles. The finite branch-level
checks are therefore:

1. invert `Q`;
2. invert `Q-1`;
3. identify the affine normalization;
4. descend `R`;
5. inspect the three puncture divisors;
6. apply polynomial uniruledness componentwise.

No hidden singular target gluing remains.

## 3. Mutations that do not escape

- Removing one puncture leaves `G_m`, still without nonconstant maps from
  `A1`.
- Adding a second source-boundary divisor leaves `C` as a component of `S_F`.
- Changing ramification or pole orders changes only pullback multiplicities.
- Omitting the exact-symplectic primitive from the argument does not rescue a
  polynomial map; the terminal theorem is stronger. For the Keller derivation,
  however, the primitive remains part of the audited input.

## 4. Mutations that escape and why

| mutation | first failed hypothesis |
|---|---|
| fill two punctures | curve becomes `A1` and has polynomial curves |
| allow denominators in `P` or `Q` | map is rational, not polynomial |
| retain generic finiteness but drop quasi-finiteness | the finite-normalization map need not contain the source as an open subset |
| drop generic finiteness | primary-source theorem also does not apply |
| replace the branch by a polynomially parametric exact curve | `TPPR-04` fails |
| use only an all-orders formal neighborhood | no global `S_F` exists |
| identify the boundary valuation with a weight | unsupported; not used |

The bounded symbolic campaign is a regression check. Generality comes from the
unit proof and the primary-source theorem, not from a finite ansatz.
