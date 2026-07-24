# Keller Index-Form Unit

- **Priority:** `P0`
- **Status:** `OPEN`
- **Dependencies:** `CLM-029`, `CLM-030`, `CLM-031`, `CLM-034`, `CLM-058`, `CLM-059`
- **Authority:** `MUTABLE_NONAUTHORITATIVE`
- **Issue:** [#3](https://github.com/snissn/planar-jacobian/issues/3)

## Load-bearing question

For the actual Keller normalization, prove that the universal index form represents a nonzero constant, equivalently construct an integral primitive element whose index ideal is the unit ideal.

## Accepted evidence

A successful result may provide a Keller-specific support theorem forcing every sheet-difference zero into intrinsic ramification, an integral primitive element with unit Fitting index, an affine-transition theorem proved on the full base, or a restricted exact theorem such as the rank-three binary-cubic unit-representation case.

## Forbidden shortcuts

Local monogenicity, generic separation, dimension counts, rationality, smoothness, fixed-sheet monodromy, squarefree branch, or the existence of an open affine plane do not substitute for the unit equation. Adding a base element to a primitive element changes no sheet difference.

## Required artifacts

State the normalization and source-open hypotheses exactly; give the universal index determinant or Fitting ideal; identify every codimension-one support component; consume source étaleness explicitly; and include mutations against the issue #3 countermodels. Reuse the banked packet under [`../issues/issue-3-unramified-index/`](../issues/issue-3-unramified-index/README.md).

## Stop rule

Stop when the Keller-specific unit-index statement is proved at exact scope, or when a strictly stronger Keller-near countermodel identifies a smaller missing hypothesis. Do not reopen the already falsified generic bridge.

## Handoff

Begin with rank three. After trace splitting, study the intrinsic binary cubic `s -> det(1,s,s^2)` on the trace-zero rank-two bundle and determine whether Keller-source étaleness forces a global section on which it is a unit.
