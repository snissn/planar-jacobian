# Path-by-Path Conflict-Resolution Log

No shared file was resolved with a blanket “ours” or “theirs” choice.

## Seven shared-file conflicts

| Path | Rich-baseline material retained | Current-main decision retained | Resolution |
|---|---|---|---|
| `README.md` | full proof-graph/archive/track/leaf orientation and validation entry points | adapter-first review rules and revision binding | manually rewritten around the canonical authority hierarchy; stale active PR #15, issue #1, and issue #20 language removed |
| `STATUS.md` | rich counts, frontier, archive warning, and nonclaim boundary | current review/coordination state | replaced by a generated view of claim, graph, queue, and archive JSON; proposal-only defect-four delta is explicitly unapplied |
| `AGENTS.md` | resume order, leaf contract, handoff, CI limits | adapter preference, local-review fallback, material-change re-review rule | manually consolidated and linked to the parallel-agent policy |
| `AGENT_PROMPT.md` | complete research read order and scientific safeguards | current review and adapter rules | replaced with a reusable issue-scoped prompt; the old issue-1 branch and PR #15-as-active instructions were removed |
| `governance/SCIENTIFIC-WORKFLOW.md` | upstream adoption, CI fallback, synchronization/freeze context | current-main repository overrides | current-main rules made authoritative and rich validation/handoff requirements incorporated |
| `research/CLAIM_LEDGER.md` | complete 51-claim fine taxonomy | every sparse-main claim and coarse status | canonical prose is generated from the unchanged rich JSON ledger; sparse-main claims are preserved in a separate historical migration ledger |
| `research/PROGRAM.md` | full multi-track proof program and cross-track interfaces | sparse-main notation and filtered-lane orientation | manually merged without changing any claim status or mathematical conclusion |

## Current-main-only paths

| Path(s) | Resolution |
|---|---|
| `governance/reviews/issue-17-defect4-independent-*.md` | retained byte-for-byte as accepted-review evidence and proposal-only delta documentation |
| `scripts/review_validate_defect4_independent.py` | retained byte-for-byte as reviewer-owned scientific regression; not treated as the repository structural validator |
| `research/SOURCES.md` | retained as a compatibility pointer after useful citations were merged into `SOURCE_INVENTORY.md` |
| `research/tracks/filtered-equivariance.md` | retained as a compatibility pointer to canonical Track M |
| `research/leaf-packets/defect-4-staircase.md` | retained as a compatibility pointer to canonical leaf L13 |

## Rich-only paths

All rich-only archive, synthesis, governance, JSON, track, leaf, script, and CI paths were preserved. Editorial governance changes were limited to paths named in this log and newly added reconciliation/governance files.

## Machine-readable surfaces

- `research/claim_ledger.json`: claim IDs, statements, statuses, tracks, and dependencies preserved.
- `research/proof_graph.json`: all nodes, node statuses, artifacts, and edges preserved.
- `research/work_queue.json`: added from the existing prose queue; it does not change graph or claim status.
- generated prose views: regenerated from machine data and checked in CI.

## Archive conflict

`archive/manifest.json` already declared both exports `metadata_only` and was preserved. `archive/conversations/index.json` contained an inconsistent lossless-reconstruction sentence; only that provenance assertion was corrected, and matching `storage_mode` fields were added.
