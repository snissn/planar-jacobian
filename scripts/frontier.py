#!/usr/bin/env python3
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[1]
g=json.loads((ROOT/'research/proof_graph.json').read_text())
for n in g['nodes']:
    if n['type']=='leaf' and n['status']=='open':
        print(f"{n['id']}: {n['title']} -> {n.get('artifact','')}")
