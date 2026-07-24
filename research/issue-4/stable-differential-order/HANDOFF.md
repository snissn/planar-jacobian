# Handoff — Stable Differential Order

> **Authority:** `MUTABLE_NONAUTHORITATIVE`  
> **Protocol verdict:** `null`

- **Leaf and branch:** L02; `issue-4/stable-differential-order-gpt56`
- **Base commit:** `296867d82d09d51ef2386de2a62067408b7f949c`
- **Exact question:** construct a finite locally free `B=C[P,Q]`-order in `L=C(x,y)` stable under `D_P,D_Q`.
- **Disposition:** the implication from existence to degree one is written exactly; no order is constructed. A ramified height-one valuation forbids every finite full stable local lattice.
- **Candidate statements:** stable order implies unit discriminant, finite etaleness, and degree one; a transverse derivation on a characteristic-zero ramified DVR has positive differential escape and preserves no full lattice.
- **Formulas/objects introduced:** connection matrix `A`; trace Gram matrix `G`; escape slope `gamma_s(D)`; conductor orders `M_N=R+t^N S`; fractional residue classes `j/e mod Z`.
- **Primary sources checked:** Stacks Tags `0BJF`, `0B3D`, `00R4`, `00NT`, `00UP`, `0H94`, `09E9`, `09EV`, `0BRM`, `0EXT`, `0EYF`; SGA 1, Expose XII, Theorem 5.1.
- **Counterexamples and mutations tested:** Kummer `t=s^e`; conductor orders; bounded-pole modules; trace dual/inverse different; canonical module; finite intersections; logarithmic replacement; non-Galois cubic; cusp divisor; boundary-coordinate mutation; characteristic-`p` reduction.
- **Validation commands:** repository structural validators after synchronization; independent symbolic spot-checks for discriminant exponents and repeated derivatives are recommended but are not scientific review.
- **Blocking findings:** no stable order exists locally at ramified height one; no argument here proves all height-one ramification absent for a hypothetical Keller counterexample; no independent exact-byte reviewer has accepted the candidate.
- **Nonblocking strengthening:** formulate the tame residue obstruction intrinsically via the determinant connection or different; extend the local theorem to excellent DVRs without passing through completed factors in the exposition.
- **Claim-ledger changes:** refine CLM-011 with the matrix formula; promote only the implication CLM-013 from `open_bridge` to mutable `candidate_proved`; existence remains the open leaf.
- **Proof-graph changes:** keep `OPEN-STABLE-ORDER` open and annotate it with the ramified-DVR obstruction; do not mark `TERM-DEGREE-ONE` unblocked.
- **Smallest next action:** prove the following codimension-one equivalence without assuming finite etaleness: for the finite normalization `Cbar/B`, exact stability of one full reflexive lattice under the canonical frame is equivalent to vanishing of the ramification divisor. Then determine whether the Keller open immersion `C[x,y] subset Spec(Cbar)` supplies a canonical reflexive lattice across the unramified-but-nonproper locus.
- **Stop-rule status:** obstruction disposition reached; the existence leaf remains open.

## Smallest next calculation

Fix one irreducible asymptotic-value curve `h(P,Q)=0` and one valuation `w` of `L` above it. Compute, directly from the inclusion

```text
C[x,y] subset Cbar subset L,
```

the `w`-adic fractional residue spectrum of the two canonical derivations on the reflexive hulls

```text
(Cbar : h^m Cbar),
Hom_B(Cbar,B),
and conductor powers.
```

The local theorem predicts that a nonzero class `j/e mod Z` survives every integer shift when `e>1`. The next calculation should determine whether the Keller identity imposes any additional relation between the spectra for `D_P` and `D_Q` beyond transversality. A proof that it does not would close the entire bounded-lattice construction family as a class-level obstruction; a proof that it does would identify the only remaining cancellation mechanism.
