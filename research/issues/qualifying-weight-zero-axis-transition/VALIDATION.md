# Validation

## Scope and environment

```text
platform: local isolated execution environment
Python: 3.13.5
SymPy: 1.14.0
scientific candidate: 7253c25b35847302ee44d697a98deedc1c70c819
candidate aggregate SHA-256: 4c1a66b7aed1a0b395745906b5484d099be1f3c17e5b067dfd3839cafa569fd3
review mode: local-adversarial-review
```

Validation establishes exact algebraic identities, support enumeration,
mutation detection, and packet consistency. It does not independently review
mathematical truth.

## Exact-candidate construction run

The candidate commit was exported to a clean temporary directory before
execution, so untracked review files could not affect the result.

```bash
git archive 7253c25b35847302ee44d697a98deedc1c70c819 | tar -x -C /tmp/zat-candidate
python3 -m compileall -q /tmp/zat-candidate/research/issues/qualifying-weight-zero-axis-transition
python3 /tmp/zat-candidate/research/issues/qualifying-weight-zero-axis-transition/defect6_transition_checker.py
```

Observed output:

```text
defect-six zero/axis transition checker: PASS
raw orientations: 16
canonical cases: 4
transition branches: 9
negative mutations: 8
exact assertions: 74
no defect-six {2,3}/{3,2} anchor, hence no pair-changing zero/axis transition
mathematical truth: established only by the accompanying analytic classification
```

The JSON mode additionally records, for every canonical system:

- all seven Rees stairs;
- exact layer polynomials;
- incident wall normals and support points;
- every zero/nonzero branch condition;
- the adjacent-face saturation result;
- the full Rees saturation result.

All 16 raw systems, four canonical systems, nine face ideals, and nine
branch-specialized full Rees ideals saturated to the unit ideal.

## Independent reviewer run

```bash
python3 research/issues/qualifying-weight-zero-axis-transition/review_defect6_transition.py
```

Observed output:

```text
independent defect-six transition review: PASS
raw orientations: 16
canonical cases: 4
mutations: 9
review assertions: 33
independent reconstruction finds no defect-six {2,3}/{3,2} system
```

The reviewer program does not import the construction program and compares its
arithmetic output to an explicit 16-row set.

## Issue-local aggregate suite

```bash
python3 -m compileall -q research/issues/qualifying-weight-zero-axis-transition
python3 research/issues/qualifying-weight-zero-axis-transition/verify_all.py
```

Expected and observed packet summary:

```text
qualifying-weight zero/axis transition packet: PASS
construction assertions: 74
review assertions: 33
raw orientations: 16
canonical cases: 4
transition branches: 9
residual systems: 0
mathematical truth: NOT established by validation alone
```

## Mutation coverage

Construction mutations:

1. delete a required selected monomial;
2. add a forbidden top monomial;
3. use a wrong `{2,3}` weighted degree;
4. drop the constant-bracket equation;
5. falsely share the origin;
6. normalize away the scalar `c`;
7. treat partial top cancellation as full descent;
8. omit a zero layer instead of retaining a zero polynomial.

The reviewer repeats those semantic classes independently and adds a ninth test
that forbids cancellation between different exponent vectors. Every mutation
was detected.

## Determinism and exactness

- all weight, support, and slope comparisons use integers or exact rational
  numbers;
- no floating-point geometry is used;
- Gröbner bases are over exact characteristic-zero coefficients;
- saturation variable names use deterministic SHA-256 signatures rather than
  process-randomized hashes;
- missing layers are explicit zeros;
- coefficients are collected by exact bivariate monomial exponents.

Candidate script SHA-256:

```text
c183fbad3c6b85929c260a1877a7727e2d6565bae2134015326d3fae4db30f29  defect6_transition_checker.py
```

Reviewer script SHA-256 at review construction:

```text
6c386fc0d7ed466ce83e25dad770af35dca3affd0acd6ba0372becbe361c734f  review_defect6_transition.py
```

## Manifest and ownership checks

The issue-local suite verifies:

- role `research-worker`;
- task issue `41`;
- the single owned path;
- absence of proposed `CLM-*` identifiers;
- presence of every required deliverable;
- valid JSON syntax and exact checker/reviewer counts.

A final changed-file audit must contain only the owned path. No workflow,
base64 payload, archive, readiness marker, synchronization script, root log, or
other temporary transport artifact belongs in the packet.

## Complete repository suite status

The issue-local construction and independent reviewer suites passed before publication.
The packet was then transplanted through the GitHub adapter onto a branch created from
exact live `main@f2399d8634521edf220d412a3e14d42eb56d89be`. The permanent read-only
repository workflow is the authoritative exact-head engineering check for the published
commit. Its run and conclusion are recorded in the pull-request metadata once available.

The maintained workflow is expected to run:

```bash
python3 -m compileall -q scripts research/issues
python3 scripts/render_views.py --check
python3 scripts/validate_repository.py
python3 scripts/validate_integration_contract.py
python3 -m unittest discover -s scripts/tests -p 'test_*.py'
python3 scripts/frontier.py
```

and every maintained issue-specific validator on the exact branch head. No green status
is claimed until the adapter reports it.

## Scientific validation boundary

The programs do not prove a general defect-six theorem, do not establish a
universal qualifying weight, do not transport the result to non-toric
normalization valuations, and do not prove `JC_2`. The analytic classification,
not the finite computation alone, supplies the exhaustiveness proof.
