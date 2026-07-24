# Planar Jacobian Research Mainline

> **Authority:** `MUTABLE_NONAUTHORITATIVE`  
> **Engineering status:** `DEVELOPMENT`  
> **Execution validity:** `NOT_A_SCIENTIFIC_EXECUTION`  
> **Protocol verdict:** `null`  
> **Scientific inference:** `none`

This repository is a durable research workspace for the two-dimensional Jacobian conjecture after the July 2026 three-dimensional counterexample. It preserves promising reductions without presenting an exploratory argument as a theorem.

The repository does **not** claim a proof of the planar conjecture. The active scientific tracker is [issue #1](https://github.com/snissn/planar-jacobian/issues/1).

## Start here

1. Read [`STATUS.md`](STATUS.md).
2. Read [`research/PROGRAM.md`](research/PROGRAM.md).
3. Inspect the claim classifications in [`research/CLAIM_LEDGER.md`](research/CLAIM_LEDGER.md).
4. Read the current technical frontier in [`research/tracks/filtered-equivariance.md`](research/tracks/filtered-equivariance.md).
5. Pick up the bounded task in [`research/leaf-packets/defect-4-staircase.md`](research/leaf-packets/defect-4-staircase.md).
6. Follow [`AGENTS.md`](AGENTS.md) before changing claim status.

## Scientific workflow

Work follows the [`scientific-mainline-workflow`](https://github.com/snissn/skills/tree/main/scientific-mainline-workflow) maintained in [`snissn/skills`](https://github.com/snissn/skills).

The governing rule is:

- construct mutable, non-decisive scientific work on an issue-scoped feature branch;
- bind review to exact candidate bytes;
- keep candidate lemmas, literature results, blocked implications, and retractions distinct;
- promote only independently reviewed frozen artifacts to `main`.

A pushed feature-branch commit is development provenance, not theorem authority.

## Current load-bearing question

Exact `G_m`-equivariance is known to force a planar Keller map to be an automorphism. The current lane studies a weighted Rees deformation of an arbitrary Keller pair. Candidate calculations eliminate grading defects through `3`; defect `4` is the first level containing a genuinely new middle Wronskian term.

> Can the defect-4 middle Wronskian be absorbed by a filtration-compatible source or target transformation, or shown to force a forbidden boundary/monodromy configuration?

No proof of that step is currently maintained.

## Sources

See [`research/SOURCES.md`](research/SOURCES.md), including T. Shaska, *Graded Keller maps and the Jacobian Conjecture*, arXiv:2607.20210.
