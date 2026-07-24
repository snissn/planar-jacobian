# Parallel-Agent Work Policy

## Branch and start state

- Use `issue-<number>/<bounded-description>` for scientific work and a dedicated `maintenance/<description>` branch for repository-only integration.
- Record the full starting commit SHA in the first artifact and issue comment.
- Never infer the start from a moving branch name after work begins.

## Artifact isolation

- Put new issue-specific work in a unique directory such as `research/issue-<number>/` or in the issue’s canonical leaf packet when the change is strictly local.
- Do not reuse another agent’s temporary directory, manifest, review path, or branch.
- Never force-push, reset, or overwrite another agent’s branch. Create a new branch when ownership or scope is ambiguous.

## Claim IDs

- Reuse an existing claim ID only when editing that exact claim’s scope under the required review rules.
- Reserve proposed new IDs in the governing issue before parallel work begins.
- Treat branch-local IDs as provisional until final synchronization against the latest canonical ledger.
- Resolve collisions manually; never renumber another agent’s published branch in place.

## Shared files and final synchronization

- During construction, avoid `research/claim_ledger.json`, `research/proof_graph.json`, `research/work_queue.json`, and their generated Markdown views.
- Record proposed deltas in issue-specific artifacts.
- After review, fetch the latest canonical baseline and make one final synchronization commit limited to shared ledgers, graph, queue, generated views, and necessary navigation metadata.
- Name the pinned pre-synchronization revision and the final synchronization commit in the handoff.

## Conflict handling

- Resolve shared-ledger and proof-graph conflicts field by field, preserving all unrelated claims, nodes, edges, and queue entries.
- Do not use blanket “ours” or “theirs” resolution on governance, ledgers, proof graphs, status files, or root orientation documents.
- When two branches allocate the same ID or edit the same dependency, stop the synchronization, compare their pinned scopes, and record the chosen migration explicitly.
- Structural validation must pass after synchronization, but CI does not replace scientific review.
