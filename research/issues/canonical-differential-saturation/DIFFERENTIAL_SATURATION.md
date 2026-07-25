# Differential Saturation of Finite Seeds

> **Claims:** `CDS-002`, `CDS-003`, `CDS-004`  
> **Authority:** `MUTABLE_NONAUTHORITATIVE`

## 1. Minimal stable closure

For a finite full seed \(M_0\subset L\), put

\[
S(M_0)=\operatorname{Sat}_D(M_0)
 =\sum_{a,b\ge0}B\,D_P^aD_Q^b(M_0).
\]

### Proposition 1.1

\(S(M_0)\) is a full \(B\)-submodule of \(L\), stable under
\(D_P,D_Q\), and contained in every pair-stable \(B\)-submodule of
\(L\) that contains \(M_0\).

### Proof

Fullness follows from \(M_0\subset S(M_0)\).  For
\(c\in B\) and \(m\in M_0\),

\[
D_P(cD_P^aD_Q^b m)
 =(\partial_Pc)D_P^aD_Q^b m
  +cD_P^{a+1}D_Q^b m,
\]

and the analogous formula holds for \(D_Q\).  Commutativity removes
any ordering ambiguity.  Minimality is immediate from closure under
both derivations.  \(\square\)

## 2. Finite saturation cannot coexist with ramification

### Theorem 2.1 — finite-seed obstruction

For every finite full \(B\)-lattice \(M_0\subset L\),

\[
S(M_0)\text{ finite over }B
 \quad\Longrightarrow\quad
O/B\text{ has no height-one ramification}.
\]

### Proof

If \(S(M_0)\) is finite, Proposition 1.1 makes it a finite full
pair-stable \(B\)-lattice.  Localize at a ramified height-one base
prime.  At least one of \(\partial_P,\partial_Q\) is transverse to the
reduced branch divisor.  The ramified-DVR no-lattice theorem excludes
a full finite lattice stable under that derivation.  Therefore no
ramified height-one prime exists.  \(\square\)

This is stronger than failure of a particular presentation.  It
excludes every finite seed, including non-divisorial seeds, if the
claim is that its complete differential saturation is finite.

## 3. Canonical normalization seed

The finite normalization \(O\) is intrinsic to the actual Keller
function-field extension, so \(S(O)\) is a canonical candidate.

### Theorem 3.1 — normalization-saturation equivalence

The following are equivalent.

1. \(S(O)\) is finite over \(B\).
2. \(S(O)=O\).
3. \(O\) is stable under \(D_P,D_Q\).
4. \(O/B\) has no height-one ramification.

Under these conditions \(S(O)\) is a finite full pair-stable lattice,
and the maintained multiplier-order/discriminant route forces
\([L:K]=1\).

### Proof

`2 => 1` is finiteness of normalization.  `2 <=> 3` follows from the
minimality of saturation.  `3 => 4` is the local transverse
ramification obstruction.  If `4` holds, both base translations
extend through every height-one unramified normalization.  Since

\[
O=\bigcap_{\operatorname{ht}q=1}O_q\subset L,
\]

they preserve \(O\), proving `4 => 3`.  The final conditional
conclusion is the predecessor multiplier-order theorem.  \(\square\)

The theorem proves coherence of the canonical saturation only by
assuming the exact condition whose absence is the issue #4 boundary.
It is an equivalence, not a construction of new boundedness.

## 4. Exact local escape

Let \(R\) be a characteristic-zero DVR with uniformizer \(t\), and
let a ramified tame factor have strict-henselian normal form

\[
S=R[s]/(s^e-t),\qquad e>1.
\]

Normalize a transverse derivation by \(\delta(t)=1\).  Its lift
satisfies

\[
D(s)=\frac{1}{e}s^{1-e}=\frac1e t^{-1}s.
\]

For every integer \(N\) and \(0<j<e\),

\[
D(t^Ns^j)=\left(N+\frac je\right)t^{N-1}s^j
\]

and hence

\[
D^n(t^Ns^j)
 =\prod_{r=0}^{n-1}\left(N+\frac je-r\right)
  t^{N-n}s^j.
\]

No factor vanishes: an integer cannot equal \(N+j/e\) when
\(0<j<e\).  The valuation tends to \(-\infty\).

Every full finite local lattice contains \(t^NS\) for some \(N\), so
it contains \(t^Ns^j\) for all \(j\).  Its saturation therefore has
no lower valuation bound.  A finite \(R\)-module inside the field is
valuation bounded.  Thus the local saturation is nonfinite.

For a general transverse derivation with \(\delta(t)\) a unit, the
same expression is the lowest-valuation term; derivatives of the unit
contribute only higher-valuation terms.  The escape conclusion is
unchanged.

## 5. Pole-bounded source intersections

Let \(E_1,\ldots,E_r\) be the divisorial components of
\(Y\setminus\operatorname{Spec}A\), and for
\(\mathbf N=(N_1,\ldots,N_r)\in\mathbf N^r\) define

\[
M(\mathbf N)
 =A\cap\{f\in L:w_{E_i}(f)\ge-N_i\ \forall i\}.
\]

Because elements of \(A\) are regular at every height-one point of
the source open, this is the affine section module of the reflexive
divisorial sheaf

\[
\mathcal O_Y\!\left(\sum_iN_iE_i\right).
\]

It is finite and full over \(B\).

### Theorem 5.1

1. If some \(E_i\) is ramified, \(S(M(\mathbf N))\) is nonfinite for
   every \(\mathbf N\).
2. If \(E_i\) is unramified and \(N_i>0\) is realized by an actual
   pole, \(S(M(\mathbf N))\) is nonfinite.
3. The only zero-pole candidate is \(M(\mathbf0)=O\), and its
   saturation is finite exactly under Theorem 3.1.

### Proof

The first assertion is Theorem 2.1, or the explicit local escape in
Section 4.  For the second, let \(p\) be the image of \(E_i\) on the
base and let \(q\) be its generic point on \(Y\).  Choose a canonical
frame member \(D\) whose base derivation is transverse to \(p\).
Because \(O_q/B_p\) is unramified, \(D\) preserves the DVR
\(S=O_q\).  For a uniformizer \(s\) of \(S\),

\[
a=D(s)\in S^\times.
\]

Indeed, a base uniformizer is a unit times \(s\), and its derivative
is a unit modulo \(s\).

By the actual-pole hypothesis there is an element of the localized
module with valuation \(-m<0\).  Write it as

\[
f=u s^{-m},\qquad u\in S^\times.
\]

Let \((m)_n=m(m+1)\cdots(m+n-1)\), with \((m)_0=1\).  Induction gives

\[
D^n(f)=(-1)^n(m)_n u a^n s^{-m-n}+g_n,
\qquad w_q(g_n)\ge -m-n+1.
\]

For the induction step, \(D\) lowers valuation by at most one because
it preserves \(S\) and \(D(s)=a\) is a unit.  Differentiating the
displayed leading term produces the unique term of valuation
\(-m-n-1\); derivatives of its coefficient and of \(g_n\) have
valuation at least \(-m-n\).  Its coefficient is
\((-1)^{n+1}(m)_{n+1}ua^{n+1}\), which is nonzero in characteristic
zero.  Hence

\[
w_q(D^n f)=-m-n
\]

for every \(n\).  The localized saturation is not valuation bounded,
whereas every finite \(B_p\)-module in \(L\) is.  Therefore the global
saturation is nonfinite.  The third assertion follows from normality
and Theorem 3.1.  \(\square\)

Reflexive hulls and finite intersections do not change this
codimension-one calculation.

## 6. Multiplier, dual, and translate constructions

For a finite full seed \(M_0\), its multiplier ring

\[
O_{M_0}=(M_0:M_0)=\{z\in L:zM_0\subset M_0\}
\]

is a finite \(B\)-order with total quotient field \(L\).  If
\(M_0\) is pair-stable, the Leibniz identity

\[
D(z)m=D(zm)-zD(m)
\]

shows that \(O_{M_0}\) is pair-stable.  This implication is only
one-way.  For the exact control

\[
B=\mathbf C[P,Q],\qquad K=L=\operatorname{Frac}(B),
\qquad M_0=P B,
\]

we have \(D_P(M_0)\not\subset M_0\) because \(D_P(P)=1\), while
cancellation gives \((M_0:M_0)=B\), which is pair-stable.

Thus taking a multiplier can create stability relative to an unstable
presentation, but no automatic construction follows: proving directly
that a finite full multiplier ring is pair-stable already produces the
stable order required by the predecessor theorem.  For a nonzero
rank-one reflexive fractional \(O\)-module \(I\), height-one
localization gives \((I_q:I_q)=O_q\), hence

\[
(I:I)=O.
\]

Consequently the named divisorial candidates—trace duals, inverse
differents, conductor or canonical twists, and reflexive source-pole
modules—do not hide a different multiplier order.

At a ramified height-one point, these full fractional lattices retain
the same intrinsic tame residue-class multiset.  Changing a
logarithmic lattice shifts representatives by integers on fixed
monodromy eigenspaces; multiplication by a ramification parameter may
also permute the character labels.  Neither operation removes the
nonzero classes in \(\mathbf Q/\mathbf Z\), so ordinary transverse
stability still fails.

A finite intersection of finitely many derivative translates remains
a finite seed, not a stable saturation.  Closing it under all
derivatives returns to Theorem 2.1.

## 7. Exact bounded-ambient formulation

For a finite full seed \(M_0\), the following are equivalent.

1. \(S(M_0)\) is finite.
2. There is a finite \(B\)-module \(N\subset L\) such that
   \(M_0\subset N\) and \(D_P(N),D_Q(N)\subset N\).
3. There is a fixed finite \(B\)-module containing every
   \(D_P^aD_Q^b(M_0)\).

The nontrivial missing input is not Noetherianity; it is construction
of this fixed ambient module.  Every known source-pole estimate
provides a growing family

\[
D_P^aD_Q^b(M_{\mathbf m})
 \subset
M_{\mathbf m+a\boldsymbol\sigma_P+b\boldsymbol\sigma_Q},
\]

not one fixed \(N\).

## 8. Subclass where saturation exists

If the original Keller morphism is finite, then \(A\) is a finite full
\(B\)-algebra and is exactly stable under \(D_P,D_Q\).  Thus
\(S(A)=A\), and the standard finite-etale argument gives degree one.
This is the proper/finite subclass and does not address the
nonproperness boundary of a hypothetical counterexample.
