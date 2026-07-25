# Local Adversarial Review

```text
review_mode: local-adversarial-review
reviewed_revision: eefb40d0475dcdc5a3b07d89ce84354a4b210280
reviewed_scope: R3BC-01 through R3BC-05, R3BC-07, and all exact scripts
constructor_independence: none; this is not independent scientific acceptance
disposition: ACCEPT_LITERATURE_BOUND_RANK_THREE_TERMINAL_AND_SCOPED_INTERNAL_REFINEMENTS; BLOCK_CONSTRUCTIVE_UNIT_SECTION_AND_BROADER_PROMOTION
```

## 1. Review protocol

This review was rerun as a separate pass after the strengthened scientific
candidate, including the full-text Orevkov audit, was pinned at

```text
eefb40d0475dcdc5a3b07d89ce84354a4b210280.
```

No proof file in that revision was edited during this rerun. The pass:

1. read the load-bearing parts of Orevkov's English primary PDF, including the
   definition of multiplicity, Theorem 1.1, and the closing degree-three cases;
2. remapped every hypothesis of that theorem to the Keller setup;
3. recomputed the field-degree-to-generic-sheet-number bridge;
4. recomputed all three rank-three special-fiber determinants;
5. challenged the simultaneous boundary-adaptation argument at semilocal primes;
6. differentiated the split-sheet Vandermonde to test the claimed differential
   limitation;
7. mutated the countermodel ladder at the first source-étale stage;
8. checked the cited MathOverflow answer against the broader prime-degree
   preprint's use of it;
9. reran the exact symbolic suite.

This is a constructor self-audit and creates no `reviewed_scoped` status.

## 2. Load-bearing questions

### A. Does normalization rank three really imply Orevkov's “three-sheeted” hypothesis?

Yes, at the exact generic scope. For a dominant polynomial map with finite field
extension, clearing denominators makes `C[x,y]` finite over a localization of
`C[P,Q]`. The Keller Jacobian makes the finite restriction étale after shrinking.
A finite étale algebra of rank three has three geometric points in every fiber.
No global properness or finiteness over the entire target is inserted.

Orevkov's Section 1 independently defines the multiplicity of the map as the
number of preimages of a generic point. Thus the packet bridge lands in the
paper's own terminology exactly.

### B. Is Orevkov being quoted at a stronger scope than the primary source?

No. The English primary PDF begins with a polynomial map `C^2 -> C^2` having
nonzero constant Jacobian, defines generic-fiber multiplicity, and states in
Theorem 1.1 that multiplicity cannot be two or three. The final proof assumes
multiplicity three, exhausts the three configurations from Lemma 4.2, and closes
with a contradiction in each case. The packet imports no all-prime-degree theorem
and no independent boundary classification from Orevkov.

`R3BC-01` remains `literature_bound` because the external ten-page proof is
source-audited rather than reproduced as a new internal proof. There is no
remaining source-access or terminology gap.

### C. Does the terminal theorem construct a unit-index section?

No. The reviewed packet states repeatedly that the rank-three hypotheses are
inconsistent, so the fixed-section problem is bypassed rather than solved
constructively. It does not exhibit `s`, `U,V`, or a monogenic order, and it does
not advertise vacuous truth as a construction.

### D. Was finite local freeness inferred merely from the word normalization?

No. The Orevkov terminal needs neither the trace bundle nor finite local
freeness. The internal cubic calculations retain the predecessor's explicitly
audited finite-locally-free rank-three hypothesis. Those conditional
calculations are separated from the literature terminal.

### E. Is every boundary cubic a cube?

No. Direct determinant recomputation gives:

```text
k x k x k:                         L1 L2 L3,
(k[epsilon]/epsilon^2) x k:        L M^2,
k[epsilon]/epsilon^3:              L^3.
```

The packet corrects, rather than assumes, the boundary-cube slogan. The use of
these three algebras is valid after strict henselization in residue
characteristic zero: residue extensions split and tame ramification of total
rank three has partitions `1+1+1`, `2+1`, or `3`.

### F. Does the boundary-adapted family handle the whole semilocal algebra?

Yes. The predecessor's finite-prime theorem chooses `theta` generating
`O_p=O tensor_B B_p`, not merely each DVR factor. Since

```text
s_T=theta+H T eta == theta mod p
```

for every boundary prime `p|H`, the full special-fiber algebra is still generated;
Nakayama gives equality of the whole semilocal localization. Taking the
trace-zero part changes the section only by a base scalar and does not alter the
generated algebra or index cubic.

### G. Is the affine-family expansion exact?

Yes. Polarization and direct symbolic expansion give

```text
Phi(theta+H T eta)
 = D+H C T+H^2 B_2 T^2+H^3 A T^3.
```

Modulo every boundary prime this is `D=Phi(theta)`, a unit. Therefore the family
cannot create a boundary factor. The packet does not infer that the remaining
polynomial is constant.

### H. Does source étaleness eliminate a scalar sheet collision?

No. On the split étale locus,

```text
Phi(s)=product_{i<j}(z_j-z_i).
```

One factor can vanish while the three source points remain distinct in `(x,y)`.
The logarithmic derivative records relative scalar velocities and does not turn
that collision into ramification. The packet preserves this predecessor
correction.

### I. Was translation stability silently assumed for a fixed value ideal?

No. It proves only the negative lemma that a nonconstant divisor cannot be
stable under both `partial_P` and `partial_Q`. It then explicitly observes that
`(Phi(s))` is not known to be stable because differentiating changes `s`. The
minimal-degree differential-ideal argument is not misapplied.

### J. Does the countermodel ladder really stop at stage 5?

Yes, under the specified source-open meaning. If the relative differential
support misses the displayed `A^2`, restriction gives
`Omega_{C[x,y]/C[P,Q]}=0`. The square Jacobian presentation then makes
`J(P,Q)` a unit of `C[x,y]`, hence a nonzero constant. The function-field degree
remains three, so Orevkov gives the contradiction. An arbitrary abstract open
`A^2` not carrying the specified restriction would not suffice, and the packet
states this caveat.

### K. Is the broader prime-degree claim safely separated?

Yes. The reviewed packet does not rely on arXiv:2407.13795. The cited
MathOverflow answer chooses a quadratic extension and constructs an example; it
does not prove a degree-two classification. The packet supplies a degree-three
rare-property model and an exact root-orbit proof that every nonconstant monomial
is primitive. That model is used only to reject the shortcut, not as a Keller or
no-unit counterexample.

## 3. Exact checks

The reviewed revision was reproduced locally with SymPy 1.14.0 and Python 3.12.
The following command passed:

```text
python3 research/issues/rank-three-boundary-cube-unit/verify_all.py
```

It reports:

```text
binary cubic and boundary-fiber verification: PASS
index, Fitting, and discriminant-square verification: PASS
boundary-adapted affine-family verification: PASS
countermodel-ladder verification: PASS
prime-degree literature-audit controls: PASS
rank-three boundary-cube packet verification: PASS
```

The scripts check algebraic identities and bounded falsification controls. They
do not prove Orevkov's theorem or mathematical truth outside their stated
scope.

## 4. Unresolved risks and limits

1. Orevkov's primary proof has been audited at its definition, theorem, proof
   architecture, and terminal cases, but it is not independently reproved in
   this packet; the claim remains `literature_bound`.
2. The conditional boundary-adaptation result consumes the predecessor's
   mutable finite-prime adaptation theorem (`CLM-029`). Orevkov's terminal does
   not depend on that claim.
3. The local cubic trichotomy is geometric after strict henselization; it is not
   a claim that one global `GL_2(B)` frame simultaneously normalizes all
   components.
4. No unit-index section is constructed and no method for degree four or higher
   follows.
5. The countermodel search is not a classification below the source-étale wall;
   only the impossibility of crossing that wall at degree three is terminal.
6. The criticism of arXiv:2407.13795v1 is limited to the identified first-case
   inference and does not adjudicate every version or every independent case.

## 5. Review disposition

### Accepted at mutable packet scope

- `R3BC-01`: exact full-text-audited application of Orevkov's primary
  rank-three theorem, at `literature_bound` scope;
- `R3BC-02`: geometric boundary-cubic trichotomy;
- `R3BC-03`: simultaneous boundary-prime elimination and exact affine-family
  polynomial;
- `R3BC-04`: differential movement without fixed-value stability;
- `R3BC-05`: countermodel ladder terminal at source étaleness;
- `R3BC-07`: packet-local rejection of the identified prime-degree shortcut.

### Blocked

- promotion to an internally proved or independently reviewed theorem;
- any statement that one concrete unit-index section has been constructed;
- any inference for prime degrees other than three;
- any proof of `JC_2`.

Final review result:

```text
ACCEPT_LITERATURE_BOUND_RANK_THREE_TERMINAL_AND_SCOPED_INTERNAL_REFINEMENTS;
BLOCK_CONSTRUCTIVE_UNIT_SECTION_AND_BROADER_PROMOTION.
```
