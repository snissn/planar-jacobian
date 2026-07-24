# Canonical Repository Map and Resume Order

## Canonical data surfaces

| Path | Role | Edit rule |
|---|---|---|
| `research/claim_ledger.json` | claim statements, statuses, tracks, dependencies | edit explicitly; regenerate prose view |
| `research/proof_graph.json` | graph nodes, statuses, artifacts, edges | synchronize with affected claims and queue |
| `research/work_queue.json` | leaf priority, issue mirror, artifact, claim dependencies | keep one entry per open canonical leaf |
| `archive/manifest.json` | source identity and storage state | never claim embedded/reconstructible bytes without the complete source |
| `governance/reconciliation-inventory.json` | pinned July 24, 2026 reconciliation inventory | historical snapshot, not a moving branch authority |

Generated views are `STATUS.md`, `research/CLAIM_LEDGER.md`, `research/PROOF_GRAPH.md`, `research/WORK_QUEUE.md`, `research/ISSUE_INDEX.md`, and `research/LEGACY_CLAIM_MIGRATION.md`.

## Scientific artifacts

- `research/tracks/`: parallel research lanes and interfaces.
- `research/leaf-packets/L01`–`L13`: the 13 canonical bounded leaves.
- `synthesis/`: maintained conversation syntheses and the correction/retraction register.
- `research/SOURCE_INVENTORY.md`: source audit queue and bound references.
- `governance/reviews/`: review evidence; review records do not silently mutate claim status.

## Governance and engineering

- `governance/AUTHORITY-HIERARCHY.md`: resolves document conflicts.
- `governance/SCIENTIFIC-WORKFLOW.md`: repository-specific workflow mechanics.
- `governance/CLAIM-STATUS.md`: canonical claim vocabulary.
- `governance/SCIENTIFIC-STATUS-TAXONOMY.md`: separates status, review, freeze, CI, and provenance.
- `governance/REVIEW-AND-FREEZE.md`: review, synchronization, and freeze gates.
- `governance/PARALLEL-AGENT-POLICY.md`: branch and concurrency rules.
- `scripts/render_views.py`: generated prose.
- `scripts/validate_repository.py`: structural validation.
- `scripts/frontier.py`: machine-derived frontier summary.
- `.github/workflows/repository-python-validators.yml`: exact-commit CI validator.

## Provenance

- `archive/manifest.json` is authoritative for storage mode.
- `archive/conversations/index.json` is navigation only.
- historical partial conversation-A chunks are non-authoritative and incomplete.
- issue [#22](https://github.com/snissn/planar-jacobian/issues/22) remains open for unavailable complete exports.

## Resume order

1. Resolve and record the current default-branch SHA.
2. Read `STATUS.md` and this map.
3. Read the authority hierarchy and scientific workflow.
4. Select one leaf from the generated work queue.
5. Read its graph node, claim dependencies, track, corrections, and source inventory.
6. Read the governing issue for newer coordination only.
7. Create an issue-scoped branch from the pinned start and follow the parallel-agent policy.
8. Keep construction artifacts isolated; propose shared-ledger deltas separately.
9. Review the identified claim at a pinned revision.
10. Synchronize shared machine data once, regenerate views, validate locally, and run exact-SHA CI.
11. Record branch, commits, review state, validation, and remaining work in the handoff.

## Compatibility paths

The sparse-main paths `research/SOURCES.md`, `research/tracks/filtered-equivariance.md`, and `research/leaf-packets/defect-4-staircase.md` are retained only as compatibility pointers to the canonical rich paths. They are not duplicate scientific surfaces.
