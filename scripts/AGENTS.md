# AGENTS.md

This file applies to validator tooling under `scripts/`.

## Role of this directory

`scripts/` is the lightweight validation seam for the AoA center.

Current scripts include:

- `validate_ecosystem.py` for schema, registry, and center-level `QUESTBOOK` surface checks
- `validate_nested_agents.py` for required local directory guidance under `docs/`, `generated/`, `schemas/`, and `scripts/`
- `validate_candidate_lineage_contract.py` for the narrow cross-repo Growth Refinery example-chain witness

## Editing posture

Keep this script surface small, repo-relative, deterministic, and limited to the documented dependencies in `requirements-dev.txt`.

When changing script logic:

- prefer crisp failure messages over hidden magic
- keep checks anchored to public repository surfaces
- avoid network access, speculative repo discovery, or layer-owned validation that belongs elsewhere
- keep cross-repo checks witness-shaped: they may validate that owner examples line up, but they must not turn this center repo into a candidate ledger
- update the local `AGENTS.md` guidance when validator expectations change
- preserve Python 3.12 compatibility for the GitHub Actions path

If a validation rule becomes complicated enough to need a broader contract, encode that contract in docs or schema first.

## Validation

After changing validator logic, run:

```bash
python -m pip install -r requirements-dev.txt
python scripts/validate_ecosystem.py
```

A script change is done when the failure mode is clearer, not more mysterious.
