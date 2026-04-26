#!/usr/bin/env python3
"""Validate the AoA-side Experience ready quest owner-route map."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[3]
ROUTE_MAP_PATH = REPO_ROOT / "mechanics" / "questbook" / "docs" / "experience-ready-owner-routes.md"
READY_DIR = REPO_ROOT / "quests" / "experience" / "ready"
OWNER_QUEUE_PATH = REPO_ROOT / "mechanics" / "owner-request-queue.json"
OWNER_DOC_PATH = REPO_ROOT / "mechanics" / "experience" / "OWNER_REQUESTS.md"

ROW_RE = re.compile(
    r"^\| \[(?P<label>AOA-Q-EXP-[^\]]+)\]\((?P<link>[^)]+)\) \| (?P<routes>[^|]+) \|"
)
ORQ_RE = re.compile(r"`(ORQ-EXPERIENCE-[A-Z]+-001)`")


def rel(path: Path) -> str:
    return path.relative_to(REPO_ROOT).as_posix()


def load_experience_request_ids() -> set[str]:
    payload = json.loads(OWNER_QUEUE_PATH.read_text(encoding="utf-8"))
    return {
        str(item.get("id"))
        for item in payload.get("requests", [])
        if item.get("mechanic") == "experience"
    }


def validate() -> list[str]:
    problems: list[str] = []
    if not ROUTE_MAP_PATH.is_file():
        return [f"{rel(ROUTE_MAP_PATH)}: missing route map"]

    text = ROUTE_MAP_PATH.read_text(encoding="utf-8")
    for phrase in (
        "It is not owner acceptance",
        "Do not update owner-request status from this table.",
        "Do not close a ready quest until owner-local acceptance",
    ):
        if phrase not in text:
            problems.append(f"{rel(ROUTE_MAP_PATH)} must say: {phrase}")

    owner_doc = OWNER_DOC_PATH.read_text(encoding="utf-8")
    valid_request_ids = load_experience_request_ids()
    seen_paths: dict[str, list[str]] = {}
    seen_request_ids: set[str] = set()

    for line_number, line in enumerate(text.splitlines(), start=1):
        match = ROW_RE.match(line)
        if not match:
            continue
        label = match.group("label")
        link = match.group("link")
        if not link.startswith("../../../quests/experience/ready/AOA-Q-EXP-"):
            problems.append(f"{rel(ROUTE_MAP_PATH)}:{line_number}: quest link must point to the ready directory")
            continue
        target = (ROUTE_MAP_PATH.parent / link).resolve()
        if target.parent != READY_DIR.resolve():
            problems.append(f"{rel(ROUTE_MAP_PATH)}:{line_number}: route target escapes ready directory")
            continue
        if not target.is_file():
            problems.append(f"{rel(ROUTE_MAP_PATH)}:{line_number}: missing quest target {link}")
        if target.stem != label:
            problems.append(f"{rel(ROUTE_MAP_PATH)}:{line_number}: label must match target filename stem")
        seen_paths.setdefault(rel(target), []).append(f"{rel(ROUTE_MAP_PATH)}:{line_number}")

        request_ids = ORQ_RE.findall(match.group("routes"))
        if not request_ids:
            problems.append(f"{rel(ROUTE_MAP_PATH)}:{line_number}: row must name at least one ORQ-EXPERIENCE request")
        for request_id in request_ids:
            if request_id not in valid_request_ids:
                problems.append(f"{rel(ROUTE_MAP_PATH)}:{line_number}: unknown Experience owner request {request_id}")
            if request_id not in owner_doc:
                problems.append(f"{rel(ROUTE_MAP_PATH)}:{line_number}: {request_id} missing from {rel(OWNER_DOC_PATH)}")
            seen_request_ids.add(request_id)

    ready_paths = {rel(path) for path in READY_DIR.glob("AOA-Q-EXP-*.md")}
    mapped_paths = set(seen_paths)
    missing = sorted(ready_paths - mapped_paths)
    extra = sorted(mapped_paths - ready_paths)
    duplicate = sorted(path for path, rows in seen_paths.items() if len(rows) > 1)
    if missing:
        problems.append(f"{rel(ROUTE_MAP_PATH)} missing ready quests: {', '.join(missing)}")
    if extra:
        problems.append(f"{rel(ROUTE_MAP_PATH)} maps non-ready quests: {', '.join(extra)}")
    if duplicate:
        problems.append(f"{rel(ROUTE_MAP_PATH)} maps quests more than once: {', '.join(duplicate)}")

    unused_request_ids = sorted(valid_request_ids - seen_request_ids)
    if unused_request_ids:
        problems.append(f"{rel(ROUTE_MAP_PATH)} does not route any ready quest to: {', '.join(unused_request_ids)}")
    return problems


def main() -> int:
    problems = validate()
    if problems:
        print("Experience ready owner-route validation failed:")
        for problem in problems:
            print(f" - {problem}")
        return 1
    print("[ok] Experience ready owner routes validated")
    return 0


if __name__ == "__main__":
    sys.exit(main())
