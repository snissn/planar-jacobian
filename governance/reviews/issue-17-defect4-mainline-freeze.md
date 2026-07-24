# Issue #17 Defect-Four Mainline Freeze

- **Disposition:** `FROZEN_ACCEPTED` at the scoped claim level
- **Canonical claim status:** `reviewed_scoped`
- **Reviewed candidate revision:** `96fc7ec34bd3b685a0edeae7ecd4404abab7e2f1`
- **Candidate aggregate SHA-256:** `21550a32815a617cdb108c41954fb422c66773656a560505aeefcbf180a4a097`
- **Independent review:** [`issue-17-defect4-independent-gpt56.md`](issue-17-defect4-independent-gpt56.md)
- **Review disposition:** `ACCEPT`

## Accepted scope

The freeze covers `CLM-047–051` and `CLM-060`:

```text
For any primitive positive weight w,
if a planar Keller pair has grading defect kappa_w <= 4,
then the pair is a polynomial automorphism.
```

The reviewed subclaims include the Rees staircase identities, resonant graded automorphism lemma, top-layer endpoint reduction, full defect-at-most-three audit, and the defect-four interior exhaustion.

## Protected scientific paths

- `research/audits/defect-4-staircase-audit.md`
- `research/audits/defect-4-case-table.md`
- `research/audits/filtered-transformation-catalogue.md`
- `research/audits/defect-4-primary-source-audit.md`
- `research/leaf-packets/L13-defect-4-staircase.md`
- `research/tracks/m-filtered-equivariance.md`
- `research/tracks/g-wright-graded-single-tree.md`
- `research/tracks/j-equivariant-degeneration.md`
- `scripts/validate_defect4_staircase.py`
- the independent reconstruction and validation records named by the review

The candidate commit remains the exact reviewed byte reference. Mainline copies may receive editorial headers, links, status labels, and transport metadata without changing the accepted mathematics.

## Forbidden stronger inference

This freeze does not establish:

- a theorem at grading defect five or higher;
- existence of a primitive positive weight with defect at most four for every Keller pair;
- termination of filtered descent for arbitrary defect;
- the planar Jacobian conjecture; or
- any result in higher dimension.

Any material change to the theorem, hypotheses, case analysis, common-power lemma, support exhaustion, transformation catalogue, or symbolic identities requires renewed review.

## Validation boundary

The candidate and independent validators are process evidence. They do not replace the independent mathematical review and do not broaden the freeze.
