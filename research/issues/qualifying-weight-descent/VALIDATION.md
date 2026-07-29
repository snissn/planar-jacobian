# Validation Record

## Issue-specific exact campaign

The final construction revision was checked with

```bash
python3 -m py_compile qwd_search_core.py qwd_search_symbolic.py \
  qwd_search_support.py validate_qualifying_weight.py
python3 validate_qualifying_weight.py \
  --max-weight 96 \
  --max-n 10 \
  --fan-instances 24 \
  --support-degree 5
```

Observed output:

```text
qualifying-weight exact search: PASS
primitive weights: 5611
affine A_N instances: 9
affine weight evaluations: 100998
finite-fan instances: 24
finite-fan brute comparisons: 134664
binomial-chain instances: 7
complete Jacobian equations: 42
missing-support patterns: 254
saturated named formal ideals: 1
exhaustive two-term support pairs: 44100 (degree <= 5)
axis-admissible support pairs: 43650
support pairs with exact minimum >=6: 32887
face-compatible high-defect pairs: 639
saturated bounded formal systems: 387
bounded formal survivors: 0
adjacent nonzero-vertex solutions checked: 1881
mutation controls: 4
exact assertions: 2488
mathematical authority: HUMAN PROOFS IN PACKET, NOT CHECK COUNTS
```

The missing-support control now checks the exact zero/nonzero propagation forced
by every adjacent binomial-chain recurrence. The zero-vertex mutation now
verifies both shared-vertex equations for distinct coprime exponent pairs at the
origin. These are semantic assertions rather than bookkeeping-only counters.

The machine-readable path was also checked:

```bash
python3 validate_qualifying_weight.py \
  --max-weight 128 --max-n 12 --fan-instances 32 \
  --support-degree 5 --json >/tmp/qwd-search.json
python3 -m json.tool /tmp/qwd-search.json >/dev/null
```

The larger campaign passed with:

```text
primitive weights: 10043
affine A_N instances: 11
affine weight evaluations: 220946
finite-fan instances: 32
finite-fan brute comparisons: 321376
exhaustive two-term support pairs: 44100
saturated bounded formal systems: 387
bounded formal survivors: 0
mutation controls: 4
exact assertions: 2520
```

The generated JSON is transient and is not committed.

## Additional adversarial fan checks

Two exact randomized stress checks were run outside the committed validator:

- 500 random finite support pairs satisfying the relevant nonnegative axis/fan
  conditions: the regular-fan minimum agreed with brute enumeration of all
  primitive weights with coordinates at most 80;
- 19,978 random ordered pairs of primitive first-quadrant rays with coordinates
  at most 100: the Euclidean subdivision retained its endpoints and order and
  every consecutive determinant was one.

The random seeds were fixed during the run. These checks are additional
falsification evidence only; the unbounded result is the written fan proof.

## Repository validation contract

The pull request exact head must pass the complete repository suite from
`AGENTS.md`:

```bash
python3 -m compileall -q scripts research/issues
python3 scripts/render_views.py --check
python3 scripts/validate_repository.py
python3 scripts/validate_integration_contract.py
python3 -m unittest discover -s scripts/tests -p 'test_*.py'
python3 scripts/frontier.py
```

Exact-head CI status and any remote validation receipt are recorded in the pull
request and final handoff, not fabricated in this construction-time file.

## Authority

Passing the scripts means the declared formulas, finite enumerations, Groebner
ideals, fan implementation, and mutation controls agree. It does not turn a
bounded search into an unbounded theorem. Mathematical authority remains the
written derivation, subject to local adversarial review and later independent
review if promotion is proposed.
