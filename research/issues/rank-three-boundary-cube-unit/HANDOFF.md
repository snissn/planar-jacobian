# Handoff — Rank-Three Keller Terminal and Boundary-Cubic Refinement

```text
role: research-worker
task_issue: #3
owned_path: research/issues/rank-three-boundary-cube-unit/
base_main: 652a5e252626fa5816445651245e8a8946cee53e
scientific_candidate: f85f9e1e7143bc36859543c3d5520d06fe99cb17
review_mode: local-adversarial-review
reviewed_revision: f85f9e1e7143bc36859543c3d5520d06fe99cb17
integration_state: integration-ready after exact-head CI
merge_authority: none in this parallel round
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

This is proposed `R3BC-01` at `literature_bound` scope. The English primary full
text was audited at its definition of multiplicity, Theorem 1.1, proof
architecture, and terminal degree-three cases. The packet does not reproduce
Orevkov's proof and does not construct a section with `Phi(s) in C*`.

## 2. Conditional internal refinements

Retaining a finite locally free normal rank-three algebra only as a conditional
algebraic model, the packet proves:

1. **Boundary-cubic trichotomy (`R3BC-02`).** Geometrically at a height-one
   prime, the index cubic is

   ```text
   L1 L2 L3,   L M^2,   or   L^3
   ```

   for ramification partitions `1+1+1`, `2+1`, or `3`. A cube occurs only at
   total ramification.

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

5. **Countermodel terminal (`R3BC-05`).** The integrated no-unit model reaches
   finite-flat/normal/connected/rational/open-`A2`, but fails source étaleness.
   Adding boundary-only different support on the specified source open would
   produce a degree-three Keller map and is impossible by `R3BC-01`.

6. **Literature falsification control (`R3BC-07`).** A cubic rare-property model
   rejects the degree-two classification used in the first case of
   arXiv:2407.13795v1. This is not needed for the Orevkov terminal and supports
   no theorem beyond that narrow audit.

## 3. Proposed global claim deltas

Allocate final global IDs dynamically.

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
statement: In a finite locally free normal rank-three algebra over a
characteristic-zero DVR, the geometric trace-zero binary index cubic is
GL2-equivalent to L1L2L3, LM^2, or L^3 according to ramification partition
1+1+1, 2+1, or 3.
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
status: candidate_proved
statement: The issue #3 no-unit model satisfies stages 1-4 of the Keller-near
ladder, while adding different support only outside the specified open A2 would
make the restricted degree-three polynomial map Keller and is impossible by
R3BC-01.
dependencies: CLM-058, CLM-066, R3BC-01
```

Keep `R3BC-07` packet-local unless separately adjudicated.

## 4. Proposed graph, leaf, and issue disposition

After independent source verification and serialized integration, consider:

1. add a terminal rank-three exclusion node supported by `R3BC-01`;
2. dispose `OPEN-KELLER-INDEX-UNIT` / L14 at the **rank-three Keller scope**,
   because the simultaneous hypotheses are inconsistent;
3. retire `CLM-059` as a rank-three construction target, explicitly noting that
   no unit section was constructed;
4. preserve `CLM-062`–`CLM-066` as conditional tools and corrections;
5. preserve `R3BC-03` as a residue-class decomposition plus restricted
   moving-divisor identity, not as an exhaustive fixed-class reduction;
6. close issue #3 only after merge and exact-main verification;
7. create no terminal edge to `JC_2`.

## 5. Shared surfaces requested, not edited

This worker changed no shared surface. Serialized integration may update:

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
research/leaf-packets/L14-keller-index-form-unit.md
research/tracks/c-monogenicity-index-divisor.md
research/tracks/monogenicity-index-divisor.md
```

Generated views must be regenerated by the integration maintainer. No workflow
change is requested.

## 6. Review and validation evidence

Pinned local adversarial review:

```text
reviewed_revision: f85f9e1e7143bc36859543c3d5520d06fe99cb17
disposition: ACCEPT_LITERATURE_BOUND_RANK_THREE_TERMINAL_AND_SCOPED_INTERNAL_REFINEMENTS; BLOCK_CONSTRUCTIVE_UNIT_SECTION_AND_BROADER_PROMOTION
```

The reviewed revision includes the repaired exact `H`-adic divisibility check:
polynomial division must have zero remainder, and nondivisible `+1` mutations
must be rejected.

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
python3 -m unittest discover -s scripts/tests -p 'test_*.py'
python3 scripts/validate_integration_contract.py
python3 scripts/render_views.py --check
python3 scripts/validate_repository.py
python3 scripts/frontier.py
python3 research/issues/issue-3-unramified-index/verify_index_models.py
python3 research/issues/rank-three-index-form-unit/verify_all.py
```

GitHub Actions run `30190603534` passed these checks at the reviewed candidate.
Passing CI is engineering evidence only and does not strengthen mathematical
status.

## 7. Integration boundary

This worker has no merge authority. The non-draft PR must remain open. It is not
on `main` until an integration maintainer re-resolves live `main`, allocates
final IDs, synchronizes shared surfaces, reruns exact-candidate validation,
merges, and verifies exact `main`.
