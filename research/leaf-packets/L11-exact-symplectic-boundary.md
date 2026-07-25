# Exact Symplectic Boundary Package

- **Priority:** `P1`
- **Status:** `OPEN`
- **Dependencies:** CLM-022, CLM-023
- **Authority:** `MUTABLE_NONAUTHORITATIVE`

## Load-bearing question

Compute and constrain the full boundary principal-part package induced by `P dQ + y dx = dH`, not only its logarithmic residues.

## Accepted evidence

A valuation-by-valuation expansion whose global compatibility contradicts a nonempty normalization boundary.

## Forbidden shortcuts

Do not conclude pole elimination from zero residues. Do not replace simultaneous boundary compatibility by a one-valuation calculation.

## Required artifacts

Local expansions, approximate-root/key-polynomial data, conductor moment conditions, singular-point corrections, and the global compatibility theorem.

## Stop rule

Stop when exactness excludes a declared boundary class or when an explicit local model demonstrates that the proposed constraint is insufficient. Bank each restricted obstruction at its exact scope.

## Handoff

Record boundary coordinates, pole orders, residues, higher coefficients, coordinate changes tested, and the first unconstrained principal part.

## Integrated one-boundary successor (2026-07-24)

The issue #5 one-boundary packet derives the first additional common-valuation equation `n a' b-m a b'=0` and shows that the leading primitive coefficient is determined rather than forced to vanish. The torus-invariant and purely unramified one-boundary subclasses are excluded at candidate scope, but `CLM-072` remains open because exactness does not eliminate higher principal parts in the non-toric class.
