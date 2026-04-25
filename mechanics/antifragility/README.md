# Antifragility Mechanic
Antifragility is a center mechanic package in `Agents-of-Abyss`. It names the center-owned route, stop-lines, and owner handoffs without taking operational truth from stronger owner repositories.
## Mechanic card
- Status: `landed`
### Trigger
Use when stress, sprawl, authority inflation, cleanup pressure, degraded mode, or a fragile pattern needs bounded review.
### Center owns
Center stress doctrine, via negativa, anti-authority posture, one-in-one-out pressure, and fragility blacklist posture.
### Stronger owner split
- Owner repositories own their local deletion, repair, resilience, and incident evidence.
- `aoa-evals` owns repair proof and regression evidence.
- `aoa-memo` owns incident lessons and retained memory.

### Inputs
- Stress event, fragility pattern, deletion candidate, authority drift, or cleanup proposal.
- Evidence that the change makes ownership, proof, or stop-lines clearer rather than merely smaller.

### Outputs
- Subtraction route, anti-authority stop-line, repair request, evidence request, or owner-local cleanup handoff.
- No one-score health metric and no deletion theater.

### Must not claim
- one-score health
- deletion theater
- owner-local cleanup authority

### Validation
```bash
python scripts/validate_mechanics_topology.py --mechanic antifragility
python scripts/validate_mechanic_readme_cards.py --mechanic antifragility
python scripts/build_mechanic_card_index.py --check
python scripts/validate_mechanic_card_index.py
python scripts/validate_owner_request_queue.py --mechanic antifragility
python scripts/build_owner_request_queue.py --check
python scripts/validate_generated_owner_request_queue.py
python scripts/validate_owner_request_docs.py --mechanic antifragility
```
### Next route
- For owner-local cleanup, route to the owning repository; for repair proof, route to `aoa-evals`; for retained lessons, route to `aoa-memo`.
- For unclear owner, return to `docs/FEDERATION_RULES.md` and `docs/REPO_ROLES.md`.


## Owner-request queue

Use [`ANTIFRAGILITY_OWNER_REPO_REQUESTS.md`](docs/ANTIFRAGILITY_OWNER_REPO_REQUESTS.md) when this mechanic produces an owner-local landing request. The central queue source is [`mechanics/owner-request-queue.json`](../owner-request-queue.json), and the compact generated companion is [`generated/owner_request_queue.min.json`](../../generated/owner_request_queue.min.json).

A request packet is not owner acceptance. Keep `antifragility` claims center-bounded until the stronger owner lands the slice and proof routes are satisfied.

## Start here
- [ANTIFRAGILITY](docs/ANTIFRAGILITY.md)
- [VIA_NEGATIVA](docs/VIA_NEGATIVA.md)
- [ANTI_AUTHORITY_RULES](docs/ANTI_AUTHORITY_RULES.md)
- [ONE_IN_ONE_OUT](docs/ONE_IN_ONE_OUT.md)
- [FRAGILITY_BLACKLIST](FRAGILITY_BLACKLIST.md)
- [LANDING_LOG](LANDING_LOG.md)
- [ROADMAP](ROADMAP.md)

- [ANTIFRAGILITY_OWNER_REPO_REQUESTS](docs/ANTIFRAGILITY_OWNER_REPO_REQUESTS.md)

## Owner boundary
Center stress, subtraction, anti-authority, and fragility-pattern doctrine; owner repositories own local repair evidence.
The card above is the compact route. The docs listed in **Start here** remain the richer source surfaces for this mechanic. Generated card indexes may reflect this package, but they do not author meaning.
## Growth posture
When this mechanic changes, keep the card small enough for a low-context agent to act safely, then place detailed doctrine in `docs/`, proof in the proof owner, memory in the memory owner, runtime in the runtime owner, and source meaning in the source owner.
