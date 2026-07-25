# Independent Review of the Fixed-Weight Defect-Five Reduction

> **Role:** `reviewer`  
> **Task issue:** [#38](https://github.com/snissn/planar-jacobian/issues/38)  
> **Owned path:** `research/issues/defect-5-independent-review/`  
> **Review mode:** `independent-review`  
> **Live-main base:** `652a5e252626fa5816445651245e8a8946cee53e`  
> **Reviewed scientific revision:** `2eeb36d232366d124b5a66774b29769ec1eba43d`  
> **Disposition:** **ACCEPT for the exact fixed-weight defect-five statement**  
> **Authority before integration:** `MUTABLE_NONAUTHORITATIVE`

## Exact reviewed statement

Let `F=(P,Q)` be a polynomial pair over `C` with `J(P,Q)=1`, and let
`w=(p,q)` be a fixed primitive positive weight. Put

```text
d_P=deg_w(P),  d_Q=deg_w(Q),
kappa_w=d_P+d_Q-p-q.
```

The review accepts exactly:

> If `kappa_w=5`, then `F` is a polynomial automorphism. More precisely, a
> nonzero resonant endpoint already yields invertibility, while every interior
> resonant system either admits a filtration-compatible polynomial
> normalization followed by a determinant-one complete-top target shear that
> strictly lowers the actual nonnegative integer defect to at most four, or is
> inconsistent with the complete weighted Rees staircase.

The accepted implication uses the already independently reviewed theorem that a
fixed primitive positive weight with defect at most four implies automorphy.

## Disposition

**ACCEPT.** The Rees identity, constant-bracket classification, scalar-retaining
normalization, common-power lemma, complete-top descent, endpoints, all four
interior positions, all primitive positive weight regimes, zero layers,
simultaneous resonances, the two new equal-weight systems, and every unequal
exception were reconstructed independently. No formal full-staircase
countermodel survived.

One flaw was found in a post-candidate, constructing-agent
`local-adversarial-review` checker: its `(a,b)=(2,3)`, `w=(2,3)` model writes
`Q_0=B x^2`, although `deg_w Q_0=6` requires `Q_0=B x^3`. The pinned human
candidate, its case table, and the construction checker use the correct degree.
The flaw therefore lowers confidence in that prior regression artifact but does
not alter this independent mathematical disposition.

## Explicit nonclaims

This review does not prove:

- that every Keller pair admits a primitive positive weight of defect at most five;
- termination of filtered descent at arbitrary defect;
- any defect-six theorem;
- the planar Jacobian conjecture;
- any statement in dimension greater than two.

## Reviewer-owned artifacts

- `BINDING.md` — exact candidate, blob, dependency, and transport binding;
- `RECONSTRUCTION.md` — independent derivation from definitions;
- `CASE_AUDIT.md` — exhaustive weight, resonance, support, and coefficient audit;
- `TRANSFORMATION_AUDIT.md` — all source and target operations and inverses;
- `COUNTERMODEL_AUDIT.md` — independent exact search, saturation, and mutations;
- `REVIEW.md` — formal independent-review disposition;
- `HANDOFF.md` — proposed integration delta without shared-surface edits;
- `VALIDATION.md` — local checker record and remote validation boundary;
- `review_validate_defect5_independent.py` — reviewer-owned exact checker;
- `INTEGRATION.json` — issue-owned integration manifest.

The candidate proof under `research/issues/defect-5-rees/` is not edited by
this review.
