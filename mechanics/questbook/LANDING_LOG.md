# Questbook Landing Log

Canonical landing ledger for the questbook mechanic.

## Current Index

Use this index before reading the full ledger:

| Entry | Why it matters now |
|---|---|
| Root mechanics topology migration | Questbook became a first-class mechanics package. |
| Quest lifecycle board activation | Lifecycle states and public quest item shape became validated. |
| Lane-first quest topology | Source placement moved to `quests/<lane>/<state>/AOA-Q-*`. |
| Center lane promotion pilot | Center quest promotion proved the source-owned dispatch seam route. |
| Agon lane activation pass | Agon center contour and owner-followthrough quests split cleanly. |
| Experience lane activation pass | Experience center-planted contracts split from stronger-owner follow-through. |
| Experience ready owner-request coverage pass | Experience ready items gained center-side owner-request packets. |
| Experience ready owner-route index | Ready Experience quests gained an AoA-side route table. |
| Quest relation model | Quest relations gained `parent`, `sidequest`, and generated validation. |
| Questbook root surface polish | Entry surfaces split route-card, direction, roadmap, parts, and ledger roles. |
| Questbook model spine and route registry | Model detail split into narrow source docs and Experience ready routing moved behind JSON. |
| Questbook parts and legacy split | Active Questbook routes moved into parts; first-contour provenance moved into legacy. |
| Questbook distillation gate | Active parts, contracts, validation files, and legacy bridge are now release-checked together. |

Read the full entry only when the change touches that route, its surfaces, or
its stop-lines. Current route starts at `mechanics/questbook/README.md`,
`mechanics/questbook/DIRECTION.md`, `mechanics/questbook/PARTS.md`,
`mechanics/questbook/parts/README.md`,
`mechanics/questbook/parts/registry.json`, and
`mechanics/questbook/PROVENANCE.md`. Detailed part routes are indexed by
`mechanics/questbook/PARTS.md` and
`mechanics/questbook/parts/registry.json`; source quest objects remain surfaced
through root `QUESTBOOK.md` and `quests/README.md`.

## Entries

### Root mechanics topology migration

Status: landed

Owner boundary: `Agents-of-Abyss` owns federation-level quest mechanics and the
root public index; repo-local obligations remain with owner repositories.

Surfaces:

- `mechanics/questbook/README.md`
- `mechanics/questbook/ROADMAP.md`
- `mechanics/questbook/parts/model-spine/README.md`
- `mechanics/questbook/legacy/raw/QUESTBOOK_FIRST_WAVE.md`
- `QUESTBOOK.md`
- `quests/README.md`

Validation: `python scripts/validate_mechanics_topology.py --mechanic questbook`

Stop-lines: no second roadmap, private scratchpad, or owner-local task sink.

Next route: keep quest items in `quests/` and route repo-local tasks to their
owners.

### Quest lifecycle board activation

Status: landed

Owner boundary: `Agents-of-Abyss` owns center quest lifecycle shape and the
public item store; owner repositories still own repo-local work truth.

Surfaces:

- `mechanics/questbook/parts/model-spine/README.md`
- `mechanics/questbook/scripts/validate_questbook_lifecycle.py`
- `mechanics/questbook/tests/test_questbook_lifecycle.py`
- `QUESTBOOK.md`
- `quests/README.md`
- `quests/*/*/` after the later lane-first topology landing

Validation: `python mechanics/questbook/scripts/validate_questbook_lifecycle.py`

Stop-lines: lifecycle placement is not a roadmap, scheduler, private memory, or
owner-local task claim.

Next route: promote quest objects by state only when the owner lane and evidence
path justify the move.

### Lane-first quest topology

Status: landed

Owner boundary: `Agents-of-Abyss` owns the center Questbook topology and public
read models; lanes name owner route, while lifecycle state names current
posture. Owner repositories still own repo-local task truth.

Surfaces:

- `QUESTBOOK.md`
- `quests/README.md`
- `quests/center/README.md`
- `quests/agon/README.md`
- `quests/experience/README.md`
- `quests/*/README.md`
- `quests/<lane>/<state>/AOA-Q-*`
- `mechanics/questbook/DIRECTION.md`
- `mechanics/questbook/PARTS.md`
- `mechanics/questbook/scripts/build_questbook_index.py`
- `mechanics/questbook/scripts/validate_questbook_lifecycle.py`
- `mechanics/questbook/scripts/validate_questbook_index.py`
- `generated/questbook_index.min.json`
- `generated/questbook_frontier.min.json`

Validation:

- `python mechanics/questbook/scripts/validate_questbook_lifecycle.py`
- `python mechanics/questbook/scripts/build_questbook_index.py --check`
- `python mechanics/questbook/scripts/validate_questbook_index.py`

Stop-lines: no root quest aliases, no root lifecycle source directories, no
generated surface as quest authority, and no repo-local task truth in the center
unless it is a federation obligation.

Next route: use lane-first promotion for real quest movement, then harvest
repeated quest families into the stronger owner mechanic or repository.

### Center lane promotion pilot

Status: landed

Owner boundary: `Agents-of-Abyss` owns the public center Questbook route and
center quest source placement. Sibling repositories remain the owners of
source dispatch, routing, role, proof, memory, and runtime truth.

Surfaces:

- `mechanics/questbook/parts/model-spine/README.md`
- `quests/center/README.md`
- `quests/agon/README.md`
- `quests/experience/README.md`
- `quests/center/done/AOA-Q-0002.yaml`
- `quests/center/triaged/AOA-Q-0003.yaml`
- `QUESTBOOK.md`
- `generated/questbook_index.min.json`
- `generated/questbook_frontier.min.json`

Validation:

- `python mechanics/questbook/scripts/validate_questbook_lifecycle.py`
- `python mechanics/questbook/scripts/build_questbook_index.py --check`
- `python mechanics/questbook/scripts/validate_questbook_index.py`

Stop-lines: public Questbook movement must not import private session notes,
turn generated summaries into authority, or move legacy center RPG quest IDs to
the RPG lane without a deliberate reanchor.

Next route: use the center pilot as the pattern for the next high-volume lane
activation pass before tightening markdown quest contracts.

### Agon lane activation pass

Status: landed

Owner boundary: `Agents-of-Abyss` owns Agon center quest placement and the
public Questbook read models. Agon owner follow-through remains a stronger
owner acceptance problem routed through `mechanics/agon/OWNER_REQUESTS.md` and
the sibling repositories.

Surfaces:

- `quests/agon/README.md`
- `quests/agon/done/AOA-Q-AGON-*.md`
- `quests/agon/ready/AOA-Q-AGON-*.md`
- `generated/questbook_index.min.json`
- `generated/questbook_frontier.min.json`
- `mechanics/questbook/LANDING_LOG.md`
- `mechanics/questbook/ROADMAP.md`

Validation:

- `python mechanics/questbook/scripts/validate_questbook_lifecycle.py`
- `python mechanics/questbook/scripts/build_questbook_index.py --check`
- `python mechanics/questbook/scripts/validate_questbook_index.py`
- `python scripts/release_check.py`

Stop-lines: do not close owner-followthrough quests merely because center law
landed, do not treat sibling file presence as owner acceptance unless a receipt
is reviewed, and do not let Agon quests become a duplicate Agon roadmap.

Next route: review `quests/agon/ready/` against `mechanics/agon/OWNER_REQUESTS.md`
and sibling receipts, then update owner-request status or close only the
quests whose owner acceptance is actually proven.

### Experience lane activation pass

Status: landed

Owner boundary: `Agents-of-Abyss` owns Experience center quest placement and
the public Questbook read models. Experience active parts and landing logs prove
center-planted contracts, while stronger owner activation remains routed
through `mechanics/experience/OWNER_REQUESTS.md` and sibling repository
receipts.

Surfaces:

- `quests/experience/README.md`
- `quests/experience/done/AOA-Q-EXP-*.md`
- `quests/experience/ready/AOA-Q-EXP-*.md`
- `generated/questbook_index.min.json`
- `generated/questbook_frontier.min.json`
- `mechanics/questbook/LANDING_LOG.md`
- `mechanics/questbook/ROADMAP.md`

Validation:

- `python mechanics/questbook/scripts/validate_questbook_lifecycle.py`
- `python mechanics/questbook/scripts/build_questbook_index.py --check`
- `python mechanics/questbook/scripts/validate_questbook_index.py`
- `python scripts/release_check.py`

Stop-lines: do not read Experience `done` as runtime activation, proof verdict,
hidden memory sovereignty, KAG canon, ToS-authored meaning, or sibling-owner
acceptance; those remain owner-local routes.

Next route: review `quests/experience/ready/` against
`mechanics/experience/OWNER_REQUESTS.md`, then update owner-request status or
close only the quests whose owner acceptance is actually proven.

### Experience ready owner-request coverage pass

Status: landed

Owner boundary: `Agents-of-Abyss` owns center-side Experience request packets
and Questbook ready-lane routing. Sibling repositories still own acceptance,
landing, proof, runtime, memory, choreography, helper, summary, skill,
technique, KAG, and ToS truth.

Surfaces:

- `mechanics/experience/OWNER_REQUESTS.md`
- `mechanics/owner-request-queue.json`
- `mechanics/OWNER_REQUEST_QUEUE.md`
- `mechanics/registry.json`
- `mechanics/experience/README.md`
- `quests/experience/README.md`
- `generated/owner_request_queue.min.json`
- `generated/mechanic_card_index.min.json`

Validation:

- `python scripts/validate_owner_request_queue.py --mechanic experience`
- `python scripts/build_owner_request_queue.py --check`
- `python scripts/validate_generated_owner_request_queue.py`
- `python scripts/validate_owner_request_docs.py --mechanic experience`
- `python scripts/validate_mechanics_topology.py --mechanic experience`
- `python scripts/validate_mechanic_readme_cards.py --mechanic experience`
- `python scripts/build_mechanic_card_index.py --check`
- `python scripts/validate_mechanic_card_index.py`

Stop-lines: do not treat the new request packets as sibling-owner acceptance,
and do not close Experience `ready` quests without owner-local receipts.

Next route: carry the new Experience request IDs into `aoa-playbooks`,
`aoa-sdk`, `aoa-stats`, `aoa-skills`, and `aoa-techniques`, then update queue
status only from owner-local acceptance evidence.

### Experience ready owner-route index

Status: landed

Owner boundary: `Agents-of-Abyss` owns the AoA-side route index that maps ready
Experience quests to center-side owner-request packets. Owner repositories
still own acceptance, landing, and proof.

Surfaces:

- `mechanics/questbook/parts/lane-owner-routes/experience-ready-owner-routes.md`
- `mechanics/questbook/scripts/validate_ready_owner_routes.py`
- `mechanics/questbook/tests/test_questbook_lifecycle.py`
- `quests/experience/README.md`
- `scripts/release_check.py`

Validation:

- `python mechanics/questbook/scripts/validate_ready_owner_routes.py`
- `python mechanics/questbook/scripts/validate_questbook_lifecycle.py`
- `python scripts/release_check.py`

Stop-lines: the route index is not owner acceptance, not owner landing, and
not permission to close ready quests without receipts.

Next route: use the route index to process Experience ready quests inside AoA
without mutating sibling repositories; only later carry specific request IDs to
owners when that becomes the chosen lane.

### Quest relation model

Status: landed

Owner boundary: `Agents-of-Abyss` owns center-side Questbook relation law,
source quest relation metadata, and generated read models. Lanes and owner
repositories still own their quest meaning, lifecycle movement, acceptance, and
closure proof.

Surfaces:

- `mechanics/questbook/parts/model-spine/README.md`
- `mechanics/questbook/parts/relation-shape/README.md`
- `mechanics/questbook/scripts/questbook_lifecycle_common.py`
- `mechanics/questbook/scripts/build_questbook_index.py`
- `mechanics/questbook/scripts/validate_questbook_index.py`
- `mechanics/questbook/scripts/validate_quest_relations.py`
- `mechanics/questbook/tests/test_questbook_lifecycle.py`
- `quests/center/*/AOA-Q-000*.yaml`
- `generated/questbook_relations.min.json`

Validation:

- `python mechanics/questbook/scripts/validate_questbook_lifecycle.py`
- `python mechanics/questbook/scripts/build_questbook_index.py --check`
- `python mechanics/questbook/scripts/validate_questbook_index.py`
- `python mechanics/questbook/scripts/validate_quest_relations.py`

Stop-lines: `sidequest` is route visibility only; it does not move ownership,
create dependencies, close quests, prove owner acceptance, or authorize runtime
activation.

Next route: use the relation map to keep center, RPG-shaped, Agon, Experience,
and future lane contours visible until a deliberate reanchor creates stronger
lane-local quest objects.

### Questbook root surface polish

Status: landed

Owner boundary: `Agents-of-Abyss` owns Questbook entry surfaces, route cards,
ledger readability, and validation guidance. Source quest meaning remains in
`quests/`, and stronger owner acceptance remains outside this package.

Surfaces:

- `mechanics/questbook/AGENTS.md`
- `mechanics/questbook/README.md`
- `mechanics/questbook/DIRECTION.md`
- `mechanics/questbook/PARTS.md`
- `mechanics/questbook/ROADMAP.md`
- `mechanics/questbook/LANDING_LOG.md`
- `generated/agents_mesh.min.json`

Validation:

- `python scripts/validate_mechanics_topology.py --mechanic questbook`
- `python scripts/validate_mechanic_readme_cards.py --mechanic questbook`
- `python scripts/validate_mechanic_landing_logs.py --mechanic questbook`
- `python scripts/validate_agents_md_shape.py`
- `python scripts/validate_agents_mesh.py`
- `python scripts/build_agents_mesh_index.py --check`
- `python scripts/validate_agents_mesh_index.py`
- `python scripts/validate_generated_freshness.py`

Stop-lines: this pass does not move quest objects, change quest lifecycle
state, update owner-request status, or reinterpret `sidequest`.

Next route: use the cleaner active surfaces as the base for later Questbook
object-shape tightening or lane-specific activation passes.

### Questbook model spine and route registry

Status: landed

Owner boundary: `Agents-of-Abyss` owns Questbook model routing, source-law
split, and AoA-side ready owner-route registries. Source quest meaning remains
in `quests/`, owner-request status remains in the owner-request queue, and
owner repositories still own acceptance, landing, proof, and closure evidence.

Surfaces:

- `mechanics/questbook/parts/model-spine/README.md`
- `mechanics/questbook/parts/lifecycle-law/README.md`
- `mechanics/questbook/parts/execution-passport/README.md`
- `mechanics/questbook/parts/harvest-route/README.md`
- `mechanics/questbook/parts/lane-owner-routes/README.md`
- `mechanics/questbook/parts/lane-owner-routes/experience-ready-owner-routes.json`
- `mechanics/questbook/parts/lane-owner-routes/experience-ready-owner-routes.md`
- `mechanics/questbook/scripts/build_ready_owner_routes.py`
- `mechanics/questbook/scripts/validate_ready_owner_routes.py`
- `mechanics/questbook/tests/test_questbook_lifecycle.py`
- `mechanics/questbook/AGENTS.md`
- `mechanics/questbook/README.md`
- `mechanics/questbook/PARTS.md`
- `mechanics/questbook/DIRECTION.md`
- `mechanics/questbook/ROADMAP.md`
- `mechanics/registry.json`
- `scripts/release_check.py`

Validation:

- `python mechanics/questbook/scripts/build_ready_owner_routes.py --check`
- `python mechanics/questbook/scripts/validate_ready_owner_routes.py`
- `python scripts/validate_mechanics_topology.py --mechanic questbook`
- `python scripts/validate_mechanic_readme_cards.py --mechanic questbook`
- `python scripts/validate_mechanic_landing_logs.py --mechanic questbook`

Stop-lines: the Questbook model document remains the spine, not a monolith; generated
ready-route Markdown is not edited by hand; route registries do not update
owner-request status, prove owner acceptance, or close ready quests.

Next route: generalize lane route registries only after another lane has real
ready-route pressure; otherwise keep the Experience registry as the single
working proof.

### Questbook parts and legacy split

Status: landed

Owner boundary: `Agents-of-Abyss` owns Questbook active part layout,
compatibility docs route, and legacy provenance accounting. Source quest
objects remain under `quests/`; owner acceptance, proof, memory, and recurring
choreography remain with stronger owners.

Surfaces:

- `mechanics/questbook/parts/AGENTS.md`
- `mechanics/questbook/parts/README.md`
- `mechanics/questbook/parts/model-spine/README.md`
- `mechanics/questbook/parts/public-index/README.md`
- `mechanics/questbook/parts/quest-store/README.md`
- `mechanics/questbook/parts/lifecycle-law/README.md`
- `mechanics/questbook/parts/generated-views/README.md`
- `mechanics/questbook/parts/relation-shape/README.md`
- `mechanics/questbook/parts/execution-passport/README.md`
- `mechanics/questbook/parts/harvest-route/README.md`
- `mechanics/questbook/parts/owner-handoffs/README.md`
- `mechanics/questbook/parts/lane-owner-routes/README.md`
- `mechanics/questbook/PROVENANCE.md`
- `mechanics/questbook/legacy/AGENTS.md`
- `mechanics/questbook/legacy/README.md`
- `mechanics/questbook/legacy/INDEX.md`
- `mechanics/questbook/legacy/DISTILLATION_LOG.md`
- `mechanics/questbook/legacy/raw/README.md`
- `mechanics/questbook/legacy/raw/QUESTBOOK_FIRST_WAVE.md`
- `mechanics/questbook/docs/README.md`
- `mechanics/questbook/docs/AGENTS.md`
- `mechanics/questbook/OWNER_REQUESTS.md`
- `mechanics/registry.json`
- `mechanics/owner-request-queue.json`

Validation:

- `python scripts/validate_mechanics_topology.py --mechanic questbook`
- `python scripts/validate_mechanic_readme_cards.py --mechanic questbook`
- `python scripts/validate_mechanic_landing_logs.py --mechanic questbook`
- `python scripts/validate_owner_request_queue.py --mechanic questbook`
- `python scripts/validate_owner_request_docs.py --mechanic questbook`
- `python mechanics/questbook/scripts/build_ready_owner_routes.py --check`
- `python mechanics/questbook/scripts/validate_ready_owner_routes.py`

Stop-lines: the parts directory is the normal active route; legacy is
provenance, not current law; docs is compatibility only; the owner-request
surface is not owner acceptance.

Next route: completed by the Questbook distillation gate below; future part
changes should extend that gate instead of relying on memory.

### Questbook distillation gate

Status: landed

Owner boundary: `Agents-of-Abyss` owns Questbook part shape, active-to-legacy
route hygiene, and package-local validation. Source quest meaning still lives
in `quests/`; stronger owner acceptance, proof, memory, and choreography remain
outside the center package.

Surfaces:

- `mechanics/questbook/parts/registry.json`
- `mechanics/questbook/scripts/validate_questbook_distillation.py`
- `mechanics/questbook/tests/test_questbook_distillation.py`
- `mechanics/questbook/PARTS.md`
- `mechanics/questbook/parts/README.md`
- `mechanics/questbook/PROVENANCE.md`
- `mechanics/questbook/legacy/INDEX.md`
- `scripts/release_check.py`

Validation:

- `python mechanics/questbook/scripts/validate_questbook_distillation.py`
- `python -m pytest -q mechanics/questbook/tests/test_questbook_distillation.py`
- `python scripts/release_check.py`

Stop-lines: the validator checks structure, indexes, direct legacy/raw leakage,
and validation command targets; it does not judge owner acceptance, prove quest
closure, or replace human review of Questbook meaning.

Next route: keep adding Questbook parts through the registry gate; if
Questbook artifact homes grow beyond docs and route JSON, extend this gate
rather than reintroducing flat active-source drift.
