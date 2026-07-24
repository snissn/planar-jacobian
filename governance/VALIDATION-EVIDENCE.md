# Validation Evidence Contract

Validation is bound to an exact candidate SHA and records engineering/process evidence only.

## Required checks

1. Python byte-compilation for all repository scripts and the issue #3 validator.
2. JSON parsing for every JSON file.
3. Prose/JSON generated-view consistency.
4. Claim-ID uniqueness, dependency existence, and acyclic closure.
5. Proof-graph node, edge, relation, review, and artifact-path checks.
6. Active queue and disposition consistency, including exact coverage of every canonical `L##` packet.
7. Internal Markdown link checks.
8. Archive metadata and no-fabrication checks.
9. Frontier rendering.
10. Defect-four candidate symbolic regression.
11. Independent defect-four review validator.
12. Issue #3 symbolic countermodel validator.
13. Issue #4 stable-order formula regression.
14. Issue #5 principal-part/tangency regression.
15. GitHub Actions on the exact integration candidate and final main SHA.

## Recording

The Actions workflow prints the tested SHA, writes separate logs for each check, and uploads an artifact named with the SHA and run ID. The PR or issue #2 handoff records the run ID, conclusion, and artifact digest. The repository file cannot contain its own final commit SHA without becoming self-referential.

## Limits

Structural checks can establish parseability, consistency, dependency closure, preserved paths, and exact symbolic identities at the tested scope. They do not evaluate unbounded mathematical truth, reviewer independence, source theorem applicability, or `JC_2`.
