# Issue #5 — adversarial review

> **Review type:** adversarial self-audit; not independent scientific review  
> **Authority:** `MUTABLE_NONAUTHORITATIVE`  
> **Baseline:** `agent/bootstrap-proof-graph@296867d82d09d51ef2386de2a62067408b7f949c`  
> **Protocol verdict:** `null`  
> **Recommended disposition:** `SCOPED_OBSTRUCTION`, not theorem promotion

## 1. Repository blobs reviewed

This review is bound to the following exact Git blob objects:

| Path | Git blob SHA |
|---|---|
| `research/issue-5/PRINCIPAL_PARTS.md` | `ce01715cf3835bdad3fde847944774e0373c6313` |
| `research/issue-5/SOURCE_AUDIT.md` | `9c8b6507e8b98358af8c00597f9757139a5a9c6a` |
| `research/leaf-packets/L03-radial-pole-elimination.md` | `ae088fe275907028d3622bd0fd0410de7293a12b` |

The review does not grant `verified_internal` status. An independent reviewer must repeat the calculations against these exact blobs before promotion.

## 2. Load-bearing claims attacked

### Attack A — sign and normalization of the canonical fields

Recompute directly:

\[
D_P=Q_y\partial_x-Q_x\partial_y,\qquad
D_Q=-P_y\partial_x+P_x\partial_y.
\]

Using \(P_xQ_y-P_yQ_x=1\),

\[
D_P(P)=1,\ D_P(Q)=0,\ D_Q(P)=0,\ D_Q(Q)=1.
\]

Therefore \(E=PD_P+QD_Q\) satisfies \(E(P)=P,E(Q)=Q\). No sign defect was found.

**Disposition:** survives.

### Attack B — minimal-polynomial differentiation may use the wrong generator

The formula

\[
\widetilde V(s)=-V_B(f)(s)/f'(s)
\]

is valid for a field generator satisfying \(f(s)=0\), but divisibility by \(f'(s)\) tests the normalization only when \(R[s]=S\) in the relevant lci neighborhood. The packet explicitly replaces the formula by \(\widetilde V(S)\subseteq S\) otherwise and includes the \(\mathbf C[[\pi^2,\pi^3]]\) countermodel.

**Disposition:** survives with the stated monogenic hypothesis. Any version omitting that hypothesis must be rejected.

### Attack C — zero residue might secretly imply the other coefficients vanish

Write \(f'(s)=\varepsilon\pi^d\) and \(\varepsilon^{-1}V_B(f)(s)=\sum_{\ell\ge0}r_\ell\pi^\ell\). Then

\[
\widetilde V(s)=-\sum_{\ell\ge0}r_\ell\pi^{\ell-d}.
\]

The residue is only \(-r_{d-1}\); the coefficients \(r_0,\ldots,r_{d-2}\) are independent. The model \(u=\pi^e,\ V=\partial_u\), \(e\ge3\), has zero residue and pole \(\pi^{1-e}/e\).

**Disposition:** the residue-only argument is falsified.

### Attack D — the tangent criterion may depend on a special coordinate choice

In tame coordinates \(u=\pi^e\),

\[
\widetilde V(\pi)=V(u)/(e\pi^{e-1}).
\]

Replacing \(u\) or \(\pi\) by a unit multiple changes the displayed expression by regular unit terms. The invariant statement is preservation of the height-one prime \(V(u)\in(u)\), so it descends from completion and unramified base change.

**Disposition:** survives.

### Attack E — radial regularity may be weaker than radial branch geometry

For an irreducible branch equation \(g\), radial regularity gives

\[
Pg_P+Qg_Q=h g.
\]

Degree comparison forces \(h\) to be constant. Ordinary homogeneous decomposition then forces \(g\) to have one degree. Over \(\mathbf C\), a homogeneous polynomial in two variables factors into linear forms, so an irreducible \(g\) is a line through the origin.

**Disposition:** survives. This proves an equivalence/obstruction, not the radiality of the actual branch divisor.

### Attack F — exact symplectic geometry may kill all negative coefficients

The coefficient equations were recomputed from

\[
dF=\sum_i(i f_i\pi^{i-1}d\pi+f_i'\pi^i dz).
\]

The signs in

\[
\sum_{i+j=r}(i p_iq_j'-j p_i'q_j)
=
\sum_{i+j=r}(i x_iy_j'-j x_i'y_j)
\]

are correct. For the primitive, the radial equation is

\[
r h_r=\sum_{i+j=r}j(p_iq_j+y_ix_j).
\]

At \(r=0\) it kills the residue. At \(r<0\), division by \(r\) defines \(h_r\) rather than forcing the right side to vanish. The polynomial example \(H=x^m,\ x=\pi^{-1}\), confirms the failure.

**Disposition:** exactness does not eliminate higher principal parts.

### Attack G — singular points may carry an independent pole

For a normal affine ring \(A\),

\[
A=\bigcap_{\operatorname{ht}\mathfrak p=1}A_{\mathfrak p}.
\]

If a rational derivation is regular in every height-one localization, then \(\delta(a)\) lies in that intersection for every \(a\in A\). This proves regularity at codimension-two points without assuming smoothness.

**Disposition:** survives. The conclusion concerns the ambient derivation. Descent to a nonnormal boundary curve can still impose conductor conditions.

### Attack H — a divisor-wise choice might globalize after all

For a general affine field, tangency to

\[
P,\quad P-Q^2,\quad P-Q^3
\]

forces successively

\[
\alpha_0=\alpha_2=0,\quad
\beta_0=\beta_1=0,\quad
\alpha_1=2\beta_2=3\beta_2,
\]

hence the zero field. The corresponding double-cover hypersurface has only isolated singularities and is normal.

**Disposition:** local affine cancellations need not globalize.

### Attack I — regularity may imply completeness in the canonical setting

The cusp Hamiltonian

\[
-3Q^2\partial_P-2P\partial_Q
\]

is logarithmic and has a regular lift through \(s^e=P^2-Q^3\). On the cusp normalization it induces \(-t^2\partial_t\), whose iterates on \(t\) span infinitely many monomials. Hence it is not locally finite and does not integrate to an algebraic \(\mathbf G_a\)- or \(\mathbf G_m\)-action.

**Disposition:** the regularity-to-integration implication is false without additional hypotheses.

### Attack J — an algebraic action might still imply degree one automatically

Shaska's Theorem 3.3 applies to a planar Keller map equivariant for actual nontrivial algebraic \(\mathbf G_m\)-actions on source and target. Before it can be invoked, one must prove integration and invariance of the source open. A finite equivariant cyclic cover shows that equivariance of a branched finite map alone is not enough.

**Disposition:** terminal edge remains blocked.

## 3. Countermodel coverage

| Required control | Model audited | Result |
|---|---|---|
| \(t=s^e\), radial | \(P=s^e,Q=z\) | lift regular |
| \(t=s^e\), nonradial | \(P=s^e+h(z),Q=z\) | explicit pole unless \(h-zh'=0\) |
| cusp | \(s^e=P^2-Q^3\) | radial pole; weighted lift regular |
| tangency intersection | \(P(P-Q^2)(P-Q^3)\) | no nonzero global affine field |
| zero residue, higher pole | \(V=\partial_u,\ u=\pi^e,\ e\ge3\) | residue zero, pole nonzero |
| nonnormal order/conductor | \(\mathbf C[[\pi^2,\pi^3]]\) | generator test misses pole |
| regular but nonintegrable | cusp Hamiltonian | not locally finite |
| exact polynomial primitive | \(H=x^m,\ x=\pi^{-1}\) | higher pole remains |

No countermodel contradicts the scoped logarithmic criterion. Several contradict the stronger radial, exactness, and integration inferences.

## 4. Source audit findings

- The Kähler-different and lci-different statements are bound to exact Stacks tags.
- Tameness and \(d=e-1\) are bound to exact Stacks tags and characteristic-zero hypotheses.
- The codimension-two intersection statement is bound to the normal-domain theorem.
- Shaska Theorem 3.3 is bound to arXiv:2607.20210v1 and is used only conditionally.
- Gutwirth is an action-linearization input, not a derivation-integration input.

No primary source was identified that supplies the missing integration or source-open invariance implication.

## 5. Review verdict

### Accepted at candidate scope

The following package is internally coherent under its stated hypotheses:

1. full monogenic Laurent principal parts and different divisibility;
2. tame equivalence between regular lift and logarithmic tangency;
3. extension across codimension two on normal \(Y\);
4. radial regularity iff every reduced ramified component is a line through the origin;
5. exact-symplectic coefficient equations and residue-only limitation;
6. failure of divisor-wise affine cancellation to globalize;
7. failure of regularity to imply algebraic integration.

### Rejected stronger claims

The candidate bytes do not justify:

- full regularity of the standard radial lift for an arbitrary Keller map;
- radiality of the actual branch divisor;
- pole elimination from zero residue or exactness;
- completeness or local finiteness of a regular lift;
- preservation of the original source open;
- degree one.

### Recommended ledger/graph action

Record the local theorems as `candidate_proved`, narrow the exact-symplectic residue claim, add a new `open_bridge` for an integrable logarithmic field preserving \(U\), mark the radial leaf `blocked`, and weaken its direct degree-one edge to `supports`.

This review is a self-audit only. It must not be represented as independent acceptance or a frozen theorem packet.
