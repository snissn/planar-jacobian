# Adversarial Review Pass

```text
review_type: CONSTRUCTOR_SELF_ADVERSARIAL_REVIEW
independence: NOT_INDEPENDENT
reviewed_base: 296867d82d09d51ef2386de2a62067408b7f949c
authority: MUTABLE_NONAUTHORITATIVE
protocol_verdict: null
freeze_disposition: BLOCKED_PENDING_INDEPENDENT_REVIEW
```

This is a separate adversarial pass over the issue-scoped artifacts. It is not the independent exact-byte `ACCEPT` required for scientific promotion. Its purpose is to expose and repair hidden assumptions before handoff.

## Reviewed path set

```text
research/issues/issue-3-unramified-index/README.md
research/issues/issue-3-unramified-index/THEOREM-PACKET.md
research/issues/issue-3-unramified-index/COLLISION-DIVISORS.md
research/issues/issue-3-unramified-index/COUNTERMODELS.md
research/issues/issue-3-unramified-index/PROPOSED-SYNC.md
research/issues/issue-3-unramified-index/HANDOFF.md
research/issues/issue-3-unramified-index/verify_index_models.py
research/issues/issue-3-unramified-index/ARTIFACT-MANIFEST.sha256
```

Shared ledger and graph edits are reviewed separately as synchronization, not as theorem authority.

## 1. Quantifier and localization audit

### Finding A1 — ambiguous height-one localization

A statement about `O_q` for each prime `q` over `p` is insufficient. The product/semilocal collision can survive even when every factor projection is generated.

**Correction applied:** all local generation statements use

```text
O_p=O tensor_B B_p
```

and the special-fiber criterion `kappa(p)[bar(theta)]=O_p/pO_p`. The `A x A` example is retained as a negative control.

### Finding A2 — generic primitivity versus integral generation

`K(theta)=L` controls only the generic fiber and does not imply `B_p[theta]=O_p`.

**Correction applied:** every generation claim is expressed through the index module, Fitting ideal, or special-fiber algebra. Generic primitivity is used only to identify the power-basis rank.

## 2. Module-theoretic audit

### Finding B1 — hidden finite-flat assumption

A global determinant formula requires equal-rank locally free modules; normality alone was initially being used too quickly.

**Correction applied:** `THEOREM-PACKET.md` includes the local proof that a finite normal surface algebra over the regular two-dimensional base is finite locally free: normality gives Cohen--Macaulay local rings, base parameters form regular sequences, and Auslander--Buchsbaum gives local freeness. No smoothness of `Y` is assumed.

### Finding B2 — rank-two quotient need not split without trace

The assertion that `O/B*1` is invertible needs the unit section to be a direct summand.

**Correction applied:** `(1/2)Tr_{O/B}` is explicitly used as the retraction before applying `Pic(B)=0`.

### Finding B3 — Fitting ideal versus conductor

The conductor and Fitting/index ideal are not generally equal.

**Correction applied:** only equality of their height-one support is asserted. The exact discriminant relation uses the Fitting determinant, not the conductor.

## 3. Local monogenicity audit

### Finding C1 — the local lemma cannot assume a coefficient field silently

The special-fiber local Artin factor needs a lift of its finite residue extension.

**Correction applied:** separability/formal etaleness is stated, and finite Newton iteration recovers the coefficient-field element inside `k[beta+tau]`.

### Finding C2 — product factors require simultaneous separation

Generators of individual local Artin factors do not automatically generate their product.

**Correction applied:** constants are chosen over the infinite residue field so that the translated annihilator polynomials are pairwise coprime; the Chinese remainder theorem then gives one product generator.

### Finding C3 — patching can create new index support

The finite-prime patching theorem might be misread as an iterative elimination algorithm.

**Correction applied:** the theorem is explicitly limited to a prescribed finite set. The connected rank-three countermodel proves that repeated patching need not terminate and may only move support.

## 4. Globalization audit

### Finding D1 — contraction of a height-one prime of `B[theta]`

The `R1` proof must show that a height-one prime of the hypersurface order contracts to height one in `B`, not to zero or to a closed point.

**Correction applied:** incomparability excludes contraction zero, and dimension preservation under a finite integral extension gives height one.

### Finding D2 — circular use of the Keller conclusion

Global monogenicity and degree one must be separated.

**Correction applied:** `R1/S2` proves `B[theta]=O` using only normalization. The Keller open immersion is introduced afterward. The derivative/minimal-polynomial contradiction then proves degree one.

### Finding D3 — Hartogs overreach

Regular functions on a punctured normal surface extend, but an affine torsor need not trivialize because `H^1` of the punctured surface can be nonzero.

**Correction applied:** the affine-transition theorem is restricted to a cover of all `Spec(B)` or to a cocycle independently shown to extend there.

## 5. Countermodel audit

### Finding E1 — disconnected products are too weak

A product algebra would show residual collisions but not refute a bridge restricted to connected normalizations.

**Correction applied:** the main countermodel is a connected domain with irreducible generic cubic.

### Finding E2 — local monogenicity must cover every base point

A model with only a codimension-two bad fiber would not refute “locally monogenic everywhere implies globally monogenic.”

**Correction applied:** the main model is generated by `w` on `D(t)` and by `e` on `D(t^2+1)`; these opens cover the whole base.

### Finding E3 — normality and branch support need proof

**Correction applied:** the one-dimensional model is checked prime by prime. At `t` and the factors of `t^2+1` the local rings are explicit DVRs; elsewhere the trace discriminant is a unit. Polynomial extension supplies the surface model.

### Finding E4 — mutation family might be too narrow

A one-parameter failure would not rule out polynomial expressions in several generators.

**Correction applied:** every element of the free rank-three algebra is uniquely `c+xw+ye`, and the universal index form is computed. The obstruction therefore covers all elements, including every polynomial expression.

### Finding E5 — collision support might still be ramified

**Correction applied:** for a ramification-adapted element the index polynomial is coprime to `t(t^2+1)`. Every height-one component of its nonempty zero divisor has unramified generic point.

### Finding E6 — rationality was not tested

**Correction applied:** a second normal rank-three model has fraction field `C(u,s)` and the same moving-index behavior, while its origin has an embedding-dimension-two nonmonogenic fiber. The artifact does not claim this model has the Keller open immersion.

## 6. Vandermonde and symbolic audit

The exact verifier independently recomputes:

- associativity of the rank-three multiplication table;
- `Phi=-(t x^3+(t^2+1)y^3)`;
- `disc(O/B)=-27t^2(t^2+1)^2`;
- the square-index discriminant identity;
- the rational model index form `-(ux^3+vy^3)`;
- the biquadratic determinant `-4c^2(u-c^2v)`;
- the Vandermonde `64c^2uv(u-c^2v)`.

The script is not used to prove normality, the no-unit degree argument, or the local-to-global theorems; those remain analytic.

## 7. Source audit

No external classification or literature theorem is imported as a new load-bearing result. `CLM-003` remains a declared dependency and is not re-promoted. The issue therefore creates no new theorem-number/source obligation. The standard commutative-algebra steps are written at the exact scope used.

## 8. Overclaim audit

The artifacts do **not** claim:

- a proof or disproof of the planar Jacobian conjecture;
- a Keller counterexample;
- that all rational normal finite covers have moving index divisors;
- that every finite-dimensional mutation family fails;
- that local monogenicity is never useful;
- that class-group information can never contribute when combined with an effective-support theorem.

The exact negative inference is only:

> The unramified moving-index divisor cannot be eliminated from the stated purely algebraic hypotheses. Any surviving proof must use additional Keller-specific structure.

## 9. Review disposition

```text
mathematical_scope_check: NO KNOWN INTERNAL BLOCKER AFTER CORRECTIONS
independent_acceptance: ABSENT
freeze_or_promotion: BLOCK
mutable_branch_handoff: READY
```

The smallest independent-review targets are:

1. the semilocal DVR generator proof, especially the coefficient-field/Newton step;
2. the finite-prime patching formula;
3. the `R1/S2` contraction argument;
4. normality and the universal index form of the connected rank-three model;
5. the exact boundary between the algebraic counterexample and the Keller-specific successor.
