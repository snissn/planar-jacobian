# Follow-up Agent Prompt

Use this prompt verbatim or adapt only the task-specific scope.

```text
You are continuing a rigorous research program on the two-dimensional Jacobian conjecture.

Repository:
  https://github.com/snissn/planar-jacobian

Intended scientific baseline:
  PR #15 / branch agent/bootstrap-proof-graph
  baseline commit 86d1b78cedd788b7335be692f9bb92921142c7d3
  https://github.com/snissn/planar-jacobian/pull/15

Active issue-scoped branch:
  issue-17/defect-4-staircase

Active task:
  issue #17
  https://github.com/snissn/planar-jacobian/issues/17

Scientific workflow:
  https://github.com/snissn/skills/tree/main/scientific-mainline-workflow

Before changing any scientific claim, read:
  scientific-mainline-workflow/SKILL.md
  scientific-mainline-workflow/references/scientific-review-checklist.md

Authority and scope:
  - MUTABLE_NONAUTHORITATIVE
  - protocol_verdict: null
  - no file in the repository proves JC_2
  - conversation exports are provenance and idea input, not theorem authority

Read in order:
  1. README.md
  2. STATUS.md
  3. AGENTS.md
  4. research/PROGRAM.md
  5. research/PROOF_GRAPH.md
  6. research/WORK_QUEUE.md
  7. research/CLAIM_LEDGER.md
  8. synthesis/CORRECTIONS_AND_RETRACTIONS.md
  9. research/tracks/m-filtered-equivariance.md
  10. research/leaf-packets/L13-defect-4-staircase.md
  11. research/tracks/g-wright-graded-single-tree.md
  12. research/tracks/j-equivariant-degeneration.md
  13. research/SOURCE_INVENTORY.md

Primary task:
  Adversarially audit the weighted Rees staircase and resolve the first
  unproved filtered case, kappa_w=4.

Setup:
  For a primitive positive weight w=(p,q), write

    d_P = deg_w P,
    d_Q = deg_w Q,
    kappa_w = d_P+d_Q-p-q,

  and decompose

    P = sum_i P_i,
    Q = sum_j Q_j,

  with deg_w P_i=d_P-i and deg_w Q_j=d_Q-j.

  Independently verify the Rees identity

    J(Pcal,Qcal)=t^(kappa_w)

  and all resulting staircase equations.

Load-bearing defect-4 equation in the central resonance pattern:

  J(P_0,Q_2)+J(P_1,Q_1)+J(P_2,Q_0)=0.

The middle Wronskian J(P_1,Q_1) is the first term absent from the
lower-defect line-pencil argument. Determine whether it can always be:

  (a) removed by a filtration-compatible target automorphism;
  (b) removed by a filtered polynomial symplectic/source transformation;
  (c) shown to force forbidden Newton--Puiseux or boundary-monodromy data;
  (d) or realized by a formal layer system disproving the staircase ansatz.

Required audit:
  - Recompute every sign, weight, and exponent independently.
  - Treat the conversation-derived kappa_w<=3 proof as a candidate.
  - Enumerate resonance positions (1,3), (2,2), and (3,1).
  - Include unequal positive weights and missing intermediate layers.
  - State every permitted source or target transformation exactly.
  - Prove each transformation preserves J=1.
  - Prove the declared descent measure strictly decreases.
  - Search primary literature on graded Keller maps, Newton inner
    polynomials, filtered symplectic normal forms, and weighted
    automorphism reduction.
  - Try to falsify every proposed lemma before strengthening it.

Do not use:
  - the retired Euler boundary-excess identity;
  - a generic-fiber Kummer model as a global Galois conclusion;
  - exactness of a form as a principalization theorem;
  - multiple sheets as evidence of a global deck symmetry;
  - unreviewed conversation prose as theorem authority.

Expected pushed artifacts:
  - a complete defect-4 case table;
  - exact derivations for every load-bearing equation;
  - a catalogue of allowed filtration-preserving transformations;
  - formal countermodels or obstruction calculations;
  - a theorem candidate, scoped obstruction, or smaller blocked invariant;
  - synchronized claim-ledger, proof-graph, work-queue, and leaf updates;
  - an adversarial review bound to exact candidate bytes.

Acceptable dispositions:
  1. full defect-4 reduction;
  2. a substantial declared subclass theorem;
  3. a formal counterexample to staircase reduction;
  4. a strictly smaller invariant obstruction with a proved reduction.

Do not broaden to higher defects until defect 4 has an exact disposition.
Do not rename the missing implication and present it as a proof of JC_2.
```
