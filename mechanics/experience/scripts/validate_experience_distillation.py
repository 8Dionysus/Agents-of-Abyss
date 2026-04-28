#!/usr/bin/env python3
"""Validate Experience active parts and the single provenance bridge."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


def _repo_root() -> Path:
    for candidate in Path(__file__).resolve().parents:
        if (candidate / "mechanics" / "registry.json").is_file():
            return candidate
    raise RuntimeError("repo root not found")


REPO_ROOT = _repo_root()
EXPERIENCE_ROOT = REPO_ROOT / "mechanics" / "experience"
LEGACY_ROOT = EXPERIENCE_ROOT / "legacy"
RAW_ROOT = LEGACY_ROOT / "raw"
PARTS_ROOT = EXPERIENCE_ROOT / "parts"
PARTS_AGENTS_PATH = PARTS_ROOT / "AGENTS.md"
ARTIFACT_MAP_PATH = EXPERIENCE_ROOT / "artifact-map.json"
PROVENANCE_RECEIPTS_PATH = EXPERIENCE_ROOT / "provenance-receipts.json"
REGISTRY_PATH = REPO_ROOT / "mechanics" / "registry.json"
PROVENANCE_PATH = EXPERIENCE_ROOT / "PROVENANCE.md"
MECHANICS_ATLAS_PATH = REPO_ROOT / "mechanics" / "README.md"
THEMATIC_DISTRICTS_PATH = REPO_ROOT / "docs" / "guardrails" / "thematic_districts.json"

PART_SLUGS = (
    "capture-kernel",
    "certification-proof",
    "adoption-federation",
    "governance-polis",
    "release-deployment",
    "office-operations",
    "service-mesh",
    "continuity-context",
    "runtime-boundary",
    "compatibility-bridges",
)

ROOT_SURFACES = (
    "README.md",
    "DIRECTION.md",
    "PARTS.md",
    "PROVENANCE.md",
    "LANDING_LOG.md",
    "ROADMAP.md",
    "OWNER_REQUESTS.md",
    "AGENTS.md",
)

LEGACY_SURFACES = (
    "AGENTS.md",
    "README.md",
    "INDEX.md",
    "DISTILLATION_LOG.md",
    "artifacts/README.md",
    "raw/README.md",
)

PART_SURFACES = (
    "README.md",
    "CONTRACT.md",
    "VALIDATION.md",
)

STALE_ACTIVE_REFS = (
    "mechanics/experience/docs/EXPERIENCE_",
    "experience/docs/EXPERIENCE_",
    "docs/EXPERIENCE_",
    "EXPERIENCE_OWNER_REPO_REQUESTS.md",
)

ACTIVE_TEXT_SUFFIXES = (".md", ".py", ".json", ".yaml", ".yml", ".toml", ".txt")
PART_ARTIFACT_DIRS = (
    "schemas",
    "examples",
    "config",
    "generated",
    "scripts",
    "tests",
)
ARTIFACT_PREFIXES = (
    "config/",
    "examples/",
    "generated/",
    "schemas/",
    "scripts/",
    "tests/",
)
ROOT_ARTIFACT_ALLOWLIST = {
    "scripts": {"validate_experience_distillation.py"},
    "tests": {"test_experience_distillation.py"},
}
PART_ARTIFACT_STATUSES = {
    "active-part-artifact",
    "active-part-validator",
    "active-part-test",
}
PACKAGE_ARTIFACT_STATUSES = {"package-validator", "package-test"}
ACTIVE_ARCHIVE_LOAD_PATTERNS = (
    "legacy/",
    "Legacy raw",
    "Primary raw provenance",
    "raw provenance",
    "raw source",
    "raw-source",
)
ACTIVE_ARCHIVE_FILENAME_RE = re.compile(r"EXPERIENCE_[A-Z0-9_]+\.md")

ACTIVE_ROUTE_POLLUTION_PATTERNS = (
    "low-context",
    "small enough",
    "legacy provenance",
    "archival sources consulted",
    "consulted through the provenance bridge",
    "sources that still need deeper distillation",
    "raw surface",
    "raw surfaces",
    "raw file",
    "raw files",
    "named by any raw",
    "touching legacy provenance",
)

ACTIVE_RELEASE_CONTOUR_FILENAME_RE = re.compile(
    r"(?:experience[-_]wave\d+|experience[-_]v\d+(?:[-_]\d+)*|"
    r"test_experience_(?:wave\d+|v\d+)|validate_experience_(?:wave\d+|v\d+))",
    re.IGNORECASE,
)
ACTIVE_RELEASE_CONTOUR_IDENTITY_RE = re.compile(
    r"\bexperience[-_](?:wave\d+|v\d+(?:[-_]\d+)*)", re.IGNORECASE
)
ACTIVE_RELEASE_CONTOUR_PY_RE = re.compile(
    r"\b(?:Experience\s+(?:Wave\s*\d+|v\d)|"
    r"(?:test|validate)_experience_(?:wave\d+|v\d+)|"
    r"WAVE\d+_CONTRACTS|wave\d+_stems|test_seeded_wave\d+|__wave\d+)",
    re.IGNORECASE,
)
ACTIVE_RELEASE_CONTOUR_VALUE_RE = re.compile(r"\bwave\d+", re.IGNORECASE)
ACTIVE_RELEASE_CONTOUR_VALUE_ALLOW_RE = re.compile(
    r"(?:legacy/raw/|AGON_WAVE\d+|seed_aoa_experience_wave0)", re.IGNORECASE
)
ACTIVE_ARTIFACT_IDENTITY_KEYS = {
    "bridge_id",
    "campaign_ref",
    "contract_ref",
    "flow_id",
    "planting_id",
    "schema_id",
}
RECEIPT_ID_RE = re.compile(r"^[a-z0-9]+(?:[.-][a-z0-9]+)*$")
ACTIVE_DIRECT_PROVENANCE_RE = re.compile(
    r"(?:mechanics/experience/legacy/raw/|"
    r"Dionysus:seed_staging/|"
    r"seed_staging/future/seed_aoa_experience_|"
    r"mechanics/agon/docs/|"
    r"mechanics/method-growth/docs/|"
    r"mechanics/recurrence/docs/|"
    r"8Dionysus:docs/|"
    r"docs/FEDERATION_RULES\.md|"
    r"aoa-experience-[A-Za-z0-9_-]+-seed-v)"
)

STALE_ROADMAP_PATTERNS = (
    "Keep Wave 1-5 and v1.2-v2.0 surfaces in `docs/`",
    "surfaces in `docs/`",
    "package-local migration next",
)

VAGUE_VALIDATION_PHRASES = (
    "targeted validators",
    "matching tests for the touched surface",
    "validator named by the bridge surface",
    "targeted deployment",
    "targeted office validators",
    "tests named by any raw",
    "named by any raw surface",
)

OWNER_STOP_LINE_PHRASES = (
    "live workspace runtime or service dispatch",
    "hidden memory sovereignty or recall authority",
    "live router engine authority",
    "owner-local activation, office installation, or adoption",
    "proof verdicts, certification truth, or regression evidence before `aoa-evals` lands them",
    "`aoa-kag` projections as source-authored meaning",
    "ToS-authored meaning or canon",
)

PART_STOP_LINE_PHRASES = {
    "capture-kernel": (
        "hidden memory sovereignty or recall authority",
        "Live route behavior",
    ),
    "certification-proof": ("certification truth", "Operational Experience adoption"),
    "adoption-federation": (
        "Owner-local activation, adoption, or acceptance",
        "Operational Experience adoption",
    ),
    "governance-polis": ("runtime enforcement", "Hidden precedent ledger"),
    "release-deployment": (
        "runtime deployment",
        "Owner-local activation, installation, or acceptance",
    ),
    "office-operations": ("Owner-local office activation", "Hybrid-agent authority"),
    "service-mesh": ("Live service runtime", "Live dispatch behavior"),
    "continuity-context": ("ambient continuity", "Live router engine authority"),
    "runtime-boundary": (
        "runtime owner gates",
        "services, storage, or lifecycle authority",
    ),
    "compatibility-bridges": ("source-authored meaning", "ToS canon"),
}

RAW_REF_RE = re.compile(r"mechanics/experience/legacy/raw/(EXPERIENCE_[A-Z0-9_]+\.md)")
PART_VALIDATOR_RAW_READ_PATTERN = 'ROOT / "mechanics" / "experience" / "legacy" / "raw"'

RAW_DOC_TOKEN_REQUIREMENTS = {
    "EXPERIENCE_WAVE1_KERNEL.md": (
        "friction_observed",
        "recurrence_detected",
        "candidate_declared",
        "review_verdict_recorded",
        "memory_gate_decided",
        "owner_route_selected",
        "projection_proposed",
        "hidden runtime execution",
        "automatic projection",
    ),
    "EXPERIENCE_WAVE2_CERTIFICATION_WATCHTOWER.md": (
        "Codex may not certify",
        "No Codex ring promotion",
        "No assistant self-deployment",
        "release is not done at activation",
        "contract-only",
        "no live service activation",
    ),
    "EXPERIENCE_WAVE3_FEDERATION_ADOPTION.md": (
        "Harvest approval is not adoption authority",
        "no direct `Tree-of-Sophia` write",
        "no Codex approval of federation harvest",
        "no assistant hidden self-rewrite",
        "no runtime activation without owner-local approval",
    ),
    "EXPERIENCE_WAVE4_POLIS_CONSTITUTION.md": (
        "Codex must not vote",
        "Assistant agents must not self-recharter",
        "Runtime jobs must not become the source of constitutional meaning",
        "no direct governance or runtime write",
    ),
    "EXPERIENCE_WAVE5_SOVEREIGN_OFFICE.md": (
        "Codex may not certify",
        "`notary.assistant` remains the first receipt-bearing office anchor",
        "allow direct runtime writes into `Tree-of-Sophia`",
        "Stats summarizes. Memo remembers. Evals judges. Routing points.",
    ),
    "EXPERIENCE_V1_2_TO_V2_0_BRIDGE.md": (
        "It is not `Experience Wave 1`",
        "`Dionysus` staged intake",
        "owner-local planting waves",
        "`EXPERIENCE_WAVE1_KERNEL.md`",
        "`EXPERIENCE_WAVE5_SOVEREIGN_OFFICE.md`",
        "`EXPERIENCE_AGON_SERVICE_SEAM_V1_1.md`",
        "`EXPERIENCE_RUNTIME_AUTHORITY_BOUNDARY.md`",
        "`AGON_PRE_PROTOCOL_STOP_LINES.md`",
        "create a new `aoa-experience` repository",
        "open a live arena",
        "install `.codex/continuity`",
        "write directly to `Tree-of-Sophia`",
        "stats become proof",
        "memo become truth",
        "routing become owner",
        "KAG become canon",
        "SDK become authority",
        "`Dionysus` become runtime",
    ),
    "EXPERIENCE_V1_2_SERVICE_MESH_OPERATIONS.md": (
        "It is Wave 2 of the current v1.2-v2.0 planting campaign",
        "It is not `Experience Wave 2`",
        "`aoa-experience-service-mesh-operations-seed-v1_2.zip`",
        "df829241ac629770635290e5da2742b81e4d5575270c94a92c34a95f4bbacb85",
        "`EXPERIENCE_V1_1_LIVE_OFFICE_EXPANSION.md`",
        "`EXPERIENCE_SERVICE_MESH_LAW.md`",
        "`EXPERIENCE_V1_2_TO_V2_0_BRIDGE.md`",
        "`EXPERIENCE_RUNTIME_AUTHORITY_BOUNDARY.md`",
        "`AGON_PRE_PROTOCOL_STOP_LINES.md`",
        "`no_hidden_assistant_self_heal`",
        "`no_drill_pass_by_codex`",
        "activate live services",
        "service-to-Agon escalation into live summon authority",
        "stats become proof",
        "memo become truth",
        "routing become owner",
        "KAG become canon",
        "SDK become authority",
    ),
    "EXPERIENCE_V1_3_OFFICE_FOUNDRY_ROLE_PAIRS.md": (
        "It is Wave 3 of the current v1.2-v2.0 planting campaign",
        "It is not `Experience Wave 3`",
        "`aoa-experience-office-foundry-role-pairs-seed-v1_3.zip`",
        "d7ccb771f742540fcee0becdbfc79de69c2f97b5704ac067029fec23fef90648",
        "`EXPERIENCE_V1_2_SERVICE_MESH_OPERATIONS.md`",
        "`EXPERIENCE_RUNTIME_AUTHORITY_BOUNDARY.md`",
        "`AGON_PRE_PROTOCOL_STOP_LINES.md`",
        "office names the work",
        "kind names the mode of becoming",
        "`no_hybrid_agent`",
        "`no_assistant_self_recharter`",
        "`no_codex_pair_approval`",
        "hybrid runtime mask",
        "`active` is not a landing state",
        "durable writes are forbidden",
        "fixture/generated-result disagreement is a validation failure",
        "stats become proof",
        "memo become truth",
        "routing become owner",
        "KAG become canon",
        "SDK become authority",
        "evals become certification authority",
    ),
    "EXPERIENCE_V1_4_AGONIC_PAIR_TRIALS_MECHANICAL_ARENA_KERNEL.md": (
        "It is Wave 4 of the current v1.2-v2.0 planting campaign",
        "It is not `Experience Wave 4`",
        "`aoa-experience-agonic-pair-trials-mechanical-arena-kernel-seed-v1_4.zip`",
        "c62a9c38b662ad7c62405c7ca2ac75fe5ea7cc05f13e001a141ad60cf2f5f404",
        "`EXPERIENCE_V1_3_OFFICE_FOUNDRY_ROLE_PAIRS.md`",
        "`AGON_ARENA_SESSION_MODEL.md`",
        "`AGON_DUEL_KERNEL_MODEL.md`",
        "`AGON_MECHANICAL_TRIALS_OVER_DUEL_KERNEL.md`",
        "Current Agon arena, packet, verdict, duel-kernel, and mechanical-trial surfaces",
        "No arena without charter",
        "No contestant without agonic kind",
        "No stance without sealed commit",
        "No summon without visible request and cost",
        "`no_live_arena_activation`",
        "`no_assistant_contestant`",
        "`no_codex_arena_verdict`",
        "`active` is not a landing state",
        "generated clean-flow examples may inform checks",
        "stats become proof",
        "memo become truth",
        "routing become owner",
        "KAG become canon",
        "SDK become authority",
        "evals become live verdict authority",
    ),
    "EXPERIENCE_V1_5_EPISTEMIC_DUEL_MODEL_OF_OTHER_FORGE.md": (
        "It is Wave 5 of the current v1.2-v2.0 planting campaign",
        "It is not `Experience Wave 5`",
        "`aoa-experience-epistemic-duel-model-of-other-forge-seed-v1_5.zip`",
        "51349824b23af2da3434e0ba6ce95fe6c5faf32bdb449b98e793d2912c73ff05",
        "`EXPERIENCE_V1_4_AGONIC_PAIR_TRIALS_MECHANICAL_ARENA_KERNEL.md`",
        "`AGON_MODEL_OF_OTHER_LAW.md`",
        "`AGON_EPISTEMIC_AGON.md`",
        "`AGON_RETENTION_RANK_ECONOMY.md`",
        "No model-of-other without sealed prediction",
        "No caricature model and no mind-reading claim",
        "`no_live_duel_activation`",
        "`no_assistant_deep_modeling`",
        "`no_codex_truth_verdict`",
        "`active` is not a landing state",
        "generated clean-flow examples may inform checks",
        "stats become proof",
        "memo become truth",
        "routing become owner",
        "KAG become canon",
        "model-of-other become truth",
    ),
    "EXPERIENCE_V1_6_EPISTEMIC_MEMORY_RANK_REPUTATION_ENGINE.md": (
        "It is Wave 6 of the current v1.2-v2.0 planting campaign",
        "It is not `Experience Wave 6`",
        "`aoa-experience-epistemic-memory-rank-reputation-engine-seed-v1_6.zip`",
        "51e403eb0ca9ac384b1edba959b67bdf457efc5813ba3aa7577e94ee87591475",
        "`EXPERIENCE_V1_5_EPISTEMIC_DUEL_MODEL_OF_OTHER_FORGE.md`",
        "`AGON_RETENTION_RANK_ECONOMY.md`",
        "`AGON_RANK_JURISDICTION_MODEL.md`",
        "`AGON_CONTRADICTION_CLOSURE_SUMMON_LAW.md`",
        "no standing is earned by a single blaze",
        "Closure is earned jurisdiction, not default completion",
        "Summon is costly visible intent, not a panic button",
        "`no_live_rank_mutation`",
        "`no_assistant_agonic_rank`",
        "`no_direct_tree_of_sophia_or_kag_canon`",
        "`active` is not a landing state",
        "turn memo candidates into durable memory",
        "treat generated clean-flow results as landed owner truth",
    ),
    "EXPERIENCE_V1_7_AFFECTIVE_ECONOMY_HONOR_TREASURY.md": (
        "It is Wave 7 of the current v1.2-v2.0 planting campaign",
        "It is not `Experience Wave 7`",
        "`aoa-experience-affective-economy-honor-treasury-seed-v1_7.zip`",
        "328872f61d4ffa16fdfd1315bf90c48ff4cfa7960b9b500275f6c8872bfe338e",
        "`EXPERIENCE_V1_6_EPISTEMIC_MEMORY_RANK_REPUTATION_ENGINE.md`",
        "`AGON_WAVE7_CENTER_HANDOFF.md`",
        "`AGON_COURT_MEMO_STATS_PREBINDING_STOP_LINES.md`",
        "`AGON_WAVE17_STOP_LINES.md`",
        "affect is a bounded control signal, not proof of consciousness",
        "claiming an affective delta is not applying a delta",
        "`no_live_affect_governance`",
        "`no_assistant_persistent_affect_rewrite`",
        "`no_direct_tree_of_sophia_or_kag_canon`",
        "`active` is not a landing state",
        "turn honor into a sovereign score or treasury court",
        "treat generated clean-flow results as landed owner truth",
    ),
    "EXPERIENCE_V1_8_CONTEXT_ROUTING_NERVOUS_SYSTEM.md": (
        "It is Wave 8 of the current v1.2-v2.0 planting campaign.",
        "It is not `Experience Wave VIII`;",
        "routing may activate layers; it may not steal meaning from their owners",
    ),
    "EXPERIENCE_V1_9_CONTEXT_MEMORY_WEAVING_CONTINUITY_LOOM.md": (
        "aoa-experience-context-memory-weaving-continuity-loom-seed-v1_9.zip",
        "It is Wave 9 of the current `v1.2 -> v2.0` planting campaign.",
        "`Experience Wave IX`",
        "No private memory sovereignty.",
        "No runtime continuity installation.",
        "not a live continuity runtime",
    ),
    "EXPERIENCE_V2_0_LIVING_WORKSPACE_CONTINUITY_RUNTIME.md": (
        "aoa-experience-living-workspace-continuity-runtime-seed-v2_0.zip",
        "It is Wave 10 of the current `v1.2 -> v2.0` planting campaign.",
        "It is not a live workspace runtime",
        "No hidden `.codex/continuity` installation.",
        "No Codex durable continuity approval.",
        "No direct `Tree-of-Sophia` runtime write.",
        "`aoa-kag` owns derived pattern lift only after later owner-local landing.",
        "not install `.codex/continuity`",
    ),
}

RAW_DOC_BANNED_SNIPPETS = {
    "EXPERIENCE_V1_9_CONTEXT_MEMORY_WEAVING_CONTINUITY_LOOM.md": (
        "aoa-experience-context-routing-nervous-system-seed-v1_8.zip",
        "It is Wave 8 of the current v1.2-v2.0 planting campaign.",
    ),
    "EXPERIENCE_V2_0_LIVING_WORKSPACE_CONTINUITY_RUNTIME.md": (
        "aoa-experience-context-memory-weaving-continuity-loom-seed-v1_9.zip",
        "It is Wave 9 of the current `v1.2 -> v2.0` planting campaign.",
    ),
}


def rel(path: Path) -> str:
    return path.relative_to(REPO_ROOT).as_posix()


def load_registry() -> dict[str, object]:
    return json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))


def load_artifact_map() -> dict[str, object]:
    return json.loads(ARTIFACT_MAP_PATH.read_text(encoding="utf-8"))


def load_provenance_receipts() -> dict[str, object]:
    return json.loads(PROVENANCE_RECEIPTS_PATH.read_text(encoding="utf-8"))


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def normalize(value: str) -> str:
    value = value.replace("`", "")
    return re.sub(r"\s+", " ", value.casefold()).strip()


def contains_phrase(text: str, phrase: str) -> bool:
    return normalize(phrase) in normalize(text)


def require_file(path: Path, problems: list[str]) -> None:
    if not path.is_file():
        problems.append(f"missing file: {rel(path)}")
        return
    text = read(path)
    if not text.endswith("\n"):
        problems.append(f"{rel(path)}: missing final newline")


def is_part_artifact_path(relative: str) -> bool:
    parts = Path(relative).parts
    return len(parts) >= 3 and parts[0] == "parts" and parts[2] in PART_ARTIFACT_DIRS


def active_text_files() -> list[Path]:
    files: list[Path] = []
    for path in EXPERIENCE_ROOT.rglob("*"):
        if not path.is_file() or path.suffix not in ACTIVE_TEXT_SUFFIXES:
            continue
        relative = path.relative_to(EXPERIENCE_ROOT).as_posix()
        if relative.startswith("legacy/raw/"):
            continue
        if relative.startswith(ARTIFACT_PREFIXES):
            continue
        if is_part_artifact_path(relative):
            continue
        files.append(path)
    return files


def active_markdown_files_without_bridge() -> list[Path]:
    files: list[Path] = []
    for path in EXPERIENCE_ROOT.rglob("*.md"):
        if not path.is_file():
            continue
        relative = path.relative_to(EXPERIENCE_ROOT).as_posix()
        if relative.startswith("legacy/") or path == PROVENANCE_PATH:
            continue
        if is_part_artifact_path(relative):
            continue
        files.append(path)
    return files


def validate_root_surfaces(problems: list[str]) -> None:
    for name in ROOT_SURFACES:
        require_file(EXPERIENCE_ROOT / name, problems)
    require_file(ARTIFACT_MAP_PATH, problems)
    require_file(PROVENANCE_RECEIPTS_PATH, problems)
    for name in LEGACY_SURFACES:
        require_file(LEGACY_ROOT / name, problems)
    require_file(EXPERIENCE_ROOT / "docs" / "AGENTS.md", problems)
    require_file(EXPERIENCE_ROOT / "docs" / "README.md", problems)
    require_file(PARTS_ROOT / "AGENTS.md", problems)
    require_file(PARTS_ROOT / "README.md", problems)

    direction = (
        read(EXPERIENCE_ROOT / "DIRECTION.md")
        if (EXPERIENCE_ROOT / "DIRECTION.md").exists()
        else ""
    )
    parts = (
        read(EXPERIENCE_ROOT / "PARTS.md")
        if (EXPERIENCE_ROOT / "PARTS.md").exists()
        else ""
    )
    readme = (
        read(EXPERIENCE_ROOT / "README.md")
        if (EXPERIENCE_ROOT / "README.md").exists()
        else ""
    )
    for slug in PART_SLUGS:
        if slug not in direction:
            problems.append(
                f"mechanics/experience/DIRECTION.md: missing part slug {slug}"
            )
        if slug not in parts:
            problems.append(f"mechanics/experience/PARTS.md: missing part slug {slug}")
        if slug not in readme:
            problems.append(f"mechanics/experience/README.md: missing part slug {slug}")
    provenance = read(PROVENANCE_PATH) if PROVENANCE_PATH.exists() else ""
    for needle in (
        "legacy/INDEX.md",
        "legacy/DISTILLATION_LOG.md",
        "legacy/artifacts/README.md",
        "legacy/raw/README.md",
    ):
        if needle not in provenance:
            problems.append(
                f"mechanics/experience/PROVENANCE.md: missing archive route {needle}"
            )
    if "only active Experience surface" not in provenance:
        problems.append(
            "mechanics/experience/PROVENANCE.md: must declare itself the only active archive bridge"
        )
    if "PROVENANCE.md" not in readme and "PROVENANCE" not in readme:
        problems.append(
            "mechanics/experience/README.md: missing provenance bridge route"
        )


def validate_parts(selected: set[str] | None, problems: list[str]) -> None:
    slugs = [slug for slug in PART_SLUGS if selected is None or slug in selected]
    for slug in slugs:
        part_dir = PARTS_ROOT / slug
        if not part_dir.is_dir():
            problems.append(f"missing part directory: {rel(part_dir)}")
            continue
        for name in PART_SURFACES:
            require_file(part_dir / name, problems)
        readme_path = part_dir / "README.md"
        contract_path = part_dir / "CONTRACT.md"
        validation_path = part_dir / "VALIDATION.md"
        readme = read(readme_path) if readme_path.exists() else ""
        contract = read(contract_path) if contract_path.exists() else ""
        validation = read(validation_path) if validation_path.exists() else ""
        parts_agents = read(PARTS_AGENTS_PATH) if PARTS_AGENTS_PATH.exists() else ""
        if "## Legacy raw sources" in readme or "## Primary raw provenance" in readme:
            problems.append(
                f"{rel(readme_path)}: active part README carries archival source inventory"
            )
        if "## Must not claim" not in contract:
            problems.append(f"{rel(contract_path)}: missing explicit stop-line section")
        for phrase in PART_STOP_LINE_PHRASES[slug]:
            if not contains_phrase(contract, phrase):
                problems.append(
                    f"{rel(contract_path)}: missing part-specific stop-line phrase {phrase!r}"
                )
        if (
            f"validate_experience_distillation.py --part {slug}" not in validation
            and f"validate_experience_distillation.py --part {slug}" not in parts_agents
        ):
            problems.append(
                f"{rel(validation_path)}: missing targeted distillation command in validation route"
            )
        for phrase in VAGUE_VALIDATION_PHRASES:
            if contains_phrase(validation, phrase):
                problems.append(
                    f"{rel(validation_path)}: vague validation phrase {phrase!r}"
                )


def validate_raw_sources(problems: list[str]) -> None:
    raw_docs = sorted(RAW_ROOT.glob("EXPERIENCE_*.md"))
    if len(raw_docs) < 140:
        problems.append(
            f"{rel(RAW_ROOT)}: expected at least 140 raw Experience sources, found {len(raw_docs)}"
        )
    old_docs = sorted((EXPERIENCE_ROOT / "docs").glob("EXPERIENCE_*.md"))
    if old_docs:
        for path in old_docs[:10]:
            problems.append(
                f"active docs directory still contains raw Experience source: {rel(path)}"
            )
        if len(old_docs) > 10:
            problems.append(
                f"active docs directory has {len(old_docs) - 10} more raw Experience sources"
            )

    index_path = LEGACY_ROOT / "INDEX.md"
    index = read(index_path) if index_path.exists() else ""
    for raw in raw_docs:
        if raw.name not in index:
            problems.append(f"{rel(index_path)}: missing raw source {raw.name}")
    indexed = set(re.findall(r"`(EXPERIENCE_[A-Z0-9_]+\.md)`", index))
    existing = {path.name for path in raw_docs}
    stale = sorted(indexed - existing)
    for name in stale[:10]:
        problems.append(
            f"{rel(index_path)}: indexed raw source missing on disk: {name}"
        )
    if len(stale) > 10:
        problems.append(
            f"{rel(index_path)}: {len(stale) - 10} more stale raw index entries"
        )


def validate_raw_source_requirements(problems: list[str]) -> None:
    index_path = LEGACY_ROOT / "INDEX.md"
    index = read(index_path) if index_path.exists() else ""

    for name, tokens in RAW_DOC_TOKEN_REQUIREMENTS.items():
        path = RAW_ROOT / name
        require_file(path, problems)
        if not path.exists():
            continue
        text = read(path)
        for token in tokens:
            if token not in text:
                problems.append(f"{rel(path)}: missing raw provenance token {token!r}")
        for snippet in RAW_DOC_BANNED_SNIPPETS.get(name, ()):
            if snippet in text:
                problems.append(
                    f"{rel(path)}: stale raw provenance snippet still present {snippet!r}"
                )

    for path in PARTS_ROOT.rglob("*"):
        if not path.is_file() or path.suffix not in ACTIVE_TEXT_SUFFIXES:
            continue
        text = read(path)
        if path.suffix == ".py" and PART_VALIDATOR_RAW_READ_PATTERN in text:
            problems.append(
                f"{rel(path)}: part validator must not direct-read legacy/raw; use package provenance gate"
            )
        for name in RAW_REF_RE.findall(text):
            raw_path = RAW_ROOT / name
            if not raw_path.is_file():
                problems.append(
                    f"{rel(path)}: references missing raw provenance source {name}"
                )
            if name not in index:
                problems.append(
                    f"{rel(path)}: references raw source not listed in legacy/INDEX.md: {name}"
                )


def validate_artifact_map(problems: list[str]) -> None:
    if not ARTIFACT_MAP_PATH.is_file():
        problems.append(f"missing file: {rel(ARTIFACT_MAP_PATH)}")
        return

    data = load_artifact_map()
    if data.get("schema_version") != "aoa_experience_artifact_map_v1":
        problems.append(
            f"{rel(ARTIFACT_MAP_PATH)}: schema_version must be aoa_experience_artifact_map_v1"
        )
    if data.get("mechanic") != "experience":
        problems.append(f"{rel(ARTIFACT_MAP_PATH)}: mechanic must be experience")
    if tuple(data.get("parts", ())) != PART_SLUGS:
        problems.append(
            f"{rel(ARTIFACT_MAP_PATH)}: parts must match active Experience part order"
        )

    artifacts = data.get("artifacts")
    if not isinstance(artifacts, list) or not artifacts:
        problems.append(f"{rel(ARTIFACT_MAP_PATH)}: artifacts must be a non-empty list")
        artifacts = []

    seen_old: set[str] = set()
    seen_new: set[str] = set()
    listed_paths: set[str] = set()
    for index, item in enumerate(artifacts):
        if not isinstance(item, dict):
            problems.append(
                f"{rel(ARTIFACT_MAP_PATH)}: artifact {index} must be an object"
            )
            continue
        kind = str(item.get("kind", ""))
        part = str(item.get("part", ""))
        old_path = str(item.get("old_path", ""))
        new_path = str(item.get("path", ""))
        if kind not in {"schema", "example", "script", "test"}:
            problems.append(
                f"{rel(ARTIFACT_MAP_PATH)}: artifact {index} has invalid kind {kind!r}"
            )
        if part != "package" and part not in PART_SLUGS:
            problems.append(
                f"{rel(ARTIFACT_MAP_PATH)}: artifact {index} has invalid part {part!r}"
            )
        status = str(item.get("status", ""))
        if part == "package":
            if status not in PACKAGE_ARTIFACT_STATUSES:
                problems.append(
                    f"{rel(ARTIFACT_MAP_PATH)}: package artifact {index} has invalid status {status!r}"
                )
        elif status not in PART_ARTIFACT_STATUSES:
            problems.append(
                f"{rel(ARTIFACT_MAP_PATH)}: artifact {index} has invalid status {status!r}"
            )
        if old_path in seen_old:
            problems.append(f"{rel(ARTIFACT_MAP_PATH)}: duplicate old_path {old_path}")
        seen_old.add(old_path)
        if new_path in seen_new:
            problems.append(f"{rel(ARTIFACT_MAP_PATH)}: duplicate path {new_path}")
        seen_new.add(new_path)

        if part == "package":
            if new_path != old_path:
                problems.append(
                    f"{rel(ARTIFACT_MAP_PATH)}: package artifact path must remain stable: {new_path}"
                )
            if kind == "script" and not new_path.startswith(
                "mechanics/experience/scripts/"
            ):
                problems.append(
                    f"{rel(ARTIFACT_MAP_PATH)}: package script outside package scripts/: {new_path}"
                )
            if kind == "test" and not new_path.startswith(
                "mechanics/experience/tests/"
            ):
                problems.append(
                    f"{rel(ARTIFACT_MAP_PATH)}: package test outside package tests/: {new_path}"
                )
        else:
            expected_prefix = f"mechanics/experience/parts/{part}/"
            if not new_path.startswith(expected_prefix):
                problems.append(
                    f"{rel(ARTIFACT_MAP_PATH)}: {new_path} must live under {expected_prefix}"
                )
            new_parts = Path(new_path).parts
            if len(new_parts) < 5 or new_parts[4] not in PART_ARTIFACT_DIRS:
                problems.append(
                    f"{rel(ARTIFACT_MAP_PATH)}: {new_path} must live in a part artifact directory"
                )
            if kind == "schema" and "/schemas/" not in new_path:
                problems.append(
                    f"{rel(ARTIFACT_MAP_PATH)}: schema artifact outside schemas/: {new_path}"
                )
            if kind == "example" and "/examples/" not in new_path:
                problems.append(
                    f"{rel(ARTIFACT_MAP_PATH)}: example artifact outside examples/: {new_path}"
                )
            if kind == "script" and "/scripts/" not in new_path:
                problems.append(
                    f"{rel(ARTIFACT_MAP_PATH)}: script artifact outside scripts/: {new_path}"
                )
            if kind == "test" and "/tests/" not in new_path:
                problems.append(
                    f"{rel(ARTIFACT_MAP_PATH)}: test artifact outside tests/: {new_path}"
                )

        new_file = REPO_ROOT / new_path
        old_file = REPO_ROOT / old_path
        if not new_file.is_file():
            problems.append(
                f"{rel(ARTIFACT_MAP_PATH)}: mapped artifact missing: {new_path}"
            )
        else:
            listed_paths.add(new_path)
        if part != "package" and old_file.exists():
            problems.append(
                f"{rel(ARTIFACT_MAP_PATH)}: old flat artifact still exists: {old_path}"
            )

    for dirname in PART_ARTIFACT_DIRS:
        root_artifact_dir = EXPERIENCE_ROOT / dirname
        if not root_artifact_dir.exists():
            continue
        allowed = ROOT_ARTIFACT_ALLOWLIST.get(dirname, set())
        for path in root_artifact_dir.iterdir():
            if not path.is_file():
                continue
            if path.name not in allowed and path.name != "README.md":
                problems.append(
                    f"{rel(path)}: flat Experience artifact must move to a part-local home"
                )

    for part in PART_SLUGS:
        for dirname in PART_ARTIFACT_DIRS:
            part_dir = PARTS_ROOT / part / dirname
            if not part_dir.exists():
                continue
            for path in part_dir.iterdir():
                if not path.is_file() or path.name == "README.md":
                    continue
                path_ref = rel(path)
                if path_ref not in listed_paths:
                    problems.append(
                        f"{path_ref}: part artifact is not listed in artifact-map.json"
                    )


def validate_provenance_receipts(problems: list[str]) -> set[str]:
    if not PROVENANCE_RECEIPTS_PATH.is_file():
        problems.append(f"missing file: {rel(PROVENANCE_RECEIPTS_PATH)}")
        return set()

    try:
        data = load_provenance_receipts()
    except json.JSONDecodeError as exc:
        problems.append(f"{rel(PROVENANCE_RECEIPTS_PATH)}: invalid JSON: {exc}")
        return set()

    if data.get("schema_version") != "aoa_experience_provenance_receipts_v1":
        problems.append(
            f"{rel(PROVENANCE_RECEIPTS_PATH)}: schema_version must be aoa_experience_provenance_receipts_v1"
        )
    if data.get("mechanic") != "experience":
        problems.append(f"{rel(PROVENANCE_RECEIPTS_PATH)}: mechanic must be experience")
    if data.get("source_of_truth") != "mechanics/experience/PROVENANCE.md":
        problems.append(
            f"{rel(PROVENANCE_RECEIPTS_PATH)}: source_of_truth must point to PROVENANCE.md"
        )

    receipts = data.get("receipts")
    if not isinstance(receipts, list) or not receipts:
        problems.append(
            f"{rel(PROVENANCE_RECEIPTS_PATH)}: receipts must be a non-empty list"
        )
        return set()

    ids: set[str] = set()
    sources: set[str] = set()
    for index, item in enumerate(receipts):
        if not isinstance(item, dict):
            problems.append(
                f"{rel(PROVENANCE_RECEIPTS_PATH)}: receipt {index} must be an object"
            )
            continue

        receipt_id = str(item.get("id", ""))
        if not receipt_id:
            problems.append(
                f"{rel(PROVENANCE_RECEIPTS_PATH)}: receipt {index} missing id"
            )
        elif receipt_id in ids:
            problems.append(
                f"{rel(PROVENANCE_RECEIPTS_PATH)}: duplicate receipt id {receipt_id}"
            )
        elif not RECEIPT_ID_RE.match(receipt_id):
            problems.append(
                f"{rel(PROVENANCE_RECEIPTS_PATH)}: invalid receipt id {receipt_id!r}"
            )
        elif re.search(r"(?:^|[.-])wave\d+|(?:^|[.-])v\d", receipt_id, re.IGNORECASE):
            problems.append(
                f"{rel(PROVENANCE_RECEIPTS_PATH)}: receipt id carries release-contour naming {receipt_id!r}"
            )
        ids.add(receipt_id)

        for key in ("kind", "owner", "source_ref", "purpose"):
            if not isinstance(item.get(key), str) or not str(item.get(key)).strip():
                problems.append(
                    f"{rel(PROVENANCE_RECEIPTS_PATH)}: receipt {receipt_id or index} missing {key}"
                )

        source_ref = str(item.get("source_ref", ""))
        if source_ref in sources:
            problems.append(
                f"{rel(PROVENANCE_RECEIPTS_PATH)}: duplicate source_ref {source_ref}"
            )
        sources.add(source_ref)
        if source_ref.startswith("mechanics/") or source_ref.startswith("docs/"):
            source_path = source_ref.split("#", 1)[0]
            if not (REPO_ROOT / source_path).is_file():
                problems.append(
                    f"{rel(PROVENANCE_RECEIPTS_PATH)}: source_ref missing on disk: {source_ref}"
                )

        consumers = item.get("active_consumers")
        if not isinstance(consumers, list) or not consumers:
            problems.append(
                f"{rel(PROVENANCE_RECEIPTS_PATH)}: receipt {receipt_id or index} must list active_consumers"
            )
            consumers = []
        for consumer in consumers:
            if consumer not in PART_SLUGS:
                problems.append(
                    f"{rel(PROVENANCE_RECEIPTS_PATH)}: receipt {receipt_id or index} has invalid active_consumer {consumer!r}"
                )

        must_not_claim = item.get("must_not_claim")
        if not isinstance(must_not_claim, list) or not must_not_claim:
            problems.append(
                f"{rel(PROVENANCE_RECEIPTS_PATH)}: receipt {receipt_id or index} must list must_not_claim"
            )

    return ids


def validate_active_receipt_refs(receipt_ids: set[str], problems: list[str]) -> None:
    for path in PARTS_ROOT.rglob("*"):
        if not path.is_file() or path.suffix not in ACTIVE_TEXT_SUFFIXES:
            continue

        text = read(path)
        if ACTIVE_DIRECT_PROVENANCE_RE.search(text):
            problems.append(
                f"{rel(path)}: active part artifact carries direct provenance/source path instead of receipt id"
            )

        if path.suffix != ".json":
            continue

        try:
            payload = json.loads(text)
        except json.JSONDecodeError as exc:
            problems.append(
                f"{rel(path)}: invalid JSON while checking receipt refs: {exc}"
            )
            continue

        def visit(value: object, pointer: str) -> None:
            if isinstance(value, dict):
                for key, child in value.items():
                    child_pointer = f"{pointer}/{key}" if pointer else key
                    if key == "receipt_ref" or key.endswith("_receipt_ref"):
                        child_value = (
                            child.get("const")
                            if isinstance(child, dict) and isinstance(child.get("const"), str)
                            else child
                        )
                        if not isinstance(child_value, str) or child_value not in receipt_ids:
                            problems.append(
                                f"{rel(path)}:{child_pointer}: unknown receipt ref {child_value!r}"
                            )
                    if key.endswith("_receipt_refs"):
                        child_values = (
                            child.get("const")
                            if isinstance(child, dict) and isinstance(child.get("const"), list)
                            else child
                        )
                        if isinstance(child, dict) and "const" not in child:
                            pass
                        elif not isinstance(child_values, list):
                            problems.append(
                                f"{rel(path)}:{child_pointer}: receipt refs must be a list"
                            )
                        else:
                            for index, item in enumerate(child_values):
                                if not isinstance(item, str) or item not in receipt_ids:
                                    problems.append(
                                        f"{rel(path)}:{child_pointer}/{index}: unknown receipt ref {item!r}"
                                    )
                    visit(child, child_pointer)
            elif isinstance(value, list):
                for index, child in enumerate(value):
                    child_pointer = f"{pointer}/{index}" if pointer else str(index)
                    visit(child, child_pointer)

        visit(payload, "")


def validate_active_artifact_names(problems: list[str]) -> None:
    for path in PARTS_ROOT.rglob("*"):
        if not path.is_file():
            continue

        if ACTIVE_RELEASE_CONTOUR_FILENAME_RE.search(path.name):
            problems.append(
                f"{rel(path)}: active artifact filename carries release-contour identity"
            )

        if path.suffix == ".py":
            text = read(path)
            if ACTIVE_RELEASE_CONTOUR_PY_RE.search(text):
                problems.append(
                    f"{rel(path)}: active Python test/validator identity carries release-contour naming"
                )

        if path.suffix != ".json":
            continue

        try:
            payload = json.loads(read(path))
        except json.JSONDecodeError as exc:
            problems.append(
                f"{rel(path)}: invalid JSON while checking active names: {exc}"
            )
            continue

        def visit(value: object, pointer: str) -> None:
            if isinstance(value, dict):
                for key, child in value.items():
                    child_pointer = f"{pointer}/{key}" if pointer else key
                    if "wave" in key.lower():
                        problems.append(
                            f"{rel(path)}:{child_pointer}: active JSON key must use functional naming, not wave"
                        )
                    if (
                        key in ACTIVE_ARTIFACT_IDENTITY_KEYS
                        and isinstance(child, str)
                        and ACTIVE_RELEASE_CONTOUR_IDENTITY_RE.search(child)
                    ):
                        problems.append(
                            f"{rel(path)}:{child_pointer}: active identity carries release-contour value {child!r}"
                        )
                    if (
                        isinstance(child, str)
                        and ACTIVE_RELEASE_CONTOUR_VALUE_RE.search(child)
                        and not ACTIVE_RELEASE_CONTOUR_VALUE_ALLOW_RE.search(child)
                    ):
                        problems.append(
                            f"{rel(path)}:{child_pointer}: active JSON value carries wave contour {child!r}"
                        )
                    visit(child, child_pointer)
            elif isinstance(value, list):
                for index, child in enumerate(value):
                    child_pointer = f"{pointer}/{index}" if pointer else str(index)
                    if (
                        isinstance(child, str)
                        and ACTIVE_RELEASE_CONTOUR_VALUE_RE.search(child)
                        and not ACTIVE_RELEASE_CONTOUR_VALUE_ALLOW_RE.search(child)
                    ):
                        problems.append(
                            f"{rel(path)}:{child_pointer}: active JSON list value carries wave contour {child!r}"
                        )
                    visit(child, child_pointer)

        visit(payload, "")


def validate_no_stale_active_refs(problems: list[str]) -> None:
    for path in active_text_files():
        text = read(path)
        for needle in STALE_ACTIVE_REFS:
            if needle in text:
                problems.append(f"{rel(path)}: stale active Experience ref {needle!r}")
                break


def validate_active_docs_are_lean(problems: list[str]) -> None:
    for path in active_markdown_files_without_bridge():
        text = read(path)
        for pattern in ACTIVE_ARCHIVE_LOAD_PATTERNS:
            if pattern in text:
                problems.append(
                    f"{rel(path)}: active doc carries archive-load marker {pattern!r}"
                )
                break
        if ACTIVE_ARCHIVE_FILENAME_RE.search(text):
            problems.append(
                f"{rel(path)}: active doc names archived Experience source files"
            )
        for pattern in ACTIVE_ROUTE_POLLUTION_PATTERNS:
            if contains_phrase(text, pattern):
                problems.append(
                    f"{rel(path)}: active route carries route-pollution marker {pattern!r}"
                )


def validate_route_surfaces(problems: list[str]) -> None:
    roadmap_path = EXPERIENCE_ROOT / "ROADMAP.md"
    roadmap = read(roadmap_path) if roadmap_path.exists() else ""
    for pattern in STALE_ROADMAP_PATTERNS:
        if pattern in roadmap:
            problems.append(f"{rel(roadmap_path)}: stale roadmap route {pattern!r}")
    for phrase in ("parts/", "PROVENANCE.md", "owner-local adoption links"):
        if phrase not in roadmap:
            problems.append(
                f"{rel(roadmap_path)}: missing current route phrase {phrase!r}"
            )

    atlas = read(MECHANICS_ATLAS_PATH) if MECHANICS_ATLAS_PATH.exists() else ""
    for pattern in ACTIVE_ROUTE_POLLUTION_PATTERNS:
        if contains_phrase(atlas, pattern):
            problems.append(
                f"{rel(MECHANICS_ATLAS_PATH)}: Experience atlas carries route-pollution marker {pattern!r}"
            )


def validate_thematic_experience_route(problems: list[str]) -> None:
    if not THEMATIC_DISTRICTS_PATH.exists():
        problems.append(f"missing file: {rel(THEMATIC_DISTRICTS_PATH)}")
        return
    data = json.loads(read(THEMATIC_DISTRICTS_PATH))
    matches = [
        item
        for item in data.get("pattern_migrations", [])
        if isinstance(item, dict) and item.get("source_glob") == "docs/EXPERIENCE_*.md"
    ]
    if len(matches) != 1:
        problems.append(
            "docs/guardrails/thematic_districts.json: expected one docs/EXPERIENCE_*.md migration route"
        )
        return
    target = matches[0].get("target_dir")
    if target != "mechanics/experience/legacy/raw":
        problems.append(
            "docs/guardrails/thematic_districts.json: docs/EXPERIENCE_*.md must route to mechanics/experience/legacy/raw"
        )


def validate_registry(problems: list[str]) -> None:
    registry = load_registry()
    experience = next(
        (
            item
            for item in registry.get("mechanics", [])
            if isinstance(item, dict) and item.get("slug") == "experience"
        ),
        None,
    )
    if not isinstance(experience, dict):
        problems.append("mechanics/registry.json: missing experience entry")
        return
    if (
        experience.get("owner_request_doc_ref")
        != "mechanics/experience/OWNER_REQUESTS.md"
    ):
        problems.append(
            "mechanics/registry.json: experience owner_request_doc_ref must point to OWNER_REQUESTS.md"
        )
    canonical = experience.get("canonical_docs")
    if not isinstance(canonical, list) or not canonical:
        problems.append(
            "mechanics/registry.json: experience canonical_docs must be non-empty"
        )
        canonical = []
    for ref in canonical:
        ref_text = str(ref)
        if ref_text.startswith("mechanics/experience/legacy/"):
            problems.append(
                f"mechanics/registry.json: archive file listed as canonical active doc: {ref_text}"
            )
        if not (REPO_ROOT / ref_text).exists():
            problems.append(
                f"mechanics/registry.json: canonical doc missing: {ref_text}"
            )
    if "mechanics/experience/PROVENANCE.md" not in canonical:
        problems.append(
            "mechanics/registry.json: experience canonical_docs must include PROVENANCE.md bridge"
        )
    if "mechanics/experience/provenance-receipts.json" not in canonical:
        problems.append(
            "mechanics/registry.json: experience canonical_docs must include provenance-receipts.json"
        )
    for required_doc in (
        "mechanics/experience/ROADMAP.md",
        "mechanics/experience/LANDING_LOG.md",
    ):
        if required_doc not in canonical:
            problems.append(
                f"mechanics/registry.json: experience canonical_docs must include {required_doc}"
            )
    if (
        "mechanics/experience/scripts/validate_experience_distillation.py"
        not in experience.get("validation_refs", [])
    ):
        problems.append(
            "mechanics/registry.json: missing validate_experience_distillation.py validation ref"
        )
    must_not_claim = experience.get("must_not_claim", [])
    if not isinstance(must_not_claim, list):
        problems.append(
            "mechanics/registry.json: experience must_not_claim must be a list"
        )
        must_not_claim = []
    joined_claims = "\n".join(str(item) for item in must_not_claim)
    readme = (
        read(EXPERIENCE_ROOT / "README.md")
        if (EXPERIENCE_ROOT / "README.md").exists()
        else ""
    )
    for phrase in OWNER_STOP_LINE_PHRASES:
        if not contains_phrase(joined_claims, phrase):
            problems.append(
                f"mechanics/registry.json: experience must_not_claim missing {phrase!r}"
            )
        if not contains_phrase(readme, phrase):
            problems.append(
                f"mechanics/experience/README.md: missing owner stop-line phrase {phrase!r}"
            )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--part",
        choices=PART_SLUGS,
        action="append",
        help="Validate a specific Experience part.",
    )
    return parser.parse_args()


def validate(selected: set[str] | None = None) -> list[str]:
    problems: list[str] = []
    receipt_ids = validate_provenance_receipts(problems)
    validate_root_surfaces(problems)
    validate_parts(selected, problems)
    validate_raw_sources(problems)
    validate_raw_source_requirements(problems)
    validate_artifact_map(problems)
    validate_active_receipt_refs(receipt_ids, problems)
    validate_active_artifact_names(problems)
    validate_no_stale_active_refs(problems)
    validate_active_docs_are_lean(problems)
    validate_route_surfaces(problems)
    validate_thematic_experience_route(problems)
    validate_registry(problems)
    return problems


def main() -> int:
    args = parse_args()
    selected = set(args.part) if args.part else None
    problems = validate(selected)
    if problems:
        print("Experience distillation validation failed:")
        for problem in problems:
            print(f" - {problem}")
        return 1
    scope = ", ".join(sorted(selected)) if selected else "all parts"
    print(f"[ok] Experience distillation validated: {scope}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
