# Questbook Direction

Questbook should make durable obligations playable without becoming a second
roadmap.

## Current Direction

- Keep root `QUESTBOOK.md` compact and public-facing.
- Keep source quest objects in `quests/<lane>/<state>/AOA-Q-*`.
- Let lanes name the owning mechanic or center route before lifecycle state
  names the current posture.
- Use relations to expose route shape without moving ownership.
- Build generated read models from source quest files instead of
  hand-maintaining global views.
- Keep `parts/model-spine/` as a spine; keep lifecycle, execution, harvest,
  and route-map detail in narrow active parts.
- Keep source object reviewability in `parts/source-contract/`, with rich
  YAML and strict Markdown contracts required for source quest files.
- Keep repeated quest route defaults in lane READMEs, not in every quest file.
- Keep executable validation commands in `AGENTS.md`; other Markdown surfaces
  route there.
- Keep ready owner-route tables generated from registries instead of
  hand-maintaining route rows.
- Keep `docs/` as a compatibility route and `legacy/` as provenance, not as
  the normal working path.

## Operating Posture

- Public index stays short.
- Source objects carry the durable obligation.
- Generated views support scanning, validation, and routing.
- Owner requests carry stronger-owner handoffs.
- Route registries connect ready quests to owner-request packets.
- `PROVENANCE.md` is the only active bridge back to legacy.
- Part registry validation keeps active parts, contracts, validation routes,
  and legacy provenance accounting synchronized.
- Post-change route review checks source, generated, owner-request, AGENTS,
  landing-log, and provenance consequences before closeout.
- Closure requires evidence, not just a cleaner board.

## Time Has Come When

- A lane gains enough active objects that its README needs a short local route
  note.
- A repeated quest family appears twice in one lane or three times across lanes
  and should be harvested into a mechanic, playbook, skill, eval, memo, or
  owner request.
- A lane gains enough strict Markdown quests that shared defaults should move
  into a lane-local README rather than repeat in each source file.
- A second lane gains enough ready owner routes to justify its own registry and
  generated projection.
- Sibling repositories are ready to accept owner-local questbooks without
  copying the center root index.

## Stop-Lines

- Do not turn quests into private TODOs.
- Do not use a generated Questbook view as source truth.
- Do not place repo-local task truth in AoA center unless it is a federation
  obligation.
- Do not route a quest to a lane only because the title sounds similar; owner
  boundary wins.
- Do not treat `sidequest` as dependency, owner transfer, acceptance, or
  closure proof.
- Do not edit generated ready owner-route tables by hand.
- Do not create or retain Markdown quest sources outside the strict source
  contract.
- Do not duplicate validation command blocks outside Questbook `AGENTS.md`.
- Do not repeat generic lane/state defaults inside every quest source.
