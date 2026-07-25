# Local Adversarial Review — Defect Five

> **Review mode:** `local-adversarial-review`  
> **Reviewer:** constructing-agent in a separately declared review pass  
> **Candidate commit:** `2eeb36d232366d124b5a66774b29769ec1eba43d`  
> **Candidate tree:** `c2b111ecf070eac1f59c7bb505e82820563ef3cd`  
> **Candidate base:** `99c90e393cde7f15e34aaae3726c4d4ab305e0fb`  
> **Candidate inventory SHA-256:** `333614389c339f4a3383856de2dfc5b977dc5dd6a6520f176b25c7116d861d12`  
> **Disposition:** `ACCEPT` at local-adversarial-review scope  
> **Canonical authority after this review:** `candidate_proved`, not `reviewed_scoped`

## 1. Exact binding

The review treats the following candidate blobs as immutable:

| Path | Git blob |
|---|---|
| `README.md` | `20e5f1e5c2c0a06f044e31b2abf27d9f499506b2` |
| `FOUNDATIONS.md` | `7ee1ae5f7fff3b34a73fee5819d35c91c531c026` |
| `TRANSFORMATIONS.md` | `4869da7f6d9a68e84d0cbe69fa621d20dcfa4b65` |
| `DERIVATION.md` | `97eeac0375ead289b0c87646e34b0e2b99411988` |
| `CASE_TABLE.md` | `e21969832bb6c8214e772f214fd352b0e786686d` |
| `COUNTERMODEL_SEARCH.md` | `d7f8b56ce0ac9a50b0f283a861cb7d78e2adcba3` |
| `VALIDATION.md` | `e7770db79053ff2835d59550d1602eec9558d8eb` |
| `validate_defect5.py` | `e702b0114642c20b71111b702ef883d6473e84d5` |

The inventory digest hashes sorted `path NUL blob-sha NUL` records. It binds
transported bytes without pretending to be a mathematical certificate.

## 2. Disposition

`ACCEPT` for the following candidate statement:

> For a planar Keller pair over `C` and a primitive positive weight `w`, if the
> actual grading defect is `kappa_w=5`, then the pair is a polynomial
> automorphism. A nonzero resonant endpoint is already invertible; every
> interior case either has an exact complete-top target descent to a
> nonnegative defect at most four or contradicts the complete stairs.

This is not an independent-review acceptance. The same agent constructed and
reviewed the packet, although the review pass and reviewer-owned checker were
kept separate. Mainline status must remain `candidate_proved` until a distinct
reviewer binds a disposition to the exact candidate revision.

## 3. Reconstruction performed

The review did not accept the conversation or the defect-four proof as authority
for transformed defect-five equations. It independently checked:

1. the chain-rule exponents in `J(Pcal,Qcal)=t^kappa` and every sign in
   `S_0,...,S_5`;
2. the constant-bracket classification and the determinant compensation in the
   scalar-retaining normalization;
3. preservation of every weighted layer by the explicit graded source inverse;
4. covariance of all unselected resonant brackets, including the sign under
   `(P,Q)->(Q,-P)`;
5. the UFD common-power argument and the exact hypotheses that make `H`
   nonconstant and homogeneous;
6. determinant-one complete-top descent, cancellation of the whole top layer,
   and strict decrease of the actual integer defect;
7. the unbounded support sieve `p<=a`, the exclusion of a `y`-term in an
   unequal-weight no-descent root, and each divisibility/congruence family;
8. all four interior offsets, with both equal-weight systems reconstructed in
   `H`-adapted coordinates;
9. every finite unequal-weight exception with its complete support; and
10. the distinction between support consistency, coefficient consistency,
    actual polynomials, and actual Keller pairs.

## 4. Adversarial challenges

The following possible failures were actively tested.

### 4.1 Sign and transformation mutations

The review substituted the plus-sign determinant, the unsigned component swap,
an uncompensated target scaling, and a non-graded source substitution. Each
mutation changes a required identity or layer degree and is detected. The
correct signed swap retains the scalar because `J(Q_b,-P_a)=J(P_a,Q_b)`.

### 4.2 Premature specialization of the resonant scalar

The selected scalar remains `c!=0` throughout construction. The exceptional
systems retain simultaneous terms such as `c-vk=1`. The contradictions occur on
earlier stairs, so no proof step silently assumes all other resonant brackets
vanish or sets `c=1` before justified.

### 4.3 Missing layers

Complete semigroup supports were regenerated through `S_5`; empty pieces are
literal zero. Removing a nominally missing layer does not alter a certificate,
while adding an unsupported monomial changes its weighted degree and is rejected.

### 4.4 Finite-looking weight patterns

A separate enumeration through primitive weights `p<=q<=160` was compared with
the unbounded inequalities. Every nonempty no-descent common-root support lies
in the declared congruence families. The enumeration is evidence; the proof of
completeness is the bound `p<=a<=4` plus the `2q<=p+a` exclusion.

### 4.5 New equal-weight terms

For `(2,3)`, the reviewer recomputed

```text
Q_1=(4B/(3A)) X P_1+E X^3
```

and found the `Y^3` coefficient of `J(P_1,Q_1)` to be
`-8B g^2/(3A)`. Thus the quadratic transverse term is forced to zero before the
remaining ideal is formed. For `(1,4)`, the reviewer regenerated the complete
quartic/cubic/quadratic chain. These are genuinely new defect-five corrections,
not applications of the defect-four middle-Wronskian row.

### 4.6 Formal countermodel search

The reviewer-owned checker independently generated and saturated the six
unequal exceptional ideals and the two equal-weight ideals. Every ideal contains
one after saturation by the required nonzero coefficients. No complete-staircase
formal countermodel survives.

## 5. Reviewer-owned checker

`review_validate_defect5_adversarial.py` imports no construction checker. Its
observed output was:

```text
review mode: local-adversarial-review
primitive weights re-enumerated (<=160): 7806
exponent-one descents reclassified: 1583
nonempty no-descent family labels: 12
independent saturated ideals eliminated: 8
largest reviewer ideal: 14 equations, 19 variables
independent Rees/normalization trials: 8
adversarial review checker: PASS
```

The run is process evidence. It does not elevate the review to independence or
replace the human reconstruction.

## 6. Scope and residual risk

No mathematical gap was found in the candidate. Residual risk is review
independence, not a named surviving weight or equation. A distinct reviewer
should focus on the equal-weight coordinate changes, the root-support exclusion,
and the exceptional support completeness before any promotion.

The accepted scope does not assert that every Keller pair has a primitive
positive weight of defect at most five, does not begin defect six, and does not
establish `JC_2`.
