# Research Program

> **Authority:** `MUTABLE_NONAUTHORITATIVE`

## Goal and common setup

The program studies polynomial maps

```text
F=(P,Q): A^2_C -> A^2_C,     J(P,Q)=1,
A=C[x,y],                    B=C[P,Q],
K=Frac(B),                   L=Frac(A).
```

Its goal is to prove that every such map is an automorphism. No branch below is presently a repository proof of `JC_2`.

The common reduction uses the integral closure of `B` in `L`. The affine source embeds as an open subset of a finite normalization over the target. If that finite normalization is étale and connected over `A^2_C`, it is trivial; the unresolved difficulty is carried by boundary sheet loss, ramification, and codimension-two gluing.

Each branch supplies a sufficient bridge, a restricted theorem candidate, a literature-bound reduction, or an obstruction. The exact status of every maintained statement is in [`claim_ledger.json`](claim_ledger.json).

## Parallel proof families

### Algebraic globalization

- global primitive elements and elimination of unramified index divisors;
- finite differential orders stable under the canonical commuting derivations;
- global complete-intersection, monogenicity, or power-basis purity criteria.

### Dynamical and Lie-theoretic globalization

- local finiteness or completeness of canonical translation, Euler, hyperbolic, or radial fields;
- algebraic integration of the canonical affine action;
- elimination of poles along the normalization boundary.

### Fiber and logarithmic geometry

- Gauss–Manin and puncture modules;
- intrinsic quasi-Albanese finiteness;
- logarithmic boundary constraints;
- exact symplectic residues and principal parts.

### Boundary models and topology

- Wright one-boundary graded reduction and Poisson rigidity;
- cusp/tangency braid elimination;
- Galois closure, inertia, and fixed-sheet constraints.

### Transformative and filtered routes

- exact `G_m`-equivariant rigidity, source-bound to Shaska’s arXiv:2607.20210;
- weighted Rees deformation and staircase equations;
- filtered reduction toward an exact graded model;
- equivariant degeneration without loss of function-field degree or boundary data;
- characteristic-p and p-curvature.

The canonical filtered packet is [`L13-defect-4-staircase.md`](leaf-packets/L13-defect-4-staircase.md). Current-main review artifacts concerning its candidate branch are preserved under [`../governance/reviews/`](../governance/reviews/). Their proposed status delta is not applied by this structural reconciliation.

## Cross-track interfaces

A filtered or graded calculation must eventually identify a global mechanism, such as:

- a monotone Newton or valuation invariant on the normalization boundary;
- a filtration-compatible polynomial source or target transformation;
- a cusp or inertia configuration excluded by the monodromy track; or
- a no-escape result preserving degree and boundary stratum under degeneration.

Conversely, a formal layer system that satisfies a staircase but cannot arise globally identifies a missing realization theorem rather than a proof of the main goal.

## Coordination and exit rules

The complete active queue is generated in [`WORK_QUEUE.md`](WORK_QUEUE.md). Issue [#2](https://github.com/snissn/planar-jacobian/issues/2) coordinates the program; leaf issues coordinate bounded work. Closed issue #1 is historical only.

A research branch exits when it supplies one of:

1. an independently checkable theorem at a declared scope;
2. a counterexample to a maintained candidate;
3. a minimal blocked implication with its dependencies and equivalent formulations;
4. a finite auditable classification; or
5. the leaf packet’s own narrower stop condition.

A restricted result remains restricted. Do not relabel a missing bridge as a lemma and treat it as proved.
