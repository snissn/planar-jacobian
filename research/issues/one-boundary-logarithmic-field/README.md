# One-Boundary Logarithmic Semisimple Field

```text
authority: MUTABLE_NONAUTHORITATIVE
scientific_status: SUBCLASS_EXCLUSION_WITH_EXACT_REDUCTION
review_mode: local-adversarial-review
base_commit: 788e94419080debf356d17123cbf81cb23b391ac
issue: 5
supporting_issue: 13
owned_path: research/issues/one-boundary-logarithmic-field/
provisional_labels: OBLF-*
```

## Disposition

This packet does **not** prove the planar Jacobian conjecture and does not
exclude every one-boundary normalization. It establishes three bounded results
at candidate scope.

1. For every irreducible reduced plane curve `g=0`, the logarithmic module
   `Der_C(C[P,Q])(-log g)` is a free rank-two module. Its Hamiltonian element is
   always available, but local finiteness is an independent condition.
2. A nontrivial one-boundary Keller normalization whose unique boundary
   component is generically ramified cannot have a reduced branch curve
   preserved by a nontrivial target `G_m` action. After a finite isogeny, the
   target action lifts through the finite normalization; the unique ramified
   boundary and the source open are invariant; the resulting equivariant
   planar Keller map is an automorphism, contradicting the nonempty boundary.
   Consequently no nonzero semisimple locally finite integral-weight target
   field compatible with those hypotheses can occur.
3. If the finite normalization is unramified in codimension one, purity makes
   it finite étale and hence degree one. Thus a one-boundary model consisting
   only of unramified sheet loss is impossible.

The surviving general class is therefore the class in which the branch has no
nontrivial torus symmetry. For fixed boundary pole orders and fixed conductor
algebra, it is reduced to the explicit Laurent, conductor, and grading system
recorded in this packet. Exactness kills the logarithmic residue but does not
kill higher principal parts.

## Exact one-boundary theorem used here

Let

```text
B = C[P,Q],  K = Frac(B),  L = C(x,y),
O = normalization of B in L,  Y = Spec(O),
U = Spec(C[x,y]) -> Y,  D = Y - U.
```

Assume:

- `F=(P,Q):U->A2` is Keller;
- `O` is finite over `B` and `Y` is normal and integral;
- the reduced support of `D` is one irreducible divisor `D0`;
- `D0` is generically ramified over one irreducible reduced branch curve
  `C=V(g)`; and
- a nontrivial algebraic `G_m` action on the target preserves `C`.

Then the model is impossible unless `D` is empty. The proof does not assume
that `Y` is smooth, that the boundary scheme is reduced, that an abstract
`A1` is a coordinate line, or that a regular derivation is complete.

The action-lifting step is a separate finite-isogeny lemma. It starts with an
actual target action, not merely a regular lifted derivation. The terminal step
uses T. Shaska, *Graded Keller maps and the Jacobian Conjecture*,
arXiv:2607.20210v1, Theorem 3.3, only after source-open invariance and genuine
source and target actions have been proved.

## Candidate labels

- `OBLF-01`: freeness and Saito presentation of the logarithmic module;
- `OBLF-02`: locally finite Jordan parts preserve the logarithmic ideal;
- `OBLF-03`: integral semisimple fields are linearizable and force a
  semi-invariant branch equation;
- `OBLF-04`: finite-isogeny lift of a target torus action through the finite
  normalization;
- `OBLF-05`: exclusion of the generically ramified one-boundary torus class;
- `OBLF-06`: purity exclusion of unramified one-boundary sheet loss;
- `OBLF-07`: leading one-boundary symplectic coefficient equation;
- `OBLF-08`: conductor and cusp descent equations;
- `OBLF-09`: surviving finite compatibility system at fixed valuation type.

Global claim identifiers are allocated only in the final synchronization step.

## Artifact map

- [`BOUNDARY_HYPOTHESES.md`](BOUNDARY_HYPOTHESES.md): exact hypotheses and
  scope separations;
- [`LOGARITHMIC_MODULE.md`](LOGARITHMIC_MODULE.md): presentation, freeness,
  Saito criterion, and element types;
- [`SEMISIMPLE_CLASSIFICATION.md`](SEMISIMPLE_CLASSIFICATION.md): Jordan
  decomposition, integral weights, linearization, action lifting, and the
  terminal subclass theorem;
- [`PRINCIPAL_PARTS.md`](PRINCIPAL_PARTS.md): full Laurent equations and the
  first one-boundary coefficient obstruction;
- [`CONDUCTOR_AND_PUNCTURES.md`](CONDUCTOR_AND_PUNCTURES.md): normalization,
  conductor descent, cusps, tangencies, and puncture moments;
- [`SOURCE_OPEN_INVARIANCE.md`](SOURCE_OPEN_INVARIANCE.md): exact ideal
  criterion and purity theorem;
- [`SUBCLASS_TABLE.md`](SUBCLASS_TABLE.md): required subclass dispositions;
- [`COUNTERMODELS.md`](COUNTERMODELS.md): cyclic covers, cusps, noncomplete
  fields, and invariance failures;
- [`REVIEW.md`](REVIEW.md): separate adversarial review bound to the candidate
  revision;
- [`HANDOFF.md`](HANDOFF.md): smallest surviving calculations;
- [`verify_oblf.py`](verify_oblf.py) and [`verify_all.py`](verify_all.py): exact
  symbolic and packet checks.

## Scientific nonclaims

Integration of this packet does not assert that every one-boundary branch is
weighted homogeneous, that exactness principalizes the boundary, that every
regular logarithmic field integrates, that the normalization baseline is fully
reviewed, or that the source theorem used in the terminal conditional has been
independently validated by this repository. Merge location is transport and
preservation only.