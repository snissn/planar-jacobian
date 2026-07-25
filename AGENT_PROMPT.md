# Reusable Issue-Scoped Agent Prompt

Use this as the common execution envelope around a bounded scientific or governance task.

## Role and start

Declare exactly one role: `research-worker`, `reviewer`, `integration-maintainer`, or `governance-maintainer`.

1. Resolve the latest live `main` and record its full SHA.
2. Read `STATUS.md`, `governance/REPOSITORY-MAP.md`, `governance/EXECUTION-LIFECYCLE.md`, `research/PROGRAM.md`, the selected leaf, its graph node, claim dependencies, track, issue, corrections, and source inventory.
3. Search for an existing branch and open pull request for the same issue and owned path. Resume it when present.
4. Reserve a unique path under `research/issues/<slug>/` or another explicitly issue-owned directory.
5. Create or update `INTEGRATION.json` in the owned packet.
6. Create a short-lived branch from the recorded `main` SHA only when no active vehicle exists.

Do not use a pull request or historical branch as the operating baseline.

## Construction

A `research-worker` uses issue-local labels for new claims. Keep proofs, calculations, source bindings, countermodels, mutations, review notes, and proposed shared deltas in the issue-owned path. Do not allocate global `CLM-*` IDs or edit shared ledgers, graphs, queues, issue indexes, README, STATUS, or generated views.

State exact hypotheses, quantifiers, dependencies, permitted inference, forbidden stronger inference, and the smallest surviving action. A conditional theorem, obstruction, failed construction, or countermodel is a valid durable result.

## Review

Prefer a distinct reviewer. When none is available, run a separately declared `local-adversarial-review`. Bind the review to the pinned revision and exact scope. Recompute the load-bearing argument, test edge cases and mutations, record commands and limitations, and return `ACCEPT` or `BLOCK`.

A reviewer does not edit the candidate proof and does not silently allocate global IDs.

## Parallel-batch boundary

Parallel workers own only issue paths. One serialized `integration-maintainer` allocates global IDs, updates shared surfaces, validates, merges, and runs the final postflight. Do not race another worker for the ledger or proof graph.

## Synchronization

Immediately before integration, resolve `main` again. If it moved, create a fresh branch from the new head, transplant only owned files, and recompute every shared delta. Never merge unrelated branch history to recover the packet.

The integration maintainer allocates global IDs only at this stage and reconciles the claim ledger, proof graph, work queue, issue index, README, STATUS, and generated views field by field. Preserve unrelated entries. Material changes to previously accepted scope require renewed review.

## Validation and transport

Run structural, generated-view, integration-contract, JSON, dependency, artifact-path, Markdown-link, workflow-policy, and issue-specific checks against the exact candidate. Run GitHub Actions on that SHA.

A worker creates at most one non-draft integration-ready pull request. The integration maintainer closes stale predecessors before replacements, merges one packet at a time, and verifies exact `main` after every merge.

## Remote completion

Use the receipt in `governance/REMOTE-COMPLETION.md`. Do not report `merged`, `closed`, `on main`, `verified`, or `green` without adapter evidence obtained in the same execution. A local file, branch workflow, prospective merge SHA, or mergeable pull request is not mainline completion.

After integration, verify live `main`, refetch critical files, verify exact-main Actions, comment on the governing issue and issue #2, and close only superseded transport pull requests or leaves whose scientific stop rule was actually met.

## Mandatory footer

Continue executing after progress updates until the task’s acceptance gate is met.
On a continuation message, resume the existing branch and PR.
Do not create a duplicate PR.
Do not claim a remote state without adapter evidence obtained in the same turn.
A local file, branch workflow, prospective merge SHA, or mergeable PR is not mainline completion.
