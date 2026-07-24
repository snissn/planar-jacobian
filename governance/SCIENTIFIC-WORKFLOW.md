# Scientific Workflow Reference

This repository uses the scientific-mainline workflow maintained at:

- repository: <https://github.com/snissn/skills>
- skill directory: <https://github.com/snissn/skills/tree/main/scientific-mainline-workflow>
- skill file: <https://github.com/snissn/skills/blob/main/scientific-mainline-workflow/SKILL.md>
- review checklist: <https://github.com/snissn/skills/blob/main/scientific-mainline-workflow/references/scientific-review-checklist.md>

The repository-specific workflow was reconciled against:

```text
snissn/skills@0a6876bc72be73295a3772733d87293fcf4d3b35
```

## Repository-specific authority

The upstream workflow supplies general process. [`AUTHORITY-HIERARCHY.md`](AUTHORITY-HIERARCHY.md) and this file govern explicit repository-specific mechanics.

## GitHub operations

- Use the connected GitHub adapter for repository reads and writes, branches, commits, issues, pull requests, comments, and review metadata whenever it supports the operation.
- Fall back to local `git`, `gh`, or another mechanism only for a capability gap.
- Confirm repository permissions, pinned base, current head, and changed-path scope before writing.
- Use non-forced ref updates. Do not rewrite published history, delete source branches, or overwrite another agent’s branch.
- Tool choice and transport success carry no scientific authority.

## Applied workflow

1. Select one canonical leaf and governing issue.
2. Pin the starting revision and create an issue-scoped branch.
3. Use a unique artifact directory and avoid shared-ledger edits during construction.
4. Commit coherent `MUTABLE_NONAUTHORITATIVE` work.
5. Bind review to identified claims at a pinned revision.
6. Prefer a distinct reviewer; permit declared `local-adversarial-review` when necessary.
7. Apply accepted scientific deltas only in a final synchronization commit against the latest canonical baseline.
8. Regenerate machine-derived views and run local structural validation.
9. Run the repository GitHub Actions validator at the exact proposed integration SHA.
10. Integrate without material unreviewed scientific changes.

The detailed concurrency rules are in [`PARALLEL-AGENT-POLICY.md`](PARALLEL-AGENT-POLICY.md).

## Review binding and revisions

Review records must identify their mode, claims, files, dependencies, and pinned revision; recompute load-bearing steps; test countercontrols; record risks; and return `ACCEPT` or `BLOCK` for the declared scope.

Shared constructor/reviewer identity alone is not a blocker. Exact-byte manifests and hashes are optional provenance rather than universal acceptance gates. Material scientific changes require renewed review; editorial or metadata-only changes do not automatically invalidate a review.

## Validation and CI

Run locally:

```bash
python3 -m compileall -q scripts
python3 scripts/render_views.py --check
python3 scripts/validate_repository.py
python3 scripts/frontier.py
```

The exact-commit fallback is [`.github/workflows/repository-python-validators.yml`](../.github/workflows/repository-python-validators.yml). Preserve the tested commit SHA, run ID, conclusion, and logs in the pull-request or issue handoff.

Structural validation checks repository consistency, identifiers, dependencies, artifact paths, generated views, archive declarations, and internal Markdown paths. It is not mathematical review, does not promote a claim, and does not issue a scientific verdict.
