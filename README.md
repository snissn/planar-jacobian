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
5. Read the moving-index disposition in [`research/tracks/monogenicity-index-divisor.md`](research/tracks/monogenicity-index-divisor.md) and its complete [issue #3 packet](research/issues/issue-3-unramified-index/README.md).
6. Pick up the bounded filtered task in [`research/leaf-packets/defect-4-staircase.md`](research/leaf-packets/defect-4-staircase.md), or the Keller-specific index successor in [`research/leaf-packets/unramified-index-elimination.md`](research/leaf-packets/unramified-index-elimination.md).
7. Follow [`AGENTS.md`](AGENTS.md) and [`governance/SCIENTIFIC-WORKFLOW.md`](governance/SCIENTIFIC-WORKFLOW.md) before changing claim status.

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

## Current load-bearing questions

### Filtered-equivariance lane

Exact `G_m`-equivariance is known to force a planar Keller map to be an automorphism. The current lane studies a weighted Rees deformation of an arbitrary Keller pair. Candidate calculations eliminate grading defects through `3`; defect `4` is the first level containing a genuinely new middle Wronskian term.

> Can the defect-4 middle Wronskian be absorbed by a filtration-compatible source or target transformation, or shown to force a forbidden boundary/monodromy configuration?

### Moving-index lane

Issue #3 proves at candidate scope that ramified height-one generation can be patched and that full codimension-one generation globalizes. It also gives smooth rational countermodels to every purely algebraic genericity argument for eliminating the remaining collision divisor.

> Can etaleness on the specified open Keller source force the universal index form to represent a nonzero constant?

Neither open bridge is claimed proved.

## Sources

See [`research/SOURCES.md`](research/SOURCES.md), including T. Shaska, *Graded Keller maps and the Jacobian Conjecture*, arXiv:2607.20210. Issue #3's source audit is [`research/issues/issue-3-unramified-index/SOURCE-AUDIT.md`](research/issues/issue-3-unramified-index/SOURCE-AUDIT.md).