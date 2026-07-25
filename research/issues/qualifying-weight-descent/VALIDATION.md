# Validation Record

## Issue-specific exact campaign

The construction revision was checked with

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

The machine-readable path was also checked:

```bash
python3 validate_qualifying_weight.py \
  --max-weight 128 --max-n 12 --fan-instances 32 \
  --support-degree 5 --json >/tmp/qwd-search.json
python3 -m json.tool /tmp/qwd-search.json >/dev/null
```

The generated JSON is transient and is not committed.

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
