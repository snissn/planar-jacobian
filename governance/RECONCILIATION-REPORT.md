# Canonical Mainline Consolidation Report

## Source revisions

| Role | Revision | Use |
|---|---|---|
| live main at start | `e542948a6d645569518437c6c0634a059415cfc4` | sole history parent for the integration branch |
| rich tree source | `588d662f7289fe3ffcee76d26b730e95be5ba537` | proof graph, ledgers, tracks, archive, validators, CI, and governance bytes only |
| issue #3 packet | current-main tree at `e542948a6d645569518437c6c0634a059415cfc4` | moving-index theorem, countermodels, handoff, provenance, and symbolic validator |
| issue #4 packet | `265a7867687ce20377e3978e8f80c5cb4d187caf` | stable-order owned files only |
| issue #5 packet | `bbd125907b05538e33202ef706b404bb3ed9fcd5` | radial/principal-part owned files only |
| reviewed defect-four candidate | `96fc7ec34bd3b685a0edeae7ecd4404abab7e2f1` | exact proof/audit/validator files covered by independent review |

## Mechanism

The integration branch was created from the latest live `main`. A new Git tree was assembled by reusing selected source blob identities and manually rewriting shared governance, claim, graph, queue, and navigation files. Source branch commits were not added as parents. No force push, published-history rewrite, or wholesale historical merge was used.

Immediately before final integration, `main` must be resolved again. If it has moved, the final tree is rebuilt on a fresh branch from the new head rather than merging divergent history.

## Preserved content

The canonical tree preserves the rich proof graph and machine graph, prose and JSON ledgers, work queue and issue index, all maintained tracks and leaf packets, validators and frontier renderer, GitHub Actions, source inventory, corrections/retractions, synthesis, metadata-only archive declarations, independent defect-four review, the complete issue #3 packet and validator, and the issue #4/#5 owned packets.

## Scientific synchronization

- Issue #3’s generic unramified-index leaf is disposed by a scoped countermodel and narrowed to the Keller-specific `L14` successor.
- Issue #4 records a conditional stable-order implication and ramified-DVR obstruction. Construction remains open and non-authoritative.
- Issue #5 records logarithmic tangency and integration obstructions. The actual Keller branch is not proved radial, and the scientific leaf remains open.
- The defect-at-most-four theorem is synchronized as `reviewed_scoped` only at the exact independently accepted positive-weight scope. No defect-five or `JC_2` status is inferred.

## Historical transport surfaces

PRs #15 and #24 are superseded rich-baseline transports. PRs #25 and #26 are superseded after their issue-owned files are verified on canonical `main`. Their branch names and revisions remain provenance, not operating baselines. The exact final main SHA and closure comments are recorded on issue #2 and the affected PRs after integration.
