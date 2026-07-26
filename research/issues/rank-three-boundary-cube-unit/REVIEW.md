# Local Adversarial Review

```text
review_mode: local-adversarial-review
reviewed_revision: f85f9e1e7143bc36859543c3d5520d06fe99cb17
reviewed_scope: R3BC-01 through R3BC-05, R3BC-07, and all exact scripts
constructor_independence: none; this is not independent scientific acceptance
disposition: ACCEPT_LITERATURE_BOUND_RANK_THREE_TERMINAL_AND_SCOPED_INTERNAL_REFINEMENTS; BLOCK_CONSTRUCTIVE_UNIT_SECTION_AND_BROADER_PROMOTION
```

## 1. Review protocol

This review was rerun after the complete corrected candidate, including proof,
summary, handoff, integration metadata, and the repaired exact divisibility
validator, was pinned at

```text
f85f9e1e7143bc36859543c3d5520d06fe99cb17.
```

The correction distinguishes one boundary-adapted congruence class from the
unrestricted unit search. The validator amendment replaces rational cancellation
by exact polynomial division with a zero-remainder requirement and adds negative
mutation controls. No file in the pinned revision was edited during this review
pass. The pass:

1. read the load-bearing parts of Orevkov's English primary PDF, including the
   definition of multiplicity, Theorem 1.1, and the closing degree-three cases;
2. remapped every theorem hypothesis to the Keller setup;
3. recomputed the field-degree-to-generic-sheet-number bridge;
4. recomputed all three rank-three special-fiber determinants;
5. challenged semilocal boundary adaptation and the residue-class quotient
   `E/H E`;
6. checked separately what one fixed `theta` does and does not parametrize;
7. differentiated the split-sheet Vandermonde;
8. mutated the countermodel ladder at source étaleness;
9. checked the MathOverflow source against the broader prime-degree preprint;
10. inspected the repaired polynomial-divisibility assertion and its negative
    controls;
11. reran the exact symbolic suite;
12. checked that README, HANDOFF, INTEGRATION, and the PR body preserve the
    corrected restricted-family scope.

This constructor self-audit creates no `reviewed_scoped` status.

## 2. Load-bearing questions

### A. Does rank three imply Orevkov's “three-sheeted” hypothesis?

Yes. Clearing denominators makes `C[x,y]` finite over a localization of
`C[P,Q]`. The Keller Jacobian makes the finite restriction étale after shrinking.
Rank three then gives three reduced geometric points in every fiber on that dense
open. Orevkov's Section 1 defines multiplicity as the number of preimages of a
generic point, so the packet lands in the paper's terminology exactly. Global
properness or finiteness over the entire target is not inserted.

### B. Is Orevkov quoted at the exact primary-source scope?

Yes. The English primary PDF begins with a polynomial map `C^2 -> C^2` having
nonzero constant Jacobian, defines generic-fiber multiplicity, and states in
Theorem 1.1 that multiplicity cannot be two or three. The final proof assumes
multiplicity three, exhausts the three configurations from Lemma 4.2, and closes
with a contradiction in every case. The packet imports no all-prime-degree
claim. `R3BC-01` remains `literature_bound` because the external proof is audited
rather than reproduced as a new internal proof.

### C. Does the terminal theorem construct a unit-index section?

No. It proves that the simultaneous rank-three Keller hypotheses are
inconsistent. It does not exhibit `s`, `U,V`, or a monogenic order, and does not
advertise vacuous truth as a construction.

### D. Was finite local freeness inferred from normalization alone?

No. Orevkov's terminal needs neither trace splitting nor finite local freeness.
The conditional binary-cubic calculations explicitly retain the predecessor's
audited finite-locally-free rank-three hypotheses.

### E. Is every boundary cubic a cube?

No. Direct determinant recomputation gives

```text
k x k x k:                         L1 L2 L3,
(k[epsilon]/epsilon^2) x k:        L M^2,
k[epsilon]/epsilon^3:              L^3.
```

After strict henselization in residue characteristic zero, these are exactly the
partitions `1+1+1`, `2+1`, and `3`. A cube occurs only at total ramification.

### F. Does boundary adaptation generate the whole semilocal algebra?

Yes, for every member of the chosen congruence class. The predecessor chooses
`theta` generating the whole semilocal localization `O_p`, not merely each DVR
factor. Since

```text
s_T=theta+H T eta == theta mod p,
```

the whole special fiber remains generated and Nakayama gives equality. Taking
the trace-zero part changes only a base scalar.

### G. Does one fixed boundary-adapted `theta` exhaust the unit search?

No. Every section `theta+H eta` has the same class in `E/H E`. A hypothetical
unit section may have another primitive boundary residue class. The finite-prime
adaptation theorem proves only that

```text
R_H={bar(theta) in E/H E : bar(theta) is primitive at every p|H}
```

is nonempty; it does not identify a class containing a unit section.

Conversely, every unit section is primitive at every boundary prime and hence
lies in exactly one class from `R_H`. For any chosen class and lift `theta`, all
sections in that class are exactly `theta+H eta`. The corrected packet therefore
has an exact union over classes, while a fixed `theta` is one class only.

### H. Is the affine-pencil expansion exact within its scope?

Yes. Polarization gives

```text
Phi(theta+H T eta)
 = D+H C T+H^2 B_2 T^2+H^3 A T^3.
```

Modulo every boundary prime this is `D=Phi(theta)`, a unit. Every factor created
in that pencil is therefore nonboundary. Failure of one pencil or one class does
not exclude a unit section in another class.

The corrected verifier treats each coefficient as a polynomial in `H`, divides
by `H^i`, and requires zero remainder. It also checks that adding `1` to the
coefficient is rejected. Thus the test now fails under the exact mutation that
made the earlier rational-cancellation check vacuous.

### I. Does source étaleness eliminate scalar sheet collisions?

No. On the split étale locus,

```text
Phi(s)=product_{i<j}(z_j-z_i).
```

One factor can vanish while the three source points remain distinct in `(x,y)`.
The logarithmic derivative records relative scalar velocities and does not turn
that collision into ramification.

### J. Was translation stability silently assumed?

No. The packet proves only that no nonconstant divisor can be stable under both
`partial_P` and `partial_Q`. It explicitly observes that `(Phi(s))` is not known
to be stable because differentiating changes `s`; the minimal-degree
translation-ideal argument is not misapplied.

### K. Does the countermodel ladder stop at stage 5?

Yes, for the specified source open. If the relative different misses the
displayed `A^2`, then `Omega_{C[x,y]/C[P,Q]}=0`; the square Jacobian presentation
makes `J(P,Q)` a unit of `C[x,y]`, hence a nonzero constant. The function-field
degree remains three, so Orevkov contradicts it. An arbitrary abstract open
`A^2` not carrying the specified restricted morphism would not suffice.

### L. Is the broader prime-degree shortcut safely separated?

Yes. The packet does not rely on arXiv:2407.13795. The cited MathOverflow answer
constructs a quadratic example and does not prove a degree-two classification.
The packet's cubic rare-property model rejects that implication only; it is not
used as a Keller or no-unit counterexample.

## 3. Exact checks

The corrected candidate was checked with Python 3.12 and SymPy 1.14.0:

```text
python3 research/issues/rank-three-boundary-cube-unit/verify_all.py
```

Output:

```text
binary cubic and boundary-fiber verification: PASS
index, Fitting, and discriminant-square verification: PASS
boundary-adapted affine-family verification: PASS
countermodel-ladder verification: PASS
prime-degree literature-audit controls: PASS
rank-three boundary-cube packet verification: PASS
```

Exact-head repository workflow run `30190603534` also passed at the reviewed
revision. The scripts verify identities and bounded falsification controls. They
do not prove Orevkov's theorem or mathematical truth beyond their stated scope.

## 4. Risks and limits

1. Orevkov's proof is full-text audited but not independently reproved; the
   terminal remains `literature_bound`.
2. Boundary adaptation consumes mutable predecessor claim `CLM-029`; the
   Orevkov terminal does not.
3. The local cubic trichotomy is geometric after strict henselization, not one
   global simultaneous `GL_2(B)` normalization.
4. One chosen primitive class in `E/H E` is not canonical or exhaustive.
5. No unit-index section is constructed and no method for degree four or higher
   follows.
6. The countermodel result is terminal only at the source-étale wall; it is not a
   classification below that wall.
7. The prime-degree criticism is limited to the identified first-case inference.
8. This local adversarial review is by the constructor and does not constitute
   independent scientific acceptance.

## 5. Disposition

Accepted at mutable packet scope:

- `R3BC-01`: full-text-audited application of Orevkov at `literature_bound`;
- `R3BC-02`: geometric boundary-cubic trichotomy;
- `R3BC-03`: exact boundary-primitive residue-class decomposition and exact
  affine-pencil identity within each chosen class;
- `R3BC-04`: differential movement without fixed-value stability;
- `R3BC-05`: countermodel ladder terminal at source étaleness;
- `R3BC-07`: packet-local rejection of the identified prime-degree shortcut.

Blocked:

- promotion to internally proved or independently reviewed status;
- any assertion that one concrete unit-index section was constructed;
- any assertion that the first adapted class exhausts all candidates;
- any inference for prime degrees other than three;
- any proof of `JC_2`.

Final result:

```text
ACCEPT_LITERATURE_BOUND_RANK_THREE_TERMINAL_AND_SCOPED_INTERNAL_REFINEMENTS;
BLOCK_CONSTRUCTIVE_UNIT_SECTION_AND_BROADER_PROMOTION.
```
