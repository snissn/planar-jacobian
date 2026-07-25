# Local Adversarial Review

> **Review mode:** `local-adversarial-review`  
> **Reviewer role:** same-session adversarial reviewer, not an independent reviewer  
> **Candidate revision:** `2a0300d3dbfba2a58622d3e60351c18dd28a094a`  
> **Candidate base:** `652a5e252626fa5816445651245e8a8946cee53e`  
> **Owned path:** `research/issues/canonical-differential-saturation/`  
> **Disposition:** `ACCEPT_SCOPED`  
> **Authority after review:** `MUTABLE_NONAUTHORITATIVE`

The scientific candidate was pinned before this review.  No candidate
proof file was edited while the review was conducted.

## 1. Reviewed statements

The review adjudicates only the following packet-local statements.

1. `CDS-001`: the canonical derivations have the displayed signs and
   commute.
2. `CDS-002`: finite differential saturation of any finite full seed
   excludes height-one ramification.
3. `CDS-003`: the normalization-seed saturation is finite exactly
   when the normalization is unramified in codimension one.
4. `CDS-004`: ramified finite pole stages and genuine positive
   unramified pole stages have nonfinite saturation.
5. `CDS-005`: for the finite-cover permutation connection, ordinary
   coherent extension across a height-one divisor is equivalent to
   trivial inertia.
6. `CDS-006`: regular holonomicity or logarithmic coherence does not
   imply ordinary structure-sheaf finiteness.
7. `CDS-007`: ordinary coherence of the full intermediate extension,
   or equivalently trivial height-one inertia, is the surviving exact
   bridge.
8. `CDS-008`: the audited duality, multiplier, jet, and cohomological
   constructions do not bypass that bridge.

No global `CLM-*` status is reviewed or promoted.

## 2. Independent recomputation

### Canonical frame

Direct substitution gives

\[
D_P(P)=1,\quad D_P(Q)=0,\quad
D_Q(P)=0,\quad D_Q(Q)=1.
\]

The commutator kills \(K=\mathbf C(P,Q)\), and finite separability of
\(L/K\) forces it to vanish.

### Saturation

Leibniz and commutativity prove that

\[
\sum_{a,b\ge0}B D_P^aD_Q^b(M_0)
\]

is the minimal pair-stable closure.  If finite, it is precisely the
kind of full local lattice excluded at a transverse ramified DVR.
For \(M_0=O\), the converse uses the codimension-one intersection
description of a normal domain and unique extension of derivations
through finite-etale DVR extensions.  No finiteness of the original
source algebra is assumed.

### Kummer escape

For \(t=s^e\),

\[
D^n(t^Ns^j)
 =
\prod_{r=0}^{n-1}(N+j/e-r)t^{N-n}s^j.
\]

When \(0<j<e\), no factor can vanish in characteristic zero, and the
valuation is unbounded below.  Integer twists, different and
conductor shifts, and reflexive hulls do not change the class
\(j/e\bmod\mathbf Z\).

### D-module criterion

An inertia cycle of length \(e\) has the full character set
\(j/e\bmod\mathbf Z\).  A nonintegral rank-one character has local
cyclic model

\[
\mathcal D/\mathcal D(t\partial_t-\alpha),
\]

whose repeated derivatives produce unbounded negative powers.  It is
regular holonomic but not finite over \(\mathcal O\).  All characters
are ordinary-coherent exactly when every cycle has length one.

The phrase “ordinary integrable connection” is read in its standard
sense: a finite locally free \(\mathcal O\)-module with flat
connection.  If one starts instead with an arbitrary coherent
\(\mathcal D\)-module, the standard local-freeness lemma for an
\(\mathcal O\)-coherent module with connection is additionally
required.  This is a vocabulary clarification, not a change to the
height-one argument.

## 3. Adversarial mutation tests

| Mutation | Result |
|---|---|
| Replace ordinary translations by logarithmic fields | Kummer normalization becomes stable; therefore this changes and weakens the theorem. |
| Shift a lattice by conductor, different, canonical, or trace-dual powers | Residues shift by integers; nonzero classes survive. |
| Take determinant or trace | Individual characters are lost; determinant residue can be integral for odd \(e\). |
| Combine all sheets | The invariant line survives, but the complementary nonzero characters remain, so fullness fails if they are discarded. |
| Drop Galois symmetry | The non-Galois cubic retains a ramified valuation factor and fractional escape. |
| Allow singular branch | Generic smooth height-one points retain the obstruction; codimension-two singularities do not cancel it. |
| Remove ramification but keep a nonproper boundary | \(D(t)\hookrightarrow\mathbf A^2\) still gives an infinite localization under \(j_+\); \(j_{!*}\) is different. |
| Invoke exact symplectic data | The Laurent control satisfies the exact identities while retaining \(j/e\). |
| Invoke Noetherianity on the pole union | Invalid because the union is not contained in a fixed finite ambient module. |
| Invoke Gauss-Manin or compact support | Produces cohomology objects, not automatically a full lattice in \(L\). |

## 4. Source audit

The source bindings were checked against the following primary
references.

- Deligne, LNM 163, Chapter II, Proposition 5.4 and Corollary 5.6:
  logarithmic extension and the monodromy/residue relation.
- Beilinson–Bernstein–Deligne, *Faisceaux pervers*, Astérisque 100:
  intermediate extension and boundary-subquotient minimality.
- Kashiwara, PRIMS 20 (1984), 319–365:
  regular-holonomic Riemann–Hilbert framework.
- Katz–Oda, J. Math. Kyoto Univ. 8 (1968), 199–213:
  Gauss-Manin construction.
- Hartshorne, Math. Ann. 254 (1980), 121–176:
  reflexive codimension-one framework.

None of those sources states the missing ordinary
\(\mathcal O\)-coherence theorem, and the packet does not attribute it
to them.

## 5. Automated review evidence

Construction-revision checks were rerun at enlarged bounds:

```text
verify_local_residues.py --max-e 30 --max-n 64
  kummer_checks: 195170
  pair_spectrum_checks: 464
  non_galois_checks: 3
  total_checks: 195637
  PASS

verify_global_bridges.py --max-degree 25 --max-n 50 --max-e 25
  inertia_partition_checks: 9295
  localization_checks: 255
  exact_symplectic_checks: 72
  total_checks: 9622
  PASS
```

The checks verify encoded identities and mutation controls; they do
not substitute for the mathematical review.

## 6. Blocking-question answers

- **Was a finite full pair-stable lattice constructed?** No.
- **Was height-one ramification excluded for every Keller pair?** No.
- **Was holonomicity conflated with \(\mathcal O\)-coherence?** No.
- **Was logarithmic stability conflated with ordinary stability?** No.
- **Was a determinant-level cancellation promoted to a full-rank
  result?** No.
- **Was the polynomial \(\mathbf A^2\)-source condition modeled by the
  counterexamples?** No; the failure is explicit.
- **Does the result prove degree one unconditionally?** No.

## 7. Verdict

`ACCEPT_SCOPED`.

The candidate correctly proves a coherence equivalence, two exact
counterexamples to proposed categorical shortcuts, and a smaller
trivial-inertia/ordinary-coherence bridge.  It does not solve
`CLM-061`.  Because the same assistant constructed and reviewed the
packet, this review is local adversarial evidence only and cannot
confer independent or frozen authority.
