# Canonical Claim-Status Vocabulary

Claim status describes the epistemic state of one identified statement. It does not encode review identity, freeze authority, CI state, or provenance completeness.

- `verified_internal`: a maintained direct derivation has been checked from the repository definitions. The exact reviewed scope, when any, is recorded separately.
- `verified_conceptual`: a stable background distinction or organizing fact, not a new load-bearing theorem.
- `candidate_proved`: a complete proof packet is present, but the claim has not completed the repository’s required review/promotion process.
- `candidate`: a promising statement with an incomplete proof, unresolved hypotheses, or an unapplied review delta.
- `literature_bound`: intended to rest on a primary-source theorem at the exact recorded scope; source binding remains part of acceptance.
- `source_audit_required`: attribution, version, hypotheses, or numerical scope is conflicting or incomplete.
- `open_bridge`: an explicitly unproved implication whose closure would materially advance a branch.
- `speculative`: an idea, analogy, or experiment without a theorem packet.
- `retired`: false, overstrong, circular, superseded, or withdrawn; it must not support a positive dependency.

## Separate evidence and authority axes

A claim may also have:

- a review record with `ACCEPT` or `BLOCK` at a pinned revision;
- a frozen scientific artifact set;
- a mainline integration checkpoint;
- passing structural validation; or
- complete or metadata-only provenance.

Those facts are recorded separately. An accepted review does not silently edit the claim ledger. A green CI run does not make a claim `verified_internal`. A frozen artifact is not necessarily a new claim status.

## Promotion rule

A status change requires an explicit synchronized edit to the JSON claim ledger and every affected graph/queue surface. Review must identify the claim and pinned revision, recompute load-bearing steps, test countercontrols, and issue a scoped disposition. A distinct reviewer is preferred; a declared `local-adversarial-review` is permitted when necessary. Exact-byte manifests and hashes are optional provenance.

Any material change to the statement, hypotheses, proof, computation, transformation, dependency, or counterexample requires renewed review of the affected scope. Editorial, formatting, link, transport, and metadata-only changes do not automatically invalidate a review.
