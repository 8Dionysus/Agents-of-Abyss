#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

import validate_nested_agents

try:
    import yaml
except ModuleNotFoundError:
    yaml = None

REPO_ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = REPO_ROOT / "generated" / "ecosystem_registry.min.json"
SCHEMA_PATH = REPO_ROOT / "schemas" / "ecosystem-registry.schema.json"
QUESTBOOK_PATH = REPO_ROOT / "QUESTBOOK.md"
QUESTBOOK_MODEL_PATH = REPO_ROOT / "docs" / "QUESTBOOK_MODEL.md"
QUESTBOOK_FIRST_WAVE_PATH = REPO_ROOT / "docs" / "QUESTBOOK_FIRST_WAVE.md"
QUESTS_PATH = REPO_ROOT / "quests"
REQUIRED_QUEST_IDS = ("AOA-Q-0001", "AOA-Q-0002", "AOA-Q-0003")

ALLOWED_STATUS = {
    "active",
    "bootstrap",
    "planned",
    "active-private",
    "active-conceptual",
    "related",
    "experimental",
    "deprecated",
}
ALLOWED_SHARED_MATURITY = {"seed", "proven", "promoted", "canonical", "deprecated"}
ALLOWED_KIND = {"meta", "source", "derived", "related"}


class ValidationError(RuntimeError):
    pass


def fail(message: str) -> None:
    raise ValidationError(message)


def read_json(path: Path) -> object:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        fail(f"missing required file: {path.relative_to(REPO_ROOT).as_posix()}")
    except json.JSONDecodeError as exc:
        fail(f"invalid JSON in {path.relative_to(REPO_ROOT).as_posix()}: {exc}")


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        fail(f"missing required file: {path.relative_to(REPO_ROOT).as_posix()}")


def read_yaml(path: Path) -> dict[str, object]:
    if yaml is None:
        fail("PyYAML is required to validate QUESTBOOK surfaces")

    try:
        payload = yaml.safe_load(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        fail(f"missing required file: {path.relative_to(REPO_ROOT).as_posix()}")
    except yaml.YAMLError as exc:
        fail(f"invalid YAML in {path.relative_to(REPO_ROOT).as_posix()}: {exc}")

    if not isinstance(payload, dict):
        fail(f"{path.relative_to(REPO_ROOT).as_posix()} must contain a YAML object")

    return payload


def validate_schema_surface() -> None:
    schema = read_json(SCHEMA_PATH)
    if not isinstance(schema, dict):
        fail("schema file must contain a JSON object")
    required_top_level = {"$schema", "$id", "title", "type", "properties", "required"}
    missing = sorted(required_top_level - set(schema))
    if missing:
        fail(f"schema is missing required top-level keys: {', '.join(missing)}")


def validate_registry() -> None:
    payload = read_json(REGISTRY_PATH)
    if not isinstance(payload, dict):
        fail("ecosystem registry must be a JSON object")

    for key in ("version", "ecosystem", "repos"):
        if key not in payload:
            fail(f"ecosystem registry is missing required key '{key}'")

    if not isinstance(payload["version"], int) or payload["version"] < 1:
        fail("registry 'version' must be an integer >= 1")
    if payload["ecosystem"] != "AoA":
        fail("registry 'ecosystem' must equal 'AoA'")

    repos = payload["repos"]
    if not isinstance(repos, list) or not repos:
        fail("registry 'repos' must be a non-empty list")

    seen_names: set[str] = set()
    required_core = {
        "Agents-of-Abyss",
        "aoa-techniques",
        "aoa-skills",
        "aoa-evals",
        "aoa-routing",
    }

    for index, repo in enumerate(repos):
        location = f"repos[{index}]"
        if not isinstance(repo, dict):
            fail(f"{location} must be an object")

        for key in ("name", "role", "status", "shared_maturity", "kind"):
            if key not in repo:
                fail(f"{location} is missing required key '{key}'")

        name = repo["name"]
        role = repo["role"]
        status = repo["status"]
        shared_maturity = repo["shared_maturity"]
        kind = repo["kind"]

        if not isinstance(name, str) or len(name) < 3:
            fail(f"{location}.name must be a string of length >= 3")
        if name in seen_names:
            fail(f"duplicate repository name in registry: '{name}'")
        seen_names.add(name)

        if not isinstance(role, str) or len(role) < 3:
            fail(f"{location}.role must be a string of length >= 3")
        if status not in ALLOWED_STATUS:
            fail(f"{location}.status '{status}' is not allowed")
        if shared_maturity not in ALLOWED_SHARED_MATURITY:
            fail(f"{location}.shared_maturity '{shared_maturity}' is not allowed")
        if kind not in ALLOWED_KIND:
            fail(f"{location}.kind '{kind}' is not allowed")

    missing_core = sorted(required_core - seen_names)
    if missing_core:
        fail(f"ecosystem registry is missing required core repos: {', '.join(missing_core)}")


def validate_nested_agents_surface() -> None:
    issues = validate_nested_agents.run_validation(REPO_ROOT)
    if issues:
        formatted = "; ".join(
            f"{location}: {message}" for location, message in issues
        )
        fail(f"nested AGENTS docs check failed: {formatted}")


def validate_questbook_surface() -> None:
    questbook_text = read_text(QUESTBOOK_PATH)
    read_text(QUESTBOOK_MODEL_PATH)
    first_wave_text = read_text(QUESTBOOK_FIRST_WAVE_PATH)

    expected_paths = {
        quest_id: QUESTS_PATH / f"{quest_id}.yaml" for quest_id in REQUIRED_QUEST_IDS
    }
    actual_ids = {
        path.stem for path in QUESTS_PATH.glob("AOA-Q-*.yaml") if path.is_file()
    }
    expected_ids = set(REQUIRED_QUEST_IDS)
    if actual_ids != expected_ids:
        missing = sorted(expected_ids - actual_ids)
        extra = sorted(actual_ids - expected_ids)
        details: list[str] = []
        if missing:
            details.append(f"missing: {', '.join(missing)}")
        if extra:
            details.append(f"extra: {', '.join(extra)}")
        joined = "; ".join(details) if details else "unexpected quest set"
        fail(f"foundation quest set must match expected center quests ({joined})")

    for quest_id, path in expected_paths.items():
        payload = read_yaml(path)

        schema_version = payload.get("schema_version")
        if schema_version != "work_quest_v1":
            fail(
                f"{path.relative_to(REPO_ROOT).as_posix()} has unsupported "
                f"schema_version '{schema_version}'"
            )

        repo = payload.get("repo")
        if repo != "Agents-of-Abyss":
            fail(
                f"{path.relative_to(REPO_ROOT).as_posix()} must target "
                "repo 'Agents-of-Abyss'"
            )

        payload_id = payload.get("id")
        if payload_id != quest_id:
            fail(
                f"{path.relative_to(REPO_ROOT).as_posix()} id '{payload_id}' "
                f"does not match filename '{quest_id}'"
            )

        if payload.get("public_safe") is not True:
            fail(f"{path.relative_to(REPO_ROOT).as_posix()} must set public_safe: true")

        if quest_id not in questbook_text:
            fail(f"QUESTBOOK.md must reference quest id '{quest_id}'")

    if "ATM10-Agent" in first_wave_text:
        fail("docs/QUESTBOOK_FIRST_WAVE.md must not reference ATM10-Agent")

    required_phrase = "It is a foundation pass, not a new numbered AoA wave."
    if required_phrase not in first_wave_text:
        fail(
            "docs/QUESTBOOK_FIRST_WAVE.md must state that the contour is not "
            "a new numbered AoA wave"
        )


def main() -> int:
    try:
        validate_schema_surface()
        validate_registry()
        validate_questbook_surface()
        validate_nested_agents_surface()
    except ValidationError as exc:
        print(f"[error] {exc}", file=sys.stderr)
        return 1

    print("[ok] validated ecosystem registry schema surface")
    print("[ok] validated generated/ecosystem_registry.min.json")
    print("[ok] validated questbook center surface")
    print("[ok] validated nested AGENTS directory guidance")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
