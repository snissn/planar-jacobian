# Review and Freeze Protocol

## Review record

Every review must identify its mode, pinned revision, claim statements, dependencies, files, computations, transformations, countercontrols, unresolved risks, and scoped `ACCEPT` or `BLOCK`.

A distinct reviewer is preferred. A declared `local-adversarial-review` is allowed when no distinct reviewer is available, but it does not become independent by naming. Exact-byte manifests are optional unless the applicable claim policy requires them.

## Synchronization

An `ACCEPT` does not silently edit the ledger. A final synchronization against the latest `main` must apply the exact claim/graph/queue delta, regenerate views, and record the reviewed revision and review path.

`reviewed_scoped` is permitted only when:

1. the exact statement and dependencies are covered by an applicable `ACCEPT`;
2. the reviewed revision is identified;
3. a freeze/synchronization record names the protected scientific paths and permitted editorial changes; and
4. the final machine ledgers apply no broader inference.

## Freeze

A freeze record identifies the accepted scope, reviewed revision, review record, protected paths, validation evidence and limits, forbidden stronger inference, and changes considered editorial or transport-only.

Material changes to the statement, hypotheses, proof step, computation, transformation, dependency, or counterexample require renewed review. Editorial, formatting, link, transport, and metadata-only changes do not automatically invalidate acceptance.

Freeze authority is separate from mainline location and from CI. A validator or green Actions run is never mathematical review.
