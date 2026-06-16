#!/usr/bin/env python3
"""Render PlantUML .puml files to .svg using Docker.

Behavior:
- Recursively find .puml files under the provided directory.
- Render only when:
  - the .svg output does not exist, or
  - the .svg is older than or the same age as the .puml.
- Use -f/--force to regenerate all discovered diagrams.

Example:
  python render_plantuml_svgs.py distributed-authorization
  python render_plantuml_svgs.py -f .
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path, PurePosixPath


DOCKER_IMAGE = "plantuml/plantuml"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Render .puml files to .svg via Docker PlantUML."
    )
    parser.add_argument(
        "path",
        type=Path,
        help="Directory to scan recursively for .puml files.",
    )
    parser.add_argument(
        "-f",
        "--force",
        action="store_true",
        help="Force regeneration of all diagrams, ignoring timestamps.",
    )
    return parser.parse_args()


def is_up_to_date(puml_file: Path, svg_file: Path) -> bool:
    if not svg_file.exists():
        return False
    return svg_file.stat().st_mtime > puml_file.stat().st_mtime


def to_container_path(repo_root: Path, file_path: Path) -> str:
    rel = file_path.relative_to(repo_root)
    return str(PurePosixPath(*rel.parts))


def render_with_docker(repo_root: Path, puml_file: Path) -> int:
    container_rel_path = to_container_path(repo_root, puml_file)

    cmd = [
        "docker",
        "run",
        "--rm",
        "-v",
        f"{repo_root}:/work",
        "-w",
        "/work",
        DOCKER_IMAGE,
        "-tsvg",
        container_rel_path,
    ]

    result = subprocess.run(cmd, check=False)
    return result.returncode


def main() -> int:
    args = parse_args()

    repo_root = Path(__file__).resolve().parent
    target_dir = args.path.expanduser()
    if not target_dir.is_absolute():
        target_dir = (Path.cwd() / target_dir).resolve()

    if not target_dir.exists() or not target_dir.is_dir():
        print(f"Error: path is not a directory: {target_dir}", file=sys.stderr)
        return 2

    try:
        target_dir.relative_to(repo_root)
    except ValueError:
        print(
            "Error: target path must be inside this repository.\n"
            f"Repo root: {repo_root}\n"
            f"Target:    {target_dir}",
            file=sys.stderr,
        )
        return 2

    if shutil.which("docker") is None:
        print("Error: docker command not found in PATH.", file=sys.stderr)
        return 2

    puml_files = sorted(target_dir.rglob("*.puml"))
    if not puml_files:
        print(f"No .puml files found under: {target_dir}")
        return 0

    to_render: list[Path] = []
    skipped: list[Path] = []

    for puml in puml_files:
        svg = puml.with_suffix(".svg")
        if args.force or not is_up_to_date(puml, svg):
            to_render.append(puml)
        else:
            skipped.append(puml)

    if not to_render:
        print("All diagrams are up to date.")
        return 0

    print(f"Found {len(puml_files)} .puml files")
    print(f"Rendering {len(to_render)} diagram(s) with Docker image: {DOCKER_IMAGE}")
    if skipped:
        print(f"Skipping {len(skipped)} up-to-date diagram(s)")

    failures = 0
    for puml in to_render:
        rel = puml.relative_to(repo_root)
        print(f"- Rendering: {rel}")
        exit_code = render_with_docker(repo_root, puml)
        if exit_code != 0:
            failures += 1
            print(f"  Failed with exit code {exit_code}: {rel}", file=sys.stderr)

    if failures:
        print(f"Completed with {failures} failure(s).", file=sys.stderr)
        return 1

    print("Done. All requested diagrams rendered successfully.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
