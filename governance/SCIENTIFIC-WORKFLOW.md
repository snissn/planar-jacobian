# Scientific Workflow Reference

This repository uses the scientific repository workflow maintained at:

- repository: <https://github.com/snissn/skills>
- skill directory: <https://github.com/snissn/skills/tree/main/scientific-mainline-workflow>
- skill file: <https://github.com/snissn/skills/blob/main/scientific-mainline-workflow/SKILL.md>
- scientific review checklist: <https://github.com/snissn/skills/blob/main/scientific-mainline-workflow/references/scientific-review-checklist.md>
- GitHub Actions Python fallback: <https://github.com/snissn/skills/blob/main/scientific-mainline-workflow/references/github-actions-python-fallback.md>

The workflow version consulted for this engineering branch is pinned to:

```text
snissn/skills@fa64c31e4c389d10fcdc04c12c5aa71450a9d4c8
```

## Applied rules

- Use an issue-scoped feature branch as the durable mutable surface.
- Commit and push coherent non-decisive scientific iterations.
- Mark mutable work `MUTABLE_NONAUTHORITATIVE` with `protocol_verdict: null`.
- Keep theorem candidates distinct from literature results, blocked implications, and retired claims.
- Bind independent scientific review to exact candidate bytes before promotion.
- Do not use a pull request or a green CI check as a substitute for adversarial theorem review.
- Integrate to the intended baseline only after the scientific workflow's review and validation gates are satisfied.

## Python validation environments

Local execution remains preferred when a usable Python runtime is available:

```bash
python3 -m compileall -q scripts
python3 scripts/validate_repository.py
python3 scripts/frontier.py
```

When the local runtime is unavailable or blocked, the repository-owned workflow
`.github/workflows/repository-python-validators.yml` is the approved fallback execution environment. It checks out and tests the exact triggering commit, records the Python version and SHA, propagates validator failures, and retains logs as a workflow artifact.

Before this workflow is present on the repository's default branch, use its `push` or `pull_request` trigger. Once it is on the default branch, it may also be dispatched manually:

```bash
workflow=repository-python-validators.yml
branch=$(git branch --show-current)

gh workflow run "$workflow" --ref "$branch"
run_id=$(gh run list \
  --workflow "$workflow" \
  --branch "$branch" \
  --event workflow_dispatch \
  --limit 1 \
  --json databaseId \
  --jq '.[0].databaseId')
gh run watch "$run_id" --exit-status
```

Inspect failures and retrieve retained logs with:

```bash
gh run view "$run_id" --log-failed
gh run download "$run_id"
```

For every CI fallback run, record the tested commit SHA, workflow revision, run ID and attempt, event, Python version, decisive commands, exit statuses, and artifact names. A green run is process evidence for those committed bytes only. It does not validate mathematical truth, promote a claim, freeze a candidate, or create a scientific verdict.

Infrastructure failure is `ENGINEERING DEFECT — NO SCIENTIFIC VERDICT`. Decision-bearing scientific executions remain subject to the workflow's separate review, freeze, qualification, trial-start, persistence, and replay rules; they must not be moved to CI merely because local execution is blocked.

The upstream skill remains authoritative for process. This file records the repository-specific adoption and the version used for issue #20.
