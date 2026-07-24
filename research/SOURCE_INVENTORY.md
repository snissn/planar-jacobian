# Source and Provenance Inventory

> **Authority:** source inventory only. A URL or conversational attribution does not certify that a repository paraphrase matches the source theorem.

## Bound source used by the filtered lane

```text
T. Shaska
Graded Keller maps and the Jacobian Conjecture
arXiv:2607.20210v1 [math.AG]
submitted 2026-07-22
```

Maintained scope: exact nontrivial `G_m`-equivariance in dimension two forces a Keller map to be an automorphism for every sign pattern of the weights. The filtered Rees claims are internal repository claims and are not attributed to this paper.

## Primary-source audit queue

| Area | Named source family or identifier | Required check |
|---|---|---|
| graded Keller maps | T. Shaska, arXiv:2607.20210 | theorem statement, all sign patterns, field and equivariance hypotheses |
| affine Lie algebra | A. Regeta, arXiv:1311.0232 | exact implication, algebraicity/conjugacy hypothesis, relation to canonical Keller fields |
| Weyl-module/Jacobian structures | V. Bavula, arXiv:2112.03177 | exact module statement and relevance to the maintained derivations |
| Brieskorn and Gauss–Manin at infinity | A. Dimca and M. Saito, arXiv:math/9906129 | finiteness, regularity, compactification, and polynomial hypotheses |
| surjective derivations | R. V. Gurjar, K. Masuda, M. Miyanishi, arXiv:1211.0744 | exact characteristic-zero and polynomial-ring hypotheses |
| compactification frameworks | A. Borisov, arXiv:1901.04073, and related work | boundary graphs, Stein factorization, and limits of numerical data |
| Newton/inner-polynomial restrictions | arXiv:2408.01279 and cited primary literature | exact degree notion, inner-polynomial hypotheses, compatibility with weighted layers |
| low-degree frontiers | Orevkov; Domrina; Żołądek and cited primary literature | geometric vs topological degree and the exact proved frontier |
| boundary normalization | Gurjar–Miyanishi and related primary sources | boundary components, singularities, affine-line fibrations, normality assumptions |
| one-boundary models | Wright and cited sources | ring presentation, simple-polynomial theorem, unresolved cases |
| irreducible fibers | Kaliman and related sources | exact reduction statement and field/hypothesis match |
| nonproperness | Jelonek and related sources | asymptotic set, covering complement, and dimension-two hypotheses |
| monogenicity | primary literature on schemes of monogenic generators | local openness, transition behavior, and globalization limits |
| affine-plane fibrations | Kraft–Russell and related results | local triviality over curves and all hypotheses |
| T-varieties | Altmann–Hausen | graded/polyhedral-divisor encoding and applicability |
| filtered normal forms | polynomial symplectic and weighted automorphism literature | which filtration-compatible transformations are polynomial and terminating |

## Scientific workflow sources

- [`snissn/skills/scientific-mainline-workflow`](https://github.com/snissn/skills/tree/main/scientific-mainline-workflow)
- [workflow skill file](https://github.com/snissn/skills/blob/main/scientific-mainline-workflow/SKILL.md)
- [scientific review checklist](https://github.com/snissn/skills/blob/main/scientific-mainline-workflow/references/scientific-review-checklist.md)

The repository-specific pin is recorded in [`../governance/SCIENTIFIC-WORKFLOW.md`](../governance/SCIENTIFIC-WORKFLOW.md).

## Conversation provenance

The declared source exports are:

- `chatgpt-export-2026-07-24.md` — 226 messages;
- `chatgpt-export-2026-07-24(2).md` — 78 messages.

Their declared byte counts and hashes are in [`../archive/manifest.json`](../archive/manifest.json). Both remain `metadata_only`; the complete bytes are unavailable and were not reconstructed. Conversation material is idea input and provenance, not theorem authority.

## Source-binding rule

Before a `literature_bound` claim becomes a load-bearing accepted dependency:

1. record authors, title, stable identifier, version, and date;
2. quote the exact theorem number and scope;
3. verify field, characteristic, degree convention, smoothness, normality, finiteness, and properness assumptions;
4. check corrections or errata;
5. identify the exact claim-ledger entries supported; and
6. explain why the hypotheses apply to the repository object.
