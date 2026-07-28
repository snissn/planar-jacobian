# Renewed Local Adversarial Review

> **Review mode:** `local-adversarial-review`  
> **Reviewer role:** same-session adversarial reviewer, not an independent reviewer  
> **Candidate revision:** `ab498bd9f40fdb36137fbe8a52658555a3eef004`  
> **Candidate base:** `652a5e252626fa5816445651245e8a8946cee53e`  
> **Owned path:** `research/issues/canonical-differential-saturation/`  
> **Disposition:** `ACCEPT_SCOPED`  
> **Authority after review:** `MUTABLE_NONAUTHORITATIVE`

The scientific candidate was pinned before this review.  No reviewed
proof or validation file was edited while the review was conducted.
The candidate extends the previously accepted local packet only by:

1. imposing the normal-frame relation in the pair-spectrum validator;
2. making the packet aggregator run both default and documented enlarged
   bounds; and
3. narrowing the unramified pole-stage table entry to stages containing
   an actual positive pole.

Reviews pinned to earlier candidates are superseded for the current
packet head.

## 1. Exact reviewed scope

`ACCEPT_SCOPED` is bound to the exact bytes of these eleven files at
candidate revision `ab498bd9f40fdb36137fbe8a52658555a3eef004`:

1. `FOUNDATIONS.md`;
2. `DIFFERENTIAL_SATURATION.md`;
3. `DMODULE_ROUTE.md`;
4. `LOGARITHMIC_LATTICES.md`;
5. `LOCAL_RESIDUES.md`;
6. `CONSTRUCTION_TABLE.md`;
7. `COUNTERMODELS.md`;
8. `SOURCE_AUDIT.md`;
9. `verify_local_residues.py`;
10. `verify_global_bridges.py`;
11. `verify_all.py`.

`README.md` is the packet summary.  Its scientific prose was checked
against the reviewed files; only review metadata may change after the
candidate pin.  `REVIEW.md`, `HANDOFF.md`, and `INTEGRATION.json` are
review and transport metadata and may record the pin, PR, validation,
risks, and handoff without expanding the accepted mathematics.

Any later material edit to a reviewed file, or to the scientific prose
of `README.md`, requires a new pinned review.

## 2. Corrections adjudicated

### 2.1 Multiplier implication

The false converse

\[
(M:M)\text{ stable}\Longrightarrow M\text{ stable}
\]

is not used.  For

\[
B=\mathbf C[P,Q],\qquad K=L=\operatorname{Frac}(B),\qquad M=PB,
\]

we have \(D_P(P)=1\notin PB\), while \((M:M)=B\) is pair-stable.
The packet uses only

\[
D(M)\subset M\Longrightarrow D((M:M))\subset(M:M).
\]

A direct proof that a finite full multiplier ring is pair-stable is
already a construction of the required stable order.  For the named
rank-one reflexive fractional \(O\)-modules, \((I:I)=O\).

### 2.2 Fractional-ideal twists

Changing a logarithmic lattice shifts residue representatives by
integers on fixed monodromy eigenspaces.  Multiplication by a
ramification parameter can instead permute tame character labels.  The
invariant statement is preservation of the complete residue-class
multiset in \(\mathbf Q/\mathbf Z\), not a common shift in a fixed basis.

### 2.3 Fullness of finite intersections

The finite-seed obstruction applies to a finite intersection of pole
stages or derivative translates only when its generic fiber is all of
\(L\).  A nonfull intersection is not a candidate lattice and is not fed
into the theorem.

### 2.4 Images of source-boundary divisors

For the finite normalization morphism

\[
\nu:Y=\operatorname{Spec}O\longrightarrow\operatorname{Spec}B,
\]

let \(q\subset O\) be the height-one generic prime of a divisorial
boundary component and \(p=q\cap B\).  Since \(B/p\subset O/q\) is
finite integral,

\[
\dim(B/p)=\dim(O/q)=1.
\]

As \(B\) has dimension two, \(p\) has height one.  Thus the DVR proof
does not silently treat a divisor contracted to codimension two.

### 2.5 Actual-pole premise at an unramified omitted divisor

The unramified pole-growth argument begins with an actual localized
section \(f=us^{-m}\), \(m>0\), and a transverse field satisfying
\(D(s)=a\in O_q^\times\).  It does not infer escape merely from a
formally positive bound vector when the corresponding module contains
no section attaining a positive pole.  The construction table now uses
this exact premise.

### 2.6 Pair-spectrum validator

The prior check rewrote

\[
r(a h_P+b h_Q)-r=r(a h_P+b h_Q-1)
\]

without imposing the normal-frame relation.  The candidate constructs
the Groebner basis of

\[
(a h_P+b h_Q-1)
\]

and verifies that the normal coefficient minus \(r=j/e\) reduces to
zero modulo that ideal.  The tangential coefficient is checked to be
identically zero.

### 2.7 Aggregator coverage

`verify_all.py` now invokes both validators at their defaults and again
at the enlarged bounds recorded below.  It then checks the required
artifact set, issue ownership, review pin, integration state, packet
labels, and forbidden categorical shortcuts.

## 3. Reviewed packet-local statements

The review adjudicates only the following mutable packet-local claims.

1. `CDS-001`: the canonical derivations have the displayed signs and
   commute.
2. `CDS-002`: finite differential saturation of any finite full seed
   excludes height-one ramification.
3. `CDS-003`: the normalization-seed saturation is finite exactly when
   the normalization is unramified in codimension one.
4. `CDS-004`: every divisorial source boundary maps onto a height-one
   base divisor; every ramified pole stage, and every unramified stage
   containing an actual positive pole, has nonfinite saturation.
5. `CDS-005`: for the finite-cover permutation connection, an embedded
   ordinary coherent extension across a generic height-one point is
   equivalent to trivial inertia there.
6. `CDS-006`: regular holonomicity or logarithmic coherence does not
   imply ordinary structure-sheaf finiteness.
7. `CDS-007`: trivial inertia at every height-one divisor is the
   surviving normalization route.  A direct global D-module route also
   needs global ordinary coherence, a compatible connection preserving
   both unscaled translations, and a torsion-free meromorphic embedding
   with generic fiber \(L\).
8. `CDS-008`: the audited dual, multiplier, intersection, jet, and
   cohomological constructions do not bypass that bridge.

No global `CLM-*` claim is allocated, promoted, frozen, or re-reviewed.

## 4. Claim-to-file and dependency bindings

| Claim | Reviewed proof files | Packet dependencies | Inherited repository dependencies |
|---|---|---|---|
| `CDS-001` | `FOUNDATIONS.md` | \(J(P,Q)=1\); finite separability of \(L/K\) | canonical-derivation context associated with `CLM-010` |
| `CDS-002` | `FOUNDATIONS.md`, `DIFFERENTIAL_SATURATION.md`, `LOCAL_RESIDUES.md` | finite full seed; transverse ramified-DVR escape | issue #4 local-DVR theorem; no global promotion |
| `CDS-003` | `DIFFERENTIAL_SATURATION.md`, `LOCAL_RESIDUES.md` | `CDS-002`; normal height-one intersection; unramified DVR extension | `CLM-003`; `CLM-010`–`CLM-013` only for the conditional consequence |
| `CDS-004` | `DIFFERENTIAL_SATURATION.md`, `LOCAL_RESIDUES.md`, `CONSTRUCTION_TABLE.md` | finite \(Y/B\); actual pole-bearing section; characteristic-zero leading coefficient | mutable source-reflexive-lattice pole filtration |
| `CDS-005` | `DMODULE_ROUTE.md`, `LOGARITHMIC_LATTICES.md`, `LOCAL_RESIDUES.md` | finite-etale permutation connection; inertia cycles; embedded full local lattice | no global coherence theorem imported |
| `CDS-006` | `DMODULE_ROUTE.md`, `LOGARITHMIC_LATTICES.md`, `COUNTERMODELS.md`, `SOURCE_AUDIT.md` | explicit Kummer and localization controls | Deligne/BBD/Kashiwara vocabulary only |
| `CDS-007` | `DIFFERENTIAL_SATURATION.md`, `DMODULE_ROUTE.md` | `CDS-003`, `CDS-005`; distinction between normalization and global D-module routes | `CLM-010`–`CLM-013` only after a stable full module exists; `CLM-061` remains open |
| `CDS-008` | `CONSTRUCTION_TABLE.md`, `COUNTERMODELS.md`, `DIFFERENTIAL_SATURATION.md`, `SOURCE_AUDIT.md` | one-way multiplier implication; \((I:I)=O\); fullness for intersections; residue-multiset invariance | mutable predecessor multiplier-order bridge |

## 5. Independent recomputation

### 5.1 Canonical frame

For

\[
D_P=Q_y\partial_x-Q_x\partial_y,\qquad
D_Q=-P_y\partial_x+P_x\partial_y,
\]

direct substitution gives

\[
D_P(P)=1,\quad D_P(Q)=0,\quad
D_Q(P)=0,\quad D_Q(Q)=1.
\]

The commutator kills \(P,Q\), hence is a \(K=\mathbf C(P,Q)\)-derivation
of the finite separable extension \(L/K\).  Therefore
\([D_P,D_Q]=0\).

### 5.2 Saturation and pole escape

Leibniz and commutativity make

\[
\operatorname{Sat}_D(M_0)
 =\sum_{a,b\ge0}B D_P^aD_Q^b(M_0)
\]

the minimal pair-stable closure.  If this is finite and \(M_0\) is
full, localization gives the prohibited finite full stable lattice at
any ramified height-one valuation.

At an unramified omitted divisor, for an actual pole-bearing section
\(f=us^{-m}\) and transverse \(D(s)=a\in O_q^\times\),

\[
D^n(f)=(-1)^n(m)_nua^ns^{-m-n}+O(s^{-m-n+1}).
\]

Characteristic zero makes the leading coefficient nonzero, so the pole
order is unbounded.

### 5.3 Kummer residues

For \(t=s^e\),

\[
\partial_t^n(t^Ns^j)
 =\prod_{r=0}^{n-1}(N+j/e-r)t^{N-n}s^j.
\]

For \(0<j<e\), none of the factors vanishes and the valuation tends to
minus infinity.  Integer lattice shifts preserve \(j/e\bmod\mathbf Z\),
and fractional ramification-parameter twists preserve the complete
multiset by permutation.

For a normal/tangent frame satisfying \(a h_P+b h_Q=1\), the pair
residue on the \(j\)-th character is

\[
(j/e,0).
\]

The candidate validator now checks the normal equality modulo the
actual frame relation rather than by a tautological rearrangement.

### 5.4 Inertia criterion

An inertia cycle of length \(e\) contributes

\[
0,1/e,\ldots,(e-1)/e\pmod{\mathbf Z}.
\]

An ordinary coherent embedded lattice stable under the transverse
translation can exist only when all classes are integral, equivalently
when every cycle has length one.  Conversely, trivial inertia gives the
unramified integral closure locally.  This is a generic height-one
criterion, not a global coherence theorem.

### 5.5 Multiplier and D-module logic

For stable \(M\), Leibniz proves stability of \((M:M)\); \(M=PB\)
disproves the converse.  A nonintegral Kummer character is modeled by

\[
\mathcal D/\mathcal D(t\partial_t-\alpha),
\]

which is regular holonomic but generates unbounded ordinary poles under
\(\partial_t\).  Thus holonomicity and logarithmic coherence do not
supply the required finite ordinary lattice.

## 6. Adversarial mutations

| Mutation | Result |
|---|---|
| Contract a divisorial boundary to codimension two | Impossible for finite \(Y\to\operatorname{Spec}B\); finite integral quotients preserve divisor dimension. |
| Apply the finite-seed theorem to a nonfull intersection | Invalid; fullness is an explicit premise. |
| Treat a positive bound as an attained pole | Invalid; the unramified theorem begins with an actual pole-bearing section. |
| Replace translations by logarithmic fields | The Kummer normalization becomes stable, weakening the target theorem. |
| Shift residue representatives by integers | Nonzero classes survive. |
| Twist by a ramification parameter | Character labels may permute; the complete class multiset survives. |
| Infer multiplier instability from seed instability | False for \(M=PB\); no such converse is used. |
| Take determinant, trace, norm, or invariants | Individual characters or fullness are lost. |
| Remove ramification but retain nonproper boundary | \(j_+\) may remain an infinite localization; \(j_{!*}\) is different. |
| Invoke exact symplectic data | The Laurent control retains \(j/e\). |
| Invoke Noetherianity on the pole union | Invalid without one fixed finite ambient module. |
| Invoke Gauss-Manin or compact support | Produces cohomology, not a full embedded lattice in \(L\). |
| Omit \(a h_P+b h_Q=1\) in the symbolic check | Detected by review; corrected by ideal reduction. |
| Run only default validator bounds | Detected by review; the aggregator now also runs the documented enlarged bounds. |

## 7. Primary-source audit

The reviewed source use remains deliberately narrow.

- Deligne, *Equations différentielles à points singuliers réguliers*,
  LNM 163 (1970), II.5.4 and II.5.6, supplies canonical logarithmic
  extensions after choosing residue representatives and relates
  monodromy to residues under the stated convention.  It does not
  remove poles or make the meromorphic D-module 
  \(\mathcal O\)-finite.
- Beilinson–Bernstein–Deligne, *Faisceaux pervers*, Astérisque 100
  (1983), supplies intermediate extension and categorical minimality.
  It does not prove ordinary \(\mathcal O\)-coherence of the associated
  D-module.
- Kashiwara, “The Riemann–Hilbert Problem for Holonomic Systems,” PRIMS
  20 (1984), 319–365, supplies the regular-holonomic/constructible
  correspondence.  Holonomicity is coherence over \(\mathcal D\), not
  over \(\mathcal O\).
- Katz–Oda, “On the differentiation of De Rham cohomology classes with
  respect to parameters,” J. Math. Kyoto Univ. 8 (1968), 199–213,
  supplies the Gauss–Manin connection under smooth-family hypotheses.
  A cohomology module is not automatically a submodule of \(L\).
- Hartshorne, “Stable Reflexive Sheaves,” Math. Ann. 254 (1980),
  121–176, supplies the standard reflexive/codimension-one framework.
  Reflexive hulls do not automatically preserve a connection or erase
  fractional residues.

The load-bearing saturation, residue, multiplier, and local coherence
claims are proved directly in the packet; no cited source is used as a
black box for the missing Keller-specific inertia theorem.

## 8. Validation evidence

The two load-bearing validator files were reconstructed byte for byte.
Their local Git blob hashes matched the candidate blobs:

```text
verify_local_residues.py  de75ce69bae2324106b42c75f8f15ba9cffb4a91
verify_global_bridges.py  1428959b91216d65eebd0f1c12a6d10681c8b7e0
verify_all.py              a4a6c5903d1ea97a4ac0676450f58848dd9dc46a
```

Byte compilation, default runs, enlarged runs, and invalid-bound
mutations passed:

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

verify_local_residues.py --max-e 1 --max-n 4
  rejected: bounds must satisfy max-e >= 2 and max-n >= 1

verify_global_bridges.py --max-degree 4 --max-n 0 --max-e 3
  rejected: bounds must satisfy max-degree >= 1, max-n >= 1,
            and max-e >= 2
```

The automated checks evaluate encoded identities and artifact
contracts.  They do not substitute for mathematical review.

## 9. Unresolved risks and exclusions

1. No Keller-specific theorem forces trivial height-one inertia.
2. No finite non-divisorial pair-stable lattice or stable multiplier
   order is constructed for an arbitrary Keller pair.
3. Generic height-one ordinary coherence does not prove global
   \(\mathcal O\)-coherence, codimension-two control, pair-stability, or
   a compatible meromorphic embedding.
4. The review does not independently re-adjudicate `CLM-010`–`CLM-013`
   or `CLM-061`.
5. None of the countermodels is a polynomial Keller counterexample on
   the full affine plane.
6. The reviewer is the constructing assistant; promotion or freeze
   requires a distinct reviewer.
7. The primary sources do not supply the missing ordinary-coherence or
   inertia-exclusion theorem.

## 10. Blocking-question answers

- **Finite full pair-stable lattice constructed?** No.
- **Height-one ramification excluded for every Keller pair?** No.
- **Finite-seed obstruction applied without fullness?** No.
- **Unramified pole escape asserted without an actual pole?** No.
- **Holonomicity or logarithmic stability conflated with ordinary
  pair-stability?** No.
- **Invalid multiplier converse used?** No.
- **Local height-one coherence promoted to global coherence?** No.
- **Either unscaled translation omitted from the direct bridge?** No.
- **Normal-frame relation omitted from the symbolic validation?** No.
- **Documented enlarged bounds omitted from the aggregator?** No.
- **Degree one claimed unconditionally?** No.

## 11. Verdict

`ACCEPT_SCOPED`.

The candidate proves the normalization-saturation coherence
equivalence, the finite-full-seed and divisorial pole-stage
obstructions, the generic height-one inertia criterion, and explicit
counterexamples to categorical shortcuts.  It isolates trivial
height-one inertia as the smallest normalization-route bridge and the
stronger global ordinary-coherence, pair-stability, and meromorphic
embedding package for a direct D-module route.  It does not solve
`CLM-061`.

Because the same assistant constructed and reviewed the packet, this
is local adversarial evidence only and cannot confer independent or
frozen authority.
