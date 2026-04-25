# Agon Mechanic
Agon is a center mechanic package in `Agents-of-Abyss`. It names the center-owned route, stop-lines, and owner handoffs without taking operational truth from stronger owner repositories.
## Mechanic card
- Status: `landed`
### Trigger
Use when conflict, contradiction, bounded pressure, survival tests, lawful moves, arena or duel grammar, packets, verdicts, retention, rank, schools, canon promotion, or ToS thresholds are involved.
### Center owns
Agon vocabulary, stop-lines, pressure doctrine, lawful-move grammar, and owner handoff expectations.
### Stronger owner split
- `aoa-playbooks` owns trial choreography and repeatable practice flows.
- `aoa-evals` owns verdict proof, evaluation discipline, and regression evidence.
- `aoa-memo` owns scars, retention memory, and bounded lessons.
- `aoa-stats` owns aggregate rank and reputation projections after proof gates.
- `aoa-routing` owns gates, handoffs, and route behavior.
- `aoa-agents` owns actor seats, role contracts, and contestant posture.
- `abyss-stack` owns runtime session bodies after runtime-owner gates.
- `Tree-of-Sophia` owns ToS canon and Sophian threshold decisions.

### Inputs
- Conflict, contradiction, pressure request, lawful move candidate, trial contour, packet model, or threshold question.
- A bounded source that can be routed without granting live arena or assistant contestant authority.

### Outputs
- Stop-line, owner handoff, trial/playbook request, proof request, memory request, route gate, or ToS threshold packet.
- No rank, verdict, scar, memory, runtime, or canon mutation inside the center.

### Must not claim
- live arena execution
- assistant contestant authority
- rank mutation
- ToS canon write authority

### Validation
```bash
python scripts/validate_mechanic_landing_logs.py --mechanic agon
python scripts/validate_mechanics_topology.py --mechanic agon
python scripts/validate_mechanic_readme_cards.py --mechanic agon
python scripts/build_mechanic_card_index.py --check
python scripts/validate_mechanic_card_index.py
python scripts/validate_owner_request_queue.py --mechanic agon
python scripts/build_owner_request_queue.py --check
python scripts/validate_generated_owner_request_queue.py
python scripts/validate_owner_request_docs.py --mechanic agon
```
### Next route
- For trial practice, route to `aoa-playbooks`; for proof, route to `aoa-evals`; for scars or retention, route to `aoa-memo`; for runtime, route to `abyss-stack` after runtime gates.
- For ToS canon or threshold authority, route to `Tree-of-Sophia`; for unclear owner, return to `docs/FEDERATION_RULES.md` and `docs/REPO_ROLES.md`.


## Owner-request queue

Use [`AGON_OWNER_REPO_REQUESTS.md`](docs/AGON_OWNER_REPO_REQUESTS.md) when this mechanic produces an owner-local landing request. The central queue source is [`mechanics/owner-request-queue.json`](../owner-request-queue.json), and the compact generated companion is [`generated/owner_request_queue.min.json`](../../generated/owner_request_queue.min.json).

A request packet is not owner acceptance. Keep `agon` claims center-bounded until the stronger owner lands the slice and proof routes are satisfied.

## Start here
- [AGON_IMPOSITION_POSTURE](docs/AGON_IMPOSITION_POSTURE.md)
- [AGON_LAWFUL_MOVE_LANGUAGE](docs/AGON_LAWFUL_MOVE_LANGUAGE.md)
- [AGON_MOVE_OWNER_BINDING](docs/AGON_MOVE_OWNER_BINDING.md)
- [AGON_GATE_ROUTING_HANDOFF](docs/AGON_GATE_ROUTING_HANDOFF.md)
- [AGON_TRIAL_PLAYBOOK_HANDOFF](docs/AGON_TRIAL_PLAYBOOK_HANDOFF.md)
- [AGON_TOS_THRESHOLD_PACKET_MODEL](docs/AGON_TOS_THRESHOLD_PACKET_MODEL.md)
- [PRE_AGON_BASELINE](docs/PRE_AGON_BASELINE.md)
- [LANDING_LOG](LANDING_LOG.md)
- [ROADMAP](ROADMAP.md)

- [AGON_OWNER_REPO_REQUESTS](docs/AGON_OWNER_REPO_REQUESTS.md)

## Owner boundary
Center pressure, lawful move, arena grammar, packets, verdict, rank, school, and canon-restraint doctrine; live arena execution and owner-local truth remain outside.
The card above is the compact route. The docs listed in **Start here** remain the richer source surfaces for this mechanic. Generated card indexes may reflect this package, but they do not author meaning.
## Growth posture
When this mechanic changes, keep the card small enough for a low-context agent to act safely, then place detailed doctrine in `docs/`, proof in the proof owner, memory in the memory owner, runtime in the runtime owner, and source meaning in the source owner.
