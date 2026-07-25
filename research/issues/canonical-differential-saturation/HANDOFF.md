# Handoff

> **Role:** `research-worker`  
> **Task issue:** `#4`  
> **Owned path:** `research/issues/canonical-differential-saturation/`  
> **Base:** `652a5e252626fa5816445651245e8a8946cee53e`  
> **Reviewed candidate:** `2a0300d3dbfba2a58622d3e60351c18dd28a094a`  
> **Integration state:** `integration-ready`, not merged

## Exact result to carry forward

The canonical normalization saturation

\[
\operatorname{Sat}_D(O)
 =\sum_{a,b\ge0}B D_P^aD_Q^b(O)
\]

is finite if and only if the finite normalization is unramified in
codimension one.  More generally, finite saturation of any finite
full seed excludes height-one ramification.

On the maximal finite-etale locus, the full pushforward is the
permutation connection.  At a height-one divisor, its ordinary
\(\mathcal O\)-coherent extension exists exactly when local inertia is
trivial.  Deligne logarithmic lattices and regular-holonomic
intermediate extensions exist in ramified Kummer models but remain
\(\mathcal O\)-infinite under a transverse translation.

Therefore no stable lattice has been constructed.  The smallest
surviving bridge is:

> prove from the polynomial Keller source that every height-one
> inertia action on the full permutation local system is trivial;
> equivalently, prove ordinary \(\mathcal O\)-coherence of its full
> intermediate extension in codimension one.

## Proposed shared synchronization

A serialized integration maintainer may, after exact-head validation
and review of the scoped mathematics, make only the following global
changes.

1. Amend the note for `CLM-061` to record:
   - normalization-seed differential saturation is coherent iff there
     is no height-one ramification;
   - ordinary coherence of the full finite-cover intermediate
     extension is equivalent to trivial height-one inertia;
   - holonomic and logarithmic coherence are insufficient;
   - no finite pair-stable lattice was constructed.
2. Add a proof-graph obstruction/reduction node for the
   `CDS-007` coherence wall, depending on `CLM-003`, `CLM-010`,
   `CLM-011`, `CLM-013`, and `CLM-061`.
3. Point `L02`, Track D, the work queue, and the issue index to this
   packet as the current issue #4 successor.
4. Allocate any global claim or graph identifiers against the live
   ledgers at integration time.  Do not reuse packet-local `CDS-*`
   labels as global identifiers without deliberate allocation.

No shared file has been edited by this branch.

## Recommended next task

Work directly on the polynomial-source restriction rather than on a
new lattice functor:

1. compactify the actual source open and finite normalization;
2. compute the inertia permutation and the embedding of source
   coordinate functions in each tame character;
3. use the fact that both canonical translations are polynomial on
   the entire source \(\mathbf A^2\), not merely on the finite-etale
   locus;
4. prove that a nontrivial inertia character would force a source
   pole or monodromy incompatible with both polynomial coordinates.

A useful exact target is:

> **Source-character exclusion.**  At the generic point of a
> ramified boundary divisor, no nonzero tame character of the
> normalization can occur in the restrictions of the polynomial
> source algebra while that algebra is stable under both canonical
> translations and has fraction field \(L\).

This target is strictly smaller than constructing a global lattice,
but it consumes the source \(\mathbf A^2\) condition that all current
countermodels lack.

## Integration cautions

- Do not state that `j_{!*}` is \(\mathcal O\)-coherent merely because
  it is regular holonomic.
- Do not replace ordinary translations by logarithmic vector fields.
- Do not infer full-rank triviality from trace, norm, invariants, or
  determinant.
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
