# Authority Hierarchy

## 1. Mathematical authority

Mathematical authority is carried by an identified claim statement, its canonical status, dependencies, and any review/freeze records bound to a pinned revision. Repository location is not authority.

A merge to `main`, a pull request, branch name, commit signature, exact-byte manifest, or green Actions run cannot by itself accept or promote a claim.

## 2. Canonical repository surfaces

For their declared fields, authority is ordered as follows:

1. [`research/claim_ledger.json`](../research/claim_ledger.json) for claim statements, dependencies, status, and explicit review metadata;
2. [`research/proof_graph.json`](../research/proof_graph.json) for dependency nodes, edges, and leaf disposition;
3. [`research/work_queue.json`](../research/work_queue.json) for active leaves and completed/disposed packets;
4. review and freeze records in [`governance/reviews/`](reviews/);
5. issue-owned scientific artifacts at their stated authority;
6. generated Markdown views, which must exactly mirror the JSON sources;
7. issues and pull requests as coordination and transport records.

When prose and machine data disagree, stop and synchronize; do not silently choose the more convenient statement.

## 3. Mainline authority

`main` is the durable preservation and integration surface for coherent research of every status, including speculative, conditional, blocked, falsified, and countermodel work. Presence on `main` means the bytes are canonical repository content, not that the mathematics is accepted.

## 4. Reviewed scope

`reviewed_scoped` requires an explicit `ACCEPT` record, reviewed revision, exact statement, and freeze/synchronization record. It authorizes only that scope. Material changes require renewed review; editorial and transport changes may be recorded without reopening the mathematics.

The defect-at-most-four scope is reviewed only as recorded in [`reviews/issue-17-defect4-mainline-freeze.md`](reviews/issue-17-defect4-mainline-freeze.md). It is not a defect-five theorem and not `JC_2`.

## 5. Coordination

Issue [#2](https://github.com/snissn/planar-jacobian/issues/2) is the durable program coordination surface. Leaf issues coordinate bounded work. Historical issue #1, PR #15, PR #24, and their branches are provenance only after consolidation.
