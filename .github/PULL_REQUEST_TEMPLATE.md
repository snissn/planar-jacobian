## Execution identity

- Role: `research-worker` / `reviewer` / `integration-maintainer` / `governance-maintainer`
- Task-Issue: `#`
- Owned-Path:
- Supersedes-PRs:
- Pinned base SHA:
- Head branch and SHA:

## Scientific scope

- Scientific status:
- Exact claims or non-delta:
- Explicit nonclaims:

## Artifact and synchronization boundaries

- Issue-specific paths:
- Shared surfaces changed:
- Global IDs allocated by integration maintainer:
- Parallel branches intentionally untouched:
- `INTEGRATION.json` path:

## Review state

- Review mode:
- Reviewed claims and pinned revision:
- Disposition:
- Material changes after review:

## Validation

- `python3 -m compileall -q scripts research/issues`
- `python3 scripts/render_views.py --check`
- `python3 scripts/validate_repository.py`
- `python3 scripts/validate_integration_contract.py`
- `python3 -m unittest discover -s scripts/tests -p 'test_*.py'`
- `python3 scripts/frontier.py`
- Issue-specific checks:
- GitHub Actions tested SHA, run ID, conclusion:

## Temporary-artifact check

- [ ] No `.b64`, workspace export, marker, one-shot workflow, root log, or branch-only sync script is included.
- [ ] Validation workflows do not mutate or push the candidate.
- [ ] This is the only open PR for the task issue and owned path.

## Remote-completion receipt

Complete after merge; do not prefill successful states.

```yaml
repository:
task_issue:
owned_path:
role:
main_before:
candidate_sha:
review_mode:
reviewed_revision:
scientific_status:
pr_number:
pr_head:
pr_merged:
merge_sha:
main_after:
compare_result:
critical_files_refetched:
actions_run_id:
actions_tested_sha:
actions_conclusion:
issue_final_state:
superseded_prs_closed:
remaining_open_prs:
scientific_nonclaims:
```

Structural validation and merge state are not mathematical review.
