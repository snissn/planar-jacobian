# Defect-4 Weighted Rees Staircase — Exact Candidate Audit

> **Authority:** `MUTABLE_NONAUTHORITATIVE`  
> **Engineering status:** `DEVELOPMENT`  
> **Execution validity:** `NOT_A_SCIENTIFIC_EXECUTION`  
> **Protocol verdict:** `null`  
> **Scientific inference:** none beyond the scoped theorem candidate below  
> **Baseline:** `86d1b78cedd788b7335be692f9bb92921142c7d3`  
> **Issue:** [#17](https://github.com/snissn/planar-jacobian/issues/17)  
> **Branch:** `issue-17/defect-4-staircase`

## Disposition

This audit reaches acceptable disposition **1**, as a theorem candidate pending
independent exact-byte review:

> **Positive-weight defect-at-most-four theorem candidate.** Let
> `F=(P,Q)` be a polynomial pair over `C` with `J(P,Q)=1`, and let
> `w=(p,q)` be a primitive positive weight. If
>
> ```text
> kappa_w = deg_w(P)+deg_w(Q)-p-q <= 4,
> ```
>
> then `F` is a polynomial automorphism.

At defect `4`, every nonzero endpoint resonance already contains a top weighted
coordinate. For each interior position `(1,3)`, `(2,2)`, and `(3,1)`, the exact
staircase equations imply either:

1. a determinant-one triangular or linear target operation cancels a top layer
   and strictly lowers `kappa_w`; or
2. the weighted support and the preceding staircase equations give a
   contradiction.

No Newton--Puiseux, boundary-monodromy, exact-form principalization, Kummer, or
global deck-symmetry assertion is used. This is not a proof of `JC_2`: it only
covers maps admitting a positive weight with defect at most four.

The maintained claim status is `candidate_proved`, not `verified_internal`,
because this session did not supply a distinct independent reviewer. See the
exact-byte review record under `governance/reviews/`.

### Review scope

```text
Evidence level: E3 (reusable exact theorem on the declared small-defect class)
Quantifier level: Q3 restricted to all polynomial Keller pairs in that class
Stability level: S0 / static algebraic statement; no dynamical stability claim
```

**NEED:** exact Rees identity and signs; resonant-pair classification;
common-power lemma; complete `kappa<=3` audit; all defect-four resonance and
weight cases; exact Jacobian preservation; strict descent; scoped nonclaims;
exact-byte binding before promotion.

**SHOULD:** a second symbolic implementation and a reviewer-selected alternative
case organization. These strengthen confidence but do not enlarge the theorem.

**COULD:** defect-five analysis, Newton--Puiseux interpretation, boundary
monodromy, or a theorem producing a small-defect weight for a general Keller
pair. None is consumed here.

**Effective assumptions:** coefficients in `C`; polynomial source and target;
`J(P,Q)=1`; one declared primitive positive weight; `kappa_w<=4`.

**Stop rule:** stop at the scoped defect-four disposition and independent
review; do not begin higher-defect promotion in this packet.

## 1. Conventions and weighted layers

Use

```text
J(f,g) = f_x g_y - f_y g_x.
```

Let `R=C[x,y]` with `deg_w x=p`, `deg_w y=q`, where `p,q>0` and
`gcd(p,q)=1`. Write `R_d` for its weighted-homogeneous degree-`d` piece and set
`R_d=0` for `d<0`.

For nonconstant `P,Q`, put

```text
d_P = deg_w P,
d_Q = deg_w Q,
kappa = d_P+d_Q-p-q,
P = sum_(i>=0) P_i,   P_i in R_(d_P-i),
Q = sum_(j>=0) Q_j,   Q_j in R_(d_Q-j).
```

An absent degree is represented by the zero layer. The top layers `P_0,Q_0`
are nonzero by definition.

## 2. Independent Rees computation

Define

```text
Pcal(t,x,y) = t^(d_P) P(t^(-p)x,t^(-q)y),
Qcal(t,x,y) = t^(d_Q) Q(t^(-p)x,t^(-q)y).
```

For the `x` derivatives,

```text
partial_x Pcal = t^(d_P-p) P_x(t^(-p)x,t^(-q)y),
partial_x Qcal = t^(d_Q-p) Q_x(t^(-p)x,t^(-q)y),
```

and for the `y` derivatives the exponents are `d_P-q` and `d_Q-q`.
Therefore

```text
J(Pcal,Qcal)
 = t^(d_P+d_Q-p-q) J(P,Q)(t^(-p)x,t^(-q)y)
 = t^kappa.
```

No sign is changed: both determinant products acquire the same factor
`t^(d_P+d_Q-p-q)`.

Because

```text
Pcal = sum_i t^i P_i,
Qcal = sum_j t^j Q_j,
```

coefficient comparison gives, for every `n>=0`,

```text
S_n := sum_(i+j=n) J(P_i,Q_j) = delta_(n,kappa).
```

Moreover,

```text
J(P_i,Q_j) lies in R_(kappa-i-j).
```

If the bracket is nonzero, its weighted degree is `kappa-i-j`. Thus every
individual term with `i+j>kappa` is zero because `R_d=0` for `d<0`. The exact staircase is consequently

```text
S_0=...=S_(kappa-1)=0,
S_kappa=1,
J(P_i,Q_j)=0 whenever i+j>kappa.
```

Since the left side is a polynomial in `t`, the identity also proves
`kappa>=0`.

## 3. Elementary algebra used in every case

### 3.1 A resonant pair is an explicit graded automorphism

If `A in R_r`, `B in R_s`, and `J(A,B)=c in C*`, then `r+s=p+q`.
Evaluating the Jacobian at the origin shows that the linear parts of `A,B`
must have rank two. A weighted-homogeneous polynomial has an `x` linear term
only in degree `p` and a `y` linear term only in degree `q`. Hence

```text
{r,s}={p,q}.
```

After ordering `p<=q` and, when necessary, applying the determinant-one target
swap `(P,Q)->(Q,-P)`, take `r=p`, `s=q`.

If `p<q`, then

```text
A = a x,
B = b y + h(x),
ab=c,
deg_w h=q.
```

If `p=q`, primitivity gives `p=q=1` and `(A,B)` is an invertible linear pair.
Thus `(A,B)` is a polynomial graded automorphism in all cases. This proof is
internal and does not depend on an external graded-Keller theorem.

### 3.2 Exact normalization and the resonant scalar

Let `psi=(A,B)` and `J(psi)=c`. The source automorphism `phi=psi^(-1)` has
Jacobian `1/c`. Postcompose the target with

```text
D(u,v)=(u,c v),   det D=c.
```

Then

```text
J(D o F o phi) = c * 1 * (1/c) = 1,
```

and the selected pair becomes

```text
(P_a,Q_b)=(x,c y).
```

The scalar `c` is retained; it is not silently normalized to one. Since `phi`
is graded and `D` is diagonal, all layer indices are preserved. The normalized
degrees are

```text
d_P=p+a,
d_Q=q+b.
```

### 3.3 Common-power lemma for the top layers

Let `f in R_alpha` and `g in R_beta` be nonzero with `J(f,g)=0`. For the
weighted Euler derivation `E=p x partial_x+q y partial_y`, Euler's identities
and `J(f,g)=0` give

```text
alpha f dg - beta g df = 0.
```

Hence `d(g^alpha/f^beta)=0` in `C(x,y)`, so

```text
g^alpha = C f^beta
```

for some `C in C*`. Let

```text
r=gcd(alpha,beta),
alpha=r m,
beta=r n,
gcd(m,n)=1.
```

Unique factorization gives a nonconstant weighted-homogeneous `H in R_r` and
nonzero scalars `a,b` with

```text
f=a H^m,
g=b H^n.
```

A factor of a homogeneous element in a positively graded domain is homogeneous,
so no ungraded factor is introduced.

### 3.4 The only descent used

If `m=1`, then `g=lambda f^n`. The triangular target automorphism

```text
(P,Q) -> (P,Q-lambda P^n)
```

preserves the Jacobian because

```text
J(P,Q-lambda P^n)=J(P,Q)-lambda n P^(n-1)J(P,P)=1.
```

It cancels the complete top layer of `Q`, so the new weighted degree satisfies
`d'_Q<d_Q`, while `d'_P=d_P`. Therefore

```text
kappa'_w < kappa_w.
```

The transpose operation is used when `n=1`. If `m=n=1`, a determinant-one
linear shear cancels one proportional top layer. The well-founded descent
measure is the nonnegative integer `kappa_w`; no lexicographic proxy is hidden.

### 3.5 A divisibility contradiction

Suppose `n>m>=2` and

```text
f=aH^m,
g=bH^n,
lambda f_x+g_y=0,
lambda,a,b != 0.
```

After removing `H^(m-1)`, one obtains

```text
lambda a m H_x + b n H^(n-m) H_y=0.
```

Thus `H` divides `H_x`. If `H_x` is nonzero this is impossible by ordinary
total degree; if `H_x=0`, the displayed equation forces `H_y=0`, contradicting
that `H` is nonconstant.

## 4. Endpoint resonance and component coordinates

If a nonzero resonant bracket has position `(0,kappa)`, normalization makes
`P_0=x` and `d_P=p`. With `p<=q`, every term of `P` has weight at most `p`, so
`P` is affine linear in `x` (or affine linear when `p=q=1`). Thus `P` is a
polynomial coordinate. In source coordinates `(u,v)` with `u=P`, the equation
`J(P,Q)=1` says `partial_v Q` is a nonzero constant, hence

```text
Q = alpha v + h(u).
```

The map is triangular and invertible. Position `(kappa,0)` is symmetric. This
proves every endpoint row without using the common-power analysis.

## 5. Independent audit of defects zero through three

The proof is by induction on `kappa` using only the strict target descent above.

### 5.1 `kappa=0`

The unique resonant pair is `(P_0,Q_0)` and has nonzero constant bracket. Its
degrees are `{p,q}`. The full components have degrees at most `p,q`, so after
the graded normalization they are affine/triangular. Hence `F` is an
automorphism.

### 5.2 `kappa=1`

Both resonant positions `(0,1)` and `(1,0)` touch a top layer, so Section 4
applies.

### 5.3 `kappa=2`

Only `(1,1)` is interior. Normalize

```text
P_1=x,
Q_1=c y,
d_P=p+1,
d_Q=q+1.
```

The first two stairs are

```text
J(P_0,Q_0)=0,
c(P_0)_x+(Q_0)_y=0.
```

If `p=q=1`, the top degrees are equal and a linear target shear lowers defect.
If `p<q`, write `P_0=aH^m`, `Q_0=bH^n`, so `n>m`. An exponent one gives target
descent; otherwise Section 3.5 gives a contradiction. This completes defect
`2`.

### 5.4 `kappa=3`, resonance `(1,2)`

Normalize

```text
P_1=x,
Q_2=c y,
d_P=p+1,
d_Q=q+2.
```

If a top common-power exponent is one, descend. Assume neither is one.

* If `p<q` and `p>1`, nonzero `P_0 in R_(p+1)` forces `q=p+1` and
  `P_0=a y`. Then `J(P_0,Q_0)=0` forces `Q_0 in C[y]`, but its degree is
  `q+2`; this would require `q|2`, impossible for `q>=3`.
* If `p=1<q`, the no-descent common-power form is
  `P_0=a x^2`, `Q_0=b x^(q+2)`. The equations `S_1=0` and `S_2=0` give
  `(Q_1)_y=0` and then `2ac x=0`, a contradiction; `P_2` is constant.
* If `p=q=1`, write
  `P_0=aH^2`, `Q_0=bH^3`, `H=u x+v y`. The equations are

  ```text
  J(P_0,Q_1)+J(x,Q_0)=0,
  J(P_0,c y)+J(x,Q_1)=0.
  ```

  The second gives `(Q_1)_y=-2acuH`. Substitution into the first has
  `y^2` coefficient `3b v^3`, so `v=0`; its `x^2` coefficient then is
  `-4a^2 c u^4`, a contradiction.

### 5.5 `kappa=3`, resonance `(2,1)`

Normalize

```text
P_2=x,
Q_1=c y,
d_P=p+2,
d_Q=q+1.
```

Again first perform any exponent-one top descent.

* If `p<q` and `p>1`, `Q_0 in R_(q+1)` must be a pure `x` power.
  Top dependence forces `P_0` to be a pure `x` power, so `p|2`; hence
  `p=2`. The case `q=3` has proportional top layers and descends. For
  `q>=5`, `P_1 in R_3` is zero and `S_1=0` reads `2acx=0`.
* If `p=1<q`, the no-descent top form is
  `P_0=a x^3`, `Q_0=b x^(q+1)`. For `q>2`, `P_1` is a multiple of `x^2`,
  and `S_1=0` reads `3acx^2=0`. The case `q=2` is a top linear descent.
* If `p=q=1`, write
  `P_0=aH^3`, `Q_0=bH^2`, `H=u x+v y`. The equations

  ```text
  J(P_0,c y)+J(P_1,Q_0)=0,
  J(P_1,c y)+J(x,Q_0)=0
  ```

  imply `(P_1)_x=-(2bv/c)H`. Substitution into the first has `x^2`
  coefficient `3ac u^3`, so `u=0`; its `y^2` coefficient then is
  `-4b^2v^4/c`, a contradiction.

The swapped degree orientation is obtained by `(P,Q)->(Q,-P)`, interchanging
`(1,2)` and `(2,1)`. Thus the conversation-derived `kappa<=3` statement has
been rederived independently.

## 6. Defect four: exact equations

For `kappa=4`, the load-bearing stairs are

```text
S_0: J(P_0,Q_0)=0,
S_1: J(P_0,Q_1)+J(P_1,Q_0)=0,
S_2: J(P_0,Q_2)+J(P_1,Q_1)+J(P_2,Q_0)=0,
S_3: J(P_0,Q_3)+J(P_1,Q_2)+J(P_2,Q_1)+J(P_3,Q_0)=0,
S_4: sum_(i+j=4) J(P_i,Q_j)=1.
```

The sign of every term is positive in the coefficient sum; each internal
Jacobian uses `f_xg_y-f_yg_x`. The middle Wronskian occurs only in `S_2`.

If `S_4` has a nonzero endpoint term, Section 4 finishes. Otherwise select a
nonzero interior resonant term. A target symplectic swap handles reversed
component degrees, and the graded source normalization gives one of the three
forms below with `p<=q`.

## 7. Position `(1,3)`

Normalize

```text
P_1=x,
Q_3=c y,
d_P=p+1,
d_Q=q+3.
```

First apply any exponent-one top target descent. Assume neither top exponent is
one.

### 7.1 Equal weights

If `p=q`, primitivity gives `(p,q)=(1,1)`. The top degrees are `(2,4)`, so
`Q_0` is a scalar multiple of `P_0^2`; this is precisely an exponent-one
descent. Hence there is no equal-weight no-descent case.

### 7.2 Unequal weights with `p>1`

A nonzero polynomial of degree `p+1<2q` can exist only when `q=p+1`, in which
case `P_0=a y`. Then `S_0=0` forces `Q_0 in C[y]`. Since
`deg_w Q_0=q+3`, this requires `q|3`. The only possibility is `(p,q)=(2,3)`,
where `Q_0` is proportional to `P_0^2` and the top target shear descends.
Thus no `p>1` no-descent case survives.

### 7.3 Unequal weights with `p=1`

The no-descent common-power lemma forces

```text
P_0=a x^2,
Q_0=b x^(q+3).
```

Now

```text
S_1=0  =>  2ax (Q_1)_y=0  =>  (Q_1)_y=0.
```

Because `P_2` is constant,

```text
S_2=0  =>  2ax (Q_2)_y=0  =>  (Q_2)_y=0.
```

Finally `P_3=0`, and

```text
S_3 = J(a x^2,c y)+J(x,Q_2) = 2ac x,
```

contradicting `S_3=0`. This calculation includes `q=2` and all missing-layer
possibilities.

Therefore `(1,3)` always descends or is impossible.

## 8. Position `(3,1)`

Normalize

```text
P_3=x,
Q_1=c y,
d_P=p+3,
d_Q=q+1.
```

Again remove every exponent-one top case by target descent.

### 8.1 Equal weights

For `(p,q)=(1,1)`, the top degrees are `(4,2)` and `P_0` is a scalar multiple
of `Q_0^2`; descend.

### 8.2 Unequal weights with `p>1`

Since `q+1<2q`, a nonzero `Q_0 in R_(q+1)` is a pure `x` power, and
`p|(q+1)`. The equation `S_0=0` then makes `P_0` a pure `x` power. Since its
degree is `p+3`, one has `p|3`, hence `p=3` and `P_0=a x^2`.

The first possible value `q=5` gives proportional top layers and descends. In
any remaining no-descent case `q>=8`, while `P_1 in R_5=0`. Therefore

```text
S_1=J(a x^2,c y)=2acx,
```

which is impossible.

### 8.3 Unequal weights with `p=1`, `q>3`

In a no-descent case the common factor has degree at most two and, since that
degree is below `q`, is a power of `x`. Thus

```text
P_0=a x^4,
Q_0=b x^(q+1).
```

But `P_1 in R_3` is a multiple of `x^3`, so

```text
S_1=J(a x^4,c y)=4acx^3,
```

contradicting `S_1=0`. The value `q=3` is a top linear descent.

### 8.4 Exceptional unequal weight `(p,q)=(1,2)`

Write the complete allowed layers

```text
P_0=a x^4,
Q_0=b x^3,
P_1=u x^3+v x y,
P_2=e x^2+f y,
Q_2=g x.
```

The equation `S_1=0` is

```text
(4ac-3bv)x^3=0,
```

so `v=4ac/(3b)` is nonzero. The coefficient of `y` in `S_2` is then

```text
c v,
```

because

```text
S_2=(-3bf+3cu)x^2+c v y.
```

This is impossible. Missing `P_2` or `Q_2` only sets some displayed
coefficients to zero and does not remove `cv`.

Therefore `(3,1)` always descends or is impossible.

## 9. Central position `(2,2)`

Normalize

```text
P_2=x,
Q_2=c y,
d_P=p+2,
d_Q=q+2.
```

The central equation is exactly

```text
c(P_0)_x + J(P_1,Q_1) + (Q_0)_y = 0.          (C)
```

Perform every exponent-one top descent first.

### 9.1 Why the middle Wronskian cannot vanish in a no-descent case

For `p<q`, write `P_0=aH^m`, `Q_0=bH^n` with `n>m>=2`. If
`J(P_1,Q_1)=0`, equation `(C)` is precisely the divisibility contradiction of
Section 3.5. Hence a no-descent central case requires

```text
J(P_1,Q_1) != 0,
P_1 != 0,
Q_1 != 0.
```

This converts the Wronskian problem into a finite support problem.

### 9.2 Unequal weights with `p>1`

The support conditions are

```text
P_1 in R_(p+1) != 0  =>  q=p+1,
Q_1 in R_(q+1) != 0  =>  p | (q+1).
```

Together they give `p|2`, so `(p,q)=(2,3)`. But then

```text
P_0=a x^2,
Q_0=b x y,
J(P_0,Q_0)=2ab x^2 != 0,
```

contradicting `S_0=0`.

### 9.3 Unequal weights `p=1`, `q>2`

In a no-descent case `gcd(3,q+2)=1`, so

```text
P_0=a x^3,
Q_0=b x^(q+2),
P_1=u x^2,
Q_1=e x^(q+1)+f x y.
```

The equation `S_1=0` is

```text
3af x^3=0,
```

so `f=0`. Then `J(P_1,Q_1)=0`, contradicting Section 9.1.

### 9.4 Exceptional central weight `(p,q)=(1,2)`

Use the complete layer forms

```text
P_0=a x^3,
Q_0=b x^4,
P_1=u x^2+v y,
Q_1=e x^3+f x y.
```

The preceding stair is

```text
S_1=(3af-4bv)x^3=0.                            (E1)
```

The middle Wronskian and central stair are

```text
J(P_1,Q_1)=(2uf-3ve)x^2-vf y,
S_2=(3ac+2uf-3ve)x^2-vf y=0.                  (E2)
```

Equation `(E2)` gives `vf=0`. Equation `(E1)`, with `a,b` nonzero, then forces
`v=f=0`, after which the `x^2` coefficient of `(E2)` is `3ac`, a
contradiction.

### 9.5 Equal weights

For `(p,q)=(1,1)`, `P_0,Q_0` have the same degree three and are proportional,
so a determinant-one linear target shear lowers defect before the Wronskian is
used.

Thus the central Wronskian is neither a surviving formal obstruction nor a
required geometric monodromy carrier at defect four.

## 10. Complete resonance disposition

The exact case table is maintained separately in
[`defect-4-case-table.md`](defect-4-case-table.md). In compressed form:

| Resonance | Equal weights | Unequal `p>1` | Unequal `p=1` | Disposition |
|---|---|---|---|---|
| endpoint | top coordinate | top coordinate | top coordinate | automorphism |
| `(1,3)` | top power descent | only `(2,3)`, top power descent | no-descent stairs contradict | descend/impossible |
| `(2,2)` | linear top descent | support forces `(2,3)`, violating `S_0` | `q>2` forces zero Wronskian; `q=2` contradicts `(E1)-(E2)` | descend/impossible |
| `(3,1)` | top power descent | `p=3`; descent or `S_1` contradiction | `q>3` support contradiction; `q=2` coefficient contradiction | descend/impossible |

Reversed resonant degree orientation is covered by the determinant-one target
swap, which interchanges `(1,3)` and `(3,1)` and fixes `(2,2)`.

## 11. Inductive closure

Assume the theorem for every defect below `kappa`, as established explicitly in
Section 5 for `kappa<=3`. At `kappa=4`, choose a nonzero resonant term from
`S_4=1`. If it is an endpoint, Section 4 makes the map an automorphism. If it
is interior, orient and normalize it as in Section 3.2. Sections 7--9 show that
either an exact top target shear produces a Keller pair with the same positive
weight and strictly smaller defect, or the normalized layer system is
impossible. In the descent case the induction hypothesis makes the transformed
pair an automorphism; composing with the inverse source and target
transformations makes the original pair an automorphism.

This proves the stated defect-at-most-four theorem candidate. The induction is
only over the fixed positive-weight integer `kappa_w`; it is not an induction
on arbitrary polynomial degree and does not enter defect `5`.

## 12. What happened to alternatives (a)--(d)

* **(a), universal target removal of `J(P_1,Q_1)`:** not used and not proved.
  An `SL_2` target change acting on a same-index layer pair preserves its
  Wronskian. The target operations used here cancel a top common power and
  lower defect; they do not assert a standalone Wronskian normal form.
* **(b), universal filtered symplectic source removal:** not used and not
  proved. A graded Jacobian-one source automorphism sends the Wronskian to its
  pullback, so it preserves nonvanishing. Arbitrary Hamiltonian exponentials
  are excluded unless polynomiality and filtration termination are proved.
* **(c), forbidden Puiseux or boundary monodromy:** unnecessary at defect four.
  Positive-weight support and the earlier stairs already close every
  no-descent case.
* **(d), formal layer countermodel:** none survives `S_0,S_1,S_2` in the
  central case. In particular, the exceptional `(1,2)` calculation is the
  smallest possible mixed-layer attempt and is inconsistent.

## 13. Falsification attempts and controls

1. **Wrong Rees exponent.** Replacing `p+q` by either `p` or `q` fails the
   direct two-product chain-rule calculation.
2. **Wrong central sign.** Reversing the sign of `J(P_1,Q_1)` changes the
   exceptional `(1,2)` coefficient equations; the symbolic validator detects
   this mutation.
3. **Setting the resonant scalar to one.** The normalization proof retains
   `c`; every exceptional contradiction uses only `c!=0`.
4. **Ignoring the preceding stair.** The central equation alone has false
   positives. For weight `(1,2)`, take

   ```text
   P_0=x^3, Q_0=x^4, P_1=y, Q_1=x^3, P_2=x, Q_2=y.
   ```

   Then `S_0=0` and `S_2=3x^2-3x^2=0`, but
   `S_1=J(y,x^4)=-4x^3`. Thus the complete staircase rejects this formal
   central-only countermodel. Equations `(E1)-(E2)` explain the general
   rejection.
5. **Missing layers.** Every absent layer is zero in the displayed complete
   homogeneous spaces. No contradiction divides by an unselected intermediate
   coefficient.
6. **Unequal weights.** Primitive pairs were split into `p=q=1`, `p=1<q`, and
   `1<p<q`; the source swap covers `p>q`.
7. **Bounded machine search.** The validator enumerates primitive weights and
   monomial supports as a regression control, but the proof above supplies the
   unbounded arithmetic argument.

Run

```text
python3 scripts/validate_defect4_staircase.py
```

for exact symbolic regression checks. Those checks are process evidence, not
the theorem proof.

## 14. Literature boundary

The source audit is in
[`defect-4-primary-source-audit.md`](defect-4-primary-source-audit.md). The
proof above is self-contained. In particular:

* Shaska's positive-weight graded Keller theorem agrees with the resonant-pair
  conclusion, but the two-variable resonant classification is proved directly
  here.
* Lee--Li's inner-polynomial/Newton program is relevant context, not a step in
  this reduction.
* Karaś's weighted bidegree work is consistent with the allowed automorphism
  operations, but no external weighted-bidegree classification is consumed.
* No general polynomial Hamiltonian normal-form theorem is invoked.

## 15. Scope and surviving obligations

The exact result is conditional only on the stated polynomial Keller pair and
one primitive positive weight with `kappa_w<=4`. It does not provide:

* a positive weight of small defect for an arbitrary Keller map;
* preservation of generic degree or boundary valuations under an arbitrary
  long degeneration;
* a reduction for defect `5` or higher;
* a Newton--Puiseux or monodromy theorem;
* an independent exact-byte `ACCEPT`.

The smallest remaining action for this issue is independent review of the
candidate manifest. Higher-defect work remains out of scope.
