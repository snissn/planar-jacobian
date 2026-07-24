# Filtration-Compatible Transformation Catalogue

> **Authority:** `MUTABLE_NONAUTHORITATIVE`  
> **Scope:** transformations admitted in the defect-at-most-four audit  
> **Jacobian convention:** `J(f,g)=f_xg_y-f_yg_x`

## 1. Target transformations

### 1.1 Affine determinant-one changes

For `A in SL_2(C)` and `b in C^2`, set

```text
T(z)=Az+b.
```

Then

```text
J(T o F)=det(A)J(F)=1.
```

Translations do not change weighted degrees. A general linear mixture can
change the ordered bidegree and is not called a descent without an explicit
leading-layer calculation.

Two used special cases are:

```text
(P,Q)->(Q,-P)               # symplectic swap
(P,Q)->(P,Q-lambda P)       # equal-degree leading cancellation
```

The swap preserves `kappa` and exchanges the component/layer positions. The
linear shear is a descent only when the displayed top layers are proportional,
so that one full top layer vanishes.

### 1.2 Triangular target automorphisms

For any `h in C[z]`,

```text
T_h(P,Q)=(P,Q-h(P))
```

is a polynomial automorphism with inverse `(P,Q+h(P))`, and

```text
J(P,Q-h(P))=J(P,Q)-h'(P)J(P,P)=1.
```

The transpose `(P-h(Q),Q)` is identical. It is filtration-compatible at the
current pair when `deg_w h(P)<=d_Q`. It is a certified strict descent when

```text
h(z)=lambda z^N,
N d_P=d_Q,
Q_0=lambda P_0^N.
```

Then `d'_Q<d_Q`, `d'_P=d_P`, and `kappa'_w<kappa_w`. Lower terms created by
`P^N` have weight below `d_Q`; no larger layer is created.

No triangular target map is declared to remove an arbitrary middle Wronskian.

## 2. Source transformations

### 2.1 Jacobian compensation rule

For a polynomial source automorphism `phi` with constant Jacobian `delta` and
an affine target map `A` with determinant `delta^(-1)`,

```text
J(A o F o phi)=det(A) (J(F) o phi) J(phi)=delta^(-1)*1*delta=1.
```

This is the exact rule used to normalize a resonant graded pair whose bracket
is `c`, rather than pretending `c=1`.

### 2.2 Graded resonant normalization

If `(P_a,Q_b)=(A,B)` and `J(A,B)=c`, the map `psi=(A,B)` is a graded
polynomial automorphism. Take

```text
phi=psi^(-1),
A_target(u,v)=(u,c v).
```

Then the combined source-target operation preserves `J=1`, preserves every
layer index, and sends the chosen pair to `(x,c y)`.

### 2.3 Source swap and weight relabeling

The source map

```text
sigma(x,y)=(y,-x)
```

has Jacobian one. Relabeling the source weight from `(p,q)` to `(q,p)` gives

```text
deg_(q,p)(H o sigma)=deg_(p,q)H,
```

so `kappa` is unchanged. This justifies assuming `p<=q` without discarding
unequal-weight cases.

### 2.4 Complete filtered source group for `p<q`

A source automorphism preserving the weighted filtration and its inverse must
have

```text
phi(x)=a x+b,
phi(y)=d y+h(x),
a,d in C*,
deg_w h<=q.
```

Indeed `phi(x)` has weight at most `p`, so it cannot involve `y` or a power
`x^k` with `k>=2`; invertibility forces `a!=0`. The second coordinate can be
linear in `y` plus a polynomial in `x`, and invertibility forces `d!=0`.
The inverse has the same filtered form. Such a map is symplectic exactly when

```text
a d=1.
```

For `p=q=1`, the complete filtered group is the affine group and its
symplectic subgroup has linear determinant one. For `p>q`, transpose the
classification.

The defect-four proof uses only the graded subgroup of this classification,
plus the source swap. It does not rely on a nonlinear filtered source
normal-form algorithm.

## 3. Wronskian behavior

### 3.1 Same-index target `SL_2` invariance

If a determinant-one linear target map acts on a layer pair by

```text
(P_i',Q_i')=(alpha P_i+beta Q_i,gamma P_i+delta Q_i),
alpha delta-beta gamma=1,
```

then

```text
J(P_i',Q_i')=J(P_i,Q_i).
```

Thus a nonzero middle Wronskian cannot be killed by such a target change.

### 3.2 Graded symplectic source invariance

For a graded source automorphism `phi` with `J(phi)=1`,

```text
J(P_i o phi,Q_i o phi)=J(P_i,Q_i) o phi.
```

Therefore nonvanishing of the middle Wronskian is preserved by every graded
symplectic source normalization. Lower filtered source terms may mix layers,
but no universal polynomial terminating elimination theorem is assumed.

## 4. Hamiltonian transformations not admitted automatically

For a polynomial Hamiltonian `H`, the formal vector field

```text
X_H=H_y partial_x-H_x partial_y
```

is divergence-free. The formal exponential `exp(X_H)` is not automatically a
polynomial automorphism: the series must terminate on both coordinate
functions, for example because `X_H` is locally nilpotent. Even when it is
polynomial, its effect on the weighted filtration and the descent measure must
be proved.

Accordingly, this audit does not use a formal Hamiltonian exponential, an
analytic symplectomorphism, or a completion-valued canonical transformation as
a polynomial source operation. Su's completion-valued `exp(ad_H)` constructions
are recorded in the primary-source audit precisely as a category boundary, not
as an allowed transformation here.

## 5. Descent ledger

| Operation | Preserves `J=1` | Effect on `kappa` | Used for |
|---|---|---|---|
| target translation | yes | unchanged | harmless normalization only |
| target `SL_2` | yes | must be calculated | orientation swap; equal-top cancellation |
| `Q->Q-lambda P^N` | yes | strictly decreases when exact top equality holds | common-power descent |
| transpose shear | yes | same | common-power descent |
| graded source `phi`, compensated target determinant | yes | unchanged | resonant normalization |
| symplectic source swap plus weight relabel | yes | unchanged | assume `p<=q` |
| arbitrary filtered Hamiltonian exponential | not admitted without proof | unknown | not used |

Every strict descent in the proof is an exact full-top cancellation and uses
`kappa_w in Z_(>=0)` as the well-founded measure.
