# Tests District

This directory holds regression tests for center contracts, generated surfaces, validators, and documentation guardrails.

Tests protect bounded claims. They do not replace proof canon in `aoa-evals` and do not grant authority beyond the claims they check.

## Use this directory when

- a generated surface changes
- a schema contract changes
- a validator changes
- an Agon or Experience center contract changes
- a release or root-surface guardrail needs regression protection

## Rules

- Pair tests with the smallest claim they protect.
- Do not turn tests into hidden source-of-truth prose.
- Keep test names close to the surface they guard.
- If a test encodes a constitutional rule, make sure the human-readable rule exists in `docs/` or root civic docs.
- Avoid broad snapshot tests that make intentional evolution hard to review.

## Baseline command

```bash
python -m pytest -q tests
```

Run targeted validators before or alongside pytest when a generated surface or schema changes.
