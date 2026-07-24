# Primary-Source Audit for the Defect-4 Staircase

> **Authority:** `MUTABLE_NONAUTHORITATIVE`  
> **Source cutoff for this packet:** 2026-07-23  
> **Scientific use:** context and consistency checks only; the defect-four proof is self-contained

## 1. Graded Keller maps

**T. Shaska, _Graded Keller maps and the Jacobian Conjecture_,
arXiv:2607.20210v1 [math.AG], submitted 2026-07-22.**

Primary source: <https://arxiv.org/abs/2607.20210v1>

The full v1 text was checked, not only the abstract. Lemma 2.2 identifies the
multiset of target degrees with the source-weight multiset when the Jacobian at
the fixed point is nonzero. Theorem 3.2 assumes weighted source and target
actions with every source weight and target degree positive and concludes that
an equivariant Keller map `C^n -> C^n` is an automorphism. Theorem 3.3 treats a
Keller map on `C^2` equivariant for a nontrivial algebraic `G_m` action and,
after polynomial linearization of both actions, gives explicit triangular,
affine, or linear forms for all weight signatures.

The present packet consumes less: it directly proves that a two-variable
positive-weight homogeneous pair with nonzero constant Jacobian has component
degrees `{p,q}` and is an explicit graded triangular/linear automorphism. No
step of the defect-four case table depends on Shaska's properness argument or
on the external linearization theorem used in the all-signatures result.

## 2. Newton inner polynomials

**Kyungyong Lee and Li Li, _On the two-dimensional Jacobian conjecture:
Magnus' formula revisited, IV_, arXiv:2408.01279v1 [math.AG, math.AC],
submitted 2024-08-02.**

Primary source: <https://arxiv.org/abs/2408.01279v1>

The paper defines inner polynomials associated with a Jacobian pair and proves
constraints on the northeastern Newton-polygon vertices of those inner
polynomials. This is directly relevant to the broader goal of controlling
successive weighted corrections.

It does not, from the source statement audited here, supply the specific
filtration-preserving target or source cancellation required for the middle
Wronskian. No Lee--Li conjecture or special-case theorem is used as a defect-four
premise.

## 3. Weighted automorphism reduction

**Marek Karaś, _On weighted bidegree of polynomial automorphisms of C^2_,
arXiv:1201.3463v1 [math.AG], submitted 2012-01-17.**

Primary source: <https://arxiv.org/abs/1201.3463v1>

The paper studies weighted bidegrees of plane polynomial automorphisms and uses
the affine/triangular structure of the plane automorphism group. This is
consistent with the target shears and filtered source forms catalogued in this
packet.

The proof here does not infer invertibility from a weighted-bidegree entry and
does not use Karaś's classification as a black box. The exact filtered source
subgroup needed here is derived directly from the inequalities
`deg_w phi(x)<=p`, `deg_w phi(y)<=q` and the same inequalities for the inverse.

## 4. Polynomial flows and local nilpotence

**Ivan Pan, _A characterization of local nilpotence for dimension two
polynomial derivations_, arXiv:2012.03773v1 [math.AC], submitted 2020-12-07.**

Primary source: <https://arxiv.org/abs/2012.03773v1>

The paper concerns local nilpotence of plane polynomial derivations and the
polynomial automorphisms commuting with them. It is relevant to proposals that
would exponentiate a Hamiltonian derivation to obtain a polynomial source
normal form.

No such general flow theorem is consumed here. A formal exponential is admitted
only after a direct proof that it is polynomial and filtration-compatible. The
defect-four proof uses no Hamiltonian exponential.


## 5. Completion-valued Poisson normal forms

**Yucai Su, _Poisson algebras, Weyl algebras and Jacobi pairs_,
arXiv:1107.1115v1 [math.RA], submitted 2011-07-06.**

Primary source: <https://arxiv.org/abs/1107.1115v1>

The paper works with a completed Puiseux/Laurent Poisson algebra and introduces
well-defined, possibly infinite products of transformations of the form
`exp(ad_H)`, together with Laurent changes such as
`(x,y)->(x,y-cx^(-1))`. This is relevant to formal Newton normalization, but
its ambient ring and convergence/termination notion are not the polynomial
source category required by issue #17. It therefore supplies no license to use
a completion-valued Hamiltonian normal form as a polynomial automorphism of
`C[x,y]`.

## 6. Negative source findings

The primary-source search did not identify a theorem that automatically:

* removes an arbitrary `J(P_1,Q_1)` by a filtered polynomial symplectomorphism;
* converts exactness of a form into principalization;
* upgrades one generic-fiber Kummer description to a global Galois statement;
* turns multiple sheets into a global deck action; or
* preserves boundary valuations and geometric degree under the full Rees
  degeneration.

None of those implications appears in the candidate proof.

## 7. Source-binding conclusion

The only external theorem presently retained in the repository's broad
filtered-equivariance lane is Shaska's exact equivariant rigidity claim. The
new defect-at-most-four candidate is an internal algebraic derivation. Lee--Li, Karaś, Pan, and Su are recorded as nearby primary literature and
limitation checks, not as hidden dependencies.
