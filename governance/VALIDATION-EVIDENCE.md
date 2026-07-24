# Structural Validation Evidence

> **Scope:** repository consistency only  
> **Mathematical truth:** not evaluated

## Local environment

- Date: 2026-07-24
- Python: `3.13.5`
- Reconciled source tree: branch `maintenance/reconcile-rich-baseline-gpt56`
- Pinned source refs: see [`RECONCILIATION-REPORT.md`](RECONCILIATION-REPORT.md)

## Commands and results

```bash
python3 -m compileall -q scripts
```

Result: `PASS`.

```bash
python3 scripts/render_views.py --check
```

Result: `generated views: PASS (6 files)`.

```bash
python3 scripts/validate_repository.py
```

Result:

```text
claims: 51
graph nodes: 34
graph edges: 50
queue leaves: 13
errors: 0
warnings: 2
repository structure: PASS
mathematical truth: NOT EVALUATED
```

The two warnings are intentional and accurate: both conversation exports are `metadata_only`, so their declared raw/gzip hashes cannot be reproduced from the current Git tree.

```bash
python3 scripts/frontier.py
```

Result: 51 claims, 34 graph nodes, 50 graph edges, 13 open leaves (`P0=7`, `P1=4`, `P2=1`, `P3=1`), two `metadata_only` exports, and `ROOT-JC2:blocked`.

All repository JSON files also parsed successfully with `python3 -m json.tool`.

## Reconciliation-preservation checks

The canonical claim projection over `id`, `status`, `track`, `statement`, and `depends_on` has the same SHA-256 in the rich source and reconciled tree:

```text
0f63e0f2ee5ee2375735c58aa4704fdf81004e14dc584b2c85d65270e5f7d1db
```

The proof graph is byte-identical to the pinned rich source:

```text
39ccadb5da1479a4103c24ef4fc7d0d7b2f93183420c540a7f952c31d62e0425
```

The archive manifest is byte-identical to the pinned rich source:

```text
a2711cd291e4e522be0216c6a7201ba08f4aee7310885faed89e32f6402684db
```

The five current-main independent-review files and `scripts/review_validate_defect4_independent.py` are checked against their pinned current-main SHA-256 values by the structural validator.

## Validator coverage

The structural validator checks:

- every JSON file parses;
- claim IDs, status vocabulary, dependency closure, and dependency acyclicity;
- proof-graph node IDs, endpoint closure, edge uniqueness, relations, and artifact paths;
- one-to-one consistency among 13 canonical leaf packets, graph leaf nodes, queue entries, issues, tracks, and claim dependencies;
- required leaf-contract sections;
- legacy claim migration links and preserved coarse statuses;
- generated prose/JSON exact consistency;
- archive storage modes, issue #22, historical partial paths, and embedded hashes when applicable;
- conversation-index/manifest consistency and prohibition on false lossless-reconstruction claims;
- internal Markdown path links;
- removal of closed issue #1 and superseded issue-1 branches from active navigation; and
- pinned rich semantic hashes plus retained current-main review-file hashes.

## GitHub Actions binding

The canonical workflow is [`.github/workflows/repository-python-validators.yml`](../.github/workflows/repository-python-validators.yml). The final exact branch-head SHA, workflow run ID, conclusion, and retained log artifact are recorded on draft PR #24 after publication, because the commit containing this file cannot contain its own SHA.
