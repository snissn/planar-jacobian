# Planar Jacobian Research Mainline

> **Repository authority:** `MUTABLE_NONAUTHORITATIVE` except for explicitly reviewed scopes  
> **Canonical integration surface:** latest `main`  
> **Main theorem:** open; this repository does not claim `JC_2`

This repository is the durable integration surface for a dependency-tracked research program on the planar Jacobian conjecture. Coherent proofs, conditional implications, countermodels, falsification results, blocked leaves, source audits, and speculative tracks may all be preserved on `main`. Their scientific authority is determined by the claim ledger and review records, never by branch location, pull-request state, or a successful merge.

## Canonical authority

The machine-readable surfaces are authoritative for their declared fields:

- [`research/claim_ledger.json`](research/claim_ledger.json) — claim statements, dependencies, and epistemic status;
- [`research/proof_graph.json`](research/proof_graph.json) — maintained dependency graph and leaf disposition;
- [`research/work_queue.json`](research/work_queue.json) — active leaves and completed/disposed packets;
- [`governance/reviews/`](governance/reviews/) — review and freeze records bound to pinned revisions.

The generated prose views are [`research/CLAIM_LEDGER.md`](research/CLAIM_LEDGER.md), [`research/PROOF_GRAPH.md`](research/PROOF_GRAPH.md), [`research/WORK_QUEUE.md`](research/WORK_QUEUE.md), [`research/ISSUE_INDEX.md`](research/ISSUE_INDEX.md), and [`STATUS.md`](STATUS.md). Do not edit generated views by hand.

A merge to `main` is transport and preservation. It does not promote a candidate, accept a proof, close a scientific leaf, or broaden a reviewed theorem.

## Current synchronized scientific boundary

- **Filtered defects:** `CLM-047–051` and `CLM-060` are `reviewed_scoped` through defect four at candidate `96fc7ec34bd3b685a0edeae7ecd4404abab7e2f1`. `CLM-073` is separately `reviewed_scoped` for a fixed primitive positive weight with actual defect five at candidate `2eeb36d232366d124b5a66774b29769ec1eba43d`, under the independent issue #38 `ACCEPT`. Neither review proves that an arbitrary Keller pair has a qualifying weight, proves arbitrary filtered termination, treats generic defect six, or establishes `JC_2`.
- **Issue #3 / rank-three index form:** the generic unramified-index bridge is disposed by `CLM-058`. The [rank-three terminal packet](research/issues/rank-three-boundary-cube-unit/README.md) records `CLM-074` at `literature_bound` scope: function-field degree three gives generic sheet number three, while Orevkov's audited primary theorem excludes that multiplicity for a polynomial Keller map. `L14` and the rank-three construction target `CLM-059` are therefore disposed without constructing a unit-index section. Conditional refinements `CLM-075`–`CLM-078` remain `candidate_proved`; no degree-four-or-higher or `JC_2` conclusion follows.
- **Issue #4 / stable lattice:** the [source-reflexive-lattice packet](research/issues/source-reflexive-lattice/README.md) proves at mutable candidate scope that a finite full module stable under both canonical translations has a finite locally free stable multiplier order, and that every finite divisorial source-pole stage escapes at ramification. `CLM-061` remains open at existence of one finite pair-stable lattice; no such lattice is constructed.
- **Issue #5 / one-boundary logarithmic field:** the predecessor packet classifies logarithmic lifting. The [one-boundary successor](research/issues/one-boundary-logarithmic-field/README.md) excludes, at mutable candidate scope, every generically ramified one-boundary model with a `G_m`-invariant reduced branch and every purely unramified one-boundary sheet-loss model. The general non-toric class remains open as `CLM-072`; exactness still permits higher principal parts.

## Start here

1. [`STATUS.md`](STATUS.md) — generated inventory, reviewed scopes, and active frontier.
2. [`governance/REPOSITORY-MAP.md`](governance/REPOSITORY-MAP.md) — canonical navigation and resume order.
3. [`research/PROGRAM.md`](research/PROGRAM.md) — common problem spine and cross-track interfaces.
4. [`research/WORK_QUEUE.md`](research/WORK_QUEUE.md) — active leaves and dispositions.
5. [`AGENTS.md`](AGENTS.md) — short-lived integration and review rules.
6. [`governance/SCIENTIFIC-WORKFLOW.md`](governance/SCIENTIFIC-WORKFLOW.md) — construction, review, synchronization, and freeze policy.
7. [`archive/MANIFEST.md`](archive/MANIFEST.md) — provenance availability and metadata-only declarations.

Issue [#2](https://github.com/snissn/planar-jacobian/issues/2) is the durable coordination surface. Leaf issues coordinate bounded research but do not override the canonical JSON surfaces. Closed issue #1 and historical bootstrap/reconciliation branches are provenance only.

## Repository layers

- `archive/` — declared source identities, historical partial chunks, and explicit metadata-only records;
- `synthesis/` — cross-conversation synthesis and corrections/retractions;
- `research/tracks/` — maintained research programs;
- `research/leaf-packets/` — bounded tasks with evidence requirements, forbidden shortcuts, stop rules, and handoffs;
- `research/issues/` and `research/issue-*` — issue-owned proof, obstruction, countermodel, and review packets;
- `governance/` — authority, source, review, concurrency, reconciliation, and validation records;
- `scripts/` — deterministic rendering, structural checks, frontier reporting, and scoped symbolic regressions.

## Mainline integration rule

Every new task starts from the latest `main`, reserves an issue-specific artifact path, uses issue-local claim labels during construction, and defers global IDs and shared ledger edits to final synchronization. Before integration, resolve `main` again; if it moved, transplant only owned files and recompute shared deltas. Do not merge an unrelated branch history merely to recover a small packet.

Branches are short-lived transport surfaces. When a pull request is useful, it should be non-draft, bounded, validated, and merged in the same run. Direct non-forced integration is permitted when repository policy allows it. Exact-byte manifests are optional provenance unless a claim-specific review requires them.

## Validation

Run against the exact candidate tree:

```bash
python3 -m compileall -q scripts research/issues
python3 -m unittest discover -s scripts/tests -p 'test_*.py'
python3 scripts/validate_integration_contract.py
python3 scripts/render_views.py --check
python3 scripts/validate_repository.py
python3 scripts/frontier.py
python3 scripts/validate_defect4_staircase.py
python3 scripts/review_validate_defect4_independent.py
python3 research/issues/issue-3-unramified-index/verify_index_models.py
python3 research/issues/rank-three-index-form-unit/verify_all.py
python3 research/issues/rank-three-boundary-cube-unit/verify_all.py
python3 scripts/validate_issue4_stable_order.py
python3 research/issues/source-reflexive-lattice/verify_all.py
python3 scripts/validate_issue5_principal_parts.py
python3 research/issues/one-boundary-logarithmic-field/verify_all.py
python3 research/issues/defect-5-rees/validate_defect5.py --max-weight 64 --json
python3 research/issues/defect-5-rees/review_validate_defect5_adversarial.py
python3 research/issues/defect-5-independent-review/review_validate_defect5_independent.py --max-weight 96
```

The GitHub Actions workflow is [`.github/workflows/repository-python-validators.yml`](.github/workflows/repository-python-validators.yml). It records the tested SHA and uploads logs. Passing checks establish repository and regression consistency only; they do not review mathematics.
