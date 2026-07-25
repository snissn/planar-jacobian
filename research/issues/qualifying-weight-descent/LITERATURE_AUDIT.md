# Primary-Source Literature Audit

```text
source_cutoff: 2026-07-24
authority: MUTABLE_NONAUTHORITATIVE
consumed_external_theorem: plane automorphism tameness only
all weighted/fan/sparse-class results: proved internally
```

## 1. Audit rule

A theorem is marked **consumed** only when its exact conclusion and hypotheses
are needed by this packet. Bibliographic proximity is not a premise. When the
accessible primary page exposed only metadata or an abstract, the entry says so
and no stronger theorem is reconstructed from memory. Conflicting numerical
frontiers are recorded separately rather than averaged.

## 2. Plane automorphism structure

### Heinrich W. E. Jung, 1942

- *Über ganze birationale Transformationen der Ebene*, J. Reine Angew. Math.
  184 (1942), 161--174.
- Primary portal: <https://eudml.org/doc/150111>

### Wouter van der Kulk, 1953

- *On polynomial rings in two variables*, Nieuw Archief voor Wiskunde (3) 1
  (1953), 33--41.

### Modern primary proof used to bind the statement

- Nguyen Van Chau, *A Simple Proof of Jung's Theorem on Polynomial
  Automorphisms of C^2*, arXiv:math/0408077.
- <https://arxiv.org/abs/math/0408077>

**Exact scope consumed.** Over `C`, every polynomial automorphism of `C^2` is a
finite product of affine/linear and elementary triangular automorphisms. Hence
the tame and full polynomial automorphism groups coincide in dimension two.
The theorem does not provide a descending factorization for a noninvertible
Keller pair, a bounded number of elementary factors, or a qualifying weight.

## 3. Ordinary degree and gcd reductions

### Arne Magnus, 1955

- *On polynomial Solutions of a differential equation*, Math. Scand. 3
  (1955), 255--260.
- Primary page/PDF: <https://doi.org/10.7146/math.scand.a-10443>

The first page states the exact coprime-degree result used in later degree
literature: there are no polynomial solutions of `J(P,Q)=1` with

```text
gcd(deg P,deg Q)=1,
deg P>=2,
deg Q>=2.
```

Equivalently, a Keller pair with coprime ordinary component degrees has one
degree equal to one, after which the plane pair is triangular/invertible. This
is context only. Ordinary degree gcd does not produce a primitive positive
weight of bounded `kappa_w`.

### H. Appelgate and H. Onishi, 1985

- *The Jacobian conjecture in two variables*, J. Pure Appl. Algebra 37 (1985),
  215--227.
- DOI: <https://doi.org/10.1016/0022-4049(85)90099-4>

The publisher abstract states a plane result under the additional hypothesis
that one component degree has at most two prime factors. A. Nowicki and Y.
Nakai, *On Appelgate--Onishi's Lemmas*, J. Pure Appl. Algebra 51 (1988),
305--310, revisits key lemmas. Its introduction says one lemma was not proved
in the earlier paper and another proof was unclear. No part of this result is
consumed here; a future promotion must bind the original proof and the later
lemma audit at theorem level.

### Marek Karaś, weighted bidegrees

- *On weighted bidegree of polynomial automorphisms of C^2*, arXiv:1201.3463;
  later Bull. Pol. Acad. Sci. Math. 70 (2022), 107--114.
- <https://arxiv.org/abs/1201.3463>

The paper studies weighted bidegrees of plane **automorphisms** using the
Jung--van der Kulk structure. It is consistent with keeping weights and
transformation classes explicit. No classification from this paper is used in
the affine theorem or finite-fan proof.

## 4. Moh and later low-degree frontiers

### R. Biggers, T. T. Moh, and M. Fried, 1983

- *On the Jacobian conjecture and the configurations of roots*, J. Reine
  Angew. Math. 340 (1983), 140--213.
- DOI: <https://doi.org/10.1515/crll.1983.340.140>

This is a historical source for the degree-100 frontier and approximate-root
configuration analysis. The broad slogan “proved through degree 100” is not
used as a theorem in this packet.

### Guccione--Guccione--Horruitiner--Valqui, 2022

- J. A. Guccione, J. J. Guccione, R. Horruitiner, C. Valqui,
  *Increasing the degree of a possible counterexample to the Jacobian
  Conjecture from 100 to 108*, arXiv:2204.14178.
- <https://arxiv.org/abs/2204.14178>

Their abstract and Theorem 2.1 give the precise surviving degree statement:
all possible degree pairs with `max(deg P,deg Q)<125` are discarded except

```text
(72,108) and (108,72).
```

Equivalently, a counterexample would have `max(deg P,deg Q)>=125` or one of
those two exceptional ordered pairs. The introduction also explains how the
paper treats the older degree-100 record and combines later Newton-corner and
equation-system results. This is why the present audit does not collapse every
historical claim into one “Moh bound.”

### Nguyen Thi Bich Thuy, 2019 preprint / 2025 publication

- *Some classes satisfying the 2-dimensional Jacobian conjecture and a proof
  of the complex conjecture until degree 104*, arXiv:1902.05923; Quaestiones
  Mathematicae 48(9) (2025), 1291--1305.
- <https://arxiv.org/abs/1902.05923>

This source states a degree-104 frontier. It is recorded separately from the
Guccione et al. 108/exceptional-pair result. The degree notions and hypotheses
are not averaged into an informal intermediate number. Neither result implies
a bounded positive-weight defect and neither is consumed in the proofs here.

## 5. Abhyankar--Moh and approximate roots

### S. S. Abhyankar and T. T. Moh, 1975

- *Embeddings of the line in the plane*, J. Reine Angew. Math. 276 (1975),
  148--166.
- DOI: <https://doi.org/10.1515/crll.1975.276.148>

Exact scope: a polynomial embedding of the affine line in the complex affine
plane is rectifiable by a plane polynomial automorphism. It is not a theorem
that a component of an arbitrary Keller pair is an embedded line, or that one
Newton edge can be rectified without changing the other component.

Related approximate-root sources are Abhyankar--Moh, *Newton--Puiseux expansion
and generalized Tschirnhausen transformation I, II*, J. Reine Angew. Math. 260
(1973), 47--83 and 261 (1973), 29--53. The present common-power and fan theorems
are proved directly and do not import an approximate-root termination theorem.

## 6. Razar and rational-fiber criteria

### Michael J. Razar, 1979

- *Polynomial maps with constant Jacobian*, Israel J. Math. 32 (1979),
  97--106.
- DOI: <https://doi.org/10.1007/BF02764906>

The primary metadata was located, but the accessible source during this run did
not expose enough theorem text to bind the exact quantifiers concerning
rationality, irreducibility, generic fibers, and coordinates. Therefore **no
Razar theorem is consumed**. This avoids converting a remembered fiber
criterion into an unsupported Newton reduction.

For comparison, W. Neumann and P. Norbury, *Nontrivial rational polynomials in
two variables have reducible fibres*, Bull. Austral. Math. Soc. 58 (1998),
501--503, states in its abstract that a rational polynomial with irreducible
fibers is a coordinate. It is also not needed here.

## 7. Formanek field-generation results

### Edward Formanek

- *Two notes on the Jacobian Conjecture*, Arch. Math. 49 (1987), 286--291,
  DOI <https://doi.org/10.1007/BF01210711>.
- *Observations About the Jacobian Conjecture*, Houston J. Math. 20 (1994),
  369--380; issue portal <https://www.math.uh.edu/~hjm/vol20-3.html>.

These papers are cited in later literature for field-generation reductions,
including recovery of a rational function field after adjoining source
coordinates to the Keller component field. The search interface did not expose
enough primary theorem text to bind exact theorem numbers and hypotheses in
this run. No Formanek result is used in the packet's proofs.

## 8. Stable degree reductions: Bass--Connell--Wright and Drużkowski

### Bass--Connell--Wright, 1982

- H. Bass, E. H. Connell, D. Wright, *The Jacobian conjecture: Reduction of
  degree and formal expansion of the inverse*, Bull. Amer. Math. Soc. 7 (1982),
  287--330.
- DOI: <https://doi.org/10.1090/S0273-0979-1982-15032-7>

The reduction replaces a general map by cubic homogeneous maps through stable,
dimension-changing constructions. It is not an automorphism-orbit reduction
inside the original `A^2` and does not preserve a selected planar Newton
polygon, positive weight, function-field degree, or normalization boundary.

### Ludwik Drużkowski, 1983

- *An effective approach to Keller's Jacobian conjecture*, Math. Ann. 264
  (1983), 303--313.
- DOI: <https://doi.org/10.1007/BF01459126>

This refines the stable cubic reduction toward cubic-linear/power-linear maps
in higher dimension. It supplies no planar tame-equivalence theorem and no
bound on the orbit complexities defined here.

### David Wright

- *The amalgamated free product structure of GL_2(k[X_1,...,X_n]) and the weak
  Jacobian theorems for two variables*, J. Pure Appl. Algebra 12 (1978),
  235--251.
- Bass--Connell--Wright, above.

The first concerns weak Jacobian statements and matrix-group structure; the
second is a stable degree reduction. Neither is a no-escape theorem from
arbitrary planar support to defect at most five.

### Arno van den Essen, 2000

- *Polynomial Automorphisms and the Jacobian Conjecture*, Birkhäuser, 2000.
- DOI: <https://doi.org/10.1007/978-3-0348-8440-2>

This is a major secondary synthesis and bibliography, not a primary source for
a new qualifying-weight theorem. It is used as a map to the literature only.

## 9. Exact equivariance and filtered context

### T. Shaska, 2026 preprint

- *Graded Keller maps and the Jacobian Conjecture*, arXiv:2607.20210v1,
  submitted 2026-07-22.
- <https://arxiv.org/abs/2607.20210v1>

The repository's existing source audit binds the exact planar statement that a
Keller map equivariant for a nontrivial algebraic `G_m` action is an
automorphism, after the source/target actions and their linearization
hypotheses are established. This packet does not invoke that theorem in its new
proofs. The unresolved issue is producing a controlled graded representative
without losing degree or boundary data.

## 10. Newton boundary and nonproperness

### Zbigniew Jelonek, 1993

- *The set of points at which a polynomial map is not proper*, Ann. Polon.
  Math. 58 (1993), 259--266.
- Primary page: <https://doi.org/10.4064/ap-58-3-259-266>

For a dominant polynomial map `C^n->C^n`, the nonproperness set is either empty
or a uniruled hypersurface, with degree control in the source theorem. This is a
target nonproperness theorem. It does not identify every divisor of the source
normalization boundary with a positive monomial weight or prove that a toric
degeneration preserves all sheets.

### Leonid Makar-Limanov, 2021

- *On the Newton polyhedron of a Jacobian pair*, Izv. Math. 85:3 (2021),
  457--467.
- English-edition DOI: <https://doi.org/10.1070/IM9067>.
- Russian original: Izv. RAN. Ser. Mat. 85:3 (2021), 127--137,
  DOI <https://doi.org/10.4213/im9067>.

The abstract describes a Newton polyhedron attached to a minimal counterexample
and applications to geometric degree and a characteristic-pair case. It is
close to the present Newton core, but no theorem from it is consumed without a
full translation of notation and hypotheses.

### Kyungyong Lee and Li Li, 2024

- *On the two-dimensional Jacobian conjecture: Magnus' formula revisited, IV*,
  arXiv:2408.01279.
- <https://arxiv.org/abs/2408.01279>

The repository's prior audit records constraints on northeastern Newton
vertices of inner polynomials. It does not supply the complete polynomial
target cancellation, orbit termination, or boundary no-escape theorem required
here.

## 11. Leading-form common powers

The only common-power statement used is proved internally from weighted Euler
identities and unique factorization:

```text
A,B weighted homogeneous and J(A,B)=0
=> A=a H^m, B=b H^n, gcd(m,n)=1.
```

No broader statement that arbitrary algebraically dependent polynomials are
global powers is consumed.

## 12. Audit conclusion

The literature supplies strong ordinary-degree, approximate-root, fiber,
stable-reduction, nonproperness, and Newton restrictions. This audit found no
primary theorem with the exact conclusion

```text
for every planar Keller pair, polynomial source/target automorphisms
produce a primitive positive weight with kappa<=5 while preserving the
relevant function-field degree and normalization-boundary data.
```

The only external theorem used by the new proofs is plane automorphism
tameness. The defect-at-most-four theorem is reviewed repository authority.
Every other item above is contextual or explicitly unconsumed.
