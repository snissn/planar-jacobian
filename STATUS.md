# Status

## Program status

- **Authority:** mutable, non-authoritative research synthesis.
- **Main theorem:** open in this repository.
- **Scientific verdict:** none.
- **Intended rich baseline:** PR [#15](https://github.com/snissn/planar-jacobian/pull/15), branch `agent/bootstrap-proof-graph`.
- **Active scientific branch:** `issue-17/defect-4-staircase`.
- **Validator engineering branch:** `issue-20/python-validator-ci`.
- **Conversation provenance:** 304 messages represented in maintained synthesis and source metadata; the complete export bytes are not yet embedded in the Git tree and are tracked in issue [#22](https://github.com/snissn/planar-jacobian/issues/22).
- **Claim ledger:** 51 claims across 9 statuses.
- **Proof graph:** 34 nodes and 49 directed edges.
- **Open leaf packets:** 13.

## New synchronized lane

Shaska's arXiv:2607.20210 is recorded as a primary source for exact `G_m`-equivariant planar Keller rigidity. Track M studies a weighted Rees filtration of an arbitrary Keller pair.

The following are **candidate**, not accepted theorem statements:

1. the weighted Rees staircase identity and resonant-layer extraction;
2. the top-layer cancellation criterion;
3. reduction of positive-weight grading defects through `kappa<=3`.

The first explicitly blocked filtered case is `kappa=4`, where the middle term

```text
J(P_1,Q_1)
```

appears in the central resonance equation. Issue [#17](https://github.com/snissn/planar-jacobian/issues/17) is the active bounded audit.

## Validation infrastructure

Issue [#20](https://github.com/snissn/planar-jacobian/issues/20) adds GitHub Actions execution of the deterministic Python validators. Local execution remains preferred; Actions is the exact-commit fallback when the local runtime is blocked. CI checks repository structure and declared provenance state, not mathematical truth.

## Highest-priority frontier

1. **Unramified index elimination.** Construct one ramification-adapted primitive element with no accidental collision divisor in the finite étale locus.
2. **Stable differential order.** Produce a finite `C[P,Q]`-order stable under both canonical lifted translations.
3. **Radial pole elimination.** Extend one canonical radial vector field across the finite normalization boundary.
4. **Filtered defect 4.** Audit the entire Rees staircase and resolve the middle Wronskian in all resonance positions.
5. **Wright graded reduction.** Preserve the nonzero constant bracket while reducing a one-boundary Keller pair to its exact graded model.
6. **Normalization baseline audit.** Reprove or precisely source every boundary, flatness, and class-group statement before building on it.

## Provenance warning

The conversations contain productive derivations, but also changing low-degree frontiers, overstrong purity statements, and candidate theorems later withdrawn. Treat conversation exports and summaries as idea input. The maintained claim ledger is the only claim-status surface.

Repository structural validation does not constitute mathematical validation. No candidate filtered result may be promoted without independent exact-byte review under the pinned scientific workflow.
