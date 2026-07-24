# Conversation Archive Manifest

The repository records the exact declared identities of the two source conversation exports: filenames, message counts, byte counts, and raw/gzip SHA-256 values. The current Git tree does **not** contain complete reconstructible chunk sets for either export.

Conversation A has historical partial base64 chunks. They are retained as non-authoritative provenance but do not form the complete gzip stream. Conversation B has no embedded chunk set. The authoritative storage state is recorded in [`archive/manifest.json`](manifest.json).

| ID | Original filename | Messages | Raw bytes | Raw SHA-256 | Gzip SHA-256 | Storage |
|---|---|---:|---:|---|---|---|
| conversation-a | `chatgpt-export-2026-07-24.md` | 226 | 485597 | `57027fa47200934f1ebe5c2444695207bb07d4aca26e6c42d4e80c6d080695af` | `0a2f4e210df054d22c1dabf7347225d0668247421c4b2acbbb82c61fd5719a7d` | metadata-only; partial historical chunks |
| conversation-b | `chatgpt-export-2026-07-24(2).md` | 78 | 184647 | `170c7fdbfb9234ebc9c1e3c31f7f6f1e2ad261f2622403e49c08adec2db692aa` | `c6819f53aab7e6427859968a237ba863ddf20c169be040f712cc786b57696996` | metadata-only |

Repository validation reports metadata-only exports as warnings rather than pretending to verify hashes it cannot reproduce. [`scripts/extract_conversations.py`](../scripts/extract_conversations.py) refuses to claim successful extraction when no complete export is embedded.

Completion is tracked in [issue #22](https://github.com/snissn/planar-jacobian/issues/22). Once the original bytes are available, deterministic chunks should be committed, the recorded hashes verified in CI, and `storage_mode` restored to `embedded`.
