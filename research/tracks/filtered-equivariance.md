# Filtered Equivariance and the Rees Staircase

> **Authority:** `MUTABLE_NONAUTHORITATIVE`  
> **Claim status:** formulas are `CANDIDATE` unless explicitly marked `LITERATURE`.

## 1. Exact graded input

**Literature result.** T. Shaska, *Graded Keller maps and the Jacobian Conjecture*, arXiv:2607.20210, proves that a nontrivially `G_m`-equivariant Keller endomorphism of `A^2` is an automorphism for every sign pattern of the weights.

The present track asks whether an arbitrary Keller map can be reduced to that exact situation through a weighted filtration.

## 2. Positive weight and grading defect

Fix a primitive positive weight

```text
w=(p,q),     p,q>0.
```

For a polynomial `H`, let `deg_w(H)` be its weighted degree. Set

```text
d_P = deg_w(P),
d_Q = deg_w(Q),
kappa = d_P+d_Q-p-q.
```

Because `J(P,Q)=1`, one expects `kappa>=0`.

Decompose by weighted layers:

```text
P = P_0+P_1+P_2+...,
Q = Q_0+Q_1+Q_2+...,

deg_w(P_i)=d_P-i,
deg_w(Q_j)=d_Q-j.
```

Zero layers are allowed.

## 3. Rees identity

Define

```text
Pcal(t,x,y)=t^{d_P} P(t^{-p}x,t^{-q}y)
            =sum_i t^i P_i(x,y),
Qcal(t,x,y)=t^{d_Q} Q(t^{-p}x,t^{-q}y)
            =sum_j t^j Q_j(x,y).
```

The chain rule gives

```text
J_{x,y}(Pcal,Qcal)
 = t^{d_P+d_Q-p-q} J(P,Q)(t^{-p}x,t^{-q}y)
 = t^kappa.
```

Therefore coefficient comparison yields the staircase equations

```text
sum_{i+j=n} J(P_i,Q_j) = 0,   0<=n<kappa,
sum_{i+j=kappa} J(P_i,Q_j) = 1.
```

Every summand in the resonant equation has weighted degree zero. Since `p,q>0`, every weighted-degree-zero polynomial is constant. Hence at least one resonant pair has

```text
J(P_i,Q_j) in C^*.
```

That pair is an exactly graded Keller automorphism by Shaska's theorem.

**Audit burden:** independently recompute all exponent signs and verify that the chosen indexing handles missing weighted degrees correctly.

## 4. Top-resonance reduction candidate

Candidate lemma:

> If a resonant pair with constant Jacobian is `(P_0,Q_j)` or `(P_i,Q_0)`, then the full map is an automorphism.

Proposed mechanism: make a graded source-coordinate change sending the resonant pair to coordinate semi-invariants. If `P_0=x` has weight `p`, every lower-weight monomial involving `x` is excluded, so

```text
P=x+f(y).
```

Then `P` is a coordinate and `J(P,Q)=1` triangularizes the full map.

**Audit burden:** check every sign pattern and the possibility that the graded automorphism has unequal coordinate weights or requires a target normalization not preserving the layer decomposition.

If valid, a counterexample must have every nonzero resonant term strictly inside the staircase:

```text
1<=i,j<=kappa-1.
```

## 5. Low-defect candidate

### Defect 0 and 1

Every resonant term touches a top layer, so the top-resonance lemma would finish these cases.

### Defect 2

Under the non-top-resonance assumption, the resonant equation reduces to

```text
J(P_1,Q_1)=1.
```

After graded normalization, take

```text
P_1=x,     Q_1=y.
```

The lower staircase equations include

```text
J(P_0,Q_0)=0,
J(P_0,y)+J(x,Q_0)=0,
```

or

```text
(P_0)_x+(Q_0)_y=0.
```

The conversation-derived argument writes the dependent top forms as

```text
P_0=f(h),     Q_0=g(h)
```

for a common weighted-homogeneous closed polynomial `h`, and interprets the divergence equation as saying that the generic fibers of `h` are parallel affine lines. This would make `h` linear and permit cancellation of a top layer by a target automorphism, reducing the defect.

**Unresolved audit points:**

- exact hypotheses needed to choose a polynomial common generator `h`;
- proof that the tangent-vector condition holds on every generic irreducible fiber;
- proof that the resulting target cancellation strictly lowers `kappa` without changing the Keller normalization.

### Defect 3

An interior resonance is of type `(1,2)` or `(2,1)`. The conversation-derived case analysis normalizes, for example,

```text
P_1=x,     Q_2=y,
```

writes the dependent top forms as powers of a common weighted-homogeneous polynomial, and uses weight arithmetic plus the first staircase equations to reduce to finitely many adjacent-weight cases. Those cases were claimed contradictory or reducible to defect at most `2`.

This argument is recorded as the candidate claim `C-DEFECT-LE3`; it has not passed independent adversarial review.

## 6. Defect 4: first new obstruction

The central resonance pattern is `(2,2)`. Normalize

```text
P_2=x,     Q_2=y.
```

The `n=2` staircase equation is

```text
J(P_0,Q_2) + J(P_1,Q_1) + J(P_2,Q_0) = 0,
```

that is,

```text
(P_0)_x + J(P_1,Q_1) + (Q_0)_y = 0.
```

At defect `2`, the middle term is absent and the top common factor is forced toward a parallel-line pencil. At defect `4`,

```text
J(P_1,Q_1)
```

can bend that pencil. It is the first algebraic term capable of representing the cusp, puncture-monodromy, or nonprincipal-boundary corrections encountered in the normalization approach.

Other resonance patterns are `(1,3)` and `(3,1)` and must be treated separately.

Candidate sublemma:

> In the `(2,2)` pattern, if `J(P_1,Q_1)=0`, then a top layer can be cancelled and the map reduces to a lower-defect case.

This sublemma also requires audit.

## 7. Candidate staircase-reduction theorem

The desired theorem is:

> For every positive weight with `kappa>0`, a filtration-compatible polynomial source or target automorphism strictly lowers `kappa`.

Iteration would reach exact grading, where the literature theorem applies.

The first unproved induction step is defect `4`. Proving it likely requires one of:

1. classify the possible middle Wronskians compatible with dependent top layers;
2. realize `J(P_1,Q_1)` as a Hamiltonian coboundary removable by a filtered symplectic transformation;
3. show a nonremovable middle Wronskian forces forbidden boundary inertia or a finite asymptotic puncture;
4. combine Newton-polygon inner-layer restrictions with the staircase equations.

## 8. Falsification targets

An agent should actively search for formal layer systems satisfying all staircase equations through defect `4` but resisting every allowed reduction. Such a system would refute the current induction ansatz even if it does not come from a global polynomial Keller map.

At minimum test:

- all resonance patterns `(1,3)`, `(2,2)`, `(3,1)`;
- unequal positive source weights;
- zero or missing intermediate layers;
- target triangular transformations of degree greater than one;
- source symplectic/Hamiltonian transformations preserving the filtration;
- common top factors with relatively prime exponents greater than one.

## 9. Maintained conclusion

Exact grading is solved by the literature. The filtered extension through defect `3` is a candidate research result. Defect `4`, specifically the middle Wronskian, is the first maintained open leaf in this lane.
