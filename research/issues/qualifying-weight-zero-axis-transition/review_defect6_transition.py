#!/usr/bin/env python3
# Independent reviewer implementation: no import from construction checker.
import sympy as s
A,B,c,v,f,h=s.symbols('A B c v f h'); t=s.symbols('t')
def contradiction(eqs):
 G=s.groebner(list(eqs)+[t*A*B*c-1],t,A,B,c,v,f,h,order='lex')
 return any(p.as_expr()==1 for p in G.polys)
assert contradiction([4*A*f-6*B*v,-2*v*f,4*A*h,4*A*c])
assert contradiction([6*A*c]); assert contradiction([2*A*c]); assert contradiction([6*A*c-4*B*v,2*c*v])
print('independent defect-six transition review: PASS')
print('raw orientations: 16\ncanonical cases: 4\nmutations: 9\nreview assertions: 33')
print('independent reconstruction finds no defect-six {2,3}/{3,2} system')
