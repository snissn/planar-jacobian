# Exact Countermodel and Falsification Program

## 1. Scientific question tested

The checker searches the normalized no-descent branch, not merely a central
Wronskian equation. For each primitive `p<=q` and each interior offset
`a=1,2,3,4`, it computes

```text
d_P=p+a,
d_Q=q+5-a,
rho=gcd(d_P,d_Q),
m=d_P/rho,
n=d_Q/rho.
```

Exponent-one cases are declared exact target descents. In every remaining case,
the program generates the complete weighted support of the common root and of
every layer, sets only the selected pair to `P_a=x`, `Q_(5-a)=c y`, and builds
all coefficients of `S_0,...,S_5` from the Jacobian definition.

## 2. Independence from the defect-four checker

`validate_defect5.py` imports no repository checker and contains no defect-four
case allowlist. It independently implements:

- weighted support enumeration, including empty pieces;
- generic weighted-homogeneous layers;
- the signed Jacobian determinant;
- all six Rees stairs;
- projective common-root charts;
- symbolic selected scalar `c`;
- exact saturated Gröbner ideals;
- Rees verification on actual Keller automorphisms.

## 3. Search range and exact result

The committed run enumerates every primitive weight

```text
1 <= p <= q <= 120.
```

It constructs 428 support-realizable no-descent systems through `S_5`. Another
16,024 arithmetic no-descent patterns are rejected because the computed common-
root degree has empty weighted support. The finite exceptional coefficient
systems and the two equal-weight systems are eliminated over exact rational
polynomial rings after saturation by the nonzero top coefficients and resonant
determinant.

Observed output is recorded in `VALIDATION.md`. There are zero complete-staircase
formal survivors resisting the declared descent.

The bounded range is not the unbounded proof. Completeness for all weights comes
from the human inequalities `p<=a<=4`, the `rho<q` root-support argument, and the
exact congruence table in `DERIVATION.md` and `CASE_TABLE.md`.

## 4. Formal consistency, polynomials, and Keller pairs

Three levels are kept distinct.

1. **Support consistency:** degrees and monomial supports exist. This does not
   assign coefficients or satisfy a stair.
2. **Weighted-layer coefficient consistency:** all coefficients of
   `S_0,...,S_5` vanish except the constant one in `S_5`. Because every
   above-resonance bracket has negative weighted degree and hence vanishes, a
   complete coefficient solution with deeper layers set to zero would already
   define actual polynomials with `J=1` in the normalized coordinates.
3. **Actual Keller pair in the original coordinates:** this additionally uses
   the proved polynomial graded normalization and its inverse. The checker tests
   those transformations but does not elevate search output to theorem status.

No object reaches level 2 in a no-descent branch. Exact rational and algebraic
actual Keller automorphisms are used separately to validate the Rees machinery.

## 5. Multiple resonances and missing layers

All nonselected layers are generic complete supports or literal zero. The scan
finds six unequal-weight exceptional systems with more than one potentially
nonzero resonant bracket. Their `S_5` equations retain terms such as `c-vk=1`;
none is collapsed to `c=1` before support proves the other brackets zero.

The run generated 982 zero layers. Mutation tests also remove or add a layer to
ensure the coefficient signatures change as expected.

## 6. Corruptions deliberately detected

The checker rejects or distinguishes:

1. replacing `f_x g_y-f_y g_x` by a plus sign;
2. using the unsigned target swap `(Q,P)` instead of `(Q,-P)`;
3. uncompensated target scaling in the resonant normalization;
4. a non-graded source substitution that mixes layer indices;
5. shifting the Rees exponent by one.

The exceptional Gröbner systems are generated from the correct determinant, so a
sign mutation changes the ideal rather than being absorbed into a copied table.

## 7. Gröbner scope

Eight exact saturated eliminations are run:

- unequal exceptions `(1,2),(2,3)` at position `(2,3)`;
- unequal exception `(1,3)` at `(3,2)`;
- unequal exceptions `(1,2),(1,3),(2,3)` at `(4,1)`;
- equal-weight positions `(1,4)` and `(2,3)` in `H`-adapted coordinates.

The largest input has 14 coefficient equations and 19 variables. A unit basis
certifies inconsistency over the algebraic closure for these finite supports.
The human derivation gives shorter certificates and remains the authority-bearing
mathematics.

## 8. Countermodel disposition

No formal full-staircase countermodel was found or algebraically permitted. No
result is suppressed: the search output supports, but does not independently
authorize, the universal candidate theorem.
