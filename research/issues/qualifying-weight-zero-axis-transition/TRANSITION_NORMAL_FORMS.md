# Transition Normal Forms

## 1. Arithmetic reduction from the constant bracket

Fix a nonzero constant bracket `J(P_a,Q_b)=c`, with `a+b=6`, and let the top
coprime exponents be `(m,n) in {(2,3),(3,2)}`. After the determinant-one
normalization in [`DEFINITIONS.md`](DEFINITIONS.md), the selected weighted
degrees are `p,q` in one of the two component assignments. Thus

```text
{m rho-a, n rho-b}={p,q}.                              (1.1)
```

Because `H` is nonconstant, one monomial `x^u y^v` occurs in it and

```text
p u+q v=rho.
```

Hence `min(p,q)<=rho`. If `m rho-a<=rho`, then
`(m-1)rho<=a`; if `n rho-b<=rho`, then `(n-1)rho<=b`.
Since `a,b<=6` and `m,n>=2`, every possibility satisfies

```text
1<=rho<=6.                                             (1.2)
```

This is the analytic exhaustion bound. The subsequent integer table is not an
unproved bounded search.

## 2. Complete raw orientation table

`assignment 0` means `(deg P_a,deg Q_b)=(p,q)`; `assignment 1` means
`(deg P_a,deg Q_b)=(q,p)`. The root-support column lists every monomial of
weight `rho`; in all cases it is a singleton.

| # | `(m,n)` | `(a,b)` | `(p,q)` | assignment | `rho` | `Supp(H)` | canonical key |
|---:|---|---|---|---:|---:|---|---|
| 1 | `(2,3)` | `(1,5)` | `(3,1)` | 0 | 2 | `{y^2}` | IV |
| 2 | `(2,3)` | `(1,5)` | `(1,3)` | 1 | 2 | `{x^2}` | IV |
| 3 | `(2,3)` | `(3,3)` | `(1,3)` | 0 | 2 | `{x^2}` | I |
| 4 | `(2,3)` | `(3,3)` | `(3,1)` | 1 | 2 | `{y^2}` | I |
| 5 | `(2,3)` | `(5,1)` | `(1,8)` | 0 | 3 | `{x^3}` | II |
| 6 | `(2,3)` | `(5,1)` | `(8,1)` | 1 | 3 | `{y^3}` | II |
| 7 | `(2,3)` | `(5,1)` | `(5,14)` | 0 | 5 | `{x}` | III |
| 8 | `(2,3)` | `(5,1)` | `(14,5)` | 1 | 5 | `{y}` | III |
| 9 | `(3,2)` | `(1,5)` | `(8,1)` | 0 | 3 | `{y^3}` | II |
| 10 | `(3,2)` | `(1,5)` | `(1,8)` | 1 | 3 | `{x^3}` | II |
| 11 | `(3,2)` | `(1,5)` | `(14,5)` | 0 | 5 | `{y}` | III |
| 12 | `(3,2)` | `(1,5)` | `(5,14)` | 1 | 5 | `{x}` | III |
| 13 | `(3,2)` | `(3,3)` | `(3,1)` | 0 | 2 | `{y^2}` | I |
| 14 | `(3,2)` | `(3,3)` | `(1,3)` | 1 | 2 | `{x^2}` | I |
| 15 | `(3,2)` | `(5,1)` | `(1,3)` | 0 | 2 | `{x^2}` | IV |
| 16 | `(3,2)` | `(5,1)` | `(3,1)` | 1 | 2 | `{y^2}` | IV |

There is no equal-weight case. If `p=q=1`, then (1.1) gives

```text
2=p+q=(m+n)rho-(a+b)=5rho-6,
```

so `5rho=8`, impossible.

## 3. Four determinant-one normal forms

The source signed swap and target signed swap generate the equivalence used in
the last column. No scalar is removed.

| key | `(m,n)` | `(a,b)` | `w=(p,q)` | `rho` | `H` | `(P_0,Q_0)` |
|---|---|---|---|---:|---|---|
| I | `(2,3)` | `(3,3)` | `(1,3)` | 2 | `x^2` | `(A x^4,B x^6)` |
| II | `(2,3)` | `(5,1)` | `(1,8)` | 3 | `x^3` | `(A x^6,B x^9)` |
| III | `(2,3)` | `(5,1)` | `(5,14)` | 5 | `x` | `(A x^2,B x^3)` |
| IV | `(3,2)` | `(5,1)` | `(1,3)` | 2 | `x^2` | `(A x^6,B x^4)` |

In every row `A B c!=0`, `P_a=x`, and `Q_b=c y`.

## 4. Why the anchor is always an axis vertex

Each row has exactly one monomial of weight `rho`. Therefore `H` is a scalar
multiple of a power of `x` in the normalized orientation, and both top faces
are vertices on the nonzero `x`-axis. There is no root edge and no origin
endpoint. Applying the determinant-one source signed swap replaces `x` by the
`y`-axis orientation.

This is a conclusion of the defect-six arithmetic, not an assumption that all
positive faces are toric or share a global composite.

## 5. Complete first-wall geometry

For an anchor `x^N`, any lower monomial `x^u y^v` with `v>0` meets it at a
positive wall normal proportional to

```text
(v,N-u).
```

Because the lower monomial has smaller anchor weight, this wall lies on the
higher-slope side of `w`. All possible off-axis monomials in the four normal
forms occur within the first six Rees layers; there is no unrepresented deeper
monomial capable of producing an earlier incident wall.

### Normal form I

At `w=(1,3)`:

```text
P anchor x^4:  wall (1,4) through y;
Q anchor x^6:  walls (1,4) through x^2 y,
               (1,5) through x y,
               (1,6) through y.
```

The complete first-wall branches are:

1. `(1,4)`, `Q`-only;
2. `(1,4)`, `P`-only;
3. `(1,4)`, shared;
4. `(1,5)`, `Q`-only after the `(1,4)` coefficients vanish;
5. `(1,6)`, `Q`-only after the earlier coefficients vanish.

Their actual adjacent defects are respectively `5,5,5,4,3`.

### Normal form II

At `w=(1,8)`, `P` has no positive incident edge. The required term `c y` in
`Q_1` creates the unique `Q`-only wall `(1,9)`, of defect five.

### Normal form III

At `w=(5,14)`, `P` has no positive incident edge. The required term `c y` in
`Q_1` creates the unique `Q`-only wall `(1,3)`, of defect one.

### Normal form IV

At `w=(1,3)`:

```text
P anchor x^6: walls (1,4), (1,5), (1,6)
              through x^2 y, x y, y;
Q anchor x^4: required wall (1,4) through y.
```

The first wall is necessarily `(1,4)`. It is either `Q`-only or shared,
depending on whether the `x^2 y` coefficient of `P_1` vanishes. Both branches
have defect five.

Thus there are exactly nine normalized branches. Their explicit face forms and
saturation results are tabulated in [`CASE_TABLE.md`](CASE_TABLE.md).

## 6. Pair-change classification

Every adjacent wall above has positive defect, so a Keller pair would require
its adjacent initial forms to have zero Jacobian and hence a new common-power
pair. The exact adjacent-face ideals already saturate to `1`; the full anchor
Rees ideals do as well. Therefore no branch reaches the stage at which a second
coprime pair could be assigned.

The source-swapped table covers `y`-axis transitions. Origin transitions are
empty. Nonshared-component transitions are explicitly represented by the
`P`-only and `Q`-only rows rather than inferred from the shared case.
