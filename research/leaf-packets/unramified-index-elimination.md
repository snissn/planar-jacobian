# Leaf Packet: Unramified Moving Index Divisor

> **Authority:** `MUTABLE_NONAUTHORITATIVE`  
> **Issue:** [#3](https://github.com/snissn/planar-jacobian/issues/3)  
> **Parent track:** [`../tracks/monogenicity-index-divisor.md`](../tracks/monogenicity-index-divisor.md)  
> **Disposition:** `SCOPED_ALGEBRAIC_OBSTRUCTION`

## Original load-bearing question

Can one construct an integral primitive element `theta in Cbar` that generates
every height-one semilocalization, in particular by eliminating all accidental
sheet-collision divisors in the finite etale locus?

## Exact disposition

The question splits into four statements.

1. **Finite-prime adaptation — candidate proved.** For every prescribed finite
   set of height-one base primes, one integral primitive element generates all
   corresponding semilocal normalization algebras. In particular, one element
   can be adapted simultaneously to every ramified divisor.
2. **Codimension-one globalization — candidate proved.** If one element
   generates at every height-one base prime, then `B[theta]=Cbar` by the exact
   `R1/S2` argument recorded in the theorem packet.
3. **Degree one after monogenicity — candidate proved.** The Keller source is
   introduced only after globalization; the derivative of the minimal
   polynomial then forces degree one without circularity.
4. **Pure algebraic elimination — false.** Explicit smooth rational rank-three
   countermodels show that every ramification-adapted element may acquire a
   nonempty index divisor at unramified generic points, even with local
   monogenicity everywhere, squarefree tame fixed-sheet branch, and an open
   affine plane.

## Surviving load-bearing question

For the actual Keller normalization, prove that source etaleness on the
specified open immersion

```text
A2_source -> Y
```

forces the universal index form to represent an element of `C*`.

The first exact case is rank three: after trace splitting, the index determinant
on the trace-zero rank-two bundle is a binary cubic. Construct a global section
on which that cubic is a nonzero constant, or derive an exact Keller-specific
identity that excludes the issue packet's anisotropic cubic patterns.

## Accepted evidence

A successful successor must supply one of:

- an integral primitive `theta` with `Fitt^B_0(Cbar/B[theta])=B`;
- a Keller-specific support theorem forcing every sheet-difference zero into
  the intrinsic ramification divisor, combined with ramified adaptation;
- an affine-transition theorem whose cocycle is proved to extend across the
  full base and to trivialize there;
- a restricted theorem, such as the rank-three binary index-form unit theorem;
- a still stronger countermodel satisfying additional Keller-near properties
  and naming the next missing hypothesis.

## Forbidden shortcuts

- checking primes of `Cbar` separately instead of `Cbar_p`;
- primitive-field generation in place of integral generation;
- generic separation on one fiber;
- a generic-parameter or dimension-count argument;
- adding `h(P,Q)` to a primitive element, since this changes no sheet
  difference;
- class-group triviality without effective-support control;
- Hartogs extension of individual functions without extension and
  trivialization of the primitive-element torsor;
- treating local monogenicity as global monogenicity.

## Work products already banked

- exact Fitting/index, discriminant, different, conductor, and Vandermonde
  formulas;
- necessary-and-sufficient height-one semilocal criterion;
- simultaneous ramified-prime patching;
- independently auditable `R1/S2` globalization;
- noncircular degree-one implication;
- linear and polynomial mutation criteria;
- Galois, non-Galois, corank-two, locally-but-not-globally monogenic, and smooth
  Keller-near countermodels;
- a separate adversarial review and exact handoff.

See [`../issues/issue-3-unramified-index/`](../issues/issue-3-unramified-index/README.md).

## Stop rule

The original generic algebraic bridge is disposed. Further work belongs to the
Keller-specific unit-index successor and must explicitly consume source
etaleness rather than repeating generic primitive-element arguments.