#!/usr/bin/env python3
"""One-shot final synchronization for the issue #4 source-lattice packet.

This script is committed only as a transport bootstrap.  It rewrites the
canonical shared surfaces, restores the permanent CI workflow, and deletes
itself before the synchronization commit is created.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def replace_once(text: str, old: str, new: str, label: str) -> str:
    if text.count(old) != 1:
        raise RuntimeError(f"{label}: expected exactly one source occurrence, found {text.count(old)}")
    return text.replace(old, new, 1)


def main() -> int:
    claim_path = ROOT / "research/claim_ledger.json"
    claims = json.loads(claim_path.read_text(encoding="utf-8"))
    by_id = {item["id"]: item for item in claims["claims"]}
    clm = by_id["CLM-061"]
    clm["statement"] = (
        "Construct a finite full B-lattice in L stable under both D_P and D_Q; "
        "its reflexive multiplier ring then gives the required finite locally free stable order."
    )
    clm["note"] = (
        "Issue #4 remains open. The source-reflexive-lattice packet proves that pair-stability is "
        "equivalent to height-one unramifiedness, that every finite divisorial source-pole stage "
        "escapes at ramification, and that multiplier closure is automatic. No finite pair-stable "
        "lattice is constructed."
    )
    claim_path.write_text(json.dumps(claims, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    graph_path = ROOT / "research/proof_graph.json"
    graph = json.loads(graph_path.read_text(encoding="utf-8"))
    node = next(item for item in graph["nodes"] if item["id"] == "OPEN-STABLE-ORDER")
    node["title"] = "Construct a finite full B-lattice stable under D_P,D_Q"
    node["note"] = (
        "CLM-011 and CLM-013 record the conditional implication. The source-reflexive-lattice "
        "successor proves the reflexive multiplier-ring bridge and excludes every finite divisorial "
        "pole stage at ramification. CLM-061 remains open at finite pair-stable lattice existence."
    )
    graph_path.write_text(json.dumps(graph, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    readme_path = ROOT / "README.md"
    readme = readme_path.read_text(encoding="utf-8")
    readme = replace_once(
        readme,
        "- **Issue #4 / stable order:** the stable-order-to-degree-one implication is a mutable "
        "conditional candidate, and the packet records a ramified-DVR no-lattice obstruction. "
        "Existence of a finite stable order remains open as `CLM-061`.",
        "- **Issue #4 / stable lattice:** the "
        "[source-reflexive-lattice packet](research/issues/source-reflexive-lattice/README.md) "
        "proves at mutable candidate scope that a finite full module stable under both canonical "
        "translations has a finite locally free stable multiplier order, and that every finite "
        "divisorial source-pole stage escapes at ramification. `CLM-061` remains open at existence "
        "of one finite pair-stable lattice; no such lattice is constructed.",
        "README issue #4 boundary",
    )
    readme = replace_once(
        readme,
        "python3 -m compileall -q scripts research/issues/issue-3-unramified-index research/issues/rank-three-index-form-unit",
        "python3 -m compileall -q scripts research/issues/issue-3-unramified-index research/issues/rank-three-index-form-unit research/issues/source-reflexive-lattice",
        "README compile command",
    )
    readme = replace_once(
        readme,
        "python3 scripts/validate_issue4_stable_order.py\n",
        "python3 scripts/validate_issue4_stable_order.py\n"
        "python3 research/issues/source-reflexive-lattice/verify_all.py\n",
        "README issue #4 checks",
    )
    readme_path.write_text(readme, encoding="utf-8")

    l02 = '''# Finite Stable Differential Order

- **Priority:** `P0`
- **Status:** `OPEN — SOURCE-POLE CONSTRUCTION CLASS OBSTRUCTED`
- **Dependencies:** CLM-010–CLM-013, CLM-061
- **Authority:** `MUTABLE_NONAUTHORITATIVE`
- **Protocol verdict:** `null`

## Load-bearing question

Construct a finite full `B=C[P,Q]`-lattice `M subset L=C(x,y)` invariant under both `D_P` and `D_Q`.

The source-reflexive-lattice successor proves that multiplicative closure need not be imposed on `M`: its reflexive multiplier ring

```text
O_M^ref = ({z in L : zM subset M})**
```

is a finite locally free stable `B`-order with total quotient field `L`. Therefore one finite full pair-stable module would enter the predecessor trace/discriminant route and force degree one.

## Current disposition

The predecessor packet proves at mutable candidate scope:

```text
finite locally free stable order
  => derivative-stable trace discriminant
  => unit discriminant
  => finite etale connected cover of A^2_C
  => degree one.
```

The successor packet sharpens the existence boundary:

1. for one derivation, a finite full stable lattice exists exactly when that derivation is logarithmic along every reduced ramified divisor;
2. a finite full lattice stable under both canonical translations exists exactly when the finite normalization has no height-one ramification;
3. the intrinsic local spectrum is the value-group quotient `(1/e)Z/Z`, with residue-degree multiplicity;
4. at `h(P,Q)=0`, the two spectra are the same scalar classes multiplied by the normal covector `(h_P,h_Q)`; a normal/tangent frame gives `(j/e,0)`, so commutativity supplies no cancellation;
5. the source algebra is the directed union of finite reflexive divisorial pole modules, but every ramified finite stage escapes, and every positive pole stage at an unramified omitted divisor escapes under a transverse member of the frame;
6. the multiplier-ring construction converts any hypothetical stable module into the required stable order.

Thus multiplicative closure is no longer the missing bridge. The unresolved step is finite-stage pair stability itself. No finite pair-stable lattice is constructed, and no planar Jacobian-conjecture conclusion is claimed.

## Accepted evidence

A successful construction requires all of:

- a finite-generation proof inside one fixed finite `B`-module;
- fullness: `M tensor_B K=L`;
- exact invariance under both canonical translations;
- a proof that the multiplier ring is finite, has total quotient field `L`, remains stable, and becomes locally free after reflexive closure;
- local bases or finite presentations and both derivation matrices;
- mutations detecting ramified, unramified-nonproper, logarithmic, and infinite-union failures.

A valid obstruction disposition must name a precise construction class and prove the obstruction for every member. The integrated successor does this for coherent divisorial source-pole stages, fixed conductor/different shifts, their reflexive hulls, and finite intersections. It does not rule out every conceivable finite non-divisorial construction.

## Forbidden shortcuts

- Do not use an infinite union of pole-order lattices as a finite module.
- Do not invoke Noetherian stabilization until all iterates lie in one fixed finite ambient module.
- Do not assume logarithmic stability implies exact translation stability.
- Do not require the initial module to be an algebra; derive and audit its multiplier order instead.
- Do not present a trace dual, inverse different, canonical module, or divisorial twist as stable merely because it is coherent or reflexive.
- Do not cancel residue representatives by integer shifts; work modulo `Z` and retain the full tame-character multiset.
- Do not infer that `dP wedge dQ=dx wedge dy` or an exact primitive removes higher poles.
- Do not assume finite etaleness, degree one, or finiteness of `C[x,y]` over `B` while constructing the lattice.

## Required artifacts

A construction must include the finite full module, both derivation matrices, the multiplier order, local-freeness and total-quotient-field proofs, discriminant control, and failure mutations. An obstruction must include the exact local spectrum, source-pole filtration, class coverage, countercontrols, and a declared review.

Current artifact set:

```text
research/issue-4/stable-differential-order/MAIN.md
research/issue-4/stable-differential-order/local-dvr-obstruction.md
research/issue-4/stable-differential-order/construction-audit.md
research/issue-4/stable-differential-order/source-bindings.md
research/issue-4/stable-differential-order/adversarial-review.md
research/issue-4/stable-differential-order/HANDOFF.md
research/issues/source-reflexive-lattice/README.md
research/issues/source-reflexive-lattice/LOCAL_RESIDUE_THEOREM.md
research/issues/source-reflexive-lattice/TWO_DERIVATION_SPECTRUM.md
research/issues/source-reflexive-lattice/SOURCE_POLE_FILTRATION.md
research/issues/source-reflexive-lattice/MULTIPLIER_RING.md
research/issues/source-reflexive-lattice/CANDIDATE_LATTICE_TABLE.md
research/issues/source-reflexive-lattice/COUNTERMODELS.md
research/issues/source-reflexive-lattice/REVIEW.md
research/issues/source-reflexive-lattice/HANDOFF.md
```

## Stop rule

Stop when either:

1. one finite full pair-stable module and its reflexive multiplier order are constructed and independently reviewed; or
2. a strictly larger, explicitly declared finite construction class is excluded by an independently reviewed obstruction.

The integrated packet reaches a constructor-reviewed class-level obstruction for divisorial source-pole constructions. Promotion remains blocked because the review is not independent. The leaf remains open.

## Handoff

Search for a finite **non-divisorial** source-derived module whose iterated canonical derivatives stay in one fixed finite ambient `B`-module. Before invoking Noetherianity, exhibit that ambient module and prove fullness. Any successful candidate automatically yields a stable order through the reflexive multiplier-ring construction; any divisorial bounded-pole candidate is already excluded by the fractional-residue theorem.
'''
    (ROOT / "research/leaf-packets/L02-stable-order.md").write_text(l02, encoding="utf-8")

    track = r'''# Track D — Stable Differential Lattice

> **Status:** `MUTABLE_NONAUTHORITATIVE`  
> **Protocol verdict:** `null`

Seek a finite full `B=C[P,Q]`-module `M subset L=C(x,y)` preserved by both canonical derivations `D_P,D_Q`. The source-reflexive-lattice successor proves that an algebra structure on `M` is not an additional hypothesis: the reflexive multiplier ring of any such module is a finite locally free stable `B`-order with total quotient field `L`.

## Audited implication

The predecessor issue #4 packet proves at mutable candidate scope:

1. in a local basis `e` of a finite locally free stable order, write `D(e)=eA`;
2. for the trace Gram matrix `G`,

   ```text
   delta(G)=A^T G+GA;
   ```

3. hence

   ```text
   delta(det G)=2 Tr(A)det G;
   ```

4. the trace-discriminant ideal is stable under `partial_P,partial_Q`;
5. every nonzero ideal of `C[P,Q]` stable under both partials is the unit ideal;
6. the order is finite etale and connected over `A^2_C`;
7. the function-field degree is one.

The successor supplies the module-to-order bridge. For a finite full stable module,

```text
O_M = {z in L : zM subset M}
```

is finite, stable, and generically `L`; its `B`-reflexive hull is an intersection of height-one localized rings and is locally free over the regular surface `B`. Therefore one finite full pair-stable module is sufficient for the audited implication.

## Sharp codimension-one theorem

For a fixed base derivation `delta`, a finite full stable lattice exists exactly when `delta` is logarithmic along every reduced ramified base divisor; in that case the normalization itself is stable.

For the pair `D_P,D_Q`, at least one member is transverse to every irreducible target divisor. Consequently:

```text
finite full pair-stable B-lattice
  <=> no height-one ramification in the finite normalization.
```

The right side is the full unramified DVR condition, including separable residue extension, not merely the numerical equation `e=1`.

## Fractional-residue spectrum

At a valuation of ramification index `e`, the intrinsic semisimplified tame spectrum is

```text
(1/e)Z / Z
```

with residue-degree multiplicity. At a branch `h(P,Q)=0`, the pair spectrum on the `j`-th tame character is

```text
(j/e)(h_P,h_Q).
```

A normal/tangent frame gives `(j/e,0)`. Integer lattice shifts move the scalar by an integer and cannot erase a nonzero class. The commuting residues are flat-compatible but do not cancel. The determinant-line sum `(e-1)/2` can be integral for odd `e`, so trace or determinant data alone lose the full obstruction.

## Source pole filtration

For the open immersion `j:U=Spec A -> Y=Spec O`, the ring direction is `O -> A`. No purity of `Y\U` is assumed. If `E_1,...,E_r` are its divisorial components, normality gives

```text
A = union_{m in N^r} Gamma(Y,O_Y(sum m_i E_i)).
```

Every fixed stage is coherent and finite over `B`; under the finite-flat surface package it is `B`-locally free. The canonical derivations shift pole bounds by finite vectors, but repeated derivatives grow linearly rather than remaining in one stage.

- ramified transverse increment: `e`;
- ramified logarithmic increment: `0`;
- unramified transverse boundary increment: `1`.

Every finite ramified stage is excluded by the local no-lattice theorem. At an unramified omitted divisor, `O` is locally stable but every stage admitting a genuine pole escapes under a transverse frame member. Commutativity controls ordering, not boundedness. The directed union is stable; no finite stage is.

## Canonical candidates and countercontrols

The successor audits the normalization, inverse different, trace dual, canonical module, conductor shifts, divisorial modules, colons, finite intersections, determinant lines, and multiplier rings. Rank-one reflexive fractional `O`-modules all have multiplier ring `O`, so they do not hide a new order.

Controls include Kummer and tame non-Galois ramification, a cusp branch, several boundary components, unramified nonproper boundary, logarithmic versus exact fields, a never-stabilizing pole union, characteristic-`p` collapse, and a Laurent exact-symplectic model. The last satisfies both `dP wedge dQ=dx wedge dy` and an exact primitive relation while retaining ramification; it is explicitly not a polynomial Keller pair on `A^2`.

## Current obstruction boundary

- `A=C[x,y]` is a pair-stable algebra but is not known finite over `B`.
- `O` is finite and locally free under the maintained surface hypotheses, but pair stability is equivalent to absence of height-one ramification.
- Every coherent divisorial pole stage, fixed conductor/different shift, reflexive hull, and finite intersection is excluded at a ramified component.
- Multiplier closure is automatic once a finite stable module exists.

The surviving route must therefore construct a finite non-divisorial source-derived module inside one fixed finite ambient module, or prove codimension-one unramifiedness by another argument.

## Issue-specific artifacts

- predecessor: `research/issue-4/stable-differential-order/`;
- successor: `research/issues/source-reflexive-lattice/`.

The successor's declared constructor adversarial review passes mutable integration but blocks promotion. No finite pair-stable lattice is constructed.

## Exit

The leaf remains open. It may close only with:

- a finite full module stable under both canonical translations, together with its audited reflexive multiplier order; or
- an independently reviewed obstruction covering a strictly larger exact construction class.
'''
    (ROOT / "research/tracks/d-stable-differential-lattice.md").write_text(track, encoding="utf-8")

    render_path = ROOT / "scripts/render_views.py"
    render_text = render_path.read_text(encoding="utf-8")
    render_text = replace_once(
        render_text,
        '        "- **Issue #4:** the stable-order-to-degree-one implication is recorded at mutable candidate scope, together with a ramified-DVR no-lattice obstruction. No finite stable order is constructed; issue #4 remains open.",',
        '        "- **Issue #4:** the source-reflexive-lattice successor proves at mutable candidate scope that a finite full pair-stable module yields a finite locally free stable multiplier order and that divisorial source-pole stages escape at ramification. No finite pair-stable lattice is constructed; issue #4 remains open.",',
        "generated STATUS issue #4 line",
    )
    render_path.write_text(render_text, encoding="utf-8")

    validator_path = ROOT / "scripts/validate_repository.py"
    validator = validator_path.read_text(encoding="utf-8")
    anchor = '''    if by_id.get("CLM-061", {}).get("status") != "open_bridge":
        error("CLM-061: stable-order existence must remain open_bridge")
'''
    addition = anchor + '''    if "finite full B-lattice" not in by_id.get("CLM-061", {}).get("statement", ""):
        error("CLM-061: source-reflexive successor must retain the finite full lattice bridge")
    if "No finite pair-stable lattice is constructed" not in by_id.get("CLM-061", {}).get("note", ""):
        error("CLM-061: successor synchronization must retain the finite-lattice nonclaim")
    source_lattice_root = ROOT / "research/issues/source-reflexive-lattice"
    required_source_lattice_files = [
        "README.md",
        "LOCAL_RESIDUE_THEOREM.md",
        "TWO_DERIVATION_SPECTRUM.md",
        "SOURCE_POLE_FILTRATION.md",
        "MULTIPLIER_RING.md",
        "CANDIDATE_LATTICE_TABLE.md",
        "COUNTERMODELS.md",
        "SOURCE_BINDINGS.md",
        "REVIEW.md",
        "HANDOFF.md",
        "CANDIDATE_MANIFEST.sha256",
        "verify_all.py",
        "verify_local_residues.py",
        "verify_filtration_and_symplectic.py",
    ]
    for relative in required_source_lattice_files:
        if not (source_lattice_root / relative).is_file():
            error(f"source-reflexive-lattice packet: missing {relative}")
    if source_lattice_root.is_dir():
        source_readme = (source_lattice_root / "README.md").read_text(encoding="utf-8")
        review_text = (source_lattice_root / "REVIEW.md").read_text(encoding="utf-8")
        if "O\\\\longrightarrow A" not in source_readme and "O -> A" not in source_readme:
            error("source-reflexive-lattice packet: ring orientation O -> A is missing")
        if "8ad9d542e5177a3240ad6c1f02b8b75e7657a085" not in review_text:
            error("source-reflexive-lattice review: reviewed candidate revision is not pinned")
        if "Promotion disposition:** `BLOCK`" not in review_text:
            error("source-reflexive-lattice review: promotion BLOCK is missing")
'''
    validator = replace_once(validator, anchor, addition, "CLM-061 validator anchor")
    validator_path.write_text(validator, encoding="utf-8")

    workflow_path = ROOT / ".github/workflows/repository-python-validators.yml"
    workflow = workflow_path.read_text(encoding="utf-8")
    workflow = replace_once(workflow, "  contents: write\n", "  contents: read\n", "workflow permissions")
    begin = "      # BEGIN ISSUE4 SELF-SYNC\n"
    end = "      # END ISSUE4 SELF-SYNC\n"
    start = workflow.find(begin)
    finish = workflow.find(end)
    if start == -1 or finish == -1 or finish < start:
        raise RuntimeError("workflow self-sync block not found")
    workflow = workflow[:start] + workflow[finish + len(end):]
    workflow_path.write_text(workflow, encoding="utf-8")

    Path(__file__).unlink()
    print("issue #4 shared synchronization prepared")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
