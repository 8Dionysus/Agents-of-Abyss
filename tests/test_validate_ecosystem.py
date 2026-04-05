from __future__ import annotations

import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


SCRIPTS_DIR = Path(__file__).resolve().parents[1] / "scripts"
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

import validate_ecosystem


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def copy_repo_text(repo_root: Path, relative_path: str) -> None:
    source = Path(__file__).resolve().parents[1] / relative_path
    destination = repo_root / relative_path
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(source.read_text(encoding="utf-8"), encoding="utf-8")


class ValidateQuestbookSurfaceTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = Path(tempfile.mkdtemp(prefix="aoa_center_questbook_"))
        self.repo_root = self.temp_dir / "Agents-of-Abyss"
        self.questbook_path = self.repo_root / "QUESTBOOK.md"
        self.questbook_model_path = self.repo_root / "docs" / "QUESTBOOK_MODEL.md"
        self.first_wave_path = self.repo_root / "docs" / "QUESTBOOK_FIRST_WAVE.md"
        self.quests_dir = self.repo_root / "quests"
        self.patches = (
            patch.object(validate_ecosystem, "REPO_ROOT", self.repo_root),
            patch.object(validate_ecosystem, "QUESTBOOK_PATH", self.questbook_path),
            patch.object(validate_ecosystem, "QUESTBOOK_MODEL_PATH", self.questbook_model_path),
            patch.object(validate_ecosystem, "QUESTBOOK_FIRST_WAVE_PATH", self.first_wave_path),
            patch.object(validate_ecosystem, "QUESTS_PATH", self.quests_dir),
            patch.object(
                validate_ecosystem,
                "RPG_ARCHITECTURE_RFC_PATH",
                self.repo_root / "docs" / "RPG_ARCHITECTURE_RFC.md",
            ),
            patch.object(
                validate_ecosystem,
                "RPG_CANONICAL_TERMINOLOGY_PATH",
                self.repo_root / "docs" / "RPG_CANONICAL_TERMINOLOGY.md",
            ),
            patch.object(
                validate_ecosystem,
                "RPG_BOUNDARY_MAP_PATH",
                self.repo_root / "docs" / "RPG_BOUNDARY_MAP.md",
            ),
            patch.object(
                validate_ecosystem,
                "DUAL_VOCABULARY_SCHEMA_PATH",
                self.repo_root / "schemas" / "dual_vocabulary_overlay.schema.json",
            ),
            patch.object(
                validate_ecosystem,
                "DUAL_VOCABULARY_EXAMPLE_PATH",
                self.repo_root / "examples" / "dual_vocabulary_overlay.example.json",
            ),
            patch.object(
                validate_ecosystem,
                "DUAL_VOCABULARY_GENERATED_PATH",
                self.repo_root / "generated" / "dual_vocabulary_overlay.json",
            ),
            patch.object(
                validate_ecosystem,
                "RPG_BRIDGE_WAVE_PATH",
                self.repo_root / "docs" / "RPG_BRIDGE_WAVE.md",
            ),
            patch.object(
                validate_ecosystem,
                "RPG_RUNTIME_PROJECTION_WAVE_PATH",
                self.repo_root / "docs" / "RPG_RUNTIME_PROJECTION_WAVE.md",
            ),
        )
        for patcher in self.patches:
            patcher.start()
            self.addCleanup(patcher.stop)
        self.addCleanup(shutil.rmtree, self.temp_dir)

    def write_valid_surface(self) -> None:
        write_text(
            self.questbook_path,
            "\n".join(
                (
                    "# QUESTBOOK.md — Agents-of-Abyss",
                    "",
                    "- `AOA-Q-0001`",
                    "- `AOA-Q-0002`",
                    "- `AOA-Q-0003`",
                )
            )
            + "\n",
        )
        write_text(self.questbook_model_path, "# QUESTBOOK_MODEL.md\n")
        write_text(
            self.first_wave_path,
            "It is a foundation pass, not a new numbered AoA wave.\n",
        )
        self.quests_dir.mkdir(parents=True, exist_ok=True)
        for quest_id in validate_ecosystem.REQUIRED_QUEST_IDS:
            write_text(
                self.quests_dir / f"{quest_id}.yaml",
                "\n".join(
                    (
                        "schema_version: work_quest_v1",
                        f"id: {quest_id}",
                        "repo: Agents-of-Abyss",
                        "public_safe: true",
                    )
                )
                + "\n",
            )

    def write_rpg_architecture_surface(self) -> None:
        write_text(
            self.repo_root / "docs" / "RPG_ARCHITECTURE_RFC.md",
            "The RPG layer MUST remain a reflection and orchestration layer.\n"
            "One universal power score MUST NOT become authoritative.\n",
        )
        write_text(
            self.repo_root / "docs" / "RPG_CANONICAL_TERMINOLOGY.md",
            "the machine vocabulary stays stable\n"
            "dual_vocabulary_overlay_v1\n",
        )
        write_text(
            self.repo_root / "docs" / "RPG_BOUNDARY_MAP.md",
            "The repo that already owns meaning keeps owning meaning.\n"
            "1. source meaning wins\n",
        )
        copy_repo_text(self.repo_root, "schemas/dual_vocabulary_overlay.schema.json")
        copy_repo_text(self.repo_root, "examples/dual_vocabulary_overlay.example.json")

    def write_rpg_bridge_wave_surface(self) -> None:
        write_text(
            self.repo_root / "docs" / "RPG_BRIDGE_WAVE.md",
            "What remained was the bridge that lets proof, composition, and navigation speak to one another without collapsing repo ownership.\n"
            "`aoa-routing` may orient. It does not own proof, party doctrine, or quest meaning.\n"
            "do not create a universal rank or power score here\n"
            "This wave is a bridge, not a throne.\n",
        )

    def write_rpg_runtime_projection_surface(self) -> None:
        write_text(
            self.repo_root / "docs" / "RPG_RUNTIME_PROJECTION_WAVE.md",
            "This document defines the first body-facing rollout for the AoA RPG reflection contour.\n"
            "It is the pass where the contour stops being only a federation of ideas and gains runtime-owned read models, generated transport collections, and a bounded projection seam.\n"
            "Let the body carry the contour.\n"
            "Do not let it rewrite the soul.\n",
        )
        copy_repo_text(self.repo_root, "generated/dual_vocabulary_overlay.json")

    def test_valid_extra_quest_file_is_allowed(self) -> None:
        self.write_valid_surface()
        write_text(
            self.quests_dir / "AOA-Q-0004.yaml",
            "\n".join(
                (
                    "schema_version: work_quest_v1",
                    "id: AOA-Q-0004",
                    "repo: Agents-of-Abyss",
                    "public_safe: true",
                )
            )
            + "\n",
        )
        write_text(
            self.questbook_path,
            self.questbook_path.read_text(encoding="utf-8") + "- `AOA-Q-0004`\n",
        )

        validate_ecosystem.validate_questbook_surface()

    def test_valid_second_wave_extra_quest_file_is_allowed(self) -> None:
        self.write_valid_surface()
        write_text(
            self.quests_dir / "AOA-Q-0005.yaml",
            "\n".join(
                (
                    "schema_version: work_quest_v1",
                    "id: AOA-Q-0005",
                    "repo: Agents-of-Abyss",
                    "state: triaged",
                    "public_safe: true",
                )
            )
            + "\n",
        )
        write_text(
            self.questbook_path,
            self.questbook_path.read_text(encoding="utf-8") + "- `AOA-Q-0005`\n",
        )

        validate_ecosystem.validate_questbook_surface()

    def test_valid_rpg_architecture_extra_quest_is_allowed(self) -> None:
        self.write_valid_surface()
        self.write_rpg_architecture_surface()
        write_text(
            self.quests_dir / "AOA-Q-0006.yaml",
            "\n".join(
                (
                    "schema_version: work_quest_v1",
                    "id: AOA-Q-0006",
                    "repo: Agents-of-Abyss",
                    "state: triaged",
                    "public_safe: true",
                )
            )
            + "\n",
        )
        write_text(
            self.questbook_path,
            self.questbook_path.read_text(encoding="utf-8") + "- `AOA-Q-0006`\n",
        )

        validate_ecosystem.validate_questbook_surface()

    def test_valid_rpg_bridge_wave_extra_quest_is_allowed(self) -> None:
        self.write_valid_surface()
        self.write_rpg_bridge_wave_surface()
        write_text(
            self.quests_dir / "AOA-Q-0007.yaml",
            "\n".join(
                (
                    "schema_version: work_quest_v1",
                    "id: AOA-Q-0007",
                    "repo: Agents-of-Abyss",
                    "state: triaged",
                    "public_safe: true",
                )
            )
            + "\n",
        )
        write_text(
            self.questbook_path,
            self.questbook_path.read_text(encoding="utf-8") + "- `AOA-Q-0007`\n",
        )

        validate_ecosystem.validate_questbook_surface()

    def test_valid_rpg_runtime_projection_extra_quest_is_allowed(self) -> None:
        self.write_valid_surface()
        self.write_rpg_architecture_surface()
        self.write_rpg_runtime_projection_surface()
        write_text(
            self.quests_dir / "AOA-Q-0008.yaml",
            "\n".join(
                (
                    "schema_version: work_quest_v1",
                    "id: AOA-Q-0008",
                    "repo: Agents-of-Abyss",
                    "state: triaged",
                    "public_safe: true",
                )
            )
            + "\n",
        )
        write_text(
            self.questbook_path,
            self.questbook_path.read_text(encoding="utf-8") + "- `AOA-Q-0008`\n",
        )

        validate_ecosystem.validate_questbook_surface()

    def test_rpg_bridge_wave_surface_missing_rule_fails(self) -> None:
        self.write_valid_surface()
        self.write_rpg_bridge_wave_surface()
        write_text(
            self.quests_dir / "AOA-Q-0007.yaml",
            "\n".join(
                (
                    "schema_version: work_quest_v1",
                    "id: AOA-Q-0007",
                    "repo: Agents-of-Abyss",
                    "state: triaged",
                    "public_safe: true",
                )
            )
            + "\n",
        )
        write_text(
            self.questbook_path,
            self.questbook_path.read_text(encoding="utf-8") + "- `AOA-Q-0007`\n",
        )
        write_text(
            self.repo_root / "docs" / "RPG_BRIDGE_WAVE.md",
            "What remained was the bridge that lets proof, composition, and navigation speak to one another without collapsing repo ownership.\n",
        )

        with self.assertRaisesRegex(
            validate_ecosystem.ValidationError,
            "routing non-authority explicit|anti-throne rule explicit",
        ):
            validate_ecosystem.validate_questbook_surface()

    def test_rpg_runtime_projection_surface_missing_generated_twin_fails(self) -> None:
        self.write_valid_surface()
        self.write_rpg_runtime_projection_surface()
        write_text(
            self.quests_dir / "AOA-Q-0008.yaml",
            "\n".join(
                (
                    "schema_version: work_quest_v1",
                    "id: AOA-Q-0008",
                    "repo: Agents-of-Abyss",
                    "state: triaged",
                    "public_safe: true",
                )
            )
            + "\n",
        )
        write_text(
            self.questbook_path,
            self.questbook_path.read_text(encoding="utf-8") + "- `AOA-Q-0008`\n",
        )
        (self.repo_root / "generated" / "dual_vocabulary_overlay.json").unlink()

        with self.assertRaisesRegex(
            validate_ecosystem.ValidationError,
            "missing required file: generated/dual_vocabulary_overlay.json",
        ):
            validate_ecosystem.validate_questbook_surface()

    def test_rpg_runtime_projection_surface_rejects_missing_overlay_id(self) -> None:
        self.write_valid_surface()
        self.write_rpg_architecture_surface()
        self.write_rpg_runtime_projection_surface()
        write_text(
            self.quests_dir / "AOA-Q-0008.yaml",
            "\n".join(
                (
                    "schema_version: work_quest_v1",
                    "id: AOA-Q-0008",
                    "repo: Agents-of-Abyss",
                    "state: triaged",
                    "public_safe: true",
                )
            )
            + "\n",
        )
        write_text(
            self.questbook_path,
            self.questbook_path.read_text(encoding="utf-8") + "- `AOA-Q-0008`\n",
        )
        write_text(
            self.repo_root / "generated" / "dual_vocabulary_overlay.json",
            json.dumps(
                {
                    key: value
                    for key, value in json.loads(
                        (self.repo_root / "generated" / "dual_vocabulary_overlay.json").read_text(
                            encoding="utf-8"
                        )
                    ).items()
                    if key != "overlay_id"
                },
                indent=2,
            )
            + "\n",
        )

        with self.assertRaisesRegex(
            validate_ecosystem.ValidationError,
            "missing required keys: overlay_id",
        ):
            validate_ecosystem.validate_questbook_surface()

    def test_rpg_runtime_projection_surface_rejects_duplicate_canonical_key(self) -> None:
        self.write_valid_surface()
        self.write_rpg_architecture_surface()
        self.write_rpg_runtime_projection_surface()
        write_text(
            self.quests_dir / "AOA-Q-0008.yaml",
            "\n".join(
                (
                    "schema_version: work_quest_v1",
                    "id: AOA-Q-0008",
                    "repo: Agents-of-Abyss",
                    "state: triaged",
                    "public_safe: true",
                )
            )
            + "\n",
        )
        write_text(
            self.questbook_path,
            self.questbook_path.read_text(encoding="utf-8") + "- `AOA-Q-0008`\n",
        )

        generated_path = self.repo_root / "generated" / "dual_vocabulary_overlay.json"
        payload = json.loads(generated_path.read_text(encoding="utf-8"))
        payload["entries"][0]["canonical_key"] = payload["entries"][1]["canonical_key"]
        generated_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")

        with self.assertRaisesRegex(
            validate_ecosystem.ValidationError,
            "must not duplicate canonical_key values",
        ):
            validate_ecosystem.validate_questbook_surface()

    def test_missing_required_foundation_quest_fails(self) -> None:
        self.write_valid_surface()
        (self.quests_dir / "AOA-Q-0003.yaml").unlink()

        with self.assertRaisesRegex(
            validate_ecosystem.ValidationError,
            "missing: AOA-Q-0003",
        ):
            validate_ecosystem.validate_questbook_surface()

    def test_invalid_extra_quest_file_fails(self) -> None:
        self.write_valid_surface()
        write_text(
            self.quests_dir / "AOA-Q-0004.yaml",
            "\n".join(
                (
                    "schema_version: work_quest_v1",
                    "id: AOA-Q-0004",
                    "repo: aoa-routing",
                    "public_safe: true",
                )
            )
            + "\n",
        )

        with self.assertRaisesRegex(
            validate_ecosystem.ValidationError,
            "AOA-Q-0004.yaml must target repo 'Agents-of-Abyss'",
        ):
            validate_ecosystem.validate_questbook_surface()

    def test_closed_extra_quest_must_not_stay_listed(self) -> None:
        self.write_valid_surface()
        write_text(
            self.quests_dir / "AOA-Q-0004.yaml",
            "\n".join(
                (
                    "schema_version: work_quest_v1",
                    "id: AOA-Q-0004",
                    "repo: Agents-of-Abyss",
                    "state: done",
                    "public_safe: true",
                )
            )
            + "\n",
        )
        write_text(
            self.questbook_path,
            self.questbook_path.read_text(encoding="utf-8") + "- `AOA-Q-0004`\n",
        )

        with self.assertRaisesRegex(
            validate_ecosystem.ValidationError,
            "QUESTBOOK.md must not list closed quest id 'AOA-Q-0004'",
        ):
            validate_ecosystem.validate_questbook_surface()

    def test_rpg_architecture_quest_requires_rfc_docs(self) -> None:
        self.write_valid_surface()
        write_text(
            self.quests_dir / "AOA-Q-0006.yaml",
            "\n".join(
                (
                    "schema_version: work_quest_v1",
                    "id: AOA-Q-0006",
                    "repo: Agents-of-Abyss",
                    "state: triaged",
                    "public_safe: true",
                )
            )
            + "\n",
        )
        write_text(
            self.questbook_path,
            self.questbook_path.read_text(encoding="utf-8") + "- `AOA-Q-0006`\n",
        )

        with self.assertRaisesRegex(
            validate_ecosystem.ValidationError,
            "missing required file: docs/RPG_ARCHITECTURE_RFC.md",
        ):
            validate_ecosystem.validate_questbook_surface()


class ValidateRegistryTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = Path(tempfile.mkdtemp(prefix="aoa_center_registry_"))
        self.repo_root = self.temp_dir / "Agents-of-Abyss"
        self.registry_path = self.repo_root / "generated" / "ecosystem_registry.min.json"
        self.patches = (
            patch.object(validate_ecosystem, "REPO_ROOT", self.repo_root),
            patch.object(validate_ecosystem, "REGISTRY_PATH", self.registry_path),
        )
        for patcher in self.patches:
            patcher.start()
            self.addCleanup(patcher.stop)
        self.addCleanup(shutil.rmtree, self.temp_dir)

    def write_valid_registry(self) -> None:
        copy_repo_text(self.repo_root, "generated/ecosystem_registry.min.json")

    def read_registry(self) -> dict[str, object]:
        return json.loads(self.registry_path.read_text(encoding="utf-8"))

    def write_registry(self, payload: dict[str, object]) -> None:
        write_text(self.registry_path, json.dumps(payload, indent=2) + "\n")

    def test_valid_documented_v1_registry_passes(self) -> None:
        self.write_valid_registry()

        validate_ecosystem.validate_registry()

    def test_missing_documented_v1_repo_fails(self) -> None:
        self.write_valid_registry()
        payload = self.read_registry()
        payload["repos"] = [
            repo
            for repo in payload["repos"]
            if isinstance(repo, dict) and repo.get("name") != "aoa-kag"
        ]
        self.write_registry(payload)

        with self.assertRaisesRegex(
            validate_ecosystem.ValidationError,
            "missing documented v1 repos: aoa-kag",
        ):
            validate_ecosystem.validate_registry()

    def test_wrong_role_for_documented_repo_fails(self) -> None:
        self.write_valid_registry()
        payload = self.read_registry()
        for repo in payload["repos"]:
            if isinstance(repo, dict) and repo.get("name") == "aoa-agents":
                repo["role"] = "persona-layer"
                break
        self.write_registry(payload)

        with self.assertRaisesRegex(
            validate_ecosystem.ValidationError,
            r"role for 'aoa-agents' must equal 'agent-layer'",
        ):
            validate_ecosystem.validate_registry()

    def test_wrong_kind_for_documented_repo_fails(self) -> None:
        self.write_valid_registry()
        payload = self.read_registry()
        for repo in payload["repos"]:
            if isinstance(repo, dict) and repo.get("name") == "abyss-stack":
                repo["kind"] = "derived"
                break
        self.write_registry(payload)

        with self.assertRaisesRegex(
            validate_ecosystem.ValidationError,
            r"kind for 'abyss-stack' must equal 'related'",
        ):
            validate_ecosystem.validate_registry()

    def test_supporting_consumer_surface_is_out_of_scope_for_compact_v1(self) -> None:
        self.write_valid_registry()
        payload = self.read_registry()
        payload["repos"].append(
            {
                "name": "aoa-sdk",
                "role": "consumer-surface",
                "status": "active",
                "shared_maturity": "seed",
                "kind": "related",
            }
        )
        self.write_registry(payload)

        with self.assertRaisesRegex(
            validate_ecosystem.ValidationError,
            "outside compact v1 scope: aoa-sdk",
        ):
            validate_ecosystem.validate_registry()


if __name__ == "__main__":
    unittest.main()
