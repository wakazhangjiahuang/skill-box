#!/usr/bin/env python3
"""Static checks for an Agent Skill and an optional local GitHub asset checkout."""
import argparse
import hashlib
import json
import re
import sys
from pathlib import Path, PurePosixPath


def validate_skill(root: Path):
    errors = []
    entry = root / "SKILL.md"
    if not entry.is_file():
        return ["SKILL.md missing"]
    body = entry.read_text(encoding="utf-8")
    match = re.match(r"\A---\n(.*?)\n---\n", body, re.S)
    if not match:
        errors.append("YAML frontmatter missing")
        return errors
    fields = dict(re.findall(r"^(name|description):\s*(.+)$", match.group(1), re.M))
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", fields.get("name", "")):
        errors.append("invalid skill name")
    if not fields.get("description"):
        errors.append("description missing")
    for target in re.findall(r"\]\(([^)]+)\)", body):
        if "://" not in target and not target.startswith("#"):
            if not (root / target.split("#", 1)[0]).is_file():
                errors.append(f"broken local reference: {target}")
    return errors


def validate_manifest(path: Path, repo: Path | None):
    errors = []
    data = json.loads(path.read_text(encoding="utf-8"))
    for field in ("schema_version", "resource_id", "repository", "ref", "entrypoints", "assets"):
        if not data.get(field):
            errors.append(f"manifest missing {field}")
    index = {}
    for item in data.get("assets", []):
        ident, raw = item.get("id"), item.get("path", "")
        relative = PurePosixPath(raw)
        if not ident or ident in index:
            errors.append(f"missing or duplicate asset id: {ident}")
        index[ident] = item
        if not raw or relative.is_absolute() or ".." in relative.parts or "\\" in raw:
            errors.append(f"unsafe asset path: {raw}")
            continue
        digest = item.get("sha256", "")
        if not re.fullmatch(r"[0-9a-f]{64}", digest):
            errors.append(f"invalid sha256: {ident}")
        if not isinstance(item.get("task_tags"), list) or not item.get("source"):
            errors.append(f"tags/source missing: {ident}")
        if repo is not None:
            asset = repo / raw
            if not asset.is_file() or asset.is_symlink():
                errors.append(f"asset missing or symlink: {raw}")
            elif hashlib.sha256(asset.read_bytes()).hexdigest() != digest:
                errors.append(f"asset digest mismatch: {raw}")
    for task, ids in data.get("entrypoints", {}).items():
        if not isinstance(ids, list) or not ids:
            errors.append(f"empty entrypoint: {task}")
            continue
        for ident in ids:
            if ident not in index:
                errors.append(f"unknown entrypoint asset: {task}/{ident}")
            elif task not in index[ident].get("task_tags", []):
                errors.append(f"tag mismatch: {task}/{ident}")
    return errors


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--skill", type=Path, required=True)
    parser.add_argument("--manifest", type=Path)
    parser.add_argument("--repo-root", type=Path)
    args = parser.parse_args()
    if args.repo_root and not args.manifest:
        parser.error("--repo-root requires --manifest")
    errors = validate_skill(args.skill)
    if args.manifest:
        try:
            errors += validate_manifest(args.manifest, args.repo_root)
        except (ValueError, OSError) as exc:
            errors.append(f"manifest unreadable: {exc}")
    for error in errors:
        print("FAIL", error)
    if errors:
        return 1
    print("PASS static skill/manifest checks; no runtime or remote access tested")
    return 0


if __name__ == "__main__":
    sys.exit(main())
