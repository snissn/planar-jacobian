#!/usr/bin/env python3
"""Independent symbolic regression for issue #17; no candidate-checker imports."""
import math, random
from collections import defaultdict
import sympy as s

MODE="independent-review"; SHA="96fc7ec34bd3b685a0edeae7ecd4404abab7e2f1"
BOUND=80; REES_TRIALS=36; EXCEPTION_TRIALS=800
x,y,t=s.symbols("x y t"); N=0; M=0

def req(ok,msg):
 global N; N+=1
 if not bool(ok): raise AssertionError(msg)
def mut(ok,msg):
 global M; req(ok,msg); M+=1
def J(f,g): return s.expand(s.diff(f,x)*s.diff(g,y)-s.diff(f,y)*s.diff(g,x))
def mons(p,q,d):
 if d<0:return []
 return [((d-q*j)//p,j) for j in range(d//q+1) if (d-q*j)%p==0]
def wdeg(f,p,q):
 return max(p*i+q*j for (i,j),c in s.Poly(s.expand(f),x,y).terms() if c)
def lay(f,p,q):
 d=wdeg(f,p,q); z=defaultdict(lambda:s.Integer(0))
 for (i,j),c in s.Poly(s.expand(f),x,y).terms(): z[d-p*i-q*j]+=c*x**i*y**j
 return d,dict(z)
def coeffs(f): return [] if s.expand(f)==0 else [s.expand(c) for c in s.Poly(s.expand(f),x,y).coeffs()]
def gen(prefix,p,q,d,tag):
 cs=[s.Symbol(f"{prefix}_{tag}_{k}") for k,_ in enumerate(mons(p,q,d))]
 return s.expand(sum(c*x**i*y**j for c,(i,j) in zip(cs,mons(p,q,d),strict=True))),cs

# Rees exponent and exact random Keller staircases.
dp,dq,ps,qs=s.symbols("dP dQ p q",integer=True)
req(s.expand((dp-ps)+(dq-qs)-(dp+dq-ps-qs))==0,"Rees x/y exponent")
req(s.expand((dp-qs)+(dq-ps)-(dp+dq-ps-qs))==0,"Rees y/x exponent")
rng=random.Random(0xD4F4A56)
def random_pair():
 P,Q=x,y
 for k in range(2):
  z=s.Symbol(f"z{k}"); d=rng.choice((2,2,3)); a=[rng.randint(-3,3) for _ in range(d+1)]
  if not any(a[1:]):a[d]=1
  h=sum(a[i]*z**i for i in range(d+1))
  if k%2==0:Q=s.expand(Q+h.subs(z,P))
  else:P=s.expand(P+h.subs(z,Q))
 return P,Q
for trial in range(REES_TRIALS):
 P,Q=random_pair(); req(J(P,Q)==1,"random pair lost J=1")
 while True:
  p,q=rng.randint(1,7),rng.randint(1,7)
  if math.gcd(p,q)==1:break
 dP,PL=lay(P,p,q); dQ,QL=lay(Q,p,q); k=dP+dQ-p-q; req(k>=0,"negative defect")
 Pc=s.expand(t**dP*P.subs({x:t**(-p)*x,y:t**(-q)*y},simultaneous=True))
 Qc=s.expand(t**dQ*Q.subs({x:t**(-p)*x,y:t**(-q)*y},simultaneous=True))
 req(s.expand(J(Pc,Qc)-t**k)==0,"direct Rees identity")
 top=max(max(PL,default=0)+max(QL,default=0),k); reson=[]
 for n in range(top+1):
  terms=[J(PL.get(i,0),QL.get(n-i,0)) for i in range(n+1)]
  req(s.expand(sum(terms)-(1 if n==k else 0))==0,f"S_{n}")
  if n==k:
   req(all(not z.has(x,y) for z in terms),"nonconstant resonant bracket"); reson=terms
  if n>k:req(all(z==0 for z in terms),"nonzero bracket above resonance")
 req(any(z!=0 for z in reson) and s.expand(sum(reson)-1)==0,"resonance")
P=x**3+2*x*y+y; Q=x**2-y**2+3*y
mut(s.diff(P,x)*s.diff(Q,y)+s.diff(P,y)*s.diff(Q,x)!=J(P,Q),"Jacobian sign mutation")
mut(s.expand((dp-ps)+(dq-qs)-(dp+dq-ps-qs+1))!=0,"Rees exponent mutation")

# Homogeneous constant-bracket support and transformations.
pairs=0
for p in range(1,BOUND+1):
 for q in range(p,BOUND+1):
  if math.gcd(p,q)!=1:continue
  pairs+=1
  if p<q:
   req(mons(p,q,p)==[(1,0)],"degree-p support")
   req(mons(p,q,q)==([(q,0),(0,1)] if p==1 else [(0,1)]),"degree-q support")
  else:req((p,q)==(1,1) and mons(p,q,1)==[(1,0),(0,1)],"equal support")
a,b,h=s.symbols("a b h",nonzero=True); qt=5
A=a*x; B=b*y+h*x**qt; phix=x/a; phiy=(y-h*(x/a)**qt)/b
req(s.expand(A.subs({x:phix,y:phiy},simultaneous=True)-x)==0,"inverse A")
req(s.expand(B.subs({x:phix,y:phiy},simultaneous=True)-y)==0,"inverse B")
req(s.expand(J(phix,phiy)-1/(a*b))==0 and wdeg(phiy,1,qt)==qt,"filtered inverse")
req(s.expand(a*b*J(phix,phiy)-1)==0,"compensation")
req(s.expand(J(Q,-P)-J(P,Q))==0,"signed swap"); mut(s.expand(J(Q,P)+J(P,Q))==0,"unsigned swap")
c=s.Symbol("c",nonzero=True); z=s.Symbol("z")
req(s.expand(J(P,c*Q)-c*J(P,Q))==0,"target scale determinant")
mut(s.expand(J(P,2*Q)-J(P,Q))!=0,"uncompensated scaling")
req(s.expand(J(P,Q-(z**4-2*z**2+3*z).subs(z,P))-J(P,Q))==0,"triangular target")
probe=2*x**4*y**3+7*x*y**5+11
req(wdeg(probe.subs({x:y,y:-x},simultaneous=True),5,2)==wdeg(probe,2,5),"source swap")
H=x**2+y; f=2*H**3; g=-3*H**5
req(J(f,g)==0 and s.cancel(g**6/f**10-s.Rational(729,1024))==0,"common powers")
Pd=x; Qd=5*x**3+y; before=wdeg(Qd,1,2); after=wdeg(Qd-5*Pd**3,1,2)
req(after<before and J(Pd,Qd-5*Pd**3)==J(Pd,Qd),"complete descent")
mut(wdeg(Qd-4*Pd**3,1,2)==before,"partial descent"); req(mons(3,7,-1)==[],"negative layer")

# Generate all no-descent systems from supports, not an allowlist.
def inconsistent(p,q,k,ai,chart):
 bi=k-ai; dP=p+ai; dQ=q+bi; r=math.gcd(dP,dQ); m=dP//r; n=dQ//r; hs=mons(p,q,r)
 H=0; vs=[]
 for j,(ix,iy) in enumerate(hs):
  u=1 if j==chart else s.Symbol(f"h{j}"); H+=u*x**ix*y**iy
  if u!=1:vs.append(u)
 A,B,C,Z=s.symbols("A B C Z"); vs += [A,B,C,Z]; PL=[]; QL=[]; tag=f"{p}_{q}_{k}_{ai}_{chart}"
 for i in range(k):
  if i==0:e,cs=A*H**m,[]
  elif i==ai:e,cs=x,[]
  else:e,cs=gen("P",p,q,dP-i,f"{tag}_{i}")
  PL.append(s.expand(e)); vs+=cs
 for j in range(k):
  if j==0:e,cs=B*H**n,[]
  elif j==bi:e,cs=C*y,[]
  else:e,cs=gen("Q",p,q,dQ-j,f"{tag}_{j}")
  QL.append(s.expand(e)); vs+=cs
 eq=[]
 for nst in range(k):eq += coeffs(sum(J(PL[i],QL[nst-i]) for i in range(nst+1)))
 eq.append(Z*A*B*C-1); uv=[]
 for v0 in vs:
  if v0 not in uv:uv.append(v0)
 G=s.groebner(eq,*uv,order="grevlex")
 return any(z.as_expr().is_number and z.as_expr()!=0 for z in G.polys),len(eq),len(uv)
summary=defaultdict(set); systems=charts=0; maxeq=maxvar=0
for p in range(1,BOUND+1):
 for q in range(p,BOUND+1):
  if math.gcd(p,q)!=1:continue
  for k in range(2,5):
   for ai in range(1,k):
    bi=k-ai; dP=p+ai; dQ=q+bi; r=math.gcd(dP,dQ); m=dP//r; n=dQ//r; hs=mons(p,q,r)
    if m<2 or n<2 or not hs:continue
    systems+=1; summary[(k,ai)].add(p)
    for chart in range(len(hs)):
     charts+=1; ok,ne,nv=inconsistent(p,q,k,ai,chart); maxeq=max(maxeq,ne); maxvar=max(maxvar,nv)
     req(ok,f"formal model survived {(p,q,k,ai,chart)}")
expected={(2,1):{1},(3,1):{1},(3,2):{1,2},(4,1):{1},(4,2):{1},(4,3):{1,3}}
req(dict(summary)==expected and pairs==1966 and systems==317 and charts==319,"support census")

# Exceptional equations and semantic corruptions.
A,B,C,u,v,e,f=s.symbols("A B C u v e f")
P0=A*x**3; Q0=B*x**4; P1=u*x**2+v*y; Q1=e*x**3+f*x*y
S1=J(P0,Q1)+J(P1,Q0); W=J(P1,Q1); S2=J(P0,C*y)+W+J(x,Q0)
req(s.expand(S1-(3*A*f-4*B*v)*x**3)==0,"central S1")
req(s.expand(W-((2*u*f-3*v*e)*x**2-v*f*y))==0,"central W")
req(s.expand(S2-((3*A*C+2*u*f-3*v*e)*x**2-v*f*y))==0,"central S2")
mut(J(P0,C*y)-W+J(x,Q0)!=S2,"middle sign")
model={A:2,B:5,C:3,u:0,v:7,e:s.Rational(6,7),f:0}
req(J(P0,Q0).subs(model)==0 and s.expand(S2.subs(model))==0,"central-only control")
mut(s.expand(S1.subs(model))==-140*x**3,"omitted S1")
r0,s0,g0=s.symbols("r s g")
P0x=A*x**4; Q0x=B*x**3; P1x=u*x**3+v*x*y; P2x=r0*x**2+s0*y; Q2x=g0*x
T1=J(P0x,C*y)+J(P1x,Q0x); T2=J(P0x,Q2x)+J(P1x,C*y)+J(P2x,Q0x)
req(s.expand(T1-(4*A*C-3*B*v)*x**3)==0,"(3,1) S1")
req(s.expand(T2-((3*C*u-3*B*s0)*x**2+C*v*y))==0,"(3,1) S2")
req(s.Poly(T2.subs({r0:0,s0:0}),x,y).coeff_monomial(y)==C*v,"missing P2")
req(s.Poly(T2.subs(g0,0),x,y).coeff_monomial(y)==C*v,"missing Q2")
mut(s.Poly(T2.subs(v,0),x,y).coeff_monomial(y)==0,"omitted xy support")
er=random.Random(0x17D4)
for i in range(EXCEPTION_TRIALS):
 nz=[j for j in range(-7,8) if j]; sub={A:er.choice(nz),B:er.choice(nz),C:er.choice(nz),u:er.randint(-7,7),v:er.randint(-7,7),e:er.randint(-7,7),f:er.randint(-7,7),r0:er.randint(-7,7),s0:er.randint(-7,7),g0:er.randint(-7,7)}
 req(not(s.expand(S1.subs(sub))==0 and s.expand(S2.subs(sub))==0),"random central solution")
 req(not(s.expand(T1.subs(sub))==0 and s.expand(T2.subs(sub))==0),"random (3,1) solution")
print(f"review mode: {MODE}\nreviewed candidate: {SHA}\nexact assertions: {N}\nsemantic mutations detected: {M}")
print(f"random exact Rees/Keller trials: {REES_TRIALS}\nprimitive weights enumerated (1 <= p <= q <= {BOUND}): {pairs}")
print(f"generated no-descent formal systems: {systems}\nprojective common-root charts eliminated: {charts}")
print(f"largest generated system: {maxeq} equations, {maxvar} variables\nrandom exceptional coefficient trials: {EXCEPTION_TRIALS}")
print("independent defect-four symbolic validation: PASS\nmathematical authority: HUMAN-READABLE REVIEW, NOT CHECK COUNT")
