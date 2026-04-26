# AGENTS.md

## Applies to

This card applies to `mechanics/rpg/parts/` and every nested part.

## Role

RPG parts are the active, concise working contracts for world grammar. They should tell an agent what the part owns, what it must not claim, and which owner route comes next.

## Read before editing

Read `mechanics/rpg/AGENTS.md`, `mechanics/rpg/DIRECTION.md`, `mechanics/rpg/PARTS.md`, and the local part `README.md` before changing a part.

## Boundaries

- Do not pull detailed source inventories into part docs.
- Do not turn RPG labels into owner-local truth.
- Do not add executable validation commands outside AGENTS surfaces.
- Keep technical artifacts inside the owning part.

## Validation

Run the RPG part lane after part changes:

```bash
python mechanics/rpg/scripts/validate_rpg_distillation.py
python mechanics/rpg/parts/vocabulary-overlay/scripts/validate_vocabulary_overlay.py
python -m pytest -q mechanics/rpg/tests mechanics/rpg/parts/vocabulary-overlay/tests
```

For release-readiness, use the package validation lane in `mechanics/rpg/AGENTS.md`.

## Closeout

Closeout must name changed parts, whether provenance or owner requests changed, checks run, checks skipped, remaining risk, and the next owner route if the part only reflects another owner.
