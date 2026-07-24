# Contributing

Use one issue-scoped branch per canonical leaf and pin the starting revision. Follow [`governance/PARALLEL-AGENT-POLICY.md`](governance/PARALLEL-AGENT-POLICY.md); keep issue-specific artifacts separate from final shared-ledger synchronization, and never overwrite another agent’s branch.

Before proposing integration, run:

```bash
python3 -m compileall -q scripts
python3 scripts/render_views.py --check
python3 scripts/validate_repository.py
python3 scripts/frontier.py
```

Bind literature-dependent claims to exact primary-source scope. Prefer an independent reviewer, while permitting a declared `local-adversarial-review` under repository governance. Do not treat pull requests or CI as mathematical review, and do not merge an unconditional theorem claim without the required scoped review and synchronization.
