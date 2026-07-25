# Qualifying-Weight Descent Handoff

```text
role: research-worker
task_issue: 41
owned_path: research/issues/qualifying-weight-descent/
base_main: 652a5e252626fa5816445651245e8a8946cee53e
construction_candidate: 3de516d76c8defd14a66b8727a6ae22618d368de
review_mode: local-adversarial-review
review_disposition: ACCEPT at mutable candidate scope
integration_state: integration-ready, not merged
```

## 1. Exact scientific disposition

The universal tame/full qualifying-weight statement remains open. The packet
returns the following supported results.

1. **Disposition 3 — substantial named class.** Every complete binomial-chain
   Keller pair `B_N` satisfies `Q=c y+lambda P^N`; one determinant-one target
   shear gives defect zero at weight `(N,1)`.
2. **Disposition 7 — the proposed scalar is inadequate without a declared
   transformation class.** The actual Keller automorphisms
   `A_N=(x+y^N,y+(x+y^N)^N)` have affine and determinant-one-linear minima
   `N^2-1`, while one nonlinear triangular target shear gives zero. The
   full-orbit scalar is zero on every automorphism by applying its inverse and
   is therefore circular as a detector.
3. **Fixed-representative finite reduction.** For each fixed Keller
   representative, the primitive-positive minimum occurs on a finite regular
   subdivision of the positive common normal fan.
4. **Minimal-counterexample obstruction.** A globally minimizing hypothetical
   counterexample has common-power initial forms at every positive weight and
   has both coprime exponents at least two at every weight attaining the global
   minimum defect. Adjacent positive edges have constant coprime ratio only
   across nonzero shared vertices.

The exact remaining bridge is to force termination of certified complete-top
descents or exclude/bound a terminal common-power core, and then connect the
toric positive-weight record to non-toric normalization-boundary valuations.

## 2. Authority boundary

Unconditional repository authority consumed:

```text
primitive positive w and kappa_w<=4 => polynomial automorphism.
```

The issue #29 fixed-weight defect-five theorem remains candidate-only. This
packet uses it only in explicitly conditional sentences. It does not claim a
universal `mu<=5`, defect-six closure, arbitrary filtered termination, or
`JC_2`.

The local adversarial review is bound to construction revision
`3de516d76c8defd14a66b8727a6ae22618d368de` and returned `ACCEPT` at mutable
candidate scope. It is not independent review and cannot support
`reviewed_scoped` promotion.

## 3. Exact construction and review artifacts

Required files are present under the owned path:

- `README.md`;
- `DEFINITIONS.md`;
- `TRANSFORMATION_ORBIT.md`;
- `MINIMAL_COUNTEREXAMPLE.md`;
- `NEWTON_WEIGHT_DICTIONARY.md`;
- `LITERATURE_AUDIT.md`;
- `CASE_TABLE.md`;
- `COUNTERMODEL_SEARCH.md`;
- `REVIEW.md`;
- `HANDOFF.md`;
- `VALIDATION.md`;
- `validate_qualifying_weight.py` with the issue-local support modules;
- `INTEGRATION.json`.

The construction comparison from live base to the pinned candidate contains
only issue-owned additions. No root README, STATUS, shared ledger, proof graph,
queue, issue index, generated view, or permanent workflow was edited.

## 4. Proposed shared deltas for a later integration maintainer

No global identifiers are allocated here. After re-resolving then-current
`main`, an integration maintainer may allocate canonical identifiers and
synchronize only the following proposed content.

### Proposed claim content

- class-indexed orbit minima exist as achieved nonnegative integers;
- `mu_aff(A_N)=mu_SL(A_N)=N^2-1` for the explicit automorphism family;
- a fixed representative has a finite exact positive-weight test set;
- the complete binomial-chain class shears to defect zero;
- the minimal-counterexample reduction retains a non-shear common-power core
  at defect-minimizing weights;
- the unqualified/full-orbit scalar is inadequate as a constructive invariant.

Suggested statuses are mutable `candidate_proved_scoped` for the exact theorems
and `open_bridge` for the terminal common-power/no-escape step. An independent
review is required before any reviewed promotion.

### Proposed graph/queue content

Add one qualifying-weight reduction node supported by the reviewed defect-four
node and, conditionally only, by the defect-five candidate. Its outgoing open
leaf should be:

```text
force a certified complete-top descent or bound/exclude the terminal
m,n>=2 common-power Newton core while preserving normalization-boundary data.
```

The affine obstruction is a transformation-class control, not a terminal
Jacobian-conjecture edge. The binomial-chain result is a scoped subclass node.

### Shared surfaces requested

- `research/tracks/m-filtered-equivariance.md`;
- `research/claim_ledger.json`;
- `research/proof_graph.json`;
- `research/work_queue.json`;
- `research/ISSUE_INDEX.md`.

These requests are proposals only; this worker branch does not edit them.

## 5. Validation receipt

Issue-specific default exact search passed with:

```text
5611 primitive weights
44100 ordered two-term support pairs
387 saturated high-defect formal systems
0 formal Keller survivors
1881 adjacent nonzero-vertex compatibility solutions
4 semantic mutation controls
2488 exact assertions
```

The larger JSON campaign at weight bound 128, `N<=12`, and 32 fan instances
also passed. The complete repository suite and exact-head CI must be verified
on the final pull-request head. Passing scripts are process evidence, not
mathematical review authority.

## 6. Next exact research tasks

The smallest useful successors are:

1. prove that every defect-minimizing common-power face with exponents
   `m,n>=2` forces a complete-top composite across its adjacent nonzero chain;
2. classify the zero/axis transition patterns that can change the coprime
   exponent pair;
3. lift the complete Rees transition equations from one fan wall through all
   adjacent walls without assuming absent monomials;
4. establish a simultaneous monomialization/no-escape theorem connecting the
   finite Newton core to the non-toric Laurent--conductor boundary system.

A defect-six staircase is not the first successor unless one of these tasks
produces a qualifying weight or a terminating descent.

## 7. Remote completion boundary

This packet is intended to remain in one non-draft integration-ready pull
request. It must not be merged during the parallel round. Completion means the
PR exact head has passed issue-specific validation and the complete repository
CI suite; it does not mean the work is on `main` or scientifically reviewed.
