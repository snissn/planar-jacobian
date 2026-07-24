# Primary-Source Bindings

> **Authority:** `MUTABLE_NONAUTHORITATIVE`  
> **Protocol verdict:** `null`  
> **Rule:** these bindings support background implications only; the local repeated-derivative obstruction is proved directly in this packet.

## 1. Finite locally free plus unit discriminant implies etale

**Source:** The Stacks Project, Section 49.3, “Discriminant of a finite locally free morphism,” especially Lemma 49.3.1, Tag `0BJF`.

**Bound statement:** for a finite locally free morphism, the morphism is etale exactly when its discriminant is empty; equivalently, the trace pairing is everywhere nondegenerate.

**Hypothesis map:**

- `Spec(M) -> Spec(B)` is finite locally free by the order hypothesis;
- the trace pairing is the multiplication trace on `M`;
- the derivative-stable ideal argument makes its determinant a unit;
- therefore the discriminant locus is empty.

**Claims supported:** CLM-011 and the finite-etale step of CLM-013.

## 2. Connected finite etale covers of `A^2_C`

**Source:** A. Grothendieck, *Revêtements étales et groupe fondamental (SGA 1)*, Lecture Notes in Mathematics 224, Springer, 1971, Expose XII (M. Raynaud), Theorem 5.1; recomposed edition A. Grothendieck and M. Raynaud, Documents Mathematiques 3, Societe Mathematique de France, 2003, arXiv:`math/0206203`.

**Bound statement:** finite etale covers of a complex algebraic variety correspond to finite topological covering spaces of its associated analytic space.

**Hypothesis map:**

- the base is `A^2_C`, whose analytification is `C^2`;
- `C^2` is contractible and therefore simply connected;
- the order is a domain, so the finite etale cover is connected;
- the corresponding connected finite topological cover has one sheet.

**Claim supported:** degree-one step of CLM-013.

## 3. Normal finite surface algebra is Cohen--Macaulay and locally free over the regular base

**Sources:**

- The Stacks Project, Tag `0B3D`: a locally Noetherian normal scheme of dimension at most two is Cohen--Macaulay.
- The Stacks Project, Tag `00R4`: miracle flatness under the regular-base, Cohen--Macaulay, and dimension hypotheses.
- The Stacks Project, Tag `00NT`: maximal Cohen--Macaulay modules over regular local rings are free.

**Bound use:** under the finite dominant equidimensional surface hypotheses, the normalization `Cbar` is finite locally free over `B`.

**Caution:** this does not apply automatically to an arbitrary nonnormal suborder. Such an order may fail `S2`, reflexivity, flatness, or local freeness.

**Claims supported:** background for CLM-004 and the normalization side of the existence tension.

## 4. Extension of derivations through etale maps

**Sources:**

- The Stacks Project, Tag `00UP`: formal etaleness and uniqueness of lifts.
- The Stacks Project, Tag `0H94`: differential operators extend uniquely through etale ring maps.

**Bound use:** a base derivation extends uniquely through finite etale/unramified base changes used in the strict-henselian reduction and preserves the etale algebra.

**Caution:** the unique extension to a ramified field exists because the field extension is separable, but it need not preserve the integral closure.

## 5. Tame DVR and Kummer local forms

**Sources:**

- The Stacks Project, Tag `09E9`: definitions of unramified, tame, and totally ramified finite extensions of DVRs.
- The Stacks Project, Tag `09EV`: the explicit Kummer DVR `A[pi^(1/e)]` and its ramification index.
- The Stacks Project, Tag `0BRM`: Abhyankar's lemma for tame ramification.
- The Stacks Project, Section 15.116, Tag `0EXT`, especially Lemma 15.116.7: characterization of tame extensions after adjoining a root of a uniformizer and an unramified extension.
- The Stacks Project, Tag `0EYF`: standard tame local models of the form `x^e=f` with `e` invertible.

**Bound use:** in residue characteristic zero, a ramified valuation factor may be tested after strict henselization in the model `t=s^e`; completion is not required for the valuation argument.

**Hypothesis map:**

- residue characteristic is zero, so every finite ramification index is tame;
- after strict henselization, residue extensions split; Hensel's lemma supplies `e`-th roots of units because `e` is invertible;
- stable lattices remain finite and stable after flat etale base change and projection to a field factor.

## 6. Direct calculations not delegated to sources

The following load-bearing statements are proved in the issue packet and do not rely on literature recollection:

- signs and values of `D_P,D_Q`;
- commutation by the vanishing of `K`-derivations on finite separable `L/K`;
- trace compatibility and `delta(G)=A^T G+GA`;
- `delta(det G)=2 Tr(A)det G`;
- derivative simplicity of nonzero ideals in `C[P,Q]`;
- repeated derivative formula in `t=s^e`;
- conductor-order multiplication tables, matrices, and discriminants;
- tame non-Galois cubic and cusp calculations;
- failure of bounded-pole, dual, conductor, intersection, logarithmic, and mod-`p` constructions.

## 7. Source-audit boundary

No source listed here is used to claim existence of a stable order or the planar Jacobian conjecture. Exact theorem numbering and applicability should receive independent review before any status beyond `MUTABLE_NONAUTHORITATIVE` is assigned.
