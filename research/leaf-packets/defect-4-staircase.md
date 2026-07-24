# Leaf Packet: Defect-4 Rees Staircase

> **Authority:** `MUTABLE_NONAUTHORITATIVE`  
> **Issue:** [#1](https://github.com/snissn/planar-jacobian/issues/1)  
> **Parent track:** [`../tracks/filtered-equivariance.md`](../tracks/filtered-equivariance.md)

## Load-bearing question

For a planar Keller pair and a positive primitive weight with grading defect `kappa=4`, do the staircase equations force a filtration-compatible reduction to smaller defect?

The central obstacle is the middle Wronskian

```text
J(P_1,Q_1)
```

in

```text
J(P_0,Q_2)+J(P_1,Q_1)+J(P_2,Q_0)=0.
```

## Required first action

Adversarially audit the candidate claims `C-REES-01`, `C-STAIR-01`, `C-RESONANCE-01`, `C-TOP-RESONANCE-01`, and `C-DEFECT-LE3` in [`../CLAIM_LEDGER.md`](../CLAIM_LEDGER.md). Do not build defect `4` on an unaudited defect-2 or defect-3 reduction.

## Exact scope

Classify all formal weighted-layer systems with:

```text
J(Pcal,Qcal)=t^4,
```

up to filtration-compatible polynomial source and target automorphisms, for the three resonance positions

```text
(1,3), (2,2), (3,1).
```

The classification may assume positive primitive source weights but must not silently assume equal weights, nonzero intermediate layers, irreducible top forms, or a particular resonance position.

## Work products

A successful branch should contain:

1. exact definitions of allowed source and target transformations;
2. a complete list of resonance and missing-layer cases;
3. independently recomputed staircase equations;
4. either a reduction theorem, a formal counterexample to the reduction ansatz, or a strictly smaller blocked subcase;
5. a review note identifying every use of algebraic dependence, closed-polynomial theory, and weight arithmetic.

## Suggested technical attacks

### A. Hamiltonian normal form

Treat the middle layers as Hamiltonians for the standard symplectic form and ask whether `J(P_1,Q_1)` is a coboundary under a filtered canonical transformation.

### B. Common-factor geometry

Write dependent top layers as powers of a common closed polynomial and determine how the middle Wronskian acts on its generic fibers. Prove or disprove that nonzero curvature forces a finite list of Puiseux types.

### C. Newton polygon compatibility

Combine the staircase equations with inner-polynomial restrictions from the Newton-polygon literature. The desired result is a contradiction or a top-layer cancellation, not merely another leading-term dependence statement.

### D. Formal falsification search

Construct finite-dimensional ansätze for weighted layers and solve the staircase equations exactly. Search for systems that survive all obvious triangular reductions. Any such system is valuable even if global realizability remains open.

## Acceptance conditions

Return `ACCEPT` only for an exact, independently reviewed artifact that proves one of:

- every defect-4 system reduces to smaller defect;
- a declared resonance subclass reduces to smaller defect;
- the candidate low-defect theorem is false, with an explicit formal or polynomial counterexample;
- defect `4` reduces to a smaller, precisely stated invariant obstruction.

## Forbidden inferences

- Do not infer the full Jacobian conjecture from a formal staircase classification unless globalization is proved.
- Do not treat symbolic agreement as a theorem.
- Do not assume a common closed generator exists without naming and checking the theorem used.
- Do not assume a target cancellation lowers the defect without recomputing the weighted degrees.
- Do not use retired Euler-excess or generic-Kummer claims.

## Stop rule

Stop once the defect-4 resonance patterns have been exhaustively dispositioned at the declared formal level. Higher defects are deferred until this leaf is reviewed.
