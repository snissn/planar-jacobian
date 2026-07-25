# Handoff

> **Role:** `research-worker`  
> **Task issue:** `#4`  
> **Owned path:** `research/issues/canonical-differential-saturation/`  
> **Base:** `652a5e252626fa5816445651245e8a8946cee53e`  
> **Reviewed candidate:** `ab498bd9f40fdb36137fbe8a52658555a3eef004`  
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
codimension one.  More generally, finite saturation of any finite full
seed excludes height-one ramification.

For each divisorial component \(E\) of the source boundary, finiteness
of

\[
Y=\operatorname{Spec}O\longrightarrow\operatorname{Spec}B
\]

forces its image to be a height-one base divisor.  If \(q\) is the
generic prime of \(E\) and \(p=q\cap B\), then
\(B/p\subset O/q\) is finite integral and both quotient rings have
dimension one.  Thus no divisorial source boundary is contracted to a
codimension-two target point.

Every finite source-pole stage meeting ramification has nonfinite
saturation.  At an unramified omitted divisor, every stage containing
an actual positive pole also escapes under a transverse canonical
translation.  The proof begins with a pole-bearing section of the
localized module and tracks its unique lowest-valuation derivative
term; it does not assume that a bare local monomial globalizes.

A finite intersection of pole stages or derivative translates is
subject to the finite-seed obstruction only if it remains full over
\(B\).  A nonfull intersection is not a lattice with generic fiber
\(L\), so it cannot solve issue #4.

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

This is equivalent only at each generic height-one point to ordinary
coherence of the local intermediate-extension module.  A direct global
D-module route is stronger: it must establish global ordinary
coherence, a compatible connection preserving both unscaled
translations, and a torsion-free embedding into the meromorphic sheaf
with generic fiber \(L\).

## Corrected multiplier, residue, and validation boundaries

For a finite full seed \(M\), pair stability implies stability of its
multiplier ring \((M:M)\), but the converse is false.  The control

\[
M=P B\subset K=L=\operatorname{Frac}(B)
\]

satisfies \(D_P(M)\not\subset M\) while \((M:M)=B\) is stable.
Seed instability therefore does not exclude a stable multiplier.

A direct proof that a finite full multiplier ring is pair-stable
already constructs the stable order required by the predecessor route.
For each named rank-one reflexive fractional \(O\)-module \(I\),

\[
(I:I)=O,
\]

so trace duals, inverse differents, canonical and conductor twists, and
divisorial source-pole modules return the normalization rather than a
hidden order.

Changing a logarithmic lattice shifts residue representatives by
integers on fixed monodromy eigenspaces, while fractional
ramification-parameter twists may permute character labels.  The full
class multiset in \(\mathbf Q/\mathbf Z\) is unchanged.

The renewed candidate also corrects two validation gaps:

1. the normal/tangent pair-spectrum check now reduces modulo the actual
   frame relation \(a h_P+b h_Q-1=0\); and
2. the packet aggregator runs both default and documented enlarged
   validator bounds.

## Supported requested dispositions

At `MUTABLE_NONAUTHORITATIVE` scope the packet reaches:

1. **Disposition (6):** counterexamples to
   `holonomic => O-finite` and
   `coherent logarithmic lattice => ordinary stable lattice`;
2. **Disposition (7):** reduction to trivial height-one inertia, with
   the stronger global ordinary-coherence, pair-stability, and
   embedding package isolated for a direct D-module route.

It does not construct a finite full pair-stable lattice, exclude
height-one ramification for every Keller pair, prove degree one, or
prove the planar Jacobian conjecture.

## Proposed shared synchronization

A serialized integration maintainer may, after re-resolving live
`main` and reviewing the scoped mathematics, make only these global
changes.

1. Amend the note for `CLM-061` to record:
   - normalization-seed differential saturation is coherent iff there
     is no height-one ramification;
   - every divisorial source boundary maps onto a height-one target
     divisor because the normalization is finite;
   - unramified stages containing an actual positive pole escape under
     a transverse translation;
   - the finite-seed obstruction applies to finite intersections only
     when they remain full;
   - at a generic height-one point, embedded ordinary coherence of the
     full permutation connection is equivalent to trivial inertia;
   - a direct global D-module route additionally needs global ordinary
     coherence, preservation by both unscaled translations, and a
     torsion-free meromorphic embedding;
   - holonomic and logarithmic coherence are insufficient;
   - seed instability does not imply multiplier instability, while a
     directly stable full multiplier is already the desired order;
   - no finite pair-stable lattice was constructed.
2. Add a proof-graph obstruction/reduction node for `CDS-007`,
   depending on `CLM-003`, `CLM-010`, `CLM-011`, `CLM-013`, and
   `CLM-061`.
3. Point `L02`, Track D, the work queue, and the issue index to this
   packet as the current issue #4 successor.
4. Allocate global claim or graph identifiers against the live ledgers
   at integration time.  Packet-local `CDS-*` labels are not global
   allocations.

No shared file has been edited by this branch.

## Recommended next task

Work directly on the polynomial-source restriction rather than on a
new generic lattice functor:

1. compactify the actual source open and finite normalization;
2. compute the inertia permutation and embedding of source coordinate
   functions in each tame character;
3. use that both canonical translations are polynomial on the entire
   source \(\mathbf A^2\), not merely on the finite-etale locus;
4. prove that a nontrivial inertia character forces source pole or
   monodromy behavior incompatible with both polynomial coordinates.

A useful exact target is:

> **Source-character exclusion.**  At the generic point of a
> ramified boundary divisor, no nonzero tame character of the
> normalization occurs in the restrictions of the polynomial source
> algebra while that algebra is stable under both canonical
> translations and has fraction field \(L\).

## Validation evidence

The exact candidate validator files were reconstructed byte for byte.
Their local Git blob hashes matched the remote candidate blobs:

```text
verify_local_residues.py  de75ce69bae2324106b42c75f8f15ba9cffb4a91
verify_global_bridges.py  1428959b91216d65eebd0f1c12a6d10681c8b7e0
verify_all.py              a4a6c5903d1ea97a4ac0676450f58848dd9dc46a
```

Byte compilation, default runs, enlarged adversarial runs, and
invalid-bound mutations passed:

```text
verify_local_residues.py
  fractional_twist_checks: 319
  kummer_checks: 7502
  pair_spectrum_checks: 77
  non_galois_checks: 3
  total_checks: 7901
  PASS

verify_global_bridges.py
  inertia_partition_checks: 271
  localization_checks: 65
  multiplier_converse_checks: 185
  exact_symplectic_checks: 27
  total_checks: 548
  PASS

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

The permanent read-only repository workflow on the exact final PR head
must confirm byte compilation of maintained Python, the integration
contract, generated views, structural validation, frontier generation,
and the complete maintained repository suite.  Its exact run locator
and conclusion belong in PR #42 so that the tested head remains
unchanged.  Passing validators records encoded identities and
repository consistency only; it does not establish mathematical truth.

## Integration cautions

- Do not state that `j_{!*}` is \(\mathcal O\)-coherent merely because
  it is regular holonomic.
- Do not replace ordinary translations by logarithmic vector fields.
- Do not omit either unscaled translation from the global D-module
  bridge.
- Do not infer global coherence from the generic height-one criterion.
- Do not apply the finite-seed theorem to a nonfull intersection.
- Do not invent a contracted divisorial boundary in the finite
  normalization; finite images of divisors remain divisorial.
- Do not infer unramified pole escape unless the stage contains an
  actual positive pole.
- Do not infer multiplier instability from seed instability.
- Do not infer full-rank triviality from trace, norm, invariants, or
  determinant.
- Preserve the full residue-class multiset under fractional twists.
- Do not infer stabilization of an unbounded pole union from
  Noetherianity.
- Preserve local-adversarial mutable status until a distinct reviewer
  adjudicates the exact candidate revision.

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
