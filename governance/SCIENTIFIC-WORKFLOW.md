# Scientific Mainline Workflow

This repository uses `main` as the durable integration surface for coherent research, including speculative, conditional, blocked, falsified, and countermodel-bearing work. Scientific authority is carried by explicit claim status and review records, not inferred from branch location, pull-request state, merge status, manifests, or CI.

## Operating roles

Every run declares one role from [`EXECUTION-LIFECYCLE.md`](EXECUTION-LIFECYCLE.md): `research-worker`, `reviewer`, `integration-maintainer`, or `governance-maintainer`. Parallel construction and serialized integration are defined in [`PARALLEL-BATCH-WORKFLOW.md`](PARALLEL-BATCH-WORKFLOW.md).

## Mainline integration rules

1. Every agent starts from the latest `main`, records its full SHA, and selects one issue or leaf. A pull request or historical branch is never the operating baseline.
2. Every task reserves a unique issue-specific artifact path before construction begins and records it in `INTEGRATION.json`.
3. Construction uses issue-local claim labels. Global claim IDs are allocated only during final integration against the then-current ledger.
4. Shared ledgers, proof graphs, README, STATUS, issue index, queue, and generated views are updated only by the integration maintainer during final synchronization.
5. Immediately before integration, re-resolve `main`. If it moved, create a fresh branch from the new head, transplant only owned files, and recompute shared deltas there.
6. Unrelated branch histories are never merged merely to recover a small packet.
7. Coherent speculative work, conditional results, blockers, falsification results, and countermodels should be integrated promptly with explicit status rather than left on a large branch.
8. A worker produces at most one small, non-draft integration-ready PR. The integration maintainer merges one validated packet at a time. A safe direct non-forced update is acceptable when repository policy permits it.
9. A merge to `main` is transport and preservation, not scientific acceptance. It does not close a leaf unless the leaf’s scientific stop rule is met.
10. Exact-byte manifests and hashes remain optional provenance unless a claim-specific review explicitly requires them.
11. A separate declared `local-adversarial-review` is allowed when no distinct reviewer is available. Shared identity must not be represented as independent review.
12. Material changes to an accepted claim, hypothesis, proof step, computation, transformation, dependency, or counterexample require renewed review. Editorial-only changes, formatting, links, transport, and metadata do not automatically invalidate acceptance.

## Continuation and duplicate prevention

A progress update is not a stopping point. A repeated or continuation message resumes the existing branch and PR. Before creating a vehicle, search for the same issue and owned path. A replacement PR is permitted only after the obsolete predecessor is closed as superseded. At most one open PR may own one issue path.

## Construction record

Record exact hypotheses, dependencies, transformations, computations, countermodels, permitted inference, forbidden stronger inference, and the smallest surviving action. Keep issue-owned files separate from shared synchronization surfaces until the packet is coherent.

## Review

A review declares `independent-review` or `local-adversarial-review`, identifies the pinned revision and exact files and claims, recomputes load-bearing reasoning, tests edge cases and mutations, records validation commands and limitations, lists unresolved risks, and returns a scoped `ACCEPT` or `BLOCK`.

A distinct reviewer is preferred. A pull request, merge, manifest, validator count, or green CI run is not mathematical review.

## Final synchronization

The integration maintainer reconciles the claim ledger, proof graph, queue and dispositions, issue index, README, STATUS, and generated views field by field. It applies an accepted review only at its exact statement, dependencies, and pinned revision. It preserves branch provenance without importing unrelated history.

## Temporary artifacts and workflows

Final integration follows [`TEMPORARY-ARTIFACT-POLICY.md`](TEMPORARY-ARTIFACT-POLICY.md). Validation workflows inspect immutable bytes and do not commit or push. Opaque transport payloads, marker files, issue-specific workflows, and branch-only synchronization scripts are forbidden from `main`.

## Validation

Against the exact integration candidate, run Python byte-compilation, generated-view consistency, JSON parsing, integration-manifest validation, prose/JSON claim-ledger consistency, claim and proof-graph dependency closure, artifact-path checks, queue/disposition consistency, internal Markdown links, workflow-permission checks, and each imported issue-specific regression check. Run GitHub Actions on that exact SHA and record the run and log artifact.

Validators are engineering evidence and do not evaluate mathematical truth.

## Remote completion

Follow [`REMOTE-COMPLETION.md`](REMOTE-COMPLETION.md). Do not report merged, closed, on-main, verified, or green states without adapter evidence obtained in the same execution.

## Coordination

Issue [#2](https://github.com/snissn/planar-jacobian/issues/2) is the durable coordination surface. After integration, record the canonical SHA, resume order, validation evidence, closed transport PRs, and surviving scientific leaves there.
