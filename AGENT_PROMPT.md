# Reusable Issue-Scoped Agent Prompt

Work on exactly one active leaf from [`research/WORK_QUEUE.md`](research/WORK_QUEUE.md).

## Start

1. Resolve the latest live `main` and record its full SHA.
2. Read `STATUS.md`, `governance/REPOSITORY-MAP.md`, `research/PROGRAM.md`, the selected leaf, its graph node, claim dependencies, track, issue, corrections, and source inventory.
3. Reserve a unique path under `research/issue-<number>/` or another explicitly issue-owned directory.
4. Create a short-lived branch from the recorded `main` SHA.

Do not use a pull request or historical branch as the operating baseline.

## Construct

Use issue-local labels for new claims. Keep proofs, calculations, source bindings, countermodels, mutations, review notes, and proposed shared deltas in the issue-owned path. Do not allocate global `CLM-*` IDs or edit shared ledgers, graphs, README, STATUS, or generated views during construction.

State exact hypotheses, quantifiers, dependencies, permitted inference, and forbidden stronger inference. A conditional theorem, obstruction, failed construction, or countermodel is a valid durable result.

## Review

Prefer a distinct reviewer. When none is available, run a separately declared `local-adversarial-review`. Bind the review to the pinned revision and exact scope. Recompute the load-bearing argument, test edge cases and mutations, record commands and limitations, and return `ACCEPT` or `BLOCK`.

Do not treat a pull request, merge, manifest, or green CI run as mathematical review.

## Synchronize

Immediately before integration, resolve `main` again. If it moved, create a fresh branch from the new head, transplant only owned files, and recompute every shared delta. Never merge an unrelated branch history to recover the packet.

Allocate global claim IDs only now. Reconcile the claim ledger, proof graph, work queue, issue index, README, STATUS, and generated views field by field. Preserve unrelated entries. Material changes to previously accepted scope require renewed review.

## Validate and integrate

Run structural, generated-view, JSON, dependency, artifact-path, Markdown-link, and issue-specific checks against the exact candidate. Run GitHub Actions on that SHA. When a PR is useful, make it non-draft and merge it in the same run after checks pass; otherwise use a safe non-forced direct update when repository policy permits.

After integration, verify live `main`, comment on the governing issue and issue #2 with the canonical SHA and resume order, and close only superseded transport PRs or leaves whose scientific stop rule was actually met.
