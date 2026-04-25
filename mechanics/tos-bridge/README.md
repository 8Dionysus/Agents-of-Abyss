# ToS bridge Mechanic
ToS bridge is a center mechanic package in `Agents-of-Abyss`. It names the center-owned route, stop-lines, and owner handoffs without taking operational truth from stronger owner repositories.
## Mechanic card
- Status: `landed`
### Trigger
Use when AoA supports Tree-of-Sophia counterpart, witness, compost, template, growth, lineage, or soil-prep work without authoring ToS meaning.
### Center owns
AoA support posture, route language, counterpart/witness/compost support boundaries, and non-authoring stop-lines.
### Stronger owner split
- `Tree-of-Sophia` owns ToS-authored meaning, canon, and source interpretation.
- AoA owner repositories own only their local support, proof, memory, routing, or derived implementation surfaces.

### Inputs
- ToS support request, counterpart mapping, witness note, compost proposal, template support, lineage pilot support, or soil-prep support.
- A source distinction between AoA support and ToS-authored meaning.

### Outputs
- Support route, witness/compost note, derived handoff, template support note, growth-support route, or soil-prep route.
- No AoA-authored ToS canon and no source interpretation authority.

### Must not claim
- AoA-authored ToS canon
- source interpretation authority
- owner-local implementation truth

### Validation
```bash
python scripts/validate_mechanics_topology.py --mechanic tos-bridge
python scripts/validate_mechanic_readme_cards.py --mechanic tos-bridge
python scripts/build_mechanic_card_index.py --check
python scripts/validate_mechanic_card_index.py
python scripts/validate_owner_request_queue.py --mechanic tos-bridge
python scripts/build_owner_request_queue.py --check
python scripts/validate_generated_owner_request_queue.py
python scripts/validate_owner_request_docs.py --mechanic tos-bridge
```
### Next route
- For ToS meaning, canon, or source interpretation, route to `Tree-of-Sophia` before making any claim.
- For unclear owner, return to `docs/FEDERATION_RULES.md` and `docs/REPO_ROLES.md`.


## Owner-request queue

Use [`TOS_BRIDGE_OWNER_REPO_REQUESTS.md`](docs/TOS_BRIDGE_OWNER_REPO_REQUESTS.md) when this mechanic produces an owner-local landing request. The central queue source is [`mechanics/owner-request-queue.json`](../owner-request-queue.json), and the compact generated companion is [`generated/owner_request_queue.min.json`](../../generated/owner_request_queue.min.json).

A request packet is not owner acceptance. Keep `tos-bridge` claims center-bounded until the stronger owner lands the slice and proof routes are satisfied.

## Start here
- [COUNTERPART_BRIDGE](docs/COUNTERPART_BRIDGE.md)
- [WITNESS_COMPOST](docs/WITNESS_COMPOST.md)
- [TOS_GROWTH_SUPPORT](docs/TOS_GROWTH_SUPPORT.md)
- [TOS_TEMPLATE_SUPPORT](docs/TOS_TEMPLATE_SUPPORT.md)
- [TOS_LINEAGE_PILOT_SUPPORT](docs/TOS_LINEAGE_PILOT_SUPPORT.md)
- [TOS_SOIL_PREP_SUPPORT](docs/TOS_SOIL_PREP_SUPPORT.md)
- [LANDING_LOG](LANDING_LOG.md)
- [ROADMAP](ROADMAP.md)

- [TOS_BRIDGE_OWNER_REPO_REQUESTS](docs/TOS_BRIDGE_OWNER_REPO_REQUESTS.md)

## Owner boundary
AoA support posture for Tree-of-Sophia; ToS authored meaning and canon stay in Tree-of-Sophia.
The card above is the compact route. The docs listed in **Start here** remain the richer source surfaces for this mechanic. Generated card indexes may reflect this package, but they do not author meaning.
## Growth posture
When this mechanic changes, keep the card small enough for a low-context agent to act safely, then place detailed doctrine in `docs/`, proof in the proof owner, memory in the memory owner, runtime in the runtime owner, and source meaning in the source owner.
