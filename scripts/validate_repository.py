#!/usr/bin/env python3
from pathlib import Path
import json, hashlib, gzip, sys
ROOT=Path(__file__).resolve().parents[1]
errors=[]; warnings=[]

def load(p):
    try: return json.loads((ROOT/p).read_text())
    except Exception as e: errors.append(f'{p}: {e}'); return {}
claims=load('research/claim_ledger.json')
graph=load('research/proof_graph.json')
manifest=load('archive/manifest.json')
claim_ids={c['id'] for c in claims.get('claims',[])}
for c in claims.get('claims',[]):
    for d in c.get('depends_on',[]):
        if d not in claim_ids: errors.append(f"claim {c['id']} missing dependency {d}")
node_ids={n['id'] for n in graph.get('nodes',[])}
for e in graph.get('edges',[]):
    if e['from'] not in node_ids: errors.append(f"edge missing from {e['from']}")
    if e['to'] not in node_ids: errors.append(f"edge missing to {e['to']}")
for n in graph.get('nodes',[]):
    a=n.get('artifact')
    if a:
        p=(ROOT/'research'/a).resolve()
        if not p.exists(): errors.append(f"node {n['id']} artifact missing: {a}")
for x in manifest.get('exports',[]):
    try:
        import base64
        b64=''.join((ROOT/p).read_text().strip() for p in x['base64_chunk_paths'])
        gz=base64.b64decode(b64)
        if hashlib.sha256(gz).hexdigest()!=x['gzip_sha256']: errors.append(f"gzip hash mismatch: {x['id']}")
        raw=gzip.decompress(gz)
        if hashlib.sha256(raw).hexdigest()!=x['raw_sha256']: errors.append(f"raw hash mismatch: {x['id']}")
    except Exception as e: errors.append(f"archive error {x.get('id')}: {e}")
for p in (ROOT/'research/leaf-packets').glob('*.md'):
    t=p.read_text()
    for marker in ['## Load-bearing question','## Accepted evidence','## Forbidden shortcuts','## Required artifacts','## Stop rule','## Handoff']:
        if marker not in t: errors.append(f'{p.relative_to(ROOT)} missing {marker}')
print(f"claims: {len(claim_ids)}")
print(f"graph nodes: {len(node_ids)}")
print(f"graph edges: {len(graph.get('edges',[]))}")
print(f"errors: {len(errors)}")
print(f"warnings: {len(warnings)}")
for x in errors: print('ERROR:',x)
for x in warnings: print('WARNING:',x)
if errors: sys.exit(1)
print('repository structure: PASS')
print('mathematical truth: NOT EVALUATED')
