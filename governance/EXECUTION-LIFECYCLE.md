# Execution Lifecycle and Role Separation

This document governs how bounded scientific and governance work moves from an idea to durable `main` without confusing transport with authority.

## Lifecycle

```text
preflight
  -> issue-owned construction
  -> pinned review
  -> integration-ready packet
  -> serialized synchronization
  -> exact-candidate validation
  -> merge
  -> exact-main verification
  -> issue and coordination handoff
```

Progress updates do not terminate the lifecycle. A continuation message resumes the current branch and pull request.

## Roles

### `research-worker`

The worker starts from latest `main`, reserves one issue-owned path, constructs or falsifies one bounded leaf, uses issue-local claim labels, records proposed shared deltas, performs the declared review mode, and leaves one non-draft integration-ready pull request. It does not edit canonical shared surfaces or claim mainline completion.

### `reviewer`

The reviewer binds review to exact claims, files, dependencies, and a pinned revision. It does not modify the candidate proof. It returns a scoped `ACCEPT` or `BLOCK`, lists unresolved risks, and identifies whether the mode is independent or local-adversarial.

### `integration-maintainer`

The integration maintainer owns canonical synchronization. It re-resolves `main`, closes stale or duplicate transport pull requests, transplants issue-owned files when necessary, allocates global IDs, reconciles shared surfaces, regenerates views, validates one packet at a time, merges, verifies exact `main`, and records completion receipts.

### `governance-maintainer`

The governance maintainer may edit process documents, templates, schemas, validators, and workflows. It does not change mathematical meaning or claim authority. Governance changes still require exact-candidate and exact-main validation.

## Stopping states

A run may end successfully only at its assigned role boundary:

- worker: one validated integration-ready PR and accurate statement that it is not yet on `main`;
- reviewer: review record bound to a pinned candidate, with no candidate modification;
- integrator: verified merge, exact-main checks, and final issue/PR states;
- governance maintainer: verified governance merge and exact-main checks.

A technical blocker is an acceptable terminal report only when it names the failed operation, returned error, current remote state, and incomplete acceptance items.
