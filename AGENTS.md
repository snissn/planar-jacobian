# Agent Operating Protocol

Read [`governance/AUTHORITY-HIERARCHY.md`](governance/AUTHORITY-HIERARCHY.md) before resolving any conflict between documents. The latest `main` is the durable integration surface; branch age, pull-request state, merge status, manifests, and CI carry no scientific authority.

## Select one role before acting

Every run declares exactly one role in its issue packet and pull request:

- `research-worker` — constructs or falsifies one bounded scientific leaf in one issue-owned path;
- `reviewer` — reviews a pinned candidate without editing the reviewed proof;
- `integration-maintainer` — serializes completed packets onto current `main` and owns shared ledgers and generated views;
- `governance-maintainer` — changes process, validation, templates, or repository structure without changing mathematics.

The lifecycle and role boundaries are defined in [`governance/EXECUTION-LIFECYCLE.md`](governance/EXECUTION-LIFECYCLE.md). Parallel batches follow [`governance/PARALLEL-BATCH-WORKFLOW.md`](governance/PARALLEL-BATCH-WORKFLOW.md).

## Resume order

1. Resolve and record the latest `main` SHA.
2. Read [`STATUS.md`](STATUS.md), [`governance/REPOSITORY-MAP.md`](governance/REPOSITORY-MAP.md), and [`research/PROGRAM.md`](research/PROGRAM.md).
3. Select one active leaf from [`research/WORK_QUEUE.md`](research/WORK_QUEUE.md) and read its issue, track, dependencies, corrections, and source bindings.
4. Search for an existing branch or open pull request for the same issue and owned path. A repeated prompt or continuation message resumes that vehicle; it does not start another one.
5. Reserve a unique issue-owned path and create or update its `INTEGRATION.json` manifest.
6. Audit every load-bearing external theorem against a primary source before reuse.

## Research-worker contract

A research worker:

- starts from current `main` and records the full SHA;
- owns exactly one issue-specific path;
- uses issue-local claim labels during construction;
- does not edit global claim ledgers, proof graphs, queues, issue indexes, README, STATUS, or generated views;
- records proposed shared deltas in the issue packet;
- performs the declared review mode;
- leaves one coherent non-draft integration-ready pull request, unless the run is explicitly assigned integration authority;
- never reports that work is on `main` before remote verification.

## Review contract

A review declares `independent-review` or `local-adversarial-review`; identifies claims, files, dependencies, and the pinned reviewed revision; recomputes load-bearing steps; tests mutations and edge cases; records commands and limits; lists unresolved risks; and returns a scoped `ACCEPT` or `BLOCK`.

A reviewer must not modify the candidate proof while reviewing it. Shared constructor/reviewer identity is permitted only as `local-adversarial-review` and must not be described as independent.

## Integration-maintainer contract

Only the integration maintainer allocates final global IDs and changes shared scientific surfaces for a parallel batch. Immediately before every integration it re-resolves `main`; if `main` moved, it creates a fresh branch, transplants only issue-owned files, and recomputes shared deltas. It closes stale or duplicate pull requests before opening replacements, merges one validated packet at a time, and runs an exact-main postflight after the batch.

## Mainline integration policy

1. Start from current `main`; never use a historical pull request or branch as the operating baseline.
2. Reserve one owned path per task.
3. Use issue-local labels during construction; allocate global IDs only during serialized integration.
4. Defer shared surfaces to the integration maintainer.
5. Re-resolve `main` immediately before synchronization.
6. Never import unrelated branch history to recover a packet.
7. Integrate coherent speculative, conditional, blocked, falsification, and countermodel work promptly with explicit status.
8. Keep pull requests short-lived, non-draft, bounded, and unique per issue-owned path.
9. Treat merge as transport and preservation, not scientific acceptance.
10. Treat exact-byte manifests as optional provenance unless a claim-specific review requires them.
11. Permit a declared local adversarial review when no distinct reviewer is available.
12. Renew review for material scientific changes; editorial and transport-only changes do not automatically invalidate acceptance.

## Continuation and duplicate-PR rules

- A progress update is not a stopping point.
- A repeated user instruction means continue the existing task.
- Before creating a branch or pull request, search for an existing vehicle for the same issue and owned path.
- At most one open pull request may own a given issue path.
- A replacement pull request may be created only after its predecessor is closed as superseded and linked to the replacement.
- A prospective merge SHA, a mergeable pull request, branch CI, local file, or workflow artifact is not mainline completion.

## Temporary-artifact rules

Final integration must comply with [`governance/TEMPORARY-ARTIFACT-POLICY.md`](governance/TEMPORARY-ARTIFACT-POLICY.md). In particular, do not merge base64 transport chunks, workspace-export workflows, readiness marker files, one-shot synchronization workflows, self-modifying Actions, root validation logs, or branch-only synchronization scripts.

## Remote completion gate

Before reporting success, follow [`governance/REMOTE-COMPLETION.md`](governance/REMOTE-COMPLETION.md) and record a completion receipt. When a pull request is used, the same execution must obtain evidence that:

1. the pull request reports `merged=true`;
2. live `main` contains the intended revision;
3. critical files were refetched from live `main`;
4. exact-main validation passed;
5. the governing issue and superseded pull requests have the reported final states.

If a write fails, report the exact adapter action, returned error, current branch and pull request, and remaining acceptance items. Never replace a blocker with a success claim.

## Status discipline

Do not conflate mutable research prose, a `literature_bound` statement, `candidate` or `candidate_proved` work, a `reviewed_scoped` claim, a review disposition, a freeze record, passing CI, merge status, or provenance completeness.

The JSON claim ledger, proof graph, and work queue are canonical. Generated views must be regenerated. A validator does not evaluate mathematical truth.

## Required validation and handoff

Run all issue-specific regression checks named by the packet plus:

```bash
python3 -m compileall -q scripts research/issues
python3 scripts/render_views.py --check
python3 scripts/validate_repository.py
python3 scripts/validate_integration_contract.py
python3 -m unittest discover -s scripts/tests -p 'test_*.py'
python3 scripts/frontier.py
```

Record the exact candidate SHA, review mode and revision, Actions run, logs, scientific nonclaims, surviving leaf, pull-request state, merge SHA, final `main` SHA, and issue state. Update issue #2 after verified mainline integration.
