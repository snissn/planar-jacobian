# Rich-Baseline Reconciliation Report

> **Scope:** repository structure, maintenance, governance, and baseline integration only  
> **Scientific change:** none  
> **Claim-status promotion:** none

## Pinned source refs

The live refs were resolved before tree comparison. The task’s expected `main` SHA had advanced by one commit.

| Source | Ref | Observed SHA | Disposition |
|---|---|---|---|
| task-start expected main | `main` expectation | `d132adc131533776509075ee70829ab34aa60f53` | historical starting expectation |
| live default branch | `main` | `7dada3a5d0c6c0bf0f40208b30215c495e17ee28` | authoritative integration parent |
| rich source baseline | PR #15 / `agent/bootstrap-proof-graph` | `296867d82d09d51ef2386de2a62067408b7f949c` | rich tree and history preserved |
| defect-four candidate | `issue-17/defect-4-staircase` | `96fc7ec34bd3b685a0edeae7ecd4404abab7e2f1` | inventoried; not merged as scientific work |
| independent review branch | `review/issue-17-defect4-independent-gpt56` | `ad768dfd577fdad595e3a160ab0675401d1eb16a` | review provenance inventoried |
| replacement branch before final reconciliation | `maintenance/reconcile-rich-baseline-gpt56` | `8dad5eab3b95cd86a3484d6545e7ce2b99a336bf` | non-destructive branch parent |

The merge base of live `main` and the rich baseline was `e9f6777a92c742f12966a74b44646f46d7b119e0`. At inspection, live `main` had 14 commits not in the rich branch, while the rich branch had 85 commits not in `main`. PR #15 was open and not cleanly mergeable.

The single commit between the task-start expected main and live main added only five independent-review Markdown artifacts and one reviewer-owned validator. It did not apply the proposal-only claim/graph delta.

## Tree inventory

The exact observed branch, issue, pull-request, and workflow inventory is machine-readable in [`reconciliation-inventory.json`](reconciliation-inventory.json).

At the observation checkpoint:

- 12 branches were retained, including the default branch, rich source branch, replacement branch, four active issue/review branches, and historical merged/superseded sources;
- 15 regular issues were open: program issue #2, 13 leaf/proof issues, and provenance issue #22;
- four pull requests were open: rich source PR #15, replacement PR #24, and parallel scientific drafts #25 and #26;
- one canonical repository validator workflow and one temporary snapshot workflow were visible.

The temporary snapshot workflow was used only to materialize exact source trees and inventory. It is omitted from the canonical reconciled tree.

## Preserved rich baseline

The reconciliation preserves the rich baseline’s:

- 51-entry canonical JSON claim ledger;
- 34-node, 50-edge JSON proof graph;
- 13 canonical leaf packets;
- 14 research tracks;
- machine-readable ledgers and generated prose views;
- archive manifest, historical partial chunks, topic summaries, and extraction safeguards;
- source inventory;
- corrections/retractions register;
- three synthesis files;
- repository validators and GitHub Actions workflow; and
- handoff and source-audit governance.

The canonical claim statements, statuses, tracks, and dependencies are unchanged. The proof-graph nodes, statuses, artifacts, and edges are unchanged. Governance-only notes referring to mandatory exact-byte review were updated to the current claim-and-revision review rule without altering mathematical content.

## Retained current-main decisions

The reconciled governance preserves the current default-branch decisions that:

- the connected GitHub adapter is preferred for supported operations;
- a distinct reviewer is preferred, but `local-adversarial-review` is permitted;
- shared reviewer/constructor identity alone is not a `BLOCK` condition;
- review acceptance is bound to identified claims and a pinned revision;
- exact-byte manifests and hashes are optional provenance;
- material scientific changes require renewed review, while editorial or metadata-only changes do not automatically invalidate review; and
- structural validation and CI are not mathematical review.

Current-main independent-review artifacts and the reviewer-owned symbolic regression script are retained byte-for-byte. Their proposed scientific delta remains unapplied.

## Governance consolidation

The repository now has one explicit authority hierarchy, one canonical fine claim taxonomy, one separate scientific-status taxonomy, one review/freeze protocol, one parallel-agent policy, and machine-generated prose views.

The sparse-main coarse claim ledger is preserved in `research/legacy_claim_ledger.json` and a generated migration table. It is historical only and cannot create duplicate claim authority.

## Archive and provenance

No unavailable conversation bytes were fabricated, inferred, or reconstructed. Both declared exports remain `metadata_only`. The false lossless-reconstruction note in `archive/conversations/index.json` was corrected. Issue #22 remains the only archive-completion path, and structural validation warns accurately about unreproducible declared hashes.

## Integration method

The replacement branch is advanced only through new commits and non-forced ref updates. The final reconciliation commit uses the existing replacement branch, live `main`, and the rich baseline as explicit parents with a manually assembled resolved tree. Source branches and PR #15 remain intact.

PR #24 is the draft replacement integration path. PR #15 must remain open until maintainers can review PR #24 and confirm the safe replacement route. Parallel scientific drafts #25 and #26, and unintegrated issue-3 work, remain out of scope and should retarget only after the canonical baseline lands.

## Scientific non-delta

**No mathematical statement was rewritten, weakened, strengthened, or newly proved by this reconciliation. No canonical claim status, proof-graph status, or dependency edge was substantively changed.**
