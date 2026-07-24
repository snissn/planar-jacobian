# Scientific Workflow Reference

This repository uses the scientific repository workflow maintained at:

- repository: <https://github.com/snissn/skills>
- skill directory: <https://github.com/snissn/skills/tree/main/scientific-mainline-workflow>
- skill file: <https://github.com/snissn/skills/blob/main/scientific-mainline-workflow/SKILL.md>
- scientific review checklist: <https://github.com/snissn/skills/blob/main/scientific-mainline-workflow/references/scientific-review-checklist.md>

The workflow version consulted for this issue branch is pinned to:

```text
snissn/skills@0a6876bc72be73295a3772733d87293fcf4d3b35
```

## Applied rules

- Use an issue-scoped feature branch as the durable mutable surface.
- Commit and push coherent non-decisive scientific iterations.
- Mark mutable work `MUTABLE_NONAUTHORITATIVE` with `protocol_verdict: null`.
- Keep theorem candidates distinct from literature results, blocked implications, and retired claims.
- Bind independent scientific review to exact candidate bytes before promotion.
- Do not use a pull request as a substitute for adversarial theorem review.
- Integrate to the intended baseline only after the scientific workflow's review and validation gates are satisfied.
- Prefer the installed GitHub adapter for authenticated repository transport when it exposes the required operation; do not infer that remote writes are impossible merely because the local `gh` executable is absent.

## Repository transport

The operational adapter procedure is recorded in [`GITHUB-ADAPTER.md`](GITHUB-ADAPTER.md). In particular:

1. establish the exact repository, permissions, base commit, current branch, and existing branch diff before any write;
2. use adapter branch, file, tree, commit, ref, and issue actions rather than treating the container's network or CLI state as authoritative;
3. use non-forced ref updates and preserve unrelated work;
4. verify the resulting branch by reading committed files and comparing it with the pinned base; and
5. keep exact-byte candidate identity, independent review, transport provenance, and mainline authority separate.

Adapter availability is an engineering capability, not scientific review. Publishing a candidate through the adapter does not change `MUTABLE_NONAUTHORITATIVE`, does not set a protocol verdict, and does not supply the required independent `ACCEPT`.

The upstream skill remains authoritative for process. This file records the repository-specific adoption and the version used during the filtered-equivariance synchronization.
