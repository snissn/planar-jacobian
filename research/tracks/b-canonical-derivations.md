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
