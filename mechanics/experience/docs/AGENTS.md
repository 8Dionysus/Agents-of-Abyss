# AGENTS.md

## Applies to

This card applies to `mechanics/experience/docs/` compatibility surfaces.

## Role

This directory is now a compatibility route only. Active Experience direction lives in `../DIRECTION.md`, `../PARTS.md`, and `../parts/`; archival accounting is routed through `../PROVENANCE.md`.

## Read before editing

Read root `AGENTS.md`, `mechanics/AGENTS.md`, `mechanics/experience/AGENTS.md`, `../DIRECTION.md`, and `../PARTS.md` before editing this lane.

## Boundaries

Do not add new heavy doctrine here. Do not use this route to bypass active part contracts, owner requests, landing logs, or provenance accounting.

## Validation

Run:

```bash
python scripts/validate_experience_distillation.py
python scripts/validate_agents_md_shape.py
python scripts/validate_agents_mesh.py
```

## Closeout

Report compatibility-route changes, whether active parts or provenance accounting changed, and checks run or skipped.
