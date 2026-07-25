# Canonical Construction Audit

> **Claims:** `CDS-003`, `CDS-004`, `CDS-006`, `CDS-008`  
> **Authority:** `MUTABLE_NONAUTHORITATIVE`

“Stable” below means exact stability under both ordinary canonical
translations, not logarithmic stability.

| Construction | Finite / coherent over \(B\) | Full generic fiber \(L\) | Differential behavior | Exact disposition |
|---|---:|---:|---|---|
| Normalization \(O\) | yes | yes | pair-stable iff no height-one ramification | canonical seed; saturation finite iff already stable |
| Source algebra \(A=\mathbf C[x,y]\) | not known | yes | exactly pair-stable | finiteness is the original nonproperness gap |
| \(\operatorname{Sat}_D(O)\) | iff no height-one ramification | yes | stable by definition | `CDS-003`; coherence is equivalent to the missing condition |
| \(\operatorname{Sat}_D(M_0)\), arbitrary finite full seed | not in general | yes | stable by definition | if finite, no height-one ramification |
| Fixed source pole module \(M(\mathbf N)\) | yes | yes | derivative shifts pole vector | any ramified stage, or any positive unramified pole stage, has nonfinite saturation |
| Directed union of all pole stages | generally not finite | yes | stable | ind-object only; no fixed finite ambient module |
| Reflexive hull of a pole stage | yes | yes | same height-one residues | no improvement |
| Finite intersection of pole stages/translates | yes | usually | not closed under all derivatives | complete saturation returns to the same obstruction |
| Multiplier ring \((M:M)\) | yes for finite \(M\) | yes when \(M\) full | stable only if \(M\) stable | converts an existing stable module to an order; does not create stability |
| Trace dual / inverse different | yes | yes | fractional classes integer-shifted | logarithmic at best; ordinary stability fails at ramification |
| Conductor dual / conductor power | yes, or zero for the source conductor | varies | integer shifts or no full module | no cancellation of \(j/e\) |
| Relative canonical module | yes | yes | determinant/dual shift | does not preserve every character under ordinary translations |
| Reflexive \(\operatorname{Hom}\) modules | yes under finite hypotheses | depends | dual residue classes | no automatic embedding as a stable full lattice in \(L\) |
| Deligne logarithmic lattice | yes | yes | stable under logarithmic fields | exists with ramification; insufficient |
| \(j_+\mathcal E\) / meromorphic localization | holonomic, often \(\mathcal O\)-infinite | yes | allows arbitrary poles | counterexample to holonomic \(\Rightarrow\) \(\mathcal O\)-finite |
| \(j_{!*}\mathcal E\) | regular holonomic | yes generically | underlying module is \(\mathcal O\)-coherent at a generic height-one point iff local inertia is trivial there | local diagnostic only; a direct global lattice also needs global coherence and a torsion-free embedding into \(L\) |
| \(j_*\mathcal O_U\) as quasi-coherent module | pole union | yes | stable as a union | not coherent in standard boundary models |
| \(j_!\) constructible extension | constructible/perverse notion | no direct module in \(L\) | categorical support condition | not a finite \(B\)-lattice |
| Relative de Rham \(H^0\) on finite-etale locus | finite vector bundle | yes | reproduces \(\mathcal E\) | inherits inertia; no improvement |
| Higher Gauss-Manin module | coherent under extra hypotheses | cohomology, not \(L\) | flat connection | wrong generic object unless a new embedding theorem is supplied |
| Compactly supported direct image | finite-dimensional/coherent in its category | not \(L\) | dual/support data | cannot be conflated with a full lattice |
| Dualizing complex / perverse dual | derived object | not directly | flips \(j_!,j_*\), dual residues | does not kill fractional classes |
| Finite-order boundary jets | yes | no or truncated | transverse derivative raises order | no finite stable jet stage |
| Determinant line | yes | rank one, not \(L\) | residue sum may be integral | loses individual tame characters |
| Finite original Keller map | yes, take \(A\) | yes | exactly stable | substantial but classical finite/proper subclass; degree one |

## Consequence

Every audited construction falls into one of four categories:

1. it is finite but ordinary stability is equivalent to no
   ramification;
2. it is stable only as an infinite pole union;
3. it is coherent only for logarithmic differential operators; or
4. it is a categorical/cohomological object whose generic fiber is
   not a full embedded lattice in \(L\).

No row supplies a new finite full pair-stable lattice under the
general Keller hypotheses.
