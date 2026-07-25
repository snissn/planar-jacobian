# Defect-five handoff

## Candidate requiring independent review

Pin the integrated revision containing this packet and review the following exact statement:

> If a planar polynomial Keller pair over `C` has grading defect `kappa_w=5` for a fixed primitive positive weight `w`, then a filtration-compatible polynomial source or target automorphism strictly lowers the actual integer defect. Hence the pair is an automorphism by the independently accepted defect-at-most-four theorem.

Do not reinterpret the statement as existence of a defect-five weight for every Keller pair.

## Highest-value review targets

1. **Normalization covariance.** Verify that the graded inverse preserves each layer index and that determinant compensation retains, rather than normalizes away, every resonant scalar.
2. **Common-power convention.** Verify that `gcd(m,n)=1` is used consistently, especially for `p=1`, `(a,b)=(3,2)`, `rho=2`, `q congruent 0 mod 4`.
3. **Generic support contradictions.** Recheck the empty/pure-`x` support claims in the unequal-weight infinite families.
4. **Finite `(4,1)` reduction.** Recheck the derivation `N<=M`, then `q<=p+3`, before accepting the three finite weights.
5. **Standard-weight mixed root.** Recompute the `H=x+y` chart from `S_1` through `S_4`; this is the first new defect-five correction chain.
6. **Simultaneous resonances.** Confirm the complete `S_5` equations and their signs in all six finite unequal systems.
7. **Top descent.** Confirm cancellation of the complete top layer, preservation of `J=1`, and strict decrease of the actual integer `kappa`.

## Reproduction

```bash
python3 research/issues/defect-5-rees/validate_defect5.py --max-weight 64 --json
```

Re-run repository-wide schema, link, claim-ledger, and proof-graph checks at the pinned revision. The script is supporting evidence only; an independent review should cite exact line ranges and either record `ACCEPT`, request a scoped correction, or provide a formal/actual countermodel.

## Status transition rule

Until an independent review is merged, retain the new global claim and successor proof-graph node as `candidate`. A later `ACCEPT` may promote only the fixed-weight defect-five reduction statement and its direct corollary through the already accepted defect-at-most-four theorem.

Do not begin defect six from this handoff.
