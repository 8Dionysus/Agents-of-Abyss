# Docs Root Source Tightening

Status: accepted
Date: 2026-04-29

## Context

The `docs/` root had become correct but denser than its role required.
`docs/README.md` repeated route-contract and mechanics-atlas detail,
`docs/LAYERS.md` carried a mechanic package table, `docs/REPO_ROLES.md` carried
an Agon-specific routing block, and `docs/FEDERATION_RULES.md` carried several
separate ToS-support rules that expressed one owner boundary.

That made the root docs useful, but it also gave future agents several places
to update the same route shape.

## Options considered

1. Keep the detailed root docs and rely on validators to catch drift.
2. Tighten root docs into role-specific maps and route detail to the current
   canonical homes.

## Decision

The `docs/` root stays a center doctrine and route map surface.

Detailed mechanic selection belongs in `mechanics/README.md`,
`mechanics/registry.json`, and `generated/mechanic_card_index.min.json`.
Route-mode detail belongs in `docs/START_HERE_ROUTE_CONTRACT.md`.
Mechanic package detail belongs in the owning mechanic package.
ToS-support law remains in `docs/FEDERATION_RULES.md` as one positive owner
boundary that routes authored meaning back to `Tree-of-Sophia`.

## Rationale

This keeps each root docs file light enough to read while preserving the route
anchors that low-context agents and validators need.

The root docs should answer:

- what owns this kind of truth?
- where does the next reader go?
- which current law protects the route?

They should route to active homes for branch detail instead of carrying a
second copy of those branches.

## Consequences

- `docs/README.md` becomes a compact docs district map.
- `docs/LAYERS.md` names the mechanics overlay and routes to the atlas.
- `docs/REPO_ROLES.md` keeps one mechanic-shaped route rule for all mechanics
  instead of carrying package-specific contours.
- `docs/FEDERATION_RULES.md` keeps ToS support as center law while reducing
  repeated ToS-specific rules.
- Tests check the new route shape so detailed package catalogs stay in their
  owning homes, including a registry-backed check that `docs/REPO_ROLES.md`
  routes all mechanics through the atlas instead of naming package paths.

Residual risk: future route changes may still tempt agents to update
`docs/README.md` first. The guardrail is to update the canonical source first,
then keep the docs root as a map.

## Source surfaces

- `docs/README.md`
- `docs/LAYERS.md`
- `docs/REPO_ROLES.md`
- `docs/FEDERATION_RULES.md`
- `docs/START_HERE_ROUTE_CONTRACT.md`
- `tests/test_docs_verify_routes.py`

## Follow-up route

Revisit this decision only when the docs-root allowlist, route modes,
mechanics registry authority, or ToS-support owner boundary changes.
