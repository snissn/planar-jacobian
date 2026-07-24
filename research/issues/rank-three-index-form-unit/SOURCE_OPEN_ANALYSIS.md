# Source Open and Boundary-Valuation Analysis

```text
claims: IDX3U-05
status: CANDIDATE_PROVED_WITH_OPEN_BOUNDARY_CUBE_IDENTITY
```

## 1. Correct inclusion

For the open immersion

```text
j: U=Spec(A) -> Y=Spec(O),
A=C[x,y],
```

the ring map is

```text
O -> A.                                                           (1.1)
```

Both rings are domains with fraction field `L`, so (1.1) is injective. Thus
`x` and `y` are regular on `U` and rational on `Y`; they need not lie in `O`.

Let

```text
D = Y-U,
Z = pi(D) subset Spec(B)
```

for the finite map `pi:Y->Spec(B)`. Since `pi` is finite, `Z` is closed. Its
codimension-one components are the images of boundary divisors; it may also
have codimension-two points.

## 2. Clearing poles by base functions

### Boundary-clearing lemma

For every `r in A`, there exists `m in B\{0}` such that

```text
m r in O.                                                         (2.1)
```

Proof. A rational function regular on `U` can have negative valuations only at
the finitely many boundary prime divisors of the Noetherian normal surface
`Y`. If `q` is such a divisor, its contraction `p=q cap B` has height one under
the finite integral map. Since `B` is a UFD, write `p=(h_p)`. The valuation
`v_q(h_p)` is positive. A sufficiently high product of the `h_p` cancels every
negative `v_q(r)`. At all nonboundary height-one primes, `r` is already regular.
Normality gives

```text
O = intersection_{height(q)=1} O_q inside L,
```

and proves (2.1). Codimension-two boundary points require no extra multiplier.

For `t=mr`, put

```text
t^0=t-(1/3)Tr(t) in E.
```

Translation invariance and cubic scaling give the exact generic determinant
formula

```text
Phi(t^0) = m^3 Phi_K(r).                                          (2.2)
```

Here `Phi_K` is the determinant cubic after base change to `K`; it is defined
for any `r in L`.

For a source-linear function

```text
r=a(P,Q)x+b(P,Q)y+c(P,Q),
```

the term `c` has no effect on `Phi_K`, while every boundary-clearing multiplier
appears with exponent three in (2.2).

The exact unit condition for this source-derived section is therefore

```text
div_B(Phi_K(a x+b y)) + 3 div_B(m) = 0.                           (2.3)
```

Equation (2.3) is the boundary-cube identity left open by this packet.

## 3. Four fixed directions away from the boundary image

Choose four distinct constants

```text
lambda_0,lambda_1,lambda_2,lambda_3 in C
```

and put `r_i=x+lambda_i y`.

### Four-direction lemma

For every geometric point `b` of

```text
W = Spec(B)-Z,
```

at least one `r_i` generates the split rank-three fiber algebra of `O_W/B_W`.

Proof. Over `W`, one has `Y_W=U_W`, and the finite map is étale because the
specified Keller source is étale. A geometric fiber consists of three distinct
points of the affine `(x,y)`-plane. For each of the three unordered pairs, the
condition

```text
Delta x + lambda Delta y = 0
```

forbids at most one scalar `lambda`; if `Delta y=0`, it forbids none because
the points are distinct. There are at most three bad scalars, so one of four
fixed distinct choices separates all three points. In a split cubic étale
algebra, pairwise distinct values are exactly the generator criterion.

This uses rank three essentially: the number of pairwise collision slopes is
at most `binom(3,2)=3`.

Choose one common multiplier `m in B` making all `m r_i` integral, and take
trace-free parts `s_i`. On `W`, `m` is invertible after enlarging `Z` by its
zero divisor, and the four values satisfy

```text
(Phi(s_0),Phi(s_1),Phi(s_2),Phi(s_3)) B_W = B_W.                  (3.1)
```

Thus a finite collection of source-derived sections generates the unit ideal
away from boundary/denominator support. This is a genuine Keller-specific
success, but it is not one unit value.

## 4. Adding a boundary-adapted section

Let `H` be the finite set of height-one base primes occurring in `Z` or in the
chosen clearing multiplier. By the issue #3 finite-prime adaptation theorem,
there exists an integral primitive `theta in O` with

```text
B_p[theta]=O_p for every p in H.                                  (4.1)
```

Together, `theta,s_0,s_1,s_2,s_3` have index values with no common height-one
factor. Equivalently, the ideal they generate has support of codimension at
least two:

```text
height(Phi(theta),Phi(s_0),...,Phi(s_3)) >= 2
```

unless it is already the unit ideal.

This finite certificate is stronger than separately choosing a generator at
each of infinitely many primes. It still does not produce one section whose
index has empty support: taking a linear combination can create new collision
divisors.

## 5. What happens to a nonboundary collision factor

Let `p` be a height-one base prime not contained in `Z`, and let `s in O` have
`p | Phi(s)`. Then the finite cover is étale at the generic fiber over `p` and
all three points lie in the Keller source. The vanishing means that two
geometric sheet values of the **single function** `s` coincide.

It does not imply that the two points coincide in `(x,y)`, and it does not make
`dP wedge dQ` vanish. Equality of one scalar projection is compatible with two
distinct étale points. Therefore

```text
sheet-value collision != ramification of U -> Spec(B).            (5.1)
```

This is the exact failure of the proposed “collision forces a critical point”
action.

## 6. Rank-three geometric interpretation

Over a split étale fiber `k^3`, write the values of `s` as `z_1,z_2,z_3`.
Up to the fixed determinant orientation,

```text
Phi(s) = product_{i<j}(z_i-z_j).                                  (6.1)
```

A zero of (6.1):

- makes `k[s]` a proper subalgebra of `k^3`;
- does not make the fiber nonreduced;
- does not create embedding dimension two in the normal cubic algebra;
- creates conductor/index support only for the suborder `B[s]`, not a
  conductor defect of `O` itself;
- is compatible with ordinary nontrivial monodromy.

Hence none of the proposed rank-three geometric conclusions follows from a
moving collision alone.

## 7. Outcome of attack B and D

Proved:

- base multipliers clear all source boundary poles;
- the index scales by the cube of that multiplier;
- four fixed source directions cover every cubic étale fiber away from the
  boundary image;
- one additional issue #3 section covers all boundary height-one primes;
- all common obstruction can be compressed to codimension two for a finite
  set of values.

Not proved:

- a fixed direction with no nonboundary collision divisor;
- cancellation of all boundary valuations in the cube identity (2.3);
- a passage from a finite family of locally good sections to one global
  primitive section.
