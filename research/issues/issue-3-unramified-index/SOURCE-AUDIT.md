# Primary-Source Audit for Issue #3

```text
authority: MUTABLE_NONAUTHORITATIVE
protocol_verdict: null
base_commit: 296867d82d09d51ef2386de2a62067408b7f949c
source_policy: primary sources only for imported results
```

## 1. Scope

The countermodels, index determinants, mutation formulas, local criterion,
finite-prime patching, and degree-one contradiction are proved directly in
the issue artifacts. They do not depend on a classification theorem.

The only imported commutative-algebra results used as load-bearing
infrastructure are the finite-flatness criterion for the normalization and
the `R1/S2` normality criterion. The globalization packet also includes a
direct denominator-ideal proof, so the second citation is a cross-check rather
than an irreplaceable black box.

The finite-normalization/open-immersion input remains `CLM-003` and the
separate source-audit obligation in `L12`; this issue does not promote it.

## 2. Finite flatness over the regular surface

**Primary source.** A. Grothendieck and J. Dieudonne, *Elements de geometrie
algebrique IV: Etude locale des schemas et des morphismes de schemas, seconde
partie*, Publications Mathematiques de l'IHES **24** (1965), Proposition
6.1.5.

**Hypotheses consumed.** The target local ring is regular; the source local
ring is Cohen--Macaulay; the morphism is locally of finite type, maps closed
points to closed points, and satisfies the dimension formula.

**Application.** For the finite normalization `Y -> Spec(B)`, every fiber has
dimension zero, finite morphisms are closed, `B_m` is a two-dimensional
regular local ring, and every two-dimensional normal local ring `O_q` is
`S2`, hence Cohen--Macaulay. The dimensions agree under the finite integral
extension. Proposition 6.1.5 therefore gives flatness. Finite flat modules are
finite locally free.

The Auslander--Buchsbaum argument written in `THEOREM-PACKET.md` is an
alternative derivation of the same local freeness statement. No stronger
smoothness assertion is used.

## 3. `R1/S2` normality

**Primary source.** Grothendieck--Dieudonne, EGA IV, second part, Theorem
5.8.6.

**Hypotheses consumed.** A Noetherian ring is normal exactly when it satisfies
`R1` and `S2` (with the usual reducedness/domain hypothesis in the form used
here).

**Application.** `B[theta]` is a hypersurface domain, hence Cohen--Macaulay and
`S2`. Equality with the normalization at every height-one base prime makes
every height-one localization a DVR, hence `R1`. The theorem then gives
normality.

For audit independence, `THEOREM-PACKET.md` also proves directly that an `S2`
domain is the intersection of its height-one localizations by applying a
regular sequence to the denominator ideal. Thus no conclusion rests only on
the citation label.

## 4. Results proved inside the packet

The following are not imported from secondary literature:

1. the semilocal height-one object `O_p=O tensor_B B_p`;
2. the special-fiber criterion `B_p[theta]=O_p`;
3. the Fitting/index determinant and local length formula;
4. the square-index discriminant identity;
5. simultaneous generation at any prescribed finite set of height-one base
   primes;
6. the distinction between intrinsic ramification and excess Vandermonde
   contact;
7. the unit-coefficient criterion for finite-dimensional mutation families;
8. the derivative/minimal-polynomial proof that global monogenicity forces
   degree one in the Keller setting.

## 5. Citation boundary

No secondary source is used to establish a mathematical claim in this issue.
The primary references above are attached only to the exact standard results
consumed. The original counterexample and restricted theorems remain
`MUTABLE_NONAUTHORITATIVE` pending independent mathematical review.
