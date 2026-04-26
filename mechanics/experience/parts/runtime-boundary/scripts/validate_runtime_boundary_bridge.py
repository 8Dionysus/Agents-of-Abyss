#!/usr/bin/env python3
"""Validate the Experience runtime boundary bridge contract."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator


def _repo_root() -> Path:
    for candidate in Path(__file__).resolve().parents:
        if (candidate / "mechanics" / "registry.json").is_file():
            return candidate
    raise RuntimeError("repo root not found")


ROOT = _repo_root()

SCHEMA_PATH = (
    ROOT
    / "mechanics"
    / "experience"
    / "parts"
    / "runtime-boundary"
    / "schemas"
    / "experience-runtime-boundary-bridge.schema.json"
)
EXAMPLE_PATH = (
    ROOT
    / "mechanics"
    / "experience"
    / "parts"
    / "runtime-boundary"
    / "examples"
    / "experience_runtime_boundary_bridge.example.json"
)

EXPECTED_SEEDS = [
    "experience.seed.service-mesh-operations",
    "experience.seed.office-role-pairs",
    "experience.seed.agonic-pair-trials-arena-kernel",
    "experience.seed.epistemic-duel-model-forge",
    "experience.seed.memory-rank-reputation",
    "experience.seed.affective-economy-honor-treasury",
    "experience.seed.context-routing",
    "experience.seed.continuity-loom",
    "experience.seed.living-workspace-continuity-runtime",
]

EXPECTED_ROUTE_KINDS = [
    "dionysus_intake",
    "center_bridge",
    "service_mesh_operations",
    "office_foundry_role_pairs",
    "mechanical_arena_kernel",
    "epistemic_duel_model_of_other",
    "rank_reputation_engine",
    "affective_honor_treasury",
    "context_routing_nervous_system",
    "continuity_loom",
    "living_workspace_continuity_runtime",
    "cross_repo_hardening",
    "dionysus_harvest_closure",
]

EXPECTED_ROUTE_SOURCE_VERSIONS = [
    None,
    None,
    "v1.2",
    "v1.3",
    "v1.4",
    "v1.5",
    "v1.6",
    "v1.7",
    "v1.8",
    "v1.9",
    "v2.0",
    None,
    None,
]

EXPECTED_OWNER_REPOS = {
    "8Dionysus",
    "Agents-of-Abyss",
    "Dionysus",
    "Tree-of-Sophia",
    "abyss-stack",
    "aoa-agents",
    "aoa-evals",
    "aoa-kag",
    "aoa-memo",
    "aoa-playbooks",
    "aoa-routing",
    "aoa-sdk",
    "aoa-skills",
    "aoa-stats",
    "aoa-techniques",
}

REQUIRED_PREDECESSOR_TOKENS = [
    "dionysus.experience-intake-note",
    "dionysus.experience-intake-map",
    "experience.raw.capture-kernel",
    "experience.raw.certification-watchtower",
    "experience.raw.federation-adoption",
    "experience.raw.polis-constitution",
    "experience.raw.sovereign-office",
    "experience.raw.agon-service-seam",
    "experience.raw.runtime-authority-boundary",
    "agon.pre-protocol-stop-lines",
    "agon.retention-rank-economy",
]

REQUIRED_CODEX_DENIALS = [
    "create a new aoa-experience repository",
    "copy raw archive proposals into owner truth",
    "open a live arena",
    "grant live summon authority",
    "grant live verdict authority",
    "write scars",
    "mutate rank reputation trust or honor",
    "schedule retention checks",
    "approve release certification or continuity",
    "install .codex/continuity",
    "activate services ports schedulers workers or daemons",
    "write directly to Tree-of-Sophia",
]

REQUIRED_ASSISTANT_DENIALS = [
    "become contestant",
    "become judge",
    "become closer",
    "become summoner",
    "become scar writer",
    "self-release",
    "self-enroll",
    "self-certify",
]

REQUIRED_DERIVED_DENIALS = {
    "stats_as_proof",
    "memo_as_truth",
    "routing_as_owner",
    "kag_as_canon",
    "sdk_as_authority",
    "dionysus_as_runtime",
}

REQUIRED_HUMAN_GATES = [
    "owner-local planting approval",
    "public-share sanitation review",
    "runtime-owner gate before any service or worker",
    "Tree-of-Sophia review before canon or interpretive intake",
]


class ValidationError(RuntimeError):
    """Raised when the Experience runtime boundary bridge drifts."""


def fail(message: str) -> None:
    raise ValidationError(message)


def _load_json(path: Path) -> dict[str, Any]:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        fail(f"missing JSON file: {path.relative_to(ROOT).as_posix()}")
        raise AssertionError from exc
    except json.JSONDecodeError as exc:
        fail(f"invalid JSON in {path.relative_to(ROOT).as_posix()}: {exc}")
        raise AssertionError from exc


def _assert_contains_all(text: str, tokens: list[str], surface: str) -> None:
    missing = [token for token in tokens if token not in text]
    if missing:
        fail(f"{surface} missing required tokens: {missing}")


def _assert_phrase_present(items: list[str], phrase: str, surface: str) -> None:
    if not any(phrase in item for item in items):
        fail(f"{surface} missing required phrase: {phrase}")


def validate_payload(payload: dict[str, Any], schema: dict[str, Any]) -> None:
    Draft202012Validator.check_schema(schema)
    errors = sorted(
        Draft202012Validator(schema).iter_errors(payload),
        key=lambda error: list(error.path),
    )
    if errors:
        path = ".".join(str(part) for part in errors[0].path) or "<root>"
        fail(f"bridge example does not match schema at {path}: {errors[0].message}")

    if payload["source_receipt_refs"] != EXPECTED_SEEDS:
        fail("source_receipt_refs must preserve the source-seed order exactly")

    route = payload["campaign_route"]
    if [step["order"] for step in route] != list(range(1, 14)):
        fail("campaign_route orders must be contiguous from 1 to 13")
    if [step["kind"] for step in route] != EXPECTED_ROUTE_KINDS:
        fail("campaign_route kinds must preserve the bridge spine")
    if [step.get("source_version") for step in route] != EXPECTED_ROUTE_SOURCE_VERSIONS:
        fail("campaign_route source_version mapping must preserve source provenance")

    if payload["status"] != "center_bridge_only":
        fail("bridge status must remain center_bridge_only")
    if payload["runtime_effect"] != "none":
        fail("bridge runtime_effect must remain none")

    predecessor_text = "\n".join(payload["predecessor_receipt_refs"])
    _assert_contains_all(
        predecessor_text,
        REQUIRED_PREDECESSOR_TOKENS,
        "predecessor_receipt_refs",
    )

    authority = payload["authority"]
    if authority["bridge_effect"] != "center_route_only":
        fail("bridge_effect must remain center_route_only")

    may_text = "\n".join(authority["codex_may"]).lower()
    forbidden_may_tokens = [
        "live arena",
        "live verdict",
        "live summon",
        "rank mutation",
        "honor mutation",
        "release approval",
        "continuity approval",
        "tree-of-sophia write",
        ".codex/continuity",
        "scheduler",
        "worker",
    ]
    leaked = [token for token in forbidden_may_tokens if token in may_text]
    if leaked:
        fail(f"codex_may grants forbidden authority: {leaked}")

    for phrase in REQUIRED_CODEX_DENIALS:
        _assert_phrase_present(authority["codex_must_not"], phrase, "codex_must_not")
    for phrase in REQUIRED_ASSISTANT_DENIALS:
        _assert_phrase_present(
            authority["assistant_must_not"],
            phrase,
            "assistant_must_not",
        )

    derived = set(authority["derived_layers_must_not"])
    if derived != REQUIRED_DERIVED_DENIALS:
        fail(
            "derived_layers_must_not must exactly deny stats, memo, routing, KAG, SDK, and Dionysus authority drift"
        )

    for phrase in REQUIRED_HUMAN_GATES:
        _assert_phrase_present(
            authority["human_gates_required"],
            phrase,
            "human_gates_required",
        )

    owners = {entry["repo"] for entry in payload["owner_split"]}
    if owners != EXPECTED_OWNER_REPOS:
        fail(f"owner_split repo set mismatch: {sorted(owners)}")

    for entry in payload["owner_split"]:
        if (
            entry["repo"] == "abyss-stack"
            and "separate runtime-owner gate" not in entry["owns"]
        ):
            fail("abyss-stack entry must require a separate runtime-owner gate")
        if (
            entry["repo"] == "Tree-of-Sophia"
            and "direct writes" not in entry["must_not"]
        ):
            fail("Tree-of-Sophia entry must deny direct writes")


def validate_files() -> None:
    for path in (SCHEMA_PATH, EXAMPLE_PATH):
        if not path.exists():
            fail(f"missing bridge surface: {path.relative_to(ROOT)}")

    schema = _load_json(SCHEMA_PATH)
    if schema.get("title") != "experience_runtime_boundary_bridge_v1":
        fail("schema title must remain experience_runtime_boundary_bridge_v1")
    if schema.get("additionalProperties") is not False:
        fail("schema must reject additional top-level properties")

    payload = _load_json(EXAMPLE_PATH)
    validate_payload(payload, schema)


def main() -> int:
    validate_files()
    print("ok: Experience runtime boundary bridge is valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
