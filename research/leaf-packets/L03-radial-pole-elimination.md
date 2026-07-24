# Radial Pole Elimination

- **Priority:** `P0`
- **Status:** `BLOCKED_BY_EXACT_TANGENCY`
- **Dependencies:** CLM-003, CLM-007, CLM-014, CLM-015, CLM-022, CLM-023, CLM-052–CLM-057
- **Authority:** `MUTABLE_NONAUTHORITATIVE`
- **Baseline:** `agent/bootstrap-proof-graph@296867d82d09d51ef2386de2a62067408b7f949c`
- **Issue branch:** `issue-5/radial-pole-elimination-gpt56`

## Load-bearing question

Show one lifted radial field extends regularly across every normalization boundary
divisor and singular point, and justify every subsequent integration and
degree-one implication.

## Scientific disposition

The local pole bridge has an exact scoped disposition, but the requested global
radial extension is not proved.

For a target field

\[
V=a(P,Q)\partial_P+b(P,Q)\partial_Q,
\]

its rational canonical lift

\[
\widetilde V=a(P,Q)D_P+b(P,Q)D_Q
\]

is regular on the normal finite surface \(Y\) if and only if \(V\) is tangent to
every reduced ramified branch component. At a monogenic height-one localization
\(S=R[s]\) with minimal polynomial \(f\),

\[
\widetilde V(s)=-\frac{V_B(f)(s)}{f'(s)},
\]

and regularity is exactly divisibility of \(V_B(f)(s)\) by the different. The
complete negative Laurent part, not only its residue, is recorded in the issue
packet.

For the standard radial field

\[
E=P D_P+Q D_Q,
\]

regularity is equivalent to

\[
P g_P+Q g_Q\in(g)
\]

for every reduced ramified branch equation \(g\). Over \(\mathbf C\), every
irreducible such component would have to be a line through the target origin.
Neither the exact symplectic identity nor its polynomial primitive forces this
condition.

Normality proves that height-one regularity extends across codimension-two
singular points. There is no separate ambient Hartogs obstruction after all
divisorial equations are solved.

A branch-dependent logarithmic combination such as

\[
\Delta_QD_P-\Delta_PD_Q
\]

does extend regularly, but a regular derivation need not be locally finite,
complete, or algebraically integrable. The terminal implication to degree one
therefore remains blocked.

## Accepted evidence

The following issue-scoped artifacts provide the accepted mutable evidence:

- [`../issue-5/PRINCIPAL_PARTS.md`](../issue-5/PRINCIPAL_PARTS.md): canonical
  formulas, different, full Laurent principal parts, geometric compatibility,
  singular-point audit, exact-symplectic coefficient equations, integration
  audit, and countermodels;
- [`../issue-5/SOURCE_AUDIT.md`](../issue-5/SOURCE_AUDIT.md): primary-source
  bindings and exact hypotheses;
- [`../issue-5/ADVERSARIAL_REVIEW.md`](../issue-5/ADVERSARIAL_REVIEW.md):
  separate adversarial self-review bound to file hashes.

This is candidate evidence only. It has not received independent scientific
review.

## Forbidden shortcuts

- Do not infer regularity from polynomiality on the original source.
- Do not infer regularity from zero logarithmic residue.
- Do not infer radial tangency from exactness of \(P\,dQ+y\,dx\).
- Do not treat a primitive element of a nonnormal order as a normalization
  generator.
- Do not choose different coefficients independently at different boundary
  divisors.
- Do not infer local finiteness, completeness, or an algebraic action from a
  regular derivation.
- Do not assume a resulting action preserves the source open subset.
- Do not use a linearization theorem before an algebraic action exists.
- Do not infer degree one from regularity alone.

## Required artifacts

Completed in the issue-scoped packet:

1. the exact canonical radial lift;
2. the monogenic formula and invariant replacement;
3. complete Laurent principal-part coefficients;
4. necessary-and-sufficient different divisibility;
5. the tame logarithmic tangency theorem;
6. a table of smooth, ramified, cusp, tangency, singular, conductor, and exact
   one-form cases;
7. global compatibility equations for radial, hyperbolic, and affine fields;
8. all coefficient equations supplied by
   \(dP\wedge dQ=dx\wedge dy\) and \(P\,dQ+y\,dx=dH\);
9. codimension-two/reflexivity and conductor proofs;
10. integration and degree-one hypothesis audit;
11. explicit countermodels;
12. source-bound terminal theorem statements;
13. separate adversarial review;
14. synchronized claim-ledger and proof-graph deltas.

## Stop rule

Stop at the exact scoped obstruction:

\[
\text{regular radial lift}
\iff
\text{every reduced ramified branch component is radial}.
\]

The Keller and exact-symplectic identities do not presently prove the right-hand
side. Regularity by itself also does not prove algebraic integration. This is the
first exact scientific disposition of the proposed radial-pole bridge, so the
leaf must not silently broaden into a classification of all boundary divisors or
all algebraic actions.

## Handoff

### Established candidate formulas

At a monogenic height-one point,

\[
\operatorname{PP}_\xi(\widetilde V(s))
 =-\sum_{\ell=0}^{d-1}r_\ell\pi^{\ell-d},
\qquad
r_\ell=\sum_{i+j=\ell}c_i b_j,
\]

with \(V_B(f)(s)=\sum c_i\pi^i\) and
\((f'(s)/\pi^d)^{-1}=\sum b_j\pi^j\). Regularity is equivalent to
\(r_0=\cdots=r_{d-1}=0\).

In tame coordinates \(u=\pi^e\),

\[
\widetilde V(\pi)=\frac{V(u)}{e\pi^{e-1}},
\]

so regularity is equivalent to \(V(u)\in(u)\).

### Tested countermodels

- \(P=s^e+h(Q)\): the radial pole is
  \((h-Qh')/(e s^{e-1})\);
- \(s^e=P^2-Q^3\): the standard radial field has a pole, while the weighted
  Euler field is regular;
- \(P,\ P-Q^2,\ P-Q^3\): each divisor admits local tangent fields but there is
  no nonzero affine-linear field tangent to all three;
- \(d(x^m)\) with \(x=\pi^{-1}\): zero residue and a nonzero higher pole;
- \(\mathbf C[[\pi^2,\pi^3]]\subset\mathbf C[[\pi]]\): an order generator hides
  a normalization pole;
- the cusp Hamiltonian field is regular but not locally finite.

### Remaining blockers

1. prove a radial or other locally finite logarithmic target field exists for
   the actual branch divisor;
2. prove its lift preserves every component of \(Y\setminus U\), including
   unramified boundary;
3. integrate it to a nontrivial algebraic action;
4. only then apply the exact planar equivariant Keller theorem.

### Smallest next action

In the first boundary class surviving Track A/L12, compute the reduced ramified
branch equation \(g\) and determine the semisimple integral-weight part of

\[
\operatorname{Der}_{\mathbf C}(B)(-\log g).
\]

For the smooth one-component case, decide whether this module contains a nonzero
locally finite field without assuming \(g\) is homogeneous. Record the first
coefficient obstruction if it does not.
