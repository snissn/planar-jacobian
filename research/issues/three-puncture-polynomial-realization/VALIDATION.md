# Validation

## Packet-specific commands

Run with Python 3.12 or newer and SymPy 1.14.0:

```bash
python3 -m compileall -q research/issues/three-puncture-polynomial-realization
python3 research/issues/three-puncture-polynomial-realization/verify_three_puncture.py --max-degree 12 --json
python3 research/issues/three-puncture-polynomial-realization/verify_all.py
```

The enlarged degree campaign is:

```bash
python3 research/issues/three-puncture-polynomial-realization/verify_three_puncture.py --max-degree 32 --json
```

The polynomial-curve theorem is not inferred from the bound. The finite
campaign mutates the exact general unit argument.

## Assertions covered

- exact branch normalization and smoothness;
- both polynomial unit certificates;
- polynomial descent of `R`;
- `P dQ=dR`;
- all listed function and differential orders;
- all-degree unit obstruction and bounded degree mutations;
- source primitive leading terms;
- rational constant-Jacobian controls for several ramification indices;
- exact primitive identity in those controls;
- detection of hidden denominators;
- puncture, nonexact-form, conductor, and generic-finiteness mutations;
- required artifact and nonclaim guards.

## Complete repository suite

The permanent workflow at `.github/workflows/repository-python-validators.yml`
must validate the exact final PR head. Its maintained checks include:

```bash
python3 -m compileall -q scripts research/issues
python3 -m unittest discover -s scripts/tests -p 'test_*.py'
python3 scripts/validate_integration_contract.py
python3 scripts/render_views.py --check
python3 scripts/validate_repository.py
python3 scripts/frontier.py
```

together with every maintained issue-specific regression.

## Interpretation

A passing run establishes exact symbolic identities, manifest/ownership
consistency, generated-view stability, and repository regressions. It does not
independently prove the primary-source theorem or promote the mutable
scientific candidate.
