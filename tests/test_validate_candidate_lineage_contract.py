from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory


REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from validate_candidate_lineage_contract import validate_chain


def write_json(path: Path, payload: dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False), encoding="utf-8")


class CandidateLineageContractValidatorTests(unittest.TestCase):
    def write_valid_workspace(self, root: Path) -> None:
        cluster_ref = "cluster:growth:aoa-sdk-checkpoint-auto-capture-verify-green"
        candidate_ref = "candidate:session-growth:reviewed-donor-harvest"

        write_json(
            root / "aoa-sdk" / "examples" / "checkpoint_lineage_hint.example.json",
            {
                "schema_version": "aoa_checkpoint_lineage_hint_v1",
                "cluster_ref": cluster_ref,
                "owner_hypothesis": "aoa-skills",
                "owner_shape": "reviewed donor harvest candidate",
                "nearest_wrong_target": "aoa-sdk",
                "evidence_refs": ["checkpoint:auto-capture:verify-green"],
                "axis_pressure": ["execution_reliability"],
                "status_posture": "stable",
            },
        )
        write_json(
            root
            / "aoa-skills"
            / "examples"
            / "session_growth_artifacts"
            / "candidate_lineage_receipt.alpha.json",
            {
                "schema_version": "aoa_candidate_lineage_receipt_v1",
                "receipt_kind": "candidate_lineage_receipt",
                "cluster_ref": cluster_ref,
                "candidate_ref": candidate_ref,
                "owner_hypothesis": "aoa-skills",
                "owner_shape": "reviewed donor harvest candidate",
                "nearest_wrong_target": "aoa-sdk",
                "status_posture": "stable",
                "evidence_refs": ["checkpoint:auto-capture:verify-green"],
            },
        )
        write_json(
            root / "Dionysus" / "examples" / "seed_lineage_entry.example.json",
            {
                "schema_version": "dionysus_seed_lineage_entry_v1",
                "seed_ref": "seed:aoa:session-growth:reviewed-donor-harvest:v1",
                "candidate_ref": candidate_ref,
                "cluster_ref": cluster_ref,
                "owner_hypothesis": "aoa-skills",
                "status_posture": "stable",
                "lifecycle_status": "staged",
                "object_ref": None,
            },
        )

    def test_accepts_one_aligned_chain(self) -> None:
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.write_valid_workspace(root)

            summary = validate_chain(root)

        self.assertEqual(summary.cluster_ref, "cluster:growth:aoa-sdk-checkpoint-auto-capture-verify-green")
        self.assertEqual(summary.candidate_ref, "candidate:session-growth:reviewed-donor-harvest")
        self.assertEqual(summary.seed_ref, "seed:aoa:session-growth:reviewed-donor-harvest:v1")

    def test_rejects_sdk_candidate_minting(self) -> None:
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.write_valid_workspace(root)
            sdk_path = root / "aoa-sdk" / "examples" / "checkpoint_lineage_hint.example.json"
            payload = json.loads(sdk_path.read_text(encoding="utf-8"))
            payload["candidate_ref"] = "candidate:forbidden"
            write_json(sdk_path, payload)

            with self.assertRaisesRegex(ValueError, "aoa-sdk example must not mint candidate_ref"):
                validate_chain(root)


if __name__ == "__main__":
    unittest.main()
