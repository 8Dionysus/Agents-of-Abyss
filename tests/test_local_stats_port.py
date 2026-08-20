from __future__ import annotations

from copy import deepcopy
import json
from pathlib import Path
import unittest

from jsonschema import Draft202012Validator


REPO_ROOT = Path(__file__).resolve().parents[1]
EVIDENCE_PATH = REPO_ROOT / "generated" / "ecosystem_registry.min.json"
SUPPORTING_PATH = REPO_ROOT / "generated" / "federation_supporting_inventory.min.json"
SCHEMA_PATH = REPO_ROOT / "schemas" / "ecosystem-registry.schema.json"
PACKET_PATH = (
    REPO_ROOT
    / "stats"
    / "packets"
    / "public-registry-active-maturity-ratio.reference.json"
)


def load_json(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def derive_active_maturity_ratio(payload: dict[str, object]) -> dict[str, object]:
    if payload.get("version") != 2 or payload.get("ecosystem") != "AoA":
        return {"status": "unknown", "reason": "unsupported_registry"}

    schema = load_json(SCHEMA_PATH)
    if list(Draft202012Validator(schema).iter_errors(payload)):
        return {"status": "unknown", "reason": "malformed_registry"}

    records = payload["repos"]
    assert isinstance(records, list)
    names = [record["name"] for record in records]
    if len(set(names)) != len(names):
        return {"status": "unknown", "reason": "duplicate_registry_identity"}

    numerator = sum(record["maturity"] == "active" for record in records)
    denominator = len(records)
    return {
        "status": "observed",
        "reason": "complete",
        "numerator": numerator,
        "denominator": denominator,
        "ratio": numerator / denominator,
    }


class LocalStatsPortTests(unittest.TestCase):
    def test_reference_packet_matches_current_registry_v2(self) -> None:
        evidence = load_json(EVIDENCE_PATH)
        packet = load_json(PACKET_PATH)
        derived = derive_active_maturity_ratio(evidence)

        self.assertEqual(derived["status"], "observed")
        self.assertEqual(packet["population"]["size"], derived["denominator"])
        self.assertEqual(packet["sample"]["size"], derived["denominator"])
        self.assertEqual(packet["value"]["numerator"], derived["numerator"])
        self.assertEqual(packet["value"]["denominator"], derived["denominator"])
        self.assertEqual(packet["value"]["number"], derived["ratio"])

    def test_complete_registry_with_no_active_rows_is_observed_zero(self) -> None:
        payload = deepcopy(load_json(EVIDENCE_PATH))
        for record in payload["repos"]:
            record["maturity"] = "bootstrap"

        derived = derive_active_maturity_ratio(payload)

        self.assertEqual(derived["status"], "observed")
        self.assertEqual(derived["numerator"], 0)
        self.assertEqual(derived["denominator"], 13)
        self.assertEqual(derived["ratio"], 0.0)

    def test_supporting_inventory_does_not_enter_registry_population(self) -> None:
        evidence = load_json(EVIDENCE_PATH)
        supporting = load_json(SUPPORTING_PATH)
        derived = derive_active_maturity_ratio(evidence)

        self.assertEqual(derived["denominator"], len(evidence["repos"]))
        self.assertNotEqual(
            derived["denominator"],
            len(evidence["repos"]) + len(supporting["repos"]),
        )

    def test_duplicate_malformed_and_unsupported_registries_are_unknown(self) -> None:
        valid = load_json(EVIDENCE_PATH)
        duplicate = deepcopy(valid)
        duplicate["repos"].append(deepcopy(duplicate["repos"][0]))
        malformed = deepcopy(valid)
        del malformed["repos"][0]["maturity"]
        empty = deepcopy(valid)
        empty["repos"] = []
        unsupported = deepcopy(valid)
        unsupported["version"] = 3

        for payload in (duplicate, malformed, empty, unsupported):
            with self.subTest(payload=payload):
                self.assertEqual(derive_active_maturity_ratio(payload)["status"], "unknown")


if __name__ == "__main__":
    unittest.main()
