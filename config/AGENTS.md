# AGENTS.md

## Applies to

This card applies to `config/` and all descendants unless a nearer `AGENTS.md` narrows the path.

## Role

`config/` holds source configuration for validators, generated mirrors, hygiene suites, and repository guardrails.

## Read before editing

Read root `AGENTS.md`, then the relevant protocol doc for the config being changed.

Use the nearest README for local file purpose. Use source docs, schemas, generated builders, validators, and owner repos as stronger authority when they apply.

## Boundaries

- Config may drive checks; it must not silently become constitutional law.
- When config changes a contract, update the human protocol and generated mirror together.
- Do not loosen vocabularies, required surfaces, or generated freshness to avoid a failure.

## Validation

Run the narrowest relevant checks first. Usual checks for this district:

```bash
python scripts/validate_status_vocabulary.py
python scripts/validate_generated_freshness.py
python scripts/validate_agents_mesh.py
```

If a listed validator is not present in the checkout yet, report that explicitly and run the closest available guardrail.

## Closeout

Report changed files, source surfaces consulted, generated files rebuilt or not rebuilt, checks run, checks skipped, and any owner boundary that may need follow-up.
