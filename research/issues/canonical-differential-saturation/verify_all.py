#!/usr/bin/env python3
"""Run packet regressions and validate the final issue-owned artifact contract."""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REQUIRED = {
    "README.md",
    "FOUNDATIONS.md",
    "DIFFERENTIAL_SATURATION.md",
    "DMODULE_ROUTE.md",
    "LOGARITHMIC_LATTICES.md",
    "LOCAL_RESIDUES.md",
    "CONSTRUCTION_TABLE.md",
    "COUNTERMODELS.md",
    "SOURCE_AUDIT.md",
    "REVIEW.md",
    "HANDOFF.md",
    "INTEGRATION.json",
    "verify_local_residues.py",
    "verify_global_bridges.py",
    "verify_all.py",
}


def run(script: str) -> None:
    """Execute one packet-local validator with the active interpreter."""
    subprocess.run([sys.executable, str(ROOT / script)], check=True)


def validate_manifest() -> None:
    """Check role, ownership, review pinning, and integration metadata."""
    manifest = json.loads((ROOT / "INTEGRATION.json").read_text())
    assert manifest["schema_version"] == 1
    assert manifest["issue_number"] == 4
    assert manifest["leaf_id"] == "L02"
    assert manifest["role"] == "research-worker"
    assert manifest["owned_paths"] == [
        "research/issues/canonical-differential-saturation/"
    ]
    assert manifest["base_sha"] == "652a5e252626fa5816445651245e8a8946cee53e"
    assert len(manifest["candidate_sha"]) == 40
    assert manifest["review_mode"] == "local-adversarial-review"
    assert manifest["reviewed_revision"] == manifest["candidate_sha"]
    assert manifest["pr_number"] == 42
    assert manifest["completion_receipt"] is None
    assert manifest["temporary_artifacts_absent"] is True
    assert manifest["integration_state"] == "integration-ready"
    for claim in manifest["proposed_global_claims"]:
        assert not str(claim.get("id", "")).startswith("CLM-")


def validate_prose() -> None:
    """Require key claims and reject known categorical or multiplier shortcuts."""
    combined = "\n".join(
        (ROOT / name).read_text()
        for name in REQUIRED
        if name.endswith(".md")
    )
    for label in ("CDS-001", "CDS-003", "CDS-005", "CDS-007"):
        assert label in combined
    forbidden = (
        "proves the planar Jacobian conjecture",
        "holonomic therefore O-coherent",
        "logarithmic therefore ordinary",
        "multiplier ring is stable only",
        "stable only when M_0 already is stable",
    )
    lower = combined.lower()
    for phrase in forbidden:
        assert phrase.lower() not in lower


def main() -> int:
    """Run exact identities and validate all required packet artifacts."""
    missing = sorted(name for name in REQUIRED if not (ROOT / name).is_file())
    if missing:
        print("missing required artifacts:", ", ".join(missing), file=sys.stderr)
        return 1
    run("verify_local_residues.py")
    run("verify_global_bridges.py")
    validate_manifest()
    validate_prose()
    print("canonical differential saturation packet: PASS")
    print(f"required artifacts: {len(REQUIRED)}")
    print("mathematical truth beyond encoded identities: NOT EVALUATED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
