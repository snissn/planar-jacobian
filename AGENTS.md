# Agent Operating Protocol

Read [`governance/AUTHORITY-HIERARCHY.md`](governance/AUTHORITY-HIERARCHY.md) before resolving any conflict between documents. The latest `main` is the durable integration surface; branch age or pull-request state carries no scientific authority.

## Resume order

1. Resolve and record the latest `main` SHA.
2. Read [`STATUS.md`](STATUS.md), [`governance/REPOSITORY-MAP.md`](governance/REPOSITORY-MAP.md), and [`research/PROGRAM.md`](research/PROGRAM.md).
3. Select one active leaf from [`research/WORK_QUEUE.md`](research/WORK_QUEUE.md) and read its issue, track, dependencies, corrections, and source bindings.
4. Reserve a unique issue-specific artifact path before construction.
5. Audit every load-bearing external theorem against a primary source before reuse.

## Mainline integration policy

1. **Start from current `main`.** Never start a new task from a pull request or another historical baseline.
2. **Reserve one owned path.** Every task uses a unique issue-specific artifact directory or explicitly owned leaf file.
3. **Use local labels during construction.** Issue packets use issue-local claim labels. Global `CLM-*` IDs are allocated only during final synchronization against the then-current ledger.
4. **Defer shared surfaces.** Do not edit README, STATUS, shared ledgers, proof graphs, queues, or issue indexes during ordinary construction. Record proposed deltas in the issue packet.
5. **Re-resolve before integration.** Fetch the latest `main` immediately before synchronization. If it moved, transplant only owned files and recompute shared deltas on the new head.
6. **Do not import unrelated history.** Never merge a historical or unrelated branch merely to recover a small packet; transplant the required files and reconcile shared changes field by field.
7. **Integrate coherent speculative work promptly.** Preserve `candidate`, `candidate_proved`, `open_bridge`, blocked, conditional, falsification, and countermodel work on `main` with explicit status rather than leaving it on a large branch.
8. **Keep pull requests short-lived.** When checks or a merge record justify a PR, open one small non-draft PR and merge it in the same run after required checks pass.
9. **Treat merge as transport.** Integration to `main` is preservation, not scientific acceptance, theorem promotion, or issue closure.
10. **Treat exact-byte manifests as optional provenance.** Require them only when a claim-specific review policy explicitly does so.
11. **Permit declared local adversarial review.** A `local-adversarial-review` is allowed when no distinct reviewer is available; it must not be mislabeled independent.
12. **Renew review for material changes.** Material changes to an accepted claim, proof, hypothesis, dependency, transformation, computation, or counterexample require renewed review. Editorial, formatting, link, transport, and metadata-only changes do not automatically invalidate acceptance.

## Status discipline

Do not conflate:

- mutable research prose;
- a `literature_bound` statement;
- `candidate` or `candidate_proved` work;
- a `reviewed_scoped` claim;
- a review disposition;
- a freeze record;
- passing CI; or
- provenance completeness.

The JSON claim ledger, proof graph, and work queue are canonical. Generated views must be regenerated. A review record does not silently edit the ledger, and a validator does not evaluate mathematical truth.

## Review contract

A review must declare `independent-review` or `local-adversarial-review`; identify claims, files, dependencies, and the pinned reviewed revision; recompute load-bearing steps; test mutations and edge cases; record commands and limits; list unresolved risks; and return a scoped `ACCEPT` or `BLOCK`.

A `reviewed_scoped` ledger entry additionally requires an `ACCEPT` record and freeze/synchronization record that bind the exact statement and revision. Never broaden that status by implication.

## Integration and handoff

Before integration:

```bash
python3 -m compileall -q scripts research/issues/issue-3-unramified-index
python3 scripts/render_views.py --check
python3 scripts/validate_repository.py
python3 scripts/frontier.py
```

Run all issue-specific regression checks named by the packet. Record the exact candidate SHA, Actions run, logs, scientific nonclaims, and surviving leaf in the PR or issue handoff. Update issue #2 with the canonical SHA and resume order after mainline integration.
