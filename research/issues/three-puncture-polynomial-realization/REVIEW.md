# Local adversarial review

```text
review_mode: local-adversarial-review
reviewed_revision: 20f34c4c2ccf7289d436aad41e25f374ea40d1f3
reviewer_identity: same assistant as constructor
independent_review: false
disposition: ACCEPT_SCOPED_DISPLAYED_BRANCH_EXCLUSION; BLOCK_BROADER_PROMOTION
```

## Reviewed candidate

The renewed review is pinned to
`20f34c4c2ccf7289d436aad41e25f374ea40d1f3` and covers the exact scientific
files and symbolic checkers named in `INTEGRATION.json`. Metadata-only
follow-up commits do not alter the reviewed proof.

The prior review at `087fd32a1994a666f6e9d3aea445e1c0ba7bd687` did not
separate generic finiteness from the quasi-finiteness needed for the
Zariski-main open immersion. Exact-head Codex review exposed that scope defect.
The renewed candidate restricts the boundary-factorization theorem to
dominant quasi-finite polynomial maps while preserving the Keller corollary,
because a Keller map is étale and therefore quasi-finite.

## Reconstruction

The review separately recomputed:

1. the two Bézout identities making `Q` and `Q-1` units;
2. the isomorphism with `C[z,z^(-1),(z-1)^(-1)]`;
3. the polynomial representative of `R` and `P dQ=dR`;
4. Zariski-main factorization for a dominant quasi-finite source map and the
   equality `S_F=pi(Y-X)` by uniqueness of normalization;
5. the component argument for the displayed curve;
6. every hypothesis of Jelonek--Lasoń Theorem 3.2;
7. the exhaustive unit proof that every `A1->C` is constant;
8. the source-pole primitive term and rational denominator control.

No step requires a monomial valuation, semigroup classification, one-place at
infinity, or a conductor bound.

## Required mutations

| mutation | review result |
|---|---|
| remove one puncture | two-puncture `G_m` still has no nonconstant `A1` morphism |
| fill two punctures | remaining `A1` admits `t`; unit proof correctly fails |
| replace the exact form by `dz/z` | nonzero residue stops order-zero recursion |
| allow `P` or `Q` a denominator | rational family satisfies both identities; polynomial theorem no longer applies |
| omit polynomial `H` | terminal nonproperness contradiction still holds; Keller derivation would lose evidence |
| silently add a second boundary divisor | displayed curve remains a component of `S_F` |
| call formal algebraization global polynomial realization | rejected by explicit denominators |
| assume conductor trivial | rejected in general by cusp mutation; proved here |
| infer a Newton weight | rejected; no simultaneous monomialization is proved |
| keep generic finiteness but drop quasi-finiteness | `G(x,y)=(x,xy)` has a line fiber over the origin, and its degree-one finite normalization cannot contain the source as the required open subset |
| drop generic finiteness | the primary uniruledness theorem also no longer applies |

## Adversarial points checked

- A parametric curve supplied through a general point cannot switch
  irreducible components: its irreducible closure lies in one component.
- The displayed curve is a component of the **nonproperness set**, not merely
  of a finite branch locus, because its source divisor is omitted from the
  source open.
- Generic finiteness is sufficient for Jelonek--Lasoń Theorem 3.2 but not for
  the open-immersion boundary factorization. The latter is invoked only under
  the packet's stronger quasi-finite hypothesis.
- The primitive lies in the affine branch ring, so no conductor obstruction is
  smuggled into the global argument.
- Polynomial affine uniruledness is not replaced by rational projective
  uniruledness.
- The stronger global theorem is not mislabeled as a Laurent or
  exact-symplectic contradiction.
- Keller étaleness supplies quasi-finiteness, and the nonempty open image in
  the irreducible target supplies dominance and generic finiteness.

## Validation

The checker covers branch, unit, primitive, divisor, polynomial-curve,
source-pole, rational-control, and mutation identities. The renewed review ran
the default and enlarged Python 3.12 campaigns (117 and 137 exact assertions),
the repository validators, and the explicit `G(x,y)=(x,xy)` mutation. The
complete repository suite is delegated to the permanent read-only workflow at
the final PR head.

## Disposition

**ACCEPT** at mutable candidate scope for the exact displayed-branch theorem.

**BLOCK** any inference to all Liouville-exact branches, all one-boundary
models, a qualifying weight, a uniform ramification bound, or `JC_2`.
Independent review remains required for promotion.
