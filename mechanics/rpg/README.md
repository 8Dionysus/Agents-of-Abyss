# RPG Mechanic
RPG is a center mechanic package in `Agents-of-Abyss`. It names the center-owned route, stop-lines, and owner handoffs without taking operational truth from stronger owner repositories.
## Mechanic card
- Status: `landed`
### Trigger
Use when progression, questlines, campaigns, roles, skills, feats, or readable adjunct reflection need to be interpreted without rewriting ownership.
### Center owns
Adjunct RPG reflection posture, progression-reading vocabulary, boundary map, and presentation grammar.
### Stronger owner split
- `aoa-agents` owns role, persona, and actor contract truth.
- `aoa-skills` owns skill-shaped object truth.
- `aoa-playbooks` owns scenario, campaign, and repeatable choreography truth.
- `aoa-evals` owns progression proof and evidence.
- `quests/` and owner repositories own quest item truth according to placement.
- `abyss-stack` owns runtime and session-state behavior after runtime gates.

### Inputs
- Progression signal, questline, campaign contour, role/skill/feat reading, or presentation need.
- A source object whose owner can be named before RPG reflection is attached.

### Outputs
- Readable reflection, progression label, campaign map, presentation route, or owner handoff.
- No hidden ontology, runtime ledger, or role-canon mutation.

### Must not claim
- hidden ontology
- runtime ledger
- role-canon mutation

### Validation
```bash
python scripts/validate_mechanics_topology.py --mechanic rpg
python scripts/validate_mechanic_readme_cards.py --mechanic rpg
python scripts/build_mechanic_card_index.py --check
python scripts/validate_mechanic_card_index.py
python scripts/validate_owner_request_queue.py --mechanic rpg
python scripts/build_owner_request_queue.py --check
python scripts/validate_generated_owner_request_queue.py
python scripts/validate_owner_request_docs.py --mechanic rpg
```
### Next route
- For role truth, route to `aoa-agents`; for skills, route to `aoa-skills`; for campaign method, route to `aoa-playbooks`; for runtime state, route to `abyss-stack` after runtime gates.
- For unclear owner, return to `docs/FEDERATION_RULES.md` and `docs/REPO_ROLES.md`.


## Owner-request queue

Use [`RPG_OWNER_REPO_REQUESTS.md`](docs/RPG_OWNER_REPO_REQUESTS.md) when this mechanic produces an owner-local landing request. The central queue source is [`mechanics/owner-request-queue.json`](../owner-request-queue.json), and the compact generated companion is [`generated/owner_request_queue.min.json`](../../generated/owner_request_queue.min.json).

A request packet is not owner acceptance. Keep `rpg` claims center-bounded until the stronger owner lands the slice and proof routes are satisfied.

## Start here
- [RPG_LAYER_MODEL](docs/RPG_LAYER_MODEL.md)
- [RPG_ARCHITECTURE_RFC](docs/RPG_ARCHITECTURE_RFC.md)
- [RPG_BOUNDARY_MAP](docs/RPG_BOUNDARY_MAP.md)
- [RPG_FIRST_WAVE](docs/RPG_FIRST_WAVE.md)
- [RPG_SECOND_WAVE](docs/RPG_SECOND_WAVE.md)
- [LANDING_LOG](LANDING_LOG.md)
- [ROADMAP](ROADMAP.md)

- [RPG_OWNER_REPO_REQUESTS](docs/RPG_OWNER_REPO_REQUESTS.md)

## Owner boundary
Adjunct RPG reflection for progression and navigation; role, skill, technique, playbook, quest item, and runtime truth remain owner-local.
The card above is the compact route. The docs listed in **Start here** remain the richer source surfaces for this mechanic. Generated card indexes may reflect this package, but they do not author meaning.
## Growth posture
When this mechanic changes, keep the card small enough for a low-context agent to act safely, then place detailed doctrine in `docs/`, proof in the proof owner, memory in the memory owner, runtime in the runtime owner, and source meaning in the source owner.
