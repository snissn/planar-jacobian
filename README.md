# Planar Jacobian Research Mainline

> **Authority:** `MUTABLE_NONAUTHORITATIVE`  
> **Engineering status:** `DEVELOPMENT`  
> **Execution validity:** `NOT_A_SCIENTIFIC_EXECUTION`  
> **Protocol verdict:** `null`  
> **Scientific inference:** `none`

This repository is a durable, dependency-tracked research workspace for the planar Jacobian conjecture. It imports maintained syntheses of two long July 2026 conversations, records their exact declared source identities and hashes, separates usable lemmas from speculative bridges and withdrawn claims, and exposes the surviving work as a proof graph with agent-sized leaves. The complete source-export bytes are not yet embedded in the Git tree; archive completion is tracked in issue [#22](https://github.com/snissn/planar-jacobian/issues/22).

**No file in this repository claims an unconditional proof of the planar Jacobian conjecture.** The repository is a research program and provenance archive.

## Baseline and active work

The intended rich baseline is PR [#15](https://github.com/snissn/planar-jacobian/pull/15), branch `agent/bootstrap-proof-graph`.

The active filtered-equivariance audit is issue [#17](https://github.com/snissn/planar-jacobian/issues/17), developed on `issue-17/defect-4-staircase`. Repository-validator CI engineering is tracked in issue [#20](https://github.com/snissn/planar-jacobian/issues/20).

## Start here

1. [`STATUS.md`](STATUS.md) — current frontier and nonclaims.
2. [`research/PROGRAM.md`](research/PROGRAM.md) — common problem spine.
3. [`research/PROOF_GRAPH.md`](research/PROOF_GRAPH.md) and [`research/proof_graph.json`](research/proof_graph.json) — branches and dependencies.
4. [`research/WORK_QUEUE.md`](research/WORK_QUEUE.md) — prioritized leaves.
5. [`research/CLAIM_LEDGER.md`](research/CLAIM_LEDGER.md) — exact claim status.
6. [`AGENTS.md`](AGENTS.md) — how to resume work without rediscovering the history.
7. [`AGENT_PROMPT.md`](AGENT_PROMPT.md) — the current defect-4 handoff prompt.
8. [`archive/MANIFEST.md`](archive/MANIFEST.md) — source identities and archive-completion status.

## Repository layers

- `archive/`: source identities, partial historical chunks, and a message-level topic index.
- `synthesis/`: narrative reconciliation and correction register.
- `research/tracks/`: parallel formal proof programs.
- `research/leaf-packets/`: bounded next tasks with stop rules and handoff contracts.
- `governance/`: status, review, source-audit, freeze, handoff, and scientific-workflow rules.
- `scripts/`: deterministic structural validation and frontier rendering.

## Current filtered lane

Exact nontrivial `G_m`-equivariance in dimension two is source-bound to T. Shaska, *Graded Keller maps and the Jacobian Conjecture*, arXiv:2607.20210.

Track [`m-filtered-equivariance.md`](research/tracks/m-filtered-equivariance.md) develops a weighted Rees staircase around that exact theorem. The claimed low-defect reduction through `kappa<=3` remains a candidate awaiting adversarial audit. The first blocked case is defect `4`, where a middle Wronskian appears.

See [`L13-defect-4-staircase.md`](research/leaf-packets/L13-defect-4-staircase.md).

## Scientific workflow

Work follows the [`scientific-mainline-workflow`](https://github.com/snissn/skills/tree/main/scientific-mainline-workflow) maintained in [`snissn/skills`](https://github.com/snissn/skills). The pinned version and repository-specific CI fallback are recorded in [`governance/SCIENTIFIC-WORKFLOW.md`](governance/SCIENTIFIC-WORKFLOW.md).

A pushed mutable-branch commit is development provenance, not theorem authority. Exact candidate bytes require independent scientific review before promotion.

## Validation

Preferred local commands:

```bash
python3 -m compileall -q scripts
python3 scripts/validate_repository.py
python3 scripts/frontier.py
```

If local Python execution is unavailable or blocked, push the exact commit and use [`.github/workflows/repository-python-validators.yml`](.github/workflows/repository-python-validators.yml). The workflow runs on pushes and pull requests; after it exists on the default branch it can also be dispatched with `gh workflow run`.

```bash
gh run list --workflow repository-python-validators.yml --branch "$(git branch --show-current)"
gh run watch <run-id> --exit-status
gh run view <run-id> --log-failed
```

The workflow records the tested SHA and Python version, runs compilation plus both repository validators, and retains logs. These checks validate repository structure, identifiers, graph closure, leaf references, archive storage declarations, and embedded archive hashes when complete chunks are present. They do **not** validate mathematical truth, promote a theorem candidate, or create a scientific verdict.
