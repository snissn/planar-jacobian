# Issue #3 Mainline Synchronization

> **Authority:** `MUTABLE_NONAUTHORITATIVE`
> **Source branch:** `issue-3/unramified-index-gpt56`
> **Source baseline:** `agent/bootstrap-proof-graph@296867d82d09d51ef2386de2a62067408b7f949c`
> **Integration base:** current `main`

The issue-scoped theorem, collision, countermodel, review, and handoff files are
preserved from the rich-baseline branch. References such as `CLM-029` through
`CLM-034` inside those files identify claims in that pinned baseline; they are
provenance identifiers, not IDs in the compact current-main ledger.

Current-main synchronization records the same mathematical disposition under
these ledger entries:

- `C-INDEX-RAMIFIED-PATCH`: simultaneous generation at any prescribed finite
  set of height-one base primes;
- `C-INDEX-R1S2-GLOBALIZE`: generation at every height-one semilocalization
  implies global monogenicity;
- `C-MONOGENIC-DEGREE-ONE`: a globally monogenic Keller normalization has
  function-field degree one;
- `C-INDEX-ALGEBRAIC-OBSTRUCTION`: the purely algebraic moving-index bridge is
  false even for a smooth rational rank-three cover containing an open affine
  plane;
- `B-KELLER-INDEX-UNIT`: the surviving bridge must use etaleness on the
  specified Keller source to force the universal index form to represent a
  unit.

No claim is promoted to `FROZEN_ACCEPTED` by transport or merge.