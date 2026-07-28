# Foundations, signs, and scope

> Authority: `MUTABLE_NONAUTHORITATIVE`  
> Labels: `NTLC-H0` through `NTLC-H10`

## 1. Keller and normalization data

Let

```text
A=C[x,y],  B=C[P,Q],  K=Frac(B),  L=C(x,y),
O=normalization of B in L,  Y=Spec(O),  U=Spec(A).
```

The packet assumes:

- `NTLC-H0`: `P,Q in C[x,y]` and `J(P,Q)=1`;
- `NTLC-H1`: `O` is finite over `B` and `Y` is normal and integral;
- `NTLC-H2`: the Zariski-main morphism identifies `U` with the specified open
  subset of `Y`;
- `NTLC-H3`: `E=Y-U` has one reduced irreducible divisorial support;
- `NTLC-H4`: `E` is generically ramified over an irreducible reduced branch
  curve `C=V(g)`;
- `NTLC-H5`: at least one of `x,y` has a pole at the valuation of `E`;
- `NTLC-H6`: all characteristic and residue characteristics are zero.

The one-boundary hypothesis is used for program placement and for the earlier
torus/source-open theorem. The local results `NTLC-01` through `NTLC-05` apply
to any generically ramified pole-supported boundary divisor satisfying the
same completed-DVR hypotheses.

## 2. Differential signs

The Jacobian convention is

```text
J(P,Q)=P_x Q_y-P_y Q_x=1.
```

Therefore

```text
dP wedge dQ = dx wedge dy.                         (2.1)
```

Moreover

```text
d(P dQ+y dx)=dP wedge dQ+dy wedge dx=0.
```

Polynomial de Rham exactness on `A2_source` gives a polynomial `H in C[x,y]`
with

```text
P dQ+y dx=dH.                                      (2.2)
```

The plus sign before `y dx` is essential. Replacing it by a minus sign gives
`d(P dQ-y dx)=2 dx wedge dy`.

## 3. Completed ramified normal form

Let `eta_C` be the generic point of the branch and `eta_E` the generic point
of `E`. Write `k=C(C)` and `ell=C(E)`. After completion, a finite unramified
coefficient extension, and extraction of a unit root, the tame extension has
form

```text
k[[u]] -> ell[[t]],   u=t^e,   e>1.                (3.1)
```

The residue extension `ell/k` is finite separable. If `omega=dP wedge dQ`, then
in the logarithmic radial basis `dt/t` its pullback has order at least `e`:

```text
omega in t^e (dt/t) wedge Omega^1_(ell/C)[[t]].     (3.2)
```

Indeed `P,Q` are series in `u`; their residue differentials wedge to zero
because `trdeg_C k=1`, while `du=e t^e dt/t`.

## 4. Laurent conventions

For a coefficient field `F` and uniformizer `t`, write

```text
f=sum_i f_i t^i,
df=sum_i t^i(i f_i dt/t+d_F f_i).
```

If `alpha=A(t) dt/t+B(t)` is a one-form, its radial residue is the coefficient
of `t^0 dt/t`. An exact differential has zero radial residue.

With

```text
P=sum p_i t^i, Q=sum q_i t^i,
x=sum x_i t^i, y=sum y_i t^i,
```

(2.1) gives for every integer `r`

```text
sum_(i+j=r)(i p_i d q_j-j q_j d p_i)
 =sum_(i+j=r)(i x_i d y_j-j y_j d x_i).            (4.1)
```

For (2.2), radial and tangential coefficients are

```text
r h_r=sum_(i+j=r) j(p_i q_j+y_i x_j),              (4.2)
d h_r=sum_(i+j=r)(p_i d q_j+y_i d x_j).            (4.3)
```

These formulas are independently rederived in the validator.

## 5. Review and filtered-equivariance boundary

The reviewed theorem available to this packet is exactly:

```text
primitive positive w and kappa_w<=4 => automorphism.
```

No step below produces such a weight. The defect-five result on current
`main` is `candidate_proved` after local adversarial review; issue #38 remains
open. This packet neither consumes nor rederives defect five.

## 6. Issue-local authority

All new labels are issue-local. Proposed global claims, graph nodes, and queue
changes appear only in `INTEGRATION.json` and `HANDOFF.md`. No shared ledger,
proof graph, queue, generated view, root README, status file, governance file,
or workflow is modified.
