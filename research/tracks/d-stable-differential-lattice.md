# Track D — Stable Differential Lattice

> **Status:** `MUTABLE_NONAUTHORITATIVE`  
> **Protocol verdict:** `null`

Seek a finite full `B=C[P,Q]`-module `M subset L=C(x,y)` preserved by both canonical derivations `D_P,D_Q`. The source-reflexive-lattice successor proves that an algebra structure on `M` is not an additional hypothesis: the reflexive multiplier ring of any such module is a finite locally free stable `B`-order with total quotient field `L`.

## Audited implication

The predecessor issue #4 packet proves at mutable candidate scope:

1. in a local basis `e` of a finite locally free stable order, write `D(e)=eA`;
2. for the trace Gram matrix `G`,

   ```text
   delta(G)=A^T G+GA;
   ```

3. hence

   ```text
   delta(det G)=2 Tr(A)det G;
   ```

4. the trace-discriminant ideal is stable under `partial_P,partial_Q`;
5. every nonzero ideal of `C[P,Q]` stable under both partials is the unit ideal;
6. the order is finite etale and connected over `A^2_C`;
7. the function-field degree is one.

The successor supplies the module-to-order bridge. For a finite full stable module,

```text
O_M = {z in L : zM subset M}
```

is finite, stable, and generically `L`; its `B`-reflexive hull is an intersection of height-one localized rings and is locally free over the regular surface `B`. Therefore one finite full pair-stable module is sufficient for the audited implication.

## Sharp codimension-one theorem

For a fixed base derivation `delta`, a finite full stable lattice exists exactly when `delta` is logarithmic along every reduced ramified base divisor; in that case the normalization itself is stable.

For the pair `D_P,D_Q`, at least one member is transverse to every irreducible target divisor. Consequently:

```text
finite full pair-stable B-lattice
  <=> no height-one ramification in the finite normalization.
```

The right side is the full unramified DVR condition, including separable residue extension, not merely the numerical equation `e=1`.

## Canonical saturation and ordinary-coherence wall

The canonical-differential-saturation successor records `CLM-079` through
`CLM-085`. It first preserves the general finite-full-seed obstruction and
then proves at mutable candidate scope that

```text
Sat_D(O) finite
  <=> no height-one ramification,
```

and that every divisorial source boundary maps onto a height-one target
divisor. Ramified pole stages escape; an unramified stage also escapes when
it contains an actual positive pole. The latter statement does not infer an
element from a formal pole bound.

For the full finite-cover permutation connection at a generic height-one
point, an embedded ordinary coherent lattice exists exactly when local
inertia is trivial. Regular holonomicity and logarithmic coherence are weaker
and do not imply ordinary structure-sheaf finiteness. A direct global
D-module route would additionally need global ordinary coherence, a
compatible connection preserving both unscaled translations, and a
torsion-free meromorphic embedding with generic fiber `L`.

The surviving exact bridge is `CLM-084`: derive trivial height-one inertia
from the actual polynomial Keller source. This is a reduction, not an
unramifiedness theorem or a stable-lattice construction.

## Fractional-residue spectrum

At a valuation of ramification index `e`, the intrinsic semisimplified tame spectrum is

```text
(1/e)Z / Z
```

with residue-degree multiplicity. At a branch `h(P,Q)=0`, the pair spectrum on the `j`-th tame character is

```text
(j/e)(h_P,h_Q).
```

A normal/tangent frame gives `(j/e,0)`. Integer lattice shifts move the scalar by an integer and cannot erase a nonzero class. The commuting residues are flat-compatible but do not cancel. The determinant-line sum `(e-1)/2` can be integral for odd `e`, so trace or determinant data alone lose the full obstruction.

## Source pole filtration

For the open immersion `j:U=Spec A -> Y=Spec O`, the ring direction is `O -> A`. No purity of `Y\U` is assumed. If `E_1,...,E_r` are its divisorial components, normality gives

```text
A = union_{m in N^r} Gamma(Y,O_Y(sum m_i E_i)).
```

Every fixed stage is coherent and finite over `B`; under the finite-flat surface package it is `B`-locally free. The canonical derivations shift pole bounds by finite vectors, but repeated derivatives grow linearly rather than remaining in one stage.

- ramified transverse increment: `e`;
- ramified logarithmic increment: `0`;
- unramified transverse boundary increment: `1`.

Every finite ramified stage is excluded by the local no-lattice theorem. At an unramified omitted divisor, `O` is locally stable but every stage admitting a genuine pole escapes under a transverse frame member. Commutativity controls ordering, not boundedness. The directed union is stable; no finite stage is.

## Canonical candidates and countercontrols

The successor audits the normalization, inverse different, trace dual, canonical module, conductor shifts, divisorial modules, colons, finite intersections, determinant lines, and multiplier rings. Rank-one reflexive fractional `O`-modules all have multiplier ring `O`, so they do not hide a new order.

Controls include Kummer and tame non-Galois ramification, a cusp branch, several boundary components, unramified nonproper boundary, logarithmic versus exact fields, a never-stabilizing pole union, characteristic-`p` collapse, and a Laurent exact-symplectic model. The last satisfies both `dP wedge dQ=dx wedge dy` and an exact primitive relation while retaining ramification; it is explicitly not a polynomial Keller pair on `A^2`.

## Current obstruction boundary

- `A=C[x,y]` is a pair-stable algebra but is not known finite over `B`.
- `O` is finite and locally free under the maintained surface hypotheses, but pair stability is equivalent to absence of height-one ramification.
- Every coherent divisorial pole stage, fixed conductor/different shift, reflexive hull, and finite intersection is excluded at a ramified component.
- Multiplier closure is automatic once a finite stable module exists.

The surviving route must therefore construct a finite non-divisorial source-derived module inside one fixed finite ambient module, or prove codimension-one unramifiedness by another argument.

## Issue-specific artifacts

- predecessor: `research/issue-4/stable-differential-order/`;
- successor: `research/issues/source-reflexive-lattice/`.
- canonical saturation successor:
  `research/issues/canonical-differential-saturation/`.

The successors' declared `local-adversarial-review` records pass mutable
integration but block reviewed promotion. No finite pair-stable lattice is
constructed.

## Exit

The leaf remains open. It may close only with:

- a finite full module stable under both canonical translations, together with its audited reflexive multiplier order; or
- an independently reviewed obstruction covering a strictly larger exact construction class.
