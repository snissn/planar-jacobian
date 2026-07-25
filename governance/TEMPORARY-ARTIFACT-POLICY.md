# Temporary Artifact and Workflow Policy

Git branches and pull requests transport source files. They must not transport opaque workspaces or self-modifying synchronization machinery into `main`.

## Forbidden in final integration

Unless explicitly reviewed as permanent source provenance, final diffs must not contain:

- `.github/**/sync/`, `.github/*-sync/`, or equivalent transport directories;
- `*.b64` payloads outside the declared historical archive policy;
- workspace-export, workspace-upload, one-shot rebuild, or branch-sync workflows;
- `.integration-ready`, `.local-review-complete`, or similar marker files;
- generated tarballs, ZIP archives, bundles, or root validation logs;
- scripts whose only purpose is to commit generated files back to a branch;
- issue-specific Actions workflows;
- Actions that commit or push to the branch being validated;
- `permissions: contents: write` in validation workflows, unless a permanent maintainer workflow is separately reviewed and explicitly allowlisted.

## Allowed durable artifacts

Keep human-readable proofs, source audits, review records, exact validators, machine-readable scientific ledgers, stable schemas, completion receipts, and permanent read-only validation workflows.

## Actions rule

GitHub Actions validates immutable candidate bytes. It may render expected output for comparison, but it must not repair, commit, or push the candidate. Validation workflows use read-only contents permissions; status publication may use `statuses: write`.

## Cleanup

Before merge, search the changed-file list and repository tree for forbidden paths. Remove one-shot synchronization scripts and reports after their durable scientific content and validation evidence have been preserved elsewhere.
