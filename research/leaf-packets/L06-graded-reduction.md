# Wright Graded Reduction

- **Priority:** `P0`
- **Status:** `OPEN`
- **Dependencies:** CLM-024, CLM-025, CLM-047–CLM-051
- **Authority:** `MUTABLE_NONAUTHORITATIVE`

## Load-bearing question

Reduce an arbitrary one-boundary Keller pair to a homogeneous nonzero constant-bracket pair without losing the constant bracket or worsening another boundary valuation.

## New filtered subproblem

The weighted Rees staircase in Track M supplies an explicit filtered formulation of this bridge. The bounded defect-4 audit is delegated to

[`L13-defect-4-staircase.md`](L13-defect-4-staircase.md), issue [#17](https://github.com/snissn/planar-jacobian/issues/17).

The conversation-derived claim that positive-weight grading defects through `3` reduce to the exact graded case is not yet accepted and must be independently audited before it can support this leaf.

## Accepted evidence

A terminating valuation/Newton/Rees procedure preserving the decisive bracket term, with:

- a well-founded reduction invariant;
- exact control of all source and target transformations;
- compatibility across every boundary valuation;
- an exact graded endpoint covered by a source-bound theorem.

## Forbidden shortcuts

- Do not replace algebraic dependence of leading forms by polynomial dependence without proof.
- Do not assume an associated-graded automorphism lifts to an automorphism.
- Do not improve one valuation while silently worsening another.
- Do not treat the defect-4 packet as sufficient for this full leaf.

## Required artifacts

Reduction invariant, termination measure, multi-valuation compatibility, final homogeneous pair, and exact linkage to the filtered defect subcases.

## Stop rule

Stop when the declared implication is proved at exact scope, or when a minimal counterexample to the proposed bridge is constructed. Bank useful restricted lemmas separately; do not widen the leaf to the entire conjecture without a graph update.

## Handoff

Record exact formulas, source bindings, tested countermodels, open sublemmas, resolved defect ranges, surviving weight patterns, and the smallest next action.