# Status

## Program status

- **Authority:** mutable, non-authoritative research synthesis.
- **Main theorem:** open in this repository.
- **Scientific verdict:** none.
- **Intended rich baseline:** PR [#15](https://github.com/snissn/planar-jacobian/pull/15), branch `agent/bootstrap-proof-graph`, commit `86d1b78cedd788b7335be692f9bb92921142c7d3`.
- **Current issue branch:** `issue-17/defect-4-staircase`.
- **Imported conversations:** 304 messages preserved losslessly in the bootstrap baseline.
- **Claim ledger:** 52 claims across 9 statuses.
- **Proof graph:** 34 nodes and 50 directed edges.
- **Open leaf packets:** 12, plus one `candidate_proved` leaf awaiting independent review.

## Filtered-lane disposition

The weighted Rees identity, resonant normalization, top-layer descent, and all cases through positive-weight grading defect `4` have been rederived in a self-contained candidate packet.

The exact scoped theorem candidate is:

```text
J(P,Q)=1 and kappa_w<=4 for one primitive positive weight w
    => (P,Q) is a polynomial automorphism.
```

At defect `4`, every endpoint resonance is a top coordinate. The interior positions `(1,3)`, `(2,2)`, and `(3,1)` either admit an exact determinant-one target shear that strictly lowers `kappa_w`, or violate an earlier staircase equation or weighted support condition. The central exceptional weight `(1,2)` is eliminated by the exact coefficient system

```text
3af=4bv,
vf=0,
3ac+2uf-3ve=0.
```

The result remains **`candidate_proved`** because a distinct independent reviewer has not accepted the exact candidate-byte manifest. It is not a proof of `JC_2`, and it does not cover defect `5` or establish that an arbitrary Keller map has a small-defect positive weight.

Primary artifacts:

- [`research/audits/defect-4-staircase-audit.md`](research/audits/defect-4-staircase-audit.md)
- [`research/audits/defect-4-case-table.md`](research/audits/defect-4-case-table.md)
- [`research/audits/filtered-transformation-catalogue.md`](research/audits/filtered-transformation-catalogue.md)
- [`research/audits/defect-4-primary-source-audit.md`](research/audits/defect-4-primary-source-audit.md)

## Highest-priority frontier

1. **Unramified index elimination.** Construct one ramification-adapted primitive element with no accidental collision divisor in the finite étale locus.
2. **Stable differential order.** Produce a finite `C[P,Q]`-order stable under both canonical lifted translations.
3. **Radial pole elimination.** Extend one canonical radial vector field across the finite normalization boundary.
4. **Defect-4 independent review.** Audit the exact candidate manifest and return `ACCEPT` or the smallest mathematical `BLOCK`; do not start defect `5` first.
5. **Wright graded reduction.** Integrate the scoped positive-weight result without assuming that a general boundary grading has defect at most four.
6. **Normalization baseline audit.** Reprove or precisely source every boundary, flatness, and class-group statement before building on it.

## Provenance warning

The conversations contain productive derivations, but also changing low-degree frontiers, overstrong purity statements, and candidate theorems later withdrawn. Treat the raw archive as idea input. The maintained claim ledger is the only status surface.

Repository validation and the constructor's adversarial audit do not constitute independent mathematical acceptance. No candidate filtered result may be frozen without exact-byte review under the pinned scientific workflow.
