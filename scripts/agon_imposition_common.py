#!/usr/bin/env python3
"""Shared builder helpers for the Agon Imposition readiness capsule."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[1]
READINESS_PATH = REPO_ROOT / "generated" / "agon_imposition_readiness.min.json"
SCHEMA_REF = "schemas/agon-imposition-readiness.schema.json"

AUTHORITY_REFS = (
    "mechanics/agon/docs/AGON_IMPOSITION_POSTURE.md",
    "mechanics/agon/docs/AGON_SURVIVAL_CRITERIA.md",
    "mechanics/agon/docs/AGON_DOUBT_AUDIT.md",
    "mechanics/agon/docs/PRE_AGON_BASELINE.md",
    "mechanics/agon/docs/AGON_WAVE0_LANDING.md",
)

BASELINE_REFS = (
    "README.md",
    "CHARTER.md",
    "ECOSYSTEM_MAP.md",
    "docs/LAYERS.md",
    "docs/FEDERATION_RULES.md",
    "mechanics/antifragility/docs/ANTI_AUTHORITY_RULES.md",
    "mechanics/agon/docs/AGON_PREPARATION_POSTURE.md",
    "ROADMAP.md",
)

VALIDATION_REFS = (
    "scripts/build_agon_imposition_readiness.py",
    "scripts/validate_agon_imposition_readiness.py",
    "tests/test_agon_imposition_readiness.py",
)

SURVIVAL_AXES: tuple[dict[str, str], ...] = (
    {
        "axis": "lawful_conflict_support",
        "question": "Does the surface help future conflict become reviewable state change rather than chat theater?",
        "owner_guard": "Do not let protocol law leak into owner repositories that only provide inputs, proof, memory, routing, or runtime support.",
    },
    {
        "axis": "source_ownership_discipline",
        "question": "Does the surface preserve source-owned meaning instead of letting the center or a derived layer absorb it?",
        "owner_guard": "Owner repositories keep their object-class truth; the center names boundaries and constitutional law only.",
    },
    {
        "axis": "actor_formation_readiness",
        "question": "Can the future arena distinguish agonic actors from civil/service assistants before protocol sessions open?",
        "owner_guard": "Actor form belongs in aoa-agents; arena law belongs in Agents-of-Abyss.",
    },
    {
        "axis": "witnessability",
        "question": "Can claims be inspected through docs, schemas, generated capsules, receipts, validators, or owner references?",
        "owner_guard": "Unwitnessed authority is not Agon-ready.",
    },
    {
        "axis": "memory_proof_stat_separation",
        "question": "Does the surface keep scars, verdicts, and derived summaries in their owning layers instead of fusing them into one authority?",
        "owner_guard": "Memo recalls; evals prove; stats derive; none reign alone.",
    },
    {
        "axis": "assistant_anti_drift",
        "question": "Does the surface prevent service assistants from becoming hidden contestants by gradual drift?",
        "owner_guard": "Civil/service actor governance must require explicit owner-reviewed recharter before any arena contestant role.",
    },
    {
        "axis": "tos_canon_restraint",
        "question": "Does the surface prevent direct arena-to-Tree canonization?",
        "owner_guard": "Arena outcomes may become candidates only through reviewable memory, proof, derived substrate, and ToS-owned judgment.",
    },
    {
        "axis": "runtime_restraint",
        "question": "Does the surface avoid claiming live services before protocol and runtime owners have landed contracts?",
        "owner_guard": "Doctrine is not runtime; runtime belongs to abyss-stack when the protocol is ready.",
    },
)

OWNER_HANDOFFS: tuple[dict[str, str], ...] = (
    {
        "concern": "Agonic actor form and civil/service assistant split",
        "owner": "aoa-agents",
        "boundary": "Own role-facing actor form, kind split, office posture, refusal posture, and eligibility; do not own arena protocol, scars, verdicts, runtime packets, or ToS promotion.",
        "next_wave": "Wave I and Wave II rechartering",
    },
    {
        "concern": "Reusable pressure-handling practice",
        "owner": "aoa-techniques",
        "boundary": "Own reusable practice patterns only; do not define lawful arena sessions.",
        "next_wave": "Wave III language of lawful moves input",
    },
    {
        "concern": "Bounded executable moves",
        "owner": "aoa-skills",
        "boundary": "Own execution workflows only; admissibility and protocol law remain center-owned.",
        "next_wave": "Wave III language of lawful moves input",
    },
    {
        "concern": "Arena entry detection",
        "owner": "aoa-routing",
        "boundary": "Own thin gates and next-hop hints; do not judge truth or own session lifecycle.",
        "next_wave": "After actor formation and protocol kernel",
    },
    {
        "concern": "Trial rituals and early mechanical campaigns",
        "owner": "aoa-playbooks",
        "boundary": "Own recurring scenario choreography; do not become arena sovereignty.",
        "next_wave": "After protocol kernel and lawful moves",
    },
    {
        "concern": "Session verdicts and breach checks",
        "owner": "aoa-evals",
        "boundary": "Own proof and bounded verdict surfaces; do not become readiness government.",
        "next_wave": "After center protocol kernel",
    },
    {
        "concern": "Scars, delta history, and retention recall",
        "owner": "aoa-memo",
        "boundary": "Own memory truth; do not certify present health or proof.",
        "next_wave": "After center protocol kernel and eval verdict surface",
    },
    {
        "concern": "Derived Agon movement summaries",
        "owner": "aoa-stats",
        "boundary": "Own derived observability; do not become score authority or judge.",
        "next_wave": "After proof and memory receipts exist",
    },
    {
        "concern": "Derived survivor structures",
        "owner": "aoa-kag",
        "boundary": "Own derived lifts only; do not replace source meaning or ToS canon.",
        "next_wave": "After retention and proof-backed survivor candidates exist",
    },
    {
        "concern": "Typed helper seams and control-plane support",
        "owner": "aoa-sdk",
        "boundary": "Support protocol consumption only after protocol surfaces exist; do not hide policy in helpers.",
        "next_wave": "After protocol kernel is stable",
    },
    {
        "concern": "Durable runtime body",
        "owner": "abyss-stack",
        "boundary": "Run services only after law, proof, memory, routing, and persistence contracts exist.",
        "next_wave": "Late runtime wave",
    },
    {
        "concern": "Slow canonization",
        "owner": "Tree-of-Sophia",
        "boundary": "Own source-first canonization; no direct arena write path.",
        "next_wave": "Only after memo, eval, KAG, and ToS-owned review",
    },
)

STOP_LINES = (
    "Do not claim a live Agon runtime in Wave 0.",
    "Do not create a new Agon-of-Abyss sibling repository.",
    "Do not add arena session, lawful move, contradiction ledger, verdict, scar, or retention schemas in Wave 0.",
    "Do not treat release-clean as Agon-ready.",
    "Do not let assistants become hidden contestants.",
    "Do not let stats, evals, memo, routing, SDK, runtime, or KAG become sovereign over Agon.",
    "Do not write directly from arena outcomes into Tree-of-Sophia canon.",
)

NEXT_ALLOWED_WAVES = (
    "Wave I: Agonic Actor Rechartering in aoa-agents",
    "Wave II: Assistant Civil Rechartering in aoa-agents",
    "Wave II.5: Formation Trial before lawful move language",
)

VERDICTS = ("survive", "recharter", "defer", "prune", "quarantine")


def resolve_local_ref(value: str) -> Path:
    path_text, _, _anchor = value.partition("#")
    target = REPO_ROOT / path_text
    if not target.exists():
        raise ValueError(f"missing local ref: {value}")
    return target


def build_payload() -> dict[str, Any]:
    payload: dict[str, Any] = {
        "schema_version": "agon_imposition_readiness_v1",
        "owner_repo": "Agents-of-Abyss",
        "surface_kind": "agon_imposition_gate",
        "status": "seed",
        "imposition_statement": "Agon is not adapted to the current system; the current system is audited for Agon survival.",
        "authority_refs": list(AUTHORITY_REFS),
        "baseline_refs": list(BASELINE_REFS),
        "survival_axes": [dict(axis) for axis in SURVIVAL_AXES],
        "verdicts": list(VERDICTS),
        "owner_handoffs": [dict(handoff) for handoff in OWNER_HANDOFFS],
        "stop_lines": list(STOP_LINES),
        "validation_refs": list(VALIDATION_REFS),
        "next_allowed_waves": list(NEXT_ALLOWED_WAVES),
    }
    validate_payload(payload, check_refs=False)
    return payload


def render_payload(payload: dict[str, Any]) -> str:
    return json.dumps(payload, ensure_ascii=False, separators=(",", ":"), sort_keys=False) + "\n"


def validate_payload(payload: dict[str, Any], *, check_refs: bool) -> None:
    required = {
        "schema_version",
        "owner_repo",
        "surface_kind",
        "status",
        "imposition_statement",
        "authority_refs",
        "baseline_refs",
        "survival_axes",
        "verdicts",
        "owner_handoffs",
        "stop_lines",
        "validation_refs",
        "next_allowed_waves",
    }
    missing = sorted(required - set(payload))
    if missing:
        raise ValueError(f"missing required fields: {', '.join(missing)}")
    if payload["schema_version"] != "agon_imposition_readiness_v1":
        raise ValueError("unexpected schema_version")
    if payload["owner_repo"] != "Agents-of-Abyss":
        raise ValueError("owner_repo must be Agents-of-Abyss")
    if payload["surface_kind"] != "agon_imposition_gate":
        raise ValueError("surface_kind must be agon_imposition_gate")
    if payload["status"] not in {"seed", "landed", "superseded"}:
        raise ValueError("status must be seed, landed, or superseded")
    if set(payload["verdicts"]) != set(VERDICTS):
        raise ValueError("verdicts must contain exactly the five Agon survival verdicts")
    if len(payload["survival_axes"]) < 8:
        raise ValueError("survival_axes must contain the Wave 0 survival lens")
    if len(payload["owner_handoffs"]) < 10:
        raise ValueError("owner_handoffs must name the federation owners affected by Agon")
    if check_refs:
        resolve_local_ref(SCHEMA_REF)
        for ref in list(payload["authority_refs"]) + list(payload["baseline_refs"]) + list(payload["validation_refs"]):
            resolve_local_ref(str(ref))


def main_build(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Build the Agon Imposition readiness capsule.")
    parser.add_argument("--check", action="store_true", help="check without rewriting generated output")
    args = parser.parse_args(argv)
    expected = render_payload(build_payload())
    if args.check:
        current = READINESS_PATH.read_text(encoding="utf-8")
        if current != expected:
            raise SystemExit("generated/agon_imposition_readiness.min.json is stale; rebuild it")
        print("[ok] generated/agon_imposition_readiness.min.json is current")
        return 0
    READINESS_PATH.write_text(expected, encoding="utf-8")
    print(f"[ok] wrote {READINESS_PATH.relative_to(REPO_ROOT)}")
    return 0


def main_validate() -> int:
    payload = json.loads(READINESS_PATH.read_text(encoding="utf-8"))
    validate_payload(payload, check_refs=True)
    expected = build_payload()
    if payload != expected:
        raise SystemExit("generated/agon_imposition_readiness.min.json does not match canonical rebuild")
    print("[ok] validated generated/agon_imposition_readiness.min.json")
    return 0
