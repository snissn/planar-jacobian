#!/usr/bin/env python3
"""Reviewer-owned adversarial checks for defect five.

This script does not import the construction checker. It reconstructs the
weight sieve, selected exceptional coefficient ideals, equal-weight ideals,
normalization determinants, and Rees identity with independent code.
"""
from __future__ import annotations

import math
from collections import Counter

import sympy as s

x, y, t = s.symbols("x y t")


def J(f: s.Expr, g: s.Expr) -> s.Expr:
    return s.expand(s.diff(f, x) * s.diff(g, y) - s.diff(f, y) * s.diff(g, x))


def supp(d: int, p: int, q: int) -> list[tuple[int, int]]:
    if d < 0:
        return []
    return [(i, j) for j in range(d // q + 1) for i in [(d - q * j) // p]
            if d - q * j >= 0 and p * i + q * j == d]


def unit_ideal(eqs: list[s.Expr], vars_: list[s.Symbol], nz: s.Expr) -> tuple[int, int]:
    z = s.Symbol("z_sat")
    G = s.groebner([s.expand(e) for e in eqs] + [z * nz - 1], *vars_, z, order="grevlex")
    assert any(g.as_expr() == 1 for g in G.polys)
    return len(eqs) + 1, len(vars_) + 1


def coeffs(exprs: list[s.Expr], X=x, Y=y) -> list[s.Expr]:
    out: list[s.Expr] = []
    for e in exprs:
        out += [s.expand(c) for _, c in s.Poly(s.expand(e), X, Y).terms() if c]
    return out


def sieve_scan(limit: int = 160) -> tuple[int, int, Counter[str]]:
    weights = descent = 0
    families: Counter[str] = Counter()
    for p in range(1, limit + 1):
        for q in range(p, limit + 1):
            if math.gcd(p, q) != 1:
                continue
            weights += 1
            for a in range(1, 5):
                b = 5 - a
                dp, dq = p + a, q + b
                rho = math.gcd(dp, dq)
                m, n = dp // rho, dq // rho
                if m == 1 or n == 1:
                    descent += 1
                    continue
                if not supp(rho, p, q):
                    continue
                assert p <= a
                if p == q:
                    assert (p, q) == (1, 1)
                    families[f"equal-{a}"] += 1
                    continue
                # Any y-monomial in a no-descent root would give 2q<=p+a.
                assert all(j == 0 for _, j in supp(rho, p, q))
                assert a % p == 0 and (q + b) % p == 0
                if a == 1:
                    assert p == 1 and q >= 3 and q % 2 == 1
                    families["a1"] += 1
                elif a == 2:
                    assert (p == 1 and q >= 2 and q % 3 != 0) or (p == 2 and q % 4 == 3)
                    families[f"a2-p{p}"] += 1
                elif a == 3:
                    assert (p == 1 and q >= 3 and q % 4 != 2) or (p == 3 and q >= 7 and q % 6 == 1)
                    families[f"a3-p{p}"] += 1
                else:
                    assert ((p == 1 and q >= 2 and q % 5 != 4)
                            or (p == 2 and q % 2 == 1 and q % 3 != 2)
                            or (p == 4 and q >= 11 and q % 8 == 3))
                    families[f"a4-p{p}"] += 1
    return weights, descent, families


def exceptional_ideals() -> list[tuple[str, list[s.Expr], list[s.Symbol], s.Expr]]:
    A, B, c = s.symbols("A B c")
    systems = []

    # (2,3), weight (1,2), built from complete layers.
    u, v, e, f, g, r, ss, k = s.symbols("u v e f g r ss k")
    P = [A*x**3, u*x**2+v*y, x, 0, 0, 0]
    Q = [B*x**5, e*x**4+f*x**2*y+g*y**2, r*x**3+ss*x*y, c*y, k*x, 0]
    E = [sum((J(P[i], Q[n-i]) for i in range(n+1)), s.Integer(0)) - (1 if n == 5 else 0) for n in range(6)]
    systems.append(("a2-1-2", coeffs(E), [A,B,c,u,v,e,f,g,r,ss,k], A*B*c))

    # (2,3), weight (2,3).
    v, f, r, k = s.symbols("v f r k")
    P = [A*x**2, v*y, x, 0, 0, 0]
    Q = [B*x**2, f*x*y, r*x**2, c*y, k*x, 0]
    E = [sum((J(P[i], Q[n-i]) for i in range(n+1)), s.Integer(0)) - (1 if n == 5 else 0) for n in range(6)]
    systems.append(("a2-2-3", coeffs(E), [A,B,c,v,f,r,k], A*B*c))

    # (3,2), weight (1,3).
    u,v,r,e,f,ss,k = s.symbols("u v r e f ss k")
    P = [A*x**4, u*x**3+v*y, r*x**2, x, 0, 0]
    Q = [B*x**5, e*x**4+f*x*y, c*y, ss*x**2, k*x, 0]
    E = [sum((J(P[i], Q[n-i]) for i in range(n+1)), s.Integer(0)) - (1 if n == 5 else 0) for n in range(6)]
    systems.append(("a3-1-3", coeffs(E), [A,B,c,u,v,r,e,f,ss,k], A*B*c))

    # (4,1), weights (1,2), (1,3), (2,3).
    u,v,w,r,ss,z,tt,k = s.symbols("u v w r ss z tt k")
    P = [A*x**5, u*x**4+v*x**2*y+w*y**2, r*x**3+ss*x*y, z*x**2+tt*y, x, 0]
    Q = [B*x**3, c*y, k*x, 0, 0, 0]
    E = [sum((J(P[i], Q[n-i]) for i in range(n+1)), s.Integer(0)) - (1 if n == 5 else 0) for n in range(6)]
    systems.append(("a4-1-2", coeffs(E), [A,B,c,u,v,w,r,ss,z,tt,k], A*B*c))

    u,v,r,tt,z,k,ell = s.symbols("u v r tt z k ell")
    P = [A*x**5, u*x**4+v*x*y, r*x**3+tt*y, z*x**2, x, 0]
    Q = [B*x**4, c*y, k*x**2, ell*x, 0, 0]
    E = [sum((J(P[i], Q[n-i]) for i in range(n+1)), s.Integer(0)) - (1 if n == 5 else 0) for n in range(6)]
    systems.append(("a4-1-3", coeffs(E), [A,B,c,u,v,r,tt,z,k,ell], A*B*c))

    v,r,tt,k = s.symbols("v r tt k")
    P = [A*x**3, v*x*y, r*x**2, tt*y, x, 0]
    Q = [B*x**2, c*y, k*x, 0, 0, 0]
    E = [sum((J(P[i], Q[n-i]) for i in range(n+1)), s.Integer(0)) - (1 if n == 5 else 0) for n in range(6)]
    systems.append(("a4-2-3", coeffs(E), [A,B,c,v,r,tt,k], A*B*c))
    return systems


def equal_ideals() -> list[tuple[str, list[s.Expr], list[s.Symbol], s.Expr]]:
    X,Y = s.symbols("X Y")
    def K(f,g): return s.expand(s.diff(f,X)*s.diff(g,Y)-s.diff(f,Y)*s.diff(g,X))
    def cxy(es): return coeffs(es, X, Y)
    out=[]

    A,B,l,ss,m,n = s.symbols("A B l ss m n")
    aa=s.symbols("a0:5"); bb=s.symbols("b0:4"); dd=s.symbols("d0:3")
    L=l*X+ss*Y; M=m*X+n*Y
    Q1=sum(aa[i]*X**(4-i)*Y**i for i in range(5))
    Q2=sum(bb[i]*X**(3-i)*Y**i for i in range(4))
    Q3=sum(dd[i]*X**(2-i)*Y**i for i in range(3))
    E=[K(A*X**2,Q1)+K(L,B*X**5),K(A*X**2,Q2)+K(L,Q1),K(A*X**2,Q3)+K(L,Q2),K(A*X**2,M)+K(L,Q3)]
    out.append(("equal-a1",cxy(E),[A,B,l,ss,m,n,*aa,*bb,*dd],A*B*K(L,M)))

    A,B,a,b,d,e,u,v,w,l,ss,m,n=s.symbols("A B a b d e u v w l ss m n")
    P1=a*X**2+b*X*Y; Q1=d*X**3+e*X**2*Y; Q2=u*X**2+v*X*Y+w*Y**2
    L=l*X+ss*Y; M=m*X+n*Y
    E=[K(A*X**3,Q1)+K(P1,B*X**4),K(A*X**3,Q2)+K(P1,Q1)+K(L,B*X**4),K(A*X**3,M)+K(P1,Q2)+K(L,Q1),K(P1,M)+K(L,Q2),K(L,M)-1]
    out.append(("equal-a2",cxy(E),[A,B,a,b,d,e,u,v,w,l,ss,m,n],A*B))
    return out


def transformation_and_rees_checks() -> int:
    u,v=s.symbols("u v")
    psi=(2*x,3*y+5*x**2)
    phi=(u/2,(v-5*(u/2)**2)/3)
    assert J(*psi)==6
    det=s.det(s.Matrix([[s.diff(phi[0],u),s.diff(phi[0],v)],[s.diff(phi[1],u),s.diff(phi[1],v)]]))
    assert s.simplify(6*det)==1
    assert J(y,-x)==1 and J(y,x)==-1
    pairs=[(x+y**2,y+(x+y**2)**3),(x+2*y**3,y-3*(x+2*y**3)**2)]
    tests=0
    for P,Q in pairs:
        assert J(P,Q)==1
        for p,q in [(1,1),(1,2),(2,3),(3,5)]:
            def wd(F): return max(p*i+q*j for (i,j),coef in s.Poly(F,x,y).terms() if coef)
            dp,dq=wd(P),wd(Q); kap=dp+dq-p-q
            Pc=s.expand(t**dp*P.subs({x:t**(-p)*x,y:t**(-q)*y}, simultaneous=True))
            Qc=s.expand(t**dq*Q.subs({x:t**(-p)*x,y:t**(-q)*y}, simultaneous=True))
            assert s.expand(J(Pc,Qc)-t**kap)==0
            tests+=1
    return tests


def main() -> int:
    weights, descents, families=sieve_scan()
    groebners=0; largest=(0,0)
    for _,eqs,vars_,nz in exceptional_ideals()+equal_ideals():
        size=unit_ideal(eqs,vars_,nz); groebners+=1; largest=max(largest,size)
    rees=transformation_and_rees_checks()
    print("review mode: local-adversarial-review")
    print(f"primitive weights re-enumerated (<=160): {weights}")
    print(f"exponent-one descents reclassified: {descents}")
    print(f"nonempty no-descent family labels: {len(families)}")
    print(f"independent saturated ideals eliminated: {groebners}")
    print(f"largest reviewer ideal: {largest[0]} equations, {largest[1]} variables")
    print(f"independent Rees/normalization trials: {rees}")
    print("adversarial review checker: PASS")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
