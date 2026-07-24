# Planar Jacobian Research Mainline

> **Authority:** `MUTABLE_NONAUTHORITATIVE`  
> **Engineering status:** `DEVELOPMENT`  
> **Execution validity:** `NOT_A_SCIENTIFIC_EXECUTION`  
> **Protocol verdict:** `null`  
> **Scientific inference:** `none`

This repository is a durable, dependency-tracked research workspace for the planar Jacobian conjecture. It imports two long July 2026 conversations, preserves them byte-for-byte in compressed form, separates usable lemmas from speculative bridges and withdrawn claims, and exposes the surviving work as a proof graph with agent-sized leaves.

**No file in this repository claims an unconditional proof of the planar Jacobian conjecture.** The current mainline is a research program and provenance archive.

## Start here

1. [`STATUS.md`](STATUS.md) — current frontier and nonclaims.
2. [`research/PROGRAM.md`](research/PROGRAM.md) — common problem spine.
3. [`research/PROOF_GRAPH.md`](research/PROOF_GRAPH.md) and [`research/proof_graph.json`](research/proof_graph.json) — branches and dependencies.
4. [`research/WORK_QUEUE.md`](research/WORK_QUEUE.md) — prioritized leaves.
5. [`research/CLAIM_LEDGER.md`](research/CLAIM_LEDGER.md) — exact claim status.
6. [`AGENTS.md`](AGENTS.md) — how to resume work without rediscovering the history.
7. [`archive/MANIFEST.md`](archive/MANIFEST.md) — lossless conversation archive.

## Repository layers

- `archive/`: original conversations, hashes, and a message-level topic index.
- `synthesis/`: narrative reconciliation and correction register.
- `research/tracks/`: parallel formal proof programs.
- `research/leaf-packets/`: bounded next tasks with stop rules and handoff contracts.
- `governance/`: status, review, source-audit, and freeze rules.
- `scripts/`: deterministic structural validation and frontier rendering.

## Current load-bearing question

A hypothetical planar Keller map is étale on the affine source but may lose sheets at infinity after finite normalization. Can the boundary data be shown to force one global object—such as a primitive element, a finite differential lattice, a regular canonical flow, a finite quasi-Albanese map, or a trivial puncture connection—that makes the normalization finite étale and therefore trivial?

## Validation

```bash
python3 scripts/validate_repository.py
python3 scripts/frontier.py
```

These checks validate repository structure, identifiers, graph closure, leaf references, and archive hashes. They do **not** validate mathematical truth.
