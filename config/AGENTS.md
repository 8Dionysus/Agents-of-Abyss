# AGENTS.md

## Applies to

This card applies to `config/` and all descendants unless a nearer `AGENTS.md` narrows the path.

## Role

`config/` holds source configuration for validators, generated mirrors, hygiene suites, and repository guardrails.

`config/registry.json` is the source map for this district. It must list every
root `config/*.json` source, its consumer scripts, generated mirrors, and
validation route.

## Read before editing

Read root `AGENTS.md`, then the relevant protocol doc for the config being changed.

Use the nearest README for local file purpose. Use source docs, schemas, generated builders, validators, and owner repos as stronger authority when they apply.

## Boundaries

- Config may drive checks; it must not silently become constitutional law.
- When config changes a contract, update the human protocol and generated mirror together.
- Do not loosen vocabularies, required surfaces, or generated freshness to avoid a failure.
- Do not add unregistered root config JSON files.
- Keep mechanic-owned seed config under the owning mechanic or part, not here.

## Validation

Run the narrowest relevant checks first. Usual checks for this district:

```bash
python scripts/validate_config_registry.py
python scripts/validate_hygiene_suite.py
python scripts/validate_status_vocabulary.py
python scripts/validate_generated_freshness.py
python scripts/validate_agents_md_shape.py
python scripts/validate_agents_mesh.py
python scripts/build_agents_mesh_index.py --check
python scripts/validate_agents_mesh_index.py
```

For release-facing config changes, also run:

```bash
python scripts/release_check.py
```

If a listed validator is not present in the checkout yet, report that explicitly and run the closest available guardrail.

## Closeout

Report changed files, source surfaces consulted, generated files rebuilt or not rebuilt, checks run, checks skipped, and any owner boundary that may need follow-up.
