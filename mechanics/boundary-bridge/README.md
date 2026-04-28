# Boundary Bridge Mechanic

Boundary bridge is a center mechanic package in `Agents-of-Abyss`.
It governs crossing owner boundaries without turning support, analogy,
translation, projection, proof, routing, runtime, or public wording into an
authority transfer.

## Mechanic card

- Status: `landed`

### Trigger

Use when one owner-owned surface must touch, support, cite, translate,
project, route, or hand off to another owner-owned surface without becoming
the other surface.

### Center owns

AoA center owns boundary-crossing doctrine, non-identity stop-lines,
counterpart vocabulary, owner-handoff packets, and the first ToS-support
reference bridge.

### Stronger owner split

- Source repositories own authored meaning, canon, source interpretation, and
  local truth.
- `Tree-of-Sophia` owns ToS-authored meaning, source authority, node law,
  lineage, and canon-facing review.
- `aoa-kag` owns derived projections without source authority.
- `aoa-routing` owns dispatch and route behavior without authored meaning.
- `aoa-memo` owns memory and witness objects without proof or canon.
- `aoa-evals` owns proof, verdict, and regression evidence.
- `aoa-playbooks` owns recurring scenario choreography.
- `aoa-sdk`, `abyss-stack`, and other owner repositories own their local
  adapters, runtime bodies, helpers, and implementation truth.

### Inputs

- A request to connect, cite, support, project, translate, route, witness, or
  hand off across owner boundaries.
- A named source owner and receiving owner.
- The bridge mode: `counterpart`, `support`, `projection`, `handoff`,
  `compatibility`, `witness`, `proof`, or `ToS support`.

### Outputs

- A bounded bridge route, owner handoff, proof route, derived projection
  boundary, or ToS-support note.
- Explicit non-identity, no-authority-transfer, and owner-acceptance
  stop-lines.
- No hidden claim that the bridge proves sameness, transfers authority, or
  lands owner-local truth.

### Must not claim

- owner acceptance without owner-local receipt
- identity between bridged surfaces
- AoA-authored ToS canon or source interpretation
- derived projection as source truth
- routing, SDK, memory, runtime, or public projection as authority
- proof before `aoa-evals` or the source owner has landed the relevant proof
- proof before the proof or source owner lands evidence

### Validation

Use the validation lane in [AGENTS.md](AGENTS.md#validation).

### Next route

- For ToS meaning, canon, or source interpretation, route to
  `Tree-of-Sophia`.
- For derived projection, route to `aoa-kag`; for dispatch behavior, route to
  `aoa-routing`; for memory or witness objects, route to `aoa-memo`; for
  proof, route to `aoa-evals`; for scenario choreography, route to
  `aoa-playbooks`.
- For unclear owner, return to `docs/FEDERATION_RULES.md` and
  `docs/REPO_ROLES.md`.

## Active route

- [DIRECTION](DIRECTION.md)
- [PARTS](PARTS.md)
- [LANDING_LOG](LANDING_LOG.md)
- [ROADMAP](ROADMAP.md)
- [OWNER_MAP](OWNER_MAP.md)
- [OWNER_REQUESTS](OWNER_REQUESTS.md)
- [PROVENANCE](PROVENANCE.md)

## Functioning parts

- [Boundary Contract](parts/boundary-contract/README.md)
- [Non-Identity Guard](parts/non-identity-guard/README.md)
- [Counterpart Edge](parts/counterpart-edge/README.md)
- [ToS Support](parts/tos-support/README.md)
- [Witness Compost](parts/witness-compost/README.md)
- [Derived Projection](parts/derived-projection/README.md)
- [Owner Handoff](parts/owner-handoff/README.md)
- [Proof Review Route](parts/proof-review-route/README.md)
- [Compatibility Route](parts/compatibility-route/README.md)

## Owner-request queue

Use [OWNER_REQUESTS](OWNER_REQUESTS.md) when this mechanic produces an
owner-local landing request. A request packet is not owner acceptance.

The central queue source is
[`mechanics/owner-request-queue.json`](../owner-request-queue.json), and the
compact generated companion is
[`generated/owner_request_queue.min.json`](../../generated/owner_request_queue.min.json).
Generated surfaces do not author meaning.

## Historical provenance

Use [PROVENANCE](PROVENANCE.md) only when auditing how counterpart, witness,
ToS-support, projection, owner-handoff, or compatibility source doctrine feeds
the active parts. Open detailed docs when source trace matters, not as the
default active route for every bridge change.

Canonical doctrine refs: [COUNTERPART_BRIDGE](docs/COUNTERPART_BRIDGE.md),
[WITNESS_COMPOST](docs/WITNESS_COMPOST.md),
[TOS_GROWTH_SUPPORT](docs/TOS_GROWTH_SUPPORT.md),
[TOS_TEMPLATE_SUPPORT](docs/TOS_TEMPLATE_SUPPORT.md),
[TOS_LINEAGE_PILOT_SUPPORT](docs/TOS_LINEAGE_PILOT_SUPPORT.md),
[TOS_SOIL_PREP_SUPPORT](docs/TOS_SOIL_PREP_SUPPORT.md), and
[TOS_BRIDGE_OWNER_REPO_REQUESTS](docs/TOS_BRIDGE_OWNER_REPO_REQUESTS.md).

## Owner boundary

AoA owns the bridge law. The bridged owners own the truth on each side.

Generated surfaces may reflect boundary-bridge routes, queues, indexes, or
cards, but they do not author boundary-bridge meaning.

## Growth posture

When this mechanic changes, preserve a clean active route: update the relevant
functioning part, preserve landing history in `LANDING_LOG.md`, keep historical
accounting behind `PROVENANCE.md`, and route ToS, KAG, routing, memo, proof,
playbook, SDK, runtime, and public projection claims to their stronger owners.
Do not make `boundary-bridge` a universal connector.
