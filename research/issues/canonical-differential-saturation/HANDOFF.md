# Handoff

> **Role:** `research-worker`  
> **Task issue:** `#4`  
> **Owned path:** `research/issues/canonical-differential-saturation/`  
> **Base:** `652a5e252626fa5816445651245e8a8946cee53e`  
> **Reviewed candidate:** `7523052bde101036bc1753acbc37ba6be78e895b`  
> **Review:** `local-adversarial-review` / `ACCEPT_SCOPED`  
> **Pull request:** `#42`, non-draft, integration-ready, not merged  
> **Integration state:** `integration-ready`, not on `main`

## Exact result to carry forward

The canonical normalization saturation

\[
\operatorname{Sat}_D(O)
 =\sum_{a,b\ge0}B D_P^aD_Q^b(O)
\]

is finite if and only if the finite normalization is unramified in
codimension one.  More generally, finite saturation of any finite
full seed excludes height-one ramification.

Every finite source-pole stage meeting ramification has nonfinite
saturation.  At an unramified omitted divisor, every stage containing
an actual pole also escapes under a transverse canonical translation.
The positive-pole proof starts from a pole-bearing section of the
localized module and tracks its unique lowest-valuation derivative
term; it does not assume that a bare local monomial globalizes.

On the maximal finite-etale locus, the full pushforward is the
permutation connection.  At the generic point of a height-one divisor,
an embedded ordinary \(\mathcal O\)-coherent full lattice exists
exactly when local inertia is trivial.  Deligne logarithmic lattices
and regular-holonomic intermediate extensions can exist in ramified
Kummer models while remaining \(\mathcal O\)-infinite under a
transverse translation.

No stable lattice has been constructed.  The smallest surviving
normalization-route bridge is:

> prove from the polynomial Keller source that every height-one
> inertia action on the full permutation local system is trivial.

This is equivalent, only at each generic height-one point, to ordinary
coherence of the corresponding local intermediate-extension module.
A direct global D-module route is stronger: it must establish global
ordinary coherence, compatibility with both unscaled translations,
and a torsion-free embedding into the meromorphic sheaf with generic
fiber \(L\).

## Corrected multiplier boundary

For a finite full seed \(M\), pair stability implies stability of its
multiplier ring \((M:M)\), but the converse is false.  The exact
control

\[
M=P B\subset K=L=\operatorname{Frac}(B)
\]

satisfies \(D_P(M)\not\subset M\) while \((M:M)=B\) is stable.
Therefore seed instability alone cannot be used to exclude a stable
multiplier.

This correction does not create a shortcut.  A direct proof that a
finite full multiplier ring is pair-stable already constructs the
stable order required by the predecessor theorem.  For every named
rank-one reflexive fractional \(O\)-module \(I\) in this packet,

\[
(I:I)=O,
\]

so the trace dual, inverse different, canonical and conductor twists,
and divisorial source-pole modules return the normalization rather
than a hidden new order.

The residue statement is likewise multiset-valued: changing a
logarithmic lattice shifts representatives by integers on fixed
monodromy eigenspaces, while fractional ramification-parameter twists
may permute character labels.  The full class multiset in
\(\mathbf Q/\mathbf Z\) is unchanged.

## Supported requested dispositions

The packet reaches, at `MUTABLE_NONAUTHORITATIVE` scope:

1. **Disposition (6):** counterexamples to
   `holonomic => O-finite` and
   `coherent logarithmic lattice => ordinary stable lattice`;
2. **Disposition (7):** reduction to trivial height-one inertia, with
   the stronger global coherence-plus-embedding package isolated for
   a direct D-module route.

It does not construct a finite full pair-stable lattice, exclude
height-one ramification for every Keller pair, prove degree one, or
prove the planar Jacobian conjecture.

## Proposed shared synchronization

A serialized integration maintainer may, after re-resolving live
`main` and reviewing the scoped mathematics, make only the following
global changes.

1. Amend the note for `CLM-061` to record:
   - normalization-seed differential saturation is coherent iff there
     is no height-one ramification;
   - at a generic height-one point, embedded ordinary coherence of the
     full permutation connection is equivalent to trivial inertia;
   - a direct global D-module route additionally needs global
     coherence and a torsion-free meromorphic embedding;
   - holonomic and logarithmic coherence are insufficient;
   - seed instability does not imply multiplier instability, while a
     directly stable full multiplier is already the desired order;
   - no finite pair-stable lattice was constructed.
2. Add a proof-graph obstruction/reduction node for the `CDS-007`
   coherence wall, depending on `CLM-003`, `CLM-010`, `CLM-011`,
   `CLM-013`, and `CLM-061`.
3. Point `L02`, Track D, the work queue, and the issue index to this
   packet as the current issue #4 successor.
4. Allocate any global claim or graph identifiers against the live
   ledgers at integration time.  Do not reuse packet-local `CDS-*`
   labels as global identifiers without deliberate allocation.

No shared file has been edited by this branch.

## Recommended next task

Work directly on the polynomial-source restriction rather than on a
new generic lattice functor:

1. compactify the actual source open and finite normalization;
2. compute the inertia permutation and the embedding of source
   coordinate functions in each tame character;
3. use that both canonical translations are polynomial on the entire
   source \(\mathbf A^2\), not merely on the finite-etale locus;
4. prove that a nontrivial inertia character would force source pole or
   monodromy behavior incompatible with both polynomial coordinates.

A useful exact target is:

> **Source-character exclusion.**  At the generic point of a
> ramified boundary divisor, no nonzero tame character of the
> normalization occurs in the restrictions of the polynomial source
> algebra while that algebra is stable under both canonical
> translations and has fraction field \(L\).

This target is strictly smaller than constructing a global lattice,
but it consumes the source \(\mathbf A^2\) condition that all current
countermodels lack.

## Validation evidence

The pinned candidate was byte-compiled and tested at default and
enlarged adversarial bounds.

```text
verify_local_residues.py --max-e 30 --max-n 64
  fractional_twist_checks: 1885
  kummer_checks: 195170
  pair_spectrum_checks: 464
  non_galois_checks: 3
  total_checks: 197522
  PASS

verify_global_bridges.py --max-degree 25 --max-n 50 --max-e 25
  inertia_partition_checks: 9295
  localization_checks: 255
  multiplier_converse_checks: 705
  exact_symplectic_checks: 72
  total_checks: 10327
  PASS
```

The packet aggregator, complete repository suite, and integration
contract are to be confirmed by the permanent read-only workflow on
the exact final PR head.  The workflow locator and conclusion are
recorded on PR #42 so that adding them does not mutate the tested head.
Passing validators records encoded identities and repository
consistency only; it does not establish mathematical truth.

## Integration cautions

- Do not state that `j_{!*}` is \(\mathcal O\)-coherent merely because
  it is regular holonomic.
- Do not replace ordinary translations by logarithmic vector fields.
- Do not infer global D-module coherence from the generic height-one
  criterion alone.
- Do not infer multiplier instability merely from seed instability.
- Do not infer full-rank triviality from trace, norm, invariants, or
  determinant.
- Do not describe every fractional-ideal twist as one common integer
  shift; preserve the full residue-class multiset.
- Do not infer stabilization of an unbounded pole union from
  Noetherianity.
- Do not claim that exact symplectic residue cancellation removes
  every tame character.
- Preserve the local-adversarial, mutable status until a distinct
  reviewer adjudicates the exact candidate revision.

## Validation commands

```bash
python research/issues/canonical-differential-saturation/verify_local_residues.py
python research/issues/canonical-differential-saturation/verify_global_bridges.py
python research/issues/canonical-differential-saturation/verify_all.py
python -m compileall -q scripts research/issues
python -m unittest discover -s scripts/tests -p 'test_*.py'
python scripts/validate_integration_contract.py --no-remote
python scripts/render_views.py --check
python scripts/validate_repository.py
python scripts/frontier.py
python scripts/validate_defect4_staircase.py
python scripts/review_validate_defect4_independent.py
python research/issues/issue-3-unramified-index/verify_index_models.py
python research/issues/rank-three-index-form-unit/verify_all.py
python scripts/validate_issue4_stable_order.py
python research/issues/source-reflexive-lattice/verify_all.py
python scripts/validate_issue5_principal_parts.py
python research/issues/one-boundary-logarithmic-field/verify_all.py
python research/issues/defect-5-rees/validate_defect5.py
python research/issues/defect-5-rees/review_validate_defect5_adversarial.py
```

The PR must remain unmerged during this parallel round.
