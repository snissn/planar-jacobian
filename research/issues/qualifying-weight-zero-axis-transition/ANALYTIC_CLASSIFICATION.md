# Analytic Classification

## Theorem `ZAT-D6-NO-TRANSITION`

Let `F=(P,Q)` be a normalized planar Keller pair over a characteristic-zero
field and let `w=(p,q)` be a primitive positive weight. Assume

```text
kappa_w(P,Q)=6
```

and that the complete top forms have coprime common-power data

```text
P_0=A H^m,  Q_0=B H^n,
(m,n) in {(2,3),(3,2)},  A B!=0.
```

Then no such pair exists. Consequently no defect-six `{2,3}` anchor can
participate in a pair-changing origin, axis, or nonshared-component transition.

## Proof

### Step 1: retain the complete defect-six sequence

The Rees identity gives

```text
S_s=sum_(i+j=s) J(P_i,Q_j)=delta_(s,6).
```

In particular `S_6=1`, so at least one scalar summand is nonzero. Choose
`a+b=6` with

```text
J(P_a,Q_b)=c!=0.                                      (1.1)
```

A nonzero constant bracket between weighted-homogeneous polynomials forces
their weighted degrees to be `{p,q}`. This follows from their linear parts at
the origin: a degree-`p` form is the only form that can contain an `x`-linear
term, and a degree-`q` form is the only form that can contain a `y`-linear term.

### Step 2: normalize with determinant-one maps only

Use the determinant-one source signed swap to arrange `p<=q`, and the
determinant-one target signed swap to place the degree-`p` selected layer in
`P`. The graded determinant-one source normalization in
[`DEFINITIONS.md`](DEFINITIONS.md) then gives

```text
P_a=x,  Q_b=c y                                      (2.1)
```

while preserving all layer indices and preserving the scalar `c`. No target
scalar normalization is used.

### Step 3: prove the arithmetic range is finite

Put `rho=deg_w(H)`. Since `d_P=m rho` and `d_Q=n rho`, (2.1) gives

```text
{m rho-a,n rho-b}={p,q}.                              (3.1)
```

A monomial `x^u y^v` occurs in the nonconstant `H`, so

```text
p u+q v=rho,
```

and hence one of `p,q` is at most `rho`. If `m rho-a<=rho`, then
`(m-1)rho<=a`; if `n rho-b<=rho`, then `(n-1)rho<=b`. Since `a,b<=6` and
`m,n>=2`,

```text
rho<=6.                                               (3.2)
```

Equations (3.1), `a+b=6`, primitivity `gcd(p,q)=1`, positivity, and the
Diophantine condition `p u+q v=rho` may now be checked for the six exact values
`rho=1,...,6`. The complete 16-row table is displayed in
[`TRANSITION_NORMAL_FORMS.md`](TRANSITION_NORMAL_FORMS.md). This finite table is
an elementary consequence of (3.2), not computational evidence substituted for
an unbounded proof.

The source and target signed swaps reduce the 16 rows to exactly four normal
forms I–IV. Each has a singleton weight-`rho` monomial set, so `H` is a monomial
and the top vertex is a nonzero coordinate-axis vertex.

### Step 4: eliminate normal form I

The complete layer support is

```text
P_0=A x^4, P_1=u x^3+v y, P_2=r x^2, P_3=x,
Q_0=B x^6, Q_1=e x^5+f x^2y, Q_2=g x^4+hxy, Q_3=c y,
```

with the remaining layers exactly as listed in
[`DEFECT6_REES_SYSTEM.md`](DEFECT6_REES_SYSTEM.md). The coefficient equations
include

```text
4Af-6Bv=0,                                            (4.1)
-2vf=0,                                               (4.2)
4Ah-5ve+3uf=0,                                        (4.3)
4Ac-4vg+3uh+2rf=0.                                    (4.4)
```

Because `A,B!=0`, (4.1) and (4.2) force `v=f=0`: either factor in (4.2)
vanishes, and (4.1) then kills the other. Equation (4.3) gives `h=0`, and
(4.4) gives `4Ac=0`, contrary to `A c!=0`.

### Step 5: eliminate normal forms II and III

In normal form II, the first correction equation is

```text
S_1=6Ac=0,
```

which contradicts `A c!=0`.

In normal form III, all unsupported degrees are retained as zero layers and

```text
S_1=2Ac=0,
```

again impossible.

### Step 6: eliminate normal form IV

The complete early layers include

```text
P_0=A x^6,
P_1=u x^5+v x^2y,
Q_0=B x^4,
Q_1=c y.
```

The first two stairs contain

```text
6Ac-4Bv=0,                                            (6.1)
2cv=0.                                                (6.2)
```

Since `c!=0`, (6.2) gives `v=0`; (6.1) then contradicts `A c!=0`.

All four normal forms are impossible. Because the 16 raw orientations are
covered by determinant-one signed swaps—and are also checked directly—no
source-order, component-order, sign, scalar, or missing-layer case remains.
This proves the theorem. `square`

## Corollary for the global minimal counterexample

Assume the fixed-weight defect-five theorem has its exact independent
acceptance integrated. A noninvertible Keller pair then has

```text
kappa_u>=6
```

for every primitive positive weight `u`. If the global minimum were six and a
minimizing face carried coprime pair `{2,3}`, the theorem above would contradict
the existence of that minimizing record.

There is a second, transition-specific contradiction. The mandatory selected
layer `c y` and every possible earlier off-axis coefficient generate one of the
nine first walls in [`CASE_TABLE.md`](CASE_TABLE.md); each has actual defect at
most five. Thus the adjacent weight itself violates the global lower bound.

Neither argument requires a local face shear to be promoted into a globally
lowering shear. No shear is used. The distinction between local cancellation
and global lexicographic descent therefore remains intact.

## Exhaustiveness of the two-wall system

The two-wall list is complete for each normal form:

1. every potential edge through the monomial axis anchor is determined by an
   off-axis support point;
2. all lattice points below the anchor degree are finite and explicit;
3. in the four arithmetic normal forms, every off-axis point capable of
   producing the first wall lies in a layer of index at most six;
4. a first-wall branch is obtained by setting every smaller-slope optional edge
   coefficient to zero and declaring at least one coefficient on the current
   wall nonzero;
5. the required selected `c y` coefficient prevents the sequence from escaping
   without an incident positive wall;
6. every branch's adjacent face equation is expanded and coefficients are
   combined only at identical exponent vectors.

This yields five branches in I, one in II, one in III, and two in IV. The
source signed swap supplies the `y`-axis copies. There is no origin copy because
the root support is never `(0,0)` and never an edge ending at `(0,0)`.

## Why no global common composite is inferred

The proof classifies one fixed defect-six anchor and its first adjacent wall.
It does not walk around all Newton polygons and does not identify the roots at
unrelated faces. The predecessor's constancy theorem remains limited to
adjacent nonzero shared vertices. The current contradiction terminates before
a second common-power pair exists.

## Relation to the non-toric boundary warning

The argument is exact in the Newton/Rees category for a primitive positive
monomial weight. A divisor on the finite normalization may remain nonmonomial in
fixed source coordinates; Laurent, conductor, or key-polynomial data can hide
global support through leading cancellations. Nothing here turns the toric
weight into a universal normalization-boundary valuation. The no-escape bridge
remains separate.
