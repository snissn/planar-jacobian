# Adversarial Review Pass

```text
review_mode: CONSTRUCTOR_LOCAL_ADVERSARIAL_REVIEW
independence: NOT_INDEPENDENT
reviewed_base: 296867d82d09d51ef2386de2a62067408b7f949c
authority: MUTABLE_NONAUTHORITATIVE
protocol_verdict: BLOCK_FOR_PROMOTION_PENDING_INDEPENDENT_REVIEW
scientific_disposition: READY_FOR_MUTABLE_HANDOFF
```

This is a separate hostile pass over the issue-scoped arguments. It is not an
independent scientific acceptance and does not authorize freezing or
promotion.

## Reviewed path set

```text
research/issues/issue-3-unramified-index/README.md
research/issues/issue-3-unramified-index/THEOREM-PACKET.md
research/issues/issue-3-unramified-index/COLLISION-DIVISORS.md
research/issues/issue-3-unramified-index/KELLER-NEAR-COUNTERMODEL.md
research/issues/issue-3-unramified-index/COUNTERMODELS.md
research/issues/issue-3-unramified-index/SOURCE-AUDIT.md
research/issues/issue-3-unramified-index/PROPOSED-SYNC.md
research/issues/issue-3-unramified-index/HANDOFF.md
research/issues/issue-3-unramified-index/verify_index_models.py
```

Shared ledger and proof-graph edits are synchronization metadata, not theorem
authority.

## 1. Quantifier and localization audit

### A1 — base prime versus normalization prime

A statement about each `O_q` over a height-one base prime `p` can miss a
collision between separate residue components. The correct object is

```text
O_p=O tensor_B B_p.
```

The special-fiber criterion is

```text
B_p[theta]=O_p
  <=> kappa(p)[bar(theta)]=O_p/pO_p.
```

The product example `A x A` confirms that factorwise projection is
insufficient.

### A2 — generic primitivity

`K(theta)=L` controls only the generic fiber. Every integral generation claim
is therefore expressed through the quotient `O/B[theta]`, its zeroth Fitting
ideal, or the entire special-fiber algebra. No proof infers local integral
generation from generic separability.

## 2. Index, discriminant, different, and conductor audit

For equal-rank locally free modules, the inclusion determinant generates
`Fitt_0(O/B[theta])`, and over a height-one DVR its valuation is the quotient
length. The square-index formula follows by changing from an integral basis
to the power basis.

The conductor is not identified with the Fitting ideal. Only equality of
their height-one support is used. The different formula
`Different(B[theta]/B)=(f_theta'(theta))` is invoked only for the monogenic
hypersurface order.

The Galois-closure determinant uses an integral basis, not a purported
integral normal basis. Intrinsic ramification is removed by subtracting the
normal-discriminant valuation; a raw Vandermonde zero is not automatically
index.

## 3. Semilocal DVR generator audit

The local proof has two delicate points.

1. A finite local Artin factor with separable residue field admits a lift of
   that residue field by formal etaleness. Newton iteration inside the
   nilpotent algebra recovers the coefficient-field element from
   `beta+tau`; the principal nilpotent generator is then recovered by
   subtraction.
2. Generators of the individual factors do not automatically generate their
   product. Translations over the infinite residue field are chosen so that
   the annihilator polynomials are pairwise coprime; the Chinese remainder
   theorem then gives one generator of the product.

No Galois hypothesis is used. The tame non-Galois example recomputes the
mechanism with mixed residue degree and ramification.

## 4. Finite-prime patching audit

For distinct height-one primes `p_i=(f_i)`, choose local generators represented
by global elements `a_i` and set

```text
h_i=product_{j!=i} f_j,
theta=sum_i h_i a_i.
```

Modulo `p_i`, all terms except the `i`th vanish, while `h_i` is a nonzero
residue scalar. Scaling by that scalar preserves generation. The theorem is
limited to a prescribed finite set. It does not assert an iterative
termination invariant: a new index divisor may appear elsewhere.

This proves simultaneous ramification adaptation because the normal
discriminant has finite height-one support.

## 5. `R1/S2` globalization audit

Let `R=B[theta]`. A height-one prime of `R` cannot contract to zero by
incomparability, and cannot contract to a height-two base prime under a finite
integral extension. It therefore contracts to a height-one prime `p` of `B`.
The equality `R_p=O_p` makes the corresponding localization a DVR, proving
`R1`.

The ring `R` is a hypersurface domain and hence `S2`. The direct denominator
argument is valid: if an element of the normalization lies in every
height-one localization, its denominator ideal has height at least two; an
`R`-regular sequence of length two in that ideal forces the element back into
`R`. Thus `R` is normal and equals `O`.

No Hartogs statement about torsors is used.

## 6. Degree-one audit

The proof first establishes `O=B[theta]` without using the Keller conclusion.
Only afterward is the open source introduced. On `A2_source`,

```text
Omega_{O/B}=O/(f_theta'(theta)) dtheta
```

restricts to zero because the source map is etale. Therefore
`f_theta'(theta)` is a unit of `C[x,y]`, hence a nonzero constant. For degree
greater than one, `f_theta'(T)-c` is a nonzero polynomial of smaller degree
vanishing at `theta`, contradicting minimality. There is no circular appeal
to degree one.

## 7. Strong countermodel recomputation

For the algebra

```text
w^2=w-u e,
we=-uv,
e^2=v(w-1),
```

the following checks were rerun independently of the prose.

### B1 — associativity and domain

All basis triples associate. On `D(u)`, `w` satisfies

```text
T^3-T^2-u^2v.
```

A rational root would lie in `C[u,v]`; specializing `v=1` would give a
polynomial root of `T^3-T^2-u^2`, impossible by degree. The generic cubic is
therefore a field.

### B2 — rationality

The relation gives

```text
v=w^2(w-1)/u^2,
```

so the fraction field is `C(u,w)`.

### B3 — universal index form

The determinant of `1,xw+ye,(xw+ye)^2` is exactly

```text
-(u x^3+x^2y+v y^3).
```

Setting `u=0` in a hypothetical unit equation forces a nonconstant linear
polynomial to be a square in `C[v]`. Hence no element generates globally.
This covers every element, not merely a selected mutation family.

### B4 — local monogenicity

The index values at `w`, `e`, and `w+e` are `-u`, `-v`, and
`-(1+u+v)`. Their principal opens cover the entire base.

### B5 — smoothness and normality

On `D(u)` the derivative with respect to `v` is `-u^2`; on `D(v)` the
derivative with respect to `u` is `v^2`. Over the remaining base point, the
`w+e` polynomial has nonzero derivative at each of its two geometric points.
Thus the total surface is smooth and hence normal.

### B6 — discriminant and branch type

The trace determinant is

```text
-v(4+27u^2v).
```

The factors are coprime and reduced. The generic cubic factors as
`T^2(T-1)` on the first component and
`(T-2/3)^2(T+1/3)` on the second. Each branch inertia is a tame transposition
with one fixed sheet. The discriminant is not a square, so the generic cubic
is non-Galois.

### B7 — open affine plane

Writing `z=1-w`, the relations are

```text
wz=ue,
we=-uv,
e^2=-vz.
```

On `Y-V(u,z)`, the glued function `s=w/u=e/z` gives an isomorphism with
`A2_{u,s}` and

```text
v=us^3-s^2.
```

The Jacobian is `s(3us-2)`, so this open plane is not an etale source. The
example is therefore not a Keller counterexample.

### B8 — moving adapted divisors

For `w+lambda e`, the index is

```text
-(u+lambda+lambda^3v).
```

Neither branch factor divides it. Its nonempty line is therefore accidental
unramified support, and distinct parameters give distinct lines.

## 8. Corrections made during this review

1. Replaced the statement that every distinct nonzero parameter in the
   diagonal model gives a distinct divisor. The divisor depends only on
   `lambda^3`.
2. Replaced “the index divisor is contained in the etale locus” by the exact
   statement that every height-one generic point of the divisor is
   unramified. Codimension-two intersections with branch components are not
   excluded unless proved separately.
3. Replaced “integral normal basis” by “integral basis” in the Vandermonde
   determinant formula.
4. Strengthened the algebraic obstruction from separate nonsmooth or
   nonrational examples to one smooth rational fixed-sheet model with an
   open affine plane.
5. Reserved claim identifiers `CLM-052` through `CLM-057` for the live
   parallel issue #5 synchronization; this branch uses `CLM-058` and
   `CLM-059`.

## 9. Overclaim audit

The artifacts do not claim:

- a proof or disproof of the planar Jacobian conjecture;
- a Keller counterexample;
- that every rational finite cover is nonmonogenic;
- that every finite-dimensional parameter family fails;
- that fixed-sheet monodromy is irrelevant when combined with source
  etaleness;
- that class groups can never contribute alongside an effective-support
  theorem;
- that local monogenicity has no positive use.

The exact negative inference is:

> The unramified moving-index divisor cannot be eliminated from the tested
> purely algebraic hypotheses, even after adding smoothness, rationality,
> squarefree fixed-sheet branching, and an open affine plane. Any surviving
> proof must use etaleness of the specified Keller source.

## 10. Review verdict

```text
internal_consistency: NO_KNOWN_BLOCKER_AFTER_CORRECTIONS
symbolic_recomputation: PASS
independent_acceptance: ABSENT
freeze_or_promotion: BLOCK
mutable_branch_handoff: ACCEPT
```

The smallest independent-review targets are:

1. the coefficient-field/Newton step in the semilocal DVR generator lemma;
2. the finite-prime patching formula;
3. the contraction step in the `R1/S2` proof;
4. smoothness, normality, and the no-unit proof for the fixed-sheet cubic;
5. the exact boundary between the algebraic countermodel and source
   etaleness in the Keller successor.
