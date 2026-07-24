# Source and Provenance Inventory

> **Authority:** source inventory only. A URL, conversational attribution, or successful symbolic check does not certify theorem applicability.

## Bound source used by the equivariant lane

```text
T. Shaska
Graded Keller maps and the Jacobian Conjecture
arXiv:2607.20210v1 [math.AG]
submitted 2026-07-22
```

Maintained scope: an actual nontrivially `G_m`-equivariant planar Keller map is an automorphism under the theorem’s exact hypotheses. Issue #5 may consume this result only after constructing an algebraic action on source and target and proving preservation of the source open. The filtered Rees theorem `CLM-060` is an internal reviewed result and is not attributed to Shaska.

## Packet-specific source bindings

- Issue #3: [`issues/issue-3-unramified-index/SOURCE-AUDIT.md`](issues/issue-3-unramified-index/SOURCE-AUDIT.md).
- Issue #4: [`issue-4/stable-differential-order/source-bindings.md`](issue-4/stable-differential-order/source-bindings.md).
- Issue #5: [`issue-5/SOURCE_AUDIT.md`](issue-5/SOURCE_AUDIT.md).
- Defect four: [`audits/defect-4-primary-source-audit.md`](audits/defect-4-primary-source-audit.md).
- Independent defect-four review: [`../governance/reviews/issue-17-defect4-independent-gpt56.md`](../governance/reviews/issue-17-defect4-independent-gpt56.md).

## Primary-source audit queue

| Area | Named source family or identifier | Required check |
|---|---|---|
| graded Keller maps | Shaska, arXiv:2607.20210 | theorem number, all weight sign patterns, field and equivariance hypotheses |
| affine Lie algebra | Regeta, arXiv:1311.0232 | exact algebraicity/conjugacy implication and applicability to canonical fields |
| Brieskorn/Gauss–Manin | Dimca–Saito, arXiv:math/9906129 | finiteness, regularity, compactification, and polynomial hypotheses |
| surjective derivations | Gurjar–Masuda–Miyanishi, arXiv:1211.0744 | exact characteristic-zero and polynomial-ring hypotheses |
| compactification | Borisov and related work | boundary graphs, Stein factorization, and numerical limits |
| low-degree frontiers | Orevkov, Domrina, Żołądek, and cited sources | geometric versus topological degree and exact proved frontier |
| boundary normalization | Gurjar–Miyanishi and related sources | boundary components, singularities, normality, and affine-line fibrations |
| one-boundary models | Wright and cited sources | ring presentation, simple-polynomial theorem, unresolved cases |
| nonproperness | Jelonek and related sources | asymptotic set and covering-complement hypotheses in dimension two |
| monogenicity | primary literature on schemes of monogenic generators | local openness, integral generation, transition behavior, and globalization limits |
| filtered normal forms | polynomial symplectic and weighted automorphism literature | which filtration-compatible operations are polynomial and terminating |

## Review and provenance bindings

The reviewed defect-four candidate is pinned at `96fc7ec34bd3b685a0edeae7ecd4404abab7e2f1`, aggregate SHA-256 `21550a32815a617cdb108c41954fb422c66773656a560505aeefcbf180a4a097`. The independent `ACCEPT` and freeze record define the exact authority; symbolic validators are regression evidence only.

The declared conversation exports and hashes are recorded in [`../archive/manifest.json`](../archive/manifest.json). Both complete exports remain `metadata_only`; historical partial chunks do not reconstruct them. No missing source bytes were fabricated.

## Source-binding rule

Before a `literature_bound` claim becomes a load-bearing reviewed dependency:

1. record authors, title, stable identifier, version, and date;
2. identify the exact theorem and scope;
3. verify field, characteristic, degree convention, normality, smoothness, finiteness, properness, and action hypotheses;
4. check corrections or errata;
5. identify the exact claim IDs supported; and
6. explain why every hypothesis applies to the repository object.
