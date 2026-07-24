# Proof Graph

## Nodes

| ID | Title | Type | Status | Artifact |
|---|---|---|---|---|
| `ROOT-JC2` | Prove every planar Keller map is an automorphism | `goal` | `blocked` | — |
| `BASE-KELLER` | Fix F=(P,Q) with J(P,Q)=1 | `foundation` | `active` | — |
| `RED-NORMALIZATION` | Construct the finite normalization Y over A2 | `reduction` | `literature_bound` | tracks/a-normalization-boundary.md |
| `RED-BOUNDARY` | Classify and control Y\A2 and its ramification | `reduction` | `open` | tracks/a-normalization-boundary.md |
| `RED-DERIVATIONS` | Use the canonical commuting translation frame | `reduction` | `active` | tracks/b-canonical-derivations.md |
| `RED-SYMPLECTIC` | Exploit exact symplectic/Lagrangian structure | `control` | `active` | tracks/i-exact-symplectic.md |
| `BR-MONOGENIC` | Global primitive element route | `branch` | `open` | tracks/c-monogenicity-index-divisor.md |
| `OPEN-UNRAMIFIED-INDEX` | Eliminate the moving index divisor in the unramified locus | `leaf` | `open` | leaf-packets/L01-unramified-index-elimination.md |
| `BR-STABLE-LATTICE` | Finite differential order route | `branch` | `open` | tracks/d-stable-differential-lattice.md |
| `OPEN-STABLE-ORDER` | Construct a finite B-order stable under D_P,D_Q | `leaf` | `open` | leaf-packets/L02-stable-order.md |
| `BR-RADIAL` | Canonical radial-field pole elimination | `branch` | `open` | tracks/b-canonical-derivations.md |
| `OPEN-BOUNDARY-POLE` | Remove poles of one lifted radial field on Y | `leaf` | `open` | leaf-packets/L03-radial-pole-elimination.md |
| `BR-QUASI-ALBANESE` | Intrinsic torus-complement route | `branch` | `open` | tracks/e-quasi-albanese-log-geometry.md |
| `OPEN-QA-FINITE` | Prove the intrinsic quasi-Albanese map is finite | `leaf` | `open` | leaf-packets/L04-quasi-albanese-finiteness.md |
| `BR-GAUSS-MANIN` | Generic-fiber puncture and connection route | `branch` | `open` | tracks/f-gauss-manin-generic-fibers.md |
| `OPEN-PUNCTURE` | Force the puncture module to vanish | `leaf` | `open` | leaf-packets/L05-gauss-manin-punctures.md |
| `BR-WRIGHT` | One-boundary graded/Poisson route | `branch` | `open` | tracks/g-wright-graded-single-tree.md |
| `OPEN-GRADED-REDUCTION` | Retain a nonzero constant bracket under graded reduction | `leaf` | `open` | leaf-packets/L06-graded-reduction.md |
| `BR-MONODROMY` | Boundary monodromy/Galois closure route | `branch` | `open` | tracks/h-monodromy-galois-braid.md |
| `OPEN-CUSP-BRAID` | Eliminate nonabelian cusp/tangency braid monodromy | `leaf` | `open` | leaf-packets/L07-cusp-braid.md |
| `BR-DEGENERATION` | Equivariant degeneration and closed-orbit route | `branch` | `open` | tracks/j-equivariant-degeneration.md |
| `OPEN-CLOSED-ORBIT` | Prove a minimal counterexample has a closed torus orbit in a fixed boundary stratum | `leaf` | `open` | leaf-packets/L08-equivariant-closed-orbit.md |
| `BR-FILTERED-EQUIVARIANCE` | Weighted Rees staircase toward exact graded rigidity | `branch` | `open` | tracks/m-filtered-equivariance.md |
| `OPEN-DEFECT-4` | Audit the staircase and resolve grading defect 4 | `leaf` | `open` | leaf-packets/L13-defect-4-staircase.md |
| `BR-CHAR-P` | Characteristic-p and p-curvature route | `branch` | `speculative` | tracks/k-characteristic-p.md |
| `OPEN-PCURVATURE` | Turn reductions mod p into a finite-monodromy contradiction | `leaf` | `open` | leaf-packets/L09-characteristic-p.md |
| `CTL-LITERATURE` | Primary-source and low-degree audit | `control` | `active` | tracks/l-literature-low-degree.md |
| `OPEN-LITERATURE` | Resolve conflicting theorem statements and exact hypotheses | `leaf` | `open` | leaf-packets/L10-literature-audit.md |
| `CTL-3D` | Use the three-dimensional marked-root construction only as idea input | `context` | `active` | tracks/0-three-dimensional-context.md |
| `OPEN-SYMPLECTIC` | Derive a boundary theorem from exact symplectic principal parts | `leaf` | `open` | leaf-packets/L11-exact-symplectic-boundary.md |
| `OPEN-BOUNDARY-BASELINE` | Audit boundary/class-group/canonical-divisor foundations | `leaf` | `open` | leaf-packets/L12-normalization-baseline.md |
| `TERM-FINITE-ETALE` | Show the finite normalization is finite étale | `terminal` | `blocked` | — |
| `TERM-DEGREE-ONE` | Show the function-field degree is one | `terminal` | `blocked` | — |
| `TERM-AUTOMORPHISM` | Apply the birational/finite Keller conclusion | `terminal` | `blocked` | — |

## Edges

| From | To | Kind |
|---|---|---|
| `BASE-KELLER` | `RED-NORMALIZATION` | `requires` |
| `BASE-KELLER` | `RED-DERIVATIONS` | `requires` |
| `BASE-KELLER` | `RED-SYMPLECTIC` | `requires` |
| `BASE-KELLER` | `BR-FILTERED-EQUIVARIANCE` | `requires` |
| `RED-NORMALIZATION` | `RED-BOUNDARY` | `requires` |
| `RED-BOUNDARY` | `OPEN-BOUNDARY-BASELINE` | `requires` |
| `RED-NORMALIZATION` | `BR-MONOGENIC` | `requires` |
| `RED-NORMALIZATION` | `BR-STABLE-LATTICE` | `requires` |
| `RED-NORMALIZATION` | `BR-RADIAL` | `requires` |
| `RED-NORMALIZATION` | `BR-QUASI-ALBANESE` | `requires` |
| `RED-NORMALIZATION` | `BR-GAUSS-MANIN` | `requires` |
| `RED-NORMALIZATION` | `BR-WRIGHT` | `requires` |
| `RED-NORMALIZATION` | `BR-MONODROMY` | `requires` |
| `RED-NORMALIZATION` | `BR-DEGENERATION` | `requires` |
| `RED-NORMALIZATION` | `BR-CHAR-P` | `requires` |
| `RED-DERIVATIONS` | `BR-STABLE-LATTICE` | `requires` |
| `RED-DERIVATIONS` | `BR-RADIAL` | `requires` |
| `RED-DERIVATIONS` | `BR-GAUSS-MANIN` | `requires` |
| `RED-SYMPLECTIC` | `OPEN-SYMPLECTIC` | `requires` |
| `BR-MONOGENIC` | `OPEN-UNRAMIFIED-INDEX` | `requires` |
| `BR-STABLE-LATTICE` | `OPEN-STABLE-ORDER` | `requires` |
| `BR-RADIAL` | `OPEN-BOUNDARY-POLE` | `requires` |
| `BR-QUASI-ALBANESE` | `OPEN-QA-FINITE` | `requires` |
| `BR-GAUSS-MANIN` | `OPEN-PUNCTURE` | `requires` |
| `BR-WRIGHT` | `OPEN-GRADED-REDUCTION` | `requires` |
| `BR-MONODROMY` | `OPEN-CUSP-BRAID` | `requires` |
| `BR-DEGENERATION` | `OPEN-CLOSED-ORBIT` | `requires` |
| `BR-FILTERED-EQUIVARIANCE` | `OPEN-DEFECT-4` | `requires` |
| `OPEN-DEFECT-4` | `OPEN-GRADED-REDUCTION` | `supports` |
| `BR-FILTERED-EQUIVARIANCE` | `BR-DEGENERATION` | `supports` |
| `BR-CHAR-P` | `OPEN-PCURVATURE` | `requires` |
| `CTL-LITERATURE` | `OPEN-LITERATURE` | `requires` |
| `CTL-LITERATURE` | `BR-FILTERED-EQUIVARIANCE` | `supports` |
| `OPEN-UNRAMIFIED-INDEX` | `TERM-DEGREE-ONE` | `sufficient-if-closed` |
| `OPEN-STABLE-ORDER` | `TERM-DEGREE-ONE` | `sufficient-if-closed` |
| `OPEN-BOUNDARY-POLE` | `TERM-DEGREE-ONE` | `sufficient-if-closed` |
| `OPEN-QA-FINITE` | `TERM-DEGREE-ONE` | `sufficient-if-closed` |
| `OPEN-PUNCTURE` | `TERM-DEGREE-ONE` | `sufficient-if-closed` |
| `OPEN-GRADED-REDUCTION` | `TERM-DEGREE-ONE` | `sufficient-if-closed` |
| `OPEN-CUSP-BRAID` | `TERM-DEGREE-ONE` | `sufficient-if-closed` |
| `OPEN-CLOSED-ORBIT` | `TERM-DEGREE-ONE` | `sufficient-if-closed` |
| `OPEN-PCURVATURE` | `TERM-DEGREE-ONE` | `sufficient-if-closed` |
| `OPEN-SYMPLECTIC` | `TERM-DEGREE-ONE` | `sufficient-if-closed` |
| `OPEN-BOUNDARY-BASELINE` | `TERM-FINITE-ETALE` | `supports` |
| `TERM-FINITE-ETALE` | `TERM-DEGREE-ONE` | `requires` |
| `TERM-DEGREE-ONE` | `TERM-AUTOMORPHISM` | `requires` |
| `TERM-AUTOMORPHISM` | `ROOT-JC2` | `requires` |
| `CTL-3D` | `BR-MONODROMY` | `idea-input` |
| `CTL-3D` | `BR-DEGENERATION` | `idea-input` |
| `OPEN-LITERATURE` | `CTL-LITERATURE` | `updates` |

## Reading rule

An edge marked `sufficient-if-closed` means the leaf is intended to provide a complete route to degree one. It does not mean the leaf is close to solved. Context and control nodes cannot by themselves establish the goal.

The defect-4 leaf is a scoped subproblem supporting the full graded-reduction leaf. Closing defect 4 alone is not represented as sufficient for `JC_2`.