# Agent Instructions

This repository uses the [`scientific-mainline-workflow`](https://github.com/snissn/skills/tree/main/scientific-mainline-workflow) from [`snissn/skills`](https://github.com/snissn/skills), with repository-specific review and tool rules in [`governance/SCIENTIFIC-WORKFLOW.md`](governance/SCIENTIFIC-WORKFLOW.md).

Before scientific work:

1. Read the upstream skill at [`scientific-mainline-workflow/SKILL.md`](https://github.com/snissn/skills/blob/main/scientific-mainline-workflow/SKILL.md).
2. Read [`governance/SCIENTIFIC-WORKFLOW.md`](governance/SCIENTIFIC-WORKFLOW.md) and the upstream scientific review checklist.
3. Read [`STATUS.md`](STATUS.md), [`research/PROGRAM.md`](research/PROGRAM.md), and [`research/CLAIM_LEDGER.md`](research/CLAIM_LEDGER.md).
4. Use the connected GitHub adapter for repository operations whenever it is available and supports the required action.
5. Work from the active issue and an issue-scoped feature branch.
6. Treat feature-branch scientific prose as `MUTABLE_NONAUTHORITATIVE` unless a documented review records `ACCEPT` for the claim at a pinned repository revision.

## Claim discipline

Every maintained mathematical statement must have one status:

- `LITERATURE`: source-bound statement attributed to a primary source;
- `CANDIDATE`: self-contained derivation awaiting documented adversarial review;
- `CONDITIONAL`: proved only under named additional hypotheses;
- `BLOCKED`: load-bearing implication not proved;
- `RETIRED`: false, circular, or dependent on an invalid step;
- `FROZEN_ACCEPTED`: reviewed scientific content accepted at a pinned revision and integrated under the scientific workflow.

Do not upgrade a claim because symbolic experiments agree with it. Do not cite conversation prose as theorem authority. Recompute load-bearing algebra independently and record all hidden hypotheses.

## Review discipline

A distinct human reviewer, agent, or subagent is preferred when available, but it is not mandatory. If the environment cannot provide a distinct reviewer or does not support subagents, the constructing assistant may perform a separate local adversarial review pass.

Do not return `BLOCK` solely because the same assistant performed construction and review. A local review must declare `local-adversarial-review`, identify the reviewed claim and pinned commit or revision, recompute the load-bearing steps, test edge cases and countermodels, record validations and unresolved risks, and return an explicit `ACCEPT` or `BLOCK` for the stated scope.

Exact-byte manifests and artifact hashes are optional. Any material change to an accepted statement, proof, computation, transformation, dependency, or counterexample requires review of the affected scope; purely editorial or metadata changes do not automatically invalidate acceptance.

## Repository operations

- Prefer the connected GitHub adapter for reads and writes, branch creation, commits, issues, pull requests, and review metadata.
- Fall back to local `git`, `gh`, or another repository mechanism only when the adapter is unavailable or does not support the operation.
- Record the branch and resulting commit or pull request in the handoff. Repository transport does not by itself change scientific authority.

## Current lane

The active technical lane is [`research/tracks/filtered-equivariance.md`](research/tracks/filtered-equivariance.md). Its load-bearing task is the defect-4 staircase packet in [`research/leaf-packets/defect-4-staircase.md`](research/leaf-packets/defect-4-staircase.md).

The preferred next artifact is an adversarial audit of the claimed `kappa_w <= 3` argument followed by a complete classification of the defect-4 resonance patterns. A valid outcome may be a theorem, a scoped obstruction, a counterexample to the candidate reduction, or a precise blocked implication.

## Commit and push policy

- Commit and push coherent non-decisive work to the issue branch.
- Keep theorem candidates visibly mutable and non-authoritative until accepted review and promotion.
- Do not merge scientific promotion changes to `main` without a documented review at a pinned revision and the validations required by the local workflow.
- Do not use a pull request merely as a substitute for theorem review unless repository policy or the user separately requests one.
