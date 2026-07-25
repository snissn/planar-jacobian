# Algebraic D-Module and Intermediate-Extension Route

> **Claims:** `CDS-005`, `CDS-006`, `CDS-007`  
> **Authority:** `MUTABLE_NONAUTHORITATIVE`

## 1. The finite-etale permutation connection

Let \(V\subset\operatorname{Spec}B\) be a dense open set over which
the normalization is finite etale and over which the specified source
open contains all sheets.  Write

\[
\pi_V:Y_V\longrightarrow V.
\]

Then

\[
\mathcal E=\pi_{V*}\mathcal O_{Y_V}
\]

is a vector bundle of rank \(d=[L:K]\).  The target derivations lift
uniquely through the finite etale map and give an integrable
connection

\[
\nabla:\mathcal E\to\mathcal E\otimes\Omega_V^1.
\]

Its horizontal local system is the permutation representation on the
\(d\) geometric sheets.  Its generic fiber, with multiplication
forgotten, is the \(K\)-vector space \(L\).

The connection on \(\mathcal E\) is canonical on \(V\).  The issue is
the nature of its extension across the complement.

## 2. Local inertia and residue classes

Let \(H=(t=0)\) be the generic point of an irreducible boundary or
branch divisor.  After strict henselization, a tame inertia orbit of
length \(e\) has Kummer form

\[
t=s^e.
\]

In the basis \(1,s,\ldots,s^{e-1}\), the logarithmic operator
\(tD_t\) acts by

\[
\operatorname{diag}
\left(0,\frac1e,\ldots,\frac{e-1}{e}\right).
\]

Equivalently, the local permutation monodromy is an \(e\)-cycle and
has all \(e\)-th roots of unity as eigenvalues.  The sign relating
residue eigenvalues to monodromy depends on whether the connection is
written on sections or horizontal solutions; the multiset of classes
in \(\mathbf Q/\mathbf Z\) and its triviality are unaffected.

For a general permutation representation, decompose inertia into
cycles of lengths \(e_1,\ldots,e_r\).  The full residue-class multiset
is

\[
\bigsqcup_{\nu=1}^r
\left\{0,\frac1{e_\nu},\ldots,
      \frac{e_\nu-1}{e_\nu}\right\}
\pmod{\mathbf Z}.
\]

## 3. Ordinary coherent extension criterion

### Theorem 3.1 — height-one D-module coherence criterion

For the finite-cover permutation connection near the generic point of
\(H\), the following are equivalent.

1. Its full generic fiber admits a finite
   \(\mathcal O\)-lattice stable under the ordinary transverse
   derivation \(D_t\).
2. It admits an \(\mathcal O\)-coherent extension carrying an
   ordinary integrable connection across \(H\).
3. Every local inertia cycle has length one.
4. The finite normalization is unramified over \(H\).
5. Every fractional residue class is zero in
   \(\mathbf Q/\mathbf Z\).

### Proof

`1 => 5` is the local no-lattice theorem, character by character.
`2 => 1` follows by taking the generic-fiber embedding and removing
torsion.  `5 <=> 3` follows from the cycle multiset above, and
`3 <=> 4` is the local finite-cover inertia criterion in
characteristic zero.  If inertia is trivial, the finite cover is
etale over the trait and the normalization itself is preserved by
\(D_t\), proving `4 => 2`.  \(\square\)

This theorem is proved locally and does not require a global
Riemann-Hilbert equivalence.

## 4. Logarithmic extension versus ordinary extension

A regular singular connection with finite monodromy has coherent
Deligne logarithmic lattices.  In a chosen residue window, a Kummer
cycle has residues \(j/e\).  The logarithmic connection preserves the
lattice under \(tD_t\), but

\[
D_t(s^j)=\frac je\,t^{-1}s^j
\]

leaves the lattice only when \(j=0\).

Thus the statement

> the canonical local system has a coherent logarithmic extension

is true in the ramified Kummer model and cannot imply no
ramification.  The required statement is ordinary
\(\mathcal O\)-coherence under unscaled translations.

## 5. The intermediate extension

Let \(j_V:V\hookrightarrow\mathbf A^2\).  On the constructible or
regular-holonomic side, one may form the intermediate extension of
the full local system/connection, denoted schematically by

\[
j_{V!*}\mathcal E.
\]

It is characterized by having no nonzero subobject or quotient
supported entirely on the boundary.  This categorical minimality does
not say that the underlying \(\mathcal O\)-module is coherent.

At a generic height-one point, the Kummer summand with nonzero
residue class is represented by a regular holonomic cyclic
\(\mathcal D\)-module of the form

\[
\mathcal D/\mathcal D(t\partial_t-\alpha),
\qquad \alpha\notin\mathbf Z.
\]

The relation gives

\[
\partial_t e=\alpha t^{-1}e,
\]

and repeated differentiation generates all negative powers of \(t\).
The module is cyclic over \(\mathcal D\) but infinite over
\(\mathcal O\).

### Corollary 5.1

The full intermediate extension is
\(\mathcal O\)-coherent at the generic point of every height-one
divisor if and only if all local inertia is trivial there.

This is exactly `CDS-007`, not a consequence of holonomicity.

## 6. Direct image distinctions

Several objects must not be conflated.

- On \(V\), \(\pi_{V*}\mathcal O_{Y_V}\) is a finite locally free
  \(\mathcal O_V\)-module with connection.
- The algebraic D-module direct image of the original quasi-finite
  map can be holonomic while containing localization behavior at
  nonproper boundary.
- \(j_{V+}\mathcal E\) permits boundary poles.
- \(j_{V!*}\mathcal E\) removes boundary-supported subquotients, but
  nontrivial local monodromy still gives an
  \(\mathcal O\)-infinite regular-singular module.
- \(j_{V*}\) on ordinary quasi-coherent modules can be an unbounded
  pole union and need not be coherent.
- \(j_!\) is not an ordinary quasi-coherent extension by zero in the
  algebraic category; its useful meaning here is constructible or
  D-module-theoretic.

No direct-image theorem used in this packet asserts ordinary
\(\mathcal O\)-finiteness.

## 7. Local-to-global theorem

### Theorem 7.1 — exact property X

Assume the full permutation connection \(\mathcal E\) has an
extension \(\mathcal M\) on \(\mathbf A^2\) satisfying:

1. \(\mathcal M\) is coherent over
   \(\mathcal O_{\mathbf A^2}\);
2. its generic fiber is identified with \(L\) as a \(K\)-vector
   space;
3. its connection is stable under both ordinary translations
   \(\partial_P,\partial_Q\).

Then \(M=\Gamma(\mathbf A^2,\mathcal M)\), embedded in \(L\), is a
finite full pair-stable \(B\)-lattice.  Its reflexive multiplier ring
is a finite locally free stable order, and the maintained
discriminant theorem forces \([L:K]=1\).

### Proof

Affineness turns \(\mathcal O\)-coherence into finite generation over
\(B\).  The generic-fiber identification gives fullness.  The
connection gives pair stability.  Apply the multiplier-order theorem
and then the stable-order discriminant theorem.  \(\square\)

One may replace conditions 1–3 by the named statement:

> the full intermediate extension \(j_{V!*}\mathcal E\) is an
> ordinary \(\mathcal O\)-coherent connection with generic fiber
> \(L\).

By Theorem 3.1, this named statement is equivalent in codimension one
to trivial inertia/no ramification.  The Keller hypotheses currently
supply the local system and connection, but not this
\(\mathcal O\)-coherence.

## 8. Cohomological constructions

### Relative de Rham degree zero

For a finite etale map, relative de Rham degree zero reproduces the
finite-etale algebra/connection \(\mathcal E\).  It does not alter its
inertia or residue spectrum.

### Gauss-Manin and higher direct images

Gauss-Manin modules are coherent under their own properness or
regularity hypotheses, but their fibers are cohomology groups, not
the generic field \(L\).  A finite-dimensional cohomology group does
not become a full rank-\([L:K]\) lattice in \(L\) without a canonical
generic-fiber embedding and the two ordinary translation actions.

### Compact support and duality

Compactly supported direct images, dualizing complexes, and perverse
duality can exchange \(j_!\) and \(j_*\) or dual residue
representatives.  They do not remove the nonzero classes modulo
\(\mathbf Z\).

### Finite jets

Finite-order jets along a boundary are coherent, but a transverse
derivation raises jet or principal-part order.  The directed union is
D-stable; no finite jet order is.

Thus none of these constructions establishes property X as stated.
