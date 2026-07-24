# Track D — Stable Differential Lattice

> **Status:** `MUTABLE_NONAUTHORITATIVE`  
> **Protocol verdict:** `null`

Seek a finite locally free `B=C[P,Q]`-order `M` in `L=C(x,y)` preserved by both canonical derivations `D_P,D_Q`. Here an order is a finite `B`-subalgebra containing `B` with total quotient field `L`; a stable module without multiplication is not the requested object.

## Audited implication

The implication from existence to degree one is now written exactly in the issue #4 packet:

1. in a local basis `e`, write `D(e)=eA`;
2. for the trace Gram matrix `G`,

   ```text
   delta(G)=A^T G+GA;
   ```

3. therefore

   ```text
   delta(det G)=2 Tr(A)det G;
   ```

4. the trace-discriminant ideal is stable under `partial_P,partial_Q`;
5. every nonzero ideal of `C[P,Q]` stable under both partials is the unit ideal;
6. a finite locally free algebra with unit discriminant is finite etale;
7. a connected finite etale cover of `A^2_C` has degree one.

Multiplicative closure, local freeness, generic separability, and connectedness are explicit hypotheses. This implication is a mutable theorem candidate; it does not construct the order.

## Local obstruction

At a height-one prime `(h)` of `B`, at least one canonical derivation is transverse because `h` cannot divide both `partial_P h` and `partial_Q h`. In the tame ramified DVR model

```text
t=s^e,
e>1,
```

a transverse derivation satisfies

```text
D^n(t^N s)
 = product_(j=0)^(n-1)(N+1/e-j)t^(N-n)s,
```

so the valuation tends to minus infinity. Consequently no full finite local lattice is stable at a ramified valuation, even before imposing multiplication.

The exact Keller-specific input is the dual translation frame. It exposes every reduced target divisor to a transverse derivation; it does not cancel the resulting poles. Exact stability can survive locally only when the ramification index is one.

## Construction audit

The issue packet tests:

- differential saturation inside a purported fixed ambient lattice;
- bounded-pole modules;
- conductor orders `R+t^N S`;
- trace duals and inverse differents;
- canonical modules;
- finite intersections of fractional ideals;
- regular-singular connection lattices;
- tame non-Galois cubic and cusp branches;
- compactification-boundary coordinate changes;
- characteristic-`p` reductions.

In the ramified Kummer model every genuine finite order fails exact translation stability. Fractional duals and bounded-pole modules fail multiplicative closure; differential saturation leaves every fixed finite module; regular-singular methods preserve only logarithmic lattices; primewise nilpotence has no uniform characteristic-zero bound.

## Current obstruction boundary

- `C[x,y]` is an exact stable algebra but is not known finite over `B`.
- The finite normalization `Cbar` is locally free under the maintained surface hypotheses but is not stable at ramified height one.
- No bounded valuation lattice can interpolate between them across a ramified divisor.

Thus the remaining route must either:

1. prove codimension-one unramifiedness by an argument independent of a stable lattice;
2. identify a Keller-specific cancellation that invalidates the Kummer residue spectrum, with an exact local calculation;
3. or construct a global object that is not valuation-bounded at an intermediate stage but nevertheless becomes a finite multiplicatively closed order without using an infinite union.

The third option currently has no viable model.

## Issue-specific artifact

See `research/issue-4/stable-differential-order/` for the exact global proof, local DVR theorem, construction table, source bindings, adversarial review, and handoff.

## Exit

The leaf remains open on existence. It may close only with:

- a finite stable order and exact proof of finite generation, local freeness, multiplication, and invariance; or
- an independently reviewed class-level obstruction showing that no allowed stable-order construction can cross the remaining Keller boundary.
