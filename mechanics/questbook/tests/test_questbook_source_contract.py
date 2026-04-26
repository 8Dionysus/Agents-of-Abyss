from __future__ import annotations

import importlib.util
import subprocess
import sys
from pathlib import Path


def _repo_root() -> Path:
    for candidate in Path(__file__).resolve().parents:
        if (candidate / "mechanics" / "registry.json").is_file():
            return candidate
    raise RuntimeError("repo root not found")


ROOT = _repo_root()
VALIDATOR = ROOT / "mechanics" / "questbook" / "scripts" / "validate_questbook_source_contract.py"


def load_validator():
    scripts_dir = str(VALIDATOR.parent)
    if scripts_dir not in sys.path:
        sys.path.insert(0, scripts_dir)
    spec = importlib.util.spec_from_file_location("validate_questbook_source_contract", VALIDATOR)
    assert spec is not None
    assert spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_validator_accepts_current_board() -> None:
    result = subprocess.run(
        [sys.executable, "mechanics/questbook/scripts/validate_questbook_source_contract.py"],
        cwd=ROOT,
        check=False,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )

    assert result.returncode == 0, result.stdout


def test_marked_markdown_requires_reviewability_sections() -> None:
    module = load_validator()
    problems: list[str] = []
    stats = {"yaml": 0, "contract_markdown": 0}
    path = ROOT / "quests" / "agon" / "ready" / "AOA-Q-AGON-9999-example.md"
    text = """# AOA-Q-AGON-9999: Example

source_contract: quest_markdown_contract_v1

## Quest

Example quest.
"""

    module.validate_markdown_contract(path, "agon", "ready", text, problems, stats)

    assert stats["contract_markdown"] == 1
    assert any("## Owner Route" in problem for problem in problems)
    assert any("## Acceptance Evidence" in problem for problem in problems)


def test_unmarked_markdown_is_rejected() -> None:
    module = load_validator()
    path = ROOT / "quests" / "agon" / "ready" / "AOA-Q-AGON-9999-example.md"
    text = "# AOA-Q-AGON-9999: Example\n\nA thin legacy-style quest.\n"

    problems: list[str] = []
    stats = {"yaml": 0, "contract_markdown": 0}
    module.validate_markdown_contract(path, "agon", "ready", text, problems, stats)

    assert stats["contract_markdown"] == 0
    assert any("source_contract: quest_markdown_contract_v1" in problem for problem in problems)


def test_marked_markdown_rejects_empty_contract_sections() -> None:
    module = load_validator()
    problems: list[str] = []
    stats = {"yaml": 0, "contract_markdown": 0}
    path = ROOT / "quests" / "agon" / "ready" / "AOA-Q-AGON-9999-example.md"
    text = """# AOA-Q-AGON-9999: Example

source_contract: quest_markdown_contract_v1

## Quest

Example quest.

## Owner Route

## Next Action

Lane/state defaults: [agon ready defaults](../README.md#ready-defaults).

## Acceptance Evidence

Lane/state defaults: [agon ready defaults](../README.md#ready-defaults).

## Stop-lines

Lane/state defaults: [agon ready defaults](../README.md#ready-defaults).
"""

    module.validate_markdown_contract(path, "agon", "ready", text, problems, stats)

    assert any("## Owner Route" in problem and "must not be empty" in problem for problem in problems)


def test_yaml_contract_requires_public_evidence() -> None:
    module = load_validator()
    path = ROOT / "quests" / "center" / "triaged" / "AOA-Q-9999.yaml"
    payload = {
        "schema_version": "work_quest_v1",
        "id": "AOA-Q-9999",
        "title": "Example",
        "repo": "Agents-of-Abyss",
        "lane": "center",
        "owner_surface": "center/example",
        "kind": "seam",
        "state": "triaged",
        "band": "near",
        "difficulty": "d1_patch",
        "risk": "r1_repo_local",
        "control_mode": "human_codex_copilot",
        "delegate_tier": "planner",
        "evidence": [],
        "public_safe": True,
    }
    problems: list[str] = []

    module.validate_yaml_contract(path, "center", "triaged", payload, problems)

    assert any("evidence" in problem for problem in problems)
