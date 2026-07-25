# Newton--Weight Dictionary

## 1. Supports, polygons, and support functions

For a nonzero polynomial

```text
R=sum_(a in Z_{>=0}^2) r_a x^(a_1)y^(a_2),
```

write

```text
Supp(R)={a:r_a!=0},
N(R)=conv(Supp(R)).
```

For a real vector `w=(p,q)` in the closed positive quadrant, define

```text
h_R(w)=max_(a in N(R)) <w,a>.
```

For primitive positive lattice `w`, this is `deg_w(R)`. For a fixed pair
`G=(P,Q)`, set

```text
M_G=N(P)+N(Q),
Delta_G=M_G-(1,1).
```

Minkowski additivity gives

```text
kappa_w(G)
 =h_P(w)+h_Q(w)-p-q
 =h_(Delta_G)(w).                                      (1.1)
```

Thus the positive-weight defect of a fixed representative is an integral,
positively homogeneous, convex piecewise-linear function. It is not determined
by ordinary component degrees alone.

The exposed face is

```text
Face_w(R)={a in N(R):<w,a>=h_R(w)}.
```

The initial polynomial `in_w(R)` uses the **actual** nonzero support on that
face. A lattice point lying in `N(R)` but absent from `Supp(R)` contributes
zero.

## 2. Common normal fan

The normal fan of `M_G=N(P)+N(Q)` is the common refinement of the normal fans of
`N(P)` and `N(Q)`. On each closed cone `sigma`, both exposed faces are fixed and
(1.1) is an integral linear form:

```text
kappa_w(G)=<w,a_P+a_Q-(1,1)>  for w in sigma,          (2.1)
```

where `a_P,a_Q` can be any vertices of the fixed faces. Passing across a
positive fan ray changes at least one exposed face. This is the exact interface
between primitive supporting weights and compact Newton edges.

After a source or target transformation, coefficient cancellation can alter
support. The support, polygon, common fan, and defect must then be rebuilt; an
old fan is not an invariant of the orbit.

## 3. Nonnegativity on the closed positive quadrant

For a normalized Keller pair, the Rees identity gives

```text
kappa_w(G)>=0
```

for every primitive positive lattice vector. Homogeneity gives the same
inequality on positive rational rays, and continuity gives it on the open real
quadrant.

The axis values are also nonnegative. For example,

```text
kappa_(1,0)(G)
 =lim_(m->infinity) kappa_(m,1)(G)/m >=0,              (3.1)
```

and similarly on the other axis. This boundary fact is required in the finite
fan theorem. It is not true for arbitrary unrelated support pairs unless the
axis inequalities are imposed.

## 4. Finite positive-weight theorem

### Theorem `QWD-FAN`

Let `G=(P,Q)` be a fixed normalized planar Keller pair. Take the rays of the
common normal fan in the closed positive quadrant, including
`e_1=(1,0),e_2=(0,1)`. Refine each two-dimensional cone into a finite regular
fan whose consecutive primitive rays `u,v` satisfy

```text
det(u,v)=1.
```

Let `T_G` be the finite set of strictly positive rays of this regular fan. If
there is no such ray, put `T_G={(1,1)}`. Then

```text
min_{w primitive positive} kappa_w(G)
 =min_{w in T_G} kappa_w(G).                            (4.1)
```

### Proof

On a regular cone `Cone(u,v)`, every lattice vector has a unique expression

```text
w=a u+b v,  a,b in Z_{>=0}.
```

The regular fan refines the common normal fan, so `kappa` is linear there:

```text
kappa_w=a kappa_u+b kappa_v.                            (4.2)
```

Both ray values are nonnegative by Section 3.

- If `u,v` are strictly positive, an interior lattice point has `a,b>=1`; its
  value cannot improve on both boundary rays.
- If `u` is an axis and `v` is strictly positive, every positive lattice point
  has `b>=1`, and (4.2) is at least `kappa_v`. The transpose is identical.
- If the coordinate quadrant is the sole cone, every positive lattice vector
  is `(a,b)` with `a,b>=1`, so (4.2) is minimized at `(1,1)`.

Taking the finite union of cones proves (4.1). `square`

A regular subdivision exists by the two-dimensional Euclidean algorithm. The
validator constructs it using exact determinants and rational slope ordering;
no floating-point geometry is used.

### Consequence and limit

The infinite primitive-weight search is finite for every **fixed** orbit
representative. The theorem does not make an automorphism orbit finite, bound
all possible supports, or preserve a fan under a transformation.

## 5. Rees layers and faces

For primitive positive `w`, write

```text
P=sum_i P_i,
Q=sum_j Q_j,
P_0=in_w(P), Q_0=in_w(Q).
```

The exact Rees equations begin

```text
J(P_0,Q_0)=0                    if kappa_w>0,            (5.1)
J(P_0,Q_1)+J(P_1,Q_0)=0         if kappa_w>1.            (5.2)
```

Equation (5.1) is the face equation. Equation (5.2) is the first transition
constraint and depends on all actual monomials in the next weighted layers. A
polygon records where a layer can live; it does not solve the coefficient
equations.

If `kappa_w=0`, the initial pair itself has constant Jacobian one. For
`1<=kappa_w<=4`, the independently reviewed fixed-weight theorem gives
invertibility. Defect five is candidate-only here.

## 6. Weighted common-power lemma

### Lemma `QWD-EDGE`

Let `A,B` be nonconstant weighted-homogeneous polynomials of positive weighted
degrees `d_A,d_B`, and assume `J(A,B)=0`. Then there exist a nonconstant
weighted-homogeneous polynomial `H`, constants `a,b in C*`, and coprime
positive integers `m,n` such that

```text
A=a H^m,
B=b H^n.                                                (6.1)
```

### Proof

Weighted Euler identities are

```text
p x A_x+q y A_y=d_A A,
p x B_x+q y B_y=d_B B.
```

They imply

```text
d_B B A_x-d_A A B_x=q y J(A,B)=0,
d_B B A_y-d_A A B_y=-p x J(A,B)=0.                     (6.2)
```

Hence both partial derivatives of `A^(d_B)/B^(d_A)` vanish in `C(x,y)`. In
characteristic zero this ratio is constant, so

```text
A^(d_B)=c B^(d_A).                                     (6.3)
```

Let `g=gcd(d_A,d_B)`, `m=d_A/g`, `n=d_B/g`. Unique factorization applied to
(6.3) gives (6.1), with `gcd(m,n)=1`. Since the grading is positive and `H^m`
is homogeneous, the least and greatest weighted pieces of `H` coincide; thus
`H` is weighted homogeneous. `square`

Only weighted initial forms are used here. No claim is made that arbitrary
nonhomogeneous algebraically dependent polynomials are global powers.

## 7. Edge lengths and divisibility

For a lattice segment with endpoint difference `(r,s)`, define

```text
ell=gcd(|r|,|s|).
```

Newton polygons multiply by Minkowski addition:

```text
N(H^m)=m N(H).
```

If the `w`-face is an edge, (6.1) gives

```text
ell_P=m ell_H,
ell_Q=n ell_H,
gcd(ell_P,ell_Q)=ell_H,                                (7.1)
m=ell_P/gcd(ell_P,ell_Q),
n=ell_Q/gcd(ell_P,ell_Q).                              (7.2)
```

Therefore, under `J(in_w P,in_w Q)=0`, either both faces are vertices (the
common root is a monomial) or both are parallel edges. One component cannot
have an edge while the other has only a vertex.

An exponent `m=1` or `n=1` identifies a potential power shear. A strict
polynomial descent still requires cancellation of the **complete top
polynomial**, not merely one exposed monomial.

## 8. Adjacent-edge compatibility

Suppose adjacent positive normals `w,w'` expose edges in both polygons and the
two edges share nonzero vertices `v_P,v_Q`. Let their coprime power pairs be
`(m,n)` and `(m',n')`. For suitable endpoints `h,h'` of the common-root
polygons,

```text
v_P=m h=m' h',
v_Q=n h=n' h'.                                          (8.1)
```

Since the shared vertices are nonzero, (8.1) gives `m/n=m'/n'`; coprimality
therefore yields

```text
(m,n)=(m',n').                                          (8.2)
```

The pair is constant along every adjacent-edge chain connected through nonzero
shared vertices in both components.

The origin is a necessary exception: all positive multiples of zero are zero,
so distinct coprime pairs can meet there. Axis vertices and chains not sharing
both component vertices remain separate. This prevents an unjustified global
composite-polynomial conclusion.

## 9. Mixed area

For lattice polygons `A,B`, define the normalized mixed-area quantity

```text
MV_Z(A,B)=2 Area(A+B)-2 Area(A)-2 Area(B).               (9.1)
```

It is a nonnegative integer and is invariant under translating either polygon.
The minimal-counterexample tuple uses `2 Area(N(P)+N(Q))`, rather than `MV_Z`,
because ordinary degree plus Minkowski area directly bounds the lattice region
containing both supports.

Neither area determines `kappa_w`, which is directional. Nor does a mixed-area
bound encode the Jacobian coefficient equations, generic degree, or preservation
of sheets under a toric degeneration.

## 10. Monomial valuations and normalization boundary

A primitive positive weight defines a monomial valuation at infinity by

```text
v_w(x)=-p,
v_w(y)=-q,
v_w(R)=-deg_w(R).
```

Equation (1.1) becomes

```text
kappa_w=-v_w(P)-v_w(Q)+v_w(x)+v_w(y).                  (10.1)
```

This is the toric pole excess measured by the Rees scaling. The common-power
face data describe the leading classes in the associated graded ring.

A divisor on the finite normalization need not be monomial in fixed polynomial
source coordinates. It may require key polynomials, Puiseux data, or non-toric
Laurent/conductor corrections. The one-boundary packet explicitly leaves such
a class. This dictionary is therefore an interface, not a monomialization or
no-escape theorem.

## 11. Exact obstruction exposed

Large defect on every positive weight of a noninvertible pair forces:

1. common-power initial forms on every positive face;
2. coprime proportional edge lengths;
3. constant coprime ratio along adjacent nonzero edge chains;
4. complete next-stair compatibility at every transition.

It does **not** force one global composite polynomial, eliminate origin/axis
transitions, bound all support types, or prove that a toric degeneration retains
normalization-boundary data.
