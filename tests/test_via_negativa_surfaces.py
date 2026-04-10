from __future__ import annotations

import json
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


def test_deletion_candidates_surface_stays_owner_aware() -> None:
    candidates = json.loads((REPO_ROOT / "DELETION_CANDIDATES.json").read_text())
    schema = json.loads(
        (REPO_ROOT / "schemas" / "deletion_candidate_list_v1.json").read_text()
    )

    assert candidates["schema_version"] == schema["properties"]["schema_version"]["const"]
    assert candidates["scope"]["pass_kind"] == "via_negativa_pruning"
    assert candidates["scope"]["candidate_mode"] == "inspect_first"
    assert candidates["guardrails"]

    seen_ids: set[str] = set()
    allowed_statuses = {
        "inspect_first",
        "safe_to_merge_if_duplicate",
        "safe_to_move_if_misplaced",
        "owner_review_required",
    }
    allowed_priorities = {"low", "medium", "high", "critical"}

    for candidate in candidates["candidates"]:
        candidate_id = candidate["candidate_id"]
        assert candidate_id not in seen_ids
        seen_ids.add(candidate_id)
        assert candidate["owner_review_required"] is True
        assert candidate["status"] in allowed_statuses
        assert candidate["priority"] in allowed_priorities
        if candidate["preferred_action"] == "delete":
            assert candidate.get("never_delete_without")


def test_center_docs_route_to_via_negativa_surfaces() -> None:
    readme = (REPO_ROOT / "README.md").read_text()
    docs_readme = (REPO_ROOT / "docs" / "README.md").read_text()

    assert "docs/VIA_NEGATIVA.md" in readme
    assert "docs/ANTI_AUTHORITY_RULES.md" in readme
    assert "docs/ONE_IN_ONE_OUT.md" in readme
    assert "DELETION_CANDIDATES.json" in readme

    assert "VIA_NEGATIVA.md" in docs_readme
    assert "ANTI_AUTHORITY_RULES.md" in docs_readme
    assert "ONE_IN_ONE_OUT.md" in docs_readme
