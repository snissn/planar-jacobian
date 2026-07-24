# Scientific Workflow Reference

This repository uses the scientific repository workflow maintained at:

- repository: <https://github.com/snissn/skills>
- skill directory: <https://github.com/snissn/skills/tree/main/scientific-mainline-workflow>
- skill file: <https://github.com/snissn/skills/blob/main/scientific-mainline-workflow/SKILL.md>
- scientific review checklist: <https://github.com/snissn/skills/blob/main/scientific-mainline-workflow/references/scientific-review-checklist.md>

The workflow version consulted for the current branch is pinned to:

```text
snissn/skills@0a6876bc72be73295a3772733d87293fcf4d3b35
```

## Repository-specific authority

The upstream skill supplies the default process. This file is authoritative for repository-specific tool use and review mechanics. Where this file explicitly differs from the pinned upstream workflow, this file governs work in `snissn/planar-jacobian`.

## GitHub operations

- Use the connected GitHub adapter for repository reads and writes, branch creation, commits, issues, pull requests, and review metadata whenever it is available and supports the required operation.
- Fall back to local `git`, `gh`, or another repository mechanism only when the adapter is unavailable or does not support the operation.
- Tool choice does not confer scientific authority. A pushed commit or pull request remains development provenance until the relevant scientific review and promotion gates are satisfied.

## Applied rules

- Use an issue-scoped feature branch as the durable mutable surface.
- Commit and push coherent non-decisive scientific iterations.
- Mark mutable work `MUTABLE_NONAUTHORITATIVE` with `protocol_verdict: null`.
- Keep theorem candidates distinct from literature results, blocked implications, and retired claims.
- Bind scientific review to an identified claim and a pinned repository revision.
- Do not use a pull request as a substitute for adversarial theorem review.
- Integrate to `main` only after the review, validation, synchronization, and freeze gates below are satisfied.

## Review modes

A distinct human reviewer, agent, or subagent is preferred when one is available. It is not an absolute requirement.

If the execution environment does not support subagents or a distinct reviewer, the constructing assistant may perform a separate local adversarial review pass. That review must not be marked `BLOCK` solely because the same assistant performed construction and review.

Every review record must:

1. declare its mode as `independent-review` or `local-adversarial-review`;
2. identify the claim IDs, statements, proof files, and dependencies in scope;
3. identify the reviewed commit SHA or other unambiguous repository revision;
4. recompute load-bearing identities rather than merely restating the construction;
5. test stated edge cases and plausible countermodels;
6. record validation commands and results;
7. list unresolved risks; and
8. issue an explicit `ACCEPT` or `BLOCK` disposition for the declared scope.

A local adversarial review may support promotion when no distinct reviewer is available, unless an issue, maintainer decision, or claim-specific policy imposes a stricter gate. A claim presented as a proof of `JC_2` additionally requires explicit maintainer approval and accepted reviews of every load-bearing dependency.

## Revision binding

Exact-byte manifests and artifact hashes are optional evidence, not mandatory workflow gates. Review acceptance is bound to the identified claim at the pinned repository revision.

Editorial, formatting, link, or metadata changes do not automatically invalidate an accepted review when they do not alter the reviewed mathematical content. Any material change to a reviewed statement, hypothesis, proof step, computation, transformation, dependency, or counterexample requires a new review of the affected scope.

## Promotion and merge

A `CANDIDATE` may become `FROZEN_ACCEPTED` when:

- the reviewed statement and proof scope are explicit;
- a review record meeting the requirements above returns `ACCEPT`;
- required validations pass;
- the claim ledger, proof graph, work queue, status files, and active leaf packet are synchronized as applicable; and
- the accepted revision is integrated to `main` without unreviewed material changes to the accepted scientific content.

The upstream skill remains the source of general process guidance; this file records the repository-specific adoption and overrides for adapter use, local-review fallback, and revision-level review binding.
