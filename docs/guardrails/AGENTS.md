# AGENTS.md

## Applies to

This card applies to `docs/guardrails/` and all descendants unless a nearer `AGENTS.md` narrows the path.

## Role

`docs/guardrails/` owns docs-local classifier, hygiene, generated freshness, and AGENTS mesh guardrail surfaces.

## Read before editing

Read root `AGENTS.md`, then `docs/AGENTS.md`, then `docs/README.md`, then this directory `README.md`.

For classifier or cleanup work, also read `THEMATIC_DISTRICT_PROTOCOL.md`, `CURRENT_SURFACE_INDEX.md`, and `docs/guardrails/thematic_districts.json`.

For link, shape, status, or freshness work, read `LINK_AND_SHAPE_HYGIENE_PROTOCOL.md`, `HYGIENE_GUARDRAIL_INDEX.md`, and `../../config/link_shape_hygiene.json`.

For AGENTS mesh work, read `../../DESIGN.AGENTS.md`,
`AGENTS_MESH_PROTOCOL.md`, `AGENTS_MESH_INDEX.md`, and
`../../config/agents_mesh.json`.

For entry-surface validation work, read
`ENTRY_SURFACE_VALIDATION_BASELINE.md`, `../../scripts/center_entry/center_entry_map_common.py`,
and `../../scripts/center_entry/validate_entry_surface_sync.py`.

## Boundaries

- Guardrails verify route shape; they do not author doctrine, mechanic law, generated meaning, or sibling-repo truth.
- Do not recreate empty docs districts for mechanics. Route mechanic records to `mechanics/<slug>/legacy/` and active mechanic work to `mechanics/<slug>/`.
- Keep validation commands here or in the nearest `AGENTS.md`; keep README surfaces map-like.
- Generated mirrors remain evidence only and must be rebuilt from their source config.
- Do not add prose-only guardrails. A new guardrail family needs human law,
  source input, validator/test coverage, release-check coverage, and an owner
  boundary in the same change.

## Validation

For docs cleanup classifier or district changes:

```bash
python scripts/docs_districts/plan_docs_thematic_cleanup.py --check
python scripts/docs_districts/validate_docs_thematic_districts.py
python scripts/docs_districts/validate_docs_migration_map.py
python scripts/docs_districts/validate_traces_district.py
python scripts/docs_districts/build_docs_thematic_index.py --check
python scripts/docs_districts/validate_docs_thematic_index.py
```

For link, shape, status, and freshness guardrail changes:

```bash
python scripts/hygiene/repair_known_link_drifts.py --check
python scripts/hygiene/validate_links.py
python scripts/hygiene/validate_markdown_shape.py
python scripts/hygiene/validate_status_vocabulary.py
python scripts/hygiene/build_link_shape_hygiene_index.py --check
python scripts/hygiene/validate_link_shape_hygiene_index.py
python scripts/hygiene/validate_generated_freshness.py
python scripts/hygiene/validate_hygiene_suite.py
```

For AGENTS mesh changes:

```bash
python scripts/agents_mesh/validate_agents_md_shape.py
python scripts/agents_mesh/validate_agents_mesh.py
python scripts/agents_mesh/build_agents_mesh_index.py --check
python scripts/agents_mesh/validate_agents_mesh_index.py
```

For entry-surface validation changes:

```bash
python scripts/center_entry/validate_entry_surface_sync.py
python scripts/center_entry/build_center_entry_map.py --check
python scripts/center_entry/validate_center_entry_map.py
python -m pytest -q tests/test_entry_surface_sync.py tests/test_center_entry_map.py
```

## Closeout

Report changed guardrail surfaces, generated mirrors rebuilt or checked, commands run, commands skipped, remaining risk, and any owner route where a mechanic-specific record was sent.
