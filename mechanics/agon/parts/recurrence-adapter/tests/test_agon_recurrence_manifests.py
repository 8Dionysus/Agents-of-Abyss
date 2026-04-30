from __future__ import annotations

import json
import re
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[5]
HOME = REPO_ROOT / "mechanics" / "agon" / "parts" / "recurrence-adapter" / "manifests"
HOOKS = HOME / "hooks"
README = HOME / "README.md"
REQUEST = (
    REPO_ROOT
    / "mechanics"
    / "agon"
    / "parts"
    / "recurrence-adapter"
    / "generated"
    / "agon_recurrence_adapter_request.min.json"
)
OLD_SERIES_WORD = "wa" + "ve"
OLD_RAW_PATH = "legacy" + "/raw"
OLD_SERIES_FILE_TOKEN = "AGON_" + "WA" + "VE"
OLD_ROOT_MANIFEST_PATH = "manifests" + "/recurrence"
OLD_FLAT_GENERATED_GLOB = "generated/" + "agon_*.min.json"
PRE_NORMALIZED_PREFIX = "legacy" + "_"


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def payload_text(data: dict) -> str:
    return json.dumps(data, sort_keys=True)


def component_files() -> list[Path]:
    return sorted(HOME.glob("component.*.json"))


def hook_files() -> list[Path]:
    return sorted(HOOKS.glob("component.*.hooks.json"))


class AgonRecurrenceManifestsTestCase(unittest.TestCase):
    def test_component_and_hook_pairs_match(self) -> None:
        components = {path.name.removesuffix(".json") for path in component_files()}
        hooks = {path.name.removesuffix(".hooks.json") for path in hook_files()}

        self.assertEqual(components, hooks)

    def test_readme_indexes_every_manifest_pair(self) -> None:
        readme = README.read_text(encoding="utf-8")

        for component in component_files():
            with self.subTest(component=component.name):
                self.assertIn(f"[`{component.name}`]({component.name})", readme)

        for hook in hook_files():
            link = f"hooks/{hook.name}"
            with self.subTest(hook=hook.name):
                self.assertIn(f"[`{link}`]({link})", readme)

    def test_component_shape_is_normalized(self) -> None:
        for component in component_files():
            data = load_json(component)

            with self.subTest(component=component.name):
                self.assertEqual(data["schema_version"], "aoa_agon_recurrence_component_manifest_v1")
                self.assertEqual(data["manifest_class"], "agon_recurrence_component")
                self.assertTrue(data["component_ref"].startswith("component:agon:"))
                self.assertEqual(data["owner_part"], "mechanics/agon/parts/recurrence-adapter")
                self.assertEqual(data["runtime_effect"], "none")
                self.assertIs(data["live_protocol"], False)
                self.assertIsInstance(data["source_refs"], list)
                self.assertIsInstance(data["observed_surfaces"], list)
                self.assertIsInstance(data["stop_lines"], list)
                text = payload_text(data)
                self.assertNotIn(OLD_ROOT_MANIFEST_PATH, text)
                self.assertNotIn(OLD_FLAT_GENERATED_GLOB, text)
                self.assertNotIn(OLD_RAW_PATH, text)
                self.assertNotIn(OLD_SERIES_FILE_TOKEN, text)
                self.assertNotIn(PRE_NORMALIZED_PREFIX, text)
                self.assertIsNone(re.search(rf"\b{OLD_SERIES_WORD}\b", text, re.IGNORECASE))

    def test_hook_shape_is_normalized(self) -> None:
        component_refs = {load_json(component)["component_ref"] for component in component_files()}

        for hook in hook_files():
            data = load_json(hook)

            with self.subTest(hook=hook.name):
                self.assertEqual(data["schema_version"], "aoa_agon_recurrence_hook_manifest_v1")
                self.assertEqual(data["manifest_class"], "agon_recurrence_hook_binding")
                self.assertIn(data["component_ref"], component_refs)
                self.assertEqual(data["owner_part"], "mechanics/agon/parts/recurrence-adapter")
                self.assertEqual(data["runtime_effect"], "none")
                self.assertIs(data["live_protocol"], False)
                self.assertIsInstance(data["bindings"], list)
                self.assertIsInstance(data["must_not_emit"], list)
                text = payload_text(data)
                self.assertNotIn(OLD_ROOT_MANIFEST_PATH, text)
                self.assertNotIn(OLD_FLAT_GENERATED_GLOB, text)
                self.assertNotIn(OLD_RAW_PATH, text)
                self.assertNotIn(OLD_SERIES_FILE_TOKEN, text)
                self.assertNotIn(PRE_NORMALIZED_PREFIX, text)
                self.assertIsNone(re.search(rf"\b{OLD_SERIES_WORD}\b", text, re.IGNORECASE))

    def test_adapter_request_paths_distinguish_local_and_owner_local(self) -> None:
        request = load_json(REQUEST)

        for component in request["requested_components"]:
            with self.subTest(component=component["component_ref"]):
                if component["target_repo"] == "Agents-of-Abyss":
                    self.assertTrue((REPO_ROOT / component["manifest_path"]).is_file())
                    self.assertTrue((REPO_ROOT / component["hook_manifest_path"]).is_file())
                else:
                    prefix = f"owner-local://{component['target_repo']}/"
                    self.assertTrue(component["manifest_path"].startswith(prefix))
                    self.assertTrue(component["hook_manifest_path"].startswith(prefix))


if __name__ == "__main__":
    unittest.main()
