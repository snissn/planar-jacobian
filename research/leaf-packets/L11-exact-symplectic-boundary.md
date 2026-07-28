# Exact Symplectic Boundary Package

- **Priority:** `P1`
- **Status:** `OPEN`
- **Dependencies:** CLM-022, CLM-023, CLM-070–CLM-072, CLM-086–CLM-094
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

## Integrated Liouville successor (2026-07-27)

The issue #5 Laurent-conductor packet normalizes a source pole to
`x=s^(-m)`, solves the full triangular recursion, and uses the order-zero
tangential primitive plus trace descent to prove

```text
P dQ=dR
```

on the normalization of the reduced target branch (`CLM-086`–`CLM-091`).
This excludes the Liouville-nonexact ramified pole-supported subclass. It does
not kill higher exact principal parts: the explicit non-toric exact control in
`CLM-093` survives all displayed formal equations but fails polynomial
realization.

The active exact-symplectic handoff is `CLM-094`: force a higher differential
or conductor obstruction from the global polynomial Keller data, or prove that
the Liouville-exact formal survivor cannot be polynomially realized. No
general one-boundary, qualifying-weight, degree-one, or planar Jacobian
conclusion is licensed.
