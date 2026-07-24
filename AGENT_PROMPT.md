# Follow-up Agent Prompt

Use this prompt verbatim or adapt only the task-specific scope.

```text
You are continuing a rigorous research program on the two-dimensional Jacobian conjecture.

Repository:
  https://github.com/snissn/planar-jacobian

Scientific workflow:
  https://github.com/snissn/skills/tree/main/scientific-mainline-workflow
  Read scientific-mainline-workflow/SKILL.md, its scientific review checklist,
  and governance/SCIENTIFIC-WORKFLOW.md before changing any claim status.

Repository operations:
  - Use the connected GitHub adapter for repository reads and writes, branches,
    commits, issues, pull requests, and review metadata whenever it is available
    and supports the required operation.
  - Fall back to local git or gh only when the adapter is unavailable or does not
    support the operation.

Operating context:
  - Active issue: https://github.com/snissn/planar-jacobian/issues/1
  - Mutable research branch: issue-1/synchronized-findings
  - This branch is MUTABLE_NONAUTHORITATIVE.
  - Do not claim that JC_2 is proved unless every load-bearing step has a
    documented accepted review and the maintainer explicitly approves promotion.

Review mode:
  - A distinct reviewer or subagent is preferred when available.
  - If the environment does not support subagents or another reviewer, perform a
    separate local adversarial review pass and label it local-adversarial-review.
  - Do not return BLOCK solely because the same assistant constructed and reviewed
    the candidate.
  - Bind the review to the claim and a pinned commit or repository revision.
    Exact-byte manifests and artifact hashes are optional, not mandatory.
  - Re-review any material change to a statement, proof, computation,
    transformation, dependency, or counterexample.

Read in order:
  1. README.md
  2. STATUS.md
  3. AGENTS.md
  4. governance/SCIENTIFIC-WORKFLOW.md
  5. research/PROGRAM.md
  6. research/CLAIM_LEDGER.md
  7. research/tracks/filtered-equivariance.md
  8. research/leaf-packets/defect-4-staircase.md
  9. research/SOURCES.md

Primary task:
  Adversarially audit the weighted Rees staircase and then resolve the first unproved filtered case, grading defect kappa=4.

Load-bearing equation in the central resonance pattern:
  J(P_0,Q_2) + J(P_1,Q_1) + J(P_2,Q_0) = 0.

The middle Wronskian J(P_1,Q_1) is the first term absent from the lower-defect line-pencil argument. Determine whether it can always be:
  (a) removed by a filtration-compatible target automorphism;
  (b) removed by a filtered polynomial symplectic/source transformation;
  (c) shown to force a forbidden Newton/Puiseux or boundary-monodromy configuration; or
  (d) realized by a formal layer system that disproves the staircase-reduction ansatz.

Required scientific discipline:
  - Independently recompute the Rees exponent and every staircase equation.
  - Audit the candidate kappa<=3 proof before depending on it.
  - Enumerate all defect-4 resonance positions: (1,3), (2,2), and (3,1), including missing layers and unequal positive weights.
  - State exactly which source and target transformations are allowed and prove that they preserve J=1 and lower the declared defect.
  - Treat conversation exports as provenance, not theorem authority.
  - Do not use the retired boundary-excess identity, the retired generic-fiber-to-global-Kummer inference, or exact-form principalization.
  - Search primary literature for weighted Keller maps, Newton inner polynomials, symplectic normal forms, and filtered/graded automorphism reductions.
  - Try to falsify each candidate lemma before strengthening it.

Expected output on an issue-scoped feature branch:
  - a theorem candidate or scoped obstruction with explicit hypotheses;
  - a complete case table for defect 4;
  - exact derivations or symbolic identities for every load-bearing equation;
  - an adversarial review note with ACCEPT/BLOCK disposition, declared review mode,
    and a pinned commit or repository revision;
  - updates to the claim ledger and active leaf packet;
  - a pushed branch commit after every coherent non-decisive step.

Acceptable outcomes:
  1. prove all defect-4 cases reduce to smaller defect;
  2. prove a substantial declared subclass reduces;
  3. find a formal counterexample to the reduction ansatz;
  4. isolate a strictly smaller invariant obstruction and prove the reduction to it.

Do not broaden to arbitrary higher defects until defect 4 has an exact disposition. Do not rename the missing implication and present it as a theorem.
```
