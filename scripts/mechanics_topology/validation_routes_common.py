"""Shared contracts for the mechanics validation-route manifest."""

from __future__ import annotations

import json
from pathlib import Path, PurePosixPath
from typing import Any


SCHEMA_VERSION = "aoa_mechanics_validation_routes_v1"
DEFAULT_MANIFEST = Path("mechanics/validation-routes.json")
LEGACY_MARKERS = (
    "<!-- centralized-child-validation:start -->",
    "<!-- centralized-child-validation:end -->",
)


def repo_root_from(start: Path | None = None) -> Path:
    current = (start or Path(__file__)).resolve()
    if current.is_file():
        current = current.parent
    for candidate in (current, *current.parents):
        if (candidate / "CHARTER.md").is_file() and (candidate / "mechanics").is_dir():
            return candidate
    raise ValueError(f"cannot locate repository root from {current}")


def load_manifest(repo_root: Path, manifest_ref: Path = DEFAULT_MANIFEST) -> dict[str, Any]:
    path = repo_root / manifest_ref
    return json.loads(path.read_text(encoding="utf-8"))


def normalize_repo_ref(value: str) -> str:
    ref = PurePosixPath(value)
    if ref.is_absolute() or ".." in ref.parts or not ref.parts:
        raise ValueError(f"not a safe repository-relative path: {value!r}")
    normalized = ref.as_posix()
    if normalized in {".", ""}:
        raise ValueError(f"not a file path: {value!r}")
    return normalized


def nearest_agents_card(repo_root: Path, surface_ref: str) -> str | None:
    surface = repo_root / surface_ref
    current = surface.parent
    while current == repo_root or repo_root in current.parents:
        candidate = current / "AGENTS.md"
        if candidate.is_file():
            return candidate.relative_to(repo_root).as_posix()
        if current == repo_root:
            break
        current = current.parent
    return None


def validate_manifest(repo_root: Path, data: dict[str, Any]) -> list[str]:
    problems: list[str] = []
    if data.get("schema_version") != SCHEMA_VERSION:
        problems.append(f"schema_version must be {SCHEMA_VERSION}")
    if data.get("owner_repo") != "Agents-of-Abyss":
        problems.append("owner_repo must be Agents-of-Abyss")

    for key in ("authority_ref", "agent_design_ref", "owner_surface", "runner_ref", "validator_ref"):
        value = data.get(key)
        if not isinstance(value, str) or not value:
            problems.append(f"{key} must be a non-empty repository-relative path")
            continue
        try:
            rel = normalize_repo_ref(value)
        except ValueError as exc:
            problems.append(f"{key}: {exc}")
            continue
        if not (repo_root / rel).is_file():
            problems.append(f"{key} does not exist: {rel}")

    stop_lines = data.get("must_not_claim")
    if not isinstance(stop_lines, list) or not stop_lines or not all(isinstance(item, str) and item for item in stop_lines):
        problems.append("must_not_claim must be a non-empty list of strings")

    routes = data.get("routes")
    if not isinstance(routes, dict) or not routes:
        return [*problems, "routes must be a non-empty object"]

    owner_cards: set[str] = set()
    for raw_surface, route in routes.items():
        try:
            surface = normalize_repo_ref(raw_surface)
        except ValueError as exc:
            problems.append(f"route key {raw_surface!r}: {exc}")
            continue
        if surface != raw_surface:
            problems.append(f"route key is not normalized: {raw_surface!r}")
        if not (repo_root / surface).is_file():
            problems.append(f"route surface does not exist: {surface}")
        if not isinstance(route, dict):
            problems.append(f"{surface}: route must be an object")
            continue

        owner_card = route.get("owner_card")
        if not isinstance(owner_card, str) or not owner_card:
            problems.append(f"{surface}: owner_card must be a non-empty string")
        else:
            try:
                owner_card = normalize_repo_ref(owner_card)
            except ValueError as exc:
                problems.append(f"{surface}: owner_card {exc}")
            else:
                owner_cards.add(owner_card)
                if not owner_card.endswith("/AGENTS.md") and owner_card != "AGENTS.md":
                    problems.append(f"{surface}: owner_card must name AGENTS.md")
                if not (repo_root / owner_card).is_file():
                    problems.append(f"{surface}: owner_card does not exist: {owner_card}")
                nearest = nearest_agents_card(repo_root, surface)
                if nearest != owner_card:
                    problems.append(
                        f"{surface}: owner_card must be nearest card {nearest!r}, found {owner_card!r}"
                    )

        commands = route.get("commands")
        if not isinstance(commands, list) or not commands:
            problems.append(f"{surface}: commands must be a non-empty list")
            continue
        for command_index, argv in enumerate(commands, start=1):
            label = f"{surface}: command {command_index}"
            if not isinstance(argv, list) or not argv or not all(isinstance(token, str) and token for token in argv):
                problems.append(f"{label} must be a non-empty argv string list")
                continue
            if argv[0] != "python":
                problems.append(f"{label} must use the python entrypoint, found {argv[0]!r}")
            if any("\n" in token or "\r" in token for token in argv):
                problems.append(f"{label} contains a newline")
            for token in argv[1:]:
                if token.endswith(".py") and not token.startswith("/") and not (repo_root / token).is_file():
                    problems.append(f"{label} references missing Python file: {token}")

    manifest_ref = DEFAULT_MANIFEST.as_posix()
    for owner_card in sorted(owner_cards):
        path = repo_root / owner_card
        if path.is_file() and manifest_ref not in path.read_text(encoding="utf-8"):
            problems.append(f"{owner_card}: routed child validation must name {manifest_ref}")

    for card in sorted((repo_root / "mechanics").glob("**/AGENTS.md")):
        text = card.read_text(encoding="utf-8")
        if any(marker in text for marker in LEGACY_MARKERS):
            problems.append(
                f"{card.relative_to(repo_root).as_posix()}: legacy centralized child validation marker remains"
            )
    return problems
