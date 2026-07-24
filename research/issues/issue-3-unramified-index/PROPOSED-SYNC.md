# Proposed Claim-Ledger and Proof-Graph Synchronization

```text
authority: MUTABLE_NONAUTHORITATIVE
protocol_verdict: null
base_commit: 296867d82d09d51ef2386de2a62067408b7f949c
synchronization_policy: apply in one final isolated commit
```

This synchronization preserves the proved conditional monogenicity branch,
records the scoped algebraic obstruction, and narrows the surviving leaf to
the Keller etale-source unit-index problem.

## 1. Parallel-branch identifier reconciliation

The live issue #5 synchronization based on the same rich baseline consumes

```text
CLM-052 through CLM-057.
```

To avoid a silent merge collision, this branch uses

```text
CLM-058  scoped moving-index counterexample,
CLM-059  Keller-specific unit-index bridge.
```

The gaps are intentional on this branch and disappear when the parallel
synchronization is reconciled. The leaf identifier `L14` and proof-graph node
`OPEN-KELLER-INDEX-UNIT` are not used by that live branch.

## 2. Claim-ledger deltas

### `CLM-008`

Keep status `candidate_proved`. Replace its note by the audited noncircular
argument:

```text
If O=B[theta], then Omega_{O/B}=O/(f'(theta))dtheta. On the
Keller source Omega_{C[x,y]/B}=0, so f'(theta) is a unit of
C[x,y], hence a nonzero constant. For degree n>1, f'(T)-c is
a nonzero polynomial of degree less than n vanishing at theta,
contrary to minimality.
```

### `CLM-029`

Promote from `candidate` to `candidate_proved` at mutable scope:

```text
For every finite set S of height-one primes of B, one integral
primitive theta generates O_p over B_p for all p in S. Applying
this to the finite ramification support gives one element adapted
at every ramified height-one prime.
```

The object is the whole semilocal algebra `O_p`, not separate `O_q` factors.

### `CLM-030`

Keep `candidate_proved`, but clarify:

```text
After CLM-029, every remaining height-one component of the index
module has an unramified generic point. No vanishing or monotonicity
of that support is implied.
```

### `CLM-031`

Replace the mixed conditional/existence wording by the proved conditional
statement and mark `candidate_proved`:

```text
If one integral primitive theta generates O_p for every height-one
base prime p, then O=B[theta]; in a Keller normalization this forces
[L:K]=1.
```

Dependencies: `CLM-008`, `CLM-034`.

### `CLM-033`

Narrow to the proved scope and mark `candidate_proved`:

```text
If primitive elements exist on a Zariski cover of all Spec(B) and
their transition functions are affine-linear, then Pic(B)=0 and
H^1(Spec(B),O_B)=0 globalize them to one primitive element.
```

Do not infer this from a cover of a punctured base without independently
extending the affine cocycle.

### `CLM-034`

Keep `candidate_proved`, with the exact contraction and denominator-ideal
proof in `THEOREM-PACKET.md`.

### New `CLM-058` — scoped algebraic obstruction

```text
status: candidate_proved
track: monogenicity
statement: There exists a connected smooth rational normal finite-flat
rank-three B-algebra that is Zariski-locally monogenic on all of
Spec(B), has squarefree tame branch with one unramified sheet over each
generic branch point, and contains an open A2, but is not globally
monogenic. Every element generating all ramified height-one
semilocalizations has nonempty index support at unramified generic points;
the displayed open A2 is not etale over the target.
depends_on: []
```

### New `CLM-059` — surviving Keller-specific bridge

```text
status: open_bridge
track: monogenicity
statement: For the Keller normalization, use L=C(x,y), the specified
open immersion A2_source -> Y, and etaleness on A2_source to construct
an integral primitive theta whose index ideal is the unit ideal.
depends_on: [CLM-001, CLM-003, CLM-029, CLM-031, CLM-058]
```

## 3. Leaf and track deltas

### Dispose `L01` at exact scope

Change its status from `OPEN` to `SCOPED_OBSTRUCTION` and record:

```text
- CLM-029 is proved at mutable-candidate scope.
- CLM-034 and the CLM-008 implication are independently auditable.
- Purely algebraic elimination of the unramified index divisor is false.
- Smoothness, rationality, fixed-sheet branch, and an open A2 do not rescue it.
- The successor must use etaleness of the specified Keller source.
```

### Add successor leaf `L14-keller-index-form-unit.md`

The successor asks:

```text
For a Keller normalization, prove that the universal index form
represents a nonzero constant.
```

Its first exact case is rank three, where the trace-zero rank-two bundle has
the intrinsic binary cubic

```text
s |-> det(1,s,s^2).
```

The leaf forbids local monogenicity, generic fiber separation, parameter
counts, class-group triviality, rationality, smoothness, fixed-sheet
monodromy, or an open affine plane from substituting for the unit equation.

### Update Track C

Record the exact disposition:

```text
ramified adaptation: proved candidate;
R1/S2 globalization: proved candidate;
purely algebraic unramified elimination: counterexample;
Keller etale-source unit-index theorem: open.
```

## 4. Proof-graph deltas

1. Mark `OPEN-UNRAMIFIED-INDEX` as `scoped_obstruction`.
2. Add

```text
OPEN-KELLER-INDEX-UNIT
  type: leaf
  status: open
  artifact: leaf-packets/L14-keller-index-form-unit.md
```

3. Remove

```text
OPEN-UNRAMIFIED-INDEX -> TERM-DEGREE-ONE
  kind: sufficient-if-closed
```

4. Add

```text
OPEN-UNRAMIFIED-INDEX -> OPEN-KELLER-INDEX-UNIT
  kind: narrows-to
BR-MONOGENIC -> OPEN-KELLER-INDEX-UNIT
  kind: requires
OPEN-KELLER-INDEX-UNIT -> TERM-DEGREE-ONE
  kind: sufficient-if-closed
```

Against the pinned baseline this yields 35 graph nodes and 51 graph edges.
There are 14 leaf-packet files, of which 13 remain open.

## 5. Queue, issue index, and status deltas

- Replace the P0 `L01` work-queue entry by `L14`.
- Retain `L01` in a dispositions section as a scoped obstruction.
- Map `L14` to issue #3 as its narrowed successor unless a separate issue is
  opened later.
- Update the status summary to 53 claims on this branch. The highest claim
  number is 59 because six identifiers are reserved by the live parallel
  issue #5 synchronization.
- Put the Keller etale-source index-form unit problem first in the frontier.

## 6. Isolation rule

All issue-scoped mathematics is committed before synchronization. The shared
files listed below are then changed together in one final squash/isolated
commit:

```text
research/CLAIM_LEDGER.md
research/claim_ledger.json
research/PROOF_GRAPH.md
research/proof_graph.json
research/leaf-packets/L01-unramified-index-elimination.md
research/leaf-packets/L14-keller-index-form-unit.md
research/tracks/c-monogenicity-index-divisor.md
research/WORK_QUEUE.md
research/ISSUE_INDEX.md
STATUS.md
```

This keeps the scientific packet separable from coordination edits and makes
parallel reconciliation mechanical.
