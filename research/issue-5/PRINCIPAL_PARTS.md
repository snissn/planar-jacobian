# Issue #5 — Canonical radial lift and full boundary principal parts

> **Authority:** `MUTABLE_NONAUTHORITATIVE`  
> **Engineering status:** `development`  
> **Execution validity:** `not an execution`  
> **Protocol verdict:** `null`  
> **Baseline:** `agent/bootstrap-proof-graph@296867d82d09d51ef2386de2a62067408b7f949c`  
> **Issue branch:** `issue-5/radial-pole-elimination-gpt56`  
> **Scientific disposition:** `SCOPED_OBSTRUCTION` — the complete height-one obstruction is logarithmic tangency. For the standard radial field this is exactly radiality of the reduced ramified branch divisor; it is not forced by the Keller or exact-symplectic identities. Regularity also does not supply algebraic integration.

## 1. Scope and notation

Let

\[
B=\mathbf C[P,Q],\qquad L=\mathbf C(x,y),
\]

let \(\bar C\) be the normalization of \(B\) in \(L\), and set

\[
Y=\operatorname{Spec}(\bar C).
\]

The original affine source is the open subset

\[
U=\mathbf A^2_{\mathrm{source}}=\operatorname{Spec}\mathbf C[x,y]\subset Y.
\]

Write \(\pi:Y\to\mathbf A^2_{P,Q}\) for the finite normalization map. The map
\(F=(P,Q):U\to\mathbf A^2_{P,Q}\) is étale because

\[
J(P,Q)=P_xQ_y-P_yQ_x=1.
\]

Every statement below concerning the actual normalization is conditional only on the normalization package represented by `CLM-003`; no smoothness of \(Y\) is assumed. Every new mathematical statement in this packet is a candidate pending independent exact-byte review.

The term **branch component** means a reduced irreducible codimension-one component of the branch divisor of \(\pi\). An unramified component of \(Y\setminus U\) is not detected by the different and is treated separately when invariance of \(U\) is discussed.

## 2. The canonical fields

With the sign convention \(dP\wedge dQ=dx\wedge dy\), define

\[
D_P=Q_y\partial_x-Q_x\partial_y,\qquad
D_Q=-P_y\partial_x+P_x\partial_y.
\]

Then

\[
D_P(P)=1,\quad D_P(Q)=0,\qquad
D_Q(P)=0,\quad D_Q(Q)=1,
\]

and \([D_P,D_Q]=0\). The canonical radial lift is

\[
E=P D_P+Q D_Q.
\]

It satisfies, exactly,

\[
E(P)=P,\qquad E(Q)=Q.
\]

More generally, every target polynomial vector field

\[
V=a(P,Q)\partial_P+b(P,Q)\partial_Q
\]

has a unique rational lift to \(L\),

\[
\widetilde V=a(P,Q)D_P+b(P,Q)D_Q.
\]

The uniqueness follows because \(P,Q\) form a separating transcendence basis and \(L/\mathbf C(P,Q)\) is finite separable. The issue is not existence on the function field; it is preservation of \(\bar C\).

The exact symplectic contraction is

\[
\iota_{\widetilde V}(dP\wedge dQ)=a\,dQ-b\,dP.
\]

In particular,

\[
\iota_E(dP\wedge dQ)=P\,dQ-Q\,dP.
\]

These formulas determine the numerator of every local pole calculation.

## 3. Exact local algebra at a height-one point

### 3.1 Monogenic formula and its invariant replacement

Let \(\eta\) be the generic point of an irreducible target divisor and let \(R=\mathcal O_{\mathbf A^2,\eta}\), a DVR with fraction field \(K\). Let \(\xi\) be a height-one point of \(Y\) over \(\eta\), and let \(S=\mathcal O_{Y,\xi}\), a DVR with fraction field \(M\subset L\).

Suppose first that \(S=R[s]\) and that the monic minimal polynomial of \(s\) over \(K\) is

\[
f(T)=T^n+a_{n-1}T^{n-1}+\cdots+a_0\in R[T].
\]

Applying the lifted derivation to \(f(s)=0\) gives

\[
0=\widetilde V(f(s))
  =f'(s)\widetilde V(s)+V_B(f)(s),
\]

where \(V_B(f)\) means that \(V\) is applied coefficientwise. Hence

\[
\boxed{\widetilde V(s)=-\frac{V_B(f)(s)}{f'(s)}}. \tag{3.1}
\]

For a monogenic finite local complete-intersection presentation, \(f'(s)\) generates the Kähler different; under the flat quasi-finite lci hypotheses it also generates the Dedekind different. Formula (3.1) is therefore a literal numerator-versus-different test.

The invariant replacement, valid without monogenicity, is

\[
\boxed{\widetilde V\text{ is regular at }\xi
       \iff \widetilde V(S)\subseteq S.} \tag{3.2}
\]

Equivalently, in completed tame coordinates it is the divisibility condition in Theorem 3.3 below. Formula (3.1) must not be applied to an arbitrary primitive field element that generates only a nonnormal order.

### 3.2 Complete Laurent principal part

Choose a uniformizer \(\pi\) of \(S\). Write

\[
f'(s)=\varepsilon\pi^d,\qquad \varepsilon\in S^\times,
\]

where \(d=v_\pi(\mathfrak D_{S/R})\) in the monogenic lci case. Expand

\[
V_B(f)(s)=\sum_{i\ge 0}c_i\pi^i,\qquad
\varepsilon^{-1}=\sum_{j\ge 0}b_j\pi^j.
\]

Set

\[
r_\ell=\sum_{i+j=\ell}c_i b_j.
\]

Then (3.1) has the complete Laurent expansion

\[
\widetilde V(s)
 =-\sum_{\ell\ge 0}r_\ell\pi^{\ell-d},
\]

and its entire negative principal part is

\[
\boxed{
\operatorname{PP}_\xi(\widetilde V(s))
  =-\sum_{\ell=0}^{d-1}r_\ell\pi^{\ell-d}.
} \tag{3.3}
\]

Thus the necessary-and-sufficient conditions are

\[
\boxed{
r_0=r_1=\cdots=r_{d-1}=0
\iff V_B(f)(s)\in \pi^dS
\iff V_B(f)(s)\in\mathfrak D_{S/R}.
} \tag{3.4}
\]

The logarithmic residue is only the coefficient \(-r_{d-1}\) of \(\pi^{-1}\). Its vanishing leaves the independent coefficients

\[
r_0,\ldots,r_{d-2}
\]

uncontrolled. For \(d\ge 2\), zero residue is strictly weaker than regularity.

### 3.3 Tame normal form and the logarithmic lifting theorem

Because the characteristic and all residue characteristics here are zero, every height-one ramified extension is tame. After completion and a finite unramified base change, one may choose a target parameter \(u\), a tangential parameter \(z\), and a uniformizer \(\pi\) such that

\[
u=\pi^e,\qquad z=z,
\]

where \(e\) is the ramification index and

\[
d=e-1.
\]

Let

\[
V=A(u,z)\partial_u+B(u,z)\partial_z.
\]

The lift satisfies

\[
\boxed{
\widetilde V(\pi)=\frac{A(\pi^e,z)}{e\pi^{e-1}},
\qquad
\widetilde V(z)=B(\pi^e,z).
} \tag{3.5}
\]

If

\[
A(u,z)=\sum_{n\ge 0}A_n(z)u^n,
\]

then

\[
\widetilde V(\pi)
 =\frac1e\sum_{n\ge 0}A_n(z)\pi^{en-e+1}. \tag{3.6}
\]

Only the term \(n=0\) can be negative. This yields the central theorem.

### Theorem 3.3 — height-one logarithmic lifting criterion

At a height-one point with reduced branch equation \(u=0\) and ramification index \(e>1\), the following are equivalent:

1. \(\widetilde V\) is regular at the point;
2. \(A(0,z)=0\);
3. \(V(u)\in(u)\);
4. the target field \(V\) is tangent to the reduced branch divisor.

For \(e=1\), the finite map is étale at the generic point and every regular target field lifts regularly.

**Proof.** Formula (3.6) is regular exactly when \(A_0(z)=0\). This is exactly \(A(u,z)\in(u)\), or \(V(u)\in(u)\). The unramified case has invertible Jacobian and no different denominator. \(\square\)

The same argument with a unit \(u=\epsilon\pi^e\) adds only regular unit-correction terms and gives the same invariant criterion.

### Corollary 3.4 — simultaneous global divisorial criterion

Let the reduced ramified branch divisor have irreducible equations \(g_1,\ldots,g_r\in B\). Then

\[
\widetilde V\text{ is regular at every height-one point of }Y
\]

if and only if

\[
\boxed{
a\,\partial_P g_i+b\,\partial_Q g_i\equiv 0\pmod{g_i}
\quad(1\le i\le r).
} \tag{3.7}
\]

Equivalently,

\[
V\in\operatorname{Der}_{\mathbf C}(B)(-\log\Delta_{\mathrm{red}}),
\qquad
\Delta_{\mathrm{red}}=\prod_i g_i.
\]

These are simultaneous equations on the single global pair \((a,b)\). Choosing different coefficients at different divisors is not a global construction.

## 4. Geometric consequences for canonical combinations

### 4.1 The standard radial field

For

\[
R_0=P\partial_P+Q\partial_Q,
\]

condition (3.7) is

\[
\boxed{
P\,g_P+Q\,g_Q\in(g)
} \tag{4.1}
\]

for every ramified branch component \(g=0\).

If \(g\) is irreducible and (4.1) holds, then \(P g_P+Q g_Q=cg\) for a constant \(c\): the left side has degree at most \(\deg g\). Decomposing \(g\) into ordinary homogeneous pieces shows that only one degree occurs. Thus \(g\) is homogeneous. Over \(\mathbf C\), a homogeneous binary polynomial factors into linear forms, so an irreducible homogeneous \(g\) is linear.

Therefore:

\[
\boxed{
E=P D_P+Q D_Q\text{ is regular across all ramified divisors}
}
\]

if and only if every irreducible reduced ramified branch component is a line through the target origin.

This is not a proof that the branch divisor is radial. It identifies radiality as the exact missing hypothesis.

For a radial field centered at \(c=(c_1,c_2)\),

\[
(P-c_1)\partial_P+(Q-c_2)\partial_Q,
\]

regularity forces every irreducible ramified component to be a line through the same center \(c\).

### 4.2 Hyperbolic and affine fields

For a diagonal field

\[
R_{\lambda,\mu}=\lambda P\partial_P+\mu Q\partial_Q,
\]

regularity along \(g=0\) is

\[
\lambda P g_P+\mu Q g_Q\in(g),
\]

so \(g\) must be weighted homogeneous for those same global weights.

For a general affine target field

\[
a=\alpha_0+\alpha_1P+\alpha_2Q,\qquad
b=\beta_0+\beta_1P+\beta_2Q,
\]

the complete compatibility system is

\[
a g_{i,P}+b g_{i,Q}\equiv0\pmod{g_i}
\quad\text{for every }i. \tag{4.2}
\]

There need not be a nonzero solution. For example, take

\[
g_1=P,\qquad g_2=P-Q^2,\qquad g_3=P-Q^3.
\]

Tangency to \(g_1\) gives \(\alpha_0=\alpha_2=0\). Tangency to \(g_2\) then gives

\[
\beta_0=\beta_1=0,\qquad \alpha_1=2\beta_2,
\]

while tangency to \(g_3\) gives

\[
\alpha_1=3\beta_2.
\]

Hence all six coefficients vanish. Each component separately admits a useful weighted or affine tangent field, but no nonzero affine field works simultaneously.

The finite normal hypersurface

\[
s^2=P(P-Q^2)(P-Q^3)
\]

makes this obstruction concrete. Its singular locus is finite, so the two-dimensional hypersurface is \(S_2\) and regular in codimension one, hence normal. No nonzero affine-linear target field lifts regularly across all three ramified components.

### 4.3 A branch-dependent logarithmic field always exists

If \(\Delta_{\mathrm{red}}\) is a reduced branch equation, then

\[
V_\Delta
 =\Delta_Q\partial_P-\Delta_P\partial_Q
\]

satisfies \(V_\Delta(\Delta)=0\). Consequently,

\[
\widetilde V_\Delta
 =\Delta_QD_P-\Delta_PD_Q
\]

is regular at every height-one point and therefore, by Section 7, on all of the normal surface \(Y\).

This is a genuine global construction, but it is branch-dependent and generally neither affine nor locally finite. It does not close the radial route.

Multiplying an arbitrary target field by \(\Delta_{\mathrm{red}}\) also gives a logarithmic field, but the same integration failure remains.

## 5. Boundary and singular-point case table

| Case | Local model / condition | Principal part of \(\widetilde V(\pi)\) | Exact regularity condition | Consequence |
|---|---|---|---|---|
| Unramified generic point | \(e=1\) | none | automatic | no height-one obstruction |
| Smooth ramified branch | \(u=\pi^e\) | \(A(0,z)/(e\pi^{e-1})\) | \(V(u)\in(u)\) | target tangency |
| Radial branch | \(u=P\), \(R_0(u)=u\) | \(\pi/e\) | satisfied | radial lift regular |
| Translated smooth branch | \(u=P-h(Q)=\pi^e\) | \([h-Qh']/(e\pi^{e-1})+\pi/e\) | \(h-Qh'=0\) | only lines through origin survive |
| Cusp branch | \(u=P^2-Q^3=\pi^e\) | \([2u-Q^3]/(e\pi^{e-1})\) for \(R_0\) | fails generically | standard radial lift has a pole |
| Weighted cusp field | \(3P\partial_P+2Q\partial_Q\) | \(6\pi/e\) | satisfied | local regular lift exists |
| Tangent components with incompatible weights | \(P,\ P-Q^2,\ P-Q^3\) | each removable separately | one global system (4.2) | only zero affine field |
| Normal codimension-two singularity | isolated singular point of \(s^e=g(P,Q)\) | controlled by adjacent height-one points | no additional ambient condition | normality/Hartogs applies |
| Nonnormal boundary order | \(\mathbf C[[\pi^2,\pi^3]]\subset\mathbf C[[\pi]]\) | may be hidden by an order generator | test the normalization, not the order | conductor audit required |
| Exact one-form | \(dH\), \(H\) Laurent in \(\pi\) | arbitrary \(\pi^{-m-1}d\pi\), \(m\ge1\) | exactness only kills \(\pi^{-1}d\pi\) | residue is insufficient |
| Regular logarithmic field | \(V_\Delta\) | none | automatic by tangency | need not integrate algebraically |

## 6. The exact symplectic identities and every principal-part coefficient

### 6.1 Different order from the symplectic form

At a smooth height-one point of the normal surface, choose completed coordinates \((\pi,z)\) as above. Then

\[
dP\wedge dQ
 =\text{unit}\cdot\pi^d\,d\pi\wedge dz,
\qquad d=e-1.
\]

The equality

\[
dP\wedge dQ=dx\wedge dy
\]

therefore identifies the same different order in the source-coordinate expression. It does not say that \(x\) and \(y\) are regular on \(Y\), and it does not make the divisor of the two-form vanish.

For a target field \(V\), solving

\[
\iota_{\widetilde V}(dP\wedge dQ)
 =\pi^*(\iota_V(dP\wedge dQ))
\]

divides the normal coefficient \(V(u)\) by the factor \(\pi^d\). The symplectic identity identifies the denominator; regularity still requires the numerator divisibility \(V(u)\in(u)\).

### 6.2 Full Laurent coefficient equations

At a generic boundary point, let \(k=\kappa(D)\) and let prime denote a chosen derivation in the tangential coefficient field. Write finite Laurent expansions

\[
\begin{aligned}
P&=\sum_i p_i\pi^i,& Q&=\sum_j q_j\pi^j,\\
x&=\sum_i x_i\pi^i,& y&=\sum_j y_j\pi^j,\\
H&=\sum_r h_r\pi^r.
\end{aligned}
\]

The source coordinates and \(H\) may have negative terms. Comparing the coefficient of \(\pi^{r-1}d\pi\wedge dz\) in

\[
dP\wedge dQ=dx\wedge dy
\]

gives, for every integer \(r\),

\[
\boxed{
\sum_{i+j=r}\left(i p_i q'_j-j p'_i q_j\right)
=
\sum_{i+j=r}\left(i x_i y'_j-j x'_i y_j\right).
} \tag{6.1}
\]

Because \(P,Q\in\bar C\), their Laurent expansions have no negative terms. Consequently the left side vanishes for \(r<0\). Equation (6.1) imposes cancellation among the negative source-coordinate coefficients, but does not make those coefficients vanish separately.

The polynomial Poincaré lemma gives a polynomial \(H\in\mathbf C[x,y]\) with

\[
P\,dQ+y\,dx=dH.
\]

Comparing radial and tangential coefficients gives, for every integer \(r\),

\[
\boxed{
r h_r
 =\sum_{i+j=r}j\left(p_iq_j+y_ix_j\right),
} \tag{6.2}
\]

and

\[
\boxed{
h'_r
 =\sum_{i+j=r}\left(p_iq'_j+y_ix'_j\right).
} \tag{6.3}
\]

These are the complete coefficient constraints supplied by the primitive.

At \(r=0\), equation (6.2) says

\[
0=\sum_{i+j=0}j(p_iq_j+y_ix_j),
\]

which is exactly the vanishing of the logarithmic residue of the exact form. For every \(r<0\), however, \(r\) is invertible in characteristic zero and (6.2) merely defines

\[
h_r=\frac1r\sum_{i+j=r}j(p_iq_j+y_ix_j).
\]

Thus a nonzero higher principal coefficient is absorbed by a negative Laurent coefficient of \(H\). Differentiating (6.2) tangentially and comparing with the radial derivative of (6.3) reproduces (6.1); there is no extra hidden principalization statement.

### 6.3 Explicit residue countercontrol

Let \(x=\pi^{-1}\) along a boundary valuation and take the polynomial \(H=x^m\), \(m\ge1\). Then

\[
dH=-m\pi^{-m-1}d\pi.
\]

The logarithmic residue is zero, but the higher pole is nonzero. Polynomiality of \(H\) on the original source is irrelevant because \(x\) itself can have a pole on \(Y\).

This directly refutes the inference

\[
\text{polynomial exact primitive}+\text{zero residue}
\Longrightarrow\text{regular boundary form}.
\]

It also supplies no statement that the canonical divisor is zero or that a boundary divisor is principal.

## 7. Codimension two, reflexivity, and conductor points

### 7.1 Normality removes a separate ambient codimension-two pole problem

Let \(A\) be a normal noetherian domain with fraction field \(K\). Then

\[
A=\bigcap_{\operatorname{ht}\mathfrak p=1}A_{\mathfrak p}
\quad\text{inside }K.
\]

Let \(\delta:K\to K\) be a rational derivation regular at every height-one localization. For \(a\in A\),

\[
\delta(a)\in A_{\mathfrak p}
\quad\text{for every height-one }\mathfrak p,
\]

so \(\delta(a)\in A\). Therefore \(\delta\) is a regular derivation of \(A\).

Applied affine-locally on \(Y\), this proves:

\[
\boxed{
\text{height-one regularity of }\widetilde V
\Longrightarrow
\text{regularity at every singular and codimension-two point of normal }Y.
} \tag{7.1}
\]

No smoothness of \(Y\) is used. The relevant sheaf is

\[
\mathcal T_Y=\mathcal H om_{\mathcal O_Y}
             (\Omega^1_Y,\mathcal O_Y),
\]

viewed inside rational derivations. The preceding intersection calculation proves directly that its sections are determined in codimension one; equivalently, the tangent sheaf is reflexive in this normal setting.

### 7.2 Preservation of boundary primes and conductors

If a rational derivation is regular on \(A\) and tangent to a height-one prime \(\mathfrak p\) after localization, then

\[
\delta(\mathfrak p)\subseteq\mathfrak p
\]

globally, because \(\mathfrak p=A\cap\mathfrak p A_{\mathfrak p}\).

If \(R\subset S\) is a finite normalization and a derivation preserves both rings, then it preserves the conductor

\[
\mathfrak c=\{r\in R:rS\subset R\}.
\]

Indeed, for \(c\in\mathfrak c\) and \(s\in S\),

\[
\delta(c)s=\delta(cs)-c\delta(s)\in R.
\]

Thus \(\delta(c)\in\mathfrak c\). Conductor moment conditions on the normalization of a singular boundary curve are genuine descent constraints, but they are not additional ambient pole conditions once (7.1) is established.

### 7.3 A primitive-order trap

Take

\[
R=\mathbf C[[u]],\qquad S=\mathbf C[[\pi]],\qquad u=\pi^2,
\]

and the nonnormal order

\[
O=R[s]=\mathbf C[[\pi^2,\pi^3]],\qquad s=\pi^3.
\]

Its relation is

\[
f(T)=T^2-u^3.
\]

For \(V=\partial_u\),

\[
\widetilde V(\pi)=\frac1{2\pi},
\]

so the lift is not regular on the normalization. Yet

\[
\widetilde V(s)=\frac32\pi\in S.
\]

Checking only the order generator \(s\) misses the pole. The conductor is \(\pi^2S\), and it is not preserved because \(\widetilde V(\pi^2)=1\notin\pi^2S\). This is why (3.1) must be tied to a genuine local normalization generator or replaced by (3.2).

## 8. Countermodels required by the leaf

### 8.1 \(t=s^e\): radial and nonradial branches

For

\[
P=s^e,\qquad Q=z,
\]

the standard radial field gives

\[
E(s)=\frac{s}{e},
\]

so it is regular.

For

\[
P=s^e+h(z),\qquad Q=z,
\]

let \(u=P-h(Q)=s^e\). Then

\[
E(u)=P-Qh'(Q)
    =u+h(z)-zh'(z),
\]

and

\[
\boxed{
E(s)=\frac{s}{e}
     +\frac{h(z)-zh'(z)}{e\,s^{e-1}}.
} \tag{8.1}
\]

For \(h=z^m\) with \(m\ne1\), the second term is a genuine pole. For a translated line \(h=az+b\), it is \(b/(e s^{e-1})\); radiality fails unless the line passes through the origin.

### 8.2 Cusp

Let

\[
g=P^2-Q^3,\qquad s^e=g.
\]

For the standard radial field,

\[
R_0(g)=2P^2-3Q^3=2g-Q^3,
\]

so

\[
R_0(s)=\frac{2s}{e}-\frac{Q^3}{e\,s^{e-1}}.
\]

The pole is nonzero. In contrast, the weighted Euler field

\[
3P\partial_P+2Q\partial_Q
\]

satisfies \(V(g)=6g\), and its lift is regular.

The surface

\[
\operatorname{Spec}
\mathbf C[[P,Q,s]]/(s^e-(P^2-Q^3))
\]

has only an isolated singularity; as a hypersurface it is \(S_2\), and regularity in codimension one makes it normal. The codimension-two singular point creates no extra derivation pole after the divisorial criterion is met.

### 8.3 Local cancellation without globalization

The three components

\[
P=0,\qquad P-Q^2=0,\qquad P-Q^3=0
\]

admit, respectively, standard or weighted local tangent fields. Section 4.2 proves that no nonzero affine-linear target field is tangent to all three. This is an explicit model in which coefficients can be chosen divisor by divisor but do not globalize.

### 8.4 Zero residue with a higher principal part

For \(e\ge3\), take \(u=\pi^e\) and \(V=\partial_u\). Then

\[
\widetilde V(\pi)=\frac1{e}\pi^{1-e}.
\]

There is no \(\pi^{-1}\) term when \(e\ge3\), so the logarithmic residue is zero, but the higher pole is nonzero.

### 8.5 A regular lift that is not locally finite

For the cusp equation \(g=P^2-Q^3\), the Hamiltonian field

\[
V_g=g_Q\partial_P-g_P\partial_Q
   =-3Q^2\partial_P-2P\partial_Q
\]

satisfies \(V_g(g)=0\) and hence lifts regularly through every cyclic cover \(s^e=g\).

On the cusp normalization \(P=t^3,\ Q=t^2\), it induces

\[
V_g(t)=-t^2.
\]

This derivation is not locally finite: its iterates on \(t\) are nonzero scalar multiples of \(t^{n+1}\) and span an infinite-dimensional space. It is not a locally nilpotent derivation and is not the infinitesimal generator of an algebraic \(\mathbf G_a\)-action; it is also not semisimple with integral weights, so it does not generate a \(\mathbf G_m\)-action.

The simpler field \(x^2\partial_x\) on \(\mathbf A^1\) gives the same warning: regularity is not completeness.

## 9. Integration and the terminal implication

A regular derivation \(\delta\) on an affine algebra is:

- the infinitesimal generator of an algebraic \(\mathbf G_a\)-action only when \(\delta\) is locally nilpotent;
- the infinitesimal generator of an algebraic \(\mathbf G_m\)-action only when the algebra carries the corresponding integral \(\mathbf Z\)-grading, so \(\delta\) is semisimple and locally finite with integral eigenvalues.

Regularity alone supplies neither condition.

If the standard radial lift were proved to integrate to a nontrivial algebraic \(\mathbf G_m\)-action on \(Y\), one would still have to prove that the open source \(U\) is invariant. Tangency to the ramified branch divisor does not automatically control unramified components of \(Y\setminus U\).

Only after obtaining actual algebraic actions on source and target and equivariance of \(F\) can one invoke the exact graded theorem: Shaska's Theorem 3.3 states that a planar Keller map equivariant for nontrivial algebraic \(\mathbf G_m\)-actions on source and target is an automorphism. Its hypothesis is an action, not merely a regular derivation.

A finite equivariant cover by itself does not force degree one. The model

\[
(P,Q)=(s^e,z):\mathbf A^2_{s,z}\to\mathbf A^2_{P,Q}
\]

is a nontrivial finite equivariant branched cover. It is not a Keller map, and precisely demonstrates why the étale-source and integration hypotheses cannot be omitted.

Consequently the former proof-graph edge

\[
\text{regular radial lift}\Longrightarrow\text{degree one}
\]

is not established. The correct chain still requires:

1. a nonzero globally logarithmic canonical field;
2. local finiteness or a direct construction of an algebraic action;
3. invariance of \(U\);
4. compatibility with \(\pi\) and \(F\);
5. application of the exact planar equivariant Keller theorem.

## 10. Exact scientific disposition

The radial-pole bridge stops at the following exact result.

### Scoped theorem candidate

For a finite normalization \(Y\to\mathbf A^2_{P,Q}\) in characteristic zero, a target polynomial vector field

\[
V=a(P,Q)\partial_P+b(P,Q)\partial_Q
\]

has a regular rational lift to the normal surface \(Y\) if and only if it is logarithmic along every reduced ramified branch component. In monogenic lci coordinates the full obstruction is the class of \(V_B(f)(s)\) modulo the different, with principal coefficients given by (3.3). Once all height-one conditions hold, normality extends the derivation across codimension two.

For \(V=P\partial_P+Q\partial_Q\), this criterion is equivalent to every reduced irreducible ramified branch component being a line through the target origin. Neither

\[
dP\wedge dQ=dx\wedge dy
\]

nor

\[
P\,dQ+y\,dx=dH
\]

forces that tangency. The primitive supplies equations (6.1)–(6.3), whose \(r=0\) member kills the logarithmic residue while negative \(r\) permit arbitrary higher principal parts.

### Forbidden stronger inference

This packet does **not** prove:

- that the actual Keller branch divisor is radial or weighted homogeneous;
- that the standard radial lift is regular;
- that a regular logarithmic lift is locally finite or complete;
- that \(U\) is invariant under a resulting action;
- that the function-field degree is one;
- the planar Jacobian conjecture.

## 11. Smallest remaining calculation

For the actual finite normalization, compute the reduced ramified branch equation

\[
\Delta_{\mathrm{red}}=\prod_i g_i
\]

at the first boundary class permitted by Track A/L12 and solve the finite compatibility problem

\[
\begin{cases}
a g_{i,P}+b g_{i,Q}\equiv0\pmod{g_i},\\
(a,b)\text{ belongs to a declared finite-dimensional locally-finite class},\\
V\text{ preserves every component of }Y\setminus U.
\end{cases}
\]

The smallest useful case is the one-boundary smooth model: determine whether the logarithmic module contains a nonzero semisimple integral-weight field without assuming the branch equation is homogeneous. A negative calculation should be recorded as a new obstruction class rather than replaced by divisor-dependent coefficients.
