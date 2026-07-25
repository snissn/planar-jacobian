# Two-Derivation Fractional-Residue Spectrum

> **Authority:** `MUTABLE_NONAUTHORITATIVE`  
> **Claims:** `SRL-004`, `SRL-005`, `SRL-010`

## 1. Residues along an asymptotic-value curve

Let `h(P,Q)` be irreducible and let `w` be a valuation of `L` above the
height-one prime `(h)`.  Write `e=e(w/h)`.  After strict henselization and an
unramified base change, choose a tame parameter `s` with

\[
h=u s^e,
\]

where `u` is a unit.  Unit-correction terms are regular and vanish in the
fractional residue.  On the `j`-th tame graded character,

\[
\operatorname{Res}_w(hD_P)=\frac je\,\overline{h_P},\qquad
\operatorname{Res}_w(hD_Q)=\frac je\,\overline{h_Q},
\]

for `j=0,...,e-1`, with residue-degree multiplicity.

Thus the pair spectrum is

\[
\boxed{
\operatorname{FRS}^{(2)}_w
 =\left\{
 \frac je(\overline{h_P},\overline{h_Q}):0\le j<e
 \right\}
 \quad\text{modulo common integral normal shifts}.}
\]

A change of local equation `h' = v h` multiplies the displayed normal vector
by the residue of the unit `v`; the intrinsic object is the scalar class
`j/e mod Z` tensored with the normal covector of the divisor.

## 2. Normal and tangent frame

At the generic point of `h=0`, the gradient is not zero.  Choose
`a,b in B_(h)` with

\[
a h_P+b h_Q\equiv1\pmod h.
\]

Define

\[
N=aD_P+bD_Q,
\qquad
T=-h_QD_P+h_PD_Q.
\]

Then

\[
N(h)\equiv1\pmod h,
\qquad
T(h)=0.
\]

The pair residue diagonalizes geometrically as

\[
\operatorname{Res}_w(hN)=j/e,
\qquad
\operatorname{Res}_w(hT)=0.
\]

Consequently the two canonical spectra contain exactly one transverse tame
obstruction and one tangential zero direction.  They do not supply two
independent fractional invariants.

## 3. Why integer shifts do not cancel the pair

Multiplying a lattice generator by `h^m` changes the pair residue by

\[
m(\overline{h_P},\overline{h_Q}).
\]

It therefore changes `j/e` by the common integer `m`; it does not permit
independent shifts in the two coordinates.  In the normal/tangent frame the
same operation is

\[
(j/e,0)\longmapsto(j/e+m,0).
\]

For `e>1`, some class remains nonzero in `Q/Z`.  Apparent cancellation in one
chosen coordinate merely means that the other coordinate is the transverse
one.

## 4. Commutativity and integrability

The field derivations satisfy

\[
[D_P,D_Q]=0.
\]

Their logarithmic residue endomorphisms commute.  This is the local flatness
condition for the rank-`[L:K]` connection.  Flatness implies that the residue
operators may be simultaneously analyzed after tame splitting, but it does
not alter their eigenvalue classes.

The scaled fields `hD_P,hD_Q` need not commute exactly.  In the tame normal
form, however, their residue matrices are scalar multiples of the same
diagonal tame-character operator, so they commute after reduction.  The
remaining commutator terms are regular tangential terms and do not alter the
fractional eigenvalue classes.  There is therefore no hidden commutator term
capable of replacing `j/e` by an integer.

## 5. Determinant cancellation is too weak

For one totally ramified factor, the determinant-line residue is

\[
\sum_{j=0}^{e-1}\frac je=\frac{e-1}{2}.
\]

For odd `e` this is an integer, even though the individual classes
`1/e,...,(e-1)/e` remain nonzero.  Hence a determinant, trace, or volume-form
calculation can lose the obstruction.  The full character multiset, not only
its sum, is required.

This explains why the exact symplectic identity can coexist with nontrivial
fractional residues: it controls a determinant line, whereas lattice
stability is a statement about every tame character.  The complete
principal-part formula in `research/issue-5/PRINCIPAL_PARTS.md` gives the
parallel warning: vanishing of one logarithmic-residue coefficient does not
remove the other negative Laurent coefficients.

## 6. Exact conclusion

- If a finite full module is stable under both `D_P,D_Q`, the normal member
  `N` is stable, so the nonzero classes force `e=1`.
- Without a finite stable module, the pair spectrum is diagnostic rather than
  contradictory.  Ramified exact-symplectic local models realize the same
  spectrum.
- Commutativity, integer gauge shifts, and the Keller volume identity do not
  add a cancellation law beyond the one-derivation transverse obstruction.
