# Issue #17 — Independent Review of the Defect-at-Most-Four Theorem Candidate

> **Review mode:** `independent-review`
> **Reviewer:** GPT-5.6 Pro
> **Disposition:** `ACCEPT`
> **Authority of this branch:** `MUTABLE_NONAUTHORITATIVE` until the repository's separate freeze/integration gates are applied
> **Scientific execution:** none

## 1. Exact binding and branch resolution

- **Repository:** `snissn/planar-jacobian`
- **Issue:** `#17`
- **Candidate branch:** `issue-17/defect-4-staircase`
- **Reviewed candidate commit:** `96fc7ec34bd3b685a0edeae7ecd4404abab7e2f1`
- **Candidate baseline:** `86d1b78cedd788b7335be692f9bb92921142c7d3`
- **Candidate manifest:** `governance/reviews/issue-17-defect-4-candidate-manifest.json`
- **Candidate aggregate SHA-256:** `21550a32815a617cdb108c41954fb422c66773656a560505aeefcbf180a4a097`
- **Manifest SHA-256 recorded by the candidate:** `27895f457975d52c726bdf037b3e82f46bacaf0160fb857c54078aee2774e987`
- **Review branch:** `review/issue-17-defect4-independent-gpt56`

The live candidate branch was resolved before review. Comparing
`96fc7ec34bd3b685a0edeae7ecd4404abab7e2f1` with
`issue-17/defect-4-staircase` returned `identical`, with zero commits ahead and
zero behind. There are therefore no later candidate-branch changes to separate
from this review.

This review covers exactly the following claim at that commit:

> Let `F=(P,Q)` be a polynomial pair over `C` with `J(P,Q)=1`, and let
> `w=(p,q)` be a primitive positive weight. If
> `kappa_w=deg_w(P)+deg_w(Q)-p-q <= 4`, then `F` is a polynomial
> automorphism.

It does **not** assert the full planar Jacobian conjecture, does not treat defect
five, and does not prove that every Keller pair admits a positive weight of
defect at most four.

The candidate proof files were not edited. This branch adds only reviewer-owned
records and an independently implemented checker.

## 2. Disposition

`ACCEPT`

Every load-bearing mathematical predicate in the declared theorem was
reconstructed and checked. No false statement, omitted weight, omitted
orientation, invalid descent, circular induction, or full-staircase formal
countermodel was found.

One literal statement requires an explicit qualification: an arbitrary target
scaling does **not** preserve `J=1` by itself. If `D(u,v)=(u,c v)`, then
`J(D o F)=c J(F)`. The candidate does not rely on the false blanket statement;
it uses this scaling only together with a graded source inverse of Jacobian
`1/c`, so the combined normalization has Jacobian one. All target swaps and
shears actually used by the proof have determinant one.

## 3. Reconstruction artifacts

The full independent derivation is split only for transport/readability:

- `governance/reviews/issue-17-defect4-independent-reconstruction-a.md` — Rees identity, resonant classification, normalization, common powers, endpoints, root-degree sieve, and defects zero through three.
- `governance/reviews/issue-17-defect4-independent-reconstruction-b.md` — complete defect-four exhaustion and inductive closure.
- `governance/reviews/issue-17-defect4-independent-case-table.md` — reviewer-selected root-degree case table.

## 7. Comparison with the candidate after reconstruction

The independent derivation agrees with the candidate on every load-bearing
formula and disposition:

- exact Rees exponent, signs, zero layers, and resonant constants;
- degree multiset `{p,q}` and triangular/linear graded classification;
- retained resonant scalar and compensated normalization;
- common-power lemma and exact full-top descent;
- endpoint coordinate argument;
- every defect-zero-through-three orientation and support exception;
- defect-four positions `(1,3)`, `(2,2)`, `(3,1)`;
- exceptional weights `(1,2)` and `(2,3)`;
- reliance on earlier stairs rather than the central equation alone;
- strong induction and inversion of all normalizations.

The candidate's prior review record correctly remained `BLOCK` solely because
the constructor was also its reviewer. No mathematical blocker recorded there
was carried forward by assumption; the formulas were recomputed here.

## 8. Independent symbolic validation

Reviewer checker:

```text
scripts/review_validate_defect4_independent.py
```

It generates weighted supports and formal staircase systems from definitions;
it does not import the candidate checker or a copied case allowlist. For every
no-descent system it generates `S_0,...,S_(kappa-1)` and uses an auxiliary
saturation variable to impose nonzero top coefficients and resonant scalar.
A unit Groebner basis certifies that the generated formal system has no complex
solution. The bounded generation is regression evidence only; the unbounded
closure is the root-degree argument above.

Commands run:

```text
python3 -m py_compile scripts/review_validate_defect4_independent.py
python3 scripts/review_validate_defect4_independent.py
```

Observed output:

```text
review mode: independent-review
reviewed candidate: 96fc7ec34bd3b685a0edeae7ecd4404abab7e2f1
exact assertions: 7361
semantic mutations detected: 8
random exact Rees/Keller trials: 36
primitive weights enumerated (1 <= p <= q <= 80): 1966
generated no-descent formal systems: 317
projective common-root charts eliminated: 319
largest generated system: 6 equations, 10 variables
random exceptional coefficient trials: 800
independent defect-four symbolic validation: PASS
mathematical authority: HUMAN-READABLE REVIEW, NOT CHECK COUNT
```

## 9. Assertions checked

| Candidate assertion | Review result |
|---|---|
| Rees exponent, determinant signs, `kappa>=0` | verified directly |
| Every lower/resonant/upper staircase statement, including zero layers | verified directly |
| Resonant brackets are constants and at least one is nonzero | verified directly |
| Constant-bracket homogeneous pair has degrees `{p,q}` | verified directly |
| Unequal-weight triangular and equal-weight linear classification | verified directly |
| Graded inverse preserves the filtration | verified directly and symbolically |
| Resonant scalar is retained | verified |
| Source normalization plus target compensation preserves `J=1` | verified |
| Target swap, shear, and triangular maps preserve `J=1` | verified |
| Arbitrary target scaling alone preserves `J=1` | falsified as a blanket statement; candidate uses only valid compensation |
| Other staircase terms survive normalization | verified by graded covariance |
| Common-power lemma in the UFD | verified without a closed-polynomial theorem |
| Complete-top cancellation and strict actual-defect descent | verified |
| Endpoint top component is a full polynomial coordinate | verified in both weight regimes and orientations |
| Defects zero through three | independently reconstructed |
| Defect four, all three interior positions | independently reconstructed |
| Exceptional `(1,2)` coefficient systems | independently recomputed |
| Exceptional `(2,3)` support system | independently recomputed |
| Multiple resonant terms and missing layers | verified |
| Same positive weight and smaller nonnegative integer after descent | verified |
| Induction is noncircular and normalizations can be inverted | verified |
| Claim-ledger/proof-graph scope excludes `JC_2` | verified |
| Source audit is non-load-bearing | verified; no external theorem is consumed by the proof |

## 10. Countermodels and corruptions attempted

1. **Wrong Jacobian sign:** replaced `f_xg_y-f_yg_x` by a plus sign; detected.
2. **Wrong Rees exponent:** shifted the exponent by one; detected.
3. **Unsigned target swap:** `(P,Q)->(Q,P)` changes the Jacobian sign; detected.
4. **Uncompensated target scaling:** changes `J=1` to `J=c`; detected.
5. **Partial top cancellation:** leaves the original weighted degree unchanged;
   rejected as a descent certificate.
6. **Central-only false model:** at weight `(1,2)`,

   ```text
   P_0=2x^3, Q_0=5x^4, P_1=7y, Q_1=(6/7)x^3,
   P_2=x, Q_2=3y
   ```

   has `S_0=S_2=0` but `S_1=-140x^3`; the earlier stair rejects it.
7. **Middle-Wronskian sign reversal:** changes the exceptional central system;
   detected.
8. **Omitted `xy` support at `(3,1),(1,2)`:** removes the decisive variable
   from a corrupted model; the complete support generator detects the omission.
9. **Missing `P_2` or `Q_2`:** the decisive `c v y` coefficient remains.
10. **Random exact coefficients:** 800 assignments were tested in both
    exceptional systems; none satisfied the full earlier-stair equations with
    nonzero top data.
11. **Generated formal systems:** 317 no-descent systems, represented by 319
    projective common-root charts over all 1,966 primitive weights
    `1<=p<=q<=80`, were generated from supports and eliminated exactly.
12. **Random exact Keller pairs:** 36 determinant-one shear compositions were
    tested against the full Rees identity, resonance, and above-resonance
    vanishing for independently sampled primitive weights.

No full-staircase countermodel survived.

## 11. Source audit and prior record

The proof is self-contained. The listed Shaska, Lee--Li, Karas, Pan, and Su
papers were checked only for the candidate's stated contextual boundaries. No
external graded-Keller, Newton, monodromy, local-nilpotence, or
completion-valued Hamiltonian theorem is used in the reconstruction.

The prior exact-byte review accurately identifies the same candidate manifest
and states a `BLOCK` whose smallest blocker is reviewer independence. This
independent review removes that blocker for the scoped theorem only.

## 12. Proposed claim-ledger and proof-graph delta

A separate reviewer proposal is recorded in
`governance/reviews/issue-17-defect4-independent-claim-graph-delta.md`.
It proposes promotion of `CLM-047` through `CLM-052` and `OPEN-DEFECT-4` only
after the repository's freeze/integration procedure. No ledger, graph, mainline,
tag, or candidate proof was changed by this review.

## 13. Remaining non-load-bearing risks

- The independent checker is bounded and cannot replace the unbounded proof.
- The inherited whole-repository validator was not required for, and does not
  confer, mathematical authority on this isolated theorem review.
- The source-audit papers remain context only; a future change that makes one a
  premise would require a new source-bound review.
- Acceptance does not itself perform promotion, freeze, merge, tagging, or
  issue closure.

These risks do not block the exact defect-at-most-four theorem at the reviewed
commit.
