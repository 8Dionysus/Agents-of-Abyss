from __future__ import annotations

import argparse
import json
from pathlib import Path

from agents_mesh_common import read_config, relative_agent_paths, repo_root_from

ROOT_DIR_EXEMPTIONS = {".git", ".venv", "venv", "env", "__pycache__", ".pytest_cache", ".mypy_cache", ".ruff_cache", ".vscode", ".idea", "node_modules", "dist", "build", "tmp", "temp"}


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate AGENTS mesh coverage and registry references.")
    parser.add_argument("--repo-root", default=None)
    args = parser.parse_args()
    repo_root = Path(args.repo_root).resolve() if args.repo_root else repo_root_from()
    config = read_config(repo_root)
    errors: list[str] = []

    if config.get("schema_version") != "aoa_agents_mesh_v1":
        errors.append("config schema_version must be aoa_agents_mesh_v1")

    paths = [entry.get("path") for entry in config.get("entries", [])]
    if len(paths) != len(set(paths)):
        errors.append("config contains duplicate AGENTS paths")

    for rel in relative_agent_paths(config):
        if not (repo_root / rel).exists():
            errors.append(f"missing required AGENTS card: {rel.as_posix()}")

    # Existing durable top-level directories should be covered unless exempt.
    configured_top_cards = {Path(path).parts[0] for path in paths if path and path.endswith("/AGENTS.md")}
    configured_top_cards.add(".")
    for child in repo_root.iterdir():
        if not child.is_dir():
            continue
        name = child.name
        if name in ROOT_DIR_EXEMPTIONS or name.startswith(".wave_"):
            continue
        if name not in configured_top_cards:
            errors.append(f"top-level directory lacks AGENTS mesh entry: {name}/")

    # mechanics/registry.json agents_ref values must be present and existing when registry exists.
    registry_path = repo_root / "mechanics" / "registry.json"
    if registry_path.exists():
        registry = json.loads(registry_path.read_text(encoding="utf-8"))
        mesh_paths = set(paths)
        for mech in registry.get("mechanics", []):
            agents_ref = mech.get("agents_ref")
            if not agents_ref:
                errors.append(f"mechanic {mech.get('slug')} lacks agents_ref")
                continue
            if agents_ref not in mesh_paths:
                errors.append(f"mechanic agents_ref not registered in AGENTS mesh: {agents_ref}")
            if not (repo_root / agents_ref).exists():
                errors.append(f"mechanic agents_ref missing on disk: {agents_ref}")

    if errors:
        raise SystemExit("AGENTS mesh validation failed:\n" + "\n".join(f"- {e}" for e in errors))
    print("AGENTS mesh validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
