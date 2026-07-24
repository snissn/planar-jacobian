# Agent Operating Protocol

This repository uses the [`scientific-mainline-workflow`](https://github.com/snissn/skills/tree/main/scientific-mainline-workflow) from [`snissn/skills`](https://github.com/snissn/skills). The version used for the current synchronization is recorded in [`governance/SCIENTIFIC-WORKFLOW.md`](governance/SCIENTIFIC-WORKFLOW.md).

## Resume order

1. Read `STATUS.md` and `research/PROGRAM.md`.
2. Select exactly one open leaf from `research/WORK_QUEUE.md`.
3. Read its leaf packet and all depended-on claims.
4. Read the corresponding track and `synthesis/CORRECTIONS_AND_RETRACTIONS.md`.
5. Audit cited external theorems against primary sources before using them as blockers or conclusions.
6. For the active filtered-equivariance task, use [`AGENT_PROMPT.md`](AGENT_PROMPT.md) and issue [#17](https://github.com/snissn/planar-jacobian/issues/17).

## Scientific status discipline

Do not promote prose, a numerical experiment, a builder/auditor agreement, a formal analogy, or a literature recollection to a theorem. Every maintained statement must carry one of the statuses in `governance/CLAIM-STATUS.md`.

A useful derivation can be committed as `MUTABLE_NONAUTHORITATIVE`. A decision-bearing theorem packet may be frozen only after exact-byte review, independent mathematical audit, and explicit claim-ledger and proof-graph updates.

## Branch discipline

- The intended rich baseline is PR #15 / `agent/bootstrap-proof-graph` until that PR is integrated.
- Work on one issue-scoped branch rooted in that baseline.
- Commit and push coherent non-decisive work as durable development provenance.
- Do not use a pull request as a substitute for scientific review.
- Do not merge a theorem candidate merely because repository validators pass; they validate structure, not mathematical truth.

## Validation execution

Run the repository Python validators locally when possible:

```bash
python3 -m compileall -q scripts
python3 scripts/validate_repository.py
python3 scripts/frontier.py
```

If the local Python runtime or process environment is blocked, push the exact branch commit and use `.github/workflows/repository-python-validators.yml` as the fallback runner. Follow [`governance/SCIENTIFIC-WORKFLOW.md`](governance/SCIENTIFIC-WORKFLOW.md), bind the result to the exact tested SHA, and preserve the GitHub Actions run ID and logs.

A CI pass is process evidence only. It does not review mathematics, promote a claim, authorize freeze, or produce a scientific verdict. A checkout, runner, permission, dependency, or Actions outage is an engineering failure with no scientific inference.

## Leaf contract

Each leaf has one load-bearing question, explicit dependencies and forbidden assumptions, accepted evidence, known failed approaches, required artifacts, a stop rule, and a handoff section. Do not widen a leaf silently. Open a new node when the proof burden changes.

## Required handoff

Record exact formulas, hidden hypotheses checked, source bindings, counterexamples tested, remaining blockers, and the smallest next calculation. Update the claim ledger and proof graph together.

## Nonclaims

Do not describe this repository as a proof of the planar Jacobian conjecture. Do not use the three-dimensional marked-root construction as authority for a planar necessity statement. Do not infer global symmetry from multiple sheets. Do not treat the conversation-derived low-defect staircase argument as accepted until independent exact-byte review records `ACCEPT`.
