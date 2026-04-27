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
        self.questbook_model_path = self.repo_root / "mechanics" / "questbook" / "parts" / "model-spine" / "README.md"
        self.first_wave_path = self.repo_root / "mechanics" / "questbook" / "legacy" / "raw" / "QUESTBOOK_FIRST_WAVE.md"
        self.quests_dir = self.repo_root / "quests"
        self.patches = (
            patch.object(validate_ecosystem, "REPO_ROOT", self.repo_root),
            patch.object(validate_ecosystem, "QUESTBOOK_PATH", self.questbook_path),
            patch.object(validate_ecosystem, "QUESTBOOK_MODEL_PATH", self.questbook_model_path),
            patch.object(validate_ecosystem, "QUESTBOOK_FIRST_WAVE_PATH", self.first_wave_path),
            patch.object(validate_ecosystem, "QUESTS_PATH", self.quests_dir),
            patch.object(
                validate_ecosystem,
                "RPG_SOURCE_BOUNDARY_PATH",
                self.repo_root / "mechanics" / "rpg" / "parts" / "source-boundary" / "README.md",
            ),
            patch.object(
                validate_ecosystem,
                "RPG_CANONICAL_TERMINOLOGY_PATH",
                self.repo_root / "mechanics" / "rpg" / "parts" / "vocabulary-overlay" / "TERMINOLOGY.md",
            ),
            patch.object(
                validate_ecosystem,
                "DUAL_VOCABULARY_SCHEMA_PATH",
                self.repo_root / "mechanics" / "rpg" / "parts" / "vocabulary-overlay" / "schemas" / "dual_vocabulary_overlay.schema.json",
            ),
            patch.object(
                validate_ecosystem,
                "DUAL_VOCABULARY_EXAMPLE_PATH",
                self.repo_root / "mechanics" / "rpg" / "parts" / "vocabulary-overlay" / "examples" / "dual_vocabulary_overlay.example.json",
            ),
            patch.object(
                validate_ecosystem,
                "DUAL_VOCABULARY_GENERATED_PATH",
                self.repo_root / "mechanics" / "rpg" / "parts" / "vocabulary-overlay" / "generated" / "dual_vocabulary_overlay.json",
            ),
            patch.object(
                validate_ecosystem,
                "RPG_QUEST_CAMPAIGN_PATH",
                self.repo_root / "mechanics" / "rpg" / "parts" / "quest-campaign" / "README.md",
            ),
            patch.object(
                validate_ecosystem,
                "RPG_RUNTIME_PROJECTION_PATH",
                self.repo_root / "mechanics" / "rpg" / "parts" / "runtime-projection" / "README.md",
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
        required_states = {
            "AOA-Q-0001": "done",
            "AOA-Q-0002": "done",
            "AOA-Q-0003": "triaged",
        }
        for quest_id, state in required_states.items():
            write_text(
                self.quests_dir / "center" / state / f"{quest_id}.yaml",
                "\n".join(
                    (
                        "schema_version: work_quest_v1",
                        f"id: {quest_id}",
                        "repo: Agents-of-Abyss",
                        "lane: center",
                        f"state: {state}",
                        "public_safe: true",
                    )
                )
                + "\n",
            )

    def write_rpg_architecture_surface(self) -> None:
        write_text(
            self.repo_root / "mechanics" / "rpg" / "parts" / "source-boundary" / "README.md",
            "RPG reflects existing AoA surfaces, but source owners keep meaning.\n"
            "universal power score\n"
            "The repository that owns the source object keeps the meaning.\n"
            "1. source meaning wins\n",
        )
        write_text(
            self.repo_root / "mechanics" / "rpg" / "parts" / "vocabulary-overlay" / "TERMINOLOGY.md",
            "the machine vocabulary stays stable\n"
            "dual_vocabulary_overlay_v1\n",
        )
        copy_repo_text(self.repo_root, "mechanics/rpg/parts/vocabulary-overlay/schemas/dual_vocabulary_overlay.schema.json")
        copy_repo_text(self.repo_root, "mechanics/rpg/parts/vocabulary-overlay/examples/dual_vocabulary_overlay.example.json")

    def write_rpg_bridge_wave_surface(self) -> None:
        write_text(
            self.repo_root / "mechanics" / "rpg" / "parts" / "quest-campaign" / "README.md",
            "## Use When\n"
            "It makes long work playable and memorable without taking quest objects from Questbook.\n"
            "routing help is useful, but proof and source meaning remain outside this part\n"
            "## Do Not Use When\n"
            "a label would imply quest closure, proof completion, or a universal rank\n",
        )

    def write_rpg_runtime_projection_surface(self) -> None:
        write_text(
            self.repo_root / "mechanics" / "rpg" / "parts" / "runtime-projection" / "README.md",
            "It names what a runtime or frontend projection would need.\n"
            "read models, transport bundles, or session-state hints need a source-boundary check\n"
            "the task would create live runtime state from center docs\n"
            "projection would rewrite source meaning\n",
        )
        copy_repo_text(self.repo_root, "mechanics/rpg/parts/vocabulary-overlay/generated/dual_vocabulary_overlay.json")

    def test_valid_extra_quest_file_is_allowed(self) -> None:
        self.write_valid_surface()
        write_text(
            self.quests_dir / "center" / "triaged" / "AOA-Q-0004.yaml",
            "\n".join(
                (
                    "schema_version: work_quest_v1",
                    "id: AOA-Q-0004",
                    "repo: Agents-of-Abyss",
                    "lane: center",
                    "state: triaged",
                    "band: frontier",
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

    def test_questbook_rejects_band_section_mismatch(self) -> None:
        self.write_valid_surface()
        write_text(
            self.quests_dir / "center" / "triaged" / "AOA-Q-0004.yaml",
            "\n".join(
                (
                    "schema_version: work_quest_v1",
                    "id: AOA-Q-0004",
                    "repo: Agents-of-Abyss",
                    "lane: center",
                    "state: triaged",
                    "band: frontier",
                    "public_safe: true",
                )
            )
            + "\n",
        )
        write_text(
            self.questbook_path,
            "\n".join(
                (
                    "# QUESTBOOK.md — Agents-of-Abyss",
                    "",
                    "## Frontier",
                    "",
                    "- `AOA-Q-0001`",
                    "- `AOA-Q-0002`",
                    "",
                    "## Near",
                    "",
                    "- `AOA-Q-0003`",
                    "- `AOA-Q-0004`",
                )
            )
            + "\n",
        )

        with self.assertRaisesRegex(
            validate_ecosystem.ValidationError,
            "QUESTBOOK.md must list quest id 'AOA-Q-0004' under the section for band 'frontier', not 'near'",
        ):
            validate_ecosystem.validate_questbook_surface()

    def test_questbook_rejects_band_listing_only_under_unmapped_section(self) -> None:
        self.write_valid_surface()
        write_text(
            self.quests_dir / "center" / "triaged" / "AOA-Q-0004.yaml",
            "\n".join(
                (
                    "schema_version: work_quest_v1",
                    "id: AOA-Q-0004",
                    "repo: Agents-of-Abyss",
                    "lane: center",
                    "state: triaged",
                    "band: frontier",
                    "public_safe: true",
                )
            )
            + "\n",
        )
        write_text(
            self.questbook_path,
            "\n".join(
                (
                    "# QUESTBOOK.md — Agents-of-Abyss",
                    "",
                    "## Frontier",
                    "",
                    "- `AOA-Q-0001`",
                    "- `AOA-Q-0002`",
                    "",
                    "## Near",
                    "",
                    "- `AOA-Q-0003`",
                    "",
                    "## Blocked / reanchor",
                    "",
                    "- `AOA-Q-0004`",
                )
            )
            + "\n",
        )

        with self.assertRaisesRegex(
            validate_ecosystem.ValidationError,
            "QUESTBOOK.md must list quest id 'AOA-Q-0004' under the section for band 'frontier', not only under an unmapped section",
        ):
            validate_ecosystem.validate_questbook_surface()

    def test_questbook_rejects_non_dash_bullets_under_unmapped_section(self) -> None:
        for bullet in ("*", "+"):
            with self.subTest(bullet=bullet):
                self.write_valid_surface()
                write_text(
                    self.quests_dir / "center" / "triaged" / "AOA-Q-0004.yaml",
                    "\n".join(
                        (
                            "schema_version: work_quest_v1",
                            "id: AOA-Q-0004",
                            "repo: Agents-of-Abyss",
                            "lane: center",
                            "state: triaged",
                            "band: frontier",
                            "public_safe: true",
                        )
                    )
                    + "\n",
                )
                write_text(
                    self.questbook_path,
                    "\n".join(
                        (
                            "# QUESTBOOK.md — Agents-of-Abyss",
                            "",
                            "## Frontier",
                            "",
                            "- `AOA-Q-0001`",
                            "- `AOA-Q-0002`",
                            "",
                            "## Near",
                            "",
                            "- `AOA-Q-0003`",
                            "",
                            "## Blocked / reanchor",
                            "",
                            f"{bullet} `AOA-Q-0004`",
                        )
                    )
                    + "\n",
                )

                with self.assertRaisesRegex(
                    validate_ecosystem.ValidationError,
                    "QUESTBOOK.md must list quest id 'AOA-Q-0004' under the section for band 'frontier', not only under an unmapped section",
                ):
                    validate_ecosystem.validate_questbook_surface()

    def test_valid_second_wave_extra_quest_file_is_allowed(self) -> None:
        self.write_valid_surface()
        write_text(
            self.quests_dir / "center" / "triaged" / "AOA-Q-0005.yaml",
            "\n".join(
                (
                    "schema_version: work_quest_v1",
                    "id: AOA-Q-0005",
                    "repo: Agents-of-Abyss",
                    "lane: center",
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
            self.quests_dir / "center" / "triaged" / "AOA-Q-0006.yaml",
            "\n".join(
                (
                    "schema_version: work_quest_v1",
                    "id: AOA-Q-0006",
                    "repo: Agents-of-Abyss",
                    "lane: center",
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
            self.quests_dir / "center" / "triaged" / "AOA-Q-0007.yaml",
            "\n".join(
                (
                    "schema_version: work_quest_v1",
                    "id: AOA-Q-0007",
                    "repo: Agents-of-Abyss",
                    "lane: center",
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
            self.quests_dir / "center" / "triaged" / "AOA-Q-0008.yaml",
            "\n".join(
                (
                    "schema_version: work_quest_v1",
                    "id: AOA-Q-0008",
                    "repo: Agents-of-Abyss",
                    "lane: center",
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
            self.quests_dir / "center" / "triaged" / "AOA-Q-0007.yaml",
            "\n".join(
                (
                    "schema_version: work_quest_v1",
                    "id: AOA-Q-0007",
                    "repo: Agents-of-Abyss",
                    "lane: center",
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
            self.repo_root / "mechanics" / "rpg" / "parts" / "quest-campaign" / "README.md",
            "## Use When\n"
            "It makes long work playable and memorable without taking quest objects from Questbook.\n"
            "## Do Not Use When\n",
        )

        with self.assertRaisesRegex(
            validate_ecosystem.ValidationError,
            "routing non-authority explicit|anti-power-score bridge rule explicit",
        ):
            validate_ecosystem.validate_questbook_surface()

    def test_rpg_runtime_projection_surface_missing_generated_twin_fails(self) -> None:
        self.write_valid_surface()
        self.write_rpg_runtime_projection_surface()
        write_text(
            self.quests_dir / "center" / "triaged" / "AOA-Q-0008.yaml",
            "\n".join(
                (
                    "schema_version: work_quest_v1",
                    "id: AOA-Q-0008",
                    "repo: Agents-of-Abyss",
                    "lane: center",
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
        (self.repo_root / "mechanics" / "rpg" / "parts" / "vocabulary-overlay" / "generated" / "dual_vocabulary_overlay.json").unlink()

        with self.assertRaisesRegex(
            validate_ecosystem.ValidationError,
            "missing required file: mechanics/rpg/parts/vocabulary-overlay/generated/dual_vocabulary_overlay.json",
        ):
            validate_ecosystem.validate_questbook_surface()

    def test_rpg_runtime_projection_surface_rejects_missing_overlay_id(self) -> None:
        self.write_valid_surface()
        self.write_rpg_architecture_surface()
        self.write_rpg_runtime_projection_surface()
        write_text(
            self.quests_dir / "center" / "triaged" / "AOA-Q-0008.yaml",
            "\n".join(
                (
                    "schema_version: work_quest_v1",
                    "id: AOA-Q-0008",
                    "repo: Agents-of-Abyss",
                    "lane: center",
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
            self.repo_root / "mechanics" / "rpg" / "parts" / "vocabulary-overlay" / "generated" / "dual_vocabulary_overlay.json",
            json.dumps(
                {
                    key: value
                    for key, value in json.loads(
                        (self.repo_root / "mechanics" / "rpg" / "parts" / "vocabulary-overlay" / "generated" / "dual_vocabulary_overlay.json").read_text(
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
            self.quests_dir / "center" / "triaged" / "AOA-Q-0008.yaml",
            "\n".join(
                (
                    "schema_version: work_quest_v1",
                    "id: AOA-Q-0008",
                    "repo: Agents-of-Abyss",
                    "lane: center",
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

        generated_path = self.repo_root / "mechanics" / "rpg" / "parts" / "vocabulary-overlay" / "generated" / "dual_vocabulary_overlay.json"
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
        (self.quests_dir / "center" / "triaged" / "AOA-Q-0003.yaml").unlink()

        with self.assertRaisesRegex(
            validate_ecosystem.ValidationError,
            "missing: AOA-Q-0003",
        ):
            validate_ecosystem.validate_questbook_surface()

    def test_invalid_extra_quest_file_fails(self) -> None:
        self.write_valid_surface()
        write_text(
            self.quests_dir / "center" / "triaged" / "AOA-Q-0004.yaml",
            "\n".join(
                (
                    "schema_version: work_quest_v1",
                    "id: AOA-Q-0004",
                    "repo: aoa-routing",
                    "state: triaged",
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
            self.quests_dir / "center" / "done" / "AOA-Q-0004.yaml",
            "\n".join(
                (
                    "schema_version: work_quest_v1",
                    "id: AOA-Q-0004",
                    "repo: Agents-of-Abyss",
                    "lane: center",
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
            self.quests_dir / "center" / "triaged" / "AOA-Q-0006.yaml",
            "\n".join(
                (
                    "schema_version: work_quest_v1",
                    "id: AOA-Q-0006",
                    "repo: Agents-of-Abyss",
                    "lane: center",
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
            "missing required file: mechanics/rpg/parts/source-boundary/README.md",
        ):
            validate_ecosystem.validate_questbook_surface()


class ValidateRegistryTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = Path(tempfile.mkdtemp(prefix="aoa_center_registry_"))
        self.repo_root = self.temp_dir / "Agents-of-Abyss"
        self.registry_path = self.repo_root / "generated" / "ecosystem_registry.min.json"
        self.supporting_inventory_path = (
            self.repo_root / "generated" / "federation_supporting_inventory.min.json"
        )
        self.patches = (
            patch.object(validate_ecosystem, "REPO_ROOT", self.repo_root),
            patch.object(validate_ecosystem, "REGISTRY_PATH", self.registry_path),
            patch.object(
                validate_ecosystem,
                "SUPPORTING_INVENTORY_PATH",
                self.supporting_inventory_path,
            ),
        )
        for patcher in self.patches:
            patcher.start()
            self.addCleanup(patcher.stop)
        self.addCleanup(shutil.rmtree, self.temp_dir)

    def write_valid_registry(self) -> None:
        copy_repo_text(self.repo_root, "generated/ecosystem_registry.min.json")
        copy_repo_text(
            self.repo_root,
            "generated/federation_supporting_inventory.min.json",
        )

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
            if isinstance(repo, dict) and repo.get("name") != "aoa-stats"
        ]
        self.write_registry(payload)

        with self.assertRaisesRegex(
            validate_ecosystem.ValidationError,
            "missing documented v1 repos: aoa-stats",
        ):
            validate_ecosystem.validate_registry()

    def test_wrong_role_for_documented_repo_fails(self) -> None:
        self.write_valid_registry()
        payload = self.read_registry()
        for repo in payload["repos"]:
            if isinstance(repo, dict) and repo.get("name") == "aoa-stats":
                repo["role"] = "stats-layer"
                break
        self.write_registry(payload)

        with self.assertRaisesRegex(
            validate_ecosystem.ValidationError,
            r"role for 'aoa-stats' must equal 'derived-observability-layer'",
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


class ValidateSupportingInventoryTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = Path(tempfile.mkdtemp(prefix="aoa_supporting_inventory_"))
        self.repo_root = self.temp_dir / "Agents-of-Abyss"
        self.supporting_inventory_path = (
            self.repo_root / "generated" / "federation_supporting_inventory.min.json"
        )
        self.patches = (
            patch.object(validate_ecosystem, "REPO_ROOT", self.repo_root),
            patch.object(
                validate_ecosystem,
                "SUPPORTING_INVENTORY_PATH",
                self.supporting_inventory_path,
            ),
        )
        for patcher in self.patches:
            patcher.start()
            self.addCleanup(patcher.stop)
        self.addCleanup(shutil.rmtree, self.temp_dir)

    def write_valid_supporting_inventory(self) -> None:
        copy_repo_text(
            self.repo_root,
            "generated/federation_supporting_inventory.min.json",
        )

    def read_supporting_inventory(self) -> dict[str, object]:
        return json.loads(self.supporting_inventory_path.read_text(encoding="utf-8"))

    def write_supporting_inventory(self, payload: dict[str, object]) -> None:
        write_text(
            self.supporting_inventory_path,
            json.dumps(payload, indent=2) + "\n",
        )

    def test_valid_supporting_inventory_passes(self) -> None:
        self.write_valid_supporting_inventory()

        validate_ecosystem.validate_supporting_inventory()

    def test_missing_documented_supporting_repo_fails(self) -> None:
        self.write_valid_supporting_inventory()
        payload = self.read_supporting_inventory()
        payload["repos"] = []
        self.write_supporting_inventory(payload)

        with self.assertRaisesRegex(
            validate_ecosystem.ValidationError,
            "supporting inventory 'repos' must be a non-empty list",
        ):
            validate_ecosystem.validate_supporting_inventory()

    def test_wrong_kind_for_supporting_repo_fails(self) -> None:
        self.write_valid_supporting_inventory()
        payload = self.read_supporting_inventory()
        repos = payload["repos"]
        assert isinstance(repos, list)
        repos[0]["kind"] = "related"
        self.write_supporting_inventory(payload)

        with self.assertRaisesRegex(
            validate_ecosystem.ValidationError,
            r"kind for 'aoa-sdk' must equal 'supporting-consumer'",
        ):
            validate_ecosystem.validate_supporting_inventory()


if __name__ == "__main__":
    unittest.main()
