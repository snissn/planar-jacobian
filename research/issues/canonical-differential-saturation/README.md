# Canonical Differential Saturation, Coherent Lattices, and Height-One Ramification

> **Role:** `research-worker`  
> **Task issue:** `#4`  
> **Owned path:** `research/issues/canonical-differential-saturation/`  
> **Base revision:** `main@652a5e252626fa5816445651245e8a8946cee53e`  
> **Authority:** `MUTABLE_NONAUTHORITATIVE`  
> **Scientific disposition:** `SCOPED_EQUIVALENCE_COUNTEREXAMPLE_AND_REDUCTION`  
> **Review mode:** `local-adversarial-review` — `ACCEPT_SCOPED` at `ab498bd9f40fdb36137fbe8a52658555a3eef004`

## Question

Let

\[
B=\mathbf C[P,Q],\qquad K=\operatorname{Frac}(B),\qquad
L=\mathbf C(x,y),
\]

for a polynomial Keller pair with \(J(P,Q)=1\).  Let \(O\) be the
normalization of \(B\) in \(L\), and let

\[
D_P=Q_y\partial_x-Q_x\partial_y,\qquad
D_Q=-P_y\partial_x+P_x\partial_y.
\]

Can the actual source open immersion produce a finite full
\(B\)-lattice \(M\subset L\) stable under both \(D_P,D_Q\)?

## Exact disposition

No new finite pair-stable lattice is constructed.  The packet proves a
canonical coherence criterion and identifies why the standard
D-module and logarithmic constructions do not cross it.

1. **Normalization-saturation equivalence.**  The canonical module

   \[
   \operatorname{Sat}_D(O)
   =\sum_{a,b\ge0}B\,D_P^aD_Q^b(O)
   \]

   is finite over \(B\) if and only if the finite normalization has no
   height-one ramification.  In the unramified case the saturation is
   already \(O\).  In the ramified case every nontrivial tame
   character escapes to arbitrarily negative valuation.

2. **Arbitrary finite seeds.**  For every finite full
   \(B\)-module \(M_0\subset L\), finite generation of
   \(\operatorname{Sat}_D(M_0)\) forces absence of height-one
   ramification.  Thus differential saturation cannot manufacture the
   missing lattice while retaining ramification.

3. **Pole-bounded source stages.**  The source open supplies a
   canonical ind-system of finite reflexive pole modules.  Since the
   normalization \(Y\to\operatorname{Spec}B\) is finite, every
   divisorial boundary component maps onto a height-one base divisor;
   there is no contracted-divisor case outside the DVR argument.
   Saturating any stage with a ramified component is nonfinite.  At an
   unramified omitted divisor, any stage containing an actual pole is
   also nonfinite under a transverse canonical translation.  The proof
   starts from a pole-bearing section of the stage and tracks its
   unique lowest-valuation term; it does not assume that a bare local
   monomial belongs to the global module.  Only the zero-pole
   normalization stage can possibly be finite and stable.

4. **Multiplier qualification.**  A pair-stable finite seed has a
   pair-stable multiplier ring, but the converse need not hold:
   \(M=P B\subset K=L\) is not \(\partial_P\)-stable whereas
   \((M:M)=B\) is stable.  Therefore seed instability alone does not
   exclude a stable multiplier.  A direct proof that a finite full
   multiplier ring is pair-stable is already a construction of the
   stable order required by the predecessor theorem.  For every named
   rank-one divisorial candidate in this packet, \((I:I)=O\), so the
   multiplier operation returns the normalization and does not bypass
   the ramification criterion.

5. **Generic height-one D-module criterion.**  On the maximal
   finite-etale locus, the pushforward is the rank-\([L:K]\)
   permutation connection.  At the generic point of a height-one
   divisor, a cycle of inertia length \(e\) contributes residue
   classes

   \[
   0,\frac1e,\ldots,\frac{e-1}{e}\pmod{\mathbf Z}.
   \]

   A logarithmic Deligne lattice exists and is coherent, but an
   embedded ordinary \(\mathcal O\)-coherent lattice stable under a
   transverse translation exists exactly when every inertia cycle has
   length one.  This is a local codimension-one criterion.  It does not
   by itself prove global coherence of a named intermediate extension,
   control codimension-two behavior, or supply an embedding into
   \(L\).

6. **Holonomicity is insufficient.**  A regular holonomic
   \(\mathcal D\)-module may be infinitely generated over
   \(\mathcal O\).  Both a Kummer finite cover and the open immersion
   \(D(t)\hookrightarrow\mathbf A^2\) provide exact controls.  The
   latter also shows that \(j_+\) and \(j_{!*}\) answer different
   questions: localization is \(\mathcal O\)-infinite while the
   intermediate extension of the trivial local system is
   \(\mathcal O\).

7. **Smallest surviving bridge.**  Prove from the polynomial Keller
   source that the full finite-etale permutation local system has
   trivial inertia at every height-one divisor.  The
   normalization-saturation theorem then makes \(O\) a finite full
   pair-stable lattice and enters the maintained multiplier-order
   route.  Equivalently only at each generic height-one point, this is
   the ordinary-coherence criterion for the local intermediate
   extension.

   A direct global D-module construction is a distinct, stronger
   formulation: prove that the full intermediate extension is
   globally \(\mathcal O\)-coherent, is preserved by both ordinary
   unscaled translations, and admits a connection-compatible
   torsion-free embedding into the meromorphic sheaf with generic
   fiber \(L\).  The audited D-module theorems do not derive this
   package from the Keller hypotheses.

Accordingly, the first supported requested dispositions are:

- **(6)** counterexamples to the proposed implications
  “holonomic \(\Rightarrow\) \(\mathcal O\)-finite” and
  “logarithmic lattice \(\Rightarrow\) ordinary stable lattice”; and
- **(7)** reduction to the exact height-one trivial-inertia statement,
  with the stronger global coherence-and-embedding package isolated
  for a direct D-module route.

## Packet-local claims

| Label | Status | Statement |
|---|---|---|
| `CDS-001` | `verified_internal` | The displayed canonical derivations have the required signs and commute. |
| `CDS-002` | `candidate_proved` | For every finite full seed, finite differential saturation forces no height-one ramification. |
| `CDS-003` | `candidate_proved` | The normalization-seed saturation is finite iff the normalization is unramified in codimension one. |
| `CDS-004` | `candidate_proved` | Every divisorial source boundary maps onto a height-one base divisor; ramified pole stages and genuine positive unramified pole stages have nonfinite saturation. |
| `CDS-005` | `candidate_proved` | At a generic height-one point of the finite-cover permutation connection, an embedded ordinary coherent lattice exists iff local inertia is trivial. |
| `CDS-006` | `counterexample` | Regular holonomic or logarithmically coherent extensions need not be finite over the ordinary structure sheaf. |
| `CDS-007` | `open_bridge` | Derive trivial height-one inertia from the polynomial Keller source; a direct global D-module route additionally requires global coherence, preservation by both unscaled translations, and a torsion-free embedding into \(L\). |
| `CDS-008` | `negative_audit` | The audited dual, canonical, jet, and cohomological constructions do not bypass `CDS-007`; multiplier stability is a separate stable-order condition, not an automatic consequence of seed coherence or instability. |

These are issue-local labels.  They allocate or promote no global
`CLM-*` identifier.

## Artifact map

- `FOUNDATIONS.md` — setup, signs, dependencies, and definitions.
- `DIFFERENTIAL_SATURATION.md` — finite-seed and normalization-seed
  coherence theorems.
- `DMODULE_ROUTE.md` — finite-etale connection, generic height-one
  criterion, and exact global coherence-and-embedding bridge.
- `LOGARITHMIC_LATTICES.md` — Deligne lattices, residues, regularity,
  and the ordinary/logarithmic distinction.
- `LOCAL_RESIDUES.md` — Kummer calculation, pair spectrum, singular
  and non-Galois mutations.
- `CONSTRUCTION_TABLE.md` — candidate-by-candidate audit.
- `COUNTERMODELS.md` — finite-cover, open-immersion, multiplier,
  non-Galois, and exact-symplectic controls.
- `SOURCE_AUDIT.md` — primary-source bindings and hypothesis limits.
- `REVIEW.md` — pinned local adversarial review.
- `HANDOFF.md` — proposed shared deltas and next exact task.
- `verify_local_residues.py`, `verify_global_bridges.py`, and
  `verify_all.py` — exact regression checks.
- `INTEGRATION.json` — issue-owned integration manifest.

## Nonclaims

This packet does not prove that a finite full pair-stable lattice
exists for an arbitrary Keller pair.  It does not prove that the
normalization is unramified, that the source is finite over the target,
that a holonomic direct image is \(\mathcal O\)-coherent, that the full
intermediate extension is globally coherent and embedded in \(L\), or
that the planar Jacobian conjecture holds.  Passing validators records
algebraic and repository consistency only.
