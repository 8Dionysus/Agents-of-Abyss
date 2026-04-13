from __future__ import annotations

import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


def read_text(relative_path: str) -> str:
    return (REPO_ROOT / relative_path).read_text(encoding="utf-8")


class DocsVerifyRoutesTestCase(unittest.TestCase):
    def test_public_and_operator_surfaces_include_full_bounded_battery(self) -> None:
        for relative_path in (
            "README.md",
            "docs/README.md",
            "AGENTS.md",
            "docs/AGENTS.md",
            "CONTRIBUTING.md",
            "generated/AGENTS.md",
        ):
            with self.subTest(path=relative_path):
                text = read_text(relative_path)
                self.assertIn("python scripts/validate_ecosystem.py", text)
                self.assertIn("python -m pytest -q tests", text)

    def test_readme_keeps_aoa_sdk_outside_compact_registry_v1_but_routes_to_supporting_inventory(self) -> None:
        readme = read_text("README.md")
        self.assertIn("aoa-sdk", readme)
        self.assertIn("outside the compact registry v1 by design", readme)
        self.assertIn("supporting machine-readable inventory", readme)

    def test_center_surfaces_name_aoa_stats_as_public_layer(self) -> None:
        readme = read_text("README.md")
        charter = read_text("CHARTER.md")
        ecosystem_map = read_text("ECOSYSTEM_MAP.md")
        roadmap = read_text("ROADMAP.md")

        self.assertIn("`aoa-stats` | derived observability and machine-first summary layer", readme)
        self.assertIn("- `aoa-stats`", charter)
        self.assertIn("`aoa-stats` | derived observability layer", ecosystem_map)
        self.assertIn("- `aoa-stats`", roadmap)

    def test_docs_readme_routes_to_aoa_stats_public_layer_decision(self) -> None:
        docs_readme = read_text("docs/README.md")
        self.assertIn("decisions/2026-04-09-aoa-stats-public-layer.md", docs_readme)
        self.assertIn("public federation contour", docs_readme)

    def test_direction_surfaces_map_routes_sdk_stats_and_seed_garden_through_root_roadmaps(self) -> None:
        direction_surfaces = read_text("docs/DIRECTION_SURFACES.md")

        self.assertIn("| `aoa-stats` | `ROADMAP.md` |", direction_surfaces)
        self.assertIn("| `aoa-sdk` | `ROADMAP.md` |", direction_surfaces)
        self.assertIn("| `Dionysus` | `ROADMAP.md` |", direction_surfaces)
        self.assertIn("| `8Dionysus` | `docs/PUBLIC_ENTRY_POSTURE.md` |", direction_surfaces)

    def test_growth_refinery_routes_include_owner_landing_and_pruning_doctrine(self) -> None:
        readme = read_text("README.md")
        docs_readme = read_text("docs/README.md")
        refinery_doc = read_text("docs/REVIEWABLE_GROWTH_REFINERY.md")
        crosswalk = read_text("docs/CANDIDATE_LINEAGE_CROSSWALK.md")
        owner_landing = read_text("docs/OWNER_LANDING_AND_PRUNING.md")

        self.assertIn("docs/OWNER_LANDING_AND_PRUNING", readme)
        self.assertIn("python scripts/validate_candidate_lineage_contract.py --workspace-root /srv", readme)
        self.assertIn("python scripts/validate_wave4_kernel_automation.py --workspace-root /srv", readme)
        self.assertIn("OWNER_LANDING_AND_PRUNING.md", docs_readme)
        self.assertIn("docs/OWNER_LANDING_AND_PRUNING.md", refinery_doc)
        self.assertIn("python scripts/validate_candidate_lineage_contract.py --workspace-root /srv", refinery_doc)
        self.assertIn("python scripts/validate_wave4_kernel_automation.py --workspace-root /srv", refinery_doc)
        self.assertIn("docs/OWNER_LANDING_AND_PRUNING.md", crosswalk)
        self.assertIn("weaker than a landed owner object", owner_landing)
        self.assertIn("let `aoa-stats` infer owner truth", owner_landing)
        self.assertIn("let `aoa-memo` turn prune or recovery writeback into landing authority", owner_landing)
        self.assertIn("let `aoa-routing` treat owner-status hints as stronger than owner-local review", owner_landing)

    def test_self_agency_continuity_routes_stay_center_bounded(self) -> None:
        readme = read_text("README.md")
        docs_readme = read_text("docs/README.md")
        method_spine = read_text("docs/METHOD_SPINE.md")
        federation_rules = read_text("docs/FEDERATION_RULES.md")
        continuity = read_text("docs/SELF_AGENCY_CONTINUITY.md")

        self.assertIn("docs/SELF_AGENCY_CONTINUITY", readme)
        self.assertIn("SELF_AGENCY_CONTINUITY.md", docs_readme)
        self.assertIn("docs/SELF_AGENCY_CONTINUITY.md", method_spine)
        self.assertIn("continuity_ref -> revision_window_ref -> reanchor_ref -> anchor_artifact_ref", continuity)
        self.assertIn("`aoa-agents` owns role-facing continuity", continuity)
        self.assertIn("`aoa-playbooks` owns recurring continuity choreography", continuity)
        self.assertIn("runtime autonomy", federation_rules)
        self.assertIn("continuity does not transfer authority away from the owning repositories", federation_rules)

    def test_component_refresh_routes_stay_owner_owned(self) -> None:
        readme = read_text("README.md")
        docs_readme = read_text("docs/README.md")
        roadmap = read_text("ROADMAP.md")
        method_spine = read_text("docs/METHOD_SPINE.md")
        federation_rules = read_text("docs/FEDERATION_RULES.md")
        refinery = read_text("docs/REVIEWABLE_GROWTH_REFINERY.md")
        component_refresh = read_text("docs/COMPONENT_REFRESH_LAW.md")

        self.assertIn("docs/COMPONENT_REFRESH_LAW", readme)
        self.assertIn("COMPONENT_REFRESH_LAW.md", docs_readme)
        self.assertIn("component refresh owner-owned", roadmap)
        self.assertIn("docs/COMPONENT_REFRESH_LAW.md", method_spine)
        self.assertIn("mystical self-healing", federation_rules)
        self.assertIn("docs/COMPONENT_REFRESH_LAW.md", refinery)
        self.assertIn("owner refresh law", component_refresh)
        self.assertIn("the shared-root Codex plane in `8Dionysus`", component_refresh)

    def test_pre_agon_preparation_routes_stay_center_bounded(self) -> None:
        readme = read_text("README.md")
        docs_readme = read_text("docs/README.md")
        roadmap = read_text("ROADMAP.md")
        layers = read_text("docs/LAYERS.md")
        repo_roles = read_text("docs/REPO_ROLES.md")
        posture = read_text("docs/AGON_PREPARATION_POSTURE.md")

        self.assertIn("docs/AGON_PREPARATION_POSTURE", readme)
        self.assertIn("AGON_PREPARATION_POSTURE.md", docs_readme)
        self.assertIn("pre-Agon landing boundary", roadmap)
        self.assertIn("Pre-Agon protocol posture", layers)
        self.assertIn("future Agon law", repo_roles)
        self.assertIn("Agon is not a live implementation layer yet", posture)
        self.assertIn("not a new sibling repository", posture)
        self.assertIn("no direct arena write path", posture)
        self.assertIn("arena -> memo -> eval -> kag -> ToS candidate", posture)

    def test_generated_agents_keeps_registry_as_publication_surface(self) -> None:
        generated_agents = read_text("generated/AGENTS.md")
        self.assertIn("published summary surface", generated_agents)
        self.assertIn("not a hidden second charter", generated_agents)

    def test_readme_and_public_support_posture_expose_center_entry_capsule(self) -> None:
        readme = read_text("README.md")
        posture = read_text("docs/PUBLIC_SUPPORT_POSTURE.md")

        self.assertIn("generated/center_entry_map.min.json", readme)
        self.assertIn("python scripts/build_center_entry_map.py --check", readme)
        self.assertIn("python scripts/validate_center_entry_map.py", readme)
        self.assertIn("generated/center_entry_map.min.json", posture)
        self.assertIn("python scripts/build_center_entry_map.py --check", posture)
        self.assertIn("python scripts/validate_center_entry_map.py", posture)


if __name__ == "__main__":
    unittest.main()
