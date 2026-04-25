# AGENTS.md

## Applies to

This card applies to `tests/` and all descendants unless a nearer `AGENTS.md` narrows the path.

## Role

`tests/` holds regression tests, contract tests, and fixtures that guard route, shape, generated freshness, mechanics topology, and ecosystem claims.
Mechanic-owned tests live under `mechanics/<slug>/tests/`; root entries for
those lanes are compatibility aliases for stable pytest commands.

## Read before editing

Read root `AGENTS.md`, `tests/README.md`, and the validator or source surface under test.

Use the nearest README for local file purpose. Use source docs, schemas, generated builders, validators, and owner repos as stronger authority when they apply.

## Boundaries

- Tests guard contracts; they do not author meaning by themselves.
- Do not delete failing assertions without updating the source contract they protect.
- Keep fixtures compact and clearly non-authoritative.
- Follow mechanic-owned aliases into `mechanics/<slug>/tests/` before editing.

## Validation

Run the narrowest relevant checks first. Usual checks for this district:

```bash
python -m pytest -q tests
python scripts/validate_agents_mesh.py
```

If a listed validator is not present in the checkout yet, report that explicitly and run the closest available guardrail.

## Closeout

Report changed files, source surfaces consulted, generated files rebuilt or not rebuilt, checks run, checks skipped, and any owner boundary that may need follow-up.
