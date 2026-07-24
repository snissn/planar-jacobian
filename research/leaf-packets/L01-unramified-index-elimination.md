# Generic Unramified Index Elimination

- **Priority:** historical `P0`
- **Status:** `DISPOSED — SCOPED_ALGEBRAIC_OBSTRUCTION`
- **Dependencies:** `CLM-029`, `CLM-030`, `CLM-031`, `CLM-058`
- **Authority:** `MUTABLE_NONAUTHORITATIVE`
- **Issue:** [#3](https://github.com/snissn/planar-jacobian/issues/3)
- **Successor:** [`L14-keller-index-form-unit.md`](L14-keller-index-form-unit.md)

## Load-bearing question

Could ramified-prime adaptation plus generic algebraic arguments eliminate every accidental index divisor in the finite étale locus?

## Accepted evidence

The issue #3 packet establishes, at mutable candidate scope, simultaneous generation at any prescribed finite set of height-one base primes, the `R1/S2` globalization implication, and the noncircular degree-one implication after global monogenicity. It also supplies an explicit smooth rational finite-flat rank-three countermodel showing that local monogenicity, tame squarefree branch, a fixed unramified sheet, and an open affine plane do not force a global power basis.

## Forbidden shortcuts

Do not replace integral generation by field primitivity, test primes of the normalization separately instead of the whole semilocal algebra over one base prime, rely on generic fiber separation or parameter counts, or use class-group triviality as if a principal index divisor were empty.

## Required artifacts

The theorem, collision, countermodel, source-audit, adversarial-review, provenance, and handoff files are preserved under [`../issues/issue-3-unramified-index/`](../issues/issue-3-unramified-index/README.md). The detailed maintained track is [`../tracks/monogenicity-index-divisor.md`](../tracks/monogenicity-index-divisor.md).

## Stop rule

Reached. `CLM-058` disposes the generic algebraic bridge at exact scope. No further work should repeat that bridge without a strictly stronger Keller-specific hypothesis.

## Handoff

Continue only through `L14`: use étaleness of the specified Keller source and its open immersion in the normalization to force the universal index form to represent a nonzero constant.
