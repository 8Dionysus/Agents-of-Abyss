# AGENTS.md

## Applies to

This card applies to `mechanics/rpg/docs/` and all descendant compatibility route documents.

## Role

`mechanics/rpg/docs/` is now a compatibility route.
Active RPG doctrine lives in `mechanics/rpg/parts/`; historical raw sources live in `mechanics/rpg/legacy/raw/` and should be reached through `mechanics/rpg/PROVENANCE.md`.

## Read before editing

Read root `AGENTS.md`, `mechanics/AGENTS.md`, `mechanics/rpg/AGENTS.md`, `mechanics/rpg/README.md`, `mechanics/rpg/PARTS.md`, and the specific active part you are routing to.

## Boundaries

- Keep detailed doctrine in active parts, not in this compatibility directory.
- Do not create owner-local activation claims, runtime claims, proof verdicts, memory objects, role contracts, playbook choreography, KAG canon, or ToS-authored meaning here.
- Do not recreate `RPG_*.md` active sources here.
- If this directory needs to point at history, route through `mechanics/rpg/PROVENANCE.md`.

## Validation

Use the package validation lane in `mechanics/rpg/AGENTS.md`.
Run the owner-request block there when `mechanics/rpg/OWNER_REQUESTS.md` changes.

<!-- centralized-child-validation:start -->

### Centralized Child Validation

Executable validation commands from child docs live here. Child docs should route to this section instead of carrying command blocks.

#### `mechanics/rpg/OWNER_REQUESTS.md`

Use the RPG package AGENTS owner-request validation block.

<!-- centralized-child-validation:end -->

## Closeout

Report source docs changed, package README or registry updates needed, generated mirrors rebuilt or not rebuilt, owner-request status affected, and checks run or skipped.
