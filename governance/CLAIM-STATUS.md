# Canonical Claim-Status Vocabulary

Claim status describes one identified statement. It is independent of branch location, pull-request state, CI, and provenance completeness.

- `reviewed_scoped`: an explicit independent or otherwise applicable `ACCEPT` is bound to the exact statement and pinned revision, and a freeze/synchronization record has applied that disposition. Authority does not extend beyond the recorded scope.
- `verified_internal`: a maintained direct derivation has been checked from repository definitions, without implying a formal independent review.
- `verified_conceptual`: a stable background distinction or organizing fact, not a new load-bearing theorem.
- `candidate_proved`: a complete proof, obstruction, countermodel, or conditional packet is present, but the required promotion review is absent or blocked.
- `candidate`: a promising statement with an incomplete proof or unresolved hypotheses.
- `literature_bound`: intended to rest on a primary-source theorem at the exact recorded scope; source binding remains part of acceptance.
- `source_audit_required`: attribution, version, hypotheses, or numerical scope is conflicting or incomplete.
- `open_bridge`: an explicitly unproved construction or implication whose closure would advance a branch.
- `speculative`: an idea, analogy, or experiment without a theorem packet.
- `retired`: false, overstrong, circular, superseded, or withdrawn; it must not support a positive dependency.

## Promotion and revision

A status change requires an explicit synchronized edit to the JSON ledger and every affected graph/queue surface. Review must identify the claim, statement, dependencies, files, and pinned revision; recompute the load-bearing reasoning; test countercontrols; and return a scoped disposition.

A distinct reviewer is preferred. A separately declared `local-adversarial-review` is permitted when no distinct reviewer is available, but it is not independent acceptance. Exact-byte manifests are optional unless a claim-specific policy requires them.

Material changes to an accepted statement, hypothesis, proof step, computation, transformation, dependency, or counterexample require renewed review. Editorial, formatting, link, transport, and metadata-only changes do not automatically invalidate acceptance.
