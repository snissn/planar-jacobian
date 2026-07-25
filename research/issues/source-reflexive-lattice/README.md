# Source-Derived Reflexive Lattices and Fractional Residues

> **Authority:** `MUTABLE_NONAUTHORITATIVE`  
> **Scientific disposition:** `SCOPED_OBSTRUCTION_AND_EQUIVALENCE`  
> **Review status:** constructor adversarial review required before integration  
> **Issue:** `#4`  
> **Branch base:** `main@788e94419080debf356d17123cbf81cb23b391ac`

## Setup and ring orientation

Let

\[
B=\mathbf C[P,Q],\qquad K=\operatorname{Frac}(B),\qquad
L=\mathbf C(x,y),
\]

let `O` be the normalization of `B` in `L`, and put

\[
Y=\operatorname{Spec}O,\qquad U=\operatorname{Spec}A,
\qquad A=\mathbf C[x,y].
\]

The Zariski-Main open immersion is

\[
j:U\hookrightarrow Y,
\]

and its ring map has the direction

\[
\boxed{O\longrightarrow A.}
\]

No statement in this packet uses the reversed inclusion.  The complement
`Y\U` is not assumed pure of codimension one.  Its divisorial part controls
rational functions; any codimension-two remainder is invisible to regular
functions on a normal surface.

The canonical commuting derivations are

\[
D_P=Q_y\partial_x-Q_x\partial_y,\qquad
D_Q=-P_y\partial_x+P_x\partial_y,
\]

with

\[
D_P(P)=1,\,D_P(Q)=0,\qquad
D_Q(P)=0,\,D_Q(Q)=1.
\]

## Exact disposition

This packet does **not** construct a finite stable order.  It establishes the
following sharper boundary for the construction route.

1. For one base derivation, a finite full stable lattice exists exactly when
   that derivation is logarithmic along every reduced ramified base divisor;
   the normalization itself then supplies the lattice.
2. For the pair `(D_P,D_Q)`, a finite full stable `B`-lattice exists exactly
   when the finite normalization has no height-one ramification.  In the
   planar complex setting, purity and triviality of connected finite etale
   covers then force degree one.
3. The intrinsic fractional-residue spectrum at a valuation of ramification
   index `e` is the value-group quotient
   `(1/e)Z/Z`, with residue-degree multiplicity.  Integer lattice shifts do
   not remove its nonzero classes.
4. At a branch `h(P,Q)=0`, the two residues form one normal-direction class:
   on the `j`-th graded character they are
   `(j/e)(h_P,h_Q)`.  A normal/tangent change of frame reduces this to
   `(j/e,0)`.  Flatness adds no cancellation mechanism.
5. Every coherent finite stage of the source pole filtration fails pair
   stability at a ramified component.  At an unramified omitted divisor,
   every stage that actually admits a pole also escapes under a transverse
   member of the Keller frame.
6. For any finite full stable module `M`, its multiplier ring, followed by
   `B`-reflexive closure, is a finite locally free stable order with total
   quotient field `L`.  Thus multiplicative closure is not the remaining
   bridge: finite-stage differential invariance is.
7. The exact symplectic identity constrains the determinant line but does not
   erase the fractional character classes or bound the source pole union.

Accordingly, requested dispositions **(3)** and **(5)** are reached at
mutable candidate scope.  Disposition **(4)** holds only in the conditional
form “a finite pair-stable lattice forces no ramification”; the residue pair
alone is compatible with ramified local exact-symplectic models.

## Provisional claim map

| ID | Status | Statement |
|---|---|---|
| `SRL-001` | `candidate_proved` | The ring orientation is `O -> A`; codimension-two complement does not affect the rational-function pole filtration. |
| `SRL-002` | `candidate_proved` | For one derivation, existence of a finite full stable lattice is equivalent to logarithmic tangency along every reduced ramified divisor. |
| `SRL-003` | `candidate_proved` | A finite full lattice stable under both canonical translations exists iff there is no height-one ramification. |
| `SRL-004` | `candidate_proved` | The intrinsic fractional-residue spectrum is the tame value-group quotient, with residue-degree multiplicity, and is invariant under lattice shifts. |
| `SRL-005` | `candidate_proved` | The two canonical residue spectra are the normal covector times the same scalar classes; commutativity supplies no additional cancellation. |
| `SRL-006` | `candidate_proved` | `A` is the directed union of coherent divisorial pole modules; each finite stage is finite over `B` under the normalization hypotheses. |
| `SRL-007` | `candidate_proved` | Ramification forces unbounded escape from every finite pole stage; unramified omitted divisors still force escape once a stage admits a pole. |
| `SRL-008` | `candidate_proved` | The reflexive multiplier ring converts every finite full stable module into a finite locally free stable order. |
| `SRL-009` | `candidate_proved` | All audited canonical rank-one reflexive candidates have multiplier ring `O`; their residues are unchanged modulo integers. |
| `SRL-010` | `candidate_proved` | Exact symplectic and exact-primitive identities do not eliminate the local fractional spectrum. |
| `SRL-011` | `open_bridge` | Produce a finite full pair-stable lattice without already proving codimension-one unramifiedness, or find a genuinely non-divisorial finite source-derived construction. |

These labels are packet-local and provisional.  They do not silently allocate
or promote shared `CLM-*` claims.

## Artifacts

- `LOCAL_RESIDUE_THEOREM.md` — sharp one-derivation and two-derivation equivalences.
- `TWO_DERIVATION_SPECTRUM.md` — intrinsic pair spectrum and flatness audit.
- `SOURCE_POLE_FILTRATION.md` — exact union, finite stages, and escape bounds.
- `MULTIPLIER_RING.md` — module-to-order construction.
- `CANDIDATE_LATTICE_TABLE.md` — candidate-by-candidate audit.
- `COUNTERMODELS.md` — Kummer, non-Galois, cusp, logarithmic, boundary, and exact-symplectic controls.
- `SOURCE_BINDINGS.md` — primary-source hypothesis bindings.
- `REVIEW.md` — declared adversarial review.
- `HANDOFF.md` — smallest surviving successor.
- `verify_local_residues.py`, `verify_filtration_and_symplectic.py`, and
  `verify_all.py` — exact symbolic regression checks.

## Nonclaims

The packet does not prove that an arbitrary Keller normalization is
unramified, finite etale, or degree one.  It does not prove that `j_*O_U` is
coherent, that its pole filtration stabilizes, or that exactness removes
higher principal parts.  A successful check run is algebraic regression
evidence, not scientific acceptance.
