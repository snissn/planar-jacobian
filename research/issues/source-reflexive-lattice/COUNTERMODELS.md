# Countermodels and Mutation Controls

> **Authority:** `MUTABLE_NONAUTHORITATIVE`  
> **Claims:** `SRL-005`, `SRL-007`, `SRL-010`

These examples test proposed implications.  Except where explicitly stated,
they are local or open-source controls, not planar polynomial Keller pairs.

## 1. Kummer ramification

Let

\[
R=\mathbf C[t,u]_{(t)},\qquad
S=R[s]/(s^e-t),\qquad e>1.
\]

The lifts of the base translations satisfy

\[
D_t(s)=\frac1{e s^{e-1}},\qquad D_u(s)=0.
\]

The normalization, every bounded pole module, every conductor order, every
trace-dual/different shift, and every finite intersection retains the classes
`j/e mod Z`.  The model separates the transverse obstruction from the
harmless tangential derivation.

## 2. Tame non-Galois cubic

For

\[
z^3-3z-t=0,
\]

the discriminant is `27(4-t^2)`, so the generic cubic is non-Galois.  At
`t=2`, with `z=-1+s` and `t=2+tau`,

\[
\tau=s^2(s-3),\qquad
D_t(s)=\frac1{3s(s-2)}.
\]

The ramified quadratic factor has the same valuation escape.  Galois
symmetry is not used by the theorem.

## 3. Cusp branch

Take

\[
h=p^2-q^3,\qquad s^e=h.
\]

Then

\[
D_p(s)=\frac{2p}{e h}s,
\qquad
D_q(s)=-\frac{3q^2}{e h}s.
\]

At the generic cusp point, `(2p,-3q^2)` is nonzero.  The pair spectrum is
`(j/e)(2p,-3q^2)`, while the weighted Euler field
`3p partial_p+2q partial_q` is logarithmic and preserves the normalization.
This separates exact translations from logarithmic stability.

## 4. Several boundary components

Let `Y=A^2_{s,r}` and

\[
U=D(sr).
\]

Then

\[
\Gamma(U,O_U)=\mathbf C[s,r,s^{-1},r^{-1}]
 =\bigcup_{m,n\ge0}s^{-m}r^{-n}\mathbf C[s,r].
\]

The two ordinary translations raise the corresponding pole bounds.  Mixed
commuting derivatives have additive growth; no common finite rectangle is
stable.

## 5. Unramified but nonproper boundary

Let `Y=A^2_{t,u}` and `U=D(t)`.  The finite map may be the identity, so there
is no ramification.  Nevertheless

\[
\partial_t(t^{-m})=-m t^{-m-1}.
\]

`O_Y` is stable, but every positive pole stage and the union approximating
`O(U)` fail finite-stage stability.  Ramification is not the only reason the
source pole union fails to stabilize.

## 6. Logarithmic versus exact translation

In the same example,

\[
t\partial_t(t^{-m})=-m t^{-m}.
\]

Every fixed pole stage is stable under the logarithmic field `t partial_t`
but not under `partial_t`.  Replacing a canonical translation by a
logarithmic field changes the problem and cannot be used as a repair.

## 7. Exact-symplectic ramified boundary control

Let

\[
Y=A^2_{s,z},\qquad
P=s^e,\qquad Q=z,
\]

and remove the ramified divisor:

\[
U=D(s).
\]

On `U`, set

\[
x=s,\qquad y=e s^{e-1}z.
\]

Then

\[
Q=\frac{y}{e x^{e-1}},
\qquad
\frac{\partial(P,Q)}{\partial(x,y)}=1,
\]

so

\[
dP\wedge dQ=dx\wedge dy.
\]

The standard primitives differ by an exact form:

\[
\boxed{x\,dy-P\,dQ=\frac{e-1}{e}\,d(xy).}
\]

Yet the boundary has ramification index `e` and the transverse spectrum is
`j/e mod Z`.  Thus even the volume identity and an exact primitive relation
do not erase the residue obstruction.

This is a generic-boundary control on `G_m x A^1`, not a polynomial Keller
pair on `A^2`: `Q` is Laurent in `(x,y)`.  It blocks only an inference from
local exact-symplectic identities to unramifiedness.

## 8. Source-pole union that never stabilizes

For `U=D(t)`, the stages

\[
M_m=t^{-m}\mathbf C[t,u]
\]

are strictly increasing because `t^{-(m+1)}` is not in `M_m`.  Their union is
stable under `partial_t`, but no stage is.  This is the exact failure of a
Noetherian-stabilization argument: the chain is not contained in a fixed
finite ambient module.

## 9. Characteristic-`p` mutation

For `p` not dividing `e`, reduction of

\[
D_t^n(s)=\prod_{r=0}^{n-1}(1/e-r)t^{-n}s
\]

can vanish at `n=p`.  The stopping index depends on `p`; it gives no uniform
characteristic-zero pole bound.  Primes dividing `e` are wild and lie outside
the tame theorem.
