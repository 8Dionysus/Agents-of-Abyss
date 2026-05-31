# Decision Note: Root Design Surface

- Decision ID: AOA-CENTER-D-0025

## Status

Accepted.

## Index Metadata

- Original date: 2026-05-06
- Surface classes: center doctrine, root surface
- Center facets: design surface
- Mechanic parents: none
- Guard families: center route law
- Posture: accepted rationale

## Context

AoA needed a durable place to name the system form it should preserve while it
grows toward OS Abyss. The candidate `DESIGN.md` describes shape, appearance,
anatomy, operation, and design principles for the center without replacing the
charter, roadmap, ecosystem map, federation rules, or agent editing law.

The placement question mattered because root files in `Agents-of-Abyss` are
civic surfaces, not a warehouse for every important note.

## Options considered

1. Keep the design text outside the repository as local source material.
2. Place the design text under `docs/` as a secondary doctrine note.
3. Land `DESIGN.md` at repository root as a civic system-form surface and wire
   it into first-reading and root-surface law.

## Decision

`DESIGN.md` is a root civic law and public-map surface for AoA system form.

The canonical first-reading route includes it after `CHARTER.md` and before
`ECOSYSTEM_MAP.md` so readers understand both authority and intended form
before reading the public federation contour.

## Rationale

Root placement is justified because the design surface answers a durable center
question: what shape AoA should preserve as it grows. It helps humans and
agents make safer root, route, generated-companion, and OS Abyss posture
changes without forcing that shape into the charter or roadmap.

Keeping it at root also prevents the design surface from being mistaken for a
mechanic receipt, docs-root note, or owner-local implementation plan.

## Consequences

- New readers get a clearer route from authority to system form to federation
  map.
- Root-editing and route changes now need to check whether the proposed shape
  still matches `DESIGN.md`.
- `DESIGN.md` must stay compact and must not absorb roadmap promises, runtime
  implementation, mechanic-local doctrine, or sibling owner truth.
- Generated entry capsules and tests must stay aligned with the new
  first-reading path.

## Source surfaces

- `DESIGN.md`
- `README.md`
- `AGENTS.md`
- `CHARTER.md`
- `ECOSYSTEM_MAP.md`
- `ROADMAP.md`
- `docs/ROOT_SURFACE_LAW.md`
- `docs/START_HERE_ROUTE_CONTRACT.md`
- `scripts/center_entry_map_common.py`
- `generated/center_entry_map.min.json`
- `tests/test_center_entry_map.py`

## Follow-up route

Revisit this decision if `DESIGN.md` starts duplicating charter authority,
roadmap direction, mechanic doctrine, or owner-local implementation truth.
