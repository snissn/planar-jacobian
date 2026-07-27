# Independent Review Validation Record

## 1. Local commands

```text
python3 -m py_compile \
  research/issues/defect-5-independent-review/review_validate_defect5_independent.py

python3 \
  research/issues/defect-5-independent-review/review_validate_defect5_independent.py \
  --max-weight 96
```

## 2. Observed reviewer-checker output

```text
review mode: independent-review
reviewed candidate: 2eeb36d232366d124b5a66774b29769ec1eba43d
primitive weights enumerated (1 <= p <= q <= 96): 2806
exponent-one descents reclassified: 817
empty common-root supports rejected: 10065
supported no-descent arithmetic cases: 342
unequal projective charts eliminated exactly: 338
unequal saturated ideals: 338
equal-weight saturated ideals: 2
derived family signatures (a,p,rho): 9
zero layers generated: 771
systems with multiple possible resonant brackets: 6
largest saturated input: 15 equations, 19 variables
semantic corruptions detected: 9
source/target orientation checks: 2
exact rational/algebraic Keller-Rees trials: 15
formal complete-staircase survivors: 0
independent defect-five review checker: PASS
mathematical authority: HUMAN RECONSTRUCTION, NOT BOUNDED CHECK COUNTS
```

## 3. Permanent workflow

The repository's permanent read-only workflow
`.github/workflows/repository-python-validators.yml` checks out the exact pull
request head and runs:

```text
python3 -m compileall -q scripts research/issues
python3 -m unittest discover -s scripts/tests -p 'test_*.py'
python3 scripts/validate_integration_contract.py
python3 scripts/render_views.py --check
python3 scripts/validate_repository.py
python3 scripts/frontier.py
```

It also runs all maintained issue-specific regression checks. The exact PR-head
run and conclusion are recorded in the PR conversation rather than embedded here:
putting a workflow run ID into this file would change the tested head and create
a self-referential validation loop.

## 4. Authority limit

Compilation, bounded enumeration, saturation, mutation tests, and Actions are
process and falsification evidence. The independent human reconstruction and
pinned disposition carry the mathematical review.
