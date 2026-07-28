# Primary-Source Audit and Hypothesis Bindings

> **Authority:** `MUTABLE_NONAUTHORITATIVE`  
> **Purpose:** identify exactly what external theory is used and what it does not prove.

The load-bearing coherence and residue equivalences in this packet are
proved directly in `DIFFERENTIAL_SATURATION.md`,
`DMODULE_ROUTE.md`, and `LOCAL_RESIDUES.md`.  The sources below bind
the categorical vocabulary and standard extension theorems; none is
cited as a theorem that constructs the missing ordinary stable
lattice.

## 1. Regular singular connections and canonical logarithmic extensions

**Primary source**

Pierre Deligne, *Equations différentielles à points singuliers
réguliers*, Lecture Notes in Mathematics 163, Springer, 1970,
DOI `10.1007/BFb0061194`.

**Exact use**

- Chapter II, especially the logarithmic-pole and existence sections,
  supplies canonical logarithmic extensions after choosing residue
  representatives.
- Proposition II.5.4 gives a unique extension with at most logarithmic
  poles and residue eigenvalues in a chosen section of
  \(\mathbf C\to\mathbf C/\mathbf Z\).
- Corollary II.5.6 relates local monodromy to the exponential of the
  residue, subject to the stated nonresonance convention.

**Hypothesis match**

The finite-cover local system has finite monodromy, hence is regular
singular.  The packet uses Deligne only to justify the existence and
functoriality of coherent logarithmic lattices.  Ordinary
\(\partial_t\)-stability is checked directly and fails in the Kummer
model.

**Not licensed**

Deligne's logarithmic extension theorem does not assert that the
connection matrix has no pole, that residues are integral, or that
the underlying meromorphic D-module is finite over the ordinary
structure sheaf.

Official text:
`https://publications.ias.edu/sites/default/files/Number9.pdf`.

## 2. Intermediate extension and perverse minimality

**Primary source**

A. A. Beilinson, J. Bernstein, and P. Deligne, *Faisceaux pervers*,
Astérisque 100, 1982/1983.

**Exact use**

The source supplies the perverse intermediate-extension operation and
its no-boundary-subobject/no-boundary-quotient characterization.

**Hypothesis match**

The finite-etale pushforward local system on a smooth dense open gives
the constructible object to which intermediate extension applies.
The packet uses only the categorical minimality statement.

**Not licensed**

Perverse intermediate extension is not a theorem of ordinary
\(\mathcal O\)-coherence.  The Kummer calculation shows that its
regular-holonomic D-module can remain \(\mathcal O\)-infinite when
local monodromy is nontrivial.  Even local ordinary coherence at every
generic height-one point would not, by this categorical theorem alone,
prove global \(\mathcal O\)-coherence, control codimension-two behavior,
or provide a torsion-free embedding into the meromorphic sheaf with
generic fiber \(L\).

Official text:
`https://publications.ias.edu/sites/default/files/Faisceaux%20pervers.pdf`.

## 3. Regular holonomic Riemann-Hilbert correspondence

**Primary source**

Masaki Kashiwara, “The Riemann-Hilbert Problem for Holonomic
Systems,” *Publ. Res. Inst. Math. Sci.* 20 (1984), 319–365,
DOI `10.2977/PRIMS/1195181610`.

**Exact use**

The source binds the correspondence between regular holonomic
systems and constructible/perverse data and records stability of
regular holonomicity under the appropriate operations.

**Hypothesis match**

The local finite-monodromy connection is regular singular, so its
minimal extension lies in the regular-holonomic category.

**Not licensed**

Holonomicity is coherence over \(\mathcal D\), not over
\(\mathcal O\).  No step in this packet infers an ordinary finite
lattice from Kashiwara's theorem.

Official text:
`https://ems.press/journals/prims/articles/3160`.

## 4. Gauss-Manin connection

**Primary source**

Nicholas M. Katz and Tadao Oda, “On the differentiation of De Rham
cohomology classes with respect to parameters,” *J. Math. Kyoto
Univ.* 8 (1968), 199–213,
DOI `10.1215/kjm/1250524135`.

**Exact use**

This source binds the construction and integrability of the
Gauss-Manin connection on relative de Rham cohomology under its
smooth-family hypotheses.

**Hypothesis match**

The packet invokes it only to distinguish a coherent cohomology
connection from a full lattice in the generic field.  No
Gauss-Manin finiteness theorem is used to bridge that distinction.

**Not licensed**

A relative cohomology module is not automatically a submodule of
\(L\), and finite-dimensional fibers do not provide fullness.

## 5. Reflexive sheaves

**Primary source**

Robin Hartshorne, “Stable Reflexive Sheaves,” *Math. Ann.* 254
(1980), 121–176, DOI `10.1007/BF01467074`.

**Exact use**

The source provides the standard codimension-one/reflexive framework.
For the specific affine regular surface \(B=\mathbf C[P,Q]\), the
packet also relies on the maintained repository proof that finite
reflexive \(B\)-modules are locally free.

**Not licensed**

Taking a reflexive hull does not automatically preserve an arbitrary
connection or erase a height-one fractional residue.  Stability is
rechecked by intersection of height-one localizations.

## 6. Multiplier rings and fractional-ideal twists

The module-to-order bridge is inherited from
`research/issues/source-reflexive-lattice/MULTIPLIER_RING.md` and is
also checked directly here.

- For a finite full module \(M\), \((M:M)\) is finite and has total
  quotient field \(L\).
- The Leibniz identity proves the one-way implication
  \(D(M)\subset M\Rightarrow D((M:M))\subset(M:M)\).
- The converse is false: for \(M=P B\subset K=L\), the seed is not
  \(\partial_P\)-stable while \((M:M)=B\) is stable.
- For every nonzero rank-one reflexive fractional \(O\)-module \(I\),
  height-one localization and intersection give \((I:I)=O\).

No external theorem is used to turn seed coherence into multiplier
stability.  If a full multiplier ring is proved pair-stable directly,
that ring is already the desired stable order.  For trace duals,
inverse differents, canonical modules, conductor twists, and other
rank-one divisorial candidates, the multiplier operation returns
\(O\) and does not bypass the normalization obstruction.

Likewise, changing logarithmic lattices shifts residue representatives
by integers on fixed monodromy eigenspaces, while fractional
ramification-parameter twists may permute the eigenspace labels.  The
invariant statement used by the packet is preservation of the full
class multiset in \(\mathbf Q/\mathbf Z\), not a common integer shift
in every chosen basis.

## 7. Zariski Main, normalization, purity, and finite-etale triviality

The packet inherits the repository bindings for:

- Grothendieck's Zariski Main Theorem and finite normalization
  factorization;
- purity of the branch locus under the maintained regular/normal
  finite-map hypotheses; and
- SGA 1, Exposé XII, Théorème 5.1, together with simple
  connectedness of \(\mathbf C^2\), for triviality of connected finite
  etale covers of \(\mathbf A^2_{\mathbf C}\).

These results are consumed only after a finite full stable lattice or
no-height-one-ramification statement has been obtained.  They are not
used to infer that statement.

## 8. Direct computations replacing advanced black boxes

The following load-bearing points are proved in the packet rather
than outsourced.

1. The signs and commutator of \(D_P,D_Q\).
2. Stability and minimality of differential saturation.
3. The Kummer residue and repeated-derivative formulas.
4. Nonvanishing of the falling-factorial coefficients in
   characteristic zero.
5. The inertia-cycle residue multiset.
6. Equivalence between an embedded ordinary local coherent lattice
   and trivial inertia for the permutation connection.
7. Failure of \(\mathcal O\)-finiteness in the Kummer and localization
   controls.
8. Persistence of the full residue-class multiset under integer
   shifts, duals, conductors, fractional-ideal twists, and reflexive
   hulls.
9. The one-way multiplier-stability implication, its converse
   countercontrol, and \((I:I)=O\) for rank-one reflexive fractional
   \(O\)-modules.
10. Extraction of a global finite stable module from a globally
    coherent, connection-compatible, torsion-free embedding into the
    meromorphic sheaf with generic fiber \(L\).

## 9. Source-audit conclusion

Primary D-module and logarithmic-extension theory provides canonical
regular-holonomic or logarithmically coherent objects.  It does not
provide the ordinary \(\mathcal O\)-coherent, translation-stable full
lattice required by issue #4.

The smallest surviving normalization-route hypothesis is trivial
height-one inertia, equivalently no height-one ramification.  At a
generic height-one point this is also equivalent to ordinary
\(\mathcal O\)-coherence of the full local intermediate extension.  A
direct global D-module construction requires the strictly more
explicit package of global \(\mathcal O\)-coherence, ordinary
translation stability, and a torsion-free embedding into the
meromorphic sheaf with generic fiber \(L\).  None of the audited
sources supplies either missing Keller-specific input.
