# Handoff

## Worker disposition

```text
role: research-worker
task_issue: 41
owned_path: research/issues/qualifying-weight-zero-axis-transition/
scientific_candidate: 7253c25b35847302ee44d697a98deedc1c70c819
review_mode: local-adversarial-review
review_disposition: ACCEPT_SCOPED
scientific_status: candidate_proved_scoped / MUTABLE_NONAUTHORITATIVE
remote_state: integration-ready branch published through GitHub adapter
```

The exact bounded result is disposition A: no defect-six `{2,3}` or `{3,2}`
common-power anchor satisfies the complete Rees equations, so no requested
pair-changing zero/axis transition exists.

## Integration preflight record

The task was ordered after the serialized integration round. Immediately before publication, live `main` resolved to

```text
f2399d8634521edf220d412a3e14d42eb56d89be
```

The packet was transplanted without shared-surface edits onto the fresh branch
`issue-41/qualifying-weight-zero-axis-transition-gpt56`. The integration maintainer must
review the exact-head validation receipt, allocate any final global IDs only during
serialized integration, and merge only in the designated postflight round.

If any scientific byte among the eight pinned candidate files changes, a new
candidate revision and renewed review are required. Base refresh, PR metadata,
validation receipts, and other transport-only edits do not change the accepted
scope when the candidate bytes remain exact.

## Proposed shared claim deltas

No final global IDs are allocated here. Suggested issue-local records for the
integration maintainer are:

- `ZAT-D6-ORIENT` — `candidate_proved_scoped`: 16 raw orientations reduce to
  four determinant-one normal forms;
- `ZAT-D6-REES` — `candidate_proved_scoped`: all four complete coefficient
  ideals saturate to `(1)` under `A B c!=0`;
- `ZAT-D6-WALL` — `candidate_proved_scoped`: all nine normalized first-wall
  branches are inconsistent and have adjacent defect at most five;
- `ZAT-D6-NO-TRANSITION` — `candidate_proved_scoped`: the first possible
  `{2,3}` pair-changing terminal transition is absent;
- `ZAT-D6-CHECK` — `verified_internal`: independent exact implementations and
  mutation campaigns agree.

Suggested shared surfaces, to be updated only by the integration maintainer:

- `research/tracks/m-filtered-equivariance.md`;
- `research/claim_ledger.json` and generated claim view;
- `research/proof_graph.json` and generated graph view;
- `research/work_queue.json` and generated queue view;
- `research/ISSUE_INDEX.md`;
- generated root status surfaces as required by current main.

## Proposed graph effect

Dispose the bounded node representing

```text
defect minimum 6 + coprime top pair {2,3}
+ zero/axis/nonshared first transition
```

at mutable candidate scope. Do not attach a terminal edge to `JC_2`.

The next exact filtered-equivariance leaf, if the global minimum remains six,
is the next coprime common-power size: unordered pairs `{2,5}` and `{3,4}`
(first total exponent seven), with the same scalar-retaining complete-stair and
transition requirements. Alternatively, a proof that the global minimum
cannot equal six would bypass that enumeration.

## No-escape boundary

Do not infer that this Newton-weight exclusion controls every divisor of the
finite normalization. The non-toric Laurent/conductor packet shows that local
boundary data need not bound all global displayed support because leading
common-power cancellations can hide layers. The monomialization/no-escape edge
remains open.

## Validation handoff

Run at minimum:

```bash
python3 -m compileall -q research/issues/qualifying-weight-zero-axis-transition
python3 research/issues/qualifying-weight-zero-axis-transition/defect6_transition_checker.py
python3 research/issues/qualifying-weight-zero-axis-transition/review_defect6_transition.py
python3 research/issues/qualifying-weight-zero-axis-transition/verify_all.py
python3 -m compileall -q scripts research/issues
python3 scripts/render_views.py --check
python3 scripts/validate_repository.py
python3 scripts/validate_integration_contract.py
python3 -m unittest discover -s scripts/tests -p 'test_*.py'
python3 scripts/frontier.py
```

Then run every maintained issue-specific suite present on the refreshed main.
Passing checks are engineering evidence, not mathematical promotion.

## Remote publication

The packet was transplanted through the GitHub adapter onto a fresh branch from
`main@f2399d8634521edf220d412a3e14d42eb56d89be`. The integration-ready pull
request and exact remote head are recorded in the PR body. The PR remains
unmerged, as required for the parallel round.
