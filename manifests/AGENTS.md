# AGENTS.md

## Applies to

This card applies to `manifests/` and all descendants unless a nearer `AGENTS.md` narrows the path.

## Role

`manifests/` holds structured manifests, seed receipts, recurrence records, and other reviewable machine-readable traces.

## Read before editing

Read root `AGENTS.md`, local README, and the schema or protocol tied to the manifest.

Use the nearest README for local file purpose. Use source docs, schemas, generated builders, validators, and owner repos as stronger authority when they apply.

## Boundaries

- Manifests preserve traceability; they do not replace source docs or owner acceptance.
- Do not promote a receipt into current law without a source surface.
- Keep identifiers stable and provenance explicit.

## Validation

Run the narrowest relevant checks first. Usual checks for this district:

```bash
python scripts/validate_links.py
python scripts/validate_generated_freshness.py
python -m pytest -q tests
```

If a listed validator is not present in the checkout yet, report that explicitly and run the closest available guardrail.

## Closeout

Report changed files, source surfaces consulted, generated files rebuilt or not rebuilt, checks run, checks skipped, and any owner boundary that may need follow-up.
