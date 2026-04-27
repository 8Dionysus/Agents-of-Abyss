# AGENTS.md

## Applies to

This card applies to `mechanics/boundary-bridge/parts/`.

## Role

Parts are the active operating routes for boundary-bridge work. They should
stay shorter and clearer than source doctrine.

## Boundaries

- Do not cite `legacy/raw/` directly.
- Use `../PROVENANCE.md` for source trace.
- Keep validation routed through `../AGENTS.md`.
- Keep owner-local truth outside AoA center.

## Validation

Use the package validator from the mechanic root:

```bash
python mechanics/boundary-bridge/scripts/validate_boundary_bridge_distillation.py
```

## Closeout

Name changed parts, owner boundaries touched, source doctrine consulted through
`../PROVENANCE.md`, and checks run.
