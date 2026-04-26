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
            "mechanics/README.md",
            "AGENTS.md",
            "docs/AGENTS.md",
            "CONTRIBUTING.md",
            "generated/AGENTS.md",
        ):
            with self.subTest(path=relative_path):
                text = read_text(relative_path)
                self.assertIn("python scripts/validate_ecosystem.py", text)
                self.assertIn("python -m pytest -q", text)

    def test_readme_keeps_aoa_sdk_outside_compact_registry_v1_but_routes_to_supporting_inventory(self) -> None:
        readme = read_text("README.md")
        self.assertIn("aoa-sdk", readme)
        self.assertIn("compact registry membership", readme)
        self.assertIn("generated/federation_supporting_inventory.min.json", readme)

    def test_center_surfaces_name_aoa_stats_as_public_layer(self) -> None:
        readme = read_text("README.md")
        charter = read_text("CHARTER.md")
        ecosystem_map = read_text("ECOSYSTEM_MAP.md")
        roadmap = read_text("ROADMAP.md")

        self.assertIn("`aoa-stats` | derived observability and machine-first summaries", readme)
        self.assertIn("- `aoa-stats`", charter)
        self.assertIn("`aoa-stats` | derived observability layer", ecosystem_map)
        self.assertIn("- `aoa-stats`", roadmap)

    def test_docs_readme_routes_to_mechanics_and_decision_notes_remain_available(self) -> None:
        docs_readme = read_text("docs/README.md")
        mechanics = read_text("mechanics/README.md")

        self.assertIn("mechanics/README.md", docs_readme)
        self.assertIn("aoa-stats", mechanics)
        self.assertTrue(
            (REPO_ROOT / "docs/decisions/2026-04-09-aoa-stats-public-layer.md").exists()
        )

    def test_direction_surfaces_map_routes_sdk_stats_and_seed_garden_through_root_roadmaps(self) -> None:
        direction_surfaces = read_text("mechanics/release-support/docs/DIRECTION_SURFACES.md")

        self.assertIn("| `aoa-stats` | `ROADMAP.md` |", direction_surfaces)
        self.assertIn("| `aoa-sdk` | `ROADMAP.md` |", direction_surfaces)
        self.assertIn("| `Dionysus` | `ROADMAP.md` |", direction_surfaces)
        self.assertIn("| `8Dionysus` | `docs/PUBLIC_ENTRY_POSTURE.md` |", direction_surfaces)

    def test_growth_refinery_routes_include_owner_landing_and_pruning_doctrine(self) -> None:
        readme = read_text("README.md")
        docs_readme = read_text("docs/README.md")
        mechanics = read_text("mechanics/README.md")
        refinery_doc = read_text("mechanics/method-growth/docs/REVIEWABLE_GROWTH_REFINERY.md")
        crosswalk = read_text("mechanics/method-growth/docs/CANDIDATE_LINEAGE_CROSSWALK.md")
        owner_landing = read_text("mechanics/method-growth/docs/OWNER_LANDING_AND_PRUNING.md")

        self.assertIn("mechanics/README.md", readme)
        self.assertIn("method-growth/docs/OWNER_LANDING_AND_PRUNING", mechanics)
        self.assertIn("python mechanics/method-growth/scripts/validate_candidate_lineage_contract.py --workspace-root /srv", mechanics)
        self.assertIn("python mechanics/method-growth/scripts/validate_wave4_kernel_automation.py --workspace-root /srv", mechanics)
        self.assertIn("OWNER_LANDING_AND_PRUNING.md", docs_readme)
        self.assertIn("mechanics/method-growth/docs/OWNER_LANDING_AND_PRUNING.md", refinery_doc)
        self.assertIn("python mechanics/method-growth/scripts/validate_candidate_lineage_contract.py --workspace-root /srv", refinery_doc)
        self.assertIn("python mechanics/method-growth/scripts/validate_wave4_kernel_automation.py --workspace-root /srv", refinery_doc)
        self.assertIn("mechanics/method-growth/docs/OWNER_LANDING_AND_PRUNING.md", crosswalk)
        self.assertIn("weaker than a landed owner object", owner_landing)
        self.assertIn("let `aoa-stats` infer owner truth", owner_landing)
        self.assertIn("let `aoa-memo` turn prune or recovery writeback into landing authority", owner_landing)
        self.assertIn("let `aoa-routing` treat owner-status hints as stronger than owner-local review", owner_landing)

    def test_self_agency_continuity_routes_stay_center_bounded(self) -> None:
        readme = read_text("README.md")
        docs_readme = read_text("docs/README.md")
        method_spine = read_text("mechanics/method-growth/docs/METHOD_SPINE.md")
        federation_rules = read_text("docs/FEDERATION_RULES.md")
        continuity = read_text("mechanics/recurrence/docs/SELF_AGENCY_CONTINUITY.md")

        self.assertIn("mechanics/recurrence/docs/SELF_AGENCY_CONTINUITY", readme)
        self.assertIn("SELF_AGENCY_CONTINUITY.md", docs_readme)
        self.assertIn("mechanics/recurrence/docs/SELF_AGENCY_CONTINUITY.md", method_spine)
        self.assertIn("continuity_ref -> revision_window_ref -> reanchor_ref -> anchor_artifact_ref", continuity)
        self.assertIn("`aoa-agents` owns role-facing continuity", continuity)
        self.assertIn("`aoa-playbooks` owns recurring continuity choreography", continuity)
        self.assertIn("runtime autonomy", federation_rules)
        self.assertIn("continuity does not transfer authority away from the owning repositories", federation_rules)

    def test_component_refresh_routes_stay_owner_owned(self) -> None:
        readme = read_text("README.md")
        docs_readme = read_text("docs/README.md")
        roadmap = read_text("ROADMAP.md")
        method_spine = read_text("mechanics/method-growth/docs/METHOD_SPINE.md")
        federation_rules = read_text("docs/FEDERATION_RULES.md")
        refinery = read_text("mechanics/method-growth/docs/REVIEWABLE_GROWTH_REFINERY.md")
        component_refresh = read_text("mechanics/recurrence/docs/COMPONENT_REFRESH_LAW.md")

        self.assertIn("mechanics/recurrence/docs/COMPONENT_REFRESH_LAW", readme)
        self.assertIn("COMPONENT_REFRESH_LAW.md", docs_readme)
        self.assertIn("component refresh owner-owned", roadmap)
        self.assertIn("mechanics/recurrence/docs/COMPONENT_REFRESH_LAW.md", method_spine)
        self.assertIn("mystical self-healing", federation_rules)
        self.assertIn("mechanics/recurrence/docs/COMPONENT_REFRESH_LAW.md", refinery)
        self.assertIn("owner refresh law", component_refresh)
        self.assertIn("the shared-root Codex plane in `8Dionysus`", component_refresh)

    def test_agon_preparation_routes_stay_center_bounded(self) -> None:
        readme = read_text("README.md")
        docs_readme = read_text("docs/README.md")
        mechanics = read_text("mechanics/README.md")
        roadmap = read_text("ROADMAP.md")
        layers = read_text("docs/LAYERS.md")
        repo_roles = read_text("docs/REPO_ROLES.md")
        posture = read_text("mechanics/agon/legacy/raw/AGON_PREPARATION_POSTURE.md")

        self.assertIn("mechanics/agon/README.md", readme)
        self.assertIn("Imposition Readiness", mechanics)
        self.assertIn("agon/PROVENANCE.md", mechanics)
        self.assertIn("agon/legacy/INDEX.md", mechanics)
        self.assertIn("PROVENANCE", docs_readme)
        self.assertIn("Agon preparation holding boundary", roadmap)
        self.assertIn("Agon preparation protocol posture", layers)
        self.assertIn("future Agon law", repo_roles)
        self.assertIn("Agon is not a live implementation layer yet", posture)
        self.assertIn("holding boundary", posture)
        self.assertIn("civil/service", posture)
        self.assertIn("not a planted wave package", posture)
        self.assertIn("not a new sibling repository", posture)
        self.assertIn("no direct arena write path", posture)
        self.assertIn("arena -> memo -> eval -> kag -> ToS candidate", posture)

    def test_agon_imposition_routes_stay_center_bounded(self) -> None:
        readme = read_text("README.md")
        docs_readme = read_text("docs/README.md")
        mechanics = read_text("mechanics/README.md")
        landing_log = read_text("mechanics/agon/LANDING_LOG.md")
        layers = read_text("docs/LAYERS.md")
        repo_roles = read_text("docs/REPO_ROLES.md")
        posture = read_text("mechanics/agon/legacy/raw/AGON_IMPOSITION_POSTURE.md")
        survival = read_text("mechanics/agon/legacy/raw/AGON_SURVIVAL_CRITERIA.md")
        audit = read_text("mechanics/agon/legacy/raw/AGON_DOUBT_AUDIT.md")
        baseline = read_text("mechanics/agon/legacy/raw/PRE_AGON_BASELINE.md")
        readiness = read_text("mechanics/agon/generated/agon_imposition_readiness.min.json")

        self.assertIn("mechanics/agon/README.md", readme)
        self.assertIn("Imposition Readiness", mechanics)
        self.assertIn("agon/PROVENANCE.md", mechanics)
        self.assertIn("agon/legacy/INDEX.md", mechanics)
        self.assertIn("PROVENANCE", docs_readme)
        self.assertIn("Agon imposition gate", landing_log)
        self.assertIn("Agon imposition gate", layers)
        self.assertIn("mechanics/agon/PROVENANCE.md", repo_roles)
        self.assertIn("Agon is now an imposed review lens", posture)
        self.assertIn("Agon is still not a live implementation layer", posture)
        self.assertIn("survive", survival)
        self.assertIn("quarantine", survival)
        self.assertIn("Wave I and Wave II", audit)
        self.assertIn("Release-clean is not Agon-ready.", baseline)
        self.assertIn("\"surface_kind\":\"agon_imposition_gate\"", readiness)
        self.assertIn("Wave I: Agonic Actor Rechartering", readiness)

    def test_agon_lawful_move_routes_stay_center_bounded(self) -> None:
        readme = read_text("README.md")
        docs_readme = read_text("docs/README.md")
        mechanics = read_text("mechanics/README.md")
        landing_log = read_text("mechanics/agon/LANDING_LOG.md")
        layers = read_text("docs/LAYERS.md")
        repo_roles = read_text("docs/REPO_ROLES.md")
        move_language = read_text("mechanics/agon/legacy/raw/AGON_LAWFUL_MOVE_LANGUAGE.md")
        landing = read_text("mechanics/agon/legacy/raw/AGON_WAVE3_LANDING.md")
        registry = read_text("mechanics/agon/generated/agon_lawful_move_registry.min.json")

        self.assertIn("mechanics/agon/README.md", readme)
        self.assertIn("Lawful Move Grammar", mechanics)
        self.assertIn("agon/PROVENANCE.md", mechanics)
        self.assertIn("agon/legacy/INDEX.md", mechanics)
        self.assertIn("PROVENANCE", docs_readme)
        self.assertIn("Agon lawful move language", landing_log)
        self.assertIn("Agon lawful move language", layers)
        self.assertIn("mechanics/agon/PROVENANCE.md", repo_roles)
        self.assertIn("lawful tongue", move_language)
        self.assertIn("pre-protocol", landing)
        self.assertIn("\"live_protocol\":false", registry)
        self.assertIn("\"runtime_effect\":\"none\"", registry)

    def test_agon_move_owner_binding_routes_stay_center_bounded(self) -> None:
        readme = read_text("README.md")
        docs_readme = read_text("docs/README.md")
        mechanics = read_text("mechanics/README.md")
        landing_log = read_text("mechanics/agon/LANDING_LOG.md")
        layers = read_text("docs/LAYERS.md")
        repo_roles = read_text("docs/REPO_ROLES.md")
        binding = read_text("mechanics/agon/legacy/raw/AGON_MOVE_OWNER_BINDING.md")
        landing = read_text("mechanics/agon/legacy/raw/AGON_WAVE4_LANDING.md")
        registry = read_text("mechanics/agon/generated/agon_move_owner_binding_registry.min.json")

        self.assertIn("mechanics/agon/README.md", readme)
        self.assertIn("Owner Binding", mechanics)
        self.assertIn("agon/PROVENANCE.md", mechanics)
        self.assertIn("agon/legacy/INDEX.md", mechanics)
        self.assertIn("PROVENANCE", docs_readme)
        self.assertIn("Agon move owner binding", landing_log)
        self.assertIn("Agon move owner binding", layers)
        self.assertIn("mechanics/agon/OWNER_REQUESTS.md", repo_roles)
        self.assertIn("owner gravity", binding)
        self.assertIn("requested_not_landed", landing)
        self.assertIn("\"status\":\"pre_protocol_owner_binding\"", registry)
        self.assertIn("\"readiness\":\"owner_binding_seeded\"", registry)

    def test_agon_gate_routing_handoff_routes_stay_center_bounded(self) -> None:
        readme = read_text("README.md")
        docs_readme = read_text("docs/README.md")
        mechanics = read_text("mechanics/README.md")
        landing_log = read_text("mechanics/agon/LANDING_LOG.md")
        layers = read_text("docs/LAYERS.md")
        repo_roles = read_text("docs/REPO_ROLES.md")
        handoff = read_text("mechanics/agon/legacy/raw/AGON_GATE_ROUTING_HANDOFF.md")
        landing = read_text("mechanics/agon/legacy/raw/AGON_WAVE5_CENTER_HANDOFF.md")
        request = read_text("mechanics/agon/generated/agon_gate_routing_handoff_request.min.json")

        self.assertIn("mechanics/agon/README.md", readme)
        self.assertIn("mechanics/README.md", docs_readme)
        self.assertIn("Gate Routing", mechanics)
        self.assertIn("agon/PROVENANCE.md", mechanics)
        self.assertIn("agon/legacy/INDEX.md", mechanics)
        self.assertIn("Agon gate routing handoff", landing_log)
        self.assertIn("Agon gate routing handoff", layers)
        self.assertIn("mechanics/agon/PARTS.md", repo_roles)
        self.assertIn("may grow a thin pre-protocol gate surface", handoff)
        self.assertIn("gate hint is not arena activation", landing)
        self.assertIn("\"status\":\"seeded_center_handoff_request\"", request)
        self.assertIn("\"required_stop_line\":\"routing hint is not arena activation\"", request)

    def test_agon_trial_playbook_handoff_routes_stay_center_bounded(self) -> None:
        readme = read_text("README.md")
        docs_readme = read_text("docs/README.md")
        mechanics = read_text("mechanics/README.md")
        landing_log = read_text("mechanics/agon/LANDING_LOG.md")
        layers = read_text("docs/LAYERS.md")
        repo_roles = read_text("docs/REPO_ROLES.md")
        handoff = read_text("mechanics/agon/legacy/raw/AGON_TRIAL_PLAYBOOK_HANDOFF.md")
        owner_request = read_text("mechanics/agon/legacy/raw/AGON_TRIAL_PLAYBOOK_OWNER_REQUEST.md")
        stop_lines = read_text("mechanics/agon/legacy/raw/AGON_TRIAL_PLAYBOOK_STOP_LINES.md")
        request = read_text("mechanics/agon/generated/agon_trial_playbook_request.min.json")

        self.assertIn("mechanics/agon/README.md", readme)
        self.assertIn("mechanics/README.md", docs_readme)
        self.assertIn("Trial Handoff", mechanics)
        self.assertIn("agon/PROVENANCE.md", mechanics)
        self.assertIn("agon/legacy/INDEX.md", mechanics)
        self.assertIn("Agon trial playbook handoff", landing_log)
        self.assertIn("Agon trial playbook handoff", layers)
        self.assertIn("mechanics/agon/PARTS.md", repo_roles)
        self.assertIn("Trial playbooks rehearse the arena. They do not open it.", handoff)
        self.assertIn("requests that `aoa-playbooks` land", owner_request)
        self.assertIn("pre-protocol choreography wave", stop_lines)
        self.assertIn("\"status\":\"seeded_pre_protocol_owner_request\"", request)
        self.assertIn("\"target_repo\":\"aoa-playbooks\"", request)

    def test_generated_agents_keeps_registry_as_publication_surface(self) -> None:
        generated_agents = read_text("generated/AGENTS.md")
        self.assertIn("published summary surface", generated_agents)
        self.assertIn("not a hidden second charter", generated_agents)

    def test_readme_and_public_support_posture_expose_center_entry_capsule(self) -> None:
        readme = read_text("README.md")
        posture = read_text("mechanics/release-support/docs/PUBLIC_SUPPORT_POSTURE.md")

        self.assertIn("generated/center_entry_map.min.json", readme)
        self.assertIn("python scripts/build_center_entry_map.py --check", readme)
        self.assertIn("python scripts/validate_center_entry_map.py", readme)
        self.assertIn("generated/center_entry_map.min.json", posture)
        self.assertIn("python scripts/build_center_entry_map.py --check", posture)
        self.assertIn("python scripts/validate_center_entry_map.py", posture)


if __name__ == "__main__":
    unittest.main()
