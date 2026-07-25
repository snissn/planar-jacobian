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
`2a0300d3dbfba2a58622d3e60351c18dd28a094a` is superseded.

## 1. Corrections that triggered renewed review

The earlier construction audit overstated multiplier stability.  The
necessity direction

\[
(M:M)\text{ stable}\Longrightarrow M\text{ stable}
\]

is false.  The corrected candidate includes the exact control

\[
B=\mathbf C[P,Q],\quad K=L=\operatorname{Frac}(B),
\quad M=PB,
\]

for which \(D_P(P)=1\notin PB\) but \((M:M)=B\) is pair-stable.
The packet now uses only the valid implication from seed stability to
multiplier stability.  A directly proved stable full multiplier ring
is already the stable order sought by the predecessor route, while
all named rank-one reflexive fractional \(O\)-modules satisfy
\((I:I)=O\).

The renewed audit also corrects residue-twist language.  Changing a
logarithmic lattice shifts representatives by integers on fixed
monodromy eigenspaces; multiplication by a ramification parameter can
permute tame character labels.  The invariant statement is that the
full residue-class multiset in \(\mathbf Q/\mathbf Z\) is unchanged.

## 2. Reviewed statements

The review adjudicates only these packet-local statements.

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
   surviving normalization-route bridge; a direct D-module route also
   requires global ordinary coherence and a torsion-free meromorphic
   embedding with generic fiber \(L\).
8. `CDS-008`: the audited dual, canonical, jet, and cohomological
   constructions do not bypass that bridge; multiplier stability is
   a separate stable-order condition.

No global `CLM-*` status is reviewed or promoted.

## 3. Exact reviewed proof and validation bytes

`ACCEPT_SCOPED` is bound to the exact bytes of these eleven files at
candidate revision `7523052bde101036bc1753acbc37ba6be78e895b`:

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
file.  Its scientific prose was checked for consistency with those
exact candidate bytes.  Its sole post-candidate change records the
completed review in the metadata header; it does not change a claim,
proof, dependency, or nonclaim.

`REVIEW.md`, `HANDOFF.md`, and `INTEGRATION.json` are review and
transport metadata.  Their post-candidate edits may record the pinned
review, PR number, exact scope, risks, and integration handoff, but may
not expand the accepted mathematics.  Any later edit to one of the
eleven reviewed files, or any scientific-prose edit to `README.md`,
requires a new pinned review before `integration-ready` remains valid.

## 4. Claim-to-file and dependency bindings

| Claim | Reviewed proof files | Packet dependencies | Inherited repository dependencies |
|---|---|---|---|
| `CDS-001` | `FOUNDATIONS.md` | `J(P,Q)=1`; finite separability of `L/K` | canonical-derivation context associated with `CLM-003` |
| `CDS-002` | `FOUNDATIONS.md`, `DIFFERENTIAL_SATURATION.md`, `LOCAL_RESIDUES.md` | `CDS-001`; finite full seed; transverse ramified-DVR escape | maintained issue #4 local-DVR theorem; no global promotion |
| `CDS-003` | `DIFFERENTIAL_SATURATION.md`, `LOCAL_RESIDUES.md` | `CDS-002`; normal height-one intersection for `O`; extension through unramified DVRs | `CLM-003`; `CLM-010`–`CLM-013` only for the conditional degree-one consequence |
| `CDS-004` | `DIFFERENTIAL_SATURATION.md`, `LOCAL_RESIDUES.md` | `CDS-002`; actual pole-bearing localized section; characteristic-zero nonvanishing | mutable source-reflexive-lattice pole filtration |
| `CDS-005` | `DMODULE_ROUTE.md`, `LOGARITHMIC_LATTICES.md`, `LOCAL_RESIDUES.md` | finite-etale permutation connection on `V`; tame inertia cycles; embedded full local lattice | no global coherence theorem inherited or asserted |
| `CDS-006` | `DMODULE_ROUTE.md`, `LOGARITHMIC_LATTICES.md`, `COUNTERMODELS.md`, `SOURCE_AUDIT.md` | explicit Kummer and open-localization controls | Deligne/BBD/Kashiwara vocabulary only; none licenses ordinary `O`-finiteness |
| `CDS-007` | `DIFFERENTIAL_SATURATION.md`, `DMODULE_ROUTE.md` | `CDS-003`, `CDS-005`; normalization route distinguished from the stronger global D-module route | `CLM-010`–`CLM-013` only after a stable full module exists; `CLM-061` remains open |
| `CDS-008` | `CONSTRUCTION_TABLE.md`, `COUNTERMODELS.md`, `DIFFERENTIAL_SATURATION.md`, `SOURCE_AUDIT.md` | valid one-way multiplier implication; `(I:I)=O`; residue-multiset invariance | mutable predecessor multiplier-order bridge; no existence result imported |

The validation files check encoded algebraic identities and mutations;
they do not promote inherited candidates or replace mathematical
review.

## 5. Unresolved risks and explicit exclusions

1. **No Keller-specific inertia exclusion.**  Polynomial source
   geometry has not been shown to force trivial height-one inertia.
2. **No stable lattice or order.**  No finite non-divisorial
   source-derived module, stable multiplier ring, or equivalent order
   is constructed for an arbitrary Keller pair.
3. **No global D-module bridge.**  Generic height-one ordinary
   coherence does not establish global \(\mathcal O\)-coherence,
   codimension-two control, or a compatible meromorphic embedding.
4. **Mutable predecessor dependencies.**  This review does not
   independently re-adjudicate `CLM-010`–`CLM-013` or `CLM-061`.
5. **Countermodels omit the decisive source condition.**  None is a
   polynomial Keller counterexample on the full affine plane.
6. **Review independence.**  The reviewer is the constructing
   assistant; promotion or freeze requires a distinct reviewer.
7. **Primary-source limit.**  The cited sources justify the named
   categorical operations and residue framework, not the missing
   ordinary-coherence or inertia theorem.

These are the exact open boundaries preserved by the scoped result.

## 6. Independent recomputation

### Canonical frame

Direct substitution gives

\[
D_P(P)=1,\quad D_P(Q)=0,\quad
D_Q(P)=0,\quad D_Q(Q)=1.
\]

The commutator restricts to zero on \(K=\mathbf C(P,Q)\), and finite
separability of \(L/K\) forces it to vanish.

### Saturation and pole escape

Leibniz and commutativity make

\[
\sum_{a,b\ge0}B D_P^aD_Q^b(M_0)
\]

the minimal pair-stable closure.  If finite, it is a full finite local
lattice excluded by the transverse ramified-DVR theorem.

At an unramified omitted divisor, take an actual pole-bearing section
\(f=us^{-m}\) and a transverse field with \(D(s)=a\in S^\times\).
Then

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
\(k\),

\[
\{(j+k)/e\bmod\mathbf Z:0\le j<e\}
=\{j/e\bmod\mathbf Z:0\le j<e\}.
\]

### Multiplier logic

For stable \(M\), the identity

\[
D(z)m=D(zm)-zD(m)
\]

proves stability of \((M:M)\).  The seed \(M=PB\) disproves the
converse.  For rank-one reflexive fractional \(O\)-modules,
height-one principalness and normal intersection give \((I:I)=O\).

### D-module criterion

A length-\(e\) inertia cycle has classes \(j/e\bmod\mathbf Z\).  A
nonintegral character is modeled by

\[
\mathcal D/\mathcal D(t\partial_t-\alpha),
\]

which is regular holonomic but generates unbounded negative powers as
an \(\mathcal O\)-module.  All characters are ordinary-coherent at the
generic height-one point exactly when every cycle has length one.
This local equivalence is not promoted to global coherence.

## 7. Adversarial mutations

| Mutation | Result |
|---|---|
| Replace translations by logarithmic fields | Kummer normalization becomes stable; the theorem has been weakened. |
| Twist fixed eigenspaces by base-divisor powers | Representatives shift by integers; nonzero classes survive. |
| Twist by a ramification parameter or fractional ideal | Character labels may permute; the complete class multiset survives. |
| Infer multiplier instability from seed instability | False for `M=PB`; the packet uses no such converse. |
| Prove a full multiplier stable directly | This already constructs the desired stable order. |
| Take determinant, trace, norm, or invariants | Individual characters are lost; fullness or obstruction data is lost. |
| Drop Galois symmetry | The non-Galois cubic retains a ramified valuation factor. |
| Allow a singular branch | The generic height-one obstruction remains. |
| Remove ramification but retain nonproper boundary | `j_+` can remain an infinite localization; `j_{!*}` is different. |
| Invoke exact symplectic data | The Laurent control retains `j/e`. |
| Invoke Noetherianity | Invalid without a fixed finite ambient module. |
| Invoke Gauss-Manin or compact support | Produces cohomology objects, not a full embedded lattice in `L`. |

## 8. Primary-source limits

The review checked the packet's use of:

- Deligne, LNM 163, II.5.4 and II.5.6, for logarithmic extensions and
  the monodromy/residue relation;
- Beilinson–Bernstein–Deligne, *Faisceaux pervers*, for intermediate
  extension and boundary-subquotient minimality;
- Kashiwara, PRIMS 20 (1984), for the regular-holonomic
  Riemann–Hilbert framework;
- Katz–Oda, J. Math. Kyoto Univ. 8 (1968), for Gauss-Manin
  construction and integrability;
- Hartshorne, Math. Ann. 254 (1980), for reflexive codimension-one
  language.

None supplies the missing ordinary \(\mathcal O\)-coherence,
trivial-inertia, or meromorphic-embedding theorem.

## 9. Automated review evidence

The candidate scripts were byte-compiled and rerun at default and
enlarged bounds:

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

Default totals were `7901` local checks and `548` global checks, both
`PASS`.  These checks do not substitute for mathematical review.

## 10. Blocking-question answers

- **Finite full pair-stable lattice constructed?** No.
- **Height-one ramification excluded for every Keller pair?** No.
- **Holonomicity conflated with ordinary coherence?** No.
- **Logarithmic stability conflated with ordinary stability?** No.
- **Invalid multiplier converse used?** No.
- **All fractional twists described as one common integer shift?** No.
- **Local height-one coherence promoted to global coherence?** No.
- **Determinant cancellation promoted to full rank?** No.
- **Countermodels claimed to satisfy the polynomial source condition?** No.
- **Degree one claimed unconditionally?** No.

## 11. Verdict

`ACCEPT_SCOPED`.

The candidate proves the normalization-saturation equivalence,
finite-seed and pole-stage obstructions, the generic height-one inertia
criterion, and counterexamples to categorical shortcuts.  It isolates
trivial height-one inertia as the smallest normalization-route bridge
and the stronger coherence-plus-embedding package for a direct
D-module route.  It does not solve `CLM-061`.

Because the same assistant constructed and reviewed the packet, this
review is local adversarial evidence only and cannot confer independent
or frozen authority.
