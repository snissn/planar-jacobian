# Contributing

All work starts from the latest `main` and uses an issue-specific artifact path. Branches are short-lived transport surfaces; `main` is the durable integration surface for coherent research at any explicit scientific status.

Use issue-local claim labels while constructing a packet. Allocate global claim IDs and update shared ledgers, graphs, README, STATUS, and generated views only during final synchronization against the then-current `main`.

A pull request, merge, exact-byte manifest, or green validator run is not mathematical review. Review authority comes from a scoped review record bound to a pinned revision. Material changes to accepted mathematics require renewed review; editorial-only changes do not.

Run the repository validators before integration:

```bash
python3 -m compileall -q scripts research/issues/issue-3-unramified-index
python3 scripts/render_views.py --check
python3 scripts/validate_repository.py
python3 scripts/frontier.py
```

Follow [`governance/SCIENTIFIC-WORKFLOW.md`](governance/SCIENTIFIC-WORKFLOW.md) for construction, review, synchronization, and integration.
