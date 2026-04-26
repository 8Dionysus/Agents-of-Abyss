#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any

def _repo_root() -> Path:
    for candidate in Path(__file__).resolve().parents:
        if (candidate / "mechanics" / "registry.json").is_file():
            return candidate
    raise RuntimeError("repo root not found")

ROOT = _repo_root()
CONFIG_PATH = ROOT / "mechanics" / "agon" / "parts" / "owner-binding" / "config" / "agon_move_owner_bindings.seed.json"
GENERATED_PATH = ROOT / "mechanics" / "agon" / "parts" / "owner-binding" / "generated" / "agon_move_owner_binding_registry.min.json"
MOVE_SEED_PATH = ROOT / "mechanics" / "agon" / "parts" / "lawful-move-grammar" / "config" / "agon_lawful_moves.seed.json"
MOVE_REGISTRY_PATH = ROOT / "mechanics" / "agon" / "parts" / "lawful-move-grammar" / "generated" / "agon_lawful_move_registry.min.json"

ALLOWED_OWNER_REPOS = {
    "Agents-of-Abyss",
    "aoa-techniques",
    "aoa-skills",
    "aoa-evals",
    "aoa-routing",
    "aoa-playbooks",
    "aoa-memo",
    "aoa-stats",
    "aoa-agents",
}

ALLOWED_MOVE_CLASSES = {
    "stance",
    "evidence",
    "trace",
    "contradiction",
    "closure",
    "summon",
    "witness",
    "revision",
    "boundary",
    "escalation",
}

STOP_WORDS = (
    "live arena session",
    "runtime packet",
    "final verdict",
    "durable scars",
    "retention",
    "Tree-of-Sophia",
)


class ValidationError(Exception):
    pass


def read_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ValidationError(f"missing required file: {path}") from exc
    except json.JSONDecodeError as exc:
        raise ValidationError(f"invalid JSON in {path}: {exc}") from exc


def write_json_min(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(data, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n",
        encoding="utf-8",
    )


def require_non_empty_string_list(value: Any, *, move_id: str, field: str) -> list[str]:
    if not isinstance(value, list) or not value:
        raise ValidationError(f"{move_id}: {field} must be a non-empty list of strings")
    if any(not isinstance(item, str) or not item.strip() for item in value):
        raise ValidationError(f"{move_id}: {field} must be a non-empty list of strings")
    return value


def collect_move_ids_from_lawful_move(root: Path = ROOT) -> set[str]:
    package_root = root / "mechanics" / "agon"
    if not package_root.exists():
        package_root = root

    lawful_move_part = package_root / "parts" / "lawful-move-grammar"
    seed = lawful_move_part / "config" / "agon_lawful_moves.seed.json"
    registry = lawful_move_part / "generated" / "agon_lawful_move_registry.min.json"

    if seed.exists():
        data = read_json(seed)
        moves = data.get("moves", [])
        return {m["move_id"] for m in moves}

    if registry.exists():
        data = read_json(registry)
        moves = data.get("moves") or data.get("bindings") or []
        return {m["move_id"] for m in moves}

    raise ValidationError(
        "owner-binding route strict check requires lawful-move-grammar route lawful move language. "
        "Expected mechanics/agon/parts/lawful-move-grammar/config/agon_lawful_moves.seed.json or mechanics/agon/parts/lawful-move-grammar/generated/agon_lawful_move_registry.min.json."
    )


def validate_config(config: dict[str, Any], *, require_lawful_move: bool = False, root: Path = ROOT) -> None:
    if config.get("schema_version") != "agon-move-owner-bindings.seed/0.1":
        raise ValidationError("unexpected schema_version")
    if config.get("lineage_ref") != "owner-binding":
        raise ValidationError("lineage_ref must be owner-binding")
    if config.get("status") != "pre_protocol_owner_binding_seed":
        raise ValidationError("unexpected status")

    bindings = config.get("bindings")
    if not isinstance(bindings, list) or not bindings:
        raise ValidationError("bindings must be a non-empty list")

    move_ids = [b.get("move_id") for b in bindings]
    if len(move_ids) != len(set(move_ids)):
        raise ValidationError("duplicate move_id in bindings")

    if require_lawful_move:
        lawful_move_ids = collect_move_ids_from_lawful_move(root)
        if set(move_ids) != lawful_move_ids:
            missing = sorted(lawful_move_ids - set(move_ids))
            extra = sorted(set(move_ids) - lawful_move_ids)
            raise ValidationError(
                f"owner-binding route binding move set does not match lawful-move-grammar route moves; missing={missing}; extra={extra}"
            )

    for binding in bindings:
        move_id = binding.get("move_id", "")
        if not move_id.startswith("agon.move."):
            raise ValidationError(f"{move_id}: invalid move_id")
        move_class = binding.get("move_class")
        if not isinstance(move_class, str) or move_class not in ALLOWED_MOVE_CLASSES:
            raise ValidationError(f"{move_id}: invalid move_class {move_class!r}")
        if not move_id.startswith(f"agon.move.{move_class}."):
            raise ValidationError(f"{move_id}: move_id class segment must match move_class {move_class!r}")
        if binding.get("lineage_ref") != "owner-binding":
            raise ValidationError(f"{move_id}: lineage_ref must be owner-binding")
        if binding.get("binding_status") != "seeded_pre_protocol_owner_binding":
            raise ValidationError(f"{move_id}: invalid binding_status")
        if binding.get("live_protocol") is not False:
            raise ValidationError(f"{move_id}: live_protocol must remain false")
        if binding.get("runtime_effect") != "none":
            raise ValidationError(f"{move_id}: runtime_effect must remain none")
        if binding.get("readiness") != "owner_binding_seeded":
            raise ValidationError(f"{move_id}: invalid readiness")

        stop_lines = " ".join(binding.get("stop_lines", []))
        for word in STOP_WORDS:
            if word not in stop_lines:
                raise ValidationError(f"{move_id}: stop_lines must mention {word!r}")

        owner_bindings = binding.get("owner_bindings")
        if not isinstance(owner_bindings, list) or len(owner_bindings) < 2:
            raise ValidationError(f"{move_id}: owner_bindings must contain at least center + one owner")

        owner_repos = [ob.get("owner_repo") for ob in owner_bindings]
        if "Agents-of-Abyss" not in owner_repos:
            raise ValidationError(f"{move_id}: center law owner binding is required")
        if len(owner_repos) != len(set(owner_repos)):
            raise ValidationError(f"{move_id}: duplicate owner_repo in owner_bindings")

        for ob in owner_bindings:
            repo = ob.get("owner_repo")
            if repo not in ALLOWED_OWNER_REPOS:
                raise ValidationError(f"{move_id}: unknown owner_repo {repo!r}")
            status = ob.get("status")
            if repo == "Agents-of-Abyss" and status != "center_law_binding_seeded":
                raise ValidationError(f"{move_id}: center binding must be center_law_binding_seeded")
            if repo != "Agents-of-Abyss" and status != "requested_not_landed":
                raise ValidationError(f"{move_id}: non-center owner binding must be requested_not_landed")
            require_non_empty_string_list(
                ob.get("candidate_refs"),
                move_id=move_id,
                field=f"{repo} candidate_refs",
            )
            require_non_empty_string_list(
                ob.get("owns_later"),
                move_id=move_id,
                field=f"{repo} owns_later",
            )
            require_non_empty_string_list(
                ob.get("does_not_own"),
                move_id=move_id,
                field=f"{repo} does_not_own",
            )

        boundary = binding.get("assistant_boundary", "")
        for forbidden in ("contestant", "judge", "closer", "summon initiator", "scar writer", "ToS promotion"):
            if forbidden not in boundary:
                raise ValidationError(f"{move_id}: assistant boundary must explicitly forbid {forbidden}")


def build_registry(config: dict[str, Any]) -> dict[str, Any]:
    validate_config(config, require_lawful_move=False)

    owner_counts: Counter[str] = Counter()
    class_counts: Counter[str] = Counter()

    compact_bindings = []
    for binding in config["bindings"]:
        class_counts[binding["move_class"]] += 1
        owner_repos = []
        candidate_refs = []
        for ob in binding["owner_bindings"]:
            owner_counts[ob["owner_repo"]] += 1
            owner_repos.append(ob["owner_repo"])
            candidate_refs.extend(ob["candidate_refs"])

        compact_bindings.append(
            {
                "move_id": binding["move_id"],
                "name": binding["name"],
                "move_class": binding["move_class"],
                "owner_repos": owner_repos,
                "candidate_refs": candidate_refs,
                "live_protocol": binding["live_protocol"],
                "runtime_effect": binding["runtime_effect"],
                "readiness": binding["readiness"],
            }
        )

    return {
        "schema_version": "agon-move-owner-binding-registry/0.1",
        "lineage_ref": "owner-binding",
        "title": "Agon move owner binding registry",
        "status": "pre_protocol_owner_binding",
        "source_move_registry": config["source_move_registry"],
        "source_move_seed": config["source_move_seed"],
        "total_bindings": len(compact_bindings),
        "owner_counts": dict(sorted(owner_counts.items())),
        "move_class_counts": dict(sorted(class_counts.items())),
        "stop_line": (
            "owner binding does not create arena sessions, live protocol packets, verdicts, "
            "scars, retention, runtime transport, or Tree-of-Sophia promotion"
        ),
        "bindings": compact_bindings,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="fail if generated output is stale")
    parser.add_argument("--strict-lawful_move-check", action="store_true", help="also compare with lawful-move-grammar route move ids")
    args = parser.parse_args(argv)

    try:
        config = read_json(CONFIG_PATH)
        validate_config(config, require_lawful_move=args.strict_lawful_move_check)
        registry = build_registry(config)

        if args.check:
            existing = read_json(GENERATED_PATH)
            if existing != registry:
                raise ValidationError(f"{GENERATED_PATH} is stale; rerun without --check")
        else:
            write_json_min(GENERATED_PATH, registry)

        print(f"ok: {len(registry['bindings'])} Agon move owner bindings")
        return 0
    except ValidationError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
