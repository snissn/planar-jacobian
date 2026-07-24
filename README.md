# Planar Jacobian Research Mainline

> **Authority:** `MUTABLE_NONAUTHORITATIVE`  
> **Engineering status:** `DEVELOPMENT`  
> **Execution validity:** `NOT_A_SCIENTIFIC_EXECUTION`  
> **Protocol verdict:** `null`  
> **Scientific inference:** `none`

This repository is a durable, dependency-tracked research workspace for the planar Jacobian conjecture. It imports two long July 2026 conversations, preserves them byte-for-byte in compressed form, separates usable lemmas from speculative bridges and withdrawn claims, and exposes the surviving work as a proof graph with agent-sized leaves.

**No file in this repository claims an unconditional proof of the planar Jacobian conjecture.** The repository is a research program and provenance archive.

## Baseline and current branch

The intended rich baseline is PR [#15](https://github.com/snissn/planar-jacobian/pull/15), branch `agent/bootstrap-proof-graph`, at commit `86d1b78cedd788b7335be692f9bb92921142c7d3`. The active issue branch is

```text
issue-17/defect-4-staircase
```

and is tracked in issue [#17](https://github.com/snissn/planar-jacobian/issues/17).

## Start here

1. [`STATUS.md`](STATUS.md) — current frontier and nonclaims.
2. [`research/PROGRAM.md`](research/PROGRAM.md) — common problem spine.
3. [`research/PROOF_GRAPH.md`](research/PROOF_GRAPH.md) and [`research/proof_graph.json`](research/proof_graph.json) — branches and dependencies.
4. [`research/WORK_QUEUE.md`](research/WORK_QUEUE.md) — prioritized leaves.
5. [`research/CLAIM_LEDGER.md`](research/CLAIM_LEDGER.md) — exact claim status.
6. [`AGENTS.md`](AGENTS.md) — how to resume work without rediscovering the history.
7. [`AGENT_PROMPT.md`](AGENT_PROMPT.md) — the current defect-4 handoff prompt.
8. [`archive/MANIFEST.md`](archive/MANIFEST.md) — lossless conversation archive.

## Repository layers

- `archive/`: original conversations, hashes, and a message-level topic index.
- `synthesis/`: narrative reconciliation and correction register.
- `research/tracks/`: parallel formal proof programs.
- `research/leaf-packets/`: bounded next tasks with stop rules and handoff contracts.
- `research/audits/`: exact derivations, case tables, source audits, and scoped candidate dispositions.
- `governance/`: status, review, source-audit, freeze, handoff, and scientific-workflow rules.
- `scripts/`: deterministic structural and symbolic validation.

## Current filtered lane

Exact nontrivial `G_m`-equivariance in dimension two is source-bound to T. Shaska, *Graded Keller maps and the Jacobian Conjecture*, arXiv:2607.20210.

Track [`m-filtered-equivariance.md`](research/tracks/m-filtered-equivariance.md) develops a weighted Rees staircase around the exact graded case. Issue #17 now contains a self-contained theorem candidate that every positive-weight Keller pair with grading defect `kappa<=4` is an automorphism. The result is `candidate_proved`, not frozen or authoritative, because an independent exact-byte review has not yet returned `ACCEPT`.

See:

- [`L13-defect-4-staircase.md`](research/leaf-packets/L13-defect-4-staircase.md);
- [`defect-4-staircase-audit.md`](research/audits/defect-4-staircase-audit.md);
- [`defect-4-case-table.md`](research/audits/defect-4-case-table.md);
- [`filtered-transformation-catalogue.md`](research/audits/filtered-transformation-catalogue.md).

This scoped candidate does not show that every Keller map has such a positive weight and does not prove `JC_2`.

## Scientific workflow

Work follows the [`scientific-mainline-workflow`](https://github.com/snissn/skills/tree/main/scientific-mainline-workflow) maintained in [`snissn/skills`](https://github.com/snissn/skills). The pinned version used for this branch is recorded in [`governance/SCIENTIFIC-WORKFLOW.md`](governance/SCIENTIFIC-WORKFLOW.md).

A pushed mutable-branch commit is development provenance, not theorem authority. Exact candidate bytes require independent scientific review before promotion.

## Validation

```bash
python3 scripts/validate_repository.py
python3 scripts/validate_defect4_staircase.py
python3 scripts/frontier.py
```

These checks validate repository structure, identifiers, graph closure, archive hashes, and exact symbolic regression identities. They do **not** by themselves validate mathematical truth.
