# Planar Jacobian Research Program

> **Authority:** `MUTABLE_NONAUTHORITATIVE` program map. Individual reviewed scope is recorded in the claim ledger and review records.

## Common problem spine

Fix a polynomial Keller map `F=(P,Q): A2_C -> A2_C` with nonzero constant Jacobian. Let `B=C[P,Q]`, `K=Frac(B)`, `L=C(x,y)`, and let `Y` be the normalization of `Spec(B)` in `L`. The main goal remains to prove `[L:K]=1`, equivalently that `F` is a polynomial automorphism.

The maintained program separates:

1. the finite normalization and its boundary/ramification;
2. canonical derivations and exact symplectic structure;
3. monogenicity and index divisors;
4. stable differential orders;
5. logarithmic and radial fields;
6. quasi-Albanese and Gauss–Manin finiteness;
7. graded, filtered, and equivariant reductions;
8. monodromy and boundary topology;
9. primary-source and low-degree controls; and
10. characteristic-p experiments.

## Current high-priority frontier

### `L14` — Keller index-form unit, issue #3

The generic unramified-index bridge is false. `CLM-058` gives a scoped smooth rational finite-flat countermodel, while `CLM-029`, `CLM-031`, and `CLM-034` bank ramified adaptation and conditional globalization. The successor must consume source étaleness and the specified open immersion `A2_source -> Y` to force the universal index form to represent a unit.

### `L02` — finite stable differential order, issue #4

`CLM-011` and `CLM-013` give the exact conditional discriminant implication at mutable candidate scope. The ramified-DVR packet proves a transverse derivation preserves no full finite lattice at a ramified valuation. Existence of a finite locally free order stable under both canonical translations remains open as `CLM-061`.

### `L03` — integrable logarithmic lift, issue #5

`CLM-052–056` record the monogenic lift formula, logarithmic tangency criterion, radial-line criterion, logarithmic-field characterization, and integration obstruction. `CLM-057` is the surviving bridge. The actual Keller branch is not proved radial; regularity, zero residue, or a branch Hamiltonian does not imply a locally finite algebraic action.

### Reviewed defect-four disposition

`CLM-047–051` and `CLM-060` are `reviewed_scoped` under the independent review and freeze records. They prove only:

```text
primitive positive weight w and kappa_w <= 4
  => the planar Keller pair is a polynomial automorphism.
```

They do not show that every Keller pair admits such a weight, do not treat defect five, and do not establish `JC_2`. `L13` is a reviewed disposition, not an active leaf and not a terminal graph node.

## Maintained tracks

- [`tracks/a-normalization-boundary.md`](tracks/a-normalization-boundary.md) — finite normalization, class group, canonical divisor, and boundary baseline.
- [`tracks/b-canonical-derivations.md`](tracks/b-canonical-derivations.md) — canonical fields, logarithmic tangency, and integration.
- [`tracks/c-monogenicity-index-divisor.md`](tracks/c-monogenicity-index-divisor.md) and [`tracks/monogenicity-index-divisor.md`](tracks/monogenicity-index-divisor.md) — global monogenicity, collision divisors, countermodels, and Keller successor.
- [`tracks/d-stable-differential-lattice.md`](tracks/d-stable-differential-lattice.md) — stable-order implication and local obstruction.
- [`tracks/e-quasi-albanese-log-geometry.md`](tracks/e-quasi-albanese-log-geometry.md) — intrinsic torus geometry.
- [`tracks/f-gauss-manin-generic-fibers.md`](tracks/f-gauss-manin-generic-fibers.md) — punctures and Gauss–Manin modules.
- [`tracks/g-wright-graded-single-tree.md`](tracks/g-wright-graded-single-tree.md) — graded one-boundary rigidity.
- [`tracks/h-monodromy-galois-braid.md`](tracks/h-monodromy-galois-braid.md) — inertia, fixed sheets, cusps, and braid monodromy.
- [`tracks/i-exact-symplectic.md`](tracks/i-exact-symplectic.md) — exact one-forms, residues, and principal parts.
- [`tracks/j-equivariant-degeneration.md`](tracks/j-equivariant-degeneration.md) — exact equivariance and no-escape degeneration.
- [`tracks/k-characteristic-p.md`](tracks/k-characteristic-p.md) — reduction and p-curvature experiments.
- [`tracks/l-literature-low-degree.md`](tracks/l-literature-low-degree.md) — primary-source and numerical frontier control.
- [`tracks/m-filtered-equivariance.md`](tracks/m-filtered-equivariance.md) — reviewed positive-weight defect-at-most-four staircase.
- [`tracks/0-three-dimensional-context.md`](tracks/0-three-dimensional-context.md) — three-dimensional marked-root mechanism as idea input only.

## Cross-track interfaces

A successful bridge must eventually control at least one global obstruction:

- finiteness/properness of the original source over the target;
- all height-one support of an index or conductor module;
- logarithmic tangency plus algebraic integration preserving the source open;
- degree and boundary type under a degeneration;
- monodromy/inertia strong enough to force one sheet; or
- a filtration-compatible descent that terminates for an arbitrary Keller pair.

A formal local identity, exact symbolic computation, or reviewed bounded theorem remains bounded until the graph records the additional global edge.

## Coordination and exit rules

The active queue and dispositions are generated in [`WORK_QUEUE.md`](WORK_QUEUE.md). Issue [#2](https://github.com/snissn/planar-jacobian/issues/2) coordinates the program. Every new task starts from the latest `main`, reserves an issue-owned path, uses issue-local labels, and defers shared synchronization to the final step.

A leaf exits when its declared stop rule yields a reviewed theorem, a rigorous obstruction, a counterexample to the maintained bridge, a finite audited classification, or a smaller successor leaf. Restricted results remain restricted.
