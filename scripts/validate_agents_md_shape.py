from __future__ import annotations

import argparse
from pathlib import Path

from agents_mesh_common import markdown_headings, read_config, relative_agent_paths, repo_root_from


def validate_card(repo_root: Path, rel: Path, required_headings: list[str], max_line_length: int, min_heading_count: int) -> list[str]:
    path = repo_root / rel
    errors: list[str] = []
    if not path.exists():
        return [f"missing required AGENTS card: {rel.as_posix()}"]
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if not lines or lines[0].strip() != "# AGENTS.md":
        errors.append(f"{rel.as_posix()}: first line must be '# AGENTS.md'")
    headings = markdown_headings(text)
    if len(headings) < min_heading_count:
        errors.append(f"{rel.as_posix()}: expected at least {min_heading_count} headings, found {len(headings)}")
    for heading in required_headings:
        if heading not in headings:
            errors.append(f"{rel.as_posix()}: missing heading {heading!r}")
    for idx, line in enumerate(lines, start=1):
        if len(line) > max_line_length:
            errors.append(f"{rel.as_posix()}:{idx}: line longer than {max_line_length} chars")
            break
    body = text.lower()
    if "do not" not in body and "must not" not in body:
        errors.append(f"{rel.as_posix()}: card must contain explicit negative boundary language")
    if "validation" not in body:
        errors.append(f"{rel.as_posix()}: card must mention validation")
    if "closeout" not in body:
        errors.append(f"{rel.as_posix()}: card must mention closeout")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate AGENTS.md readability and required sections.")
    parser.add_argument("--repo-root", default=None)
    args = parser.parse_args()
    repo_root = Path(args.repo_root).resolve() if args.repo_root else repo_root_from()
    config = read_config(repo_root)
    required = config.get("required_headings", [])
    max_line_length = int(config.get("max_line_length", 240))
    min_heading_count = int(config.get("min_heading_count", 7))
    errors: list[str] = []
    for rel in relative_agent_paths(config):
        entry = next((e for e in config.get("entries", []) if e.get("path") == rel.as_posix()), {})
        entry_required = entry.get("required_headings") or ["# AGENTS.md", *required]
        # The first-line requirement is checked separately; remove it from normal heading search if present.
        entry_required = [h for h in entry_required if h != "# AGENTS.md"]
        errors.extend(validate_card(repo_root, rel, entry_required, max_line_length, min_heading_count))
    if errors:
        raise SystemExit("AGENTS.md shape validation failed:\n" + "\n".join(f"- {e}" for e in errors))
    print("AGENTS.md shape validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
