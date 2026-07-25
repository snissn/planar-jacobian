# Remote Completion Gate

Remote completion is a verified state, not an intention or local result.

## Required evidence

When a pull request is used, the same execution that reports completion must obtain:

1. pull-request metadata showing `merged=true`;
2. the live `main` SHA after merge;
3. a comparison showing the intended revision is contained in or identical to live `main`;
4. critical files refetched from live `main`;
5. exact-main workflow status and tested SHA;
6. the governing issue’s final state;
7. final states of every superseded pull request.

A prospective merge commit, mergeable PR, branch workflow, local file, patch, bundle, or workflow artifact is insufficient.

## Completion receipt

Record this block in the final PR or issue comment:

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

## Failure receipt

When completion is blocked, record:

```yaml
failed_adapter_action:
returned_error:
current_branch:
current_pr:
completed_acceptance_items:
incomplete_acceptance_items:
```

Do not convert a failure receipt into a success statement.
