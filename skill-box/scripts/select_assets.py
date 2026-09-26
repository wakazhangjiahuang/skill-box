#!/usr/bin/env python3
"""Resolve exact manifest assets for one task; no network side effects."""
import argparse
import json
import sys
from pathlib import Path
from validate_release import validate_manifest


def select(manifest: Path, task: str):
    data = json.loads(manifest.read_text(encoding="utf-8"))
    ids = data.get("entrypoints", {}).get(task)
    if not ids:
        raise ValueError(f"no entrypoint for task: {task}")
    by_id = {item["id"]: item for item in data["assets"]}
    return {
        "resource_id": data["resource_id"],
        "repository": data["repository"],
        "ref": data["ref"],
        "task": task,
        "assets": [by_id[ident] for ident in ids],
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("manifest", type=Path)
    parser.add_argument("task")
    args = parser.parse_args()
    errors = validate_manifest(args.manifest, None)
    if errors:
        parser.error("; ".join(errors))
    try:
        print(json.dumps(select(args.manifest, args.task), ensure_ascii=False, indent=2))
    except ValueError as exc:
        parser.error(str(exc))
    return 0


if __name__ == "__main__":
    sys.exit(main())
