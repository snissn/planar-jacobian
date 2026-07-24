# Agent Operating Protocol

This repository follows the pinned upstream scientific workflow together with repository-specific governance. Read [`governance/AUTHORITY-HIERARCHY.md`](governance/AUTHORITY-HIERARCHY.md) before resolving any conflict between documents.

## Resume order

1. Read [`STATUS.md`](STATUS.md) and [`governance/REPOSITORY-MAP.md`](governance/REPOSITORY-MAP.md).
2. Read [`research/PROGRAM.md`](research/PROGRAM.md).
3. Select exactly one open leaf from [`research/WORK_QUEUE.md`](research/WORK_QUEUE.md).
4. Read its canonical leaf packet, graph node, claim dependencies, track, and relevant corrections.
5. Read the governing GitHub issue for coordination changes after the pinned base.
6. Audit every load-bearing external theorem against primary sources before reuse.
7. Follow [`governance/PARALLEL-AGENT-POLICY.md`](governance/PARALLEL-AGENT-POLICY.md) before creating or updating a branch.

## Authority and status discipline

The machine-readable claim ledger, proof graph, and work queue are canonical for their respective fields. Generated Markdown views must be regenerated rather than edited directly.

Do not conflate:

- mutable research prose;
- a `literature_bound` claim;
- a theorem candidate;
- an accepted review record;
- frozen scientific content;
- engineering validation; or
- provenance-only material.

A review disposition does not by itself rewrite the claim ledger. A freeze does not change a claim’s mathematical statement. A green validator does not review mathematics.

## Review discipline

A distinct reviewer is preferred, but a declared `local-adversarial-review` is permitted when the environment cannot provide another reviewer or subagent. Shared constructor/reviewer identity is not, by itself, a reason to return `BLOCK`.

Every review must identify the claim and pinned revision, declare its mode, recompute load-bearing steps, test edge cases and countermodels, record unresolved risks, and return an explicit scoped `ACCEPT` or `BLOCK`. Exact-byte manifests and hashes are optional provenance. Material scientific changes require renewed review of the affected scope; editorial or metadata-only changes do not automatically invalidate a review.

## Repository operations

- Prefer the connected GitHub adapter whenever it supports the required operation.
- Confirm the repository, permissions, base SHA, branch head, and changed-path scope before writing.
- Use non-forced updates. Never overwrite another agent’s branch, rewrite published history, or delete source branches as a synchronization shortcut.
- Keep issue-scoped scientific work separate from final shared-ledger synchronization.
- Treat a pushed branch and pull request as development provenance, not theorem authority.

## Validation

Run:

```bash
python3 -m compileall -q scripts
python3 scripts/render_views.py --check
python3 scripts/validate_repository.py
python3 scripts/frontier.py
```

Use the repository GitHub Actions validator at the exact proposed integration SHA. Record its run ID and conclusion. These checks validate JSON, generated views, graph closure, artifact paths, leaf contracts, archive declarations, and internal Markdown paths. They do not validate mathematical truth.

## Required handoff

Record the pinned starting revision, issue and branch, unique artifact directory, claim IDs touched, exact formulas or source statements used, countercontrols tested, validation commands, review state, final synchronization commit, remaining conflict risks, and the smallest next action.

## Nonclaims

Do not describe this repository as a proof of the planar Jacobian conjecture. Do not use the three-dimensional marked-root construction as authority for a planar necessity statement. Do not infer global symmetry from multiple sheets. Do not promote a candidate merely because a review proposal, symbolic check, or CI run exists.
