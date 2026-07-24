# Review Records

Files in this directory are review evidence bound to the claims and revisions named inside them. A review disposition does not automatically mutate `research/claim_ledger.json` or `research/proof_graph.json`.

The issue-17 independent review records an `ACCEPT` for the candidate at `96fc7ec34bd3b685a0edeae7ecd4404abab7e2f1`. Its `issue-17-defect4-independent-claim-graph-delta.md` file states that the delta is proposal-only. This structural reconciliation retains the review and leaves the canonical machine-ledger statuses and proof graph unchanged.

Exact-byte manifests and hashes appearing in historical review records are preserved as provenance. Repository-wide governance now treats such hashes as optional unless a claim-specific policy requires them.
