# Decision Note: Root Roadmap Uses Horizon Direction

Status: accepted
Date: 2026-04-30

## Context

`ROADMAP.md` had accumulated phase, release-contour, mechanic, and future-work
detail in one root surface. That made it too easy for future agents to treat
root roadmap history as a replacement for mechanic-local roadmaps, landing
logs, changelog history, quests, or owner-repository direction.

The center still needs a program-level direction surface, but the mechanics
tree now owns local future pressure and landing ledgers.

## Options considered

1. Keep phase-numbered root roadmap sections and trim them occasionally.
2. Turn root `ROADMAP.md` into a link-only index to mechanic roadmaps.
3. Make root `ROADMAP.md` a horizon-based center direction surface with explicit
   update rules and route splits.

## Decision

Root `ROADMAP.md` uses named horizons for center-wide direction and keeps
mechanic-local future work, checked landings, release history, durable
obligations, and sibling implementation direction in their stronger owning
surfaces.

Route-law surfaces now treat `direction-change` as a change to center-wide
roadmap direction, horizon posture, maturity posture, owner-route pressure,
future triggers, registry or entry contour, release-support direction, or
public release contour.

## Rationale

Named horizons are easier to keep current than numbered phases once the repo has
many mechanics with their own roadmaps. They preserve the root's center-wide
direction role without pulling Agon, Experience, recurrence, release-support, or
future owner-repository work back into one large document.

Explicit update rules also give future agents a clear closeout question: did the
change move the center, or did it only land a local surface?

## Consequences

- Root roadmap stays shorter and more durable as mechanics grow.
- Mechanic `ROADMAP.md` and `LANDING_LOG.md` files carry more responsibility.
- Tests now check the route split instead of requiring mechanic detail in root.
- Future root direction changes must update entry route surfaces and generated
  route capsules together.

## Source surfaces

- `ROADMAP.md`
- `AGENTS.md`
- `README.md`
- `docs/START_HERE_ROUTE_CONTRACT.md`
- `scripts/center_entry_map_common.py`
- `generated/center_entry_map.min.json`
- `tests/test_roadmap_parity.py`
- `tests/test_docs_verify_routes.py`

## Follow-up route

Revisit this decision only if root `ROADMAP.md` becomes too thin to guide
program direction or too broad to stay distinct from mechanic-local roadmaps.
