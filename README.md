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
6. Follow [`AGENTS.md`](AGENTS.md) and [`governance/SCIENTIFIC-WORKFLOW.md`](governance/SCIENTIFIC-WORKFLOW.md) before changing claim status.

## Scientific workflow

Work follows the [`scientific-mainline-workflow`](https://github.com/snissn/skills/tree/main/scientific-mainline-workflow) maintained in [`snissn/skills`](https://github.com/snissn/skills), with repository-specific rules recorded in [`governance/SCIENTIFIC-WORKFLOW.md`](governance/SCIENTIFIC-WORKFLOW.md).

The governing rules are:

- construct mutable, non-decisive scientific work on an issue-scoped feature branch;
- use the connected GitHub adapter for repository operations whenever it is available and supports the action;
- bind review to identified claims at a pinned commit or repository revision;
- prefer a distinct reviewer, while permitting a declared local adversarial review when the environment does not support subagents or another reviewer;
- keep candidate lemmas, literature results, blocked implications, and retractions distinct; and
- promote only reviewed and validated artifacts to `main`.

Exact-byte manifests and artifact hashes are optional. Material scientific changes after acceptance require review of the affected scope, while editorial or metadata-only changes do not automatically invalidate a review.

A pushed feature-branch commit or pull request is development provenance, not theorem authority.

## Current load-bearing question

Exact `G_m`-equivariance is known to force a planar Keller map to be an automorphism. The current lane studies a weighted Rees deformation of an arbitrary Keller pair. Candidate calculations eliminate grading defects through `3`; defect `4` is the first level containing a genuinely new middle Wronskian term.

> Can the defect-4 middle Wronskian be absorbed by a filtration-compatible source or target transformation, or shown to force a forbidden boundary/monodromy configuration?

No proof of that step is currently maintained.

## Sources

See [`research/SOURCES.md`](research/SOURCES.md), including T. Shaska, *Graded Keller maps and the Jacobian Conjecture*, arXiv:2607.20210.
