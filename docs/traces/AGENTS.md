# AGENTS.md

## Applies to

This card applies to `docs/traces/` and all descendants unless a nearer `AGENTS.md` narrows the path.

## Role

`docs/traces/` holds migration manifests, conflict records, provenance trails, and apply-script output.

## Read before editing

Read root `AGENTS.md`, then `docs/AGENTS.md`, then `docs/README.md`. If this district is affected by
docs thematic cleanup, also read `docs/guardrails/THEMATIC_DISTRICT_PROTOCOL.md` and
`docs/guardrails/CURRENT_SURFACE_INDEX.md` when present.

## Boundaries

- Do not treat this district as stronger than its source surfaces.
- Traces are receipts; do not handwave them into current authority.
- Keep provenance, dates, and source relationships explicit.
- Route current mechanic doctrine to `mechanics/<slug>/` packages when a package owns the material.
- Route owner-local truth to the owner repository instead of expanding the center.

## Validation

Use docs and hygiene guardrails:

```bash
python scripts/validate_agents_md_shape.py
python scripts/validate_agents_mesh.py
python scripts/validate_links.py
python scripts/validate_markdown_shape.py
python -m pytest -q
```

If thematic district indexes or migration maps changed, run their matching builders and validators too.

## Closeout

Report what moved or changed, whether the file is current law, receipt, trace, audit evidence, or legacy route, and which links or generated mirrors were checked.
