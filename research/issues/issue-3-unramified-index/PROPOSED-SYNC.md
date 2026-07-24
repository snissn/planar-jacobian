# Proposed Claim-Ledger and Proof-Graph Synchronization

```text
authority: MUTABLE_NONAUTHORITATIVE
protocol_verdict: null
base_commit: 296867d82d09d51ef2386de2a62067408b7f949c
synchronization_policy: apply in one final isolated commit
```

This file separates the issue-scoped mathematical artifacts from the shared coordination edits. The proposed synchronization is deliberately minimal: preserve the existing monogenicity branch, record the scoped algebraic obstruction, and narrow the surviving leaf to the Keller-specific unit-index problem.

## 1. Claim-ledger deltas

### `CLM-008`

Keep status `candidate_proved`. Replace the note by the audited noncircular argument:

```text
If O=B[theta], then Omega_{O/B}=O/(f'(theta))dtheta. On the
Keller source Omega_{C[x,y]/B}=0, so f'(theta) is a unit of
C[x,y], hence a nonzero constant. For degree n>1, f'(T)-c is
a nonzero polynomial of degree <n vanishing at theta, contrary
to minimality.
```

### `CLM-029`

Promote from `candidate` to `candidate_proved` on the mutable branch:

```text
For every finite set S of height-one primes of B, one integral
primitive theta generates O_p over B_p for all p in S. Apply this
to the finite ramification support.
```

The proof must refer to the entire semilocal algebra `O_p`, not to separate local rings `O_q`.

### `CLM-030`

Keep `candidate_proved`, but clarify that its support statement is conditional on `CLM-029` and says only:

```text
all remaining height-one index support is unramified;
no vanishing or monotonicity is implied.
```

### `CLM-031`

The current wording mixes a proved conditional implication with the unproved existence assertion. Replace it by the proved conditional theorem and mark it `candidate_proved`:

```text
If one integral primitive element generates O_p over B_p for every
height-one p, then O=B[theta]; for a Keller normalization this forces
[L:K]=1.
```

Dependencies: `CLM-008`, `CLM-034`.

### `CLM-033`

Narrow the statement to the proved scope and mark it `candidate_proved`:

```text
If primitive elements exist on a Zariski cover of all Spec(B) and
their transition functions are affine-linear, then Pic(B)=0 and
H^1(Spec(B),O_B)=0 globalize them to one primitive element.
```

Do not infer this from a cover of the punctured base. Extension of the affine cocycle across a codimension-two set remains unproved.

### `CLM-034`

Keep `candidate_proved`, with the exact `R1/S2` proof recorded in `THEOREM-PACKET.md`.

### New `CLM-052` — scoped algebraic obstruction

```text
status: candidate_proved
track: monogenicity
statement: There exists a connected normal finite-flat rank-three
B-algebra, Zariski-locally monogenic on all of Spec(B), for which
every element generating all ramified height-one semilocalizations
has a nonempty index divisor at unramified generic points.
depends_on: []
```

### New `CLM-053` — surviving Keller-specific bridge

```text
status: open_bridge
track: monogenicity
statement: For the Keller normalization, use L=C(x,y), the open
immersion A2_source -> Y, and source etaleness to construct an
integral primitive theta with unit index ideal.
depends_on: [CLM-029, CLM-030, CLM-031, CLM-052]
```

## 2. Leaf and track deltas

### Dispose `L01` at exact scope

Change its status from `OPEN` to `SCOPED_OBSTRUCTION` and add:

```text
- CLM-029 is proved at mutable-candidate scope.
- CLM-034 and the CLM-008 implication are independently audited.
- Purely algebraic elimination of the unramified index divisor is false.
- The successor must consume the Keller open-immersion package.
```

### Add successor leaf `L14-keller-index-form-unit.md`

The successor should ask only:

```text
For a Keller normalization, prove that the universal index form
represents a nonzero constant. First exact case: in rank three,
show that the binary cubic index form represents an element of C*.
```

It must forbid local monogenicity, generic fiber separation, parameter counts, and class-group triviality as substitutes for the unit equation.

### Update Track C

Replace the generic-existence question by the exact disposition:

```text
ramified adaptation: proved candidate;
R1/S2 globalization: proved candidate;
pure algebraic unramified elimination: counterexample;
Keller-specific unit-index theorem: open.
```

## 3. Proof-graph deltas

1. Mark node `OPEN-UNRAMIFIED-INDEX` as `scoped_obstruction`.
2. Add node:

```text
OPEN-KELLER-INDEX-UNIT
  type: leaf
  status: open
  artifact: leaf-packets/L14-keller-index-form-unit.md
```

3. Replace the edge

```text
OPEN-UNRAMIFIED-INDEX -> TERM-DEGREE-ONE
```

by

```text
OPEN-UNRAMIFIED-INDEX -> OPEN-KELLER-INDEX-UNIT   kind: narrows-to
OPEN-KELLER-INDEX-UNIT -> TERM-DEGREE-ONE         kind: sufficient-if-closed
```

This preserves the branch while preventing the scoped counterexample from being misread as a route to degree one.

## 4. Queue and status deltas

- Replace the P0 L01 work-queue entry by the new L14 leaf.
- Retain L01 in a short dispositions section.
- Update counts to 53 claims, 35 graph nodes, 51 graph edges, and 13 open leaves.

## 5. Reconciliation note

The new identifiers `CLM-052`, `CLM-053`, and `L14` are proposed against the pinned PR #15 baseline. If another parallel branch has already consumed those identifiers, renumber only in the final shared synchronization commit; do not alter the issue-specific theorem and countermodel paths.
