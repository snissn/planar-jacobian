# Finite Stable Differential Order

- **Priority:** `P0`
- **Status:** `OPEN — SOURCE-POLE CONSTRUCTION CLASS OBSTRUCTED`
- **Dependencies:** CLM-010–CLM-013, CLM-061
- **Authority:** `MUTABLE_NONAUTHORITATIVE`
- **Protocol verdict:** `null`

## Load-bearing question

Construct a finite full `B=C[P,Q]`-lattice `M subset L=C(x,y)` invariant under both `D_P` and `D_Q`.

The source-reflexive-lattice successor proves that multiplicative closure need not be imposed on `M`: its reflexive multiplier ring

```text
O_M^ref = ({z in L : zM subset M})**
```

is a finite locally free stable `B`-order with total quotient field `L`. Therefore one finite full pair-stable module would enter the predecessor trace/discriminant route and force degree one.

## Current disposition

The predecessor packet proves at mutable candidate scope:

```text
finite locally free stable order
  => derivative-stable trace discriminant
  => unit discriminant
  => finite etale connected cover of A^2_C
  => degree one.
```

The successor packet sharpens the existence boundary:

1. for one derivation, a finite full stable lattice exists exactly when that derivation is logarithmic along every reduced ramified divisor;
2. a finite full lattice stable under both canonical translations exists exactly when the finite normalization has no height-one ramification;
3. the intrinsic local spectrum is the value-group quotient `(1/e)Z/Z`, with residue-degree multiplicity;
4. at `h(P,Q)=0`, the two spectra are the same scalar classes multiplied by the normal covector `(h_P,h_Q)`; a normal/tangent frame gives `(j/e,0)`, so commutativity supplies no cancellation;
5. the source algebra is the directed union of finite reflexive divisorial pole modules, but every ramified finite stage escapes, and every positive pole stage at an unramified omitted divisor escapes under a transverse member of the frame;
6. the multiplier-ring construction converts any hypothetical stable module into the required stable order.

The canonical-differential-saturation successor sharpens the same wall without
claiming a construction:

1. finite differential saturation of any finite full seed excludes
   height-one ramification (`CLM-079`);
2. saturation of the normalization is finite exactly when the finite
   normalization is unramified in codimension one (`CLM-080`);
3. every divisorial source boundary lies over a height-one target divisor,
   ramified pole stages escape, and an unramified stage containing an actual
   positive pole also escapes (`CLM-081`);
4. generic height-one ordinary coherence of the full permutation connection
   is equivalent to trivial local inertia (`CLM-082`);
5. regular holonomicity and logarithmic coherence do not imply ordinary
   structure-sheaf finiteness (`CLM-083`);
6. the surviving source-character exclusion is `CLM-084`; and
7. dual, canonical, full-intersection, jet, cohomological, and automatic
   multiplier shortcuts are disposed only at the declared construction-class
   scope (`CLM-085`).

Thus multiplicative closure is no longer the missing bridge. The unresolved step is finite-stage pair stability itself. No finite pair-stable lattice is constructed, and no planar Jacobian-conjecture conclusion is claimed.

## Accepted evidence

A successful construction requires all of:

- a finite-generation proof inside one fixed finite `B`-module;
- fullness: `M tensor_B K=L`;
- exact invariance under both canonical translations;
- a proof that the multiplier ring is finite, has total quotient field `L`, remains stable, and becomes locally free after reflexive closure;
- local bases or finite presentations and both derivation matrices;
- mutations detecting ramified, unramified-nonproper, logarithmic, and infinite-union failures.

A valid obstruction disposition must name a precise construction class and prove the obstruction for every member. The integrated successor does this for coherent divisorial source-pole stages, fixed conductor/different shifts, their reflexive hulls, and finite intersections. It does not rule out every conceivable finite non-divisorial construction.

## Forbidden shortcuts

- Do not use an infinite union of pole-order lattices as a finite module.
- Do not invoke Noetherian stabilization until all iterates lie in one fixed finite ambient module.
- Do not assume logarithmic stability implies exact translation stability.
- Do not require the initial module to be an algebra; derive and audit its multiplier order instead.
- Do not present a trace dual, inverse different, canonical module, or divisorial twist as stable merely because it is coherent or reflexive.
- Do not cancel residue representatives by integer shifts; work modulo `Z` and retain the full tame-character multiset.
- Do not infer that `dP wedge dQ=dx wedge dy` or an exact primitive removes higher poles.
- Do not assume finite etaleness, degree one, or finiteness of `C[x,y]` over `B` while constructing the lattice.

## Required artifacts

A construction must include the finite full module, both derivation matrices, the multiplier order, local-freeness and total-quotient-field proofs, discriminant control, and failure mutations. An obstruction must include the exact local spectrum, source-pole filtration, class coverage, countercontrols, and a declared review.

Current artifact set:

```text
research/issue-4/stable-differential-order/MAIN.md
research/issue-4/stable-differential-order/local-dvr-obstruction.md
research/issue-4/stable-differential-order/construction-audit.md
research/issue-4/stable-differential-order/source-bindings.md
research/issue-4/stable-differential-order/adversarial-review.md
research/issue-4/stable-differential-order/HANDOFF.md
research/issues/source-reflexive-lattice/README.md
research/issues/source-reflexive-lattice/LOCAL_RESIDUE_THEOREM.md
research/issues/source-reflexive-lattice/TWO_DERIVATION_SPECTRUM.md
research/issues/source-reflexive-lattice/SOURCE_POLE_FILTRATION.md
research/issues/source-reflexive-lattice/MULTIPLIER_RING.md
research/issues/source-reflexive-lattice/CANDIDATE_LATTICE_TABLE.md
research/issues/source-reflexive-lattice/COUNTERMODELS.md
research/issues/source-reflexive-lattice/REVIEW.md
research/issues/source-reflexive-lattice/HANDOFF.md
research/issues/canonical-differential-saturation/README.md
research/issues/canonical-differential-saturation/DIFFERENTIAL_SATURATION.md
research/issues/canonical-differential-saturation/DMODULE_ROUTE.md
research/issues/canonical-differential-saturation/LOGARITHMIC_LATTICES.md
research/issues/canonical-differential-saturation/LOCAL_RESIDUES.md
research/issues/canonical-differential-saturation/CONSTRUCTION_TABLE.md
research/issues/canonical-differential-saturation/COUNTERMODELS.md
research/issues/canonical-differential-saturation/SOURCE_AUDIT.md
research/issues/canonical-differential-saturation/REVIEW.md
research/issues/canonical-differential-saturation/HANDOFF.md
```

## Stop rule

Stop when either:

1. one finite full pair-stable module and its reflexive multiplier order are constructed and independently reviewed; or
2. a strictly larger, explicitly declared finite construction class is excluded by an independently reviewed obstruction.

The integrated packet reaches a class-level obstruction for divisorial source-pole constructions under a declared `local-adversarial-review`. Promotion remains blocked because the review is not independent. The leaf remains open.

## Handoff

Prove the source-character exclusion in `CLM-084`: at every ramified
height-one boundary valuation, rule out nontrivial inertia characters using
the actual polynomial source algebra and both canonical translations. A
direct D-module substitute must separately provide global ordinary coherence,
preservation by both unscaled translations, and a torsion-free meromorphic
embedding with generic fiber `L`. A finite non-divisorial module remains a
valid construction target only if all iterates stay in one exhibited finite
full ambient `B`-module.
