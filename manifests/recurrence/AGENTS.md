# AGENTS.md

## Applies to

This card applies to `manifests/recurrence/` and all descendant recurrence manifest records.

## Role

`manifests/recurrence/` stores structured recurrence and return-related receipts. It supports bounded continuity review without claiming ambient memory, runtime self-healing, or hidden autonomy.

## Read before editing

Read root `AGENTS.md`, `manifests/AGENTS.md`, `mechanics/recurrence/AGENTS.md`, and `mechanics/recurrence/docs/RECURRENCE_PRINCIPLE.md` when present.

## Boundaries

- A recurrence manifest is a receipt, not a memory sovereign.
- Do not claim runtime continuity, automatic repair, or hidden state.
- Keep provenance, source surfaces, and validation references explicit.

## Validation

Run recurrence and manifest checks:

```bash
python scripts/validate_agents_md_shape.py
python scripts/validate_agents_mesh.py
python scripts/validate_links.py
python scripts/validate_mechanics_topology.py
python -m pytest -q
```

## Closeout

Report manifest records changed, recurrence source surfaces consulted, generated mirrors rebuilt or not rebuilt, and checks run or skipped.
