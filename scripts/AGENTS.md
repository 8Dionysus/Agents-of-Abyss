# AGENTS.md

This file applies to validator tooling under `scripts/`.

## Role of this directory

`scripts/` is the lightweight validation seam for the AoA center.

Current scripts include:

- `validate_ecosystem.py` for schema and registry integrity checks
- `validate_nested_agents.py` for required local directory guidance under `docs/`, `generated/`, `schemas/`, and `scripts/`

## Editing posture

Keep this script surface small, zero-dependency, repo-relative, and deterministic.

When changing script logic:

- prefer crisp failure messages over hidden magic
- keep checks anchored to public repository surfaces
- avoid network access, speculative repo discovery, or layer-owned validation that belongs elsewhere
- update the local `AGENTS.md` guidance when validator expectations change
- preserve Python 3.12 compatibility for the GitHub Actions path

If a validation rule becomes complicated enough to need a broader contract, encode that contract in docs or schema first.

## Validation

After changing validator logic, run:

```bash
python scripts/validate_ecosystem.py
```

A script change is done when the failure mode is clearer, not more mysterious.
