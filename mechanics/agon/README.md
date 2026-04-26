# Agon Mechanic

Agon is a center mechanic package in `Agents-of-Abyss`. It makes pressure,
contest, contradiction, and threshold work lawful without taking operational
truth from stronger owner repositories.

## Mechanic card

- Status: `landed`

### Trigger

Use when conflict, contradiction, bounded pressure, survival tests, lawful
moves, arena or duel grammar, packets, verdicts, retention, rank, schools,
canon promotion, or ToS thresholds are involved.

### Center owns

Agon vocabulary, stop-lines, pressure doctrine, lawful-move grammar, and owner
handoff expectations.

### Stronger owner split

- `aoa-playbooks` owns trial choreography and repeatable practice flows.
- `aoa-evals` owns verdict proof, evaluation discipline, and regression evidence.
- `aoa-memo` owns scars, retention memory, and bounded lessons.
- `aoa-stats` owns aggregate rank and reputation projections after proof gates.
- `aoa-routing` owns gates, handoffs, and route behavior.
- `aoa-agents` owns actor seats, role contracts, and contestant posture.
- `abyss-stack` owns runtime session bodies after runtime-owner gates.
- `aoa-kag` owns derived provenance-aware knowledge substrates.
- `Tree-of-Sophia` owns ToS canon and Sophian threshold decisions.

### Inputs

- Conflict, contradiction, pressure request, lawful move candidate, trial
  contour, packet model, or threshold question.
- A bounded source that can be routed without granting live arena or assistant
  contestant authority.

### Outputs

- Stop-line, owner handoff, trial/playbook request, proof request, memory
  request, route gate, KAG handoff, or ToS threshold packet.
- No rank, verdict, scar, memory, runtime, KAG, or canon mutation inside the
  center.

### Must not claim

- live arena execution
- assistant contestant authority
- rank mutation
- ToS canon write authority

### Validation

```bash
python mechanics/agon/scripts/validate_agon_distillation.py
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

- For trial practice, route to `aoa-playbooks`; for proof, route to
  `aoa-evals`; for scars or retention, route to `aoa-memo`; for runtime, route
  to `abyss-stack` after runtime gates.
- For KAG promotion, route to `aoa-kag`; for ToS canon or threshold authority,
  route to `Tree-of-Sophia`; for unclear owner, return to
  `docs/FEDERATION_RULES.md` and `docs/REPO_ROLES.md`.

## Active route

- [DIRECTION](DIRECTION.md)
- [PARTS](PARTS.md)
- [LANDING_LOG](LANDING_LOG.md)
- [ROADMAP](ROADMAP.md)
- [OWNER_REQUESTS](OWNER_REQUESTS.md)
- [PROVENANCE](PROVENANCE.md)

## Functioning parts

- [Imposition Readiness](parts/imposition-readiness/README.md)
- [Lawful Move Grammar](parts/lawful-move-grammar/README.md)
- [Owner Binding](parts/owner-binding/README.md)
- [Gate Routing](parts/gate-routing/README.md)
- [Trial Handoff](parts/trial-handoff/README.md)
- [Recurrence Adapter](parts/recurrence-adapter/README.md)
- [Packet Arena](parts/packet-arena/README.md)
- [Duel Kernel](parts/duel-kernel/README.md)
- [Verdict Retention Rank](parts/verdict-retention-rank/README.md)
- [Epistemic KAG](parts/epistemic-kag/README.md)
- [Sophian Threshold](parts/sophian-threshold/README.md)
- [Compatibility Bridges](parts/compatibility-bridges/README.md)

## Owner-request queue

Use [OWNER_REQUESTS](OWNER_REQUESTS.md) when this mechanic produces an
owner-local landing request. The central queue source is
[`mechanics/owner-request-queue.json`](../owner-request-queue.json), and the
compact generated companion is
[`generated/owner_request_queue.min.json`](../../generated/owner_request_queue.min.json).
Generated surfaces do not author meaning.

A request packet is not owner acceptance. Keep `agon` claims center-bounded
until the stronger owner lands the slice and proof routes are satisfied.

## Source provenance

Use [PROVENANCE](PROVENANCE.md) only when auditing how detailed source-docs,
wave notes, handoffs, generated capsules, or model families feed the active
parts. The active route stays on the part map above.

## Owner boundary

Center pressure, lawful move, arena grammar, packets, verdict, rank, school,
KAG, and canon-restraint doctrine; live arena execution and owner-local truth
remain outside.

## Growth posture

When this mechanic changes, preserve a clean active route: update the relevant
functioning part, preserve landing history in `LANDING_LOG.md`, keep detailed
source accounting behind `PROVENANCE.md`, and route proof, memory, runtime,
actor, KAG, and ToS claims to their stronger owners.
