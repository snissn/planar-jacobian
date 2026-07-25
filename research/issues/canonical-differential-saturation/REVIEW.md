# Renewed Local Adversarial Review

> **Review mode:** `local-adversarial-review`  
> **Reviewer role:** same-session adversarial reviewer, not an independent reviewer  
> **Candidate revision:** `d8c9dc19ad6201042afb315ccab57489c863105b`  
> **Candidate base:** `652a5e252626fa5816445651245e8a8946cee53e`  
> **Owned path:** `research/issues/canonical-differential-saturation/`  
> **Disposition:** `ACCEPT_SCOPED`  
> **Authority after review:** `MUTABLE_NONAUTHORITATIVE`

The corrected scientific candidate was pinned before this renewed
review.  No candidate proof or validation file was edited while the
review was conducted.  Reviews pinned to earlier candidates are
superseded for the current packet head.

## 1. Corrections adjudicated in this review

### Multiplier implication

The false necessity direction

\[
(M:M)\text{ stable}\Longrightarrow M\text{ stable}
\]

has been removed.  For

\[
B=\mathbf C[P,Q],\quad K=L=\operatorname{Frac}(B),
\quad M=PB,
\]

we have \(D_P(P)=1\notin PB\) while \((M:M)=B\) is pair-stable.
The packet uses only the valid implication from seed stability to
multiplier stability.  A directly stable finite full multiplier ring
is already the desired stable order; the named rank-one reflexive
fractional \(O\)-modules satisfy \((I:I)=O\).

### Fractional-ideal twists

Changing a logarithmic lattice shifts residue representatives by
integers on fixed monodromy eigenspaces, while multiplication by a
ramification parameter can permute the tame character labels.  The
correct invariant is the complete residue-class multiset in
\(\mathbf Q/\mathbf Z\), which is unchanged.

### Fullness of finite intersections

A finite intersection of pole stages or derivative translates is
subject to the finite-seed obstruction only if its generic fiber is
all of \(L\).  If the intersection is not full, it is not a candidate
for the required lattice.  The construction table and saturation
proof now state this condition explicitly.

### Images of source-boundary divisors

The normalization morphism

\[
\nu:Y=\operatorname{Spec}O\longrightarrow\operatorname{Spec}B
\]

is finite.  If \(q\subset O\) is the height-one generic prime of a
divisorial component \(E\), and \(p=q\cap B\), then
\(B/p\subset O/q\) is finite integral.  Hence

\[
\dim(B/p)=\dim(O/q)=1.
\]

Since \(B\) is a two-dimensional polynomial ring, \(p\) is
height one.  Thus every divisorial source-boundary component maps onto
a height-one base divisor; no contracted-divisor or codimension-two
image is silently covered by the DVR proof.  The unramified
positive-pole argument is therefore legitimately localized at the
DVR extension \(B_p\subset O_q\).

## 2. Reviewed statements

The review adjudicates only these packet-local statements.

1. `CDS-001`: the canonical derivations have the displayed signs and
   commute.
2. `CDS-002`: finite differential saturation of any finite full seed
   excludes height-one ramification.
3. `CDS-003`: the normalization-seed saturation is finite exactly
   when the normalization is unramified in codimension one.
4. `CDS-004`: every divisorial source boundary maps onto a height-one
   base divisor; ramified pole stages and genuine positive unramified
   pole stages have nonfinite saturation.
5. `CDS-005`: for the finite-cover permutation connection, an embedded
   ordinary coherent extension across one generic height-one point is
   equivalent to trivial inertia there.
6. `CDS-006`: regular holonomicity or logarithmic coherence does not
   imply ordinary structure-sheaf finiteness.
7. `CDS-007`: trivial inertia at every height-one divisor is the
   surviving normalization route; a direct D-module route also needs
   global ordinary coherence, a connection preserving both unscaled
   translations, and a torsion-free meromorphic embedding with generic
   fiber \(L\).
8. `CDS-008`: the audited dual, multiplier, intersection, jet, and
   cohomological constructions do not bypass that bridge.

No global `CLM-*` status is reviewed or promoted.

## 3. Exact reviewed proof and validation bytes

`ACCEPT_SCOPED` is bound to the exact bytes of these eleven files at
candidate revision `d8c9dc19ad6201042afb315ccab57489c863105b`:

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

`README.md` is the packet summary rather than a load-bearing proof
file.  Its scientific prose was checked against those candidate bytes.
Its permitted post-candidate edit is limited to recording the completed
review in the metadata header.

`REVIEW.md`, `HANDOFF.md`, and `INTEGRATION.json` are review and
transport metadata.  They may record the review pin, PR number, exact
scope, risks, validation, and handoff, but may not expand the accepted
mathematics.  A later edit to one of the eleven reviewed files, or a
scientific-prose edit to `README.md`, requires a new pinned review.

## 4. Claim-to-file and dependency bindings

| Claim | Reviewed proof files | Packet dependencies | Inherited repository dependencies |
|---|---|---|---|
| `CDS-001` | `FOUNDATIONS.md` | `J(P,Q)=1`; finite separability of `L/K` | canonical-derivation context associated with `CLM-003` |
| `CDS-002` | `FOUNDATIONS.md`, `DIFFERENTIAL_SATURATION.md`, `LOCAL_RESIDUES.md` | `CDS-001`; finite full seed; transverse ramified-DVR escape | maintained issue #4 local-DVR theorem; no global promotion |
| `CDS-003` | `DIFFERENTIAL_SATURATION.md`, `LOCAL_RESIDUES.md` | `CDS-002`; normal height-one intersection for `O`; extension through unramified DVRs | `CLM-003`; `CLM-010`–`CLM-013` only for the conditional degree-one consequence |
| `CDS-004` | `DIFFERENTIAL_SATURATION.md`, `LOCAL_RESIDUES.md`, `CONSTRUCTION_TABLE.md` | `CDS-002`; finiteness of `Y/B`; actual pole-bearing localized section; characteristic-zero nonvanishing; fullness before applying Theorem 2.1 | mutable source-reflexive-lattice pole filtration |
| `CDS-005` | `DMODULE_ROUTE.md`, `LOGARITHMIC_LATTICES.md`, `LOCAL_RESIDUES.md` | finite-etale permutation connection on `V`; tame inertia cycles; embedded full local lattice | no global coherence theorem inherited or asserted |
| `CDS-006` | `DMODULE_ROUTE.md`, `LOGARITHMIC_LATTICES.md`, `COUNTERMODELS.md`, `SOURCE_AUDIT.md` | explicit Kummer and open-localization controls | Deligne/BBD/Kashiwara vocabulary only; none licenses ordinary `O`-finiteness |
| `CDS-007` | `DIFFERENTIAL_SATURATION.md`, `DMODULE_ROUTE.md` | `CDS-003`, `CDS-005`; normalization route distinguished from the stronger global D-module route | `CLM-010`–`CLM-013` only after a stable full module exists; `CLM-061` remains open |
| `CDS-008` | `CONSTRUCTION_TABLE.md`, `COUNTERMODELS.md`, `DIFFERENTIAL_SATURATION.md`, `SOURCE_AUDIT.md` | one-way multiplier implication; `(I:I)=O`; fullness condition for intersections; residue-multiset invariance | mutable predecessor multiplier-order bridge; no existence result imported |

The validation files check encoded identities and mutations; they do
not promote inherited candidates or replace mathematical review.

## 5. Unresolved risks and explicit exclusions

1. **No Keller-specific inertia exclusion.**  Polynomial source
   geometry has not been shown to force trivial height-one inertia.
2. **No stable lattice or order.**  No finite non-divisorial
   source-derived module, stable multiplier ring, or equivalent order
   is constructed for an arbitrary Keller pair.
3. **No global D-module bridge.**  Generic height-one ordinary
   coherence does not establish global \(\mathcal O\)-coherence,
   codimension-two control, preservation by both translations, or a
   compatible meromorphic embedding.
4. **Mutable predecessor dependencies.**  This review does not
   independently re-adjudicate `CLM-010`–`CLM-013` or `CLM-061`.
5. **Countermodels omit the decisive source condition.**  None is a
   polynomial Keller counterexample on the full affine plane.
6. **Review independence.**  The reviewer is the constructing
   assistant; promotion or freeze requires a distinct reviewer.
7. **Primary-source limit.**  The cited sources justify the named
   categorical operations and residue framework, not the missing
   ordinary-coherence or inertia theorem.

## 6. Independent recomputation

### Canonical frame

Direct substitution gives

\[
D_P(P)=1,\quad D_P(Q)=0,\quad
D_Q(P)=0,\quad D_Q(Q)=1.
\]

The commutator restricts to zero on \(K=\mathbf C(P,Q)\), and finite
separability of \(L/K\) forces it to vanish.

### Saturation, finite intersections, and pole escape

Leibniz and commutativity make

\[
\sum_{a,b\ge0}B D_P^aD_Q^b(M_0)
\]

the minimal pair-stable closure.  The local ramification obstruction
applies precisely when \(M_0\) is finite and full.  Thus a nonfull
finite intersection is excluded as a candidate rather than fed into
the theorem.

For a divisorial source boundary, finiteness of \(Y/B\) gives the
height-one DVR pair \(B_p\subset O_q\) above.  In the unramified case,
take an actual pole-bearing section \(f=us^{-m}\) and a transverse
field with \(D(s)=a\in O_q^\times\).  Then

\[
D^n(f)=(-1)^n(m)_nua^ns^{-m-n}+O(s^{-m-n+1}),
\]

so pole order grows without assuming that a bare monomial globalizes.

### Kummer residues and twists

For \(t=s^e\),

\[
D^n(t^Ns^j)=
\prod_{r=0}^{n-1}(N+j/e-r)t^{N-n}s^j.
\]

For \(0<j<e\), the valuation is unbounded below.  For every integer
\(k\), the multisets \(\{(j+k)/e\}\) and \(\{j/e\}\) agree modulo
\(\mathbf Z\).

### Multiplier and D-module logic

For stable \(M\), Leibniz proves stability of \((M:M)\); \(M=PB\)
disproves the converse.  For rank-one reflexive fractional
\(O\)-modules, height-one principalness and normal intersection give
\((I:I)=O\).

A length-\(e\) inertia cycle has classes \(j/e\bmod\mathbf Z\).  A
nonintegral character is modeled by

\[
\mathcal D/\mathcal D(t\partial_t-\alpha),
\]

which is regular holonomic but \(\mathcal O\)-infinite.  The local
criterion is not a global coherence or pair-stability theorem.

## 7. Adversarial mutations

| Mutation | Result |
|---|---|
| Contract a divisorial `E_i` to codimension two | Impossible inside finite `Y -> Spec B`; finite integral quotients preserve the divisor dimension. |
| Apply the finite-seed theorem to a nonfull intersection | Invalid; the packet now makes fullness an explicit premise. |
| Replace translations by logarithmic fields | Kummer normalization becomes stable; the theorem is weakened. |
| Twist fixed eigenspaces by base-divisor powers | Representatives shift by integers; nonzero classes survive. |
| Twist by a ramification parameter | Character labels may permute; the complete class multiset survives. |
| Infer multiplier instability from seed instability | False for `M=PB`; no such converse is used. |
| Prove a full multiplier stable directly | This already constructs the desired stable order. |
| Take determinant, trace, norm, or invariants | Individual characters or fullness are lost. |
| Remove ramification but retain nonproper boundary | `j_+` may remain an infinite localization; `j_{!*}` is different. |
| Invoke exact symplectic data | The Laurent control retains `j/e`. |
| Invoke Noetherianity | Invalid without a fixed finite ambient module. |
| Invoke Gauss-Manin or compact support | Produces cohomology, not a full embedded lattice in `L`. |

## 8. Primary-source limits

The review checked the packet's use of Deligne for logarithmic
extensions and residue/monodromy, BBD for intermediate extension,
Kashiwara for the regular-holonomic Riemann–Hilbert framework,
Katz–Oda for Gauss-Manin, and Hartshorne for reflexive
codimension-one language.  None supplies the missing ordinary
\(\mathcal O\)-coherence, trivial-inertia, pair-stability, or
meromorphic-embedding theorem.

## 9. Automated review evidence

The two exact remote validator files were reconstructed byte for byte;
their local Git blob hashes matched the repository blobs
`053d71a550992dfe6be5edb99d1ab0e578c557a3` and
`1428959b91216d65eebd0f1c12a6d10681c8b7e0`.  Byte compilation and
enlarged runs passed:

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

The checks do not substitute for mathematical review.

## 10. Blocking-question answers

- **Finite full pair-stable lattice constructed?** No.
- **Height-one ramification excluded for every Keller pair?** No.
- **A contracted divisorial boundary silently covered?** No.
- **Finite-seed obstruction applied without fullness?** No.
- **Holonomicity or logarithmic stability conflated with ordinary pair
  stability?** No.
- **Invalid multiplier converse used?** No.
- **Local height-one coherence promoted to global coherence?** No.
- **Both unscaled translations omitted from the direct bridge?** No in
  the candidate; transport metadata is required to preserve them.
- **Degree one claimed unconditionally?** No.

## 11. Verdict

`ACCEPT_SCOPED`.

The corrected candidate proves the normalization-saturation
coherence equivalence, finite-seed and divisorial pole-stage
obstructions, the generic height-one inertia criterion, and exact
counterexamples to categorical shortcuts.  It isolates trivial
height-one inertia as the smallest normalization-route bridge and the
stronger ordinary-coherence, pair-stability, and embedding package for
a direct D-module route.  It does not solve `CLM-061`.

Because the same assistant constructed and reviewed the packet, this
review is local adversarial evidence only and cannot confer independent
or frozen authority.
