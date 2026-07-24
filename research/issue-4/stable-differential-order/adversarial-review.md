# Adversarial Review Record — Issue #4 Stable Differential Order

> **Authority:** `MUTABLE_NONAUTHORITATIVE`  
> **Engineering status:** `DEVELOPMENT`  
> **Execution validity:** `NOT_A_SCIENTIFIC_EXECUTION`  
> **Protocol verdict:** `null`  
> **Reviewer status:** constructor self-audit; not independent acceptance.

## Review identity

- **Pinned base:** `296867d82d09d51ef2386de2a62067408b7f949c`
- **Branch:** `issue-4/stable-differential-order-gpt56`
- **Checkpoint:** finite stable differential order, analytic obstruction disposition
- **Claim type:** exact conditional theorem plus class-level local obstruction candidate
- **Quantifier:** every finite full lattice over the declared characteristic-zero ramified DVR; every finite locally free stable `B`-order for the global implication
- **Stability level:** exact invariance, not logarithmic invariance
- **Forbidden inference:** no claim that a stable order exists and no claim of the planar Jacobian conjecture

## Candidate-byte manifest reviewed

The self-audit was performed against these exact precommit bytes:

| Path | SHA-256 |
|---|---|
| `research/issue-4/stable-differential-order/MAIN.md` | `10b776fa341c5d65835c79887908194744244f3e4ef70e736331983919cfae7b` |
| `research/issue-4/stable-differential-order/local-dvr-obstruction.md` | `0b79b43aff7669d39ea9f702f96cb822c6ad769e755d4683074fc9d5f4ee94c6` |
| `research/issue-4/stable-differential-order/construction-audit.md` | `c36bc7a262cefe72625121b41c8769500d8f7dee98a9d4fa4f909974b2933bd8` |
| `research/issue-4/stable-differential-order/source-bindings.md` | `87795e355df8f9c432795f4aecf66a2577946058645e56e333f8deb71c89b4b9` |
| `research/issue-4/stable-differential-order/HANDOFF.md` | `4acecb509ea19841b85167c990d7a7250114872f92430aa1097faf4e795777d5` |

This review file is the record of that audit and is not self-hashed into its own manifest.

## NEED predicates

1. The canonical derivation signs and all four values on `P,Q` are correct.
2. The commutator proof does not assume invertibility of the Keller map.
3. Trace compatibility is derived from multiplication matrices, not asserted.
4. The local connection convention is fixed and yields `delta(G)=A^T G+GA`.
5. The determinant formula includes the factor `2` and is basis-independent.
6. The derivative-stable ideal argument uses characteristic zero explicitly.
7. Unit discriminant is applied only to a finite locally free algebra.
8. Connectedness is justified from containment in the field `L`.
9. The degree-one step is bound to the complex base and Riemann existence.
10. The local no-lattice theorem controls an arbitrary full lattice, not only the normalization basis.
11. The Kummer reduction does not assume Galois symmetry.
12. Repeated differentiation has a nonvanishing leading coefficient in characteristic zero.
13. Every proposed construction is checked for finite generation, local freeness, multiplication, exact stability, and circularity at the level at which it is proposed.
14. No ascending-union stabilization is invoked without a fixed finite ambient module.
15. Exact translations are not replaced by logarithmic vector fields.

## Independent recomputations inside the self-audit

### Canonical frame

Direct substitution gives

```text
D_P(P)=1, D_P(Q)=0,
D_Q(P)=0, D_Q(Q)=1.
```

The commutator kills `K=C(P,Q)` and hence vanishes on finite separable `L/K`.

### Trace determinant

With row-basis convention `D(e)=eA`, differentiation of `z e=eM_z` gives

```text
delta(M_z)=M_(D z)+M_z A-A M_z.
```

Taking traces and then differentiating the Gram matrix independently reproduces

```text
delta(G)=A^T G+GA,
delta(det G)=2 Tr(A)det G.
```

Changing to the opposite column-basis convention transposes `A` but leaves the determinant coefficient unchanged. This mutation detects a convention error without changing the theorem.

### Kummer escape

For `t=s^e` and `D(t)=1`, direct induction gives

```text
D^n(t^N s)
 = product_(j=0)^(n-1)(N+1/e-j)t^(N-n)s.
```

The coefficient never vanishes in characteristic zero for `e>1`, and the `s`-valuation is `e(N-n)+1`. A sign mutation in `D(s)` changes the first canonical identity and is detected immediately.

### Discriminants

The self-audit recomputed

```text
Disc(X^e-t)=(-1)^[e(e-1)/2+e-1] e^e t^(e-1),
Disc(R+t^N S)=unit * t^[(e-1)(2N+1)],
Disc(S^vee)=unit * t^(1-e).
```

The conductor exponent follows independently by the square of the basis-change determinant. The inverse-different exponent follows by the square of the norm of `(e s^(e-1))^(-1)`.

## Adversarial findings

### Finding A — multiplication is load-bearing

A stable finite module does not by itself have multiplication matrices or an algebra trace. The main discriminant proof correctly assumes an order. The local obstruction is deliberately stronger and applies to modules, but it is not presented as fulfilling the order-construction objective.

**Disposition:** closed in the candidate.

### Finding B — finite torsion-free is not global local freeness

Over the two-dimensional base, finite torsion-free modules can fail local freeness at closed points. The candidate states local freeness as a hypothesis and identifies reflexivity over the regular surface as a sufficient replacement. It does not silently pass to a double dual.

**Disposition:** closed in scope; double-dual constructions remain unproved.

### Finding C — Kummer reduction could hide Galois assumptions

The first draft risked binding the general tame reduction to an incorrect source tag. The source inventory was corrected to Stacks Tags `09E9`, `09EV`, `0BRM`, `0EXT`, and `0EYF`. The proof now passes to a strict henselization, projects to one field factor, writes `t=u s^e`, and removes `u` by Hensel's lemma. No global deck group is used.

**Disposition:** corrected in the reviewed bytes.

### Finding D — differentiating a nonconstant unit could alter the leading term

In the general transverse case `D(t)=a in R^x`, repeated derivatives also differentiate `a`. Those terms remain one `t`-power higher because `D(a) in R`; the lowest term is still

```text
c_n a^n t^(N-n)s.
```

The candidate states this filtration argument rather than copying the constant-unit formula unchanged.

**Disposition:** closed in the candidate.

### Finding E — logarithmic regularity is a false positive

The normalization and every conductor order are stable under `tD_t`, while none is stable under `D_t`. The cusp Euler field supplies the same mutation. The candidate consistently labels logarithmic stability as insufficient.

**Disposition:** closed; mutation passes.

### Finding F — non-Galois and cusp cases

The cubic `z^3-3z-t` has nonsquare discriminant and a ramified quadratic local factor with valuation drop `2` per derivative. The cusp model has poles at the generic height-one point even though both numerators vanish at the closed cusp. These cases prevent the proof from relying on Galois symmetry or smooth branch geometry.

**Disposition:** closed in the candidate.

### Finding G — characteristic `p` is not uniform evidence

For `p` not dividing `e`, the product coefficient in `D^p(s)` vanishes modulo `p`. This destroys, rather than uniformly controls, the characteristic-zero escape sequence. No characteristic-zero conclusion is drawn from primewise nilpotence.

**Disposition:** closed; no mod-`p` promotion.

### Finding H — CLM-013 conflates implication with existence

The baseline labels the stable-order-to-degree-one implication `open_bridge` while its note says the missing step is existence. The candidate separates these statements: the implication is `candidate_proved`; `OPEN-STABLE-ORDER` remains open because no order is constructed.

**Disposition:** proposed synchronized correction.

## Source review

- Stacks Tag `0BJF` states the exact finite-locally-free discriminant criterion used.
- SGA 1, Expose XII, Theorem 5.1 supplies the comparison with finite topological covers over `C`.
- Stacks Tags `0B3D`, `00R4`, and `00NT` support the finite-normalization flatness background under the declared dimension hypotheses.
- Stacks Tags `00UP` and `0H94` support extension through etale base change.
- Stacks Tags `09E9`, `09EV`, `0BRM`, `0EXT`, and `0EYF` support the tame DVR context and standard model.

No source is used for the direct determinant or repeated-derivative calculations.

## Review disposition

**`BLOCK` — promotion/freeze is blocked.**

The block is not a detected algebraic contradiction. It is required because:

1. this is a constructor self-audit, not an independent review;
2. the exact candidate bytes have not received an external `ACCEPT`;
3. the load-bearing existence question remains open.

The files may be committed and pushed as coherent `MUTABLE_NONAUTHORITATIVE` provenance. They may not be frozen, promoted to reviewed authority, or used to claim the planar Jacobian conjecture.

## Surviving positive lemmas

Even under the `BLOCK` disposition, the following exact candidate lemmas survive for independent review:

- canonical commuting translation frame with the stated signs;
- trace derivative and determinant formula;
- bi-translation simplicity of nonzero ideals of `C[P,Q]`;
- stable finite locally free order implies finite etale and degree one;
- transverse tame ramification excludes every full stable finite DVR lattice;
- conductor, inverse-different, bounded-pole, finite-intersection, regular-singular, and primewise-reduction families do not solve the ramified local problem.
