# AGENTS.md

## Applies to

This card applies to `mechanics/questbook/` and every nested path under that
scope until a nearer `AGENTS.md` narrows the lane.

## Read before editing

Read `DIRECTION.md`, `PARTS.md`, and the relevant owner route only when Questbook meaning changes.
## Boundaries

- Do not use this lane to override owner-local truth, generated-source
  boundaries, sibling-repo authority, or release validation contracts.
- Do not treat `sidequest` as owner transfer, dependency, acceptance, or closure
  proof.
- Do not turn Questbook into a second roadmap, private scratchpad, scheduler,
  proof ledger, runtime state, or hidden memory.
- Generated Questbook surfaces summarize source quest files; they do not author
  quest meaning.

## Closeout

Closeout must name changed active parts, source quest lanes affected, generated
mirrors rebuilt or not rebuilt, owner-request status affected, checks run,
checks skipped, remaining risk, and the next owner route if this lane was only a
waypoint.

If `PROVENANCE.md` was consulted, name only the relevant model, archive map, or
receipt section. Do not enumerate raw legacy sources unless the task
specifically audited archive evidence in depth.

## Role

Questbook owns the mechanics of public obligations, quest lifecycle, placement,
risk, difficulty, relations, and harvest rules.

Root `QUESTBOOK.md` remains the public index. `quests/` remains the quest item
store. Source quest objects live under lane-first lifecycle directories such as
`quests/center/triaged/`, `quests/agon/ready/`, and `quests/experience/done/`;
root-level `AOA-Q-*` aliases and root lifecycle directories are intentionally
absent.

## Source Surfaces

- `README.md`: package entry and route.
- `DIRECTION.md`: current active mechanic direction.
- `PARTS.md`: active functioning-part map.
- `parts/`: concise active questbook contracts.
- `OWNER_REQUESTS.md`: center-side owner request packet.
- `ROADMAP.md`: current and next questbook contour.
- `LANDING_LOG.md`: checked questbook landing ledger.
- `PROVENANCE.md`: controlled bridge to legacy and source accounting.
- `legacy/`: archival source material, not active law.
- `quests/`: source quest item store outside the mechanic package.
- `generated/`: generated questbook views that mirror source quest files.
- `docs/`: detailed doctrine and support notes.

## Post-change route review

Before closeout, review the changed route rather than only the changed file:

- Source quest changed: confirm lane, lifecycle state, source contract,
  relation shape, generated Questbook views, and owner boundary.
- Part changed: confirm `parts/registry.json`, `PARTS.md`, `parts/README.md`,
  the part contract, validation route, landing log, and provenance route still
  agree.
- Owner-request route changed: confirm the request packet, queue, generated
  queue, ready-owner route table, and owner acceptance boundary.
- AGENTS, docs, or decision surface changed: rebuild the matching generated
  index and make sure the active route did not move into legacy/raw.
- Repeated defaults appear in quest sources: move the default to the lane
  README and keep only a short per-quest route to it.
- Future route pressure changed: update `ROADMAP.md` only when the trigger is
  concrete and useful.
- Checked landing changed: update `LANDING_LOG.md`.
- Card-facing route, owner boundary, validation refs, or public summaries
  changed: update `mechanics/registry.json` and generated indexes.

Keep executable validation routes in the repository `VALIDATION.md` map. Other
Questbook Markdown surfaces should route to the package route instead of
duplicating command blocks.

## Validation

Run the narrow checks for the touched surface:

Use the applicable validation route when route, generated, validation, or
release-facing surfaces change together.
