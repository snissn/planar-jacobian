# Filtered Rees Defect-4 Staircase

- **Priority:** `P0`
- **Status:** `OPEN`
- **Issue:** [#17](https://github.com/snissn/planar-jacobian/issues/17)
- **Dependencies:** CLM-016, CLM-047, CLM-048, CLM-049, CLM-050
- **Authority:** `MUTABLE_NONAUTHORITATIVE`

## Load-bearing question

For a positive primitive source weight `w=(p,q)`, resolve the first unproved filtered case

```text
kappa_w = deg_w(P)+deg_w(Q)-p-q = 4.
```

Determine whether every defect-4 Keller pair reduces to lower defect, or whether a formal layer system disproves the proposed staircase-reduction ansatz.

## Required independent recomputation

1. Recompute the weighted Rees identity

   ```text
   J(Pcal,Qcal)=t^kappa.
   ```

2. Derive every staircase equation from coefficient comparison.
3. Audit the claimed `kappa<=3` reduction before using it.
4. Verify Shaska's exact graded theorem at the precise hypotheses consumed.

## Case table

Treat every interior resonant position:

```text
(1,3), (2,2), (3,1).
```

For each position include:

- unequal positive weights;
- zero or absent intermediate layers;
- common-factor exponents of the leading layers;
- all determinant-one affine and triangular target normalizations;
- every source transformation claimed to preserve the filtration;
- explicit proof that the chosen reduction measure decreases.

## Central obstruction

In the `(2,2)` normalization, isolate the equation

```text
J(P_0,Q_2)+J(P_1,Q_1)+J(P_2,Q_0)=0.
```

The middle Wronskian `J(P_1,Q_1)` is the first correction absent from the defect-2 line-pencil mechanism.

Determine whether it can be:

1. removed by a filtration-compatible target automorphism;
2. removed by a polynomial filtered symplectic/source transformation;
3. shown to force forbidden Newton--Puiseux or boundary-monodromy data;
4. or realized by a consistent formal layer system.

## Accepted evidence

An accepted artifact must provide exact algebra, not only examples or computer output. Symbolic computation may validate identities, enumerate bounded cases, or discover countermodels, but every promoted implication requires a human-readable proof covering the declared case space.

## Forbidden shortcuts

- Do not treat the conversation-derived `kappa<=3` argument as established.
- Do not infer polynomial dependence from algebraic dependence of leading forms without proof.
- Do not use a transformation without proving preservation of `J=1` and strict descent.
- Do not use the retired boundary-excess identity.
- Do not infer a global cyclic extension from a Kummer model on one generic fiber.
- Do not infer principalization from exactness of a differential form.
- Do not broaden to arbitrary defect before defect 4 has an exact disposition.

## Required artifacts

- complete resonance/weight case table;
- exact derivation of all load-bearing identities;
- normalization catalogue for allowed transformations;
- adversarial falsification attempts and any formal countermodels;
- a theorem candidate, scoped obstruction, or smaller blocked invariant;
- claim-ledger and proof-graph updates;
- independent review bound to the identified claim and pinned revision, with `ACCEPT` or `BLOCK`; exact-byte hashes are optional provenance.

## Stop rule

Stop at the first exact scientific disposition:

1. all defect-4 cases reduce to smaller defect;
2. a substantial named subclass reduces;
3. a formal counterexample refutes the reduction ansatz;
4. a strictly smaller invariant obstruction is isolated and the reduction to it is proved.

Do not advertise a scoped result as a proof of `JC_2`.

## Handoff

Record:

- exact branch and commit;
- reviewed file hashes;
- source versions and hypotheses;
- equations checked independently;
- countermodels attempted;
- surviving resonance cases;
- the smallest next calculation.