# Defect Five: Weighted Rees Staircase

> **Issue:** [#29](https://github.com/snissn/planar-jacobian/issues/29)  
> **Construction status:** `CANDIDATE_PROVED`  
> **Review status:** constructing-agent validation only until `REVIEW.md` is added at a pinned revision  
> **Exact disposition:** universal defect-five closure, with endpoint systems already invertible and every interior system admitting strict top-layer descent to defect at most four

## Result

Let `F=(P,Q)` be a polynomial pair over `C` with `J(P,Q)=1`, let
`w=(p,q)` be a primitive positive weight, and put

```text
d_P=deg_w(P),  d_Q=deg_w(Q),
kappa_w=d_P+d_Q-p-q.
```

The packet proves the following candidate theorem.

> **D5-THEOREM.** If `kappa_w=5`, then `F` is a polynomial automorphism.
> More precisely, a nonzero resonant endpoint already makes one component a
> polynomial coordinate. If all nonzero resonances are interior, then after an
> exact filtration-preserving normalization either a complete top layer is
> cancelled by a determinant-one target shear, lowering the actual integer
> defect to at most four, or the complete stairs `S_0,...,S_5` are inconsistent.

The accepted defect-at-most-four theorem is used only after a strict descent.
No defect-four case equation is imported into the new defect-five exhaustion.

## Exact scientific disposition

This is disposition **1** from issue #29:

```text
every defect-five system reduces to defect at most four,
with resonant endpoints already automorphisms.
```

The proof does not leave an exceptional weight, a smaller invariant obstruction,
or a formal weighted-layer countermodel. The first new corrections occur at
standard weight `(1,1)`: the `(1,4)` chain and the `(2,3)` quadratic/cubic
middle interaction are not consequences of the defect-four middle-Wronskian
calculation. They are derived separately in `DERIVATION.md`.

## Scope boundary

This packet does **not** prove that every Keller pair admits a primitive positive
weight of defect at most five. It does not prove termination for arbitrary
defect, does not begin defect six, and does not prove `JC_2`.

A merge into `main` is transport of a mutable scientific candidate. Unless a
distinct independent reviewer accepts the pinned candidate, the canonical status
must remain `candidate_proved`, not `reviewed_scoped` or frozen.

## Packet map

- `FOUNDATIONS.md` — exact dependency binding and independently rederived Rees identities;
- `TRANSFORMATIONS.md` — every source and target operation used, with filtration behavior;
- `DERIVATION.md` — complete human proof, including all six resonant positions;
- `CASE_TABLE.md` — exhaustive weight/resonance/support table and exceptional equations;
- `COUNTERMODEL_SEARCH.md` — exact falsification design and bounded results;
- `validate_defect5.py` — independent-from-defect-four symbolic checker;
- `VALIDATION.md` — local exact command output and authority limits;
- `REVIEW.md` — pinned local adversarial review, added separately from construction;
- `HANDOFF.md` — integration and independent-review handoff.

## Claim labels during construction

The issue-local labels are:

- `D5-REES`: exact Rees identity and stairs through `S_5`;
- `D5-NORM`: scalar-retaining graded normalization and simultaneous-resonance covariance;
- `D5-DESCENT`: complete-top cancellation and strict actual-defect decrease;
- `D5-SIEVE`: common-root/support exhaustion;
- `D5-EQUAL`: the two genuinely new equal-weight contradictions;
- `D5-THEOREM`: the scoped defect-five theorem candidate.

Global `CLM-*` identifiers are intentionally allocated only in the final
synchronization against the then-current `main`.
