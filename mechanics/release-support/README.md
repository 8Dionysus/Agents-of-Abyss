# Release support Mechanic
Release support is a center mechanic package in `Agents-of-Abyss`. It names the center-owned route, stop-lines, and owner handoffs without taking operational truth from stronger owner repositories.
## Mechanic card
- Status: `landed`
### Trigger
Use when a public claim, release surface, changelog, roadmap, direction surface, support posture, or audit route must be checked.
### Center owns
Center release posture, public claim boundaries, federation release protocol, release runbook, and roadmap/changelog/direction separation.
### Stronger owner split
- Sibling repositories own their local release truth and implementation evidence.
- `aoa-evals` owns proof evidence for quality or regression claims.
- Generated surfaces reflect source truth but do not author release truth.

### Inputs
- Public claim, release note, roadmap change, direction update, audit finding, or support statement.
- Source evidence sufficient to decide whether the center may support the claim.

### Outputs
- Supportable claim, stop-line, release checklist route, direction-surface update, audit route, or sibling handoff.
- No unverified public claim and no substitution of roadmap history for changelog truth.

### Must not claim
- unverified public claim
- sibling release truth
- roadmap history as changelog

### Validation
```bash
python scripts/validate_mechanics_topology.py --mechanic release-support
python scripts/release_check.py
python scripts/validate_mechanic_readme_cards.py --mechanic release-support
python scripts/build_mechanic_card_index.py --check
python scripts/validate_mechanic_card_index.py
python scripts/validate_owner_request_queue.py --mechanic release-support
python scripts/build_owner_request_queue.py --check
python scripts/validate_generated_owner_request_queue.py
python scripts/validate_owner_request_docs.py --mechanic release-support
```
### Next route
- For sibling release truth, route to the sibling repository before claiming support.
- For proof-dependent claims, route to `aoa-evals`; for unclear owner, return to `docs/FEDERATION_RULES.md` and `docs/REPO_ROLES.md`.


## Owner-request queue

Use [`RELEASE_SUPPORT_OWNER_REPO_REQUESTS.md`](docs/RELEASE_SUPPORT_OWNER_REPO_REQUESTS.md) when this mechanic produces an owner-local landing request. The central queue source is [`mechanics/owner-request-queue.json`](../owner-request-queue.json), and the compact generated companion is [`generated/owner_request_queue.min.json`](../../generated/owner_request_queue.min.json).

A request packet is not owner acceptance. Keep `release-support` claims center-bounded until the stronger owner lands the slice and proof routes are satisfied.

## Start here
- [PUBLIC_SUPPORT_POSTURE](docs/PUBLIC_SUPPORT_POSTURE.md)
- [FEDERATION_RELEASE_PROTOCOL](docs/FEDERATION_RELEASE_PROTOCOL.md)
- [RELEASING](docs/RELEASING.md)
- [DIRECTION_SURFACES](docs/DIRECTION_SURFACES.md)
- [LANDING_LOG](LANDING_LOG.md)
- [ROADMAP](ROADMAP.md)

- [RELEASE_SUPPORT_OWNER_REPO_REQUESTS](docs/RELEASE_SUPPORT_OWNER_REPO_REQUESTS.md)

## Owner boundary
Center release posture and public claim boundaries; sibling repositories own local release truth.
The card above is the compact route. The docs listed in **Start here** remain the richer source surfaces for this mechanic. Generated card indexes may reflect this package, but they do not author meaning.
## Growth posture
When this mechanic changes, keep the card small enough for a low-context agent to act safely, then place detailed doctrine in `docs/`, proof in the proof owner, memory in the memory owner, runtime in the runtime owner, and source meaning in the source owner.
