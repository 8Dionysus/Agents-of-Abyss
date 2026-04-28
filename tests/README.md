# Tests District

This directory holds regression tests for center contracts, generated surfaces, validators, and documentation guardrails.

Tests protect bounded claims. They do not replace proof canon in `aoa-evals` and do not grant authority beyond the claims they check.

Mechanic-owned tests live in `mechanics/<slug>/tests/`. Root `tests/` keeps
only root-owned contract tests.

## Use this directory when

- a generated surface changes
- a schema contract changes
- a root config registry or config consumer contract changes
- a validator changes
- a link, Markdown shape, status vocabulary, or generated freshness guardrail changes
- an AGENTS-card mesh, local card, or mesh index changes
- an Agon, Experience, RPG, antifragility, method-growth, or Questbook contract changes
- an Experience active part or provenance bridge changes
- a Questbook item changes lifecycle placement
- a release or root-surface guardrail needs regression protection

## Rules

- Pair tests with the smallest claim they protect.
- Do not turn tests into hidden source-of-truth prose.
- Keep test names close to the surface they guard.
- If a test encodes a constitutional rule, make sure the human-readable rule exists in `docs/` or root civic docs.
- Avoid broad snapshot tests that make intentional evolution hard to review.

## Baseline command

```bash
python -m pytest -q
```

Run targeted validators before or alongside pytest when a generated surface,
schema, or hygiene guardrail changes.

For Experience active-part or provenance-bridge changes, run:

```bash
python mechanics/experience/scripts/validate_experience_distillation.py
```

For link and shape hygiene changes, run:

```bash
python scripts/validate_config_registry.py
python scripts/validate_hygiene_suite.py
```

For AGENTS mesh changes, run:

```bash
python scripts/validate_agents_md_shape.py
python scripts/validate_agents_mesh.py
python scripts/build_agents_mesh_index.py --check
python scripts/validate_agents_mesh_index.py
```

For Questbook lifecycle changes, run:

```bash
python mechanics/questbook/scripts/validate_questbook_lifecycle.py
python mechanics/questbook/scripts/build_questbook_index.py --check
python mechanics/questbook/scripts/validate_questbook_index.py
```
