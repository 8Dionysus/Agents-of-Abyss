# AGENTS.md

## Applies to

This card applies to `generated/` and every nested path under that scope until a nearer `AGENTS.md` narrows the lane.

## Role

`generated/` holds root-published compact read models, route capsules, indexes, and summary surfaces. These files help low-context agents and validators move quickly while source surfaces keep meaning.

## Read before editing

Read root `AGENTS.md`, this card, `generated/README.md`, and the source surface named for the generated file.

For manual registry summaries, read the relevant schema and center prose before editing. For Questbook read models, read `mechanics/questbook/AGENTS.md` and rebuild with the Questbook builder.

## Boundaries

- Do not treat generated files as stronger than source docs, schemas, source registries, quest source files, validators, or owner repositories.
- Do not hand-edit generated files when a builder exists.
- Do not place mechanic part-local generated capsules in root `generated/`.
- Do not use root generated summaries to absorb sibling implementation truth or owner-local acceptance.
- Keep root-published Questbook generated files as read models over `quests/`, not quest authority.
- Keep manual published summaries compact, schema-aligned, and validated with the named validator.

## Editing posture

Use the surface table in `generated/README.md` before changing any file here.

Root-built surfaces:

- `center_entry_map.min.json`
- `mechanic_card_index.min.json`
- `owner_request_queue.min.json`
- `docs_thematic_index.min.json`
- `link_shape_hygiene.min.json`
- `agents_mesh.min.json`

Manual published summaries:

- `ecosystem_registry.min.json`
- `federation_supporting_inventory.min.json`

These summaries keep the machine-readable public contour and supporting
inventory aligned with `visibility`, `maturity`, relation, and kind axes. Treat
them as published summaries, not a hidden second charter.
Each one is a published summary surface, not a source charter.

Mechanic-built root-published Questbook read models:

- `questbook_index.min.json`
- `questbook_frontier.min.json`
- `questbook_relations.min.json`

When a generated file begins to carry new meaning, update the owner source surface first, then rebuild or validate the generated mirror.

## Validation

Run the narrow checks for the touched surface:

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
python mechanics/questbook/scripts/build_questbook_index.py --check
python mechanics/questbook/scripts/validate_questbook_index.py
python scripts/validate_generated_freshness.py
python scripts/validate_ecosystem.py
python -m pytest -q
```

Run `python scripts/release_check.py` when generated, route, schema, AGENTS, or release-facing surfaces change together.

## Closeout

Closeout must name changed generated surfaces, source surfaces consulted,
builders run or intentionally skipped, validators run, validators skipped,
remaining risk, and the next owner route when root `generated/` was only a
publication surface.
