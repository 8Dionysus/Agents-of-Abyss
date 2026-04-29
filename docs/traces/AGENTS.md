# AGENTS.md

## Applies to

This card applies to `docs/traces/` and all descendants unless a nearer `AGENTS.md` narrows the path.

## Role

`docs/traces/` holds repo-level movement receipts: migration manifests,
conflict records, generic apply-script output, and link-repair traces.

Traces explain how a repository surface moved or was repaired. They do not
decide what the moved material means.

## Read before editing

Read root `AGENTS.md`, then `docs/AGENTS.md`, then `docs/README.md`. If this district is affected by
docs thematic cleanup, also read `docs/guardrails/THEMATIC_DISTRICT_PROTOCOL.md` and
`docs/guardrails/CURRENT_SURFACE_INDEX.md` when present.

## Boundaries

- Do not treat this district as stronger than its source surfaces.
- Traces are receipts; do not handwave them into current authority.
- Keep provenance, dates, and source relationships explicit.
- Route current mechanic doctrine to `mechanics/<slug>/` packages when a package owns the material.
- Route mechanic-specific source traces to `mechanics/<slug>/legacy/raw/`
  through that mechanic's `PROVENANCE.md` or `LANDING_LOG.md`.
- Route audit evidence to `mechanics/audit/`.
- Route decision rationale to `docs/decisions/`.
- Route owner-local truth to the owner repository instead of expanding the center.

Do not create `docs/traces/` in another repository until that repository has
real movement receipts to preserve. No empty trace doors.

## Post-change route review

After adding, moving, or deleting a trace:

1. identify whether the receipt is generic repo movement or mechanic-owned history;
2. update `README.md` so every active trace file is indexed;
3. keep generated, guardrail, and mechanic routes aligned when the source action changed them;
4. run the trace validator and the docs guardrail validators.

## Validation

Use docs and hygiene guardrails:

```bash
python scripts/validate_traces_district.py
python scripts/validate_agents_md_shape.py
python scripts/validate_agents_mesh.py
python scripts/validate_links.py
python scripts/validate_markdown_shape.py
python -m pytest -q
```

If thematic district indexes or migration maps changed, run their matching builders and validators too.

## Closeout

Report the trace type, source action, owner route, whether the file is current
law, receipt, trace, audit evidence, or legacy route, and which links,
validators, or generated mirrors were checked.
