# Local Adversarial Review

```text
review_mode: local-adversarial-review
reviewed_scope: IDX3U-01 through IDX3U-08
reviewed_revision: pre-integration owned packet
constructor_independence: none; this is not independent scientific acceptance
disposition: ACCEPT_SCOPED_PACKET; BLOCK_PRIMARY_THEOREM_PROMOTION
```

## 1. Review protocol

The review was performed as a separate pass after construction. It recomputed
the load-bearing determinant, differential, boundary, and countermodel steps;
mutated the proposed implications against the issue #3 model; and ran the exact
symbolic scripts. It does not upgrade any statement to `reviewed_scoped`.

## 2. Adversarial questions and results

### A. Was finite flatness inferred from normalization alone?

No. Every use of a vector bundle, trace splitting, determinant line, or
Quillen-Suslin is explicitly conditional on finite local freeness. The
normal-surface/regular-base flatness argument and its source are restated.

### B. Was the ring inclusion reversed?

No. Every source restriction uses `O -> A=C[x,y]`. Source functions are treated
as rational functions on `Y` until boundary poles are cleared.

### C. Is `Phi` really intrinsic?

Yes. It is `1 wedge s wedge s^2 in det(O)`, identified with `det(E)` by the
trace splitting. Frame covariance is carried by the determinant line.

### D. Does the universal coefficient ideal solve the unit problem?

No. The initial formulation was attacked with the issue #3 cubic. Its
`X^2Y` coefficient is a unit, so its content/Fitting ideal is `B`, while the
banked specialization proof rules out every unit value. The packet now treats
this as an explicit correction, not a theorem route.

### E. Were canonical derivations assumed to preserve `O`?

No. A denominator `h_D` is chosen by clearing the finitely many coordinates of
`D(e_i)`. Only `h_D partial_D(J_Phi) subset J_Phi` is asserted. The local
formula divides by the different generator `f'(s)` and keeps that denominator.

### F. Does collision of two sheet values force a Keller critical point?

No. Over a split étale cubic fiber, one scalar projection can identify two
distinct points while `(x,y)` still separates them. The review rejected the
critical-point inference and the embedding-dimension/conductor variants.

### G. Does freeness of `E` trivialize the canonical or different divisor?

No. The issue #3 boundary chart gives
`det(partial(u,s)/partial(e,v))=e/v^2`, an explicit nontrivial boundary
coefficient despite a free rank-three algebra. The canonical shortcut was
removed.

### H. Is the four-direction lemma uniform?

Yes at its stated scope. A rank-three fiber has three unordered pairs and hence
at most three bad scalar slopes. Four fixed constants guarantee one separating
linear form. The lemma is applied only over `W` where the entire finite fiber
lies in the specified source. Boundary fibers are handled separately by issue
#3 finite-prime adaptation.

### I. Does the finite family imply one section?

No. The review deliberately stops at a gcd-one/codimension-two certificate.
The issue #3 countermodel shows that even a unit coefficient ideal and a
fiberwise generator cover do not force a global section.

### J. Is the primitive-coordinate identity sign-correct?

Yes. Starting from

```text
dt=-(F_PdP+F_QdQ)/F_T
```

and expanding the coefficient determinant gives

```text
J^{-1}=[F_T(X_PY_Q-X_QY_P)
       +F_P(X_QY_T-X_TY_Q)
       +F_Q(X_TY_P-X_PY_T)]/F_T.
```

The symbolic script checks the abstract identity and the special case
`F=T^3-P`, `Y=3QT^2`.

### K. Is the countermodel exclusion stronger than proved?

No. The proved invariant exclusion concerns the different meeting `U`. The
packet explicitly states that unramified moving index divisors survive this
exclusion. The triangular/affine-coordinate deformation test is not presented
as an exhaustive deformation theorem.

## 3. Symbolic review commands

```text
python3 research/issues/rank-three-index-form-unit/verify_rank_three_index.py
python3 research/issues/rank-three-index-form-unit/verify_differential_identity.py
python3 research/issues/rank-three-index-form-unit/verify_countermodel_boundary.py
python3 research/issues/rank-three-index-form-unit/verify_all.py
```

The scripts verify:

- the generic binary cubic determinant;
- coefficient recovery from values;
- the issue #3 multiplication/index/discriminant identity;
- the abstract and specialized symplectic coefficient identity;
- the open-plane relations and Jacobian;
- the boundary coordinate Jacobian;
- the exact affine-coordinate constant-Jacobian repair family.

## 4. Unresolved risks

1. The issue #3 finite-prime adaptation and globalization remain candidate
   dependencies rather than independently accepted theorems.
2. The finite-normalization/open-immersion baseline remains source-bound in
   `CLM-003` and is not promoted here.
3. No valuation theorem has been proved from the coefficient congruence (5.1).
4. Codimension-two failure of the generator scheme may still obstruct a global
   section even after all height-one data are covered by finitely many values.
5. The counterexample search is nonexhaustive.

## 5. Review disposition

`ACCEPT_SCOPED_PACKET`: the stated foundations, corrections, finite source
certificate, differential identity, and countermodel exclusions survive this
local adversarial pass.

`BLOCK_PRIMARY_THEOREM_PROMOTION`: no proof that one integral section has unit
index was obtained. The packet must remain `BLOCKED`/`candidate_proved` at its
individual scoped claims, never `reviewed_scoped` or a rank-three theorem.
