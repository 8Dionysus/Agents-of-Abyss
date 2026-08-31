# AGENTS.md

## Applies to

This card applies to `mechanics/rpg/parts/` and every nested part.

## Role

RPG parts are the active, concise working contracts for world grammar. They should tell an agent what the part owns, what it must not claim, and which owner route comes next.

## Read before editing


## Boundaries

- Do not pull detailed source inventories into part docs.
- Do not turn RPG labels into owner-local truth.
- Do not add executable validation commands outside VALIDATION.md surfaces or
  the source manifest.
- Keep technical artifacts inside the owning part.

## Validation

Run the RPG part lane after part changes:

For release-readiness, use the package route in the repository
[`VALIDATION.md`](../../../VALIDATION.md).

## Closeout

Closeout must name changed parts, whether provenance or owner requests changed, checks run, checks skipped, remaining risk, and the next owner route if the part only reflects another owner.
