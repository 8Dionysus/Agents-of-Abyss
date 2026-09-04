# AGENTS.md

## Applies to

This card applies to `quests/` and all descendants unless a nearer `AGENTS.md` narrows the path.

## Role

`quests/` holds the quest item store for public obligations, visible work items, and bounded follow-through records.

Lane-first lifecycle directories are the source placement. Top-level `AOA-Q-*` aliases and root lifecycle directories are intentionally absent; edit `quests/<lane>/<state>/AOA-Q-*` directly.

## Read before editing

Read the quest port contract and owner route only when lifecycle or placement changes.
## Boundaries

- Quests are not a second roadmap.
- Do not use quests as hidden memory or private task dumps.
- Do not assign owner-local commitments unless the owner repo accepts them.

## Validation

Run the narrowest relevant checks first. Usual checks for this district:

Use the direct route in the repository [`VALIDATION.md`](../VALIDATION.md); it
names the applicable manifest key and no-shell runner.

If a listed validator is not present in the checkout yet, report that explicitly and run the closest available guardrail.

## Closeout

Report changed files, source surfaces consulted, generated files rebuilt or not rebuilt, checks run, checks skipped, and any owner boundary that may need follow-up.
