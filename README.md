# Planar Jacobian Research Mainline

> **Authority:** `MUTABLE_NONAUTHORITATIVE`  
> **Engineering status:** `DEVELOPMENT`  
> **Execution validity:** `NOT_A_SCIENTIFIC_EXECUTION`  
> **Protocol verdict:** `null`  
> **Scientific inference:** `none`


This repository is a durable research workspace for the two-dimensional Jacobian conjecture after the July 2026 three-dimensional counterexample. It memorializes two long exploratory conversations, separates candidate lemmas from retracted or literature-dependent claims, and exposes the surviving proof program as a dependency graph with agent-sized leaves.

The repository does **not** claim a proof of the planar conjecture. As of 2026-07-23, the published discussion around the new three-dimensional counterexample continues to describe the two-dimensional case as open. The immediate purpose is to prevent repeated rediscovery, make assumptions and gaps explicit, and let independent agents resume any proof branch from a bounded handoff packet.

## Start here

1. Read [`STATUS.md`](STATUS.md).
2. Read [`research/PROGRAM.md`](research/PROGRAM.md).
3. Inspect [`research/PROOF_GRAPH.md`](research/PROOF_GRAPH.md) or the machine-readable [`research/proof_graph.json`](research/proof_graph.json).
4. Select an open leaf in [`research/leaf-packets/`](research/leaf-packets/).
5. Read the corresponding track under [`research/tracks/`](research/tracks/).
6. Check every depended-on statement in [`research/CLAIM_LEDGER.md`](research/CLAIM_LEDGER.md).
7. Follow [`AGENTS.md`](AGENTS.md) and the governance files before changing claim status.

## Repository layers

- `archive/conversations/`: immutable raw exports and message-level topic index.
- `research/synthesis/`: broad narrative synthesis of both conversations.
- `research/tracks/`: parallel proof programs, including their honest current boundaries.
- `research/leaf-packets/`: bounded tasks that another agent can pick up without reconstructing the full history.
- `research/proof_graph.json`: dependency graph and frontier.
- `research/claim_ledger.json`: candidate, open, retired, and source-bound claims.
- `governance/`: scientific status, review, freeze, and handoff rules.
- `scripts/`: deterministic structural validators and frontier rendering.

## Current load-bearing question

The conversations repeatedly converge on one obstruction:

> A hypothetical planar Keller counterexample is locally rigid and locally étale on the affine plane, but its finite normalization can lose sheets at infinity. Can the boundary data be shown to force one global algebraic structure—such as a principal different, a global primitive element, a stable differential lattice, a complete canonical flow, or a finite quasi-Albanese map—that makes the normalization finite étale and therefore trivial?

No one bridge is currently established. The proof graph keeps the competing routes parallel rather than presenting one preferred speculation as settled.

## Validation

```bash
python3 scripts/validate_repository.py
python3 scripts/frontier.py
```

The first command checks graph integrity, claim references, artifact paths, and transcript hashes. It does not validate mathematical truth.

## Authority boundary

Raw conversations are provenance and idea input, not theorem authority. A statement may enter the maintained mainline only after:

- its exact formulation is recorded;
- primary sources are bound where it is literature-dependent;
- a self-contained proof or exact reduction is independently reviewed;
- known counterexamples and hidden hypotheses are checked;
- the claim ledger and proof graph are updated together.

See [`governance/CLAIM-STATUS.md`](governance/CLAIM-STATUS.md).
