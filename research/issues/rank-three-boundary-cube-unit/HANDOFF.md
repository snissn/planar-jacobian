# Handoff — Rank-Three Keller Terminal and Boundary-Cubic Refinement

```text
role: research-worker
task_issue: #3
owned_path: research/issues/rank-three-boundary-cube-unit/
base_main: def93d34174cb87a1d59573bcae395a79b635040
scientific_candidate: PENDING_CORRECTED_CANDIDATE
review_mode: none
reviewed_revision: null
integration_state: construction
merge_authority: none; worker hands off a non-draft integration-ready PR
```

## 1. Exact result

For

```text
F=(P,Q): C2 -> C2,
J(P,Q) in C*,
K=C(P,Q),
L=C(x,y),
```

field degree `[L:K]=3` makes `F` generically three-sheeted. Orevkov's 1987
primary theorem states that a three-sheeted polynomial map `C2 -> C2` cannot
have constant Jacobian. Therefore no planar Keller map, and hence no actual
Keller normalization, has rank three.

This is packet label `R3BC-01` at `literature_bound` scope. The English primary
full text was audited at its definition of multiplicity, Theorem 1.1, proof
architecture, and terminal degree-three cases. The packet does not reproduce
Orevkov's proof and does not construct a section with `Phi(s) in C*`. A future
integration maintainer must allocate the next available global claim identifier
against then-current `main`.

## 2. Conditional internal refinements

Retaining a finite locally free normal rank-three algebra only as a conditional
algebraic model, the packet proves:

1. **Boundary-cubic trichotomy (`R3BC-02`).** After strict henselization of a
   height-one DVR and passage to the geometric special fiber, the trace-zero
   index cubic is

   ```text
   L1 L2 L3,   L M^2,   or   L^3
   ```

   for ramification partitions `1+1+1`, `2+1`, or `3`. A cube occurs only at
   total ramification. This is not one simultaneous global `GL_2(B)` form.

2. **Boundary-stable class (`R3BC-03`).** If `H` is the square-free product of
   target boundary primes and `theta` is primitive at all of them, then

   ```text
   s_T=theta+H T eta
   ```

   remains primitive at every boundary prime and

   ```text
   Phi(s_T)=D+H C T+H^2 B_2 T^2+H^3 A T^3.
   ```

   Every factor created in that pencil is a nonboundary scalar collision.

3. **Exact residue-class decomposition.** Let

   ```text
   R_H={bar(theta) in E/H E : bar(theta) is primitive at every p|H}.
   ```

   Finite-prime adaptation proves `R_H` is nonempty. For a fixed class and lift
   `theta`, all sections in that class are exactly `theta+H E`. The unrestricted
   conditional unit problem is therefore the union over all classes in `R_H`.
   One initially chosen `theta` is not canonical and need not contain a
   hypothetical unit-index section.

4. **Differential limitation (`R3BC-04`).** No nonconstant divisor is stable
   under both target translations, but a fixed-section value ideal is not shown
   translation-stable. Canonical derivations move scalar collisions; they do not
   eliminate them.

5. **Countermodel terminal (`R3BC-05`, `literature_bound`).** The integrated
   no-unit model reaches
   finite-flat/normal/connected/rational/open-`A2`, but fails source étaleness.
   In the audited finite-normalization factorization, the relevant `A2` is the
   specified displayed source open `U=Spec(C[x,y])`. If the relative different
   has no support on `U`, then `Omega_{C[x,y]/C[P,Q]}=0`, so the induced
   degree-three polynomial map has constant nonzero Jacobian and is excluded by
   `R3BC-01`. An arbitrary abstract open `A2` is insufficient.

6. **Literature falsification control (`R3BC-07`).** A cubic rare-property model
   rejects the degree-two classification used in the first case of
   arXiv:2407.13795v1. This is not needed for the Orevkov terminal and supports
   no theorem beyond that narrow audit. It remains packet-local and is excluded
   from proposed global synchronization.

## 3. Proposed global claim deltas

This worker proposes the following issue-local labels. It does not reserve
global identifiers. The integration maintainer must allocate identifiers
dynamically and recompute every dependency against the latest `main`.

### `R3BC-01` — rank-three terminal

```text
status: literature_bound
statement: A planar polynomial Keller map cannot have function-field degree
three. Degree three is generic multiplicity three, while Orevkov's primary 1987
theorem excludes constant Jacobian for a three-sheeted polynomial map C2 to C2.
dependencies: CLM-001, CLM-002
source: Orevkov, Math. USSR-Izv. 29 (1987), DOI 10.1070/IM1987v029n03ABEH000984
nonclaims: no constructive unit-index section, no higher-degree result, no JC_2
```

### `R3BC-02` — boundary trichotomy

```text
status: candidate_proved
statement: After strict henselization and passage to the geometric special
fiber, the trace-zero binary index cubic of a finite locally free normal
rank-three algebra over a characteristic-zero DVR is GL2-equivalent to L1L2L3,
LM^2, or L^3 according to ramification partition 1+1+1, 2+1, or 3.
dependencies: CLM-062
```

### `R3BC-03` — boundary classes and pencils

```text
status: candidate_proved
statement: Boundary-primitive sections decompose into classes in E/H E. Within
any chosen class theta+H E, every affine pencil theta+HT eta remains primitive
at all boundary primes and has index D+HCT+H^2B_2T^2+H^3AT^3; every factor
created in the pencil is a nonboundary scalar collision. Finite-prime adaptation
proves at least one primitive class exists but does not select a class containing
a unit-index section.
dependencies: CLM-029, CLM-062, CLM-064, CLM-066
```

### `R3BC-04` — differential limitation

```text
status: candidate_proved
statement: No nonconstant fixed divisor in C[P,Q] is invariant under both target
translations, but the Keller differential congruence does not make a named
fixed-section index ideal translation-stable; moving scalar collisions are not
ramification.
dependencies: CLM-010, CLM-012, CLM-065, CLM-066
```

### `R3BC-05` — countermodel ladder terminal

```text
status: literature_bound
statement: Under the audited finite-normalization/source-open factorization, the
issue #3 no-unit countermodel reaches the finite-flat, normal, connected,
rational, open-A2 stages; if the relative different has no support on the
specified displayed source open U=Spec(C[x,y]), then Omega_{C[x,y]/C[P,Q]}=0,
the induced degree-three polynomial map has constant nonzero Jacobian, and
Orevkov excludes it.
dependencies: CLM-058, CLM-066, R3BC-01
```

Keep `R3BC-07` packet-local and excluded from global synchronization unless it is
separately adjudicated.

## 4. Graph, leaf, and issue disposition

Proposed for a future serialized integration after renewed review:

1. add `TERM-RANK-THREE-EXCLUSION`, supported by the dynamically allocated
   global form of `R3BC-01` and by the literature-control surface;
2. dispose `OPEN-KELLER-INDEX-UNIT` / L14 at the **rank-three Keller scope**,
   because the simultaneous hypotheses are inconsistent;
3. retire `CLM-059` as a rank-three construction target, explicitly noting that
   no unit section was constructed;
4. preserve `CLM-062`–`CLM-066` as conditional tools and corrections;
5. preserve the dynamically allocated form of `R3BC-03` as a residue-class
   decomposition plus restricted
   moving-divisor identity, not as an exhaustive fixed-class reduction;
6. close issue #3 only after merge and exact-main verification;
7. create no terminal edge to `JC_2`.

## 5. Proposed shared deltas

The worker changes none of these files. A future integration maintainer should
recompute and synchronize, on then-current `main`:

```text
README.md
STATUS.md
research/claim_ledger.json
research/CLAIM_LEDGER.md
research/proof_graph.json
research/PROOF_GRAPH.md
research/work_queue.json
research/WORK_QUEUE.md
research/ISSUE_INDEX.md
research/PROGRAM.md
research/leaf-packets/L14-keller-index-form-unit.md
research/tracks/c-monogenicity-index-divisor.md
research/tracks/monogenicity-index-divisor.md
```

Generated views are regenerated by the integration maintainer. The guarded
packet verifier is already conditionally covered by the current-main workflow
from governance PR #53; this worker does not edit that workflow.

## 6. Review and validation evidence

Renewed local adversarial review is pending the corrected candidate:

```text
reviewed_revision: null
disposition: PENDING
```

The renewed review must pin the corrected candidate, re-audit Orevkov's primary
source, recompute all load-bearing internal steps, test mutations, and record
the full required command set. Shared constructor/reviewer identity is a local
adversarial review, never an independent review.

Packet-local command:

```bash
python3 research/issues/rank-three-boundary-cube-unit/verify_all.py
```

Expected final line:

```text
rank-three boundary-cube packet verification: PASS
```

Exact-head repository checks:

```bash
python3 -m compileall -q scripts research/issues
python3 scripts/render_views.py --check
python3 scripts/validate_repository.py
python3 scripts/validate_integration_contract.py
python3 -m unittest discover -s scripts/tests -p 'test_*.py'
python3 scripts/frontier.py
python3 research/issues/issue-3-unramified-index/verify_index_models.py
python3 research/issues/rank-three-index-form-unit/verify_all.py
git diff --check
```

The final PR-head workflow result is recorded in the PR body. Passing CI is
engineering evidence only and does not strengthen mathematical status.

## 7. Integration boundary

The research worker leaves one coherent non-draft PR containing only the owned
issue path. It does not merge or edit shared scientific surfaces. A distinct
integration-maintainer run must re-resolve `main`, transplant only this packet,
allocate global identifiers, recompute proposed shared deltas, obtain review and
CI, merge serially, and complete the live-main receipt.
