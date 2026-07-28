# Track B — Canonical Derivations, Logarithmic Tangency, and Integration

> **Status:** `MUTABLE_NONAUTHORITATIVE`

The Keller identity supplies commuting polynomial fields `D_P,D_Q` lifting target translations. Polynomial target fields lift rationally as combinations of these canonical derivations.

## Exact issue #5 disposition

At a monogenic height-one normalization `S=R[s]` with minimal polynomial `f`, the lift of a target derivation `V` satisfies

```text
V~(s) = -V_B(f)(s) / f'(s).
```

Regularity is equivalent to divisibility by the different, and globally to logarithmic tangency along every reduced ramified branch component. For the standard radial field `P∂_P+Q∂_Q`, this criterion would force every irreducible reduced ramified branch component to be a line through the origin. The Keller identities do not prove that condition.

A branch Hamiltonian gives a regular logarithmic lift, but regularity does not imply local finiteness, completeness, or algebraic integration. An equivariant terminal theorem may be used only after proving an actual algebraic action and preservation of the original source open.

## Active leaf

[`L03-radial-pole-elimination.md`](../leaf-packets/L03-radial-pole-elimination.md) remains open under the narrower goal in `CLM-057`: produce a nonzero locally finite logarithmic target field preserving the source open, or prove radial tangency directly.

The complete candidate packet is [`../issue-5/PRINCIPAL_PARTS.md`](../issue-5/PRINCIPAL_PARTS.md), with source audit and adversarial self-review in the same directory.

## Integrated one-boundary successor (2026-07-24)

[`../issues/one-boundary-logarithmic-field/README.md`](../issues/one-boundary-logarithmic-field/README.md) records `CLM-067`–`CLM-070`: freeness of the one-curve logarithmic module, Jordan-part stability, a finite-isogeny action lift, and exclusion of a `G_m`-invariant reduced branch in the unique generically ramified boundary class. All remain mutable candidates; `CLM-072` is the non-toric successor.

## Integrated Liouville successor (2026-07-27)

[`../issues/non-toric-one-boundary-closure/README.md`](../issues/non-toric-one-boundary-closure/README.md)
records `CLM-086`–`CLM-094`. Under a generically ramified
pole-supported boundary hypothesis, it proves normalized branch Liouville
exactness and excludes the Liouville-nonexact non-toric subclass at mutable
candidate scope. This does not construct a locally finite logarithmic field or
an algebraic action, so `CLM-057` is not promoted.

The active L03 handoff is now the smaller `CLM-094` polynomial-realization
bridge for the Liouville-exact survivor. No general one-boundary
classification, source-open action, or terminal equivariant implication is
claimed.
