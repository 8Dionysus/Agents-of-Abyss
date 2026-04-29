# QUESTBOOK.md - Agents-of-Abyss

This questbook holds federation-level cross-repo obligations only. It does not absorb repo-local quest detail from sibling repositories.

It is a root index, not a second roadmap. Program direction belongs in [ROADMAP](ROADMAP.md). Questbook model law starts in [mechanics/questbook/model-spine](mechanics/questbook/parts/model-spine/README.md), and lifecycle detail lives in [lifecycle-law](mechanics/questbook/parts/lifecycle-law/README.md). Backing quest files live in lane-first lifecycle directories under [`quests/`](quests/).

Top-level `quests/AOA-Q-*` aliases are intentionally absent. The source placement for each quest object is `quests/<lane>/<state>/AOA-Q-*`.

Quest relations are summarized in
[`questbook_relations`](generated/questbook_relations.min.json) and explained
in [`relation-shape`](mechanics/questbook/parts/relation-shape/README.md). A
`sidequest` relation is route visibility, not ownership transfer or closure.

## Frontier

- `AOA-Q-0004` - define the first adjunct RPG reflection layer without mutating quest or role canon.
- `AOA-Q-0006` - fix the runtime/frontend architecture law for the AoA RPG layer.
- `AOA-Q-0007` - define the RPG bridge wave for unlock proof, party composition, and derived navigation.
- `AOA-Q-0008` - define the RPG runtime/projection wave for the first body-facing AoA slice.

## Near

- `AOA-Q-0003` - shape the next contour after foundation proof without widening too early.
- `AOA-Q-0005` - define the second RPG reflection wave for skills as abilities and techniques as feats.
- Root-surface follow-through - after [docs/ROOT_SURFACE_LAW](docs/ROOT_SURFACE_LAW.md) lands, keep mechanic receipts in the owning `mechanics/<slug>/legacy/raw/` route and generic movement evidence in `docs/traces/`.

## Blocked / reanchor

- none yet

## Harvest candidates

- none yet

## Backing files

- `quests/center/<state>/AOA-Q-*.yaml`
- `quests/agon/<state>/AOA-Q-AGON-*.md`
- `quests/experience/<state>/AOA-Q-EXP-*.md`
- future lane-specific families use the same `quests/<lane>/<state>/AOA-Q-*` contract
- generated summaries: [`questbook_index`](generated/questbook_index.min.json), [`questbook_frontier`](generated/questbook_frontier.min.json), and [`questbook_relations`](generated/questbook_relations.min.json)

## Rule

A quest can survive in this root index only if it crosses repository boundaries or changes the center's constitutional posture. Repo-local tasks belong to their owner repository.
