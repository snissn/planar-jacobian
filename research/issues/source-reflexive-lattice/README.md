# Source-Derived Reflexive Lattice and Fractional-Residue Packet

> **Authority:** `MUTABLE_NONAUTHORITATIVE`  
> **Protocol verdict:** `null`  
> **Issue:** `#4` — finite stable differential order  
> **Disposition:** `SCOPED_CLASS_OBSTRUCTION`  
> **Claim labels:** provisional `SRL-*`; no global claim status is promoted by this packet.

## Correct orientation and scope

Fix a planar Keller pair with Jacobian one and write

```text
B = C[P,Q],      K = Frac(B),
L = C(x,y),      O = normalization of B in L,
Y = Spec(O),     U = Spec(A) = A2_source.
```

The Zariski-main open immersion is

```text
j: U -> Y,
```

and its affine ring map has the required direction

```text
O -> A = C[x,y].
```

No argument below uses the reversed inclusion as a scheme map. Both rings are subrings of `L`, so the displayed map is also the inclusion `O subset A` inside the common function field.

Let `D=Y\U`. Its divisorial part is

```text
D_div = E_1 + ... + E_r,
```

where the `E_i` are the height-one irreducible components of the complement. Lower-dimensional components are retained in the geometric notation but do not change reflexive pole modules or regular functions on a normal surface.

The canonical lifted translations are

```text
D_P =  Q_y partial_x - Q_x partial_y,
D_Q = -P_y partial_x + P_x partial_y.
```

They commute, preserve `A`, and restrict to `partial_P,partial_Q` on `B`; they need not preserve `O`.

## Exact result

This packet proves, at mutable candidate scope, the following combined obstruction.

1. **Codimension-one equivalence (`SRL-001`).** A full finite reflexive `B`-lattice stable under the complete canonical frame exists exactly when the finite normalization has no height-one ramification. In the unramified direction the normalization `O` itself is the canonical lattice. Locally, one transverse derivation suffices; globally, both canonical derivations are required because neither fixed translation is transverse to every divisor.
2. **Intrinsic residues (`SRL-002`, `SRL-003`).** At a branch of ramification index `e`, the normalized logarithmic residue spectrum is the multiset `0,1/e,...,(e-1)/e mod Z`, with residue-degree multiplicity. For `D_P,D_Q`, the two raw residue operators are proportional to the normal covector `(h_P,h_Q)` and to one common grading operator. A tangential combination cancels its own normal pole, but every transverse combination retains the same nonintegral classes. Simultaneous integer shifts do not remove them.
3. **Source-pole filtration (`SRL-004`, `SRL-005`).** The source algebra is the union of coherent reflexive divisorial modules `O_Y(sum m_iE_i)`. Every fixed stage is finite over `B`. At any boundary divisor, a transverse canonical translation sends a pole of order `m>0` to successively deeper poles, with valuation dropping by the ramification index at every iteration. Thus no pole-bearing finite stage is stable, even when that boundary is unramified.
4. **Module-to-order bridge (`SRL-006`).** The multiplier ring of a full finite reflexive stable lattice is a finite locally free stable `B`-order with total quotient field `L`. Consequently a successful finite stable module would already produce the stable order required by the predecessor packet. For every rank-one reflexive `O`-fractional ideal, including every source-pole module, the multiplier ring is just `O`.
5. **Class-level disposition (`SRL-009`).** The open immersion does not canonically produce a proper finite stable lattice: ramification forbids every full finite lattice, while unramified boundary poles escape every finite source stage. The only pole-free canonical candidate left by this construction class is `O`; proving it stable is equivalent to eliminating height-one ramification.

This does **not** prove that the actual Keller normalization is unramified, finite étale, degree one, or that the planar Jacobian conjecture holds.

## Provisional claim map

| Label | Status in this packet | Statement |
|---|---|---|
| `SRL-001` | candidate proved | Global canonical-frame stable-lattice existence is equivalent to absence of height-one ramification. |
| `SRL-002` | candidate proved | The fractional residue spectrum is an intrinsic multiset in `Q/Z`, unchanged by uniformizer and lattice choices. |
| `SRL-003` | candidate proved | The two canonical residue operators are normal-covector multiples of one grading operator; the pair gives no cancellation beyond tangency. |
| `SRL-004` | candidate proved | `A` is the directed union of coherent reflexive divisorial pole modules, each finite over `B`. |
| `SRL-005` | candidate proved | Every pole-bearing finite source stage has unbounded transverse differential escape. |
| `SRL-006` | candidate proved | A full finite reflexive stable module yields a finite locally free stable multiplier order with quotient field `L`. |
| `SRL-007` | audited classification | The canonical candidate table records finiteness, reflexivity, multiplication, matrices, residues, and circularity. |
| `SRL-008` | candidate obstruction | The Keller symplectic identity and exact primitive identify denominators and coefficient relations but do not cancel fractional residues or higher source poles. |
| `SRL-009` | scoped class obstruction | The entire coherent source-pole-filtration construction class cannot produce a proper finite stable lattice. |
| `SRL-010` | open bridge | Eliminate actual Keller height-one ramification/divisorial boundary by an input not equivalent to assuming a stable lattice. |

## Artifact map

- [`LOCAL_RESIDUE_THEOREM.md`](LOCAL_RESIDUE_THEOREM.md) — local and global equivalence, strict henselization, completion, residue extensions, and characteristic-zero scope.
- [`TWO_DERIVATION_SPECTRUM.md`](TWO_DERIVATION_SPECTRUM.md) — intrinsic residue definition and the exact `D_P,D_Q` compatibility calculation.
- [`SOURCE_POLE_FILTRATION.md`](SOURCE_POLE_FILTRATION.md) — boundary purity audit, union theorem, finite-stage behavior, and escape calculation.
- [`MULTIPLIER_RING.md`](MULTIPLIER_RING.md) — finite-order construction and exact stability proof.
- [`CANDIDATE_LATTICE_TABLE.md`](CANDIDATE_LATTICE_TABLE.md) — required candidate-by-candidate audit.
- [`COUNTERMODELS.md`](COUNTERMODELS.md) — ramified, non-Galois, cusp, multi-boundary, unramified nonproper, logarithmic, and nonstabilizing controls.
- [`REVIEW.md`](REVIEW.md) — declared local adversarial review and inference boundary.
- [`HANDOFF.md`](HANDOFF.md) — exact surviving obstruction and next calculation.
- [`verify_source_reflexive_lattice.py`](verify_source_reflexive_lattice.py) — exact rational local-algebra regressions and artifact-contract checks.

## Predecessor and consumed packets

This packet consumes, without changing their authority:

- [`../../issue-4/stable-differential-order/MAIN.md`](../../issue-4/stable-differential-order/MAIN.md),
- [`../../issue-4/stable-differential-order/local-dvr-obstruction.md`](../../issue-4/stable-differential-order/local-dvr-obstruction.md),
- [`../../issue-4/stable-differential-order/construction-audit.md`](../../issue-4/stable-differential-order/construction-audit.md), and
- [`../../issue-5/PRINCIPAL_PARTS.md`](../../issue-5/PRINCIPAL_PARTS.md).

The stable-order implication remains conditional, and leaf [`L02`](../../leaf-packets/L02-stable-order.md) remains open.
