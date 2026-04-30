# AGENTS.md

## Applies to

This card applies to `mechanics/agon/parts/recurrence-adapter/manifests/` and
all descendant manifest records.

## Role

This directory owns Agon recurrence component receipts and review-only hook
binding receipts for the recurrence adapter part.

## Read before editing

Read root `AGENTS.md`, `mechanics/agon/parts/AGENTS.md`,
`mechanics/agon/parts/recurrence-adapter/README.md`, local `README.md`, and
`manifests/registry.json`.

## Boundaries

- Component receipts and hook receipts move as pairs.
- Hook records emit review pressure, owner dossiers, or observation candidates.
- Do not use recurrence manifests as memory sovereignty, runtime continuity,
  automatic repair, verdict authority, rank mutation, or ToS meaning.
- Owner-requested manifest names stay request names until the target owner lands
  them.

## Validation

```bash
python mechanics/agon/parts/recurrence-adapter/scripts/validate_agon_recurrence_manifests.py
python mechanics/agon/parts/recurrence-adapter/scripts/validate_agon_recurrence_adapter_request.py
python -m pytest -q mechanics/agon/parts/recurrence-adapter/tests/test_agon_recurrence_manifests.py
```

## Closeout

Report manifest records changed, source surfaces consulted, generated adapter
request rebuilt or intentionally left untouched, checks run or skipped, and
owner-local manifest requests that remain open.
