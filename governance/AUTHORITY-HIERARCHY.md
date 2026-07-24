# Repository Authority Hierarchy

This hierarchy resolves conflicts without changing the substantive content of a scientific claim.

## 1. Upstream scientific workflow

The pinned `snissn/skills` scientific-mainline workflow supplies general construction, review, validation, and handoff practice. Its pin is recorded in [`SCIENTIFIC-WORKFLOW.md`](SCIENTIFIC-WORKFLOW.md).

## 2. Repository-specific governance

Repository-specific files govern where they explicitly refine or override the upstream defaults. In particular, this repository:

- prefers the connected GitHub adapter for supported repository operations;
- prefers a distinct reviewer but permits a declared `local-adversarial-review` when necessary;
- does not treat shared constructor/reviewer identity alone as a reason for `BLOCK`;
- binds review acceptance to identified claims at a pinned repository revision;
- treats exact-byte manifests and hashes as optional provenance rather than universal acceptance gates;
- requires renewed review for material scientific changes, not automatically for editorial or metadata-only changes; and
- treats structural validation and CI as engineering evidence, never mathematical review.

The governing repository files are:

1. this authority hierarchy;
2. [`SCIENTIFIC-WORKFLOW.md`](SCIENTIFIC-WORKFLOW.md);
3. [`CLAIM-STATUS.md`](CLAIM-STATUS.md);
4. [`SCIENTIFIC-STATUS-TAXONOMY.md`](SCIENTIFIC-STATUS-TAXONOMY.md);
5. [`REVIEW-AND-FREEZE.md`](REVIEW-AND-FREEZE.md);
6. [`SOURCE-AUDIT.md`](SOURCE-AUDIT.md); and
7. [`PARALLEL-AGENT-POLICY.md`](PARALLEL-AGENT-POLICY.md).

## 3. Canonical scientific and queue data

The following machine-readable files are authoritative for the fields they own:

| Surface | Authority |
|---|---|
| [`research/claim_ledger.json`](../research/claim_ledger.json) | claim IDs, statements, claim statuses, tracks, dependencies, and notes |
| [`research/proof_graph.json`](../research/proof_graph.json) | graph nodes, node statuses, artifacts, and dependency edges |
| [`research/work_queue.json`](../research/work_queue.json) | leaf priority, issue mirror, artifact, track, and claim dependencies |
| [`archive/manifest.json`](../archive/manifest.json) | declared archive identity and storage mode |

Generated prose views—`CLAIM_LEDGER.md`, `PROOF_GRAPH.md`, `WORK_QUEUE.md`, `ISSUE_INDEX.md`, `LEGACY_CLAIM_MIGRATION.md`, and `STATUS.md`—must match these sources exactly under `scripts/render_views.py --check`.

## 4. Research prose and artifacts

Tracks, leaf packets, synthesis files, review records, and source inventories explain and support the machine-readable surfaces. They do not silently override a claim status or graph edge. A discrepancy must be resolved by an explicit synchronized change, with renewed review when the change is scientifically material.

## 5. Issues, branches, and pull requests

GitHub metadata is a coordination and transport surface. It may identify the latest branch, review, or handoff, but it cannot promote a claim, freeze content, or replace the machine-readable ledger. Issue [#2](https://github.com/snissn/planar-jacobian/issues/2) coordinates the program; leaf issues mirror bounded packets. Closed issue #1 and its branches are historical provenance only.

## Status-taxonomy migration

The sparse mainline used a coarse vocabulary. The rich ledger uses a finer claim taxonomy. Migration is conservative:

| Legacy status | Canonical treatment | Constraint |
|---|---|---|
| `LITERATURE` | `literature_bound` | exact primary-source scope still required |
| `CANDIDATE` | `candidate` or `candidate_proved` | choose only according to the proof packet already present; migration supplies no strengthening |
| `CONDITIONAL` | an appropriate canonical status with every hypothesis retained | no automatic one-to-one conversion |
| `BLOCKED` | `open_bridge` | the missing implication remains unproved |
| `RETIRED` | `retired` | no reuse as a positive dependency |
| `FROZEN_ACCEPTED` | separate accepted-review/freeze metadata plus an appropriate canonical claim status | acceptance and authority are separate axes |

Every sparse-main claim and its original coarse status is retained in [`research/legacy_claim_ledger.json`](../research/legacy_claim_ledger.json) and the generated [`research/LEGACY_CLAIM_MIGRATION.md`](../research/LEGACY_CLAIM_MIGRATION.md). That ledger is historical and cannot be used as a second dependency surface.

## Conflict rule

When two maintained files disagree:

1. preserve the scientific statement and status from the canonical machine data;
2. apply explicit repository governance over older workflow mechanics;
3. preserve historical evidence in a clearly labeled migration, review, or provenance record;
4. update generated views from JSON rather than editing them directly; and
5. use issue/branch metadata only to locate the latest bounded work.
