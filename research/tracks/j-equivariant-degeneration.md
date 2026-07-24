# Track J — Equivariant Degeneration

> Status: `MUTABLE_NONAUTHORITATIVE`

The three-dimensional example shows how a residual torus can organize a nonproper étale cover. In the plane, exact nontrivial `G_m`-equivariance is source-bound to Shaska's arXiv:2607.20210 and forces a Keller map to be an automorphism for every sign pattern of the weights.

The unresolved global problem is therefore not exact symmetry but **no-escape passage from a general map to a controlled graded representative**.

## Two degeneration scales

### Coefficient-space closed orbit

A torus limit of a bounded-degree Keller map can become an automorphism, lower function-field degree, or discard a boundary valuation. A useful degeneration must remain inside a stratum with fixed:

- function-field degree;
- boundary dual graph;
- valuation key sequences;
- ramification and inertia data.

### Weighted Rees staircase

Track [`m-filtered-equivariance.md`](m-filtered-equivariance.md) fixes a positive source weight and retains all weighted layers in a Rees family. Issue #17 now supplies a self-contained theorem candidate that every positive-weight pair with `kappa_w<=4` is an automorphism. The middle Wronskian at defect four is eliminated by exact earlier-stair equations and weighted support, not by a no-escape theorem.

This result is still `candidate_proved` pending independent review, and it does not address weights of defect at least five.

## Missing no-escape/bounded-defect theorem

A full route now needs a well-founded invariant or geometric theorem that does at least one of the following:

1. produces a primitive positive weight with `kappa_w<=4` for a minimal counterexample;
2. lowers arbitrary positive-weight defect into the proved domain;
3. proves a coefficient-space torus limit remains in a stratum with fixed degree and boundary data.

Any transformation must preserve `J(P,Q)=1`, lower the declared invariant, avoid deleting boundary valuations or generic sheets, and terminate. The issue-17 target shears meet those requirements only once the pair is already inside the small-defect staircase.

## Exit

This track exits through either:

- a proof that a minimal counterexample has a closed torus orbit inside a fixed boundary stratum;
- a no-escape reduction into an independently accepted `kappa_w<=4` positive-weight pair; or
- a terminating higher-defect staircase reduction with the same degree and boundary controls.

The defect-four candidate is scoped support, not a proof of any global exit statement.
