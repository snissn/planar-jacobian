# Issue #3 — Unramified Moving Index Divisor

```text
authority: MUTABLE_NONAUTHORITATIVE
engineering_status: DEVELOPMENT
execution_validity: NOT_A_SCIENTIFIC_EXECUTION
protocol_verdict: null
scientific_inference: scoped algebraic disposition only
base_commit: 296867d82d09d51ef2386de2a62067408b7f949c
base_ref: agent/bootstrap-proof-graph
branch: issue-3/unramified-index-gpt56
```

## Exact disposition

The moving-index route splits into three independent statements.

1. **Ramified height-one adaptation is valid.** For the finitely many ramified height-one primes of `B=C[P,Q]`, one integral element can be chosen to generate all corresponding semilocal DVR algebras simultaneously. The proof uses tame local monogenicity and a patching construction over the principal base primes. This supplies a complete proof candidate for `CLM-029`.
2. **Codimension-one generation globalizes.** If one integral primitive element generates `Cbar_p` over `B_p` for every height-one prime `p` of `B`, then `B[theta]` is `R1` and `S2`, hence normal, and therefore equals `Cbar`. Restriction to the Keller source then makes the derivative of the minimal polynomial a nonzero constant, forcing field degree one. This independently audits `CLM-034` and the degree-one implication in `CLM-008`.
3. **The purely algebraic unramified-elimination bridge is false.** A rank-three finite-flat normal algebra over `C[t,v]` is constructed which is Zariski-locally monogenic on the entire base but not globally monogenic. Every element generating all ramified height-one localizations has a nonempty index divisor contained in the finite étale locus. Constant and polynomial primitive-element mutations only move this divisor. Thus genericity, local monogenicity, class-group triviality of the base, and finite-dimensional parameter counts do not eliminate moving collisions.

The remaining bridge is necessarily Keller-specific. The two countermodels isolate what is not yet used: simultaneously, `L=C(x,y)`, an open immersion `A2_source -> Spec(Cbar)`, and étaleness on that source. Rationality alone and local monogenicity alone are both insufficient.

## Artifact map

- [`THEOREM-PACKET.md`](THEOREM-PACKET.md): precise quantifiers, local criterion, index/discriminant/different formulas, simultaneous ramification adaptation, `R1/S2` globalization, and the degree-one proof.
- [`COLLISION-DIVISORS.md`](COLLISION-DIVISORS.md): Galois-closure Vandermonde formulas, intrinsic versus accidental collisions, mutation criteria, primitive-element schemes, monodromy, and divisor-class limits.
- [`COUNTERMODELS.md`](COUNTERMODELS.md): the locally-but-not-globally monogenic rank-three algebra, a rational corank-two model, a biquadratic sheet-collision model, and tame non-Galois local tests.
- [`ADVERSARIAL-REVIEW.md`](ADVERSARIAL-REVIEW.md): separate self-adversarial audit; it is not an independent `ACCEPT`.
- [`PROPOSED-SYNC.md`](PROPOSED-SYNC.md): proposed claim-ledger, leaf, track, work-queue, and proof-graph changes.
- [`HANDOFF.md`](HANDOFF.md): exact surviving bridge and smallest next calculation.
- [`verify_index_models.py`](verify_index_models.py): optional exact SymPy recomputation of the finite multiplication, index, discriminant, and Vandermonde identities.
- [`ARTIFACT-MANIFEST.sha256`](ARTIFACT-MANIFEST.sha256): SHA-256 manifest for the issue-scoped candidate bytes, excluding the manifest itself.

## Source boundary

No new external theorem is used as a load-bearing step. Standard commutative-algebra facts are either proved at the scope consumed or stated with their hypotheses in the theorem packet. The finite-normalization/open-immersion baseline remains the repository's `CLM-003` dependency and is not promoted here; its primary-source audit remains in `L12`.
