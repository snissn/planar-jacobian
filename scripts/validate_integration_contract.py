#!/usr/bin/env python3
"""Validate packet ownership, PR roles, temporary artifacts, and read-only CI."""
from __future__ import annotations

import argparse, json, os, re, subprocess, sys, urllib.request
from dataclasses import dataclass
from pathlib import Path
from typing import Any

SHA = re.compile(r"^[0-9a-f]{40}$")
ROLES = {"research-worker", "reviewer", "integration-maintainer", "governance-maintainer"}
REVIEWS = {"none", "independent-review", "local-adversarial-review"}
STATES = {"construction", "review", "integration-ready", "merged", "blocked"}
SHARED = {"README.md", "STATUS.md", "research/claim_ledger.json", "research/CLAIM_LEDGER.md", "research/proof_graph.json", "research/PROOF_GRAPH.md", "research/work_queue.json", "research/WORK_QUEUE.md", "research/ISSUE_INDEX.md"}
FIELDS = {"schema_version", "issue_number", "leaf_id", "role", "owned_paths", "base_sha", "candidate_sha", "scientific_status", "review_mode", "reviewed_revision", "proposed_global_claims", "proposed_graph_nodes", "shared_surfaces_requested", "supersedes_prs", "temporary_artifacts_absent", "integration_state"}
OPTIONAL = {"pr_number", "completion_receipt"}
WORKFLOW = ".github/workflows/repository-python-validators.yml"

@dataclass
class PullRequestContext:
    number: int; draft: bool; base_ref: str; base_sha: str; head_sha: str; body: str; repository: str

@dataclass
class Result:
    errors: list[str]; warnings: list[str]
    def error(self, message: str) -> None: self.errors.append(message)
    def warning(self, message: str) -> None: self.warnings.append(message)

def packets(root: Path) -> list[Path]:
    parent = root / "research/issues"
    return sorted(p for p in parent.iterdir() if p.is_dir() and any(p.iterdir())) if parent.is_dir() else []

def owned(path: str, roots: list[str]) -> bool:
    return any(path == r.rstrip("/") or path.startswith(r.rstrip("/") + "/") for r in roots)

def read_manifest(path: Path, root: Path, result: Result) -> dict[str, Any]:
    try: value = json.loads(path.read_text())
    except Exception as exc:
        result.error(f"{path.relative_to(root)}: invalid JSON: {exc}"); return {}
    if not isinstance(value, dict): result.error(f"{path.relative_to(root)}: manifest must be an object"); return {}
    rel = path.relative_to(root).as_posix()
    missing, unknown = FIELDS - set(value), set(value) - FIELDS - OPTIONAL
    if missing: result.error(f"{rel}: missing fields {sorted(missing)}")
    if unknown: result.error(f"{rel}: unknown fields {sorted(unknown)}")
    if value.get("schema_version") != 1: result.error(f"{rel}: schema_version must be 1")
    if not isinstance(value.get("issue_number"), int) or value.get("issue_number", 0) < 1: result.error(f"{rel}: invalid issue_number")
    if not value.get("leaf_id"): result.error(f"{rel}: leaf_id is required")
    if value.get("role") not in ROLES: result.error(f"{rel}: invalid role")
    if value.get("integration_state") not in STATES: result.error(f"{rel}: invalid integration_state")
    for field in ("base_sha", "candidate_sha"):
        if not SHA.fullmatch(str(value.get(field, ""))): result.error(f"{rel}: invalid {field}")
    mode, revision = value.get("review_mode"), value.get("reviewed_revision")
    if mode not in REVIEWS: result.error(f"{rel}: invalid review_mode")
    if mode == "none" and revision is not None: result.error(f"{rel}: reviewed_revision must be null")
    if mode != "none" and not SHA.fullmatch(str(revision or "")): result.error(f"{rel}: reviewed_revision required")
    roots = value.get("owned_paths")
    if not isinstance(roots, list) or not roots: result.error(f"{rel}: owned_paths must be nonempty"); roots = []
    packet_root = path.parent.relative_to(root).as_posix() + "/"
    if packet_root not in roots: result.error(f"{rel}: owned_paths must include {packet_root}")
    for field in ("proposed_global_claims", "proposed_graph_nodes", "shared_surfaces_requested", "supersedes_prs"):
        if not isinstance(value.get(field), list): result.error(f"{rel}: {field} must be an array")
    if value.get("temporary_artifacts_absent") is not True: result.error(f"{rel}: temporary_artifacts_absent must be true")
    if value.get("integration_state") == "merged" and value.get("role") not in {"integration-maintainer", "governance-maintainer"}: result.error(f"{rel}: merged packet needs maintainer role")
    return value

def scan_tree(root: Path, result: Result) -> None:
    try:
        tracked = subprocess.check_output(["git", "ls-files"], cwd=root, text=True, stderr=subprocess.DEVNULL).splitlines()
        paths = [root / rel for rel in tracked]
    except Exception:
        paths = [path for path in root.rglob("*") if path.is_file()]
    for path in paths:
        if not path.is_file(): continue
        rel, name = path.relative_to(root).as_posix(), path.name
        low = rel.lower()
        if name.endswith(".b64") and not rel.startswith("archive/conversations/"): result.error(f"forbidden base64 transport payload: {rel}")
        if name in {".integration-ready", ".local-review-complete"}: result.error(f"forbidden readiness marker: {rel}")
        if rel.startswith("research/issues/") and (name == "SYNC_REPORT.md" or (name.startswith("sync_") and name.endswith(".py"))): result.error(f"integration-only file on main: {rel}")
        if path.parent == root and (name.endswith(".log") or name.endswith(".zip") or name.endswith(".tar.gz")): result.error(f"forbidden root artifact: {rel}")
        if rel.startswith(".github/") and any(x in low for x in ("workspace-export", "workspace_upload", "one-shot", "rebuild", "-sync/")): result.error(f"forbidden GitHub transport path: {rel}")
    workflow_dir = root / ".github/workflows"
    if not workflow_dir.is_dir(): result.error("missing .github/workflows"); return
    for path in workflow_dir.glob("*.y*ml"):
        rel, text = path.relative_to(root).as_posix(), path.read_text()
        if rel != WORKFLOW: result.error(f"issue-specific or unapproved workflow: {rel}")
        if re.search(r"(?mi)^\s*contents\s*:\s*write\s*$", text): result.error(f"workflow may not request contents: write: {rel}")
        for mutation in (r"\bgit\s+push\b", r"\bgit\s+commit\b", r"gh\s+api[^\n]*(?:contents|git/refs)"):
            if re.search(mutation, text, re.I): result.error(f"workflow mutates candidate bytes: {rel}")

def event_context() -> PullRequestContext | None:
    path = os.getenv("GITHUB_EVENT_PATH")
    if not path or not Path(path).is_file(): return None
    data = json.loads(Path(path).read_text()); pr = data.get("pull_request")
    if not isinstance(pr, dict): return None
    return PullRequestContext(int(pr["number"]), bool(pr.get("draft")), str(pr["base"]["ref"]), str(pr["base"]["sha"]), str(pr["head"]["sha"]), str(pr.get("body") or ""), str(data.get("repository", {}).get("full_name") or os.getenv("GITHUB_REPOSITORY", "")))

def marker(body: str, label: str) -> str | None:
    found = re.search(rf"(?mi)^\s*-?\s*{re.escape(label)}\s*:\s*(.+?)\s*$", body)
    return found.group(1).strip().strip("`") if found else None

def changed_files(root: Path, context: PullRequestContext, result: Result) -> list[str]:
    try: return [x for x in subprocess.check_output(["git", "diff", "--name-only", f"{context.base_sha}...{context.head_sha}"], cwd=root, text=True).splitlines() if x]
    except Exception as exc: result.error(f"unable to compute PR files: {exc}"); return []

def open_prs(repository: str, token: str, result: Result) -> list[dict[str, Any]]:
    if not repository or not token: return []
    request = urllib.request.Request(f"https://api.github.com/repos/{repository}/pulls?state=open&per_page=100", headers={"Accept": "application/vnd.github+json", "Authorization": f"Bearer {token}"})
    try:
        with urllib.request.urlopen(request, timeout=20) as response: value = json.loads(response.read())
        return value if isinstance(value, list) else []
    except Exception as exc: result.warning(f"duplicate-PR lookup unavailable: {exc}"); return []

def validate_pr(manifests: list[dict[str, Any]], context: PullRequestContext, files: list[str], result: Result, remote: list[dict[str, Any]]) -> None:
    if context.draft: result.error("integration pull requests must not be draft")
    if context.base_ref != "main": result.error("pull request must target main")
    if not files: result.error("pull request changed-file set is empty"); return
    def governance_path(path: str) -> bool:
        name = Path(path).name
        return (
            path.startswith(("governance/", "scripts/", ".github/"))
            or path in {"AGENTS.md", "AGENT_PROMPT.md"}
            or path.endswith("/INTEGRATION.json")
            or (path.startswith("research/issues/") and name == "SYNC_REPORT.md")
            or (path.startswith("research/issues/") and name.startswith("sync_") and name.endswith(".py"))
        )
    governance = all(governance_path(f) for f in files)
    body_issue = marker(context.body, "Task-Issue")
    body_owned = marker(context.body, "Owned-Path")
    matching = [
        m for m in manifests
        if body_issue == f"#{m.get('issue_number')}"
        and body_owned == (m.get("owned_paths") or [None])[0]
    ]
    if governance:
        touched: list[dict[str, Any]] = []
        role = "governance-maintainer"
    else:
        if len(matching) != 1:
            result.error("PR body must identify exactly one manifest by Task-Issue and Owned-Path")
            return
        touched = matching
        role = touched[0].get("role")
    if not governance and role not in {"research-worker", "reviewer", "integration-maintainer"}:
        result.error("PR lacks one manifest-declared role"); return
    roots = [r for m in touched for r in m.get("owned_paths", [])]
    if role in {"research-worker", "reviewer"}:
        for f in files:
            if f in SHARED: result.error(f"{role} may not edit shared surface {f}")
            if not owned(f, roots): result.error(f"{role} changed path outside ownership: {f}")
        for m in touched:
            for claim in m.get("proposed_global_claims", []):
                if isinstance(claim, dict) and str(claim.get("id", "")).startswith("CLM-"): result.error("workers/reviewers must use issue-local claim labels")
    if role == "integration-maintainer":
        manifest = touched[0]
        if manifest.get("base_sha") != context.base_sha: result.error("integration manifest base_sha does not match current PR base")
    if role == "governance-maintainer":
        bad = [f for f in files if f.startswith("research/") and not governance_path(f)]
        if bad: result.error("governance PR changes scientific content: " + ", ".join(bad))
    body_role = marker(context.body, "Role")
    if body_role != role: result.error(f"PR body Role must be {role}")
    for m in touched:
        expected_issue, expected_owned = f"#{m.get('issue_number')}", m.get("owned_paths", [None])[0]
        if body_issue != expected_issue: result.error(f"PR body Task-Issue must be {expected_issue}")
        if body_owned != expected_owned: result.error(f"PR body Owned-Path must be {expected_owned}")
        for other in remote:
            if int(other.get("number", 0)) == context.number: continue
            body = str(other.get("body") or "")
            if marker(body, "Task-Issue") == expected_issue or marker(body, "Owned-Path") == expected_owned: result.error(f"duplicate open PR #{other.get('number')} for {expected_issue} / {expected_owned}")

def validate_root(root: Path, *, context: PullRequestContext | None = None, changed_files: list[str] | None = None, remote_prs: list[dict[str, Any]] | None = None) -> Result:
    result, manifests = Result([], []), []
    for directory in packets(root):
        path = directory / "INTEGRATION.json"
        if not path.is_file(): result.error(f"missing integration manifest: {path.relative_to(root)}")
        else: manifests.append(read_manifest(path, root, result))
    scan_tree(root, result)
    if context: validate_pr(manifests, context, changed_files or [], result, remote_prs or [])
    return result

def main() -> int:
    parser = argparse.ArgumentParser(); parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1]); parser.add_argument("--no-remote", action="store_true"); args = parser.parse_args()
    root, result = args.root.resolve(), Result([], [])
    context = event_context(); files = changed_files(root, context, result) if context else []
    remote = [] if args.no_remote or not context else open_prs(context.repository, os.getenv("GITHUB_TOKEN", ""), result)
    checked = validate_root(root, context=context, changed_files=files, remote_prs=remote)
    checked.errors[:0] = result.errors; checked.warnings[:0] = result.warnings
    print(f"integration manifests: {len(packets(root))}\nerrors: {len(checked.errors)}\nwarnings: {len(checked.warnings)}")
    for x in checked.errors: print("ERROR:", x)
    for x in checked.warnings: print("WARNING:", x)
    if checked.errors: return 1
    print("integration contract: PASS\nmathematical truth: NOT EVALUATED"); return 0

if __name__ == "__main__": raise SystemExit(main())
