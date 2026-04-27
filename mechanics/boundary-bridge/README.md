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

## Active Parts

Use [PARTS](PARTS.md) as the default operating map.

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

## Source Doctrine

The ToS-support documents remain active doctrine sources and are routed through
[PROVENANCE](PROVENANCE.md). Open them when source trace matters, not as the
default active route for every bridge change.

## Source Surfaces

- [DIRECTION.md](DIRECTION.md)
- [PARTS.md](PARTS.md)
- [OWNER_MAP.md](OWNER_MAP.md)
- [PROVENANCE.md](PROVENANCE.md)
- [OWNER_REQUESTS.md](OWNER_REQUESTS.md)
- [COUNTERPART_BRIDGE.md](docs/COUNTERPART_BRIDGE.md)
- [WITNESS_COMPOST.md](docs/WITNESS_COMPOST.md)
- [TOS_GROWTH_SUPPORT.md](docs/TOS_GROWTH_SUPPORT.md)
- [TOS_TEMPLATE_SUPPORT.md](docs/TOS_TEMPLATE_SUPPORT.md)
- [TOS_LINEAGE_PILOT_SUPPORT.md](docs/TOS_LINEAGE_PILOT_SUPPORT.md)
- [TOS_SOIL_PREP_SUPPORT.md](docs/TOS_SOIL_PREP_SUPPORT.md)
- [TOS_BRIDGE_OWNER_REPO_REQUESTS.md](docs/TOS_BRIDGE_OWNER_REPO_REQUESTS.md)
- [parts/README.md](parts/README.md)
- [legacy/README.md](legacy/README.md)

Generated surfaces may reflect boundary-bridge routes, queues, indexes, or
cards, but they do not author boundary-bridge meaning.

## Owner boundary

AoA owns the bridge law. The bridged owners own the truth on each side.

## Growth posture

Grow this mechanic only when a new owner-boundary crossing repeats enough to
need a reusable route. Do not make `boundary-bridge` a universal connector.
It exists to keep boundaries legible while allowing support, translation,
projection, proof, and handoff to happen without collapse.
