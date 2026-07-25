# Logarithmic Lattices, Regular Singularities, and Residues

> **Claims:** `CDS-005`, `CDS-006`  
> **Authority:** `MUTABLE_NONAUTHORITATIVE`

## 1. Local regular-singular form

On a punctured trait with parameter \(t\), a regular singular
connection admits a logarithmic lattice \(M_{\log}\) for which

\[
\nabla:M_{\log}\longrightarrow
M_{\log}\otimes\frac{dt}{t}.
\]

Equivalently, \(t\partial_t\) preserves \(M_{\log}\).  The residue is
the endomorphism induced by \(t\nabla_{\partial_t}\) on
\(M_{\log}/tM_{\log}\).

Choosing a different logarithmic lattice shifts residue eigenvalues
by integers.  Therefore the eigenvalue classes in
\(\mathbf C/\mathbf Z\) are intrinsic.

For a finite-cover permutation local system the monodromy is finite,
so the local connection is regular singular and semisimple after
tame splitting.  Its intrinsic classes are rational.

## 2. Deligne lattice in the Kummer model

For

\[
t=s^e
\]

the finite normalization basis \(1,s,\ldots,s^{e-1}\) satisfies

\[
tD_t(s^j)=\frac je s^j.
\]

Thus \(S=R[s]/(s^e-t)\) is a coherent logarithmic lattice with residue
spectrum

\[
0,\frac1e,\ldots,\frac{e-1}{e}.
\]

It is not stable under \(D_t\) when \(e>1\), because

\[
D_t(s^j)=\frac je\,t^{-1}s^j.
\]

This model disproves any bridge from existence of a coherent
logarithmic lattice to existence of an ordinary stable lattice.

## 3. Integer shifts and canonical windows

Multiplying a local generator by \(t^m\) changes the residue
representative

\[
\alpha\longmapsto\alpha+m.
\]

A Deligne extension selects one representative from each class by
choosing a strip or section of \(\mathbf C\to\mathbf C/\mathbf Z\).
No choice turns a nonzero class \(j/e\) into zero.

Trace duals, inverse differents, canonical modules, and conductor
twists amount locally to such integral shifts, possibly with a
permutation of characters.  Their class multisets are unchanged.

## 4. Two canonical derivations

At a reduced branch \(h(P,Q)=0\), strict-henselian tame coordinates
give \(h=us^e\).  On the \(j\)-th tame character, the pair of
logarithmic residues is

\[
\frac je(\overline{h_P},\overline{h_Q}).
\]

Choose \(a,b\) with

\[
ah_P+bh_Q\equiv1\pmod h
\]

and define the normal and tangent fields

\[
N=aD_P+bD_Q,\qquad
T=-h_QD_P+h_PD_Q.
\]

Then the residue pair is

\[
\operatorname{Res}(hN)=j/e,\qquad
\operatorname{Res}(hT)=0.
\]

The commuting pair therefore contains one transverse obstruction and
one tangential zero direction.  Commutativity makes the residues
compatible; it does not cancel the transverse class.

## 5. Combining sheets

An \(e\)-cycle permutation representation contains a one-dimensional
invariant line with residue class zero.  The complementary characters
have classes \(1/e,\ldots,(e-1)/e\).

Taking invariants, trace, norm, determinant, or a symmetric
combination can discard the obstructed characters.  A full lattice in
\(L\) must retain all \(e\) dimensions.  Combining sheets therefore
cannot cancel the full obstruction.

The determinant residue is

\[
\sum_{j=0}^{e-1}\frac je=\frac{e-1}{2}.
\]

For odd \(e\) this is integral even though every nonzero character
class survives.  Determinant-line exactness is too weak.

## 6. Irregularity and Stokes data

The local system arising from a finite etale cover has finite
monodromy.  Around a normal-crossing compactification divisor it has
regular singularities; there is no nontrivial exponential irregular
part or Stokes filtration for this finite local system.

This does not prove that every global D-module direct image attached
to the nonproper original map is represented solely by that
intermediate extension.  Open direct image can retain localization
pieces.  The packet therefore makes no global “no irregularity”
claim beyond the finite local-system summand on the finite-etale
locus.

## 7. Singular and non-Galois branch

Residues are computed at the generic point of each irreducible
reduced branch component, which is smooth.  Singular points of the
branch curve have codimension two in the target surface and do not
erase a generic height-one obstruction.

Galois symmetry is unnecessary.  After strict henselization, a
non-Galois extension separates into valuation factors; every
ramified factor has a tame inertia cycle and its own fractional
classes.  A full stable lattice would project to a stable lattice in
each factor, which is impossible for a nontrivial cycle.

## 8. Compatibility with exact symplectic data

The Keller identity

\[
dP\wedge dQ=dx\wedge dy
\]

and the polynomial exact primitive constrain determinant and
principal-part data.  They do not provide an operation that changes
each residue class modulo \(\mathbf Z\).  The existing Laurent
exact-symplectic control realizes ramification and the same fractional
spectrum outside the polynomial \(\mathbf A^2\)-source class.

Therefore exact symplectic compatibility does not upgrade a
logarithmic lattice to an ordinary stable lattice.
