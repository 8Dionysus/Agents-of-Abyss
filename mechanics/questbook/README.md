# Questbook Mechanic

Questbook is the center mechanic for public, durable obligations. It keeps
follow-up work visible without becoming a second roadmap, private scratchpad,
or repo-local task sink.

## Mechanic card

- Status: `landed`

### Trigger

Use when an obligation must survive the current session as a public,
reviewable follow-up without becoming a second roadmap or private scratchpad.

### Center owns

Federation-level quest mechanics, root public quest index posture, lane-first
quest item placement, generated read models, and obligation lifecycle language.

### Stronger owner split

- Owner repositories own repo-local obligations and local task truth.
- `quests/` holds public quest items in lane-first lifecycle directories, not
  private scratch work.
- `aoa-playbooks` owns recurring quest choreography when a quest becomes
  repeatable method.
- `aoa-evals` owns proof obligations attached to quest closure.
- `aoa-memo` owns lessons retained after quest completion.

### Inputs

- Deferred obligation, follow-up, risk, dependency, or public work item that
  must not be lost.
- Enough context to choose center quest placement or route the obligation to
  the owner repository.

### Outputs

- Quest item, root questbook index update, generated Questbook read model,
  owner-local task route, proof request, or closure note.
- No private scratchpad and no parallel roadmap.

### Must not claim

- second roadmap
- private scratchpad
- repo-local task sink

### Validation

```bash
python scripts/validate_mechanics_topology.py --mechanic questbook
python mechanics/questbook/scripts/validate_questbook_lifecycle.py
python mechanics/questbook/scripts/build_questbook_index.py --check
python mechanics/questbook/scripts/validate_questbook_index.py
python mechanics/questbook/scripts/validate_quest_relations.py
python mechanics/questbook/scripts/build_ready_owner_routes.py --check
python mechanics/questbook/scripts/validate_ready_owner_routes.py
python mechanics/questbook/scripts/validate_questbook_distillation.py
python scripts/validate_mechanic_readme_cards.py --mechanic questbook
python scripts/build_mechanic_card_index.py --check
python scripts/validate_mechanic_card_index.py
python scripts/validate_owner_request_queue.py --mechanic questbook
python scripts/build_owner_request_queue.py --check
python scripts/validate_generated_owner_request_queue.py
python scripts/validate_owner_request_docs.py --mechanic questbook
```

### Next route

- For repo-local obligations, route to the owner repository instead of keeping
  them in the center.
- For unclear owner, return to `docs/FEDERATION_RULES.md` and
  `docs/REPO_ROLES.md`.

## Start Here

- Model spine: [`parts/model-spine`](parts/model-spine/README.md)
- Lifecycle law: [`parts/lifecycle-law`](parts/lifecycle-law/README.md)
- Execution passport:
  [`parts/execution-passport`](parts/execution-passport/README.md)
- Harvest route: [`parts/harvest-route`](parts/harvest-route/README.md)
- Lane owner-route contract:
  [`parts/lane-owner-routes`](parts/lane-owner-routes/README.md)
- Active parts: [`PARTS.md`](PARTS.md)
- Parts index: [`parts/README.md`](parts/README.md)
- Parts registry: [`parts/registry.json`](parts/registry.json)
- Direction: [`DIRECTION.md`](DIRECTION.md)
- Roadmap: [`ROADMAP.md`](ROADMAP.md)
- Landing ledger: [`LANDING_LOG.md`](LANDING_LOG.md)
- Provenance bridge: [`PROVENANCE.md`](PROVENANCE.md)
- Root public index: [`QUESTBOOK.md`](../../QUESTBOOK.md)
- Quest item store: [`quests/README.md`](../../quests/README.md)

## Specialized Routes

- Relation shape: [`parts/relation-shape`](parts/relation-shape/README.md)
- First contour provenance: [`PROVENANCE.md`](PROVENANCE.md)
- Owner-request packets: [`OWNER_REQUESTS.md`](OWNER_REQUESTS.md)
- Experience ready owner routing:
  [`experience-ready-owner-routes.md`](parts/lane-owner-routes/experience-ready-owner-routes.md)
- Experience ready owner route registry:
  [`experience-ready-owner-routes.json`](parts/lane-owner-routes/experience-ready-owner-routes.json)

## Owner Boundary

Quest lifecycle and public obligation mechanics; root QUESTBOOK remains index
and quests/ remains lane-first lifecycle item store.

Generated card indexes and generated Questbook views may reflect this package,
but they do not author meaning.

## Growth Posture

When this mechanic changes, keep active routes readable and functional. Place
detailed doctrine in `docs/`, proof in the proof owner, memory in the memory
owner, runtime in the runtime owner, and source meaning in the source owner.
