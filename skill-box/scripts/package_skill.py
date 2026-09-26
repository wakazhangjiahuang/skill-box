#!/usr/bin/env python3
"""Package one validated Skill folder; this is not a Plugin ZIP."""
import argparse
import zipfile
from pathlib import Path
from validate_release import validate_skill


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("skill", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    skill = args.skill.resolve()
    errors = validate_skill(skill)
    if errors:
        parser.error("; ".join(errors))
    files = sorted(p for p in skill.rglob("*") if p.is_file() and "__pycache__" not in p.parts)
    for p in files:
        if p.is_symlink():
            parser.error(f"symlink not allowed: {p}")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(args.output, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in files:
            info = zipfile.ZipInfo(f"{skill.name}/{path.relative_to(skill).as_posix()}")
            info.date_time = (2026, 1, 1, 0, 0, 0)
            info.compress_type = zipfile.ZIP_DEFLATED
            archive.writestr(info, path.read_bytes())
    with zipfile.ZipFile(args.output) as archive:
        assert archive.testzip() is None
        assert f"{skill.name}/SKILL.md" in archive.namelist()
    print(f"PASS Skill ZIP: {args.output} ({len(files)} files); Plugin manifest not included")


if __name__ == "__main__":
    main()
