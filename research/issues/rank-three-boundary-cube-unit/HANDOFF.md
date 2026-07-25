# Handoff — Rank-Three Keller Terminal and Boundary-Cubic Refinement

```text
role: research-worker
task_issue: #3
owned_path: research/issues/rank-three-boundary-cube-unit/
base_main: 652a5e252626fa5816445651245e8a8946cee53e
scientific_candidate: c281ecd845fe63e88b47ae16f99135325a2f988f
review_mode: local-adversarial-review
reviewed_revision: c281ecd845fe63e88b47ae16f99135325a2f988f
integration_state: integration-ready after exact-head CI
merge_authority: none in this parallel round
```

## 1. Exact result

The actual rank-three Keller case is excluded by a primary-source theorem rather
than solved by constructing a global primitive section.

Let

```text
F=(P,Q): C2 -> C2,
J(P,Q) in C*,
K=C(P,Q),
L=C(x,y).
```

If `[L:K]=3`, finite localization plus the Keller condition makes `F` a
generically three-sheeted polynomial map. Orevkov's 1987 theorem states that the
Jacobian of a three-sheeted polynomial map `C2 -> C2` cannot be constant.
Therefore no planar Keller map, and hence no Keller normalization, has rank
three.

This is `R3BC-01` at `literature_bound` scope. The packet does not reconstruct
Orevkov's proof and does not produce one section with `Phi(s) in C*`.

## 2. Strongest internal refinement

Conditionally retaining a finite locally free normal rank-three algebra, the
packet proves:

1. **Boundary-cubic trichotomy (`R3BC-02`).** After geometric strict-henselian
   reduction at a height-one prime, the index cubic is

   ```text
   L1 L2 L3,   L M^2,   or   L^3
   ```

   according to ramification partition `1+1+1`, `2+1`, or `3`. A cube occurs
   only at total ramification.

2. **Simultaneous boundary elimination (`R3BC-03`).** If `H` is the square-free
   product of all target boundary primes and `theta` generates every boundary
   semilocalization, then

   ```text
   s_T=theta+H T eta
   ```

   remains primitive at every boundary prime for all `T in B`, and

   ```text
   Phi(s_T)=D+H C T+H^2 B_2 T^2+H^3 A T^3.
   ```

3. **Exact counterfactual bridge.** If the Orevkov terminal is deliberately set
   aside, the only remaining equation is

   ```text
   D+H C T+H^2 B_2 T^2+H^3 A T^3=lambda in C*.
   ```

   Every irreducible factor is a nonboundary scalar sheet-collision divisor;
   boundary valuations have already been removed.

4. **Differential limitation (`R3BC-04`).** No nonconstant divisor is stable
   under both target translations, but the fixed-section value ideal is not
   shown translation-stable. Canonical derivations move collision divisors; they
   do not eliminate them.

5. **Countermodel ladder terminal (`R3BC-05`).** The integrated no-unit model
   reaches finite-flat/normal/connected/rational/open-`A2`, but fails source
   étaleness. Adding boundary-only different support on the specified source
   open produces a rank-three Keller map and is impossible by Orevkov. Thus the
   ladder stops exactly at the first genuine Keller condition.

6. **Literature falsification control (`R3BC-07`).** A cubic rare-property field
   model disproves the degree-two classification used in the first case of
   arXiv:2407.13795v1. This audit is not needed for `R3BC-01` and supports no
   theorem beyond rejecting that shortcut.

## 3. Proposed global claim deltas

The integration maintainer should allocate final global IDs dynamically. The
issue-local proposals are:

### `R3BC-01` — terminal literature claim

```text
status: literature_bound
statement: A planar polynomial Keller map cannot have function-field degree
three. A degree-three map is generically three-sheeted, while Orevkov's primary
1987 theorem says a three-sheeted polynomial map C2 -> C2 cannot have constant
Jacobian.
dependencies: CLM-001, CLM-002
source: Orevkov, Math. USSR-Izv. 29 (1987), DOI 10.1070/IM1987v029n03ABEH000984
nonclaims: no constructive unit-index section, no higher-degree result, no JC_2
```

### `R3BC-02` — conditional boundary trichotomy

```text
status: candidate_proved
statement: In a finite locally free normal rank-three algebra over a
characteristic-zero DVR, the geometric reduction of the trace-zero binary index
cubic is GL2-equivalent to L1L2L3, LM^2, or L^3 according to ramification
partition 1+1+1, 2+1, or 3.
dependencies: CLM-062
```

### `R3BC-03` — boundary-stable affine family

```text
status: candidate_proved
statement: After choosing one section primitive at every target boundary prime
and a square-free product H of those primes, every section theta+HT eta remains
primitive at the boundary and has index
D+HCT+H^2B_2T^2+H^3AT^3; hence all remaining factors are nonboundary scalar
collisions.
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

`R3BC-07` should remain packet-local literature-audit provenance unless an
integrator separately decides that the narrowly stated counterexample merits a
global claim.

## 4. Proposed graph, leaf, and issue disposition

After independent verification of the source binding and successful serialized
integration, the integration maintainer should consider:

1. add a terminal rank-three exclusion node supported by `R3BC-01`;
2. mark `OPEN-KELLER-INDEX-UNIT` / L14 disposed at the **rank-three Keller
   scope**, because its simultaneous hypotheses are inconsistent;
3. change `CLM-059` from an open rank-three bridge to a disposed or retired
   rank-three construction target, with a note that no unit section was
   constructed;
4. preserve `CLM-062`–`CLM-066` as conditional algebraic tools and corrections,
   not as unnecessary or false claims;
5. preserve the exact counterfactual equation from `R3BC-03` as the strongest
   internal boundary/moving-divisor identity;
6. close issue #3 only after merge and exact-main verification, with the
   Orevkov-based rank-three disposition and explicit nonclaims;
7. do not create a terminal edge to `JC_2`.

## 5. Shared surfaces requested, not edited

This worker changed no shared surface. Proposed serialized updates may involve:

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

Generated views must be regenerated by the integration maintainer after final ID
allocation. No permanent workflow change is requested.

## 6. Review and validation evidence

Pinned local adversarial review:

```text
reviewed_revision: c281ecd845fe63e88b47ae16f99135325a2f988f
disposition: ACCEPT_LITERATURE_BOUND_RANK_THREE_TERMINAL_AND_SCOPED_INTERNAL_REFINEMENTS; BLOCK_CONSTRUCTIVE_UNIT_SECTION_AND_BROADER_PROMOTION
```

Packet-local exact command:

```bash
python3 research/issues/rank-three-boundary-cube-unit/verify_all.py
```

Expected output ends with:

```text
rank-three boundary-cube packet verification: PASS
```

Predecessor and repository checks required on the exact pull-request head:

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

The permanent read-only repository workflow runs the complete maintained suite.
Passing CI is engineering evidence and does not strengthen the mathematical
status.

## 7. Integration boundary

This parallel worker has no merge authority. The integration-ready PR must
remain open and non-draft. It is not on `main` until a later integration
maintainer re-resolves live `main`, allocates global IDs, synchronizes the shared
surfaces, reruns exact-candidate validation, merges, and verifies exact `main`.
