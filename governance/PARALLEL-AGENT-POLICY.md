# Parallel-Agent and Short-Lived Branch Policy

## Start and ownership

- Resolve the latest `main`; do not use a historical PR or branch as a baseline.
- Use `issue-<number>/<bounded-description>` for research and `maintenance/<description>` for repository integration.
- Reserve one unique issue-owned directory or file and record the starting SHA.
- Never reset, overwrite, or force-push another agent’s branch.

## Claim IDs and shared files

- Use issue-local labels during construction.
- Allocate new global IDs only during final integration against the latest ledger.
- Record proposed shared deltas in the issue packet.
- Do not edit shared ledgers, graphs, README, STATUS, or generated views until final synchronization.

## Rebase-by-transplant

Before integration, resolve `main` again. If it moved, create a fresh branch from the new head and transplant only owned files. Recompute shared deltas and generated views. Do not merge unrelated branch history or use blanket `ours`/`theirs` resolution on scientific or governance surfaces.

## Integration lifetime

Coherent speculative or blocked work should be integrated promptly with explicit status. A PR, when useful, is non-draft, bounded, validated, and merged in the same run. Direct non-forced integration is allowed when policy permits. Delete or close obsolete transport surfaces only after useful bytes and provenance are verified on `main`.

## Collision handling

When two packets propose the same global ID or shared dependency, compare their pinned scopes and allocate final IDs in one synchronization commit. Preserve published issue-local labels in provenance; never rewrite another branch solely to remove a collision.
