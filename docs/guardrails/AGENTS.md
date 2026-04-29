# AGENTS.md

## Applies to

This card applies to `docs/guardrails/` and all descendants unless a nearer `AGENTS.md` narrows the path.

## Role

`docs/guardrails/` owns docs-local classifier, hygiene, generated freshness, and AGENTS mesh guardrail surfaces.

## Read before editing

Read root `AGENTS.md`, then `docs/AGENTS.md`, then `docs/README.md`, then this directory `README.md`.

For classifier or cleanup work, also read `THEMATIC_DISTRICT_PROTOCOL.md`, `CURRENT_SURFACE_INDEX.md`, and `docs/guardrails/thematic_districts.json`.

For link, shape, status, or freshness work, read `LINK_AND_SHAPE_HYGIENE_PROTOCOL.md`, `HYGIENE_GUARDRAIL_INDEX.md`, and `../../config/link_shape_hygiene.json`.

For AGENTS mesh work, read `AGENTS_MESH_PROTOCOL.md`, `AGENTS_MESH_INDEX.md`, and `../../config/agents_mesh.json`.

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
python scripts/plan_docs_thematic_cleanup.py --check
python scripts/validate_docs_thematic_districts.py
python scripts/validate_docs_migration_map.py
python scripts/build_docs_thematic_index.py --check
python scripts/validate_docs_thematic_index.py
```

For link, shape, status, and freshness guardrail changes:

```bash
python scripts/repair_known_link_drifts.py --check
python scripts/validate_links.py
python scripts/validate_markdown_shape.py
python scripts/validate_status_vocabulary.py
python scripts/build_link_shape_hygiene_index.py --check
python scripts/validate_link_shape_hygiene_index.py
python scripts/validate_generated_freshness.py
python scripts/validate_hygiene_suite.py
```

For AGENTS mesh changes:

```bash
python scripts/validate_agents_md_shape.py
python scripts/validate_agents_mesh.py
python scripts/build_agents_mesh_index.py --check
python scripts/validate_agents_mesh_index.py
```

## Closeout

Report changed guardrail surfaces, generated mirrors rebuilt or checked, commands run, commands skipped, remaining risk, and any owner route where a mechanic-specific record was sent.
