# Independent Review Disposition — Fixed-Weight Defect Five

> **Review mode:** `independent-review`  
> **Reviewer:** GPT-5.6 Pro  
> **Role:** `reviewer`  
> **Task issue:** `#38`  
> **Owned path:** `research/issues/defect-5-independent-review/`  
> **Reviewed candidate:** `2eeb36d232366d124b5a66774b29769ec1eba43d`  
> **Disposition:** **ACCEPT for the exact fixed-weight defect-five statement**  
> **Branch authority:** `MUTABLE_NONAUTHORITATIVE` until serialized integration

## 1. Exact disposition

**ACCEPT.** For a planar polynomial Keller pair over `C` and a fixed primitive
positive weight `w`, actual grading defect `kappa_w=5` implies that the pair is a
polynomial automorphism. A nonzero resonant endpoint is directly invertible.
Every interior resonant system either has a determinant-one complete-top shear
that strictly lowers the actual nonnegative integer defect to at most four, or
contradicts the complete weighted Rees staircase.

This is disposition **1** from issue #38. No narrower subclass, corrected theorem
statement, case-table change, or formal weighted-layer counterexample is needed.

## 2. Load-bearing findings

| Requirement | Independent result |
|---|---|
| Rees identity and `S_0,...,S_5` | verified from the chain rule, with signs and zero layers |
| Above-resonance vanishing | verified individually from weighted degree |
| Constant-bracket homogeneous classification | verified; degree multiset is `{p,q}` |
| Scalar-retaining normalization | verified, including determinant compensation and covariance |
| Common-power lemma | verified in the UFD with characteristic-zero and homogeneity hypotheses |
| Maximal common-root convention | verified; `H` may itself be a proper polynomial power |
| Complete-top descent | verified; entire top layer cancels with no same-weight replacement |
| Endpoints | verified in both orientations and weight orders |
| Four interior positions | exhausted independently |
| Equal weights | both new defect-five systems reconstructed and eliminated |
| Unequal weights | unbounded family sieve reconstructed and every exception checked |
| `p=1`, `(3,2)`, `rho=2`, `4|q` | explicitly checked and excluded |
| Missing layers | treated as literal zero supports |
| Simultaneous resonances | retained with exact scalar equations |
| Formal countermodels | none survived exact saturation |
| Source/target swaps and inverses | verified |

## 3. Non-load-bearing regression defect

The later constructing-agent adversarial checker uses `Q_0=B x^2` instead of
`B x^3` in the `(2,3)` position at weight `(2,3)`. This is an exact bug in that
checker, but it does not occur in the pinned human candidate, the candidate case
table, or the construction checker. The reviewer-owned checker detects the
corruption and eliminates the correct system. The review disposition therefore
remains `ACCEPT`; a separate engineering correction may repair the old checker
without changing scientific status.

## 4. Dependency and scope

After strict descent, the proof invokes only the independently reviewed theorem
that fixed primitive positive weight and defect at most four imply automorphy.
The review does not infer a qualifying weight for an arbitrary Keller pair.

Specifically, this acceptance does not establish:

- defect-six closure;
- arbitrary filtered-descent termination;
- the existence of any bounded-defect weight for every Keller pair;
- `JC_2`;
- a higher-dimensional analogue.

## 5. Residual risks

- The symbolic scan is bounded and is not the proof of unbounded support
  completeness; the human divisibility argument is load-bearing.
- Gröbner calculations are regression and falsification evidence, not a
  substitute for the displayed hand contradictions.
- Promotion, freeze, shared-ledger edits, issue closure, and mainline authority
  require a separate integration maintainer.

No residual risk names a surviving mathematical case or blocks the exact
reviewed statement.

## 6. Candidate immutability

No candidate proof file was modified. This review PR contains only reviewer-owned
artifacts and its manifest. It proposes shared synchronization in `HANDOFF.md`
and `INTEGRATION.json` but performs none.
