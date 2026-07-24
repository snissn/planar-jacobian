# Reviewer-Selected Case Table — Root-Degree Organization

> **Review mode:** `independent-review`
> **Reviewed commit:** `96fc7ec34bd3b685a0edeae7ecd4404abab7e2f1`
> **Disposition:** `ACCEPT`

This table is generated from the reviewer’s organizing lemma rather than the
candidate’s case split.

After source-weight orientation take `p<=q`. For a selected interior resonant
position `(a,b)`, use the determinant-one target swap when needed and normalize

```text
P_a=x,  Q_b=c y,
d_P=p+a,  d_Q=q+b,
c!=0.
```

The top stair gives `P_0=A H^m`, `Q_0=B H^n`. Exact target descent handles
`m=1` or `n=1`. In a no-descent case `m,n>=2`; since `deg_w H>=p`,

```text
p+a=m deg_w(H)>=2p,
so p<=a.
```

Zero layers are allowed in every row. “Earlier stairs” means equations
`S_n=0` with `n<kappa`, not merely the resonant equation.

## Universal rows

| Situation | Exact conclusion |
|---|---|
| Nonzero resonant endpoint | The normalized top component is a full polynomial coordinate; the Keller equation makes the other component triangular. |
| Top common-power exponent one | A determinant-one triangular target automorphism cancels the complete top layer and strictly lowers the actual integer defect. |
| Equal top degrees and dependent top forms | A determinant-one linear shear cancels one complete top layer. |
| Reversed component-degree orientation | `(P,Q)->(Q,-P)`; positions `(a,b)` and `(b,a)` are exchanged. |
| `p>q` | Source swap `(x,y)->(y,-x)` with weight relabeling; `kappa` is unchanged. |

## Defects zero through three

| Defect / offset | No-descent weights left by `p<=a` | Complete support consequence | Earlier stairs used | Disposition |
|---|---|---|---|---|
| `kappa=0` | none | unique resonant pair touches both top layers | `S_0=1` | endpoint automorphism |
| `kappa=1` | none | both positions are endpoints | `S_1=1` | endpoint automorphism |
| `kappa=2`, `a=1` | `p=1`, `q>1` after equal-top removal | `P_0=A x^2`, `Q_0=B x^(q+1)` | `S_1=2Acx` | impossible |
| `kappa=3`, `a=1`, `q>1` | `p=1` | `P_0=A x^2`, `Q_0=B x^(q+2)`, `P_2` constant | `S_1` gives `(Q_1)_y=0`; `S_2=2Acx` | impossible |
| `kappa=3`, `a=1`, `q=1` | `(1,1)` | `P_0=A(ux+vy)^2`, `Q_0=B(ux+vy)^3` | two preceding stairs; coefficients `3Bv^3`, then `-4A^2cu^4` | impossible |
| `kappa=3`, `a=2`, `p=1`, `q>2` | `p=1` | pure `x` top powers; `P_1 in C x^2` | `S_1=3Acx^2` | impossible |
| `kappa=3`, `a=2`, `(p,q)=(1,2)` | — | equal top degree three | `S_0` | linear descent |
| `kappa=3`, `a=2`, `p=2` | surviving no-descent weights have `q>=5` | `P_0=A x^2`, `P_1 in R_3=0` | `S_1=2Acx` | impossible; `(2,3)` descends |
| `kappa=3`, `a=2`, `q=p=1` | `(1,1)` | `P_0=A(ux+vy)^3`, `Q_0=B(ux+vy)^2` | two preceding stairs; coefficients `3Acu^3`, then `-4B^2v^4/c` | impossible |

## Defect four

| Position / offset | No-descent weights left | Complete support consequence | Earlier stairs used | Disposition |
|---|---|---|---|---|
| `(1,3)`, `a=1` | `p=1`; equal weights descend | in every remaining case `P_0=A x^2`, `Q_0=B x^(q+3)`, `P_2` constant, `P_3=0` | `S_1`: `(Q_1)_y=0`; `S_2`: `(Q_2)_y=0`; `S_3=2Acx` | impossible |
| `(2,2)`, equal weights | `(1,1)` | top degree-three forms proportional | `S_0` | linear descent |
| `(2,2)`, zero middle Wronskian | any unequal no-descent case | `P_0=A H^m`, `Q_0=B H^n`, `n>m>=2` | central preceding stair forces `H|H_x` | impossible |
| `(2,2)`, nonzero Wronskian, `p>1` | support forces `(p,q)=(2,3)` | `P_1` and `Q_1` supports force the weight; `P_0=A x^2`, `Q_0=Bxy` | `S_0=J(P_0,Q_0)=2ABx^2` | impossible |
| `(2,2)`, `p=1`, `q>2` | pure `x` top powers | `P_1=u x^2`, `Q_1=e x^(q+1)+fxy` | `S_1=3Af x^3` gives `f=0`; Wronskian then zero; central contradiction | impossible |
| `(2,2)`, `(p,q)=(1,2)` | exceptional finite support | `P_1=u x^2+vy`, `Q_1=e x^3+fxy` | `3Af=4Bv`; `(3Ac+2uf-3ve)x^2-vfy=0` | `vf=0`, then `v=f=0`, then `3Ac=0`; impossible |
| `(3,1)`, `p=1`, `q>3` | pure `x` top powers | `P_1 in Cx^3` | `S_1=4Acx^3` | impossible; equal/proportional top cases descend |
| `(3,1)`, `(p,q)=(1,2)` | exceptional finite support | `P_1=u x^3+vxy`, `P_2=r x^2+sy`, `Q_2=gx` | `4Ac=3Bv`; `S_2=(3cu-3Bs)x^2+cvy` | `v!=0`, so `cvy` is impossible |
| `(3,1)`, `p=2` | none | root degree must divide `5` and be at least `2`; only `5` remains, giving exponent one | common-root degree | descent or no case |
| `(3,1)`, `p=3` | `q=5` descends; remaining no-descent weights have `q>=8` | `P_0=A x^2`, `P_1 in R_5=0` | `S_1=2Acx` | impossible |

## Completeness certificate

For `kappa<=4`, every nonzero resonant term is either an endpoint or one of the
listed interior offsets. The root-degree inequality excludes all larger `p`.
The source and target swaps cover both source-weight orders and both component
degree orientations. The equations use generic complete homogeneous layers, so
simultaneous resonances and absent layers are included rather than treated as
separate assumptions.
