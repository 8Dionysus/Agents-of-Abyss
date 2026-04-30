# QUESTBOOK.md - Agents-of-Abyss

This questbook is the compact public index for center-level obligations that
should survive the current diff.

It holds federation-level cross-repo obligations only. It does not absorb
repo-local quest detail from sibling repositories.

It is a root index, not a second roadmap. Program direction belongs in
[ROADMAP](ROADMAP.md). Questbook model law starts in
[model-spine](mechanics/questbook/parts/model-spine/README.md), and lifecycle
detail lives in [lifecycle-law](mechanics/questbook/parts/lifecycle-law/README.md).
Backing quest files live in lane-first lifecycle directories under [`quests/`](quests/).

Top-level `quests/AOA-Q-*` aliases are intentionally absent. The source
placement for each quest object is `quests/<lane>/<state>/AOA-Q-*`.

Quest relations are summarized in
[`questbook_relations`](generated/questbook_relations.min.json) and explained
in [`relation-shape`](mechanics/questbook/parts/relation-shape/README.md). A
`sidequest` relation is route visibility, not ownership transfer or closure.

## Update trigger

Update this root index when a public obligation crosses repository boundaries
or changes the center's constitutional posture.

Use the nearest owner route instead when the obligation is local to one
mechanic, technical district, or sibling repository. Use:

- `ROADMAP.md` for direction, horizon posture, and future trigger contours
- `CHANGELOG.md` for released repository history
- mechanic `LANDING_LOG.md` files for checked mechanic landings
- mechanic `OWNER_REQUESTS.md` files for stronger-owner handoff packets
- `docs/decisions/` for durable rationale

If a closeout leaves a durable obligation but this file stays unchanged, say why
the obligation belongs to another owner route.

## Frontier

- `AOA-Q-0004` - define the first adjunct RPG reflection layer without mutating quest or role canon.
- `AOA-Q-0006` - fix the runtime/frontend architecture law for the AoA RPG layer.
- `AOA-Q-0007` - define the RPG bridge wave for unlock proof, party composition, and derived navigation.
- `AOA-Q-0008` - define the RPG runtime/projection wave for the first body-facing AoA slice.

## Near

- `AOA-Q-0003` - shape the next contour after foundation proof without widening too early.
- `AOA-Q-0005` - define the second RPG reflection wave for skills as abilities and techniques as feats.

## Blocked / reanchor

No center-level public blocked or reanchor item is currently listed here.

## Harvest candidates

No center-level public harvest candidate is currently listed here.

## Backing files

- `quests/center/<state>/AOA-Q-*.yaml`
- `quests/agon/<state>/AOA-Q-AGON-*.md`
- `quests/experience/<state>/AOA-Q-EXP-*.md`
- future lane-specific families use the same `quests/<lane>/<state>/AOA-Q-*`
  contract
- generated summaries: [`questbook_index`](generated/questbook_index.min.json),
  [`questbook_frontier`](generated/questbook_frontier.min.json), and
  [`questbook_relations`](generated/questbook_relations.min.json)

Root `QUESTBOOK.md` lists center-lane public bands. Lane-local ready queues live
in the backing quest files, lane README gates, and generated summaries.

## Rule

A quest can survive in this root index only if it crosses repository boundaries
or changes the center's constitutional posture. Repo-local tasks belong to their
owner repository.
