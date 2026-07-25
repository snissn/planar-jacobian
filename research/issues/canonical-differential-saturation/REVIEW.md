# Renewed Local Adversarial Review

> **Review mode:** `local-adversarial-review`  
> **Reviewer role:** same-session adversarial reviewer, not an independent reviewer  
> **Candidate revision:** `7523052bde101036bc1753acbc37ba6be78e895b`  
> **Candidate base:** `652a5e252626fa5816445651245e8a8946cee53e`  
> **Owned path:** `research/issues/canonical-differential-saturation/`  
> **Disposition:** `ACCEPT_SCOPED`  
> **Authority after review:** `MUTABLE_NONAUTHORITATIVE`

The corrected scientific candidate was pinned before this renewed
review.  No candidate proof or validation file was edited while the
review was conducted.  The earlier review at
`2a0300d3dbfba2a58622d3e60351c18dd28a094a` is superseded for the
current packet head.

## 1. Correction that triggered renewed review

The earlier construction audit contained the overstatement that the
multiplier ring \((M:M)\) is stable only when the seed \(M\) is
stable.  The necessity direction is false.  The corrected candidate
includes the exact control

\[
B=\mathbf C[P,Q],\qquad K=L=\operatorname{Frac}(B),
\qquad M=P B:
\]

\[
D_P(P)=1\notin P B,
\qquad
(M:M)=B.
\]

Thus seed stability implies multiplier stability, but not conversely.
The repaired packet now treats direct stability of a full multiplier
ring as a separate exact stable-order condition.  This does not create
a new Keller construction: proving that condition already constructs
the desired finite full stable order, while every named rank-one
reflexive fractional \(O\)-module satisfies \((I:I)=O\).

The renewed audit also replaces the loose assertion that every dual or
fractional-ideal modification is a common integer residue shift.  On a
fixed monodromy eigenspace, logarithmic-lattice changes shift a residue
representative by an integer; multiplication by \(s^k\) can also
permute tame character labels.  The invariant statement is that the
full residue-class multiset in \(\mathbf Q/\mathbf Z\) is unchanged.

## 2. Reviewed statements

The review adjudicates only the following packet-local statements.

1. `CDS-001`: the canonical derivations have the displayed signs and
   commute.
2. `CDS-002`: finite differential saturation of any finite full seed
   excludes height-one ramification.
3. `CDS-003`: the normalization-seed saturation is finite exactly
   when the normalization is unramified in codimension one.
4. `CDS-004`: ramified finite pole stages and genuine positive
   unramified pole stages have nonfinite saturation.
5. `CDS-005`: for the finite-cover permutation connection, an embedded
   ordinary coherent extension across one generic height-one point is
   equivalent to trivial inertia there.
6. `CDS-006`: regular holonomicity or logarithmic coherence does not
   imply ordinary structure-sheaf finiteness.
7. `CDS-007`: trivial inertia at every height-one divisor is the
   surviving normalization-route bridge; a direct D-module route
   additionally requires global ordinary coherence and a torsion-free
   meromorphic embedding with generic fiber \(L\).
8. `CDS-008`: the audited dual, canonical, jet, and cohomological
   constructions do not bypass that bridge; multiplier stability is
   not automatic and, if established directly, is already the desired
   stable-order construction.

No global `CLM-*` status is reviewed or promoted.

## 3. Independent recomputation

### Canonical frame

Direct substitution gives

\[
D_P(P)=1,\quad D_P(Q)=0,\quad
D_Q(P)=0,\quad D_Q(Q)=1.
\]

The commutator restricts to zero on \(K=\mathbf C(P,Q)\).  Since
\(L/K\) is finite separable in characteristic zero, every
\(K\)-derivation of \(L\) vanishes, so \([D_P,D_Q]=0\).

### Saturation

Leibniz and commutativity prove that

\[
\sum_{a,b\ge0}B D_P^aD_Q^b(M_0)
\]

is the minimal pair-stable closure.  If it is finite, it is a full
finite local lattice of the kind excluded by the transverse
ramified-DVR theorem.  For \(M_0=O\), the converse uses the
codimension-one intersection description of the normal domain and
unique extension of derivations through finite-etale DVR extensions.
No finiteness of the original source algebra is assumed.

### Positive unramified pole stages

At an unramified omitted divisor, choose a local pole-bearing section
\(f=us^{-m}\) from the actual localized stage and a transverse
canonical derivation with \(D(s)=a\in S^\times\).  The unique
lowest-valuation term is

\[
D^n(f)=(-1)^n(m)_nua^ns^{-m-n}
      +O(s^{-m-n+1}).
\]

Characteristic zero makes \((m)_n\ne0\), so the pole order grows
without assuming that a bare monomial belongs to the global module.

### Kummer escape and fractional twists

For \(t=s^e\),

\[
D^n(t^Ns^j)
 =
\prod_{r=0}^{n-1}(N+j/e-r)t^{N-n}s^j.
\]

When \(0<j<e\), no factor can vanish and the valuation is unbounded
below.  For every integer \(k\),

\[
\{(j+k)/e\bmod\mathbf Z:0\le j<e\}
 =\{j/e\bmod\mathbf Z:0\le j<e\}.
\]

This verifies the corrected multiset statement for different,
canonical, conductor, trace-dual, and fractional-ideal mutations.

### Multiplier logic

For a stable seed \(M\),

\[
D(z)m=D(zm)-zD(m)
\]

proves \(D((M:M))\subset(M:M)\).  The control \(M=P B\) disproves
the converse.  For a rank-one reflexive fractional \(O\)-module
\(I\), local principalness at height one gives
\((I_q:I_q)=O_q\), and normal intersection gives \((I:I)=O\).
The corrected packet uses no invalid converse.

### D-module criterion

An inertia cycle of length \(e\) has the full character set
\(j/e\bmod\mathbf Z\).  A nonintegral rank-one character has local
cyclic model

\[
\mathcal D/\mathcal D(t\partial_t-\alpha),
\]

whose repeated derivatives produce unbounded negative powers.  It is
regular holonomic but not finite over \(\mathcal O\).  All characters
are ordinary-coherent at the generic height-one point exactly when
every cycle has length one.

This local equivalence is not promoted to a global equivalence.  The
direct global theorem separately assumes an
\(\mathcal O_{\mathbf A^2}\)-coherent extension, a compatible
ordinary connection, and an injective meromorphic realization with
generic fiber \(L\).  Affineness then yields the desired finite full
pair-stable module.

## 4. Adversarial mutation tests

| Mutation | Result |
|---|---|
| Replace ordinary translations by logarithmic fields | Kummer normalization becomes stable; therefore this changes and weakens the theorem. |
| Shift fixed eigenspaces by base-divisor powers | Residue representatives change by integers; nonzero classes survive. |
| Twist by a ramification parameter, inverse different, or canonical fractional ideal | Character labels may permute, but the complete class multiset is unchanged. |
| Infer multiplier instability from seed instability | False; \(M=P B\) has stable multiplier \(B\). The packet now uses only the valid one-way implication. |
| Prove a full multiplier ring stable directly | This is not a shortcut: it is already the finite full stable order required by the predecessor theorem. |
| Take determinant or trace | Individual characters are lost; determinant residue can be integral for odd \(e\). |
| Combine all sheets | The invariant line survives, but the complementary nonzero characters remain, so fullness fails if they are discarded. |
| Drop Galois symmetry | The non-Galois cubic retains a ramified valuation factor and fractional escape. |
| Allow singular branch | Generic smooth height-one points retain the obstruction; codimension-two singularities do not cancel it. |
| Remove ramification but keep a nonproper boundary | \(D(t)\hookrightarrow\mathbf A^2\) still gives an infinite localization under \(j_+\); \(j_{!*}\) is different. |
| Invoke exact symplectic data | The Laurent control satisfies the exact identities while retaining \(j/e\). |
| Invoke Noetherianity on the pole union | Invalid because the union is not contained in a fixed finite ambient module. |
| Invoke Gauss-Manin or compact support | Produces cohomology objects, not automatically a full lattice in \(L\). |

## 5. Primary-source audit

The source bindings were checked against the following primary
references.

- Deligne, LNM 163, II.5.4 and II.5.6: a chosen residue section gives
  a coherent logarithmic extension, and monodromy is related to the
  exponential of the residue.  This licenses logarithmic, not
  ordinary, stability.
- Beilinson–Bernstein–Deligne, *Faisceaux pervers*, Astérisque 100:
  intermediate extension is characterized by boundary-subquotient
  minimality; that categorical statement is not ordinary
  \(\mathcal O\)-finiteness.
- Kashiwara, PRIMS 20 (1984), 319–365: the regular-holonomic
  Riemann–Hilbert framework concerns \(\mathcal D\)-coherence and
  constructibility, not finite generation over \(\mathcal O\).
- Katz–Oda, J. Math. Kyoto Univ. 8 (1968), 199–213: Gauss-Manin
  construction and integrability under smooth-family hypotheses; its
  cohomology modules are not automatically embedded full lattices in
  \(L\).
- Hartshorne, Math. Ann. 254 (1980), 121–176: reflexive
  codimension-one framework; connection stability after reflexive hull
  is still checked directly.

None of these sources supplies the missing Keller-specific ordinary
coherence, trivial-inertia, or meromorphic-embedding theorem.

## 6. Automated review evidence

The exact candidate scripts were byte-compiled and rerun at default
and enlarged bounds.  Enlarged results were:

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

Default results were `7901` local checks and `548` global checks, both
`PASS`.  These checks verify encoded identities and mutation controls;
they do not substitute for the mathematical review.

## 7. Blocking-question answers

- **Was a finite full pair-stable lattice constructed?** No.
- **Was height-one ramification excluded for every Keller pair?** No.
- **Was holonomicity conflated with \(\mathcal O\)-coherence?** No.
- **Was logarithmic stability conflated with ordinary stability?** No.
- **Was multiplier stability inferred from an invalid converse?** No;
  the false converse is explicitly refuted and removed.
- **Was a common integer shift incorrectly asserted for every
  fractional-ideal twist?** No; the corrected invariant is the full
  residue-class multiset.
- **Was local height-one ordinary coherence conflated with the stronger
  global D-module bridge?** No.
- **Was a determinant-level cancellation promoted to a full-rank
  result?** No.
- **Was the polynomial \(\mathbf A^2\)-source condition modeled by the
  counterexamples?** No; the failure is explicit.
- **Does the result prove degree one unconditionally?** No.

## 8. Verdict

`ACCEPT_SCOPED`.

The corrected candidate proves the normalization-saturation
coherence equivalence, the finite-seed and pole-stage obstructions,
the generic height-one inertia criterion, and exact counterexamples to
categorical shortcuts.  It isolates trivial height-one inertia as the
smallest normalization-route statement and the stronger global
coherence-plus-embedding package for a direct D-module route.  It does
not solve `CLM-061`.

Because the same assistant constructed and reviewed the packet, this
review is local adversarial evidence only and cannot confer independent
or frozen authority.
