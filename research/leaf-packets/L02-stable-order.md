# Finite Stable Differential Order

- **Priority:** `P0`
- **Status:** `OPEN — RAMIFIED-DVR OBSTRUCTION RECORDED`
- **Dependencies:** CLM-010–CLM-013
- **Authority:** `MUTABLE_NONAUTHORITATIVE`
- **Protocol verdict:** `null`

## Load-bearing question

Construct a finite locally free `C[P,Q]`-order in `C(x,y)` invariant under `D_P` and `D_Q`.

An order must be a finite `C[P,Q]`-subalgebra containing `C[P,Q]` with total quotient field `C(x,y)`. A stable finite module without multiplicative closure does not satisfy the leaf.

## Current disposition

The implication from a stable order to degree one has been rederived at exact candidate scope:

```text
stable order
  => derivative-stable trace discriminant
  => unit discriminant
  => finite etale connected cover of A^2_C
  => degree one.
```

Existence remains open. The issue #4 local theorem proves that, for a characteristic-zero ramified DVR and a derivation transverse to the base uniformizer, no full finite lattice is stable. In `t=s^e`, repeated differentiation gives

```text
v_s(D^n(t^N s))=e(N-n)+1 -> -infinity.
```

Because one of `partial_P,partial_Q` is transverse to every irreducible target divisor, a global stable order could exist only after codimension-one ramification has already been eliminated.

## Accepted evidence

A successful construction requires all of:

- a finite-generation proof inside one fixed finite `C[P,Q]`-module;
- local freeness, or a proved replacement sufficient for the determinant and etale steps;
- multiplicative closure and the correct total quotient field;
- exact invariance under both canonical translations;
- local bases or finite presentations and both derivation matrices;
- discriminant control;
- mutations detecting sign, pole-order, multiplication, and logarithmic/exact substitutions.

A valid obstruction disposition requires an exact declared construction class and a proof covering every member of that class.

## Forbidden shortcuts

- Do not use an infinite union of pole-order lattices.
- Do not invoke Noetherian stabilization until all terms lie in one fixed finite module.
- Do not assume logarithmic stability implies exact translation stability.
- Do not present a trace dual, inverse different, or canonical module as an order without proving multiplication.
- Do not infer a global Galois symmetry from local inverse branches.
- Do not assume finite etaleness, degree one, or the desired finiteness of `C[x,y]` while constructing the order.

## Required artifacts

The order, a basis or presentation, derivation matrices, discriminant computation, and failure mutations; or a rigorously scoped obstruction with the same local algebra and construction audit.

Current artifact set:

```text
research/issue-4/stable-differential-order/MAIN.md
research/issue-4/stable-differential-order/local-dvr-obstruction.md
research/issue-4/stable-differential-order/construction-audit.md
research/issue-4/stable-differential-order/source-bindings.md
research/issue-4/stable-differential-order/adversarial-review.md
research/issue-4/stable-differential-order/HANDOFF.md
```

## Stop rule

Stop when the declared implication and either the construction or a class-level obstruction are independently reviewed at exact scope. Bank restricted local lemmas separately. Do not widen the leaf to the entire conjecture without a graph update.

The present mutable packet reaches an obstruction disposition but not an independent review and not a construction. The leaf therefore remains open.

## Handoff

The smallest next calculation is the fractional residue spectrum of `D_P,D_Q` on reflexive conductor/different lattices at one asymptotic-value divisor. Determine whether the Keller frame supplies any relation beyond transversality that can cancel the nonintegral classes `j/e mod Z`. Record exact formulas, source bindings, countermodels, open sublemmas, and the surviving inference boundary.
