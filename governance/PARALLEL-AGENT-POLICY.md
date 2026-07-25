# Parallel-Agent and Short-Lived Branch Policy

## Start and ownership

- Resolve the latest `main`; do not use a historical PR or branch as a baseline.
- Declare `research-worker`, `reviewer`, `integration-maintainer`, or `governance-maintainer`.
- Use `issue-<number>/<bounded-description>` for research and `maintenance/<description>` for repository integration.
- Reserve one unique issue-owned directory or file, record the starting SHA, and add `INTEGRATION.json`.
- Search for an existing branch and pull request for the same issue and path before creating another.
- Never reset, overwrite, or force-push another agent’s branch.

## Claim IDs and shared files

- Workers use issue-local labels during construction.
- Only the serialized integration maintainer allocates new global IDs.
- Workers record proposed shared deltas in the issue packet.
- Workers and reviewers do not edit shared ledgers, graphs, README, STATUS, queues, issue indexes, or generated views.

## Rebase-by-transplant

Before integration, resolve `main` again. If it moved, create a fresh branch from the new head and transplant only owned files. Recompute shared deltas and generated views. Do not merge unrelated branch history or use blanket `ours`/`theirs` resolution on scientific or governance surfaces.

## Pull-request uniqueness and continuation

- At most one open PR may own a given issue path.
- A continuation message resumes the existing PR.
- A replacement PR is opened only after the predecessor is closed as superseded and linked to the replacement.
- Draft PRs are not generic storage.
- Workers leave one non-draft integration-ready PR; the integration maintainer merges packets serially.

## Integration lifetime

Coherent speculative or blocked work should be integrated promptly with explicit status. A PR is bounded, validated, and short-lived. Direct non-forced integration is allowed when policy permits. Close obsolete transport surfaces only after useful bytes and provenance are verified on `main`.

## Collision handling

When packets propose the same global ID or shared dependency, the integration maintainer allocates final IDs in merge order. Preserve published issue-local labels in provenance; never rewrite another branch solely to remove a collision.

## Batch postflight

After all packet merges, the integration maintainer runs the complete exact-main suite, verifies no duplicate open PRs or forbidden temporary artifacts remain, and updates issue #2 with the final canonical SHA and resume order.
