from __future__ import annotations

import argparse
import re
from pathlib import Path

try:
    from agents_mesh_common import inherited_chain_paths, markdown_headings, read_config, relative_agent_paths, repo_root_from
except ModuleNotFoundError:  # pragma: no cover - package import route
    from scripts.agents_mesh.agents_mesh_common import (
        inherited_chain_paths,
        markdown_headings,
        read_config,
        relative_agent_paths,
        repo_root_from,
    )


RUNNABLE_AGENT_LINE_RE = re.compile(
    r"^[ \t]*(?:(?:[-*]|\d+[.)])[ \t]+)?`?\$?[ \t]*(?:"
    r"python3?(?:[ \t]+-m)?[ \t]+|pytest(?=[ \t`])|"
    r"uv[ \t]+run[ \t]+(?:pytest|python)\b|pip3?[ \t]+|"
    r"git[ \t]+(?:status|diff|commit|push|fetch|checkout|switch|merge|tag)\b|"
    r"ruff[ \t]+(?:check|format)\b|mypy(?=[ \t]))",
    re.IGNORECASE,
)
INLINE_AGENT_COMMAND_RE = re.compile(
    r"`(?:python3?(?:\s+-m)?\s+|pytest(?=\s)|"
    r"uv\s+run\s+(?:pytest|python)\b|pip3?\s+|"
    r"git\s+(?:status|diff|commit|push|fetch|checkout|switch|merge|tag)\b|"
    r"ruff\s+(?:check|format)\b|mypy\s+)[^`\n]+`",
    re.IGNORECASE,
)
IMPERATIVE_SCRIPT_RE = re.compile(
    r"\b(?:run|execute|invoke|call|validate with|check with|regenerate with)\s+"
    r"(?:the\s+)?`(?:[^`]+/)+[^`]+\.(?:py|sh)`",
    re.IGNORECASE,
)
READ_SECTION_RE = re.compile(r"^##\s+(?:read\s+before\s+editing|read\s+first|reading\s+order|required\s+reading|start\s+here)\b", re.IGNORECASE)
HEADING_RE = re.compile(r"^#{1,6}\s+")


def validate_prompt_light_rules(rel: Path, text: str) -> list[str]:
    errors: list[str] = []
    if "```" in text or "~~~" in text:
        errors.append(f"{rel.as_posix()}: AGENTS cards must not contain fenced blocks")
    for line_number, line in enumerate(text.splitlines(), start=1):
        if RUNNABLE_AGENT_LINE_RE.search(line):
            errors.append(f"{rel.as_posix()}:{line_number}: runnable command must live in an on-demand validation surface")
            break
        if INLINE_AGENT_COMMAND_RE.search(line):
            errors.append(f"{rel.as_posix()}:{line_number}: inline runnable command must live in an on-demand validation surface")
            break
        if IMPERATIVE_SCRIPT_RE.search(line):
            errors.append(f"{rel.as_posix()}:{line_number}: imperative script procedure must live in an on-demand validation surface")
            break

    lines = text.splitlines()
    for index, line in enumerate(lines):
        if not READ_SECTION_RE.match(line):
            continue
        body: list[str] = []
        for candidate in lines[index + 1 :]:
            if HEADING_RE.match(candidate) and candidate.startswith("## "):
                break
            body.append(candidate)
        section = "\n".join(body)
        if "README.md" in section and not re.search(
            r"\b(?:when|if|only|task|relevant|material|conditional|optional)\b",
            section,
            re.IGNORECASE,
        ):
            errors.append(f"{rel.as_posix()}: README route under Read before editing must be task-conditional")
            break
    return errors


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
    errors.extend(validate_prompt_light_rules(rel, text))
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
    chain_budget_bytes = int(config.get("chain_budget_bytes", 32768))
    registered_paths = relative_agent_paths(config)
    errors: list[str] = []
    for rel in registered_paths:
        entry = next((e for e in config.get("entries", []) if e.get("path") == rel.as_posix()), {})
        entry_required = entry.get("required_headings") or ["# AGENTS.md", *required]
        # The first-line requirement is checked separately; remove it from normal heading search if present.
        entry_required = [h for h in entry_required if h != "# AGENTS.md"]
        errors.extend(validate_card(repo_root, rel, entry_required, max_line_length, min_heading_count))
        chain_paths = inherited_chain_paths(rel, registered_paths)
        if all((repo_root / path).is_file() for path in chain_paths):
            chain_bytes = sum(len((repo_root / path).read_bytes()) for path in chain_paths)
            if chain_bytes > chain_budget_bytes:
                rendered_chain = " + ".join(path.as_posix() for path in chain_paths)
                errors.append(
                    f"{rel.as_posix()}: inherited AGENTS chain is {chain_bytes} bytes, "
                    f"over {chain_budget_bytes}: {rendered_chain}"
                )
    if errors:
        raise SystemExit("AGENTS.md shape validation failed:\n" + "\n".join(f"- {e}" for e in errors))
    print("AGENTS.md shape validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
