# Track M — Filtered Equivariance and the Weighted Rees Staircase

> **Authority:** `REVIEWED_SCOPED` only for the pinned positive-weight defect-at-most-four theorem  
> **Reviewed issue:** [#17](https://github.com/snissn/planar-jacobian/issues/17)  
> **Reviewed revision:** `96fc7ec34bd3b685a0edeae7ecd4404abab7e2f1`  
> **Scientific inference:** primitive positive weight and `kappa_w<=4` imply automorphism; no broader inference
> **Defect-five candidate:** issue [#29](https://github.com/snissn/planar-jacobian/issues/29), `CLM-073`; local-adversarial-review only  

## Purpose

Exact nontrivial `G_m`-equivariance is a literature-backed rigidity class for planar Keller maps: T. Shaska states that a `G_m`-equivariant planar Keller map is an automorphism for every sign pattern of the weights (arXiv:2607.20210v1, submitted 2026-07-22).

This track studies whether a general Keller pair can be reduced toward that exact graded case through a weighted Rees filtration. Issue #17 produced a self-contained proof through positive-weight grading defect `4`. An independent review returned `ACCEPT` at the pinned candidate revision, and the mainline freeze record preserves exactly that scope. It does not show that an arbitrary Keller pair has such a small-defect weight.

## 1. Exact weighted Rees staircase

Fix a primitive positive weight `w=(p,q)`. Put

```text
d_P=deg_w P,
d_Q=deg_w Q,
kappa_w=d_P+d_Q-p-q,
P=sum_i P_i,  deg_w P_i=d_P-i,
Q=sum_j Q_j,  deg_w Q_j=d_Q-j.
```

Define

```text
Pcal=t^(d_P)P(t^(-p)x,t^(-q)y)=sum_i t^iP_i,
Qcal=t^(d_Q)Q(t^(-p)x,t^(-q)y)=sum_j t^jQ_j.
```

The chain rule gives exactly

```text
J(Pcal,Qcal)=t^(d_P+d_Q-p-q)J(P,Q)=t^kappa_w.
```

Hence

```text
sum_(i+j=n)J(P_i,Q_j)=0     for n<kappa_w,
sum_(i+j=kappa_w)J(P_i,Q_j)=1.
```

Each individual bracket lies in the homogeneous piece of degree `kappa_w-i-j` (and has that degree when nonzero); therefore every bracket with `i+j>kappa_w` is zero. This sharper no-tail statement is part of CLM-047.

## 2. Resonant normalization

At least one term on the resonant stair has nonzero constant bracket. If

```text
J(P_a,Q_b)=c in C*,
a+b=kappa_w,
```

then the weighted degrees of `P_a,Q_b` are exactly `{p,q}`. In two variables this gives an explicit graded triangular or linear automorphism. Pair its inverse source change with a compensating target determinant so that `J=1` is preserved and the selected layers become

```text
P_a=x,
Q_b=c y.
```

The scalar `c` is retained. The complete transformation proof is in [`../audits/filtered-transformation-catalogue.md`](../audits/filtered-transformation-catalogue.md).

## 3. Exact descent

The top equation `J(P_0,Q_0)=0` gives

```text
P_0=aH^m,
Q_0=bH^n,
gcd(m,n)=1.
```

If `m=1` or `n=1`, an exact triangular target shear cancels one full top layer and strictly lowers the nonnegative integer `kappa_w`. Equal top degrees use a determinant-one linear shear. This is the only descent mechanism used through defect `4`.

A resonant position touching `P_0` or `Q_0` makes that full component a polynomial coordinate and therefore makes the Keller map triangular after a source coordinate change.

## 4. Independently audited defects zero through three

The earlier conversation claim has been rederived without using conversation prose:

```text
kappa_w<=3  =>  F is an automorphism.
```

The interior defect-2 equation reduces to a common-power divisibility contradiction unless a top shear lowers defect. For defect `3`, both positions `(1,2)` and `(2,1)` are treated for equal weights, `p=1<q`, and `1<p<q`, including absent layers. The exact equations are in [`../audits/defect-4-staircase-audit.md`](../audits/defect-4-staircase-audit.md).

This statement is included in the independently reviewed scope bound to `96fc7ec34bd3b685a0edeae7ecd4404abab7e2f1`.

## 5. Defect four

The exact stairs are

```text
S_0=J(P_0,Q_0)=0,
S_1=J(P_0,Q_1)+J(P_1,Q_0)=0,
S_2=J(P_0,Q_2)+J(P_1,Q_1)+J(P_2,Q_0)=0,
S_3=J(P_0,Q_3)+J(P_1,Q_2)+J(P_2,Q_1)+J(P_3,Q_0)=0.
```

Endpoint resonance is already triangular. The three interior positions have the following disposition:

* `(1,3)`: after top-power descent is removed, weighted support forces `p=1`; `S_1,S_2` make the relevant `y` derivatives vanish, while `S_3=2acx`, impossible.
* `(2,2)`: in a no-descent case a zero middle Wronskian would force `H|H_x`. A nonzero Wronskian requires both middle layers. For `p>1` support forces `(p,q)=(2,3)`, contradicting `S_0`. For `p=1,q>2`, `S_1` forces the Wronskian to vanish. For `(1,2)`, exact coefficients give `3af=4bv` and `vf=0`, followed by `3ac=0`, impossible.
* `(3,1)`: the transpose arithmetic forces top descent or an `S_1` support contradiction; the exceptional `(1,2)` row gives a nonzero `cv y` coefficient in `S_2`.

Thus every defect-four case either lowers to a proven smaller defect or is impossible. The complete table is [`../audits/defect-4-case-table.md`](../audits/defect-4-case-table.md).

## 6. Middle-Wronskian conclusion

The term `J(P_1,Q_1)` is not removed by a claimed universal target or source normal form. In fact, same-index `SL_2` target changes preserve it, and graded symplectic source changes pull it back and preserve nonvanishing.

Instead, the full staircase shows that a nonzero middle Wronskian cannot survive all support and preceding-stair constraints in a no-descent defect-four pair. No boundary-monodromy or Newton--Puiseux theorem is needed at this defect.

## 7. Literature boundary

The primary-source audit is [`../audits/defect-4-primary-source-audit.md`](../audits/defect-4-primary-source-audit.md). Shaska, Lee--Li, Karaś, and Pan are recorded at their exact scoped relevance. None supplies a hidden missing implication in the candidate proof.

## 8. Reviewed theorem and nonclaims

The reviewed conclusion is

```text
primitive positive w and kappa_w<=4  =>  F is an automorphism.
```

It does not imply:

* that every Keller map has a positive weight with `kappa_w<=4`;
* that the Rees family preserves generic degree or boundary valuations;
* a reduction at defect `5`;
* or `JC_2`.

## 9. Defect five candidate and successor review

Issue #29 banks the fixed-weight defect-five theorem in [`../issues/defect-5-rees/README.md`](../issues/defect-5-rees/README.md) as `CLM-073` with status `candidate_proved`. The exact candidate `2eeb36d232366d124b5a66774b29769ec1eba43d` received a separate local-adversarial-review `ACCEPT`, not independent acceptance.

Every resonant endpoint is invertible; every interior system either admits complete-top strict descent to `kappa_w<=4` or contradicts the complete staircase. The standard-weight coupled transverse chains are the first new defect-five correction and are not imported from the defect-four middle-Wronskian row.

The successor leaf [`L15-defect-5-staircase.md`](../leaf-packets/L15-defect-5-staircase.md) and issue [#38](https://github.com/snissn/planar-jacobian/issues/38) request independent review. No qualifying-weight existence, defect-six, arbitrary-termination, or `JC_2` claim is introduced.

## Exit

The mathematical stop rule for defect `4` has been reached by a full scoped reduction, and an independent reviewer bound `ACCEPT` to the exact candidate revision. The branch and review are preserved as provenance; current-main synchronization is editorial except for the explicit reviewed-status delta. Defect `5` is banked only as mutable candidate `CLM-073`; independent review remains open as `L15`. A qualifying-weight theorem, defect six, and `JC_2` remain outside this track's reviewed scope.
