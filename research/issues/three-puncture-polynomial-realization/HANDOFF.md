# Handoff

```text
role: research-worker
task_issue: 5
coordinating_issue: 13
owned_path: research/issues/three-puncture-polynomial-realization/
base_sha: b4545bd9ca395c023b0d452feee29b5e6f77f83e
scientific_candidate: 20f34c4c2ccf7289d436aad41e25f374ea40d1f3
integration_state: integration-ready
```

## Result to preserve

The displayed smooth branch

```text
P Q^2(Q-1)^2+(Q-1)^2+Q^2=0
```

is impossible as the image of an omitted divisor in the finite-normalization
factorization of any dominant quasi-finite polynomial map `C^2->C^2`.
Consequently it is impossible for a polynomial Keller map, which is étale and
therefore quasi-finite.

The proof is:

```text
branch = P1-{0,1,infinity}
  => no nonconstant polynomial A1 curve
  + boundary image = component of S_F
  + Jelonek--Lasoń polynomial uniruledness of S_F
  => contradiction.
```

Exactness and conductor both survive: `R` belongs to the branch ring and has a
target-polynomial representative.

## Requested global synchronization

An integration maintainer should, after resolving the live ledger:

1. bank the exact displayed-branch exclusion at candidate scope;
2. mark the predecessor Liouville-exact polynomialization bridge disposed only
   for this one branch;
3. retain the general bridge for polynomially parametric Liouville-exact
   branches;
4. update the L03 and L11 leaves without implying a qualifying weight;
5. cite the exact primary-source theorem and local review binding.

No global claim ID is allocated here.

## Next smallest branch

The surviving class consists of Liouville-exact non-toric target branches that
**do** admit nonconstant polynomial `A1` curves. The next useful split is by
the normalization of such a polynomial curve and the behavior of the descended
primitive along its unique place at infinity. That is a new task; it is not
proved here.

## Nonclaims

No general one-boundary theorem, source semigroup classification, conductor
bound, ramification bound, simultaneous monomialization, qualifying weight, or
`JC_2` conclusion is requested.
