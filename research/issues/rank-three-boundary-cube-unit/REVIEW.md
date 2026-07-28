# Renewed Local Adversarial Review

```text
review_mode: local-adversarial-review
reviewed_revision: 3a0ba94eecd723295a4148814300242dba8ddae1
reviewed_scope: R3BC-01 through R3BC-05, packet-local R3BC-07, all issue-owned proof files, and all exact scripts
constructor_independence: none; constructor and reviewer are the same assistant
disposition: ACCEPT_FOR_WORKER_HANDOFF_AT_DECLARED_STATUSES; BLOCK_BROADER_PROMOTION
```

## 1. Pinned candidate and review boundary

This review is bound only to

```text
3a0ba94eecd723295a4148814300242dba8ddae1
```

on base

```text
def93d34174cb87a1d59573bcae395a79b635040.
```

The candidate contains only
`research/issues/rank-three-boundary-cube-unit/`. The proof, scripts, proposed
claim statements, and scientific status assignments were not edited during the
review pass. The review record and transport metadata are added afterward.

The reviewed files are:

```text
BINARY_CUBIC_GEOMETRY.md
BOUNDARY_VALUATIONS.md
COUNTERMODEL_LADDER.md
DIFFERENTIAL_CONTROL.md
FOUNDATIONS.md
HANDOFF.md
INTEGRATION.json
LITERATURE_AUDIT.md
README.md
REVIEW.md
UNIT_VALUE_SEARCH.md
verify_all.py
verify_binary_cubic.py
verify_boundary_family.py
verify_countermodel_ladder.py
verify_index_and_fitting.py
verify_prime_degree_audit.py
```

The candidate consumes existing claims `CLM-001`, `CLM-002`, `CLM-010`,
`CLM-012`, `CLM-029`, `CLM-058`, and `CLM-062` through `CLM-066` only at their
current canonical scopes. It proposes issue-local labels `R3BC-01` through
`R3BC-05`; it allocates no global claim identifier.

Because the constructor and reviewer are the same assistant, this is not an
independent review and creates no `reviewed_scoped` authority.

## 2. Primary-source audit

The load-bearing external source was reopened and read at the relevant points:

- S. Yu. Orevkov, “On three-sheeted polynomial mappings of `C^2`,”
  *Mathematics of the USSR-Izvestiya* **29**:3 (1987), 587–596,
  DOI `10.1070/IM1987v029n03ABEH000984`;
- primary record: <https://www.mathnet.ru/eng/im1571>;
- English primary PDF:
  <https://www.mathnet.ru/php/getFT.phtml?jrnid=im&option_lang=eng&paperid=1571&what=fullteng>.

The review verified:

1. Section 1 begins with a polynomial map `C^2 -> C^2` with nonzero constant
   Jacobian.
2. The paper defines multiplicity as the number of preimages of a generic
   target point.
3. Theorem 1.1 excludes multiplicity two or three.
4. The closing proof assumes multiplicity three, treats the three cases
   supplied by Lemma 4.2, excludes the first two by simply connected
   complements, and excludes the third by the branch-order contradiction after
   the Abhyankar–Moh rectification.

The packet imports only the multiplicity-three exclusion. It does not import
an all-prime-degree theorem and does not claim to reproduce Orevkov's proof.
`R3BC-01` therefore remains `literature_bound`.

## 3. Recomputed load-bearing steps

### A. Function-field degree and generic sheet number

The review recomputed the bridge independently:

1. algebraicity of `x,y` over `K=C(P,Q)` lets one invert one nonzero
   `h in B=C[P,Q]` so that `A_h=B_h[x,y]` is finite over `B_h`;
2. the nonzero constant Jacobian gives `Omega_{A/B}=0`;
3. after shrinking to the finite-flat locus, `A_h/B_h` is finite étale of rank
   `[L:K]`;
4. a geometric generic fiber therefore has `[L:K]` reduced points.

Thus field degree three is exactly Orevkov's multiplicity-three hypothesis.
No global properness assumption is introduced.

### B. Rank-three special-fiber determinants

After the declared strict-henselian/geometric base change, the review directly
recomputed

```text
k x k x k:                         (z2-z1)(z3-z1)(z3-z2),
(k[epsilon]/epsilon^2) x k:        b(c-a)^2,
k[epsilon]/epsilon^3:              b^3.
```

On the trace-zero plane these yield the three geometric binary-cubic forms

```text
L1 L2 L3,   L M^2,   L^3.
```

The cube occurs only for total ramification. The packet does not claim a
simultaneous global `GL_2(B)` form.

### C. Semilocal boundary adaptation and residue classes

The review checked that the predecessor's `CLM-029` applies to the whole
semilocal algebra over each height-one base prime. If `H` is the square-free
product of boundary primes and `theta` is primitive at all of them, then

```text
theta+H T eta == theta mod p
```

for every `p|H`. The special-fiber generator criterion and Nakayama therefore
preserve generation at every boundary prime.

The polarization identity was recomputed:

```text
Phi(theta+H T eta)
 = D+H C T+H^2 B_2 T^2+H^3 A T^3.
```

The review also checked the scope correction: one chosen `theta` represents
only one class in `E/H E`. The full conditional search is the union over all
boundary-primitive classes `R_H`; finite-prime adaptation proves nonemptiness,
not a canonical class containing a unit-valued section.

### D. Differential collision behavior

On a split étale chart,

```text
D log Phi(s)
 = sum_{i<j} D(z_j-z_i)/(z_j-z_i).
```

The review mutated a collision factor in two directions:

```text
f=P,  D=partial_P:  D(f)/f=1/P       (transverse pole),
f=P,  D=partial_Q:  D(f)/f=0         (tangent; no pole forced).
```

This confirms the corrected statement. A pole requires nonzero relative
sheet velocity modulo the collision divisor; source étaleness alone does not
force that transversality.

The minimal-degree proof that no nonconstant divisor is stable under both
target translations is valid. The packet does not infer that a fixed-section
ideal is stable under either translation.

### E. Countermodel source-open wall

The review retained the exact factorization

```text
U=Spec(C[x,y]) -> Y=Spec(O) -> Spec(C[P,Q]).
```

If the relative different misses this specified `U`, restriction gives
`Omega_{C[x,y]/C[P,Q]}=0`. The square Jacobian presentation then makes
`J(P,Q)` a unit of `C[x,y]`, hence a nonzero constant. Function-field degree
three invokes `R3BC-01`. Because the terminal step imports Orevkov,
`R3BC-05` is correctly `literature_bound`, not `candidate_proved`.

An arbitrary abstract open `A^2` in a rational surface does not satisfy this
argument and is not used.

### F. Rare-property falsification control

For

```text
L=C(s,v),
R=C(s^3,v),
x=s+v,
y=s+2v,
```

the inverse coordinate change `s=2x-y`, `v=y-x` and degree-three extension
were checked. The root multiset of `(t+1)^i(t+2)^j` cannot be stable under a
nontrivial cube-root rotation for `(i,j)!=(0,0)`, so every such monomial lies
outside `R` and generates the prime-degree extension. This rejects only the
identified degree-two classification shortcut. `R3BC-07` remains packet-local
and is not a Keller theorem.

## 4. Mutation and edge-case tests

The review exercised the following controls:

1. exact independent determinant recomputation for all three rank-three
   geometric special fibers;
2. exact positive and negative `H^i` divisibility tests for the affine-family
   coefficients;
3. transverse versus tangent logarithmic-derivative mutations;
4. the integrated no-unit countermodel and its nonconstant source Jacobian;
5. fixed-first-coordinate constant-Jacobian repairs, which reduce to a
   triangular degree-one map;
6. bounded cyclotomic and finite-field mutations for the rare-property model;
7. smoothness checks for all three constant-level geometric fiber forms;
8. exact Fitting determinant and discriminant-square identities;
9. exact predecessor issue #3 countermodel and rank-three regression suites;
10. an exact diff check confirming that the candidate proof remained unchanged
    throughout review.

All controls passed.

## 5. Exact commands and results

The host default `python3` is Python 3.10.12. The packet guard rejected it as
expected:

```text
Python 3.12 or newer is required; found 3.10.12
```

The canonical review environment was Python 3.12.10 with exact SymPy 1.14.0,
provided by

```bash
uv run --python 3.12 --with sympy==1.14.0 -- bash -c '...'
```

Within that environment the following exact commands passed:

```bash
python3 research/issues/rank-three-boundary-cube-unit/verify_all.py
python3 research/issues/issue-3-unramified-index/verify_index_models.py
python3 research/issues/rank-three-index-form-unit/verify_all.py
python3 -m compileall -q scripts research/issues
python3 scripts/render_views.py --check
python3 scripts/validate_repository.py
python3 scripts/validate_integration_contract.py
python3 -m unittest discover -s scripts/tests -p 'test_*.py'
python3 scripts/frontier.py
git diff --check
```

Recorded results:

```text
rank-three boundary-cube packet verification: PASS
all exact symbolic checks: PASS
rank-three packet verification: PASS
generated views: PASS (6 files)
repository structure: PASS
integration contract: PASS (7 manifests)
unit tests: PASS (20 tests)
frontier: ROOT-JC2 remains blocked; L14 remains open on candidate main
git diff --check: PASS
```

`validate_repository.py` emitted only the two existing metadata-only archive
warnings for `conversation-a` and `conversation-b`. Mathematical truth is not
evaluated by these validators.

## 6. Status-by-claim disposition

- `R3BC-01`: `ACCEPT` as a primary-full-text-audited,
  `literature_bound` application of Orevkov.
- `R3BC-02`: `ACCEPT` at `candidate_proved` scope for the geometric local
  rank-three cubic trichotomy.
- `R3BC-03`: `ACCEPT` at `candidate_proved` scope for the residue-class
  decomposition and exact within-class affine-family identity.
- `R3BC-04`: `ACCEPT` at `candidate_proved` scope for movement without
  fixed-value stability, including the tangent/transverse correction.
- `R3BC-05`: `ACCEPT` as `literature_bound` at the specified source-open wall.
- `R3BC-07`: `ACCEPT` only as a packet-local falsification control against one
  identified external shortcut.

## 7. Unresolved risks and explicit nonclaims

1. Orevkov's proof is audited, not independently reproved.
2. The conditional boundary adaptation consumes mutable predecessor claim
   `CLM-029`.
3. The cubic trichotomy is geometric after base change, not a global normal
   form.
4. No preferred boundary residue class is constructed.
5. No unit-index section is constructed.
6. No degree-four-or-higher case follows.
7. The countermodel ladder is terminal only at the specified source-open wall.
8. The rare-property criticism does not adjudicate every claim or later
   revision of the cited preprint.
9. This same-constructor review is not independent and creates no freeze or
   `reviewed_scoped` status.
10. No statement proves `JC_2`.

## 8. Final review result

```text
ACCEPT_FOR_WORKER_HANDOFF_AT_DECLARED_STATUSES:
  R3BC-01 and R3BC-05 are literature_bound;
  R3BC-02 through R3BC-04 are candidate_proved;
  R3BC-07 remains packet-local.

BLOCK:
  internally-proved Orevkov status;
  constructive unit-index status;
  any degree-four-or-higher inference;
  independent or reviewed_scoped promotion;
  any terminal edge to JC_2.
```

## 9. Post-review non-scientific corrections

After this review was recorded, Codex review of PR #54 found that the
provenance header in `FOUNDATIONS.md` still named the superseded construction
base `652a5e252626fa5816445651245e8a8946cee53e`. The header was corrected to
the actual base
`def93d34174cb87a1d59573bcae395a79b635040`, consistently with `README.md`,
`HANDOFF.md`, `INTEGRATION.json`, and the commit graph.

This post-review edit changes provenance metadata only. It changes no
hypothesis, statement, proof step, computation, status assignment, dependency,
or nonclaim, so the scoped review of scientific candidate
`3a0ba94eecd723295a4148814300242dba8ddae1` remains applicable under the
repository's editorial/transport renewal rule.

CodeRabbit then identified two documentation inconsistencies and one
equivalence-preserving SymPy cleanup. The README and handoff now show the
canonical pinned Python 3.12 / SymPy 1.14.0 invocation and identify
`verify_all.py` as the guarded packet entry point. The boundary-family
congruence check now computes the same zero remainder directly on expressions
rather than converting through `Poly` and back. Both forms return zero under
the pinned environment; the latter removes representation-dependent return
typing.

These changes alter neither the asserted identity nor any mathematical claim.
The complete pinned suite was rerun afterward. No scientific review renewal is
required for these documented editorial and exact-equivalence changes.
