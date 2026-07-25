# Handoff

> Authority: `MUTABLE_NONAUTHORITATIVE`  
> Current disposition: `SUBCLASS_EXCLUSION_WITH_EXACT_REDUCTION`

## 1. What is banked

The packet banks the following candidate-scoped results.

1. `Der_C(C[P,Q])(-log g)` is free of rank two for every irreducible reduced
   plane branch, with an exact syzygy presentation and Saito determinant test.
2. Jordan semisimple and nilpotent parts of a locally finite logarithmic field
   remain logarithmic.
3. An integral semisimple logarithmic field gives a genuine target `G_m`
   action; after target linearization, `g` is a semi-invariant of a diagonal
   action.
4. A target torus action preserving the branch lifts through the finite
   normalization after a finite isogeny.
5. In the unique generically ramified boundary class, the lifted action
   preserves `U`; the exact equivariant planar Keller theorem excludes the
   model.
6. A unique generically unramified boundary is excluded by purity and triviality
   of finite etale covers of `A2_C`.
7. One-boundary exactness gives the leading relation

   ```text
   n a' b-m a b'=0
   ```

   but does not eliminate higher principal parts.

## 2. Smallest surviving calculation

The next calculation should not search for another arbitrary logarithmic field.
It should fix one non-toric boundary type and solve the complete finite system.

Recommended first case:

```text
- D0 smooth and rational;
- target branch C smooth but not assumed A1;
- pole orders (m,n) minimal among a hypothetical counterexample;
- one puncture on the normalization;
- fixed ramification index e.
```

Compute successively:

1. the leading common function `c(t)` from
   `a=alpha c^(m/d), b=beta c^(n/d)`;
2. the next two orders of (2.1)-(2.3);
3. the induced divisor of `c(t)` at the unique puncture;
4. the conductor quotient, which is trivial in the smooth case;
5. whether the resulting target branch equation admits any diagonal
   semi-invariance;
6. if it does, invoke `OBLF-05`; if it does not, record the first nonzero
   invariant obstruction.

For a singular successor, use the smallest non-weighted numerical semigroup
and carry the same calculation modulo its conductor.

## 3. Exact open bridge

The remaining bridge is

```text
one-boundary Laurent/conductor data
=> target semi-invariance, contradiction, or a forbidden conductor moment.
```

The packet proves neither implication globally. It makes the target explicit
at each fixed valuation and conductor type.

## 4. Review boundary

`REVIEW.md` is a separate local adversarial pass. Its acceptance, if any, is
only acceptance for candidate integration. Independent review is still needed
before promotion or freeze. In particular the finite-isogeny lifting lemma and
the dependence on arXiv:2607.20210v1 should be reviewed independently.

## 5. Validation

Run from the repository root:

```bash
python3 -m compileall -q research/issues/one-boundary-logarithmic-field
python3 research/issues/one-boundary-logarithmic-field/verify_all.py
python3 scripts/render_views.py --check
python3 scripts/validate_repository.py
python3 scripts/frontier.py
```

Passing these commands checks exact symbolic identities and repository
consistency. It does not establish mathematical truth.

## 6. Integration note

The owned path is

```text
research/issues/one-boundary-logarithmic-field/
```

Shared claims, graph, queue, root README, status, and workflow changes are made
only in the final synchronization commit after re-resolving `main`. If `main`
moves, transplant this owned path onto the new head and regenerate the shared
views; do not merge unrelated branch history.