# RPG Mechanic

RPG is a center mechanic package in `Agents-of-Abyss`.
It names the readable reflection layer for progression, quest-linked work, campaigns, skills, feats, and public presentation without taking operational truth from stronger owner repositories.

## Mechanic card

Status: `landed`

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

Use the validation lane in [mechanics/rpg/AGENTS.md](AGENTS.md#validation) for executable commands.

### Next route

- For role truth, route to `aoa-agents`; for skills, route to `aoa-skills`; for campaign method, route to `aoa-playbooks`; for runtime state, route to `abyss-stack` after runtime gates.
- For unclear owner, return to `docs/FEDERATION_RULES.md` and `docs/REPO_ROLES.md`.

## Active route

- [DIRECTION](DIRECTION.md)
- [USAGE](USAGE.md)
- [PARTS](PARTS.md)
- [LANDING_LOG](LANDING_LOG.md)
- [ROADMAP](ROADMAP.md)
- [OWNER_REQUESTS](OWNER_REQUESTS.md)
- [PROVENANCE](PROVENANCE.md)

## Functioning parts

- [World Grammar](parts/world-grammar/README.md)
- [Source Boundary](parts/source-boundary/README.md)
- [Vocabulary Overlay](parts/vocabulary-overlay/README.md)
- [Quest Campaign](parts/quest-campaign/README.md)
- [Progression Unlocks](parts/progression-unlocks/README.md)
- [Runtime Projection](parts/runtime-projection/README.md)
- [Owner Handoffs](parts/owner-handoffs/README.md)

## Owner-request queue

Use [OWNER_REQUESTS](OWNER_REQUESTS.md) when this mechanic produces an
owner-local role, skill, playbook, proof, quest, runtime, or presentation
request. The central queue source is
[`mechanics/owner-request-queue.json`](../owner-request-queue.json), and the
compact generated companion is
[`generated/owner_request_queue.min.json`](../../generated/owner_request_queue.min.json).
Generated surfaces do not author meaning.

A request packet is not owner acceptance. Keep `rpg` claims center-bounded
until the stronger owner lands the slice and proof routes are satisfied.

## Historical provenance

Use [PROVENANCE](PROVENANCE.md) only when auditing how RPG source history,
terminology, playable obligation readings, worked examples, or preserved source
material feed the active parts. The default route stays on the active route and
functioning parts above.

For vocabulary artifacts, start from
[Vocabulary Overlay](parts/vocabulary-overlay/README.md), then use the
terminology, schema, example, generated overlay, and validator named there.

Canonical support refs:
[TERMINOLOGY](parts/vocabulary-overlay/TERMINOLOGY.md),
[PLAYABLE_OBLIGATION](parts/quest-campaign/PLAYABLE_OBLIGATION.md), and
[playable-obligation-route](parts/quest-campaign/examples/playable-obligation-route.md).

## Owner boundary

Adjunct RPG reflection for progression and navigation; role, skill, technique, playbook, quest item, and runtime truth remain owner-local.

Generated surfaces may help transport the RPG vocabulary, but they do not
author meaning.

## Growth posture

When this mechanic changes, preserve a clean active route: update the relevant
functioning part, preserve landing history in `LANDING_LOG.md`, keep historical
accounting behind `PROVENANCE.md`, and route role, skill, playbook, proof,
quest, runtime, and presentation claims to their stronger owners.
