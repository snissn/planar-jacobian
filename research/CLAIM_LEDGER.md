# Claim Ledger

> **Authority:** `MUTABLE_NONAUTHORITATIVE`

Statuses follow [`AGENTS.md`](../AGENTS.md). `CANDIDATE` means the argument appears self-contained in the research notes but has not passed independent exact-byte scientific review.

| ID | Statement | Status | Notes / dependency |
|---|---|---|---|
| LIT-GRADED-01 | Every nontrivially `G_m`-equivariant planar Keller map is an automorphism for every sign pattern of the weights. | `LITERATURE` | T. Shaska, arXiv:2607.20210. |
| LIT-LIE-01 | Algebraicity/conjugacy of the canonical Keller-induced affine Lie algebra would imply the planar Jacobian conjecture. | `LITERATURE` | Regeta lane; verify exact theorem statement before reuse. |
| C-REES-01 | For positive weight `w=(p,q)`, the Rees deformation satisfies `J(Pcal,Qcal)=t^kappa`, where `kappa=deg_w P+deg_w Q-p-q`. | `CANDIDATE` | Direct chain-rule identity; requires independent sign/normalization audit. |
| C-STAIR-01 | Weighted layers satisfy `sum_{i+j=n}J(P_i,Q_j)=0` for `n<kappa` and `=1` for `n=kappa`. | `CANDIDATE` | Formal coefficient comparison from C-REES-01. |
| C-RESONANCE-01 | Some resonant pair `(P_i,Q_j)`, `i+j=kappa`, has nonzero constant Jacobian and hence is an exactly graded automorphism. | `CANDIDATE` | Uses positivity of source weights so weight-zero polynomials are constants, then LIT-GRADED-01. |
| C-TOP-RESONANCE-01 | If a resonant constant-Jacobian pair uses a top layer (`i=0` or `j=0`), the original map is an automorphism. | `CANDIDATE` | Lower-weight monomial classification after graded normalization must be audited. |
| C-DEFECT-LE3 | If `kappa_w<=3` for some positive primitive weight, then the Keller map is an automorphism. | `CANDIDATE` | Conversation-derived case analysis; highest-priority adversarial audit. |
| B-DEFECT-4 | Defect `4` contains a middle Wronskian such as `J(P_1,Q_1)` that defeats the lower-defect line-pencil reduction. | `BLOCKED` | Active leaf packet. |
| C-PRINCIPAL-DIFFERENT | A principal Kähler different for the finite normalization forces the original Keller map to be an automorphism. | `CANDIDATE` | Short localization/unit argument; audit Fitting-base-change and finite-etale steps. |
| C-CI-NORMALIZATION | A globally monogenic or relative complete-intersection normalization forces invertibility. | `CANDIDATE` | Consequence of C-PRINCIPAL-DIFFERENT. |
| C-LOCAL-FINITE-EULER | Local finiteness of the canonical pulled-back Euler/hyperbolic derivation forces invertibility. | `CANDIDATE` | Uses algebraic torus linearization and weight analysis. |
| C-BRIESKORN-FINITE | Finiteness of one relative Brieskorn module over its pencil coordinate forces invertibility. | `CANDIDATE` | Gauss--Manin regularity step needs careful source binding and audit. |
| B-BOUNDARY-GLUING | Local primitive elements/differents at boundary divisors need not glue globally; proving principalization is a missing bridge. | `BLOCKED` | Common endpoint of normalization, puncture, and symmetry lanes. |
| R-EULER-EXCESS | `d=1+sum e_i+C_boundary` for a finite normalization. | `RETIRED` | Contradicted by the cusp model and based on an invalid Euler decomposition. |
| R-GENERIC-KUMMER | A finite Kummer cover on a generic `PQ` fiber makes `L/K` cyclic Galois. | `RETIRED` | Fiberwise cyclicity does not imply the full two-dimensional extension is Galois. |
| R-EXACT-FORM-PRINCIPAL | Exactness of the canonical two-form forces its zero divisor/canonical class to vanish. | `RETIRED` | Explicit Wright-type examples can have an exact canonical form with nonzero boundary divisor. |
| R-NUMERICAL-FRAMEWORK | Picard/intersection framework data alone force simplicity or realizability. | `RETIRED` | Numerical data do not determine puncture/braid monodromy or global polynomial gluing. |

## Promotion rule

A `CANDIDATE` may become `FROZEN_ACCEPTED` only after:

1. the exact statement and proof bytes are pinned;
2. all domains, degree conventions, and coordinate changes are explicit;
3. an independent reviewer recomputes every load-bearing identity;
4. known counterexamples and edge cases are tested;
5. the review disposition is bound to the exact commit and artifact hashes.
