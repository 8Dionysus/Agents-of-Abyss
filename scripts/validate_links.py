#!/usr/bin/env python3
"""Validate local Markdown links without fetching external URLs."""
from __future__ import annotations

import argparse
import re
import sys
import urllib.parse
from dataclasses import dataclass
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))
from hygiene_common import iter_markdown_files, load_config, relpath  # noqa: E402

INLINE_LINK_RE = re.compile(r"(?<!!)\[[^\]\n]+\]\(([^)\n]+)\)")
IMAGE_LINK_RE = re.compile(r"!\[[^\]\n]*\]\(([^)\n]+)\)")
REFERENCE_LINK_RE = re.compile(r"^\s*\[[^\]]+\]:\s+(\S+)", re.MULTILINE)
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
SCHEME_RE = re.compile(r"^[A-Za-z][A-Za-z0-9+.-]*:")


@dataclass(frozen=True)
class LinkOccurrence:
    source: Path
    line: int
    target: str
    kind: str


def split_target(raw: str) -> str:
    target = raw.strip()
    if not target:
        return target
    if target.startswith("<") and ">" in target:
        target = target[1 : target.index(">")]
    elif " " in target:
        first, rest = target.split(" ", 1)
        if rest.strip().startswith(('"', "'")):
            target = first
    return target.strip()


def occurrences(path: Path) -> list[LinkOccurrence]:
    text = path.read_text(encoding="utf-8")
    found: list[LinkOccurrence] = []
    for kind, regex in (("link", INLINE_LINK_RE), ("image", IMAGE_LINK_RE), ("reference", REFERENCE_LINK_RE)):
        for match in regex.finditer(text):
            line = text.count("\n", 0, match.start()) + 1
            found.append(LinkOccurrence(path, line, split_target(match.group(1)), kind))
    return found


def slugify_heading(text: str) -> str:
    text = re.sub(r"[`*_~]", "", text)
    text = re.sub(r"[^\w\s-]", "", text, flags=re.UNICODE).strip().lower()
    text = re.sub(r"\s+", "-", text)
    return text


def anchors_for(path: Path) -> set[str]:
    anchors: set[str] = set()
    counts: dict[str, int] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        match = HEADING_RE.match(line)
        if not match:
            continue
        slug = slugify_heading(match.group(2))
        if not slug:
            continue
        count = counts.get(slug, 0)
        counts[slug] = count + 1
        anchors.add(slug if count == 0 else f"{slug}-{count}")
    return anchors


def is_ignored_external(target: str, ignored_schemes: set[str]) -> bool:
    if target.startswith("#"):
        return False
    match = SCHEME_RE.match(target)
    return bool(match and match.group(0)[:-1].lower() in ignored_schemes)


def normalize_local_target(root: Path, source: Path, target: str) -> tuple[Path, str]:
    target = urllib.parse.unquote(target)
    path_part, _, fragment = target.partition("#")
    if path_part.startswith("/"):
        dest = root / path_part.lstrip("/")
    elif path_part:
        dest = source.parent / path_part
    else:
        dest = source
    return dest.resolve(), urllib.parse.unquote(fragment)


def validate(root: Path, *, check_anchors: bool | None = None) -> list[str]:
    config = load_config(root)
    link_cfg = config.get("link_validation", {})
    ignored_schemes = {s.lower() for s in link_cfg.get("ignore_schemes", ["http", "https", "mailto", "tel", "data"])}
    if check_anchors is None:
        check_anchors = bool(link_cfg.get("check_anchors_by_default", False))
    problems: list[str] = []
    root_resolved = root.resolve()
    anchor_cache: dict[Path, set[str]] = {}
    for path in iter_markdown_files(root, config):
        for occ in occurrences(path):
            target = occ.target
            if not target or is_ignored_external(target, ignored_schemes):
                continue
            if target.startswith("javascript:"):
                problems.append(f"{relpath(root, path)}:{occ.line}: javascript link is not allowed")
                continue
            dest, fragment = normalize_local_target(root, path, target)
            try:
                dest.relative_to(root_resolved)
            except ValueError:
                problems.append(f"{relpath(root, path)}:{occ.line}: link escapes repository root: {target}")
                continue
            if not dest.exists():
                problems.append(f"{relpath(root, path)}:{occ.line}: broken local {occ.kind}: {target}")
                continue
            if fragment and check_anchors and dest.is_file() and dest.suffix.lower() == ".md":
                anchors = anchor_cache.setdefault(dest, anchors_for(dest))
                if fragment not in anchors:
                    problems.append(
                        f"{relpath(root, path)}:{occ.line}: missing anchor #{fragment} in {relpath(root, dest)}"
                    )
    return problems


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--check-anchors", action="store_true")
    args = parser.parse_args()
    root = Path(args.repo_root).resolve()
    problems = validate(root, check_anchors=True if args.check_anchors else None)
    if problems:
        print("Local Markdown link validation failed:")
        for problem in problems:
            print(f" - {problem}")
        return 1
    print("Local Markdown links validated.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
