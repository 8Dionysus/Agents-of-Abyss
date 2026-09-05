# Validation Routes

This is the on-demand executable validation map for the Agents-of-Abyss
repository. Inherited `AGENTS.md` cards name the applicable lane; they do not
carry command matrices. Run the narrowest route first, then widen checks when
the changed surface or release boundary requires it.

## Core route

For a repository-wide change, use the release gate after focused checks. The
gate owns the ordered compatibility, documentation, topology, hygiene, and
test battery for this repository.

```text
python scripts/release_gate/release_check.py
```

The release gate needs a compatible `aoa-stats` checkout through
`AOA_STATS_ROOT`, `.deps/aoa-stats`, or `../aoa-stats` when its compatibility
step is enabled.

## AGENTS mesh

Use these checks when an inherited card, mesh registry, or generated mesh view
changes:

```text
python scripts/agents_mesh/validate_nested_agents.py
python scripts/agents_mesh/validate_agents_md_shape.py
python scripts/agents_mesh/validate_agents_mesh.py
python scripts/agents_mesh/build_agents_mesh_index.py --check
python scripts/agents_mesh/validate_agents_mesh_index.py
```

## Documentation and hygiene

Use the docs and hygiene lanes for route, decision, Markdown, link, status, or
generated-freshness changes:

```text
python scripts/docs_districts/plan_docs_thematic_cleanup.py --check
python scripts/docs_districts/validate_docs_thematic_districts.py
python scripts/docs_districts/validate_docs_migration_map.py
python scripts/docs_districts/validate_traces_district.py
python scripts/docs_districts/validate_decision_records.py
python scripts/docs_districts/build_docs_thematic_index.py --check
python scripts/docs_districts/validate_docs_thematic_index.py
python scripts/hygiene/validate_links.py
python scripts/hygiene/validate_markdown_shape.py
python scripts/hygiene/validate_status_vocabulary.py
python scripts/hygiene/build_link_shape_hygiene_index.py --check
python scripts/hygiene/validate_link_shape_hygiene_index.py
python scripts/hygiene/validate_generated_freshness.py
python scripts/hygiene/validate_hygiene_suite.py
```

## Center and registry lanes

Use the center-entry, organ, registry, and source-owned checks when those
surfaces are affected:

```text
python scripts/center_entry/validate_entry_surface_sync.py
python scripts/center_entry/build_center_entry_map.py --check
python scripts/center_entry/validate_center_entry_map.py
python scripts/organ_contract/validate_organ_contract.py
python scripts/root_registries/validate_ecosystem.py
python scripts/root_registries/validate_config_registry.py
python scripts/root_registries/validate_manifests_registry.py
python scripts/root_registries/validate_schema_registry.py
python scripts/root_registries/validate_scripts_district.py
python scripts/root_registries/validate_tests_district.py
```

## Mechanics

`mechanics/validation-routes.json` is the exact source manifest for child
surfaces. Inspect a route before execution and use the no-shell runner for one
exact repository-relative surface:

```text
python scripts/mechanics_topology/validate_validation_routes.py
python scripts/mechanics_topology/run_validation_route.py --surface <repo-relative-path> --show
python scripts/mechanics_topology/run_validation_route.py --surface <repo-relative-path>
```

Package topology and owner-request routes are checked through their owning
validators:

```text
python scripts/mechanics_topology/validate_mechanic_readme_cards.py
python scripts/mechanics_topology/build_mechanic_card_index.py --check
python scripts/mechanics_topology/validate_mechanic_card_index.py
python scripts/mechanics_topology/validate_mechanics_topology.py
python scripts/mechanics_topology/validate_mechanic_artifact_topology.py
python scripts/mechanics_topology/validate_mechanic_landing_logs.py
python scripts/owner_requests/validate_owner_request_queue.py
python scripts/owner_requests/build_owner_request_queue.py --check
python scripts/owner_requests/validate_generated_owner_request_queue.py
python scripts/owner_requests/validate_owner_request_docs.py
```

Part-local `VALIDATION.md` surfaces name their exact key in
`mechanics/validation-routes.json` and the no-shell runner route. The manifest
owns the underlying argv lists; do not copy those commands into an inherited
card or imply that a local surface is an independent command authority.

Package registry validation refs remain addressable from this map:

- `mechanics/method-growth/scripts/validate_method_growth_mechanic.py`
- `mechanics/distillation/scripts/validate_distillation_mechanic.py`
- `mechanics/growth-cycle/scripts/validate_growth_cycle_mechanic.py`
- `mechanics/recurrence/scripts/validate_recurrence_mechanic.py`
- `mechanics/checkpoint/scripts/validate_checkpoint_mechanic.py`
- `mechanics/experience/scripts/validate_experience_distillation.py`
- `mechanics/agon/scripts/validate_agon_distillation.py`
- `mechanics/antifragility/scripts/validate_antifragility_distillation.py`
- `mechanics/questbook/scripts/validate_questbook_lifecycle.py`
- `mechanics/questbook/scripts/build_questbook_index.py`
- `mechanics/questbook/scripts/validate_questbook_index.py`
- `mechanics/questbook/scripts/build_ready_owner_routes.py`
- `mechanics/questbook/scripts/validate_ready_owner_routes.py`
- `mechanics/questbook/scripts/validate_questbook_distillation.py`
- `mechanics/rpg/scripts/validate_rpg_distillation.py`
- `mechanics/rpg/parts/vocabulary-overlay/scripts/validate_vocabulary_overlay.py`
- `mechanics/boundary-bridge/scripts/validate_boundary_bridge_distillation.py`
- `mechanics/audit/scripts/validate_audit_distillation.py`
- `mechanics/release-support/scripts/validate_release_support_distillation.py`

Questbook part registry commands remain addressable from this map:

```text
python scripts/mechanics_topology/validate_mechanics_topology.py --mechanic questbook
python scripts/mechanics_topology/validate_mechanic_readme_cards.py --mechanic questbook
python mechanics/questbook/scripts/validate_questbook_lifecycle.py
python mechanics/questbook/scripts/build_questbook_index.py --check
python mechanics/questbook/scripts/validate_questbook_index.py
python mechanics/questbook/scripts/validate_questbook_source_contract.py
python mechanics/questbook/scripts/validate_quest_relations.py
python scripts/owner_requests/validate_owner_request_queue.py --mechanic questbook
python scripts/owner_requests/validate_owner_request_docs.py --mechanic questbook
python mechanics/questbook/scripts/build_ready_owner_routes.py --check
python mechanics/questbook/scripts/validate_ready_owner_routes.py
python scripts/owner_requests/validate_owner_request_queue.py --mechanic experience
python scripts/owner_requests/validate_owner_request_docs.py --mechanic experience
```

Shared hygiene and generated-freshness routes remain under
[Documentation and hygiene](#documentation-and-hygiene).
The shared ecosystem route remains under
[Center and registry lanes](#center-and-registry-lanes).
Shared owner-request queue routes remain under [Mechanics](#mechanics).

## Focused districts

The following owner routes are available when the named district changes:

```text
python scripts/stats/validate_local_stats_port.py
```

Shared link and Markdown-shape routes remain under
[Documentation and hygiene](#documentation-and-hygiene).

Use the nearest district validator and focused test module named by its source
registry. The broad test route is:

```text
python -m pytest -q
```

## Release landing

The complete ordinary branch, pull request, CI, merge, and post-landing sync
procedure is maintained in [`docs/RELEASING.md`](docs/RELEASING.md). This map
only exposes the local validation entrypoint; it does not grant push, PR,
merge, release, or owner-acceptance authority.
