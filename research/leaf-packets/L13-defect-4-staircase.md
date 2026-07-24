# Filtered Rees Defect-4 Staircase

- **Priority:** `P0`
- **Status:** `REVIEWED_SCOPED`
- **Issue:** [#17](https://github.com/snissn/planar-jacobian/issues/17)
- **Dependencies:** CLM-047–CLM-051, CLM-060
- **Authority:** `REVIEWED_SCOPED` for the exact theorem at the pinned revision; all broader inferences remain `MUTABLE_NONAUTHORITATIVE`
- **Historical baseline:** `86d1b78cedd788b7335be692f9bb92921142c7d3`
- **Reviewed candidate revision:** `96fc7ec34bd3b685a0edeae7ecd4404abab7e2f1`
- **Independent review:** [`../../governance/reviews/issue-17-defect4-independent-gpt56.md`](../../governance/reviews/issue-17-defect4-independent-gpt56.md), disposition `ACCEPT`
- **Freeze record:** [`../../governance/reviews/issue-17-defect4-mainline-freeze.md`](../../governance/reviews/issue-17-defect4-mainline-freeze.md)

## Load-bearing question

For a positive primitive source weight `w=(p,q)`, resolve

```text
kappa_w=deg_w(P)+deg_w(Q)-p-q=4.
```

**Reviewed scoped disposition:** every defect-four pair either has a top-coordinate resonance, admits an exact triangular/linear target operation that strictly lowers `kappa_w`, or violates an earlier staircase equation. Combined with the independently rederived lower-defect cases, this gives the reviewed theorem `kappa_w<=4 => F is an automorphism` at the pinned candidate revision.

## Required independent recomputation

Completed in [`../audits/defect-4-staircase-audit.md`](../audits/defect-4-staircase-audit.md):

1. The chain rule gives `J(Pcal,Qcal)=t^kappa` with no sign change.
2. Every coefficient equation is derived from `sum_(i+j=n)J(P_i,Q_j)=delta_(n,kappa)`.
3. Brackets above the resonant stair vanish individually by negative weighted degree.
4. The candidate `kappa<=3` proof is rederived for both orientations and all positive primitive weights.
5. The resonant two-variable graded pair is classified directly; Shaska's theorem is context rather than a hidden dependency.

## Case table

The complete case table is [`../audits/defect-4-case-table.md`](../audits/defect-4-case-table.md). It covers:

```text
(1,3), (2,2), (3,1),
```

including equal weights, unequal weights, source-weight swap, reversed resonant degree orientation, absent intermediate layers, common-power exponents, and every transformation used.

The central exceptional weight `(1,2)` is governed by

```text
3af=4bv,
J(P_1,Q_1)=(2uf-3ve)x^2-vfy,
3ac+2uf-3ve=0,
vf=0,
```

which is inconsistent because `a,b,c` are nonzero.

## Central obstruction

After normalizing `(P_2,Q_2)=(x,cy)`, the exact equation is

```text
c(P_0)_x+J(P_1,Q_1)+(Q_0)_y=0.
```

In a no-descent unequal-weight case, a zero middle Wronskian forces `H|H_x` for the top common factor and is impossible. A nonzero Wronskian forces both middle layers to exist. Their weighted supports reduce to `(p,q)=(2,3)`, which violates `J(P_0,Q_0)=0`, or to `p=1`; the latter is eliminated by `S_1` except for `(1,2)`, where the displayed coefficient system is inconsistent.

The Wronskian is not claimed to be universally removable by target or source normal form. Same-index target `SL_2` changes preserve it, and graded symplectic source changes pull it back. The full staircase, rather than a standalone normal-form theorem, closes the case.

## Accepted evidence

The maintained evidence is exact symbolic algebra plus a human-readable unbounded proof. [`../../scripts/validate_defect4_staircase.py`](../../scripts/validate_defect4_staircase.py) recomputes exceptional identities, support arithmetic, and mutation controls. Its output is process evidence only.

An independent reviewer reconstructed the load-bearing proof and returned `ACCEPT` for the exact candidate revision. Validator counts remain process evidence; authority is carried by the bound review and freeze record.

## Forbidden shortcuts

- Do not cite the old conversation derivation as authority; use the maintained audit.
- Do not infer polynomial dependence from generic algebraic dependence without the weighted common-power proof.
- Do not use a transformation without its exact Jacobian and strict-descent calculation.
- Do not use the retired boundary-excess identity.
- Do not infer a global cyclic extension from a Kummer model on one generic fiber.
- Do not infer principalization from exactness of a differential form.
- Do not infer a global deck action from multiple sheets.
- Do not broaden this reviewed scope to defect `5`, existence of a qualifying weight for every Keller map, or `JC_2`.

## Required artifacts

Completed candidate artifacts:

- [`../audits/defect-4-staircase-audit.md`](../audits/defect-4-staircase-audit.md)
- [`../audits/defect-4-case-table.md`](../audits/defect-4-case-table.md)
- [`../audits/filtered-transformation-catalogue.md`](../audits/filtered-transformation-catalogue.md)
- [`../audits/defect-4-primary-source-audit.md`](../audits/defect-4-primary-source-audit.md)
- synchronized claim ledger, proof graph, queue disposition, track, and status files
- exact-byte construction review and independent `ACCEPT` under `governance/reviews/`
- mainline freeze record binding the reviewed revision and protected scientific paths

## Stop rule

The mathematical stop rule is reached under disposition **1**, full defect-four reduction, and the independent review gate is satisfied at the pinned revision. Issue #17 may close after verified mainline synchronization. Any defect-five work requires a separate issue-local packet and review scope.

No scoped result in this packet is a proof of `JC_2`.

## Handoff

- **Base commit:** `86d1b78cedd788b7335be692f9bb92921142c7d3`.
- **Candidate branch:** `issue-17/defect-4-staircase`.
- **Exact equations:** Rees identity and `S_0` through `S_4` are in the main audit.
- **Transformations:** only compensated graded source normalization, determinant-one swaps/shears, and exact triangular target top cancellation.
- **Descent:** strict decrease of the nonnegative integer `kappa_w`.
- **Countermodels attempted:** central-only cancellations fail the preceding stair; no polynomial weighted layer system survives all required stairs.
- **Surviving resonance cases:** none at defect four after top descent and endpoint-coordinate cases.
- **Review result:** independent `ACCEPT` bound to `96fc7ec34bd3b685a0edeae7ecd4404abab7e2f1`; see the reconstruction, case table, and freeze record.
- **Editorial synchronization:** current-main IDs and navigation may change without changing the reviewed mathematics.
- **Next scientific scope:** none in this packet. Defect `5` or a theorem producing a qualifying weight is separate work.
