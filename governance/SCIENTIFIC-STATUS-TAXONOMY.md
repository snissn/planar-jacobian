# Scientific Status Taxonomy

Every maintained artifact should distinguish these axes.

| Axis | Canonical examples | Meaning |
|---|---|---|
| claim status | `reviewed_scoped`, `candidate_proved`, `open_bridge`, `retired` | epistemic state of one statement |
| graph/leaf state | `open`, `reviewed`, `disposed`, `blocked` | program position and stop-rule outcome |
| review state | none, `independent-review`, `local-adversarial-review`, `ACCEPT`, `BLOCK` | scoped evaluation bound to a pinned revision |
| freeze state | named reviewed paths and permitted editorial changes | protection of reviewed scientific scope |
| repository transport | branch, PR, commit, mainline merge | byte preservation and history only |
| engineering validation | passing, failing, qualified | structural or executable consistency only |
| provenance | embedded, reproducible, `metadata_only`, historical partial | availability of source bytes |
| scientific inference | exact permitted statement and forbidden stronger inference | what a reader may conclude |

`MUTABLE_NONAUTHORITATIVE`, `CANDIDATE`, conditional, blocked, falsification, and countermodel work may all be integrated into `main`. `reviewed_scoped` or a freeze requires the applicable review gate. No axis silently changes another.
