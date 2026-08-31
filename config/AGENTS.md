# AGENTS.md

## Applies to

This card applies to `config/` and all descendants unless a nearer `AGENTS.md` narrows the path.

## Role

`config/` holds source configuration for validators, generated mirrors, hygiene suites, and repository guardrails.

`config/registry.json` is the source map for this district. It must list every
root `config/*.json` source, its consumer scripts, generated mirrors, and
validation route.

## Read before editing


## Boundaries

- Config may drive checks; it must not silently become constitutional law.
- When config changes a contract, update the human protocol and generated mirror together.
- Do not loosen vocabularies, required surfaces, or generated freshness to avoid a failure.
- Do not add unregistered root config JSON files.
- Keep mechanic-owned seed config under the owning mechanic or part, not here.

## Validation

Run the narrowest relevant checks first. Usual checks for this district:

For release-facing config changes, also run:

If a listed validator is not present in the checkout yet, report that explicitly and run the closest available guardrail.

## Closeout

Report changed files, source surfaces consulted, generated files rebuilt or not rebuilt, checks run, checks skipped, and any owner boundary that may need follow-up.
