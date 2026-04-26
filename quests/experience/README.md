# experience Quest Lane

Experience obligations and staged contract follow-through.

## Lane route

Use this lane for Experience quest families whose source ID and owner route
already belong to the Experience mechanic. The lane records lifecycle state; it
is not a second Experience roadmap or landing ledger.

Current source split:

- `done`: center-planted Experience contract quests whose surviving route now
  lives in active Experience parts, part-local artifacts, validators, or the
  Experience landing ledger.
- `ready`: stronger-owner follow-through quests where the next honest action is
  owner-request review, owner-local acceptance evidence, or sibling receipt
  routing before any operational claim. The current owner-request map covers
  runtime, memory, routing, proof, role, KAG, ToS, playbook, SDK, stats, skill,
  and technique lanes.
- `triaged`: only for newly captured Experience pressure whose owner route is
  known but whose next action is not yet clear.

## Promotion rule

Promote an Experience quest only when the relevant active part, owner boundary,
and validation route are clear enough to act from the quest source without
opening legacy/raw material first.

Move center-planted contract quests to `done` only when active Experience
surfaces prove the contract. Move stronger-owner follow-through quests to
`ready` when the center has request surfaces and the remaining work is owner
acceptance or receipt review, not more center doctrine.

If a ready quest names a stronger owner that is missing from
[`mechanics/experience/OWNER_REQUESTS.md`](../../mechanics/experience/OWNER_REQUESTS.md),
repair the request map before moving the quest again.

The AoA-side route index for current ready quests lives in
[`experience-ready-owner-routes.md`](../../mechanics/questbook/parts/lane-owner-routes/experience-ready-owner-routes.md).
It maps ready quest files to `ORQ-EXPERIENCE-*` packets without claiming owner
acceptance.

## Stop-lines

- Do not route active work through legacy/raw receipts.
- Do not duplicate Experience ROADMAP or LANDING_LOG history inside quests.
- Do not treat generated Questbook summaries as source state.
- Do not treat `done` as runtime activation, proof verdict, hidden memory
  sovereignty, KAG canon, ToS-authored meaning, or sibling-owner acceptance.

## Strict Source Defaults

Use these defaults from individual `AOA-Q-EXP-*` Markdown sources instead of
repeating generic route text in every quest file. Quest-specific sections may
add sharper evidence or stop-lines when needed.

### ready defaults

- Owner route: `mechanics/experience/`.
- Next action: confirm current owner boundary and owner-request or sibling
  receipt status before moving the quest.
- Acceptance evidence: cite owner-local surfaces, validation output, or an
  owner-request receipt before moving the quest to `done`.
- Stop-lines: the quest is not owner acceptance, runtime activation, closure
  proof, or implementation truth.

### done defaults

- Owner route: `mechanics/experience/`.
- Next action: keep the quest as a closed receipt unless a new quest or
  owner-request follow-up is opened.
- Acceptance evidence: the landed Experience part, part-local artifact,
  validator, or landing ledger named by the quest preserves closure evidence.
- Stop-lines: `done` does not grant live runtime, hidden memory sovereignty,
  KAG canon, ToS-authored meaning, or sibling-owner acceptance.

Quest source files in this lane use lifecycle subdirectories only when items exist. The lifecycle states are `captured`, `triaged`, `ready`, `active`, `blocked`, `reanchor`, `done`, and `dropped`.

Do not create top-level `AOA-Q-*` aliases in this lane. Keep each quest under `<lane>/<state>/AOA-Q-*` and keep root `QUESTBOOK.md` as the public index, not a second roadmap.
