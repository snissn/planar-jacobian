# Issue #3 Provenance Manifest

```text
authority: MUTABLE_NONAUTHORITATIVE
manifest_kind: Git blob object IDs (SHA-1)
base_commit: 296867d82d09d51ef2386de2a62067408b7f949c
branch: issue-3/unramified-index-gpt56
manifest_excludes_itself: true
```

The identifiers below are the exact Git blob object IDs of the issue-scoped
candidate files after the constructor adversarial review. They are repository
object identifiers, not claims of scientific acceptance.

| Path | Git blob SHA-1 |
|---|---|
| `README.md` | `a0a0385b444b2e35b08e61fc422f10dd397acce4` |
| `THEOREM-PACKET.md` | `dab6c6f017a7c8c797e74291653eb3c07cd82002` |
| `COLLISION-DIVISORS.md` | `15237082cd7cd68b000b37ff6412db9282950387` |
| `KELLER-NEAR-COUNTERMODEL.md` | `637babf6af2e8c9f9acbd838f40e6f5d7cb331dc` |
| `COUNTERMODELS.md` | `c768972da6edeffb04d6be51cdb5d7a72b12698f` |
| `SOURCE-AUDIT.md` | `8b07e3cdc433f415aa2ed6f128230424d02ac267` |
| `ADVERSARIAL-REVIEW.md` | `1f257747d947a89a13bd0a6a53f7769a6b06cbf7` |
| `PROPOSED-SYNC.md` | `4a12643f42e52c4647c94fa6156c1db3b65835dd` |
| `HANDOFF.md` | `84e663604f1a0b3bfcf51df39a0408e382262699` |
| `verify_index_models.py` | `f3287f9520585ad1e709edfd2113d4596e165328` |

## Verification

For a checked-out repository, Git verifies a listed object by

```bash
git hash-object research/issues/issue-3-unramified-index/<FILE>
```

The output must equal the corresponding object ID above. This manifest
replaces the earlier SHA-256 list, which became stale when the audited files
were materially revised.
