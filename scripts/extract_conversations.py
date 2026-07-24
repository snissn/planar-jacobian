#!/usr/bin/env python3
from pathlib import Path
import base64
import gzip
import hashlib
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
manifest = json.loads((ROOT / "archive/manifest.json").read_text())
out = ROOT / "archive/extracted"
out.mkdir(exist_ok=True)

extracted = 0
skipped = 0

for export in manifest["exports"]:
    export_id = export["id"]
    storage_mode = export.get("storage_mode", "embedded")
    if storage_mode != "embedded":
        skipped += 1
        print(
            f"SKIP {export_id}: storage_mode={storage_mode}; "
            "the complete source bytes are not embedded in this Git tree",
            file=sys.stderr,
        )
        continue

    chunk_paths = export.get("base64_chunk_paths", [])
    missing = [path for path in chunk_paths if not (ROOT / path).exists()]
    if missing:
        raise SystemExit(
            f"{export_id}: missing embedded chunks: {', '.join(missing)}"
        )

    encoded = "".join((ROOT / path).read_text().strip() for path in chunk_paths)
    compressed = base64.b64decode(encoded, validate=True)
    if hashlib.sha256(compressed).hexdigest() != export["gzip_sha256"]:
        raise SystemExit(f"{export_id}: gzip SHA-256 mismatch")

    raw = gzip.decompress(compressed)
    if hashlib.sha256(raw).hexdigest() != export["raw_sha256"]:
        raise SystemExit(f"{export_id}: raw SHA-256 mismatch")
    if len(raw) != export["raw_bytes"]:
        raise SystemExit(f"{export_id}: raw byte-count mismatch")

    destination = out / export["original_filename"]
    destination.write_bytes(raw)
    extracted += 1
    print(destination)

if extracted == 0:
    raise SystemExit(
        "No conversation export is fully embedded. See archive/manifest.json "
        "and the archive_completion_issue before attempting extraction."
    )

if skipped:
    print(f"Extracted {extracted}; skipped {skipped} metadata-only export(s).")
