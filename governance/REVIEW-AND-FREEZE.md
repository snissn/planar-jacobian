# Review and Freeze Protocol

## Construction

1. Construct bounded scientific work on an issue-scoped branch from a pinned revision.
2. Keep issue-specific artifacts separate from shared ledgers and proof graphs.
3. Commit coherent mutable work as durable provenance without implying promotion.
4. State exact claims, hypotheses, dependencies, transformations, computations, and forbidden stronger inferences.

## Review

A distinct human, agent, or subagent reviewer is preferred. When none is available, the constructor may perform a separate declared `local-adversarial-review`. Shared identity is not by itself a reason for `BLOCK`.

Every review must:

1. declare `independent-review` or `local-adversarial-review`;
2. identify claim IDs, statements, dependencies, files, and the pinned reviewed revision;
3. recompute the load-bearing reasoning rather than summarize it;
4. test edge cases and plausible countermodels;
5. record validation commands and their limits;
6. list unresolved risks; and
7. return a scoped `ACCEPT` or `BLOCK`.

Exact-byte manifests, aggregate hashes, and file hashes may be retained as strong provenance, but they are optional unless a claim-specific policy explicitly requires them. Review acceptance is bound to the identified claim and pinned repository revision.

## Synchronization and promotion

An accepted review is not itself a claim-ledger edit. A proposed status or graph delta must be applied explicitly in a final synchronization commit after checking the latest canonical baseline. Update the claim ledger, proof graph, queue, status views, and leaf packet together where applicable.

Material changes to the reviewed statement, hypotheses, proof step, computation, transformation, dependency, or counterexample require renewed review of the affected scope. Editorial, formatting, link, transport, and metadata-only changes do not automatically invalidate acceptance.

## Freeze

A freeze record identifies:

- the accepted claim and scope;
- the pinned revision;
- the review record and disposition;
- the paths protected from material scientific change;
- validation evidence and its limits; and
- any permitted editorial or metadata changes.

Freeze authority is separate from the canonical claim status. Integrate only the synchronized reviewed scope, preserving mutable branch provenance.

A repository validator or green GitHub Actions run is never mathematical review.
