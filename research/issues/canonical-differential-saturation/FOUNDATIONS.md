# Foundations and Exact Setup

> **Claims:** `CDS-001`, foundations for `CDS-002`–`CDS-008`  
> **Authority:** `MUTABLE_NONAUTHORITATIVE`

## 1. Keller data

Let \(P,Q\in\mathbf C[x,y]\) satisfy

\[
J(P,Q)=P_xQ_y-P_yQ_x=1.
\]

Set

\[
A=\mathbf C[x,y],\qquad B=\mathbf C[P,Q]\cong\mathbf C[U,V],
\]
\[
K=\operatorname{Frac}(B),\qquad L=\operatorname{Frac}(A).
\]

The Jacobian condition makes \(P,Q\) algebraically independent and
the induced morphism

\[
F:\operatorname{Spec}A\longrightarrow\operatorname{Spec}B
\]

etale and quasi-finite.  Let \(O\) be the normalization of \(B\) in
the finite separable field extension \(L/K\), and put
\(Y=\operatorname{Spec}O\).  Zariski Main gives the source open
immersion

\[
j:\operatorname{Spec}A\hookrightarrow Y
\]

with ring direction \(O\to A\), followed by the finite normalization
map \(Y\to\operatorname{Spec}B\).

No argument below assumes that \(A\) is finite over \(B\), that
\(Y\to\operatorname{Spec}B\) is etale, or that \(j\) is surjective.

## 2. Canonical derivations and signs

Define

\[
D_P=Q_y\partial_x-Q_x\partial_y,\qquad
D_Q=-P_y\partial_x+P_x\partial_y.
\]

Then

\[
\begin{aligned}
D_P(P)&=Q_yP_x-Q_xP_y=1, &
D_P(Q)&=Q_yQ_x-Q_xQ_y=0,\\
D_Q(P)&=-P_yP_x+P_xP_y=0, &
D_Q(Q)&=-P_yQ_x+P_xQ_y=1.
\end{aligned}
\]

Hence

\[
D_P|_B=\partial_P,\qquad D_Q|_B=\partial_Q.
\]

The commutator kills both \(P\) and \(Q\).  It is therefore a
\(K\)-derivation of \(L\).  Since \(L/K\) is finite separable in
characteristic zero, every \(K\)-derivation of \(L\) vanishes, so

\[
[D_P,D_Q]=0.
\]

This proves `CDS-001` independently of the predecessor packet.

## 3. Lattices and ordinary stability

A **finite full \(B\)-lattice in \(L\)** is a finite torsion-free
\(B\)-submodule \(M\subset L\) such that

\[
M\otimes_BK=L.
\]

It is **pair-stable** when

\[
D_P(M)\subset M,\qquad D_Q(M)\subset M.
\]

Ordinary pair-stability is stronger than logarithmic stability.  At a
divisor \(h=0\), a logarithmic lattice need only be preserved by
\(hD_P,hD_Q\), or by the sheaf of logarithmic vector fields.  The
issue #4 discriminant route requires ordinary stability under the
unscaled target translations.

## 4. Differential saturation

For a finite full seed \(M_0\subset L\), define

\[
\operatorname{Sat}_D(M_0)
 =\sum_{a,b\ge0}B\,D_P^aD_Q^b(M_0)\subset L.
\]

Because \(D_P,D_Q\) commute and restrict to derivations of \(B\), this
is the smallest \(B\)-submodule of \(L\) containing \(M_0\) and stable
under both derivations.  It is full, but it need not be finite.

Finiteness is equivalent to the existence of one fixed finite
ambient \(B\)-module \(N\subset L\) containing all iterates.  Merely
knowing that every finite set of iterates lies in some finite pole
stage does not provide such an \(N\).

## 5. Coherence vocabulary

Since the target is affine, an \(\mathcal O_{\mathbf A^2}\)-module is
coherent exactly when its module of global sections is finite over
\(B\).  Thus “ordinary \(\mathcal O\)-coherent lattice” and “finite
\(B\)-lattice” are interchangeable in the affine statements below.

A coherent logarithmic lattice is instead a coherent module preserved
by logarithmic differential operators.  It can have a connection
matrix with simple poles.  It is not an ordinary stable lattice.

A holonomic \(\mathcal D\)-module is finite over the noncommutative
ring of differential operators and has minimal characteristic
dimension.  Neither condition implies finite generation over
\(\mathcal O\).

## 6. Consumed predecessor results

This packet consumes, without promoting, the following maintained
issue #4 candidates.

1. A finite full pair-stable \(B\)-module has a finite stable
   multiplier ring; its \(B\)-reflexive hull is a finite locally free
   stable order with total quotient field \(L\).
2. A finite locally free stable order has derivative-stable trace
   discriminant, hence unit discriminant, is finite etale, and has
   degree one.
3. At a characteristic-zero ramified height-one valuation, a
   transverse target derivation preserves no full finite lattice.
4. For the pair \(D_P,D_Q\), existence of a finite full pair-stable
   lattice is equivalent to absence of height-one ramification in the
   finite normalization.

The new contribution is to compute what these facts mean for the
canonical differential saturation, D-module, logarithmic, and
cohomological constructions requested in this successor.

## 7. Circularity controls

The following implications are forbidden in this packet.

- \(A\) is stable, therefore \(A\) is finite over \(B\).
- A direct image is holonomic, therefore its underlying
  \(\mathcal O\)-module is finite.
- A regular singular connection has a logarithmic lattice, therefore
  it has an ordinary stable lattice.
- A determinant residue is integral, therefore every residue class is
  integral.
- A finite-dimensional cohomology group is a full lattice in \(L\).
- A directed union of coherent pole stages stabilizes by
  Noetherianity without first placing the union in a fixed finite
  ambient module.
