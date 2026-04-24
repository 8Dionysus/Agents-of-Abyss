# Generated District

This directory holds compact machine-facing surfaces built from stronger source documents.

Generated files help low-context agents, validators, and local tooling orient quickly. They are not the primary source of meaning.

## Current role

| Surface family | Role |
|---|---|
| `center_entry_map.min.json` | compact center-entry map for low-context orientation |
| `ecosystem_registry.min.json` | compact public AoA contour registry |
| `federation_supporting_inventory.min.json` | supporting consumers and adjacent support surfaces outside compact registry v1 |
| `agon_*.min.json` | generated Agon pre-protocol or candidate registry surfaces |
| `dual_vocabulary_overlay.json` | derived vocabulary overlay surface |

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
python scripts/validate_ecosystem.py
```

Run the matching Agon, Experience, or registry validator for touched generated surfaces.
