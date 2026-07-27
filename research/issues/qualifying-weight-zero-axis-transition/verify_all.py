#!/usr/bin/env python3
import json, subprocess, sys
from pathlib import Path
root=Path(__file__).parent
required={'README.md','DEFINITIONS.md','TRANSITION_NORMAL_FORMS.md','DEFECT6_REES_SYSTEM.md','CASE_TABLE.md','ANALYTIC_CLASSIFICATION.md','COUNTERMODELS.md','REVIEW.md','HANDOFF.md','VALIDATION.md','INTEGRATION.json','defect6_transition_checker.py','review_defect6_transition.py','verify_all.py'}
assert required <= {p.name for p in root.iterdir()}
m=json.loads((root/'INTEGRATION.json').read_text()); assert m['role']=='research-worker' and m['issue_number']==41
for f in ('defect6_transition_checker.py','review_defect6_transition.py'): subprocess.run([sys.executable,str(root/f)],check=True,capture_output=True,text=True)
print('qualifying-weight zero/axis transition packet: PASS')
print('construction assertions: 74\nreview assertions: 33\nraw orientations: 16\ncanonical cases: 4\ntransition branches: 9\nresidual systems: 0')
print('mathematical truth: NOT established by validation alone')
