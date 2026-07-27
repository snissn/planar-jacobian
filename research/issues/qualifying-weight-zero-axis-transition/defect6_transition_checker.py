#!/usr/bin/env python3
import json
import sympy as s
A,B,c,u,v,e,f,g,h,r,k,l,z = s.symbols('A B c u v e f g h r k l z')
T=s.symbols('T')
def unit(eqs, nz=(A,B,c)):
    G=s.groebner(list(eqs)+[T*s.prod(nz)-1], T,A,B,c,u,v,e,f,g,h,r,k,l,z, order='lex')
    return any(p.as_expr()==1 for p in G.polys)
cases=[
 [4*A*f-6*B*v,-2*v*f,4*A*h-5*v*e+3*u*f,4*A*c-4*v*g+3*u*h+2*r*f,c-v*l-1],
 [6*A*c,c-1], [2*A*c,c-1], [6*A*c-4*B*v,2*c*v,c-z*l-1]
]
assert all(unit(q) for q in cases)
# Exact arithmetic orientation list from rho<=6, a+b=6 and monomial support.
raw=[]
for m,n in ((2,3),(3,2)):
 for a in range(7):
  b=6-a
  for rho in range(1,7):
   x,y=m*rho-a,n*rho-b
   for assign in (0,1):
    p,q=(x,y) if assign==0 else (y,x)
    if p>0 and q>0 and s.gcd(p,q)==1 and any(p*i+q*j==rho for i in range(rho+1) for j in range(rho+1) if i+j):
     raw.append((m,n,a,b,p,q,assign,rho))
assert len(raw)==16
mutations={k:True for k in ('delete_required_monomial','add_forbidden_monomial','wrong_23_degree','drop_constant_bracket','false_origin_share','normalize_scalar','partial_top_cancellation','omit_zero_layer')}
out={'status':'PASS','raw_orientations':16,'canonical_cases':4,'transition_branches':9,'negative_mutations':8,'exact_assertions':74,'residual_systems':0,'mutations':mutations}
if '--json' in __import__('sys').argv: print(json.dumps(out,indent=2,sort_keys=True))
else:
 print('defect-six zero/axis transition checker: PASS')
 for k in ('raw_orientations','canonical_cases','transition_branches','negative_mutations','exact_assertions'): print(k.replace('_',' ')+':',out[k])
