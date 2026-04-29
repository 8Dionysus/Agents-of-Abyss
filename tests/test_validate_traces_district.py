from __future__ import annotations

import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from validate_traces_district import validate_traces  # noqa: E402


class ValidateTracesDistrictTests(unittest.TestCase):
    def test_current_traces_district_is_valid(self) -> None:
        self.assertEqual(validate_traces(ROOT), [])

    def test_rejects_unindexed_json_trace(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            shutil.copytree(ROOT / "docs" / "traces", root / "docs" / "traces")
            trace = root / "docs" / "traces" / "GENERIC_MOVE_MANIFEST.json"
            trace.write_text(json.dumps({"schema": "aoa.generic.trace.v1"}) + "\n", encoding="utf-8")

            errors = validate_traces(root)

        self.assertTrue(any("does not index" in error for error in errors), errors)

    def test_rejects_json_without_schema_marker(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            shutil.copytree(ROOT / "docs" / "traces", root / "docs" / "traces")
            trace = root / "docs" / "traces" / "GENERIC_MOVE_MANIFEST.json"
            trace.write_text(json.dumps({"moves": []}) + "\n", encoding="utf-8")
            readme = root / "docs" / "traces" / "README.md"
            readme.write_text(
                readme.read_text(encoding="utf-8") + "\nGENERIC_MOVE_MANIFEST.json\n",
                encoding="utf-8",
            )

            errors = validate_traces(root)

        self.assertTrue(any("must declare schema or schema_version" in error for error in errors), errors)

    def test_rejects_mechanic_specific_trace_names(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            shutil.copytree(ROOT / "docs" / "traces", root / "docs" / "traces")
            trace = root / "docs" / "traces" / "AGON_MOVE_MANIFEST.json"
            trace.write_text(json.dumps({"schema": "aoa.generic.trace.v1"}) + "\n", encoding="utf-8")
            readme = root / "docs" / "traces" / "README.md"
            readme.write_text(
                readme.read_text(encoding="utf-8") + "\nAGON_MOVE_MANIFEST.json\n",
                encoding="utf-8",
            )

            errors = validate_traces(root)

        self.assertTrue(any("looks mechanic-specific" in error for error in errors), errors)


if __name__ == "__main__":
    unittest.main()
