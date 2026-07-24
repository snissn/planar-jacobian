# Planar Jacobian Research Mainline

> **Authority:** `MUTABLE_NONAUTHORITATIVE`  
> **Engineering status:** `DEVELOPMENT`  
> **Execution validity:** `NOT_A_SCIENTIFIC_EXECUTION`  
> **Protocol verdict:** `null`  
> **Scientific inference:** `none`

This repository is a durable, dependency-tracked research workspace for the planar Jacobian conjecture. It preserves the rich proof graph, machine-readable claim ledger, parallel tracks, 13 bounded leaf packets, maintained syntheses, correction register, source inventory, structural validators, and provenance metadata assembled in the original bootstrap line.

**The repository does not claim an unconditional proof of the planar Jacobian conjecture.** A claim’s status, an accepted review, a frozen artifact, a green CI run, and complete provenance are separate facts.

## Canonical authority

The authority hierarchy is defined in [`governance/AUTHORITY-HIERARCHY.md`](governance/AUTHORITY-HIERARCHY.md). In brief:

1. the pinned upstream scientific workflow supplies general process;
2. repository-specific governance supplies explicit local overrides;
3. [`research/claim_ledger.json`](research/claim_ledger.json), [`research/proof_graph.json`](research/proof_graph.json), and [`research/work_queue.json`](research/work_queue.json) are the canonical machine-readable status and queue surfaces;
4. generated Markdown views mirror those JSON files; and
5. issues, branches, and pull requests coordinate work but do not change scientific status.

The reconciliation source refs, branch inventory, and conflict decisions are recorded in [`governance/RECONCILIATION-REPORT.md`](governance/RECONCILIATION-REPORT.md). PR #15 remains preserved as the rich source branch until the replacement integration path is accepted; it is not the active coordination surface for new work.

## Start here

1. [`STATUS.md`](STATUS.md) — generated repository status and P0 frontier.
2. [`governance/REPOSITORY-MAP.md`](governance/REPOSITORY-MAP.md) — canonical paths and resume order.
3. [`research/PROGRAM.md`](research/PROGRAM.md) — common problem spine.
4. [`research/PROOF_GRAPH.md`](research/PROOF_GRAPH.md) — generated dependency graph.
5. [`research/WORK_QUEUE.md`](research/WORK_QUEUE.md) — generated leaf queue.
6. [`research/CLAIM_LEDGER.md`](research/CLAIM_LEDGER.md) — generated claim-status view.
7. [`AGENTS.md`](AGENTS.md) and [`governance/PARALLEL-AGENT-POLICY.md`](governance/PARALLEL-AGENT-POLICY.md) — operating rules.
8. [`archive/MANIFEST.md`](archive/MANIFEST.md) — provenance state and issue #22.

Issue [#2](https://github.com/snissn/planar-jacobian/issues/2) is the durable program coordination surface. Each canonical leaf also has its own issue, listed in [`research/ISSUE_INDEX.md`](research/ISSUE_INDEX.md). Closed issue #1 and its branches are historical provenance only.

## Repository layers

- `archive/`: declared source identities, historical partial chunks, topic summaries, and explicit `metadata_only` storage declarations.
- `synthesis/`: narrative reconciliation and corrections/retractions.
- `research/tracks/`: parallel formal research programs.
- `research/leaf-packets/`: bounded tasks with evidence requirements and stop rules.
- `research/*.json`: canonical claim, graph, queue, and legacy-migration data.
- `governance/`: authority, review, source-audit, concurrency, handoff, and reconciliation records.
- `scripts/`: deterministic rendering, structural validation, archive handling, and frontier reporting.

## Review and scientific status

A distinct reviewer is preferred. A declared `local-adversarial-review` is permitted when necessary, and shared constructor/reviewer identity is not by itself a reason to return `BLOCK`. Review acceptance is bound to an identified claim at a pinned repository revision. Exact-byte manifests and hashes may strengthen provenance, but they are not universal acceptance gates.

Material scientific changes require renewed review of the affected scope. Editorial, link, formatting, transport, or metadata-only changes do not automatically invalidate an accepted review. Structural validation and GitHub Actions remain engineering evidence, not mathematical review.

Current-main review artifacts for the defect-four candidate are retained under [`governance/reviews/`](governance/reviews/). Their proposed claim/graph delta remains proposal-only in this reconciliation; no machine-ledger claim status was promoted.

## Provenance boundary

The repository records declared filenames, message counts, byte counts, and hashes for two source conversations. The complete source-export bytes are unavailable in the Git tree. Both exports remain `metadata_only`; historical partial chunks cannot reconstruct either export. Archive completion remains issue [#22](https://github.com/snissn/planar-jacobian/issues/22).

## Validation

Run:

```bash
python3 -m compileall -q scripts
python3 scripts/render_views.py --check
python3 scripts/validate_repository.py
python3 scripts/frontier.py
```

The canonical GitHub Actions workflow is [`.github/workflows/repository-python-validators.yml`](.github/workflows/repository-python-validators.yml). It binds validation to the tested commit SHA and retains logs. Passing checks establish repository consistency only; they do not establish mathematical truth or promote a claim.
