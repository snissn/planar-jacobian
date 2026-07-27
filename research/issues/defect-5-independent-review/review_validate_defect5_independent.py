#!/usr/bin/env python3
"""Independent exact checker for the fixed-weight defect-five review.

It imports neither defect-five checker and uses no candidate case allowlist.
Weighted supports, all stairs, saturations, orientations, and mutations are
regenerated from definitions.  The bounded scan is falsification evidence; the
human review proves the unbounded support classification.
"""
from __future__ import annotations

import argparse, json, math, time
from pathlib import Path
import sympy as s

CANDIDATE = "2eeb36d232366d124b5a66774b29769ec1eba43d"
x, y, t = s.symbols("x y t")


def J(f, g):
    return s.expand(s.diff(f, x) * s.diff(g, y) - s.diff(f, y) * s.diff(g, x))


def support(d, p, q):
    if d < 0:
        return []
    return [((d - q*j)//p, j) for j in range(d//q + 1) if (d - q*j) >= 0 and (d - q*j) % p == 0]


def piece(name, d, p, q, variables):
    terms = []
    for i, j in support(d, p, q):
        z = s.Symbol(f"{name}_{i}_{j}")
        variables.append(z)
        terms.append(z*x**i*y**j)
    return s.Add(*terms) if terms else s.Integer(0)


def coeffs(f, X=x, Y=y):
    f = s.expand(f)
    return [] if f == 0 else [s.expand(c) for _, c in s.Poly(f, X, Y).terms() if c]


def wd(f, p, q):
    f = s.expand(f)
    return -10**9 if f == 0 else max(p*i + q*j for (i, j), c in s.Poly(f, x, y).terms() if c)


def mono(f, i, j, X=x, Y=y):
    return s.Poly(s.expand(f), X, Y).coeff_monomial(X**i*Y**j)


def arithmetic(p, q, a):
    b = 5-a; dp = p+a; dq = q+b; rho = math.gcd(dp, dq)
    return dict(p=p, q=q, a=a, b=b, dp=dp, dq=dq, rho=rho,
                m=dp//rho, n=dq//rho, hs=support(rho, p, q))


def build(case, chart=0):
    p,q,a,b,dp,dq,m,n = [case[k] for k in ("p","q","a","b","dp","dq","m","n")]
    variables=[]; h=[]
    for k,(i,j) in enumerate(case["hs"]):
        z=s.Integer(1) if k==chart else s.Symbol(f"h_{i}_{j}")
        if k != chart: variables.append(z)
        h.append(z*x**i*y**j)
    H=s.Add(*h); A,B,c=s.symbols("A B c"); variables += [A,B,c]
    P=[]; Q=[]
    for i in range(6):
        P.append(A*H**m if i==0 else x if i==a else piece(f"P{i}",dp-i,p,q,variables))
        Q.append(B*H**n if i==0 else c*y if i==b else piece(f"Q{i}",dq-i,p,q,variables))
    stairs=[]; equations=[]
    for k in range(6):
        E=s.expand(sum((J(P[i],Q[k-i]) for i in range(k+1)),s.Integer(0))-(1 if k==5 else 0))
        stairs.append(E); equations += coeffs(E)
    return dict(case=case,P=P,Q=Q,S=stairs,eq=equations,var=variables,A=A,B=B,c=c)


def unit_ideal(equations, variables, nonzero):
    equations=[s.expand(e) for e in equations if s.expand(e)!=0]
    used=set(nonzero.free_symbols)
    for e in equations: used |= e.free_symbols
    variables=[v for v in dict.fromkeys(variables) if v in used]
    z=s.Symbol("review_saturation")
    G=s.groebner([*equations,z*nonzero-1],*variables,z,order="grevlex")
    assert any(g.as_expr()==1 for g in G.polys), "formal system survived"
    return len(equations)+1,len(variables)+1


def check_unbounded(c):
    if c["m"]==1 or c["n"]==1 or not c["hs"]: return
    p,q,a,b=c["p"],c["q"],c["a"],c["b"]
    if p==q:
        assert (p,q)==(1,1); return
    assert p<=a and all(j==0 for _,j in c["hs"]) and c["rho"]<q
    assert a%p==0 and (q+b)%p==0
    if a==1: assert p==1 and q>=3 and q%2==1
    elif a==2 and p==1: assert q>=2 and q%3!=0
    elif a==2 and p==2: assert q%4==3
    elif a==3 and p==1: assert q>=3 and q%4!=2
    elif a==3 and p==3: assert q>=7 and q%6==1
    elif a==4 and p==1: assert q>=2 and q%5!=4
    elif a==4 and p==2: assert q%2==1 and q%3!=2
    elif a==4 and p==4: assert q>=11 and q%8==3
    else: raise AssertionError(c)


def equal_a1():
    A,B,l,r,m,n=s.symbols("A B l r m n"); variables=[A,B,l,r,m,n]
    L=l*x+r*y; M=m*x+n*y
    P=[A*x**2,L,piece("EA1P2",0,1,1,variables),0,0,0]
    Q=[B*x**5,piece("EA1Q1",4,1,1,variables),piece("EA1Q2",3,1,1,variables),
       piece("EA1Q3",2,1,1,variables),M,piece("EA1Q5",0,1,1,variables)]
    E=[]
    for k in range(6): E += coeffs(sum((J(P[i],Q[k-i]) for i in range(k+1)),s.Integer(0))-(1 if k==5 else 0))
    return E,variables,A*B*J(L,M)


def equal_a2():
    A,B,a,b,g,E=s.symbols("A B a b g E")
    P1=a*x**2+b*x*y+g*y**2
    Q1=s.Rational(4,3)*B/A*x*P1+E*x**3
    assert s.simplify(mono(J(P1,Q1),0,3)+s.Rational(8,3)*B*g**2/A)==0
    d,e,u,v,w,l,r,m,n=s.symbols("d e u v w l r m n")
    P1=a*x**2+b*x*y; Q1=d*x**3+e*x**2*y; Q2=u*x**2+v*x*y+w*y**2
    L=l*x+r*y; M=m*x+n*y
    P=[A*x**3,P1,L,0,0,0]; Q=[B*x**4,Q1,Q2,M,0,0]
    equations=[]
    for k in range(6): equations += coeffs(sum((J(P[i],Q[k-i]) for i in range(k+1)),s.Integer(0))-(1 if k==5 else 0))
    return equations,[A,B,a,b,d,e,u,v,w,l,r,m,n],A*B


def sub(f,X,Y):
    u,v=s.symbols("review_u review_v")
    return s.expand(f.subs({x:u,y:v},simultaneous=True).subs({u:X,v:Y},simultaneous=True))


def mutations():
    count=0
    plus=lambda f,g:s.expand(s.diff(f,x)*s.diff(g,y)+s.diff(f,y)*s.diff(g,x))
    assert J(y,x)==-1 and plus(y,x)==1; count+=1
    P=x+y**2; Q=y
    assert J(Q,P)==-1 and J(Q,-P)==1; count+=1
    u,v=s.symbols("u v"); psi=(2*x,3*y+5*x**2); c=J(*psi)
    phi=(u/2,(v-5*(u/2)**2)/3)
    D=s.Matrix([[s.diff(phi[0],u),s.diff(phi[0],v)],[s.diff(phi[1],u),s.diff(phi[1],v)]]).det()
    assert c==6 and s.simplify(c*D)==1 and D!=1; count+=1
    for d in range(17):
        f=sum((1+i+3*j)*x**i*y**j for i,j in support(d,1,2))
        if f: assert all(i+2*j==d for (i,j),z in s.Poly(sub(f,x/2,(y-5*(x/2)**2)/3),x,y).terms() if z)
    assert {i+2*j for (i,j),z in s.Poly(sub(y,x,y+x),x,y).terms() if z}=={1,2}; count+=1
    P=x+y**2; Q=y+P**3; dp,dq=wd(P,1,2),wd(Q,1,2); k=dp+dq-3
    Pc=s.expand(t**dp*P.subs({x:t**-1*x,y:t**-2*y},simultaneous=True))
    Qc=s.expand(t**dq*Q.subs({x:t**-1*x,y:t**-2*y},simultaneous=True))
    assert J(Pc,Qc)==t**k and J(Pc,Qc)!=t**(k+1); count+=1
    P=x+y+1; Q=P**2+y
    assert J(P,Q)==1 and wd(Q-P**2,1,1)==1 and wd(Q-x**2,1,1)==2; count+=1
    f=x**3+x*y; assert wd(sub(f,y,-x),2,1)==wd(f,1,2) and J(y,-x)==1; count+=1
    z=build(arithmetic(1,2,2)); v0=mono(z["P"][1],0,1); k0=mono(z["Q"][4],1,0)
    assert s.expand(z["S"][5]-(z["c"]-v0*k0-1))==0; count+=1
    z=build(arithmetic(2,3,2)); assert wd(z["Q"][0],2,3)==z["case"]["dq"]==6
    assert wd(z["B"]*x**2,2,3)==4; count+=1
    return count


def swap_checks():
    L=x+2*y; M=3*x+7*y
    P=[x**2,L,0,0,0,0]; Q=[x**5,x**4,x**3,x**2,M,0]
    Ps,Qs=Q,[-f for f in P]
    assert J(Ps[4],Qs[1])==J(P[1],Q[4])
    for k in range(6):
        assert s.expand(sum((J(P[i],Q[k-i]) for i in range(k+1)),s.Integer(0))-
                        sum((J(Ps[i],Qs[k-i]) for i in range(k+1)),s.Integer(0)))==0
    return 2


def keller_trials():
    r=s.sqrt(2)
    pairs=[(x+y**2,y+(x+y**2)**3),(x+2*y**3,y-3*(x+2*y**3)**2),
           (x+r*y**2,y+r/2*(x+r*y**2)**2)]
    weights=[(1,1),(1,2),(2,3),(3,5),(4,7)]; out=0
    for P,Q in pairs:
        assert J(P,Q)==1
        for p,q in weights:
            dp,dq=wd(P,p,q),wd(Q,p,q); k=dp+dq-p-q
            Pc=s.expand(t**dp*P.subs({x:t**-p*x,y:t**-q*y},simultaneous=True))
            Qc=s.expand(t**dq*Q.subs({x:t**-p*x,y:t**-q*y},simultaneous=True))
            assert J(Pc,Qc)==t**k; out+=1
    return out


def run(limit):
    start=time.time(); R=dict(primitive_weights=0,exponent_one_descents=0,empty_root_obstructions=0,
        no_descent_cases=0,projective_charts=0,unequal_saturated_ideals=0,equal_saturated_ideals=0,
        zero_layers=0,multiple_resonance_systems=0,formal_survivors=0)
    families=set(); largest=(0,0)
    for p in range(1,limit+1):
      for q in range(p,limit+1):
       if math.gcd(p,q)!=1: continue
       R["primitive_weights"]+=1
       for a in range(1,5):
        c=arithmetic(p,q,a)
        if c["m"]==1 or c["n"]==1: R["exponent_one_descents"]+=1; continue
        if not c["hs"]: R["empty_root_obstructions"]+=1; continue
        R["no_descent_cases"]+=1; check_unbounded(c); families.add((a,p,c["rho"]))
        if p==q: continue
        for chart in range(len(c["hs"])):
            R["projective_charts"]+=1; z=build(c,chart)
            R["zero_layers"]+=sum(f==0 for f in [*z["P"],*z["Q"]])
            if sum(J(z["P"][i],z["Q"][5-i])!=0 for i in range(6))>1: R["multiple_resonance_systems"]+=1
            for i in range(6):
              for j in range(6):
                if i+j>5: assert J(z["P"][i],z["Q"][j])==0
            largest=max(largest,unit_ideal(z["eq"],z["var"],z["A"]*z["B"]*z["c"]))
            R["unequal_saturated_ideals"]+=1
    for E,V,N in (equal_a1(),equal_a2()):
        largest=max(largest,unit_ideal(E,V,N)); R["equal_saturated_ideals"]+=1
    R.update(review_mode="independent-review",reviewed_candidate=CANDIDATE,max_weight=limit,
             family_signatures=len(families),largest_ideal_equations=largest[0],largest_ideal_variables=largest[1],
             semantic_mutations_detected=mutations(),orientation_swap_checks=swap_checks(),
             exact_keller_rees_trials=keller_trials(),elapsed_seconds=round(time.time()-start,3),status="PASS",
             authority="bounded falsification evidence; human reconstruction proves unbounded closure")
    return R


def output(R):
    labels=[("primitive weights enumerated (1 <= p <= q <= %s)"%R["max_weight"],"primitive_weights"),
      ("exponent-one descents reclassified","exponent_one_descents"),("empty common-root supports rejected","empty_root_obstructions"),
      ("supported no-descent arithmetic cases","no_descent_cases"),("unequal projective charts eliminated exactly","projective_charts"),
      ("unequal saturated ideals","unequal_saturated_ideals"),("equal-weight saturated ideals","equal_saturated_ideals"),
      ("derived family signatures (a,p,rho)","family_signatures"),("zero layers generated","zero_layers"),
      ("systems with multiple possible resonant brackets","multiple_resonance_systems")]
    print("review mode:",R["review_mode"]); print("reviewed candidate:",R["reviewed_candidate"])
    for label,key in labels: print(f"{label}: {R[key]}")
    print(f"largest saturated input: {R['largest_ideal_equations']} equations, {R['largest_ideal_variables']} variables")
    print("semantic corruptions detected:",R["semantic_mutations_detected"])
    print("source/target orientation checks:",R["orientation_swap_checks"])
    print("exact rational/algebraic Keller-Rees trials:",R["exact_keller_rees_trials"])
    print("formal complete-staircase survivors:",R["formal_survivors"])
    print("independent defect-five review checker: PASS")
    print("mathematical authority: HUMAN RECONSTRUCTION, NOT BOUNDED CHECK COUNTS")


def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--max-weight",type=int,default=64); ap.add_argument("--json",action="store_true"); ap.add_argument("--json-output",type=Path)
    a=ap.parse_args()
    if a.max_weight<8: ap.error("--max-weight must be at least 8")
    R=run(a.max_weight)
    print(json.dumps(R,indent=2,sort_keys=True)) if a.json else output(R)
    if a.json_output: a.json_output.write_text(json.dumps(R,indent=2,sort_keys=True)+"\n")
    return 0

if __name__=="__main__": raise SystemExit(main())
