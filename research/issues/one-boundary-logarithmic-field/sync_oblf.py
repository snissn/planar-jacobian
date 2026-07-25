#!/usr/bin/env python3
"""Synchronize the one-boundary packet into maintained repository surfaces.

This script is intentionally issue-owned.  It is idempotent and may be run only
against the exact branch derived from main@114aefeaf98429a3bd08ca9429b4ceebd3d21e08
or a later tree that still ends at CLM-066 without conflicting OBLF allocation.
"""
from __future__ import annotations

import json
import subprocess
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[3]
PACKET = "research/issues/one-boundary-logarithmic-field/README.md"
MARKER = "## Integrated one-boundary successor (2026-07-24)"


def load_json(relative: str) -> dict[str, Any]:
    return json.loads((ROOT / relative).read_text(encoding="utf-8"))


def dump_json(relative: str, data: dict[str, Any]) -> None:
    (ROOT / relative).write_text(
        json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )


def replace_once(relative: str, old: str, new: str) -> None:
    path = ROOT / relative
    text = path.read_text(encoding="utf-8")
    if new in text:
        return
    if old not in text:
        raise RuntimeError(f"{relative}: expected synchronization anchor not found")
    path.write_text(text.replace(old, new, 1), encoding="utf-8")


def append_once(relative: str, section: str) -> None:
    path = ROOT / relative
    text = path.read_text(encoding="utf-8")
    first_line = section.strip().splitlines()[0]
    if first_line in text:
        return
    path.write_text(text.rstrip() + "\n\n" + section.strip() + "\n", encoding="utf-8")


def sync_claims() -> None:
    ledger = load_json("research/claim_ledger.json")
    claims = ledger["claims"]
    ids = [item["id"] for item in claims]
    if ids[-1] == "CLM-072":
        return
    expected = [f"CLM-{number:03d}" for number in range(1, 67)]
    if ids != expected:
        raise RuntimeError(
            "claim allocation moved or conflicted; rebuild synchronization from latest main"
        )

    for item in claims:
        if item["id"] == "CLM-057":
            item["note"] = (
                "Smallest surviving issue #5 bridge. The one-boundary successor "
                "excludes torus-invariant and purely unramified one-boundary subclasses "
                "at candidate scope, while CLM-072 records the remaining non-toric "
                "Laurent/conductor system. Regularity and zero residue still do not "
                "supply integration."
            )
            break

    claims.extend(
        [
            {
                "id": "CLM-067",
                "status": "candidate_proved",
                "track": "canonical-derivations",
                "statement": (
                    "For every irreducible reduced plane curve g=0 over C, "
                    "Der_C(C[P,Q])(-log g) is a free rank-two module, identified "
                    "with Syz(g_P,g_Q,-g); a logarithmic pair is a basis exactly "
                    "when its determinant is a nonzero constant multiple of g."
                ),
                "depends_on": [],
                "note": (
                    "Issue #5 one-boundary packet, OBLF-01. Freeness does not select "
                    "a complete or locally finite field; Saito's determinant criterion "
                    "is source-bound."
                ),
            },
            {
                "id": "CLM-068",
                "status": "candidate_proved",
                "track": "canonical-derivations",
                "statement": (
                    "For a locally finite logarithmic derivation of C[P,Q], the "
                    "additive Jordan semisimple and nilpotent parts remain logarithmic; "
                    "an integral semisimple part integrates to a target G_m action, "
                    "and after polynomial target linearization the invariant irreducible "
                    "branch equation is a diagonal semi-invariant."
                ),
                "depends_on": ["CLM-056", "CLM-067"],
                "note": (
                    "Issue #5 one-boundary packet, OBLF-02/03. Irrational weight ratios "
                    "are not made integral by scalar rescaling; a torus-closure "
                    "cocharacter can be a different field. No claim is made that every "
                    "branch admits such a field."
                ),
            },
            {
                "id": "CLM-069",
                "status": "candidate_proved",
                "track": "canonical-derivations",
                "statement": (
                    "For a finite normal affine cover Y->X that is finite etale off a "
                    "G_m-invariant divisor, a finite isogeny of the target G_m action "
                    "lifts algebraically to Y; if Y-U has one irreducible generically "
                    "ramified divisor, the lifted action preserves U."
                ),
                "depends_on": ["CLM-003", "CLM-053", "CLM-066", "CLM-068"],
                "note": (
                    "Issue #5 one-boundary packet, OBLF-04/05. This is a new "
                    "finite-isogeny lifting lemma accepted only by local adversarial "
                    "review; independent scrutiny is required before promotion."
                ),
            },
            {
                "id": "CLM-070",
                "status": "candidate_proved",
                "track": "canonical-derivations",
                "statement": (
                    "A nontrivial Keller normalization with one irreducible generically "
                    "ramified boundary divisor cannot have its reduced branch curve "
                    "preserved by a nontrivial target G_m action: after the isogeny lift "
                    "and source-open invariance, equivariance forces an automorphism and "
                    "empty boundary."
                ),
                "depends_on": ["CLM-001", "CLM-015", "CLM-016", "CLM-069"],
                "note": (
                    "Issue #5 one-boundary packet, OBLF-05. Conditional on T. Shaska, "
                    "arXiv:2607.20210v1, Theorem 3.3. This excludes coordinate-line, "
                    "weighted-homogeneous, weighted-cusp, and hyperbolic monomial "
                    "branches under the exact one-boundary hypotheses, not all smooth "
                    "branches."
                ),
            },
            {
                "id": "CLM-071",
                "status": "candidate_proved",
                "track": "normalization",
                "statement": (
                    "If a Keller normalization has exactly one boundary divisor and it "
                    "is generically unramified, purity makes the finite normalization "
                    "finite etale and connectedness forces degree one; purely unramified "
                    "one-boundary sheet loss is impossible."
                ),
                "depends_on": ["CLM-003", "CLM-005", "CLM-066"],
                "note": (
                    "Issue #5 one-boundary packet, OBLF-06; uses purity of branch locus "
                    "and triviality of connected finite etale covers of A2_C. It does "
                    "not address an unramified boundary component when other ramified "
                    "components are present."
                ),
            },
            {
                "id": "CLM-072",
                "status": "open_bridge",
                "track": "exact-symplectic",
                "statement": (
                    "For the remaining non-toric one-boundary class, solve the fixed "
                    "valuation/conductor compatibility system: leading source poles "
                    "satisfy n a' b-m a b'=0, while exactness determines but need not "
                    "kill higher principal parts."
                ),
                "depends_on": [
                    "CLM-023",
                    "CLM-057",
                    "CLM-067",
                    "CLM-068",
                    "CLM-069",
                    "CLM-070",
                    "CLM-071",
                ],
                "note": (
                    "Issue #5 one-boundary packet, OBLF-07/09. The system is finite "
                    "only after pole orders, ramification index, boundary normalization, "
                    "conductor algebra, and punctures are fixed; no uniform bound or "
                    "general one-boundary exclusion is proved."
                ),
            },
        ]
    )
    dump_json("research/claim_ledger.json", ledger)


def sync_graph() -> None:
    graph = load_json("research/proof_graph.json")
    nodes = graph["nodes"]
    node_by_id = {node["id"]: node for node in nodes}
    node_by_id["OPEN-BOUNDARY-POLE"]["title"] = (
        "Solve the non-toric one-boundary Laurent-conductor bridge"
    )
    node_by_id["OPEN-BOUNDARY-POLE"]["note"] = (
        "Issue #5 classifies logarithmic lifting, excludes G_m-invariant and "
        "purely unramified one-boundary subclasses at candidate scope, and leaves "
        "CLM-072: a fixed-type non-toric Laurent/conductor system."
    )
    if "RED-ONE-BOUNDARY-LOG" not in node_by_id:
        nodes.append(
            {
                "id": "RED-ONE-BOUNDARY-LOG",
                "title": "One-boundary logarithmic semisimple obstruction",
                "type": "reduction",
                "status": "active",
                "artifact": "issues/one-boundary-logarithmic-field/README.md",
                "note": (
                    "Candidate packet excludes torus-invariant generically ramified "
                    "and purely unramified one-boundary models; the general non-toric "
                    "fixed-type system remains open."
                ),
            }
        )

    wanted = [
        ("RED-NORMALIZATION", "requires", "RED-ONE-BOUNDARY-LOG"),
        ("RED-DERIVATIONS", "requires", "RED-ONE-BOUNDARY-LOG"),
        ("RED-SYMPLECTIC", "requires", "RED-ONE-BOUNDARY-LOG"),
        ("BR-WRIGHT", "supports", "RED-ONE-BOUNDARY-LOG"),
        ("RED-ONE-BOUNDARY-LOG", "supports", "OPEN-BOUNDARY-POLE"),
    ]
    existing = {(e["from"], e["kind"], e["to"]) for e in graph["edges"]}
    for source, kind, target in wanted:
        if (source, kind, target) not in existing:
            graph["edges"].append({"from": source, "to": target, "kind": kind})
    dump_json("research/proof_graph.json", graph)


def sync_queue() -> None:
    queue = load_json("research/work_queue.json")
    by_id = {item["id"]: item for item in queue["leaves"]}
    l03 = by_id["L03"]
    l03["title"] = "Non-Toric One-Boundary Laurent-Conductor Bridge"
    l03["claim_dependencies"] = [
        "CLM-014",
        "CLM-015",
        "CLM-023",
        "CLM-052",
        "CLM-053",
        "CLM-054",
        "CLM-055",
        "CLM-056",
        "CLM-057",
        "CLM-067",
        "CLM-068",
        "CLM-069",
        "CLM-070",
        "CLM-071",
        "CLM-072",
    ]
    l11 = by_id["L11"]
    for claim_id in ["CLM-070", "CLM-071", "CLM-072"]:
        if claim_id not in l11["claim_dependencies"]:
            l11["claim_dependencies"].append(claim_id)
    dump_json("research/work_queue.json", queue)


def sync_prose() -> None:
    replace_once(
        "README.md",
        "- **Issue #5 / radial field:** the packet records the logarithmic tangency criterion, full principal-part obstruction, and failure of regularity to imply algebraic integration. The actual Keller branch is not proved radial, and the leaf remains open.",
        "- **Issue #5 / one-boundary logarithmic field:** the predecessor packet classifies logarithmic lifting. The [one-boundary successor](research/issues/one-boundary-logarithmic-field/README.md) excludes, at mutable candidate scope, every generically ramified one-boundary model with a `G_m`-invariant reduced branch and every purely unramified one-boundary sheet-loss model. The general non-toric class remains open as `CLM-072`; exactness still permits higher principal parts.",
    )
    replace_once(
        "README.md",
        "python3 -m compileall -q scripts research/issues/issue-3-unramified-index research/issues/rank-three-index-form-unit research/issues/source-reflexive-lattice",
        "python3 -m compileall -q scripts research/issues/issue-3-unramified-index research/issues/rank-three-index-form-unit research/issues/source-reflexive-lattice research/issues/one-boundary-logarithmic-field",
    )
    replace_once(
        "README.md",
        "python3 scripts/validate_issue5_principal_parts.py\n",
        "python3 scripts/validate_issue5_principal_parts.py\npython3 research/issues/one-boundary-logarithmic-field/verify_all.py\n",
    )

    append_once(
        "research/leaf-packets/L03-radial-pole-elimination.md",
        f"""
{MARKER}

The successor packet [`../issues/one-boundary-logarithmic-field/README.md`](../issues/one-boundary-logarithmic-field/README.md) proves, at mutable candidate scope, that a nontrivial one-boundary Keller normalization cannot have a reduced branch preserved by a nontrivial target `G_m` action. It also excludes a unique generically unramified boundary by purity. Thus coordinate-line, weighted-homogeneous, weighted-cusp, and hyperbolic monomial branch subclasses are disposed under the exact one-boundary hypotheses.

The leaf remains open as `CLM-072`: for a branch with no target torus symmetry, solve the fixed valuation/conductor system beginning with `n a' b-m a b'=0`. No uniform bound on valuation or conductor types, and no general smooth one-boundary theorem, is claimed.
""",
    )
    replace_once(
        "research/leaf-packets/L03-radial-pole-elimination.md",
        "- **Status:** `OPEN — BLOCKED_BY_TANGENCY_AND_INTEGRATION`",
        "- **Status:** `OPEN — NARROWED_TO_NON_TORIC_COMPATIBILITY`",
    )
    replace_once(
        "research/leaf-packets/L03-radial-pole-elimination.md",
        "- **Dependencies:** CLM-003, CLM-007, CLM-014, CLM-015, CLM-022, CLM-023, CLM-052–CLM-057",
        "- **Dependencies:** CLM-003, CLM-007, CLM-014, CLM-015, CLM-022, CLM-023, CLM-052–CLM-057, CLM-067–CLM-072",
    )

    append_once(
        "research/leaf-packets/L11-exact-symplectic-boundary.md",
        f"""
{MARKER}

The issue #5 one-boundary packet derives the first additional common-valuation equation `n a' b-m a b'=0` and shows that the leading primitive coefficient is determined rather than forced to vanish. The torus-invariant and purely unramified one-boundary subclasses are excluded at candidate scope, but `CLM-072` remains open because exactness does not eliminate higher principal parts in the non-toric class.
""",
    )
    append_once(
        "research/tracks/b-canonical-derivations.md",
        f"""
{MARKER}

[`../issues/one-boundary-logarithmic-field/README.md`](../issues/one-boundary-logarithmic-field/README.md) records `CLM-067`–`CLM-070`: freeness of the one-curve logarithmic module, Jordan-part stability, a finite-isogeny action lift, and exclusion of a `G_m`-invariant reduced branch in the unique generically ramified boundary class. All remain mutable candidates; `CLM-072` is the non-toric successor.
""",
    )
    append_once(
        "research/tracks/g-wright-graded-single-tree.md",
        f"""
{MARKER}

The weighted-homogeneous one-boundary subclass is now excluded at candidate scope by `CLM-070`, provided the exact normalization and unique generically ramified boundary hypotheses hold. This does not supply the simultaneous graded reduction sought by `CLM-025`; it removes only the class in which an actual target grading already preserves the reduced branch.
""",
    )
    append_once(
        "research/tracks/i-exact-symplectic.md",
        f"""
{MARKER}

The one-boundary successor retains the full Laurent equations and adds the leading relation `n a' b-m a b'=0`. It explicitly rejects the inference from one boundary and zero residue to weighted homogeneity or pole elimination. The remaining fixed-type conductor/principal-part system is `CLM-072`.
""",
    )


def sync_validator_and_renderer() -> None:
    replace_once(
        "scripts/validate_repository.py",
        'expected_sequence = [f"CLM-{number:03d}" for number in range(1, 67)]',
        'expected_sequence = [f"CLM-{number:03d}" for number in range(1, 73)]',
    )
    replace_once(
        "scripts/validate_repository.py",
        '        error("CLM-059: fixed-section bridge must retain the universal-content correction")\n',
        '        error("CLM-059: fixed-section bridge must retain the universal-content correction")\n'
        '    for claim_id in ["CLM-067", "CLM-068", "CLM-069", "CLM-070", "CLM-071"]:\n'
        '        if by_id.get(claim_id, {}).get("status") != "candidate_proved":\n'
        '            error(f"{claim_id}: one-boundary successor result must remain candidate_proved")\n'
        '    if by_id.get("CLM-072", {}).get("status") != "open_bridge":\n'
        '        error("CLM-072: non-toric one-boundary compatibility system must remain open_bridge")\n'
        '    if "no uniform bound" not in by_id.get("CLM-072", {}).get("note", ""):\n'
        '        error("CLM-072: fixed-type reduction must retain its no-uniform-bound nonclaim")\n'
        '    if "arXiv:2607.20210v1" not in by_id.get("CLM-070", {}).get("note", ""):\n'
        '        error("CLM-070: terminal subclass exclusion must retain exact external dependency")\n',
    )
    replace_once(
        "scripts/render_views.py",
        '- **Issue #5:** regular lifting is classified by logarithmic tangency, and regularity is separated from algebraic integration. The Keller branch divisor is not proved radial; issue #5 remains open.',
        '- **Issue #5:** the one-boundary successor excludes torus-invariant generically ramified and purely unramified one-boundary subclasses at mutable candidate scope. The general non-toric Laurent/conductor system remains open as `CLM-072`; exactness still permits higher principal parts.',
    )


def sync_workflow() -> None:
    replace_once(
        ".github/workflows/repository-python-validators.yml",
        "run: python -m compileall -q scripts research/issues/issue-3-unramified-index research/issues/rank-three-index-form-unit research/issues/source-reflexive-lattice",
        "run: python -m compileall -q scripts research/issues/issue-3-unramified-index research/issues/rank-three-index-form-unit research/issues/source-reflexive-lattice research/issues/one-boundary-logarithmic-field",
    )
    replace_once(
        ".github/workflows/repository-python-validators.yml",
        '      - name: Add frontier to job summary\n',
        '      - name: "Validate issue #5 one-boundary successor"\n'
        '        shell: bash\n'
        '        run: |\n'
        '          set -o pipefail\n'
        '          python research/issues/one-boundary-logarithmic-field/verify_all.py | tee issue5-one-boundary.log\n\n'
        '      - name: Add frontier to job summary\n',
    )
    replace_once(
        ".github/workflows/repository-python-validators.yml",
        "            issue5-principal-parts.log\n",
        "            issue5-principal-parts.log\n            issue5-one-boundary.log\n",
    )


def write_sync_record() -> None:
    path = ROOT / "research/issues/one-boundary-logarithmic-field/SYNC_REPORT.md"
    path.write_text(
        """# Synchronization report

```text
source_main: 114aefeaf98429a3bd08ca9429b4ceebd3d21e08
candidate_revision: 02547f9a1c8c72486ad2bb07a06a10fde1351af4
review_revision: 3a96a48280228a7e38a4ca488109f90147d59b1c
allocated_claims: CLM-067 through CLM-072
leaf_status: OPEN
scientific_status: SUBCLASS_EXCLUSION_WITH_EXACT_REDUCTION
```

The synchronization allocates candidate claims, adds one active reduction node,
updates the open `L03` and supporting `L11` frontier, regenerates maintained
views, and adds exact-revision validation for the issue-owned symbolic checks.
It does not edit general governance files, mark the leaf reviewed, or create a
terminal edge to `JC_2`.
""",
        encoding="utf-8",
    )


def render() -> None:
    subprocess.run(
        ["python3", str(ROOT / "scripts/render_views.py"), "--write"],
        cwd=ROOT,
        check=True,
    )


def main() -> int:
    if not (ROOT / PACKET).is_file():
        raise RuntimeError("owned packet missing")
    sync_claims()
    sync_graph()
    sync_queue()
    sync_prose()
    sync_validator_and_renderer()
    sync_workflow()
    write_sync_record()
    render()
    print("OBLF shared synchronization: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
