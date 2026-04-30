# AGENTS.md

## Applies to

This card applies to `tests/` and all descendants unless a nearer `AGENTS.md`
narrows the path.

## Role

`tests/` holds root-owned regression tests, contract tests, and compact
fixtures for center routes, root districts, generated surfaces, mechanics
topology, hygiene, and ecosystem claims.

## Read before editing

Read root `AGENTS.md`, local `README.md`, `tests/registry.json`, and the source
surface named by the relevant registry family.

Use mechanic package guidance for tests under `mechanics/<slug>/tests/` or
`mechanics/<slug>/parts/<part>/tests/`.
Use `Spark/AGENTS.md` for tests under `Spark/tests/`.

## Boundaries

- Root `tests/` owns root-owned center tests.
- Mechanic-owned tests belong with the owning mechanic or part.
- Tests guard contracts; they do not author meaning by themselves.
- Do not delete failing assertions without updating the source contract they
  protect.
- Keep fixtures compact and clearly non-authoritative.
- If a test encodes a constitutional rule, make sure the human-readable rule
  exists in `docs/`, `mechanics/`, or root civic docs.

## Validation

Run the narrowest relevant checks first. Usual checks for this district:

```bash
python scripts/validate_tests_district.py
python -m pytest -q tests/test_tests_district.py
python -m pytest -q
```

For release-facing test changes, also run:

```bash
python scripts/release_check.py
```

## Closeout

Report test registry entries changed, root tests touched, source surfaces
consulted, generated files rebuilt or intentionally left untouched, checks run,
checks skipped, and the owner route when a test belongs outside root.
