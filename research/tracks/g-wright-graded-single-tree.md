# Track G — Wright Grading and Single-Tree Poisson Rigidity

> Status: `MUTABLE_NONAUTHORITATIVE`

In the smooth one-boundary model, the coordinate ring embeds in a Laurent ring with strong divisibility conditions on positive and negative graded pieces. The logs contain a candidate proof that no exactly homogeneous pair has nonzero constant bracket.

### New scoped support

Track M now contains a self-contained `candidate_proved` result for ordinary positive source weights with

```text
kappa_w<=4.
```

It gives exact top-power target descent and eliminates all three defect-four interior resonances. This is useful only if the Wright grading can be represented by such a positive polynomial weight with defect at most four while retaining the relevant constant bracket.

### Missing theorem

Convert an arbitrary Keller pair in the Wright one-boundary ring to a graded initial pair while retaining the first nonzero symplectic term and controlling all boundary valuations. Ordinary leading-form dependence is insufficient: powers with coprime exponents and multiple boundary valuations resist triangular reduction. The new small-defect theorem does not establish this conversion and does not bound the Wright defect.

### Broader single-tree form

If all boundary components lie in one exceptional affine-line fiber, prove that no normal affine-line-fibered surface ring can contain a constant-bracket pair unless the boundary is empty.

### Exit

A simultaneous Newton/valuation reduction that preserves the constant term and reaches either the homogeneous no-go theorem or the independently accepted positive-weight `kappa<=4` domain.

## Integrated one-boundary successor (2026-07-24)

The weighted-homogeneous one-boundary subclass is now excluded at candidate scope by `CLM-070`, provided the exact normalization and unique generically ramified boundary hypotheses hold. This does not supply the simultaneous graded reduction sought by `CLM-025`; it removes only the class in which an actual target grading already preserves the reduced branch.
