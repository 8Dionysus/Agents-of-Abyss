# Experience Direction

Experience is the center mechanic for making lived work reviewable. This file
owns the current operating direction only; it does not replace the part map,
landing ledger, roadmap, owner-request packet, or provenance bridge.

## Source-of-truth split

- `README.md`: package entry card and shortest route.
- `DIRECTION.md`: current operating direction.
- `PARTS.md`: map of functioning Experience parts.
- `parts/`: concise active part contracts.
- `OWNER_REQUESTS.md`: center-side owner request packet.
- `LANDING_LOG.md`: canonical landing ledger.
- `ROADMAP.md`: future contour, not a historical ledger.
- `artifact-map.json`: old flat artifact path receipts.
- `provenance-receipts.json`: receipt IDs used by active artifacts when they
  must cite older packets, seed inputs, or sibling surfaces.
- `PROVENANCE.md`: the only active bridge back to archive accounting.

## Current direction

- Keep active behavior routed through [PARTS](PARTS.md) and the owning
  `parts/<slug>/` contract before touching archive evidence.
- Keep receipt indirection stable: active artifacts cite old packets, staged
  seed inputs, and sibling-owner surfaces through `provenance-receipts.json`.
- Keep owner-local activation outside Experience center docs; runtime, memory,
  proof, routing, role, KAG, and ToS claims route to stronger owners.
- Keep landed history in `LANDING_LOG.md` and future pressure in `ROADMAP.md`.
- Keep incoming packets distilled into a functioning part instead of rebuilding
  a flat docs lane.

Active parts stay in this order: `capture-kernel`, `certification-proof`,
`adoption-federation`, `governance-polis`, `release-deployment`,
`office-operations`, `service-mesh`, `continuity-context`,
`runtime-boundary`, `compatibility-bridges`.

## Distillation law

New waves, bridge packets, and long exploratory surfaces must not become the active route by accumulation. After a packet lands, distill the surviving function into the relevant part `README.md`, `CONTRACT.md`, or `VALIDATION.md`, then update archival accounting through `PROVENANCE.md`.

Schemas, examples, validators, and tests cite older packets or sibling surfaces
through receipt IDs from `provenance-receipts.json`; do not reintroduce direct
source paths into active part artifacts.

A functioning part should make three things clear:

- what does this part own at the center
- what stronger owner keeps operational authority
- which validation or owner route makes the claim reviewable

## Stop-lines

- Do not claim live workspace runtime from Experience center docs.
- Do not claim hidden memory sovereignty.
- Do not claim live router engine authority.
- Do not claim owner-local activation before the owner repository accepts and proves the slice.
- Do not claim operational Experience adoption, KAG/source meaning transfer, or ToS canon from center docs.
- Do not let historical packets become the primary route.

## Validation

```bash
python mechanics/experience/scripts/validate_experience_distillation.py
python scripts/validate_mechanics_topology.py --mechanic experience
python scripts/validate_mechanic_readme_cards.py --mechanic experience
```
