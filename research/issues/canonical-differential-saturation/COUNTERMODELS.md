# Countermodels and Mutation Controls

> **Claims:** `CDS-006`, controls for `CDS-002`–`CDS-008`  
> **Authority:** `MUTABLE_NONAUTHORITATIVE`

The examples below test proposed bridges.  None is asserted to be a
counterexample to the planar Jacobian conjecture.

## 1. Finite Kummer cover: regular holonomic but not O-finite

Let

\[
\pi:\mathbf A^2_{s,u}\longrightarrow\mathbf A^2_{t,u},
\qquad t=s^e,\quad e>1.
\]

This is finite, normal, and rational.  It is ramified along \(s=0\)
and is not a Keller map because its Jacobian is \(es^{e-1}\).

On the finite-etale complement \(t\ne0\), the pushforward connection
is the permutation local system of an \(e\)-cycle.  It decomposes
after adjoining characters into rank-one regular-singular pieces with

\[
t\partial_t e_j=\frac je e_j.
\]

Each nonzero character generates arbitrary negative powers of \(t\)
under \(\partial_t\).  The minimal regular-holonomic extension is
cyclic over \(\mathcal D\) but infinite over \(\mathcal O\).
Meanwhile the normalization itself is a coherent logarithmic lattice.

This simultaneously falsifies:

- holonomic \(\Rightarrow\) \(\mathcal O\)-finite;
- regular singular \(\Rightarrow\) ordinary stable lattice; and
- coherent logarithmic lattice \(\Rightarrow\) ordinary stable
  lattice.

The missing Keller condition is source etaleness across the entire
specified affine source.

## 2. Unramified nonproper open immersion

Let

\[
j:U=D(t)\subset\mathbf A^2_{t,u}\hookrightarrow\mathbf A^2.
\]

The local system is trivial and there is no ramification.  However,

\[
j_*\mathcal O_U
 =\mathcal O_{\mathbf A^2}[t^{-1}]
 =\bigcup_{m\ge0}t^{-m}\mathcal O_{\mathbf A^2}
\]

is not coherent over \(\mathcal O_{\mathbf A^2}\), and

\[
\partial_t^n(t^{-1})=(-1)^n n!t^{-n-1}.
\]

The D-module direct image/localization is holonomic but
\(\mathcal O\)-infinite.  In contrast, the intermediate extension of
the trivial local system is the smooth connection
\(\mathcal O_{\mathbf A^2}\).

This proves that \(j_+\), \(j_*\), and \(j_{!*}\) cannot be
interchanged in the coherence argument.  It also shows that absence
of ramification does not make every positive pole stage stable.

Here \(U\cong\mathbf G_m\times\mathbf A^1\), not the required
\(\mathbf A^2\) source.  The example is a categorical and
nonproperness control.

## 3. Tame non-Galois cubic

For

\[
z^3-3z-t=0,
\]

the generic cover is non-Galois.  Near \(t=2\), the ramified
quadratic factor has local parameter relation

\[
t-2=s^2(s-3).
\]

The transverse derivation has a simple fractional pole, producing the
class \(1/2\).  Thus the local obstruction does not rely on a global
deck group or Galois decomposition.

## 4. Singular branch

For

\[
s^e=p^2-q^3,
\]

the cusp branch is singular only at codimension two.  Its generic
normal covector is nonzero, and the pair residue remains

\[
\frac je(2p,-3q^2).
\]

A logarithmic weighted Euler field preserves the normalization, but a
transverse translation does not.  Singular branch geometry does not
cancel generic fractional residues.

## 5. Exact-symplectic Laurent control

Let

\[
P=s^e,\qquad Q=z,\qquad
x=s,\qquad y=es^{e-1}z
\]

on \(D(s)\times\mathbf A^1\).  Then

\[
Q=\frac{y}{ex^{e-1}},\qquad
\frac{\partial(P,Q)}{\partial(x,y)}=1,
\]

and

\[
x\,dy-P\,dQ=\frac{e-1}{e}\,d(xy).
\]

The boundary still has ramification index \(e\) and fractional
classes \(j/e\).  Therefore the symplectic volume identity and an
exact primitive relation do not remove the obstruction.

This is not a polynomial Keller pair on the full affine plane:
\(Q\) is Laurent in \((x,y)\).

## 6. Several boundary components

For

\[
U=D(sr)\subset\mathbf A^2_{s,r},
\]

the ring of functions is

\[
\mathbf C[s,r,s^{-1},r^{-1}]
 =\bigcup_{m,n\ge0}s^{-m}r^{-n}\mathbf C[s,r].
\]

The commuting translations independently increase the two pole
bounds.  Commutativity makes mixed differentiation order-independent
but provides no common finite rectangle.

## 7. Multiplier stability does not imply seed stability

Take

\[
B=\mathbf C[P,Q],\qquad K=L=\operatorname{Frac}(B),
\qquad M=P B.
\]

The module \(M\) is finite and full, but

\[
\partial_P(P)=1\notin P B,
\]

so it is not stable under the canonical translation
\(\partial_P\).  Nevertheless, cancellation in the domain \(B\)
gives

\[
(M:M)=\{z\in K:zP B\subset P B\}=B,
\]

and \(B\) is stable under both \(\partial_P,\partial_Q\).

Thus stability of a seed is sufficient but not necessary for
stability of its multiplier ring.  This control does not bypass issue
#4: it is the degree-one case, and in a nontrivial extension a direct
proof that a finite full multiplier ring is pair-stable is already a
construction of the desired stable order.  For the named rank-one
divisorial candidates, the inherited calculation \((I:I)=O\) returns
the normalization and therefore does not hide ramification.

## 8. Rank-three rational A2-open control already in the repository

The issue #3 packet records a connected smooth rational normal
finite-flat rank-three algebra containing an open \(\mathbf A^2\)
but not globally monogenic.  Its displayed \(\mathbf A^2\) open is
not etale over the target.  It demonstrates that rationality and the
mere presence of an affine-plane open do not supply the Keller
differential frame.

This packet consumes only that scoped lesson; it does not alter the
issue #3 construction.

## 9. Exact condition not modeled

A decisive countermodel to `CDS-007` would need all of:

1. a normal finite cover \(Y\to\mathbf A^2\);
2. an open \(U\cong\mathbf A^2\);
3. all ramification contained in \(Y\setminus U\);
4. the map \(U\to\mathbf A^2\) etale with constant polynomial
   Jacobian in affine coordinates;
5. nontrivial height-one inertia.

Such an object would be a genuine planar Keller counterexample
framework.  None of the controls above satisfies all five
conditions.  The audit therefore isolates, rather than assumes away,
the polynomial-source condition.
