#!/usr/bin/env python3
from pathlib import Path
import base64, gzip, json
ROOT=Path(__file__).resolve().parents[1]
m=json.loads((ROOT/'archive/manifest.json').read_text())
out=ROOT/'archive/extracted'; out.mkdir(exist_ok=True)
for e in m['exports']:
    b64=''.join((ROOT/p).read_text().strip() for p in e['base64_chunk_paths'])
    raw=gzip.decompress(base64.b64decode(b64))
    q=out/e['original_filename']; q.write_bytes(raw); print(q)
