from __future__ import annotations

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class GeneratedOwnerRequestQueueTests(unittest.TestCase):
    def test_generated_owner_request_queue_shape(self):
        payload = json.loads((ROOT / "generated/owner_request_queue.min.json").read_text(encoding="utf-8"))
        self.assertEqual(payload["schema_version"], "aoa_generated_owner_request_queue_v1")
        self.assertEqual(payload["request_count"], len(payload["requests"]))
        self.assertEqual(payload["mechanic_count"], 9)
        self.assertEqual(payload["status_counts"]["requested"], payload["request_count"])


if __name__ == "__main__":
    unittest.main()
