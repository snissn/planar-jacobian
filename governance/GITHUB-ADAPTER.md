# GitHub Adapter Procedure

> **Scope:** repository transport and coordination only  
> **Scientific authority:** none

Future agents must check the installed GitHub adapter before reporting that a branch, commit, or issue update cannot be published. The adapter is independent of the container's local `gh` executable and independent of direct DNS access from shell commands.

## 1. Discover and confirm capability

1. Read the installed GitHub skill before repository work.
2. Discover only the needed adapter functions, for example by querying the GitHub tool resource for `branch`, `commit`, `files`, or `issue`.
3. Retrieve repository metadata and confirm `push` permission before attempting a write.
4. Fetch the active issue and its comments for steering changes.

Do not expose connector credentials or internal adapter payloads in repository files or issue comments.

## 2. Establish exact branch state

- Resolve the repository as `owner/name`.
- Pin the intended base by full commit SHA.
- Read at least one known file at the target branch to confirm that the ref resolves.
- Compare the pinned base and target branch before writing.
- If branch creation reports that the reference already exists, do not overwrite it. Inspect and compare the existing branch instead.
- Preserve unrelated branch work. Use a non-forced ref update unless an explicitly reviewed recovery procedure authorizes otherwise.

The branch-search action may return no rows even when a slash-containing branch resolves through file reads. Treat an exact `fetch_file(..., ref=branch)` or successful compare as stronger evidence than an empty branch-search result.

## 3. Publish files

### Small changes

For one or a few files:

1. fetch an existing file and retain its blob SHA;
2. call the adapter's file-update action with the complete replacement text, blob SHA, branch, and commit message; or
3. call the file-create action for a path that does not exist.

Do not run concurrent writes to the same path.

### Coherent multi-file changes

For a coherent multi-file commit:

1. obtain the current branch-head commit SHA from a successful adapter write or another exact adapter result;
2. create a Git tree using that current commit SHA as `base_tree_sha` and entries containing exact repository paths, mode `100644`, type `blob`, and complete contents;
3. create one commit with that tree and the current head as `parent_sha`; and
4. move the branch ref to the new commit with `force=false`.

The installed adapter used for issue #17 accepted the current commit SHA as `base_tree_sha` and returned the derived tree SHA. Always inspect the returned result and stop on an adapter error.

For exact-byte scientific work, verify local hashes before transport and refetch decisive files after the ref update. A later governance-only commit may follow, but it must not silently modify the candidate file set bound by the scientific manifest.

## 4. Coordinate through the issue

Use the issue-comment action to record:

- branch and exact commit;
- base commit;
- changed artifact set;
- validation results and their limits;
- review disposition and remaining blocker; and
- the next bounded action.

The adapter's top-level issue-comment action may name its numeric parameter `pr_number`; for a normal issue, pass the issue number there. Do not close an active scientific issue unless its maintained stop rule and governance gate are actually satisfied.

## 5. Verify transport

After publication:

- compare the branch with the pinned base;
- fetch the candidate manifest and representative scientific files from the branch;
- verify the branch contains the intended paths and no accidental probe or temporary file;
- record the final commit in the issue; and
- distinguish transport success from scientific acceptance.

A pushed mutable branch is durable development provenance. It is not a freeze commit, mainline integration, protocol verdict, or proof of `JC_2`.

## 6. Fallback rule

Use local `git` or `gh` only for a gap the adapter does not cover. Before declaring a transport blocker, document which adapter action was discovered, what exact call failed, and why no supported adapter alternative applies. Absence of a local `gh` binary by itself is not a blocker.

## 7. Exact-review transport records

A manifest or review record may contain a transport snapshot from the moment the candidate bytes were assembled. When later adapter publication changes only repository transport state, do not rewrite the exact manifest merely to make that historical block look current: doing so changes the bytes under review. Preserve the bound manifest, record the later branch commit and publication status in the governing issue or a separate transport record, and obtain renewed review only when a scientific candidate byte changes.

For issue #17, the manifest's local-only transport block is intentionally generation-time provenance. The GitHub issue records the subsequent adapter publication; the candidate aggregate and manifest SHA-256 values remain unchanged.
