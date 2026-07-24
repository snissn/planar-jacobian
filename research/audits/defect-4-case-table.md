# Defect-4 Resonance and Weight Case Table

> **Authority:** `MUTABLE_NONAUTHORITATIVE`  
> **Baseline:** `86d1b78cedd788b7335be692f9bb92921142c7d3`  
> **Companion proof:** [`defect-4-staircase-audit.md`](defect-4-staircase-audit.md)

Conventions: `p<=q` after the determinant-one source swap and weight relabeling;
the selected resonant pair is oriented to degrees `(p,q)` by the target swap
`(P,Q)->(Q,-P)` when necessary. `c` denotes its nonzero Jacobian. A zero
intermediate layer is allowed in every row.

## Universal rows

| Selected position | Normalized pair | Top degrees `(alpha,beta)` | Exact disposition |
|---|---|---|---|
| `(0,4)` | `P_0=x`, `Q_4=c y` | `(p,q+4)` | `P` is a coordinate; `F` is triangular after a source coordinate change. |
| `(4,0)` | `P_4=x`, `Q_0=c y` | `(p+4,q)` | `Q` is a coordinate; transpose of the preceding row. |
| any interior | `P_a=x`, `Q_b=c y` | `(p+a,q+b)` | `P_0=aH^m`, `Q_0=bH^n`. If `m=1` or `n=1`, a triangular target shear cancels the top layer and strictly lowers `kappa`. |

## Interior position `(1,3)`

Here `d_P=p+1`, `d_Q=q+3`.

| Weight regime | Complete support consequence | Staircase used | Disposition |
|---|---|---|---|
| `(1,1)` | top degrees `(2,4)`; `Q_0=lambda P_0^2` | `S_0` common-power lemma | target descent |
| `1<p<q` | `P_0!=0` forces `q=p+1`, `P_0=a y`; then `Q_0 in C[y]` and `q|3` | `S_0` | only `(2,3)`, where `Q_0=lambda P_0^2`; otherwise impossible |
| `p=1<q`, exponent-one top power | common-power exponent `m=1` | `S_0` | target descent |
| `p=1<q`, no top descent | `P_0=a x^2`, `Q_0=b x^(q+3)` | `S_1`, `S_2`, `S_3` | `(Q_1)_y=(Q_2)_y=0`, then `S_3=2acx`, impossible |

The last row includes `q=2` and any absent `Q_1,Q_2`.

## Interior position `(2,2)`

Here `d_P=p+2`, `d_Q=q+2`; the central equation is

```text
c(P_0)_x+J(P_1,Q_1)+(Q_0)_y=0.
```

| Weight regime | Complete support consequence | Staircase used | Disposition |
|---|---|---|---|
| `(1,1)` | `P_0,Q_0` proportional of degree `3` | `S_0` | linear target descent |
| `p<q`, no top descent, `J(P_1,Q_1)=0` | `P_0=aH^m`, `Q_0=bH^n`, `n>m>=2` | `S_2` | forces `H|H_x`, impossible |
| `1<p<q`, Wronskian nonzero | `P_1!=0` forces `q=p+1`; `Q_1!=0` forces `p|(q+1)` | support plus `S_0` | only `(2,3)`, but `J(a x^2,bxy)!=0`; impossible |
| `p=1`, `q>2`, no top descent | `P_0=a x^3`, `Q_0=b x^(q+2)`, `P_1=u x^2`, `Q_1=e x^(q+1)+fxy` | `S_1` then `S_2` | `f=0`, hence Wronskian zero, impossible |
| `(p,q)=(1,2)` | `P_1=u x^2+v y`, `Q_1=e x^3+fxy` | `S_1`, `S_2` | `3af=4bv` and `vf=0`; hence `v=f=0`, then `3ac=0`, impossible |

## Interior position `(3,1)`

Here `d_P=p+3`, `d_Q=q+1`.

| Weight regime | Complete support consequence | Staircase used | Disposition |
|---|---|---|---|
| `(1,1)` | top degrees `(4,2)`; `P_0=lambda Q_0^2` | `S_0` | target descent |
| `1<p<q` | `Q_0` pure `x`; dependence makes `P_0` pure `x`; then `p=3` | `S_0` | `q=5` or another exponent-one relation descends; otherwise `P_1 in R_5=0` and `S_1=2acx`, impossible |
| `p=1`, `q>3`, no top descent | `P_0=a x^4`, `Q_0=b x^(q+1)`, `P_1=u x^3` | `S_1` | `S_1=4acx^3`, impossible |
| `p=1`, `q=3` | equal top degrees `4` | `S_0` | linear target descent |
| `(p,q)=(1,2)` | `P_1=u x^3+vxy`, `P_2=e x^2+fy`, `Q_2=gx` | `S_1`, `S_2` | `4ac=3bv`, so `v!=0`; coefficient `cv y` in `S_2` is impossible |

## Reversed degree orientation

If the chosen resonant pair has degrees `(q,p)` rather than `(p,q)`, apply

```text
(P,Q) -> (Q,-P).
```

This operation has determinant one, preserves `J=1`, swaps positions
`(1,3)<->(3,1)`, fixes `(2,2)`, and exchanges the corresponding table rows.
No orientation is omitted.

## Descent certificate

Every descent row uses one of

```text
(P,Q) -> (P,Q-lambda P^N),
(P,Q) -> (P-lambda Q^N,Q),
(P,Q) -> (P,Q-lambda P)
```

with exact top-layer equality. Each has target Jacobian one. The cancelled
component has strictly smaller weighted degree, so the integer

```text
kappa_w=d_P+d_Q-p-q
```

strictly decreases. No row claims descent merely from cancellation inside a
single coefficient equation.
