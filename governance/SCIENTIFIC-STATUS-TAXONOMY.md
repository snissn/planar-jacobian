# Scientific Status Taxonomy

Every maintained artifact should distinguish the following dimensions.

| Dimension | Examples | Meaning |
|---|---|---|
| scientific mutability | `MUTABLE_NONAUTHORITATIVE`, reviewed freeze, mainline checkpoint | whether the artifact may be revised and what repository authority it carries |
| claim status | `literature_bound`, `candidate`, `candidate_proved`, `open_bridge`, `retired`, and the other canonical values | epistemic status of an identified mathematical statement |
| review state | no review, `independent-review`, `local-adversarial-review`, `ACCEPT`, `BLOCK` | scoped evaluation bound to a pinned revision |
| frozen scientific content | named paths and revision accepted without material scientific changes | exact scientific scope protected by a freeze decision |
| engineering validation | development, passing, failing, qualified | repository structure, execution, or tooling state only |
| execution validity | not an execution, valid, invalid | whether a declared computation or protocol run met its execution contract |
| protocol verdict | `null`, pass, scoped failure, inconclusive | outcome of a declared scientific protocol, when one exists |
| provenance | embedded/reproducible, `metadata_only`, historical partial | availability and reproducibility of source bytes |
| scientific inference | exact statement and forbidden stronger inference | what the artifact permits a reader to conclude |

## Required distinctions

- **Mutable research** may be useful and durable without being authoritative.
- **Literature-bound claims** require exact source and hypothesis matching.
- **Theorem candidates** require review; a complete-looking proof packet is not automatic acceptance.
- **Accepted reviews** are evidence at a pinned revision, not an automatic ledger mutation.
- **Frozen scientific content** identifies protected reviewed bytes or scope; it is distinct from claim status.
- **Engineering validation** establishes structural or execution properties only.
- **Provenance-only material** records origins and identity without supplying theorem authority.

Most files in this repository are analytic notes or governance records, not scientific executions. Their `protocol_verdict` is therefore `null`.
