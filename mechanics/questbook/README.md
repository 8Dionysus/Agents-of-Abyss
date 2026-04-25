# Questbook Mechanic
Questbook is a center mechanic package in `Agents-of-Abyss`. It names the center-owned route, stop-lines, and owner handoffs without taking operational truth from stronger owner repositories.
## Mechanic card
- Status: `landed`
### Trigger
Use when an obligation must survive the current session as a public, reviewable follow-up without becoming a second roadmap or private scratchpad.
### Center owns
Federation-level quest mechanics, root public quest index posture, quest item placement, and obligation lifecycle language.
### Stronger owner split
- Owner repositories own repo-local obligations and local task truth.
- `quests/` holds public center quest items, not private scratch work.
- `aoa-playbooks` owns recurring quest choreography when a quest becomes repeatable method.
- `aoa-evals` owns proof obligations attached to quest closure.
- `aoa-memo` owns lessons retained after quest completion.

### Inputs
- Deferred obligation, follow-up, risk, dependency, or public work item that must not be lost.
- Enough context to choose center quest placement or route the obligation to the owner repository.

### Outputs
- Quest item, root questbook index update, owner-local task route, proof request, or closure note.
- No private scratchpad and no parallel roadmap.

### Must not claim
- second roadmap
- private scratchpad
- repo-local task sink

### Validation
```bash
python scripts/validate_mechanics_topology.py --mechanic questbook
python scripts/validate_mechanic_readme_cards.py --mechanic questbook
python scripts/build_mechanic_card_index.py --check
python scripts/validate_mechanic_card_index.py
python scripts/validate_owner_request_queue.py --mechanic questbook
python scripts/build_owner_request_queue.py --check
python scripts/validate_generated_owner_request_queue.py
python scripts/validate_owner_request_docs.py --mechanic questbook
```
### Next route
- For repo-local obligations, route to the owner repository instead of keeping them in the center.
- For unclear owner, return to `docs/FEDERATION_RULES.md` and `docs/REPO_ROLES.md`.


## Owner-request queue

Use [`QUESTBOOK_OWNER_REPO_REQUESTS.md`](docs/QUESTBOOK_OWNER_REPO_REQUESTS.md) when this mechanic produces an owner-local landing request. The central queue source is [`mechanics/owner-request-queue.json`](../owner-request-queue.json), and the compact generated companion is [`generated/owner_request_queue.min.json`](../../generated/owner_request_queue.min.json).

A request packet is not owner acceptance. Keep `questbook` claims center-bounded until the stronger owner lands the slice and proof routes are satisfied.

## Start here
- [QUESTBOOK_MODEL](docs/QUESTBOOK_MODEL.md)
- [QUESTBOOK_FIRST_WAVE](docs/QUESTBOOK_FIRST_WAVE.md)
- [QUESTBOOK](../../QUESTBOOK.md)
- [README](../../quests/README.md)
- [LANDING_LOG](LANDING_LOG.md)
- [ROADMAP](ROADMAP.md)

- [QUESTBOOK_OWNER_REPO_REQUESTS](docs/QUESTBOOK_OWNER_REPO_REQUESTS.md)

## Owner boundary
Quest lifecycle and public obligation mechanics; root QUESTBOOK remains index and quests/ remains item store.
The card above is the compact route. The docs listed in **Start here** remain the richer source surfaces for this mechanic. Generated card indexes may reflect this package, but they do not author meaning.
## Growth posture
When this mechanic changes, keep the card small enough for a low-context agent to act safely, then place detailed doctrine in `docs/`, proof in the proof owner, memory in the memory owner, runtime in the runtime owner, and source meaning in the source owner.
