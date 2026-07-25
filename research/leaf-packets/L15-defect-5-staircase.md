# L15 — Independent Review of Fixed-Weight Defect Five

> **Construction issue:** [#29](https://github.com/snissn/planar-jacobian/issues/29)  
> **Review issue:** [#38](https://github.com/snissn/planar-jacobian/issues/38)  
> **Issue packet:** [`../issues/defect-5-rees/`](../issues/defect-5-rees/)  
> **Banked claim:** `CLM-073` (`candidate_proved`)  
> **Required review mode:** `independent-review`

## Load-bearing question

Independently review the exact issue #29 candidate at `2eeb36d232366d124b5a66774b29769ec1eba43d`: for a fixed primitive positive weight and actual grading defect five, does every Keller pair have a resonant endpoint or a filtration-compatible strict descent to defect at most four?

## Forbidden shortcuts

- Do not treat the local adversarial review as independent acceptance.
- Do not infer existence of a defect-at-most-five weight for every Keller pair.
- Do not omit zero layers, simultaneous resonances, either source-weight order, or either target-component order.
- Do not begin defect six or attach a terminal `JC_2` edge.

## Required artifacts

- independent reconstruction of normalization, complete-top descent, support sieve, equal-weight chains, and finite exceptional systems;
- an independently implemented checker or exact hand calculations;
- a pinned `ACCEPT` or `BLOCK` review record;
- a synchronization proposal limited to `CLM-073` and `OPEN-DEFECT-5`.

## Candidate evidence

The issue packet contains a complete derivation, exact case table, from-definitions checker, mutation controls, saturated Gröbner eliminations, and a separate local-adversarial-review checker. These are falsification evidence, not independent theorem authority.

## Stop rule

Return `ACCEPT` only after every load-bearing case and transformation is independently reconstructed at the pinned bytes. Otherwise return the smallest exact `BLOCK`, correction, or formal countermodel.

## Handoff

On independent `ACCEPT`, promote only the fixed-weight defect-five statement. Preserve the nonclaims about qualifying-weight existence, defect six, arbitrary termination, and `JC_2`.
