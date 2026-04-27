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

## Start Here

- Direction: [DIRECTION](DIRECTION.md)
- Usage contract: [USAGE](USAGE.md)
- Parts atlas: [PARTS](PARTS.md) and [parts](parts/)
- World grammar: [world-grammar](parts/world-grammar/README.md)
- Source boundaries: [source-boundary](parts/source-boundary/README.md)
- Vocabulary overlay: [vocabulary-overlay](parts/vocabulary-overlay/README.md), [terminology](parts/vocabulary-overlay/TERMINOLOGY.md), [schema](parts/vocabulary-overlay/schemas/dual_vocabulary_overlay.schema.json), [example](parts/vocabulary-overlay/examples/dual_vocabulary_overlay.example.json), and [generated overlay](parts/vocabulary-overlay/generated/dual_vocabulary_overlay.json)
- Quest and progression contours: [quest-campaign](parts/quest-campaign/README.md) and [progression-unlocks](parts/progression-unlocks/README.md)
- Playable obligation reading: [quest-campaign/PLAYABLE_OBLIGATION](parts/quest-campaign/PLAYABLE_OBLIGATION.md)
- Runtime and handoff contours: [runtime-projection](parts/runtime-projection/README.md) and [owner-handoffs](parts/owner-handoffs/README.md)
- Provenance: [PROVENANCE](PROVENANCE.md) and [legacy](legacy/)
- Owner requests: [OWNER_REQUESTS](OWNER_REQUESTS.md)
- Status: [LANDING_LOG](LANDING_LOG.md) and [ROADMAP](ROADMAP.md)

## Working Law

RPG is an overlay of legibility.
It may provide names like class, rank, feat, party, quest, campaign, unlock, reputation, or resource when those names help agents navigate.
The names remain adjunct labels unless the relevant owner repository lands the underlying object, proof, or runtime behavior.

RPG is allowed to grow as world grammar when the game form improves routing, judgment, memory, proof, or consequence.
It should stay silent when game language would only decorate ordinary work.

Generated surfaces may help transport the RPG vocabulary, but they do not author meaning.
The authored route starts from docs and owner boundaries, then becomes machine-checkable through the package validator.

## Owner Boundary

Adjunct RPG reflection for progression and navigation; role, skill, technique, playbook, quest item, and runtime truth remain owner-local.
The card above is the compact route.
The parts listed in **Start Here** are the active mechanic surfaces.
Historical sources remain preserved, but active work should route through `PROVENANCE.md` before consulting them.
