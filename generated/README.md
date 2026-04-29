# Generated District

This directory holds compact machine-facing surfaces built from stronger source documents.

Generated files help low-context agents, validators, and local tooling orient quickly. Source docs, source registries, source quest files, schemas, builders, validators, and owner repositories keep authority.

Root `generated/` contains root-published compact mirrors and indexes. Mechanic-local generated companions live under the owning mechanic package.

## Surface Classes

| Class | Meaning |
|---|---|
| Root-built | Built by a root `scripts/build_*` command from root-owned or mechanics registry sources. |
| Manual published summary | Tracked JSON summary validated against source docs and schemas, with no builder yet. |
| Mechanic-built root-published | Built by a mechanic script but published in root `generated/` because the read model summarizes a root source store or public root index. |

## Current Surfaces

| Surface | Class | Source | Builder | Validator |
|---|---|---|---|---|
| [`center_entry_map.min.json`](center_entry_map.min.json) | Root-built | `docs/START_HERE_ROUTE_CONTRACT.md` | `scripts/build_center_entry_map.py` | `scripts/validate_center_entry_map.py` |
| [`ecosystem_registry.min.json`](ecosystem_registry.min.json) | Manual published summary | `README.md`, `CHARTER.md`, `ECOSYSTEM_MAP.md`, `docs/LAYERS.md`, `docs/FEDERATION_RULES.md` | manual, no builder | `scripts/validate_ecosystem.py` |
| [`federation_supporting_inventory.min.json`](federation_supporting_inventory.min.json) | Manual published summary | ecosystem support posture and supporting-inventory schema | manual, no builder | `scripts/validate_ecosystem.py` |
| [`mechanic_card_index.min.json`](mechanic_card_index.min.json) | Root-built | `mechanics/registry.json`, mechanic package README cards | `scripts/build_mechanic_card_index.py` | `scripts/validate_mechanic_card_index.py` |
| [`owner_request_queue.min.json`](owner_request_queue.min.json) | Root-built | `mechanics/owner-request-queue.json`, owner request docs | `scripts/build_owner_request_queue.py` | `scripts/validate_generated_owner_request_queue.py` |
| [`docs_thematic_index.min.json`](docs_thematic_index.min.json) | Root-built | `docs/guardrails/thematic_districts.json` | `scripts/build_docs_thematic_index.py` | `scripts/validate_docs_thematic_index.py` |
| [`link_shape_hygiene.min.json`](link_shape_hygiene.min.json) | Root-built | `config/link_shape_hygiene.json` | `scripts/build_link_shape_hygiene_index.py` | `scripts/validate_link_shape_hygiene_index.py` |
| [`agents_mesh.min.json`](agents_mesh.min.json) | Root-built | `config/agents_mesh.json` and registered `AGENTS.md` cards | `scripts/build_agents_mesh_index.py` | `scripts/validate_agents_mesh_index.py` |
| [`questbook_index.min.json`](questbook_index.min.json) | Mechanic-built root-published | `quests/` lane-first source files | `mechanics/questbook/scripts/build_questbook_index.py` | `mechanics/questbook/scripts/validate_questbook_index.py` |
| [`questbook_frontier.min.json`](questbook_frontier.min.json) | Mechanic-built root-published | `generated/questbook_index.min.json` | `mechanics/questbook/scripts/build_questbook_index.py` | `mechanics/questbook/scripts/validate_questbook_index.py` |
| [`questbook_relations.min.json`](questbook_relations.min.json) | Mechanic-built root-published | `generated/questbook_index.min.json` and source quest relations | `mechanics/questbook/scripts/build_questbook_index.py` | `mechanics/questbook/scripts/validate_questbook_index.py` |

## Placement

Use root `generated/` for compact read models that are published by the AoA center or summarize a root source store.

Use mechanic-local `generated/` directories when a generated file serves one mechanic part or package. Use the owning sibling repository when a generated file summarizes sibling-owned implementation truth.

## Edit Posture

- Rebuild generated files when a builder exists.
- Validate manual published summaries against their schema and source docs.
- Keep root-published Questbook read models aligned with the Questbook builder and the root `quests/` source store.
- Move new meaning back to the owner source surface before regenerating.
- Use [AGENTS.md#validation](AGENTS.md#validation) for the current command lane.
