# Local adversarial review

```text
review_mode: local-adversarial-review
candidate_revision: 02321cf2a78989f8d3cc57872c1e76961d3cd0d1
disposition: ACCEPT_FOR_CANDIDATE_INTEGRATION
promotion_disposition: BLOCK_PROMOTION
reviewer_independence: NOT_INDEPENDENT_SAME_ASSISTANT
```

## 1. Reviewed scope

The review is bound to the exact issue-owned candidate revision above. That
revision contains the mathematical files and exact symbolic validators, but not
this review, the later handoff, or the integration manifest. The review tests
whether the packet is coherent enough for preservation as mutable candidate
work. It does not confer reviewed authority, independently accept a theorem, or
license a general one-boundary conclusion.

Critical files reviewed:

- `FOUNDATIONS.md`;
- `BOUNDARY_NORMALIZATION.md`;
- `LAURENT_RECURSION.md`;
- `CONDUCTOR_GLUING.md`;
- `LOGARITHMIC_FIELDS.md`;
- `WEIGHT_EXTRACTION.md`;
- `CASE_TABLE.md`;
- `FORMAL_MODELS.md`;
- `SOURCE_AUDIT.md`;
- `validate_laurent_conductor.py` and `verify_all.py`.

## 2. Attack: differential signs and ramification order

The sign check starts from

```text
dP wedge dQ=dx wedge dy
```

and recomputes

```text
d(P dQ+y dx)=0,
d(P dQ-y dx)=2 dx wedge dy.
```

At a tame completed ramified DVR, a target local parameter has order `e` in
the logarithmic radial basis `dt/t`; the tangential residue differentials wedge
to zero because the residue field has transcendence degree one. Therefore the
pulled-back target two-form has order at least `e`.

**Disposition:** pass. The sign mutation and arbitrary-index formal controls are
symbolically checked.

## 3. Attack: the change `s=x^(-1/m)`

The proof needs more than replacing the leading coefficient. After adjoining an
`m`-th root of the leading coefficient, the binomial series gives an actual
formal uniformizer `s` with `x=s^(-m)`. Since `s=t` times a unit, the radial
basis changes by a unit plus a tangential term. Wedges of tangential one-forms
vanish in the one-variable coefficient field, so this change cannot manufacture
a lower-order radial coefficient.

With `y=sum c_j s^j`, direct differentiation gives

```text
dx wedge dy=-m sum_j s^(j-m) ds/s wedge d c_j.
```

Distinct powers cannot cancel. The conclusion `c_j in C` for `j<m+e` uses that
a finite extension of a complex function field introduces no new constants.

**Disposition:** pass at formal-local candidate scope. No algebraization of `s`
is claimed.

## 4. Attack: the resonant coefficient and branch exactness

Because `P,Q` are regular power series, `P dQ` has no radial `s^0 ds/s`
coefficient. The exact differential `dH` also has zero radial residue. Thus the
unique source resonance is

```text
-m c_m=0.
```

Since `dx` is purely radial after normalization, the tangential order-zero
coefficient of `y dx` is zero. The tangential order-zero equation is therefore

```text
pullback(P dQ)=d h_0.
```

Tracing through the finite separable coefficient and residue-field extensions
commutes with the universal derivation and sends a base form to the field degree
times that form. This yields `P dQ=dR` in the normalized target branch function
field.

**Disposition:** pass. This is the packet's load-bearing new theorem. It should
receive independent review before promotion.

## 5. Attack: divisors and the one-puncture shortcut

The first draft risk was to treat the leading coefficient as an ordinary unit
on the affine boundary. The final candidate distinguishes a rational conormal
section from a function. The common-power conclusion is made in the function
field and records divisors without dividing at zeros. A one-puncture unit is
constant only after an honest function trivialization is separately supplied;
a line-bundle section can have nonzero degree at that puncture.

**Disposition:** corrected before the pinned candidate; pass.

## 6. Attack: conductor descent

From `dR=P dQ` and regularity of `P dQ`, a pole of `R` on the affine normalized
curve would differentiate to a pole, so `R` belongs to the normalization ring.
The class `[R] in Abar/A_C` is finite conductor data.

A stronger draft inference treated every nonzero class as a Keller
contradiction. That is not justified: the source primitive coefficient need not
itself be a function on the singular target branch. The final packet says that
the class is obstructive only when the separately declared gluing problem
requires target descent.

**Disposition:** corrected before the pinned candidate; pass.

## 7. Attack: explicit non-toric branches

For

```text
g_ne=P(P-1)Q-1,
```

the normalization calculation gives residues `+1` and `-1` for `P dQ`, so the
branch is excluded at order zero.

For

```text
g_ex=P Q^2(Q-1)^2+(Q-1)^2+Q^2,
```

the normalization `Q=z`, `P=d(1/z+1/(z-1))/dz` gives exact `P dQ`. The curve
excludes `Q=0,1`; its coefficient of `P` is a unit on the curve, so it is smooth
with normalization `P1-{0,1,infinity}`. Three punctures exclude the axis,
same-sign binomial, and hyperbolic monomial classes from the predecessor torus
classification.

The logarithmic-basis construction for a branch linear in `P` was also attacked.
A coefficient depending only on `Q` was insufficient; the final construction
uses `c=u(Q)P+v(Q)` and is verified symbolically.

**Disposition:** pass. The exact branch is correctly called a formal/control
survivor, not a Keller counterexample.

## 8. Attack: formal models and realization labels

The arbitrary-`e,m` family satisfies the complete displayed Jacobian and
primitive identities. The stronger rational control generates the full source
function field and has a polynomial primitive, but its target function
`P=x^(-e)` is not polynomial. The non-toric mutation adds rational denominators
in both the target and primitive.

**Disposition:** pass. The first failed Keller condition is stated explicitly as
polynomial realization. No model is mislabeled as algebraized, polynomial, or
Keller.

## 9. Attack: bounded-weight extraction

The pole vector supplies a candidate weight but not the weighted degrees of the
whole polynomials. The common-power cancellation

```text
y^m0-lambda x^n0
```

has arbitrarily large displayed powers while its first valuation layer cancels.
This proves only that the current local data do not imply a defect bound. It is
not claimed to be a Keller-preserving mutation or a counterexample to a future
qualifying-weight theorem.

**Disposition:** pass. No use is made of the unreviewed defect-five candidate.

## 10. Scope attacks

The theorem requires a generically ramified divisor and at least one source
coordinate pole. The packet does not prove that every one-boundary model has
such a pole, does not bound the valuation/conductor types, and does not turn
formal all-orders consistency into algebraization. Connectedness and purity are
not overextended beyond the predecessor exclusions.

**Disposition:** pass with the explicit surviving global bridge `NTLC-09`.

## 11. Validation evidence

The candidate validator independently checks:

- the symplectic and primitive signs;
- the leading common-power equation and a sign mutation;
- normalized recursion indexing;
- exact and nonexact three-puncture branches;
- a logarithmic Saito basis for the exact branch;
- the cusp conductor control;
- arbitrary-index toric and non-toric formal families;
- field-generating rational controls;
- cancellation powers and weight-dependent defects.

The packet verifier additionally checks artifact completeness, ownership,
manifest fields, review binding, issue-local labels, and absence of forbidden
transport files.

## 12. Final disposition

`ACCEPT_FOR_CANDIDATE_INTEGRATION` means the packet supports the exact mutable
claim:

```text
ramified pole-supported one-boundary Keller data
=> P dQ is exact on the normalized target branch;
therefore the Liouville-nonexact non-toric subclass is impossible.
```

`BLOCK_PROMOTION` remains mandatory because the same assistant constructed and
reviewed the candidate, the formal change and trace descent have not received an
independent mathematical review, and the general Liouville-exact class remains
open at conductor, higher differential, algebraization, polynomial realization,
and Newton-support control.
