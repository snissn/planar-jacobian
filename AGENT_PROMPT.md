# Follow-up Agent Prompt

Use this prompt verbatim for the independent scientific review of issue #17.

```text
You are independently reviewing a theorem candidate in a rigorous research
program on the two-dimensional Jacobian conjecture.

Repository:
  https://github.com/snissn/planar-jacobian

Intended scientific baseline:
  PR #15 / branch agent/bootstrap-proof-graph
  baseline commit 86d1b78cedd788b7335be692f9bb92921142c7d3
  https://github.com/snissn/planar-jacobian/pull/15

Candidate branch:
  issue-17/defect-4-staircase

Active task:
  independent exact-byte review of issue #17
  https://github.com/snissn/planar-jacobian/issues/17

Scientific workflow:
  https://github.com/snissn/skills/tree/main/scientific-mainline-workflow

Before reviewing any scientific claim, read:
  scientific-mainline-workflow/SKILL.md
  scientific-mainline-workflow/references/scientific-review-checklist.md

Authority and scope:
  - MUTABLE_NONAUTHORITATIVE
  - protocol_verdict: null
  - no file in the repository proves JC_2
  - conversation exports are provenance, not theorem authority
  - do not accept a manifest whose bytes differ from the review record

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
  11. research/audits/defect-4-staircase-audit.md
  12. research/audits/defect-4-case-table.md
  13. research/audits/filtered-transformation-catalogue.md
  14. research/audits/defect-4-primary-source-audit.md
  15. governance/reviews/issue-17-defect-4-exact-byte-review.md
  16. governance/reviews/issue-17-defect-4-candidate-manifest.json

Candidate theorem:
  For a primitive positive weight w=(p,q), every planar Keller pair with

    kappa_w=deg_w(P)+deg_w(Q)-p-q <= 4

  is a polynomial automorphism.

Primary review burden:
  - Recompute the Rees chain-rule exponent and every staircase sign.
  - Prove the homogeneous common-power lemma without importing algebraic
    dependence as polynomial dependence.
  - Verify the compensated source/target normalization retains the nonzero
    resonant scalar and preserves J=1.
  - Verify endpoint resonance makes a full component a coordinate.
  - Recompute both interior orientations at kappa=3.
  - Recompute defect-4 positions (1,3), (2,2), and (3,1), including reversed
    resonant degree orientation, unequal weights, and missing layers.
  - In the central exceptional weight (1,2), independently derive

      3af=4bv,
      J(P_1,Q_1)=(2uf-3ve)x^2-vfy,
      (3ac+2uf-3ve)x^2-vfy=0.

  - In the (3,1) exceptional weight (1,2), independently derive the nonzero
    cv*y coefficient in S_2.
  - Verify every target descent cancels a complete top layer and strictly
    lowers kappa_w.
  - Try to build a formal polynomial layer countermodel before accepting the
    support exhaustion.
  - Run both repository and defect-four validators, but do not treat them as
    mathematical authority.

Do not use:
  - the retired Euler boundary-excess identity;
  - a generic-fiber Kummer model as a global Galois conclusion;
  - exactness of a form as a principalization theorem;
  - multiple sheets as evidence of a global deck symmetry;
  - the constructor's prose as authority.

Required disposition:
  Return exactly ACCEPT or BLOCK, bound to the exact candidate manifest and
  the scoped kappa_w<=4 theorem. On BLOCK, identify the smallest false equation,
  omitted case, circular premise, or manifest/provenance defect. On ACCEPT,
  promote only the scoped theorem; do not claim JC_2 or begin defect 5 in the
  same review. Use FAIL SELECTED REALIZATION or CLASS-LEVEL OBSTRUCTION only if
  the scientific-review checklist genuinely requires one of those dispositions.
```
