# Entry Surface Validation Baseline

This guardrail surface names the baseline commands that center entry surfaces may
reference instead of repeating the full list inline.

## Role

The machine source for this command set is `scripts/center_entry/center_entry_map_common.py`.
`scripts/center_entry/validate_entry_surface_sync.py` verifies that this surface contains the
baseline commands and that entry surfaces either include those commands directly
or point here.

Use `scripts/release_gate/release_check.py` as the broad gate for release-facing or repo-wide
changes. The commands below stay visible so route surfaces remain inspectable
without turning every entry document into a validation catalog.

## Baseline commands

```bash
python scripts/hygiene/repair_known_link_drifts.py --check
python scripts/organ_contract/validate_organ_contract.py
python scripts/hygiene/validate_links.py
python scripts/hygiene/validate_markdown_shape.py
python scripts/hygiene/validate_status_vocabulary.py
python scripts/hygiene/build_link_shape_hygiene_index.py --check
python scripts/hygiene/validate_link_shape_hygiene_index.py
python scripts/agents_mesh/validate_agents_md_shape.py
python scripts/agents_mesh/validate_agents_mesh.py
python scripts/agents_mesh/build_agents_mesh_index.py --check
python scripts/agents_mesh/validate_agents_mesh_index.py
python scripts/center_entry/validate_entry_surface_sync.py
python scripts/center_entry/build_center_entry_map.py --check
python scripts/center_entry/validate_center_entry_map.py
python scripts/mechanics_topology/validate_mechanics_topology.py
python scripts/mechanics_topology/validate_mechanic_landing_logs.py
python scripts/hygiene/validate_generated_freshness.py
python scripts/hygiene/validate_hygiene_suite.py
python scripts/root_registries/validate_ecosystem.py
python -m pytest -q
```

## Boundary

This baseline does not replace local validators. It gives entry surfaces a compact
way to point to the current center-wide command set while local `AGENTS.md` cards
continue to own lane-specific checks.
