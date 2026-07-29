# Local Adversarial Review — Qualifying-Weight Descent

```text
review_mode: local-adversarial-review
reviewed_revision: 574a42de10d3927dd76ad5c6e8b3aa4fcd1f114b
reviewed_base: 652a5e252626fa5816445651245e8a8946cee53e
reviewer: constructing agent in a separate review pass
disposition: ACCEPT at mutable candidate scope
```

## 1. Exact binding

This review treats construction commit
`574a42de10d3927dd76ad5c6e8b3aa4fcd1f114b` as immutable. The comparison with
its live base reports twenty-four commits and sixteen added files, all under

```text
research/issues/qualifying-weight-descent/
```

No root README, STATUS file, shared claim ledger, proof graph, work queue,
issue index, generated view, governance file, validator workflow, or other
issue-owned path is changed.

The construction revision already contains an earlier draft `REVIEW.md`. The
present review supersedes that draft and does not use it as a scientific
premise. The review independently rechecks the mathematical artifacts and
executable evidence at the pinned construction revision.

The reviewed claims are only:

1. existence of each explicitly class-indexed achieved minimum `mu_C`;
2. the exact affine-orbit formula `mu_aff(A_N)=mu_SL(A_N)=N^2-1`;
3. collapse of `A_N` by one declared nonlinear target shear;
4. the exact full/tame diagnosis `mu_full(F)<=4` if and only if `F` is
   invertible, using the reviewed fixed-weight defect-four theorem;
5. the finite regular-fan test for a fixed Keller representative;
6. the weighted common-power and adjacent nonzero-vertex lemmas;
7. the complete binomial-chain theorem `Q=c y+lambda P^N`;
8. finiteness of the certificate-directed combinatorial core;
9. the corrected global minimal-counterexample obstruction; and
10. the exact bounded search at the four declared realizability levels.

The review does not accept a universal tame/full bound five, termination of
arbitrary complete-top descent, a global finite support list, simultaneous
monomialization of normalization-boundary valuations, the fixed-weight
defect-five candidate, or `JC_2`.

## 2. Disposition

`ACCEPT` at `local-adversarial-review / MUTABLE_NONAUTHORITATIVE` scope.

No mathematical blocker was found in the exact scoped statements after the
corrections recorded below. This is not independent review because the same
agent constructed and reviewed the packet. The packet is integration-ready as
a candidate theorem/obstruction record only.

## 3. Corrections required before this binding

### 3.1 Minimality at nonminimizing weights

An early draft overclaimed that a global minimal counterexample has no
exponent-one complete-top shear at every positive weight. A strict decrease
from a nonminimal defect can remain at or above the selected global minimum.
The bound construction states only the valid consequence:

```text
if kappa_u(F)=kappa_min,
then a complete-top exponent-one shear is impossible.
```

At a nonminimizing weight, such a shear remains a valid directed descent
certificate but is not itself a contradiction.

### 3.2 Full-orbit scalar versus a constructive invariant

The unqualified orbit scalar was replaced by class-indexed values. The review
also sharpened the full/tame diagnosis. If `F` is an automorphism, its inverse
as a target automorphism gives `mu_full(F)=0`. Conversely, an achieved value at
most four gives an automorphism-equivalent fixed-weight pair with defect at
most four; the independently reviewed theorem makes that pair, and hence `F`,
an automorphism. Therefore

```text
F invertible <=> mu_full(F)<=4 <=> mu_tame(F)<=4.
```

The proposed full-orbit scalar is therefore a reformulation of the terminal
problem at the reviewed threshold, not a prior descent invariant. A bound-five
version is stated only conditionally on independent acceptance of the exact
fixed-weight defect-five candidate.

### 3.3 Finiteness of the directed core

The original draft cited the finite-fan theorem too quickly when claiming that
all weights in a six-coordinate minimizing core form a finite set. The bound
proof now uses the first and sixth coordinates exactly. If

```text
Lambda(G,w)=(K,D,S,E,A,T),  w=(p,q),
```

then

```text
p+q=d_R(w)+d_S(w)-kappa_w=T-K.
```

Only finitely many positive primitive integer pairs lie on that line. Ordinary
degree and support-cardinality coordinates separately make the support-pair
set finite. The fan theorem supplies a computable test for a fixed support; it
is not used as a substitute for the full finiteness argument.

### 3.4 Semantic validator controls

The missing-binomial-support campaign formerly counted hole patterns without
encoding the recurrence obstruction. It now checks that every adjacent
recurrence forces `q_k=0` if and only if `q_(k+1)=0` on the declared nonzero
`a,b` chart, so nonzero endpoints with an interior hole are inconsistent.

The zero-vertex mutation formerly checked only a trivial multiplication by
zero. It now verifies both shared-vertex equations for distinct coprime power
pairs at `h=h'=(0,0)`, demonstrating exactly why the nonzero hypothesis in the
adjacency lemma is necessary.

### 3.5 Literature metadata and authority

The Makar-Limanov citation now distinguishes the English-edition pagination
and DOI from the Russian original. The Appelgate--Onishi entry records the
later primary lemma audit and consumes no theorem from that chain. No
bibliographic statement is used as a substitute for a load-bearing proof.

## 4. Reconstruction and adversarial checks

### 4.1 Rees identity and nonnegative defect

For a primitive positive weight `w=(p,q)`, direct chain-rule recomputation gives

```text
Pcal=t^d_P P(t^-p x,t^-q y),
Qcal=t^d_Q Q(t^-p x,t^-q y),
J(Pcal,Qcal)=t^(d_P+d_Q-p-q)=t^kappa_w.
```

The left side is polynomial in `t`, so `kappa_w` is a nonnegative integer. The
coefficient equations are exactly

```text
sum_(i+j=r) J(P_i,Q_j)=delta_(r,kappa_w).
```

This validates both the well-order argument and the face/transition equations.

### 4.2 Transformation classes and achieved minima

Every transformation class is separately declared. A source/target pair is
admitted only when its constant Jacobians multiply to one, so the transformed
pair remains normalized Keller. The identity and weight `(1,1)` make the value
set nonempty; it is a subset of `N`, so its least member is an achieved value.
No compactness, orbit closure, or finite generation is asserted.

The classes are not silently unioned:

- determinant-one linear;
- compensated affine;
- triangular target;
- fixed-weight graded source;
- tame; and
- full polynomial.

Jung--van der Kulk is consumed only for equality of the tame and full plane
automorphism groups.

### 4.3 Affine obstruction family

For

```text
A_N=(x+y^N, y+(x+y^N)^N),  N>=2,
```

write the independent linear parts of arbitrary affine source coordinates as
`M,L`. With

```text
epsilon=deg_w(M),
delta=deg_w(L),
D=max(epsilon,N delta),
```

ordinary-degree separation prevents cancellation between `M` and `L^N`, and
`D>N delta/N=delta`. Thus the two pre-target component degrees are `D,ND`.
An affine target row containing the second component has degree `ND`; a row
without it has degree `D`. Invertibility of the target matrix gives degree sum
at least `(N+1)D`.

For ordered coordinate weights `r<=s`, either `L` contains the weight-`s`
variable and `D>=Ns`, or `L` is supported on the weight-`r` variable and
independence forces `D>=max(s,Nr)`. The two cases give

```text
kappa_w>=N^2-1.
```

The original representative at weight `(N,1)` achieves equality. Translations
alter no positive weighted top degree. One target shear
`(u,v)->(u,v-u^N)` then sends `A_N` to `(x+y^N,y)` and gives defect zero at the
same weight. The family is therefore an actual Keller-level obstruction to an
affine-only bound, not a counterexample to the tame/full question.

### 4.4 Full/tame equivalence at defect four

The review checked both directions of the exact diagnosis. Orbit inversion
proves the zero value for automorphisms. In the converse direction the minimum
is achieved, the transformed pair remains normalized Keller, and the reviewed
fixed-weight defect-at-most-four theorem applies at its exact scope. Source and
target automorphisms then transport invertibility back to `F`.

No statement at defect five is promoted. The threshold-five version remains
conditional on the issue #29 candidate's independent acceptance.

### 4.5 Finite regular-fan theorem

The support-function identity is exact:

```text
kappa_w=h_(N(P)+N(Q)-(1,1))(w).
```

It is integral linear on every cone of the common normal fan. Positive Keller
defects imply nonnegative axis values by limits along primitive rays
`(m,1)` and `(1,m)`. After a unimodular subdivision, every lattice vector in a
cone has a unique expression `a u+b v`. Nonnegative ray values show that no
interior primitive vector improves on the finite ray candidates. When the
coordinate quadrant is the sole cone, `(1,1)` is the exact minimum candidate.

The result is fixed-representative only. Every support-changing transformation
requires rebuilding the polygon and fan.

### 4.6 Weighted common powers and edge arithmetic

Weighted Euler identities give, with signs checked,

```text
d_B B A_x-d_A A B_x=q y J(A,B),
d_B B A_y-d_A A B_y=-p x J(A,B).
```

When the bracket vanishes, both partial derivatives of
`A^(d_B)/B^(d_A)` vanish. Characteristic zero and UFD factorization yield

```text
A=a H^m,
B=b H^n,
gcd(m,n)=1,
```

with `H` weighted homogeneous. Newton multiplication gives edge lengths
`m ell_H,n ell_H`. Hence both exposed faces are vertices or both are parallel
edges; one edge and one vertex cannot occur.

### 4.7 Adjacent-edge compatibility

At adjacent positive edges sharing nonzero vertices in both component
polygons, endpoint equations have the exact form

```text
v_P=m h=m' h',
v_Q=n h=n' h'.
```

The nonzero shared vectors force equal rational ratios, and coprimality forces
`(m,n)=(m',n')`. At the origin every positive multiple is zero, so incompatible
pairs can meet; the packet retains this exception and does not infer one global
composite polynomial.

### 4.8 Complete binomial-chain theorem

For

```text
P=a x+b y^N,
Q=c y+sum_(k=0)^N q_k x^k y^(N(N-k)),
```

the constant Jacobian coefficient is `ac`. At exponent
`x^k y^(N(N-k)-1)`, the only two contributions are

```text
N a(N-k)q_k,
-N b(k+1)q_(k+1).
```

Thus the complete system is

```text
ac=1,
a(N-k)q_k=b(k+1)q_(k+1).
```

Solving it gives

```text
q_k=lambda binom(N,k)a^k b^(N-k),
Q=c y+lambda P^N.
```

The entire top polynomial, not one monomial, is cancelled by the declared
target shear. The sheared pair has defect zero and an explicit inverse. On the
nonzero endpoint chart, the recurrence propagates nonzero coefficients through
the full chain, so missing interior monomials are exactly excluded.

### 4.9 Global minimal-counterexample program

The six coordinates of `Lambda` are nonnegative integers, so the global
counterexample universe is well-ordered if nonempty. The reviewed defect-four
theorem gives `kappa_u>=5` for every positive weight of a noninvertible pair.
The selected first coordinate is global across all normalized noninvertible
Keller pairs and weights.

At any weight attaining that same global minimum defect, an exponent-one
complete-top shear would produce a noninvertible normalized pair with smaller
first coordinate, a contradiction. Other positive faces retain the exact
common-power data but may admit local descents that do not cross the global
minimum. Minimizing over all counterexamples also ensures that no compensated
source/target orientation exposes a smaller six-coordinate record.

The first two Rees equations record the exact transition constraints. Missing
monomials are literal zeros, while contributions landing at the same exponent
are collected before any cancellation claim. A weighted degree falls only when
the entire former face cancels.

### 4.10 Directed core finiteness

For a fixed minimizing six-tuple, ordinary degree bounds all lattice exponents,
support cardinality bounds support choices, and `p+q=T-K` bounds the primitive
positive weights. Exposed faces and their lattice records are then finite.
Coefficients may vary in algebraic families; no finiteness of coefficient
orbits is claimed.

### 4.11 Search levels, saturation, and mutations

The final exact default campaign was rerun and returned:

```text
primitive weights: 5611
ordered two-term support pairs: 44100
face-compatible high-defect pairs: 639
saturated formal systems: 387
formal Keller survivors: 0
adjacent nonzero-vertex solutions: 1881
mutation controls: 4
exact assertions: 2488
```

The larger JSON run with weight bound 128, `N<=12`, and 32 fan instances also
passed, with 10,043 primitive weights, 321,376 fan/brute comparisons, and 2,520
exact assertions. Five hundred random support-pair fan comparisons and 19,978
random primitive-ray subdivision checks also passed.

The exhaustive coefficient ideals are saturated by the declared nonzero
support coefficients. The search distinguishes support, formal-layer,
polynomial, and Keller levels. Its zero-survivor result is confined to the
bounded exactly-two-term library and the named `(2,3)` template; it is not used
as unbounded theorem authority.

## 5. Literature challenge

Every load-bearing new algebraic result except plane automorphism tameness is
proved internally. Stable higher-dimensional degree reductions are not treated
as planar orbit reductions. Remembered Razar or Formanek criteria whose exact
primary theorem text was not available are explicitly unconsumed. Conflicting
low-degree frontiers are reported separately, and the Makar-Limanov English and
Russian bibliographic records are not conflated.

No audited source supplied the exact no-escape theorem required to move from an
arbitrary planar Keller pair to a defect-at-most-five positive monomial weight
while preserving degree and normalization-boundary data.

## 6. Residual risks and next review target

The substantive open risks are not hidden cases in the scoped proofs. They are:

- whether arbitrary Keller support admits a terminating sequence of certified
  complete-top descents;
- whether a terminal coprime-power core with both exponents at least two can be
  bounded or excluded;
- whether zero/axis transitions permit an unbounded change of coprime power
  data; and
- whether positive monomial weights can be related to all non-toric
  normalization-boundary valuations without losing degree or sheets.

A future independent reviewer should focus on the arbitrary affine-source
lower bound, axis handling in the finite-fan theorem, the full-orbit equivalence,
the exact boundary between minimizing and nonminimizing weights, and the
coefficient-completeness of transition equations.

## 7. Authority statement

This local review supports integration of the issue-owned packet at mutable
candidate scope. It does not authorize `reviewed_scoped`, allocate a global
claim identifier, edit shared surfaces, close the qualifying-weight bridge,
merge the pull request, or claim `JC_2`.
