# Agent Instructions

This repository uses the [`scientific-mainline-workflow`](https://github.com/snissn/skills/tree/main/scientific-mainline-workflow) from [`snissn/skills`](https://github.com/snissn/skills).

Before scientific work:

1. Read the upstream skill at [`scientific-mainline-workflow/SKILL.md`](https://github.com/snissn/skills/blob/main/scientific-mainline-workflow/SKILL.md).
2. Read [`STATUS.md`](STATUS.md), [`research/PROGRAM.md`](research/PROGRAM.md), and [`research/CLAIM_LEDGER.md`](research/CLAIM_LEDGER.md).
3. Work from the active issue and an issue-scoped feature branch.
4. Treat all feature-branch scientific prose as `MUTABLE_NONAUTHORITATIVE` unless an exact-byte independent review records `ACCEPT`.

## Claim discipline

Every maintained mathematical statement must have one status:

- `LITERATURE`: source-bound statement attributed to a primary source;
- `CANDIDATE`: self-contained derivation awaiting independent adversarial review;
- `CONDITIONAL`: proved only under named additional hypotheses;
- `BLOCKED`: load-bearing implication not proved;
- `RETIRED`: false, circular, or dependent on an invalid step;
- `FROZEN_ACCEPTED`: independently reviewed exact artifact integrated under the scientific workflow.

Do not upgrade a claim because symbolic experiments agree with it. Do not cite conversation prose as theorem authority. Recompute load-bearing algebra independently and record all hidden hypotheses.

## Current lane

The active technical lane is [`research/tracks/filtered-equivariance.md`](research/tracks/filtered-equivariance.md). Its load-bearing task is the defect-4 staircase packet in [`research/leaf-packets/defect-4-staircase.md`](research/leaf-packets/defect-4-staircase.md).

The preferred next artifact is an adversarial audit of the claimed `kappa_w <= 3` argument followed by a complete classification of the defect-4 resonance patterns. A valid outcome may be a theorem, a scoped obstruction, a counterexample to the candidate reduction, or a precise blocked implication.

## Commit and push policy

- Commit and push coherent non-decisive work to the issue branch.
- Keep theorem candidates visibly mutable and non-authoritative.
- Do not merge to `main` without exact-byte scientific review and the validations required by the upstream workflow.
- Do not open a PR merely as a substitute for theorem review unless repository policy or the user separately requests one.
