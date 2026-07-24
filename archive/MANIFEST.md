# Conversation Archive Manifest

The two source conversations are stored losslessly as chunked base64-encoded gzip streams. Concatenate the listed chunks, base64-decode, then gunzip. `scripts/extract_conversations.py` performs this reconstruction.

| ID | Original filename | Messages | Raw bytes | Raw SHA-256 | Gzip SHA-256 | Chunks |
|---|---|---:|---:|---|---|---:|
| conversation-a | `chatgpt-export-2026-07-24.md` | 226 | 485597 | `57027fa47200934f1ebe5c2444695207bb07d4aca26e6c42d4e80c6d080695af` | `0a2f4e210df054d22c1dabf7347225d0668247421c4b2acbbb82c61fd5719a7d` | 14 |
| conversation-b | `chatgpt-export-2026-07-24(2).md` | 78 | 184647 | `170c7fdbfb9234ebc9c1e3c31f7f6f1e2ad261f2622403e49c08adec2db692aa` | `c6819f53aab7e6427859968a237ba863ddf20c169be040f712cc786b57696996` | 6 |

Chunk paths are enumerated in `archive/manifest.json`. `archive/conversations/index.json` links the compact topic summaries; the compressed streams contain every original message.
