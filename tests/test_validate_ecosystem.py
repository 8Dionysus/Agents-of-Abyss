from __future__ import annotations

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


if __name__ == "__main__":
    unittest.main()
