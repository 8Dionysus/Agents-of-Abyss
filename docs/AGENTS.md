# AGENTS.md

## Applies to

This card applies to `docs/` and every nested path under that scope until a nearer `AGENTS.md` narrows the lane.

## Role

`docs/` is the center doctrine, route-law, and map surface for Agents-of-Abyss.

It keeps the federation legible without absorbing mechanic truth, sibling-repo truth, generated truth, runtime truth, or Tree-of-Sophia authored meaning.

## Read before editing

Read the repository root `AGENTS.md`, this card, and the nearest `README.md` or protocol surface before changing files in this lane.

For root or docs placement work, read `ROOT_SURFACE_LAW.md`, `README.md`, and `guardrails/README.md`.

For mechanic work, leave this lane and read `../mechanics/AGENTS.md` plus the nearest `../mechanics/<slug>/AGENTS.md`.

## Boundaries

- Do not use `docs/` to override owner-local truth, generated-source boundaries, sibling-repo authority, or release validation contracts.
- Keep flat `docs/` files limited to current center doctrine, current route law, owner maps, and compatibility routes.
- Put docs guardrail law under `guardrails/`.
- Put audit evidence in `../mechanics/audit/`, put decisions and traces in their named districts, and land registry contract changes through schemas, generated capsules, validators, and source docs together.
- Put mechanic receipts and mechanic legacy under `../mechanics/<slug>/legacy/`, not under empty `docs/<slug>/` doors.

## Role of this directory

Important current docs-root surfaces:

- `README.md` maps the docs surface for humans and agents.
- `FEDERATION_RULES.md` keeps source-of-truth boundaries explicit.
- `LAYERS.md` maps layer ownership without becoming a mechanic catalog.
- `REPO_ROLES.md` gives compact repository routing.
- `ROOT_SURFACE_LAW.md` governs root and docs-root placement.
- `START_HERE_ROUTE_CONTRACT.md` governs public entry route modes.
- `MECHANICS.md` is a compatibility route to `../mechanics/README.md`.

Guardrail surfaces live in `guardrails/`:

- `guardrails/THEMATIC_DISTRICT_PROTOCOL.md`
- `guardrails/CURRENT_SURFACE_INDEX.md`
- `guardrails/thematic_districts.json`
- `guardrails/LINK_AND_SHAPE_HYGIENE_PROTOCOL.md`
- `guardrails/HYGIENE_GUARDRAIL_INDEX.md`
- `guardrails/AGENTS_MESH_PROTOCOL.md`
- `guardrails/AGENTS_MESH_INDEX.md`

## Editing posture

Keep docs compact, declarative, and routing-aware.

When editing:

- prefer boundaries, roles, and relationships over implementation detail
- route readers to neighboring AoA repositories instead of restating their internals
- keep AoA versus `Tree-of-Sophia` ownership boundaries explicit
- update related center-layer documents coherently when terminology or doctrine changes
- keep README surfaces map-like and keep validation command lists in `AGENTS.md`

Do not let this directory become a shadow corpus for techniques, skills, evals, memory objects, runtime configs, mechanic packets, or ToS-authored meaning.

## Decision review

When a docs change chooses a durable route, owner split, placement law,
validator authority, workflow expectation, or public contract, review whether
`decisions/` needs a decision record. Use `decisions/AGENTS.md` for the record
shape. If no record is needed, say so in closeout.

## Validation

For docs-root or guardrail topology changes:

```bash
python scripts/plan_docs_thematic_cleanup.py --check
python scripts/validate_docs_thematic_districts.py
python scripts/validate_docs_migration_map.py
python scripts/validate_traces_district.py
python scripts/validate_decision_records.py
python scripts/build_docs_thematic_index.py --check
python scripts/validate_docs_thematic_index.py
python scripts/repair_known_link_drifts.py --check
python scripts/validate_links.py
python scripts/validate_markdown_shape.py
python scripts/validate_status_vocabulary.py
python scripts/build_link_shape_hygiene_index.py --check
python scripts/validate_link_shape_hygiene_index.py
python scripts/validate_agents_md_shape.py
python scripts/validate_agents_mesh.py
python scripts/build_agents_mesh_index.py --check
python scripts/validate_agents_mesh_index.py
python scripts/validate_generated_freshness.py
python scripts/validate_hygiene_suite.py
```

If center route contracts, generated maps, or public claims changed, also run:

```bash
python scripts/validate_entry_surface_sync.py
python scripts/build_center_entry_map.py --check
python scripts/validate_center_entry_map.py
python scripts/validate_mechanics_topology.py
python scripts/validate_mechanic_landing_logs.py
python scripts/validate_ecosystem.py
python -m pytest -q
```

Use the owning mechanic `AGENTS.md` for mechanic-specific validators.

## Closeout

Closeout must name changed surfaces, owner routes affected, checks run, checks skipped, remaining risk, and the next owner route if this lane was only a waypoint.
