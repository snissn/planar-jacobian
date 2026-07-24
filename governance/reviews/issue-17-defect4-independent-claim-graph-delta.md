# Proposed Claim-Ledger and Proof-Graph Delta

> **Review mode:** `independent-review`
> **Reviewed candidate:** `96fc7ec34bd3b685a0edeae7ecd4404abab7e2f1`
> **Independent disposition:** `ACCEPT`
> **Application status:** proposal only; not applied by this review

## 1. Claim ledger

After the repository's exact freeze/integration procedure binds this review to
the candidate bytes, change only the following statuses:

| Claim | Current | Proposed | Dependency change |
|---|---|---|---|
| `CLM-047` — exact positive-weight Rees staircase | `candidate_proved` | `verified_internal` | none |
| `CLM-048` — resonant graded pair classification | `candidate_proved` | `verified_internal` | none |
| `CLM-049` — endpoint resonance implies automorphism | `candidate_proved` | `verified_internal` | none |
| `CLM-050` — defects at most three | `candidate_proved` | `verified_internal` | none |
| `CLM-051` — defect-four interior exhaustion | `candidate_proved` | `verified_internal` | none |
| `CLM-052` — positive-weight defect at most four theorem | `candidate_proved` | `verified_internal` | none |

Suggested note appended to each promoted claim:

```text
Independent review ACCEPT bound to candidate
96fc7ec34bd3b685a0edeae7ecd4404abab7e2f1,
candidate aggregate
21550a32815a617cdb108c41954fb422c66773656a560505aeefcbf180a4a097,
and review branch review/issue-17-defect4-independent-gpt56.
```

For `CLM-052`, retain the existing scope note and add:

```text
This is not JC_2, does not cover defect >=5, and does not prove existence of a
small-defect positive weight for an arbitrary Keller pair.
```

No other claim status or dependency is justified by this review.

## 2. Proof graph

After the same freeze/integration gate:

| Node / edge | Current | Proposed |
|---|---|---|
| `OPEN-DEFECT-4.status` | `candidate_proved` | `verified_internal` |
| `OPEN-DEFECT-4.artifact` | `leaf-packets/L13-defect-4-staircase.md` | retain; add the independent review as a bound review artifact if the schema permits |
| `OPEN-DEFECT-4 -> OPEN-GRADED-REDUCTION` | `supports` | retain unchanged |
| `BR-FILTERED-EQUIVARIANCE.status` | `open` | retain unchanged |
| all terminal nodes and `ROOT-JC2` | unchanged | unchanged |

Do **not** add an edge from `OPEN-DEFECT-4` to `TERM-DEGREE-ONE` or
`TERM-AUTOMORPHISM`. The accepted theorem covers only the declared
positive-weight small-defect subclass. The full graded-reduction leaf still
needs a theorem that produces or preserves a qualifying weight for the class it
intends to control.

## 3. Issue state

The mathematical independence blocker is resolved by this `ACCEPT`, but this
review does not close issue #17 automatically. Closure should follow only after
maintainers apply the exact reviewed delta under the repository's freeze and
integration procedure and verify the resulting hashes.

## 4. Explicit non-delta

This proposal does not:

- edit the candidate proof;
- begin defect five;
- promote any external literature claim;
- change `ROOT-JC2` from `blocked`;
- merge, tag, freeze, or push to `main`;
- infer that every Keller pair admits a primitive positive weight with
  `kappa_w<=4`.
