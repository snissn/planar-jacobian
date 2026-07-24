# Issue #17 Exact-Byte Adversarial Review

> **Authority:** `MUTABLE_NONAUTHORITATIVE`  
> **Review kind:** constructor adversarial audit; **not independent acceptance**  
> **Disposition:** `BLOCK`  
> **Block scope:** promotion, freeze, and downstream theorem authority only  
> **Protocol verdict:** `null`  
> **Scientific execution:** none

## Binding identity

- **Repository:** `snissn/planar-jacobian`
- **Baseline:** `86d1b78cedd788b7335be692f9bb92921142c7d3`
- **Intended baseline PR:** `#15`
- **Issue:** `#17`
- **Candidate branch name:** `issue-17/defect-4-staircase`
- **Candidate manifest:** `issue-17-defect-4-candidate-manifest.json`
- **Manifest SHA-256:** `27895f457975d52c726bdf037b3e82f46bacaf0160fb857c54078aee2774e987`
- **Candidate aggregate SHA-256:** `21550a32815a617cdb108c41954fb422c66773656a560505aeefcbf180a4a097`
- **Candidate files:** `20`
- **Workflow SHA:** `08bd5bc84654523677ebb851be09d4f4b3a81013`
- **Review-checklist SHA:** `4b94e69fb2a936cafbb5b034c9380e9a551a1ce2`
- **Evidence-scope SHA:** `63bda2c2398709d7ccc9433e1ed9cb93db56f3db`

Any change to a listed candidate file, the baseline, the manifest, the scope, or
the theorem statement invalidates this review record.

## Declared checkpoint

```text
Evidence level: E3
Quantifier level: Q3 restricted to all polynomial Keller pairs in the
                  declared positive-weight defect-at-most-four class
Stability level: S0 / static algebraic theorem; no dynamical stability claim
```

Candidate theorem:

> For a primitive positive weight `w=(p,q)`, every polynomial pair
> `F=(P,Q)` over `C` with `J(P,Q)=1` and
> `kappa_w=deg_w(P)+deg_w(Q)-p-q<=4` is a polynomial automorphism.

The candidate does not assert `JC_2`, does not treat defect at least five, and
does not prove that an arbitrary Keller pair admits a positive weight of defect
at most four.

## NEED findings

### 1. Rees identity and staircase — positive

The chain rule was recomputed from the two determinant products. Both carry the
factor

```text
t^(d_P+d_Q-p-q),
```

so `J(Pcal,Qcal)=t^kappa`. Coefficient comparison gives

```text
sum_(i+j=n) J(P_i,Q_j)=delta_(n,kappa).
```

Each bracket lies in the homogeneous piece of weight `kappa-i-j`; hence every
bracket above the resonant stair vanishes individually. No sign or exponent
blocker was found.

### 2. Resonant-pair classification and normalization — positive

A nonzero constant bracket at a weighted-homogeneous pair forces an invertible
linear part at the origin, so the component-degree multiset is `{p,q}`. For
`p<q`, the pair is explicitly triangular; for `p=q`, primitivity gives the
ordinary linear case. The inverse graded source map has Jacobian `1/c`, and the
compensating target map `(u,v)->(u,cv)` has determinant `c`; their composition
preserves `J=1` and sends the selected layers to `(x,cy)`. No silent
normalization `c=1` remains.

### 3. Common-power lemma and target descent — positive

For nonzero homogeneous `f,g` with `J(f,g)=0`, contraction of `df wedge dg`
with the weighted Euler field gives

```text
alpha f dg-beta g df=0.
```

Unique factorization yields `f=aH^m`, `g=bH^n` with coprime exponents. When one
exponent is one, the exact triangular target shear cancels a complete top layer,
preserves `J=1`, and strictly lowers the nonnegative integer `kappa_w`. No
cancellation confined to one coefficient equation is counted as descent.

### 4. Defects zero through three — positive

The lower-defect candidate was not imported from conversation prose. Endpoint
resonances, the defect-two divisibility contradiction, both defect-three
orientations, equal weights, `p=1<q`, `1<p<q`, and absent layers were recomputed.
The equal-weight coefficient identities were independently checked symbolically.
No omitted lower-defect resonance was found.

### 5. Defect-four resonance table — positive

All endpoint positions make a full component a coordinate. The interior
positions have the following exact disposition:

- `(1,3)`: top-power descent or the sequence `S_1,S_2,S_3` gives
  `S_3=2acx`;
- `(3,1)`: top-power descent, a support contradiction, or at weight `(1,2)`
  a nonzero `cv y` coefficient in `S_2`;
- `(2,2)`: a zero middle Wronskian gives the common-factor divisibility
  contradiction; a nonzero Wronskian forces finite support cases, with the
  exceptional weight `(1,2)` governed by

  ```text
  3af=4bv,
  J(P_1,Q_1)=(2uf-3ve)x^2-vfy,
  (3ac+2uf-3ve)x^2-vfy=0.
  ```

  These equations force `v=f=0` and then `3ac=0`, impossible.

The source swap with weight relabeling covers `p>q`, and the determinant-one
target swap covers reversed resonant degree orientation. No surviving formal
full-staircase layer system was found.

### 6. Adversarial countermodel control — positive

The central equation alone admits a false positive:

```text
P_0=x^3, Q_0=x^4, P_1=y, Q_1=x^3, P_2=x, Q_2=y.
```

It satisfies `S_0=0` and `S_2=0`, but `S_1=-4x^3`. This exact countermodel to a
central-only argument confirms that the preceding stair is load-bearing and is
properly retained in the proof.

### 7. Transformation catalogue — positive

Every target and source operation used by the proof is stated with its exact
Jacobian. Same-index target `SL_2` changes preserve the middle Wronskian, and
graded symplectic source changes pull it back, so the packet does not claim a
false universal Wronskian-removal normal form. Completion-valued or formal
Hamiltonian exponentials are excluded unless polynomiality and filtration
termination are separately proved.

### 8. Literature boundary — positive at stated use

The full hypotheses of Shaska's v1 Theorems 3.2 and 3.3 were checked. Lee--Li,
Karaś, Pan, and Su are used only as primary-literature context and category
boundaries. The theorem candidate is self-contained and does not consume a
Newton, monodromy, or filtered-Hamiltonian theorem.

### 9. Validation and synchronization — positive as process evidence

```text
symbolic/support checks: 2443
primitive weights enumerated: 1966
defect-four regression validation: PASS
claims: 52
graph nodes: 34
graph edges: 50
candidate synchronization: PASS
```

The inherited full-repository validator was not run in the local overlay because
the complete baseline checkout and archive payloads were unavailable. The
manifest records that limitation. No validator result is treated as mathematical
authority.

## Disposition

`BLOCK`

The smallest blocker is **reviewer independence**. The pinned workflow states
that the constructor must not be the sole reviewer and requires final
independent acceptance of the exact candidate bytes for a scientific analytic
result. This record was produced by the same assistant that constructed and
revised the candidate. It therefore cannot confer acceptance, freeze, or
mainline authority even though this adversarial pass found no mathematical
counterexample or omitted defect-four case.

The exact surviving result is retained as `candidate_proved` on a mutable,
non-authoritative branch artifact. A distinct reviewer must recompute the NEED
items against the manifest and return `ACCEPT` or the smallest concrete
mathematical/provenance `BLOCK`.

## Nonblocking deferrals

**SHOULD:** a second independent symbolic implementation and an alternative
organization of the support exhaustion.

**COULD:** defect-five work, Newton--Puiseux or boundary-monodromy
interpretation, and a theorem forcing a small-defect positive weight for a
general Keller pair.

None of these broader items is a reason to block the scoped mathematics; the
current `BLOCK` is solely the mandatory independence/provenance gate.
