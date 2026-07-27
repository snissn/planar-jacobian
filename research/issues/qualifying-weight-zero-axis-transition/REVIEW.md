# Local-Adversarial Review

## Review binding

```text
review_mode: local-adversarial-review
reviewer_identity: same assistant as constructor
candidate_revision: 7253c25b35847302ee44d697a98deedc1c70c819
candidate_tree: 9eb1632f736af9c62f437cdf732f4e6b48608113
candidate_aggregate_sha256: 4c1a66b7aed1a0b395745906b5484d099be1f3c17e5b067dfd3839cafa569fd3
review_disposition: ACCEPT_SCOPED
promotion_disposition: BLOCK_WITHOUT_INDEPENDENT_REVIEW
```

This is not an independent review. The candidate proof files were not modified
during review. Review scripts and transport metadata were added after the
candidate was pinned.

## Exact reviewed statement

For a normalized planar Keller pair and a primitive positive weight of actual
defect six, complete top common-power exponents `(2,3)` or `(3,2)` are
incompatible with the complete Rees equations. Therefore the issue #41 global
minimal-counterexample configuration has no pair-changing zero/axis or
nonshared-component transition adjacent to such a face.

The review does not accept a general defect-six theorem or any stronger global
termination claim.

## Reviewed files

The pinned candidate contains exactly:

- `README.md`;
- `DEFINITIONS.md`;
- `TRANSITION_NORMAL_FORMS.md`;
- `DEFECT6_REES_SYSTEM.md`;
- `CASE_TABLE.md`;
- `ANALYTIC_CLASSIFICATION.md`;
- `COUNTERMODELS.md`;
- `defect6_transition_checker.py`.

## Dependency audit

The review checked the candidate against the exact scientific dependencies:

- defect-at-most-four freeze at reviewed candidate
  `96fc7ec34bd3b685a0edeae7ecd4404abab7e2f1`;
- defect-five independent-review head
  `c31fa0361daabb06c08148ea3941e281433869f6`;
- qualifying-weight predecessor head
  `de43b37c9ab26d6a58801906fcabfd1d5f083344`;
- non-toric one-boundary warning head
  `fd8af6398bbed85e6e34f886ff1d1a1c395ce296`.

The local theorem itself uses only the Rees identity, constant-bracket
classification, weighted common powers, and characteristic-zero algebra. The
defect-four/five results enter only in the global minimal-counterexample
corollary. The non-toric packet is used only to prevent an unjustified
normalization-boundary inference.

## Independent reconstruction performed in review

The reviewer-owned
[`review_defect6_transition.py`](review_defect6_transition.py) imports no code
from the construction checker. It independently performed the following.

1. Reproved the analytic bound `rho<=6` from the selected scalar bracket and a
   monomial of `H`.
2. Enumerated the integer constraints for both exponent orders, all seven
   positions `a+b=6`, both source-weight assignments, and all primitive source
   orders. The resulting set was compared to an explicit 16-row expected set.
3. Rebuilt all weighted-homogeneous layers for the four determinant-one normal
   forms with a separate support generator.
4. Re-expanded every coefficient of `S_0,...,S_6` with a separate Jacobian
   implementation.
5. Saturated each complete ideal by `A B c` and obtained the unit ideal.
6. Saturated the four decisive subideals, independently confirming the short
   human contradictions.
7. Tested nine semantic corruptions independently of the construction mutation
   harness.

Observed output:

```text
independent defect-six transition review: PASS
raw orientations: 16
canonical cases: 4
mutations: 9
review assertions: 33
independent reconstruction finds no defect-six {2,3}/{3,2} system
```

## Adversarial questions and findings

### Did the proof stop at `S_0` or `S_1`?

No. All seven stairs are generated and recorded. Normal forms I and IV retain
simultaneous constant-bracket contributions in `S_6`:

```text
c-v ell=1,
c-z ell=1.
```

The contradiction happens earlier, but the constant layer is not dropped.

### Was a scalar silently normalized to one?

No. The determinant-one source normalization yields `(x,c y)`. The variable
`c` is saturated as nonzero and remains in every applicable equation. Only the
complete `S_6` equation can constrain its value.

### Were target or source determinants changed?

No. The only orientation maps are the signed determinant-one source and target
swaps. The scalar-retaining graded source maps each have determinant one. The
review recalculated their determinants and layer preservation.

### Are all component/source orders covered?

Yes. The construction checker builds and saturates all 16 raw systems directly.
The analytic table and reviewer enumeration reproduce the same 16 rows. The
four normal forms are only a human-readable quotient under declared maps.

### Could a missing semigroup degree hide a variable?

No. Every degree is generated from `p u+q v=d`. Unsupported layers are literal
zero. Normal form III deliberately contains multiple zero layers and is tested
without index compression.

### Could two different Jacobian monomials cancel?

No. Equations are extracted from `Poly(...,x,y)` after exact expansion. Only
identical exponent vectors are combined. The shared wall in normal form I, for
example, has independent `x^5` and `xy` coefficients.

### Could an origin transition have been omitted?

No. The exact orientation table shows every weight-`rho` monomial set is a
singleton `{x^r}` or `{y^r}` with `r>0`. The top common-root polygon is a
nonzero axis vertex, never the origin and never an edge ending at the origin.

### Could a deeper layer create an earlier adjacent wall?

No in these four normal forms. The review enumerated every lattice point below
the anchor degree. Every off-axis point capable of meeting the anchor occurs at
layer index at most six; all are represented in the checker. The required
`c y` term ensures an incident wall if optional earlier edge coefficients
vanish.

### Was a local shear confused with global descent?

No shear is used in the contradiction. The packet explicitly separates the two
notions. The global corollary instead uses nonexistence of the anchor and,
independently, the fact that every first adjacent wall has actual defect at most
five.

## Mutation matrix

| mutation | expected rejection | construction | reviewer |
|---|---|---:|---:|
| delete required selected monomial | support/constant-bracket failure | PASS | PASS |
| add forbidden top monomial | top support mismatch | PASS | PASS |
| use wrong `{2,3}` weighted degree | coprime degree-ratio mismatch | PASS | PASS |
| drop `S_6=1` | incomplete staircase | PASS | PASS |
| falsely declare origin sharing | exponent-vector mismatch | PASS | PASS |
| normalize away `c` | uncompensated scalar loss | PASS | PASS |
| call partial top cancellation descent | old top degree remains | PASS | PASS |
| omit a zero layer | Rees index length changes | PASS | PASS |
| cancel different exponent vectors | coefficient collection mismatch | n/a | PASS |

## Review verdict

**ACCEPT_SCOPED** for the exact theorem and empty transition classification at
candidate `7253c25b35847302ee44d697a98deedc1c70c819`.

The proof is short enough to stand independently of the checker: a proved
`rho<=6` bound yields four determinant-one normal forms, and their explicit
coefficient equations contradict `A B c!=0`. The exact programs provide
orientation, support, saturation, and mutation regression evidence.

## Remaining risks and blockers

- This same-session review is not independent and cannot promote the theorem to
  frozen or `reviewed_scoped` canonical authority.
- The scientific review was pinned before transport. The unchanged owned-path
  candidate was later transplanted onto live
  `main@f2399d8634521edf220d412a3e14d42eb56d89be`; this transport-only metadata
  refresh does not alter the reviewed mathematics.
- Exact-head Actions status must be read from the resulting pull request before
  integration; green CI is engineering evidence only.
- The theorem treats only actual defect six and coprime pair `{2,3}`. The next
  common-power sizes, higher defects, and the non-toric no-escape bridge remain
  open.
