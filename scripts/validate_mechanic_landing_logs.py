#!/usr/bin/env python3
"""Validate Agon and Experience landing logs."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FIELDS = (
    "Status:",
    "Owner boundary:",
    "Surfaces:",
    "Validation:",
    "Stop-lines:",
    "Next route:",
)

MECHANICS: dict[str, dict[str, object]] = {
    "agon": {
        "path": "mechanics/agon/LANDING_LOG.md",
        "required_phrases": (
            "Agon imposition gate",
            "Agon lawful move language",
            "Agon move owner binding",
            "Agon gate routing handoff",
            "Agon trial playbook handoff",
            "Later Agon center waves",
            "not live arena execution",
        ),
        "required_surfaces": (
            "mechanics/agon/docs/AGON_IMPOSITION_POSTURE.md",
            "mechanics/agon/docs/AGON_SURVIVAL_CRITERIA.md",
            "mechanics/agon/docs/AGON_DOUBT_AUDIT.md",
            "mechanics/agon/docs/PRE_AGON_BASELINE.md",
            "mechanics/agon/docs/AGON_WAVE0_LANDING.md",
            "generated/agon_imposition_readiness.min.json",
            "schemas/agon-imposition-readiness.schema.json",
            "examples/agon_doubt_audit.example.json",
            "scripts/build_agon_imposition_readiness.py",
            "scripts/validate_agon_imposition_readiness.py",
            "tests/test_agon_imposition_readiness.py",
            "mechanics/agon/docs/AGON_LAWFUL_MOVE_LANGUAGE.md",
            "mechanics/agon/docs/AGON_MOVE_REGISTRY_MODEL.md",
            "mechanics/agon/docs/AGON_MOVE_OWNER_HANDOFFS.md",
            "mechanics/agon/docs/AGON_WAVE3_LANDING.md",
            "config/agon_lawful_moves.seed.json",
            "generated/agon_lawful_move_registry.min.json",
            "schemas/agon-lawful-move.schema.json",
            "schemas/agon-lawful-move-registry.schema.json",
            "examples/agon_lawful_move.example.json",
            "scripts/build_agon_lawful_move_registry.py",
            "scripts/validate_agon_lawful_moves.py",
            "tests/test_agon_lawful_moves.py",
            "mechanics/agon/docs/AGON_MOVE_OWNER_BINDING.md",
            "mechanics/agon/docs/AGON_MOVE_BINDING_MATRIX_MODEL.md",
            "mechanics/agon/docs/AGON_OWNER_REPO_REQUESTS.md",
            "mechanics/agon/docs/AGON_PRE_PROTOCOL_STOP_LINES.md",
            "mechanics/agon/docs/AGON_WAVE4_LANDING.md",
            "config/agon_move_owner_bindings.seed.json",
            "generated/agon_move_owner_binding_registry.min.json",
            "schemas/agon-move-owner-binding.schema.json",
            "schemas/agon-move-owner-binding-registry.schema.json",
            "examples/agon_move_owner_binding.example.json",
            "scripts/build_agon_move_owner_binding_registry.py",
            "scripts/validate_agon_move_owner_bindings.py",
            "tests/test_agon_move_owner_bindings.py",
            "mechanics/agon/docs/AGON_GATE_ROUTING_HANDOFF.md",
            "mechanics/agon/docs/AGON_GATE_ROUTING_OWNER_REQUEST.md",
            "mechanics/agon/docs/AGON_GATE_ROUTING_STOP_LINES.md",
            "mechanics/agon/docs/AGON_WAVE5_CENTER_HANDOFF.md",
            "config/agon_gate_routing_handoff_request.seed.json",
            "generated/agon_gate_routing_handoff_request.min.json",
            "schemas/agon-gate-routing-handoff-request.schema.json",
            "examples/agon_gate_routing_handoff_request.example.json",
            "scripts/build_agon_gate_routing_handoff_request.py",
            "scripts/validate_agon_gate_routing_handoff_request.py",
            "tests/test_agon_gate_routing_handoff_request.py",
            "mechanics/agon/docs/AGON_TRIAL_PLAYBOOK_HANDOFF.md",
            "mechanics/agon/docs/AGON_TRIAL_PLAYBOOK_OWNER_REQUEST.md",
            "mechanics/agon/docs/AGON_TRIAL_PLAYBOOK_STOP_LINES.md",
            "mechanics/agon/docs/AGON_WAVE6_CENTER_HANDOFF.md",
            "config/agon_trial_playbook_request.seed.json",
            "generated/agon_trial_playbook_request.min.json",
            "schemas/agon-trial-playbook-request.schema.json",
            "examples/agon_trial_playbook_request.example.json",
            "scripts/build_agon_trial_playbook_request.py",
            "scripts/validate_agon_trial_playbook_request.py",
            "tests/test_agon_trial_playbook_request.py",
        ),
        "glob_families": (
            "mechanics/agon/docs/AGON_*.md",
            "generated/agon_*.min.json",
            "schemas/agon-*.schema.json",
            "config/agon_*.seed.json",
            "examples/agon_*.example.json",
            "scripts/*agon*.py",
            "tests/test_agon_*.py",
        ),
    },
    "experience": {
        "path": "mechanics/experience/LANDING_LOG.md",
        "required_phrases": (
            "Experience Wave 1 kernel",
            "Experience Wave 5 sovereign office",
            "Experience v1.2 to v2.0 bridge",
            "Experience v2.0 living workspace continuity runtime",
            "Experience active parts plus provenance bridge",
            "Experience active docs provenance-load cleanup",
            "does not activate live workspace",
        ),
        "required_surfaces": (
            "mechanics/experience/DIRECTION.md",
            "mechanics/experience/PARTS.md",
            "mechanics/experience/parts/README.md",
            "mechanics/experience/PROVENANCE.md",
            "mechanics/experience/OWNER_REQUESTS.md",
            "mechanics/experience/parts/capture-kernel/README.md",
            "mechanics/experience/parts/certification-proof/README.md",
            "mechanics/experience/parts/adoption-federation/README.md",
            "mechanics/experience/parts/governance-polis/README.md",
            "mechanics/experience/parts/office-operations/README.md",
            "mechanics/experience/parts/runtime-boundary/README.md",
            "mechanics/experience/parts/service-mesh/README.md",
            "mechanics/experience/parts/compatibility-bridges/README.md",
            "mechanics/experience/parts/continuity-context/README.md",
            "scripts/validate_experience_wave1.py",
            "scripts/validate_experience_wave2.py",
            "scripts/validate_experience_wave3.py",
            "scripts/validate_experience_wave4.py",
            "scripts/validate_experience_wave5.py",
            "scripts/validate_experience_distillation.py",
            "scripts/validate_experience_v1_2_to_v2_0_bridge.py",
            "scripts/validate_experience_v2_0_living_workspace_continuity_runtime.py",
            "tests/test_experience_wave1.py",
            "tests/test_experience_wave2.py",
            "tests/test_experience_wave3.py",
            "tests/test_experience_wave4.py",
            "tests/test_experience_wave5.py",
            "tests/test_experience_distillation.py",
            "tests/test_experience_v1_2_to_v2_0_bridge.py",
            "tests/test_experience_v2_0_living_workspace_continuity_runtime.py",
        ),
        "glob_families": (
            "mechanics/experience/legacy/raw/EXPERIENCE_*.md",
            "generated/experience_*.min.json",
            "schemas/experience-*.schema.json",
            "config/experience_*.seed.json",
            "examples/experience_*.example.json",
            "scripts/*experience*.py",
            "tests/test_experience_*.py",
        ),
    },
}


def iter_entries(text: str) -> list[tuple[str, str]]:
    matches = list(re.finditer(r"^### .+$", text, flags=re.MULTILINE))
    entries: list[tuple[str, str]] = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        title = match.group(0).removeprefix("### ").strip()
        entries.append((title, text[match.start() : end]))
    return entries


def looks_like_surface(ref: str) -> bool:
    return (
        "/" in ref
        or ref.endswith((".md", ".py", ".json"))
        or ref in {"README.md", "ROADMAP.md", "CHANGELOG.md"}
    )


def validate_log(mechanic: str) -> list[str]:
    spec = MECHANICS[mechanic]
    rel_path = str(spec["path"])
    path = REPO_ROOT / rel_path
    problems: list[str] = []

    if not path.exists():
        return [f"{rel_path}: missing"]

    text = path.read_text(encoding="utf-8")
    if not text.endswith("\n"):
        problems.append(f"{rel_path}: missing final newline")

    for phrase in spec["required_phrases"]:
        if str(phrase) not in text:
            problems.append(f"{rel_path}: missing required phrase {phrase!r}")

    entries = iter_entries(text)
    if not entries:
        problems.append(f"{rel_path}: missing landing entries")

    for title, entry in entries:
        for field in REQUIRED_FIELDS:
            if field not in entry:
                problems.append(f"{rel_path}: entry {title!r} missing {field}")

    for surface in spec["required_surfaces"]:
        surface_text = str(surface)
        if f"`{surface_text}`" not in text:
            problems.append(f"{rel_path}: missing required surface `{surface_text}`")
        if not (REPO_ROOT / surface_text).exists():
            problems.append(f"{rel_path}: listed required surface does not exist: {surface_text}")

    for match in re.finditer(r"`([^`]+)`", text):
        ref = match.group(1)
        if not looks_like_surface(ref):
            continue
        path_ref = ref.partition("#")[0]
        if "*" in path_ref:
            continue
        if path_ref.startswith(("python ", "v")):
            continue
        if not (REPO_ROOT / path_ref).exists():
            problems.append(f"{rel_path}: backtick surface does not exist: {ref}")

    return problems


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate mechanic LANDING_LOG surfaces.")
    parser.add_argument(
        "--mechanic",
        choices=sorted(MECHANICS),
        action="append",
        help="Mechanic to validate; may be passed more than once. Defaults to all.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    mechanics = args.mechanic or sorted(MECHANICS)
    problems: list[str] = []
    for mechanic in mechanics:
        problems.extend(validate_log(mechanic))

    if problems:
        print("Mechanic landing log validation failed:")
        for problem in problems:
            print(f"  - {problem}")
        return 1

    print("[ok] validated mechanic LANDING_LOG surfaces: " + ", ".join(mechanics))
    return 0


if __name__ == "__main__":
    sys.exit(main())
