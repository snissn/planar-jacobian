# Issue #38 Defect-Five Mainline Freeze

- **Disposition:** `FROZEN_ACCEPTED` at the scoped claim level
- **Canonical claim status:** `reviewed_scoped`
- **Reviewed candidate revision:** `2eeb36d232366d124b5a66774b29769ec1eba43d`
- **Candidate aggregate SHA-256:** `333614389c339f4a3383856de2dfc5b977dc5dd6a6520f176b25c7116d861d12`
- **Independent review:** [`../../research/issues/defect-5-independent-review/REVIEW.md`](../../research/issues/defect-5-independent-review/REVIEW.md)
- **Independent review packet head:** `c31fa0361daabb06c08148ea3941e281433869f6`
- **Review disposition:** `ACCEPT`

## Accepted scope

The freeze covers `CLM-073`:

```text
For any fixed primitive positive weight w,
if a planar Keller pair has actual integer grading defect kappa_w = 5,
then a filtration-compatible polynomial source or target automorphism
strictly lowers the actual defect to at most four, and the pair is a
polynomial automorphism by the reviewed defect-at-most-four theorem.
```

The independent review reconstructs the Rees identity and complete staircase, scalar-retaining normalization, common-power reduction, complete-top descent, endpoints, all four interior positions, both weight and component orders, zero layers, simultaneous resonances, equal-weight systems, and unequal exceptional systems.

## Protected scientific paths

- `research/issues/defect-5-rees/README.md`
- `research/issues/defect-5-rees/DERIVATION.md`
- `research/issues/defect-5-rees/CASE_TABLE.md`
- `research/issues/defect-5-rees/validate_defect5.py`
- `research/issues/defect-5-independent-review/REVIEW.md`
- `research/issues/defect-5-independent-review/BINDING.md`
- `research/issues/defect-5-independent-review/review_validate_defect5_independent.py`
- the exact candidate and independent reconstruction records named by the review

The candidate commit remains the exact reviewed byte reference. Mainline copies may receive editorial headers, links, status labels, transport metadata, and the non-load-bearing adversarial-checker support correction without changing the accepted mathematics.

## Engineering correction outside the theorem bytes

The constructing-agent adversarial checker formerly placed the `(2,3)` target leading layer at weight `(2,3)` on `B*x**2`. The correct weight-six layer is `B*x**3`; the maintained checker now asserts that `(3,0)` is supported and `(2,0)` is not. This repair does not modify the pinned theorem, case table, construction checker, accepted statement, or review binding.

## Forbidden stronger inference

This freeze does not establish:

- existence of a qualifying primitive positive weight for every Keller pair;
- termination of filtered descent for arbitrary defect;
- a generic theorem at defect six or higher;
- the planar Jacobian conjecture; or
- any result in higher dimension.

Any material change to the theorem, hypotheses, case analysis, support exhaustion, transformation catalogue, common-power argument, or symbolic identities requires renewed independent review.

## Validation boundary

The candidate, adversarial, and independent validators are process evidence. They do not replace the independent mathematical review and do not broaden the freeze.
