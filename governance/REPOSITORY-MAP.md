# Repository Map and Resume Order

## Canonical navigation

1. [`../STATUS.md`](../STATUS.md)
2. [`EXECUTION-LIFECYCLE.md`](EXECUTION-LIFECYCLE.md)
3. [`PARALLEL-BATCH-WORKFLOW.md`](PARALLEL-BATCH-WORKFLOW.md)
4. [`REMOTE-COMPLETION.md`](REMOTE-COMPLETION.md)
5. [`../research/PROGRAM.md`](../research/PROGRAM.md)
6. [`../research/WORK_QUEUE.md`](../research/WORK_QUEUE.md)
7. [`../research/PROOF_GRAPH.md`](../research/PROOF_GRAPH.md)
8. [`../research/CLAIM_LEDGER.md`](../research/CLAIM_LEDGER.md)
9. [`../research/ISSUE_INDEX.md`](../research/ISSUE_INDEX.md)
10. [`../AGENTS.md`](../AGENTS.md)

Issue [#2](https://github.com/snissn/planar-jacobian/issues/2) is the durable coordination surface. Latest `main` is the only operating baseline.

## Governance and validation

- `governance/SCIENTIFIC-WORKFLOW.md` — scientific and integration authority rules;
- `governance/EXECUTION-LIFECYCLE.md` — role boundaries and stopping states;
- `governance/PARALLEL-BATCH-WORKFLOW.md` — parallel workers and serialized integration;
- `governance/REMOTE-COMPLETION.md` — evidence and completion receipt;
- `governance/TEMPORARY-ARTIFACT-POLICY.md` — forbidden transport artifacts and workflow rules;
- `governance/INTEGRATION-MANIFEST.schema.json` — issue-packet integration contract;
- `scripts/validate_integration_contract.py` — manifest, PR-boundary, workflow, and temporary-artifact validation;
- `scripts/validate_repository.py` — canonical ledgers, graph, queue, provenance, generated views, and link validation.

## Scientific layers

- `research/tracks/` — maintained program tracks;
- `research/leaf-packets/` — canonical active or disposed bounded tasks;
- `research/issues/issue-3-unramified-index/` — moving-index theorem, countermodel, audit, provenance, and validator packet;
- `research/issues/rank-three-index-form-unit/` — rank-three Keller index-form successor;
- `research/issues/source-reflexive-lattice/` — issue #4 source-lattice obstruction successor;
- `research/issues/one-boundary-logarithmic-field/` — issue #5 one-boundary successor;
- `research/issue-4/stable-differential-order/` — predecessor stable-order theorem and ramified-DVR obstruction;
- `research/issue-5/` — predecessor radial/logarithmic principal-part packet;
- `research/audits/` — defect-four exact proof and source audits;
- `governance/reviews/` — independent review, local review, manifests, and freeze records.

## Current resume rule

Use the generated [`../research/WORK_QUEUE.md`](../research/WORK_QUEUE.md) for current priority and state. Do not maintain a second handwritten leaf order here.

`L01` is disposed by a scoped countermodel. `L13` is reviewed at defect-at-most-four scope. Neither disposition proves `JC_2`.

## Provenance and archive

The rich baseline, historical PRs, and branch refs are recorded in [`RECONCILIATION-REPORT.md`](RECONCILIATION-REPORT.md) and [`reconciliation-inventory.json`](reconciliation-inventory.json). They are not active operating baselines. Conversation exports remain metadata-only as declared in [`../archive/manifest.json`](../archive/manifest.json).
