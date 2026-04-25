# Generated District

This directory holds compact machine-facing surfaces built from stronger source documents.

Generated files help low-context agents, validators, and local tooling orient quickly. They are not the primary source of meaning.

Mechanic-owned generated companions live in `mechanics/<slug>/generated/`.
Root generated paths may remain as compatibility aliases for established
commands and public references.

## Current role

| Surface family | Role |
|---|---|
| `center_entry_map.min.json` | compact center-entry map for low-context orientation |
| `ecosystem_registry.min.json` | compact public AoA contour registry |
| `federation_supporting_inventory.min.json` | supporting consumers and adjacent support surfaces outside compact registry v1 |
| `mechanic_card_index.min.json` | compact reflection of mechanic package entry cards |
| `owner_request_queue.min.json` | compact center-side owner request queue |
| `docs_thematic_index.min.json` | compact map of docs thematic districts |
| `link_shape_hygiene.min.json` | compact mirror of Wave E hygiene guardrails |
| `agents_mesh.min.json` | compact mirror of Wave F AGENTS-card coverage |
| mechanic aliases | generated companions such as `agon_*.min.json` or `dual_vocabulary_overlay.json` routed to mechanic homes |

## Rules

- Do not hand-edit generated files when a builder exists.
- Do not cite generated files as stronger than source docs.
- Regenerate and validate together.
- Keep generated files compact and machine-readable.
- If a generated surface begins to carry new meaning, move that meaning back into the owner source document.

## Baseline checks

```bash
python scripts/build_center_entry_map.py --check
python scripts/validate_center_entry_map.py
python scripts/build_mechanic_card_index.py --check
python scripts/validate_mechanic_card_index.py
python scripts/build_owner_request_queue.py --check
python scripts/validate_generated_owner_request_queue.py
python scripts/build_docs_thematic_index.py --check
python scripts/validate_docs_thematic_index.py
python scripts/build_link_shape_hygiene_index.py --check
python scripts/validate_link_shape_hygiene_index.py
python scripts/build_agents_mesh_index.py --check
python scripts/validate_agents_mesh_index.py
python scripts/validate_agents_mesh.py
python scripts/validate_agents_md_shape.py
python scripts/validate_generated_freshness.py
python scripts/validate_ecosystem.py
```

Run the matching Agon, Experience, or registry validator for touched generated surfaces.
