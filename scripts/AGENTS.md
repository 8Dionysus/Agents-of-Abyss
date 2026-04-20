# AGENTS.md

This file applies to validation and builder tooling under `scripts/`.

## Role of this directory

`scripts/` is the lightweight validation seam for the AoA center.

Current scripts include:

- `validate_ecosystem.py` for schema, registry, and center-level `QUESTBOOK` surface checks
- `validate_nested_agents.py` for required local directory guidance under `docs/`, `generated/`, `schemas/`, and `scripts/`
- `validate_candidate_lineage_contract.py` for the narrow cross-repo Growth Refinery example-chain witness
- `validate_wave4_kernel_automation.py` for the reviewed wave 4 next-kernel and automation follow-through seam across sibling repos
- `agon_imposition_common.py` for the canonical Agon Wave 0 capsule payload,
  local-reference checks, and shared build/validate entrypoints
- `build_agon_imposition_readiness.py` for deterministic rebuild or stale-check
  of `generated/agon_imposition_readiness.min.json`
- `validate_agon_imposition_readiness.py` for the explicit Wave 0 readiness
  contract check
- `build_agon_lawful_move_registry.py` for deterministic rebuild or stale-check
  of `generated/agon_lawful_move_registry.min.json`
- `validate_agon_lawful_moves.py` for the explicit Wave III lawful move
  vocabulary contract check

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

After changing the Agon Wave 0 builder or validator, also run:

```bash
python scripts/build_agon_imposition_readiness.py --check
python scripts/validate_agon_imposition_readiness.py
python -m pytest -q tests/test_agon_imposition_readiness.py
```

After changing the Agon Wave III builder or validator, also run:

```bash
python scripts/build_agon_lawful_move_registry.py --check
python scripts/validate_agon_lawful_moves.py
python -m pytest -q tests/test_agon_lawful_moves.py
```

A script change is done when the failure mode is clearer, not more mysterious.
