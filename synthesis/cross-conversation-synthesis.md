# Cross-Conversation Synthesis

## Shared spine

Both conversations converge on the same diagram. Let `B=C[P,Q]`, `A=C[x,y]`, and let `C` be the integral closure of `B` in `Frac(A)`. A hypothetical counterexample factors through a finite normalization `Y=Spec(C)` containing the affine source as an open subset. The map is étale on that open subset, while missing sheets are carried by the boundary.

The proof problem is to show that this boundary cannot exist.

## Equivalent-looking globalizers

The following are not asserted to be formally equivalent without hypotheses, but they are the main globalizers:

- **primitive element:** `C=B[theta]`;
- **stable order:** a finite `B`-lattice preserved by both lifted translations;
- **regular flow:** a canonical radial/affine vector field extends without poles;
- **finite quasi-Albanese:** the intrinsic map to `(G_m)^2` is finite;
- **trivial puncture module:** no finite asymptotic values remain on generic fibers;
- **graded reduction:** a one-boundary pair reduces to a homogeneous constant-bracket pair;
- **monodromy collapse:** cusp/tangency braid data cannot generate a transitive nonproper cover.

Every branch aims to convert local étaleness into a global finite étale map.

## Complementarity

Conversation A contributes detailed incidence geometry, graded rings, monogenicity, quasi-Albanese, and explicit boundary models. Conversation B contributes the canonical Lie frame, local-finiteness viewpoint, and a cleaner symmetry/globalization narrative.

## Program decision

No single branch is privileged as the proof. The repository keeps the branches parallel and shares only verified foundations. The highest-value work is on the narrow global bridges, not on producing additional reformulations of the same obstruction.
