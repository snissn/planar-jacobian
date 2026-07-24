# Claim Ledger

> **Authority:** `MUTABLE_NONAUTHORITATIVE`

Statuses follow [`AGENTS.md`](../AGENTS.md). `CANDIDATE` means the argument appears self-contained in the research notes but has not passed a documented adversarial review for the claim at a pinned repository revision. A distinct reviewer is preferred; a declared local adversarial review is permitted when the environment does not support subagents or another reviewer.

| ID | Statement | Status | Notes / dependency |
|---|---|---|---|
| LIT-GRADED-01 | Every nontrivially `G_m`-equivariant planar Keller map is an automorphism for every sign pattern of the weights. | `LITERATURE` | T. Shaska, arXiv:2607.20210. |
| LIT-LIE-01 | Algebraicity/conjugacy of the canonical Keller-induced affine Lie algebra would imply the planar Jacobian conjecture. | `LITERATURE` | Regeta lane; verify exact theorem statement before reuse. |
| C-REES-01 | For positive weight `w=(p,q)`, the Rees deformation satisfies `J(Pcal,Qcal)=t^kappa`, where `kappa=deg_w P+deg_w Q-p-q`. | `CANDIDATE` | Direct chain-rule identity; requires adversarial sign/normalization audit. |
| C-STAIR-01 | Weighted layers satisfy `sum_{i+j=n}J(P_i,Q_j)=0` for `n<kappa` and `=1` for `n=kappa`. | `CANDIDATE` | Formal coefficient comparison from C-REES-01. |
| C-RESONANCE-01 | Some resonant pair `(P_i,Q_j)`, `i+j=kappa`, has nonzero constant Jacobian and hence is an exactly graded automorphism. | `CANDIDATE` | Uses positivity of source weights so weight-zero polynomials are constants, then LIT-GRADED-01. |
| C-TOP-RESONANCE-01 | If a resonant constant-Jacobian pair uses a top layer (`i=0` or `j=0`), the original map is an automorphism. | `CANDIDATE` | Lower-weight monomial classification after graded normalization must be audited. |
| C-DEFECT-LE3 | If `kappa_w<=3` for some positive primitive weight, then the Keller map is an automorphism. | `CANDIDATE` | Conversation-derived case analysis; highest-priority adversarial audit. |
| B-DEFECT-4 | Defect `4` contains a middle Wronskian such as `J(P_1,Q_1)` that defeats the lower-defect line-pencil reduction. | `BLOCKED` | Active leaf packet. |
| C-PRINCIPAL-DIFFERENT | A principal Kähler different for the finite normalization forces the original Keller map to be an automorphism. | `CANDIDATE` | Short localization/unit argument; audit Fitting-base-change and finite-etale steps. |
| C-CI-NORMALIZATION | A globally monogenic or relative complete-intersection normalization forces invertibility. | `CANDIDATE` | Consequence of C-PRINCIPAL-DIFFERENT; the monogenic degree-one implication is written noncircularly in issue #3. |
| C-INDEX-LOCAL-CRITERION | For an integral primitive `theta`, generation at a height-one base prime is equivalent to vanishing of `Cbar_p/B_p[theta]`, to a unit Fitting/index ideal, and to generation of the entire semilocal special fiber. | `CANDIDATE` | Issue #3 theorem packet; testing separate primes of `Cbar` over `p` is insufficient. |
| C-INDEX-RAMIFIED-PATCH | For every prescribed finite set of height-one primes of `B=C[P,Q]`, one integral primitive element generates all corresponding semilocal normalization algebras simultaneously. | `CANDIDATE` | Issue #3; apply the semilocal DVR generator lemma and principal-prime patching. In particular this handles all ramified height-one primes. |
| C-INDEX-R1S2-GLOBALIZE | If one integral primitive element generates `Cbar_p` over `B_p` for every height-one base prime, then `B[theta]=Cbar`. | `CANDIDATE` | Issue #3; `B[theta]` is a hypersurface and hence `S2`, while height-one equality gives `R1`. A direct intersection proof is also recorded. |
| C-MONOGENIC-DEGREE-ONE | If the Keller normalization is globally monogenic, then `[C(x,y):C(P,Q)]=1`. | `CANDIDATE` | Issue #3; after globalization, `Omega_{Cbar/B}=Cbar/(f'(theta))dtheta`, source etaleness makes `f'(theta)` a polynomial unit, and minimality forces degree one. |
| C-INDEX-ALGEBRAIC-OBSTRUCTION | Purely algebraic unramified-index elimination is false: a connected smooth normal finite-flat rational rank-three cover, locally monogenic everywhere and containing an open `A2`, can have no global power basis and can force every ramification-adapted element to acquire unramified index support. | `CANDIDATE` | Explicit issue #3 countermodel with index form `-(uX^3+X^2Y+vY^3)`. Its open affine plane is not etale over the base. |
| B-KELLER-INDEX-UNIT | For the actual Keller normalization, use etaleness on the specified open affine-plane source to construct an integral primitive element whose index ideal is a unit. | `BLOCKED` | Exact survivor of issue #3. Rationality, smoothness, local monogenicity, squarefree tame branching, a fixed sheet, an open `A2`, genericity, and divisor-class triviality are insufficient without source etaleness. |
| C-LOCAL-FINITE-EULER | Local finiteness of the canonical pulled-back Euler/hyperbolic derivation forces invertibility. | `CANDIDATE` | Uses algebraic torus linearization and weight analysis. |
| C-BRIESKORN-FINITE | Finiteness of one relative Brieskorn module over its pencil coordinate forces invertibility. | `CANDIDATE` | Gauss--Manin regularity step needs careful source binding and audit. |
| B-BOUNDARY-GLUING | Local primitive elements/differents at boundary divisors need not glue globally; proving principalization is a missing bridge. | `BLOCKED` | Issue #3 proves finite ramified-prime patching but supplies countermodels to purely algebraic global elimination. |
| R-EULER-EXCESS | `d=1+sum e_i+C_boundary` for a finite normalization. | `RETIRED` | Contradicted by the cusp model and based on an invalid Euler decomposition. |
| R-GENERIC-KUMMER | A finite Kummer cover on a generic `PQ` fiber makes `L/K` cyclic Galois. | `RETIRED` | Fiberwise cyclicity does not imply the full two-dimensional extension is Galois. |
| R-EXACT-FORM-PRINCIPAL | Exactness of the canonical two-form forces its zero divisor/canonical class to vanish. | `RETIRED` | Explicit Wright-type examples can have an exact canonical form with nonzero boundary divisor. |
| R-NUMERICAL-FRAMEWORK | Picard/intersection framework data alone force simplicity or realizability. | `RETIRED` | Numerical data do not determine puncture/braid monodromy or global polynomial gluing. |
| R-GENERIC-INDEX-AVOIDANCE | A generic primitive element, generic linear mutation, or pairwise distinct values on one fiber eliminate all codimension-one sheet collisions. | `RETIRED` | Issue #3 computes moving collision divisors and shows the exact condition is a global unit equation for the universal index form. |

## Promotion rule

A `CANDIDATE` may become `FROZEN_ACCEPTED` only after:

1. the exact statement, proof scope, claim IDs, and dependencies are identified;
2. all domains, degree conventions, and coordinate changes are explicit;
3. a documented adversarial review recomputes every load-bearing identity and returns `ACCEPT` for a pinned commit or repository revision;
4. the review declares whether it was an `independent-review` or a `local-adversarial-review`, with the local mode permitted when no distinct reviewer or subagent is available;
5. known counterexamples and edge cases are tested;
6. required validations pass and their results are recorded; and
7. any later material change to the accepted statement, proof, computation, transformation, or dependency is reviewed again.

Exact-byte manifests and artifact hashes may be retained as optional provenance, but they are not required for promotion. Editorial, formatting, link, and metadata-only changes do not automatically invalidate an accepted review.