# Growth Cycle Mechanic

Growth Cycle is a center mechanic package in `Agents-of-Abyss`.
It names how a reviewed agent-process moves from one growth state to the next
without letting any stage pretend to be the whole system.

## Mechanic card

Status: `landed`

### Trigger

Use when a reviewed work cycle or agent process must move through checkpoint,
reviewed closeout, donor harvest, progression, route choice, automation scan,
diagnosis, repair, quest promotion, or owner handoff without letting any one
stage pretend to be the whole system.

### Center owns

Center growth-cycle law, stage order, stop-lines, owner split, review gates,
and handoff route grammar for reviewed agent-process lifecycle.

### Stronger owner split

- `aoa-sdk` owns hooks, checkpoint ledgers, closeout context, local control
  panel behavior, and typed cycle helpers.
- `aoa-skills` owns executable donor, progression, diagnosis, repair, quest,
  automation, and fork skills.
- `aoa-agents` owns self-agent checkpoint, approval, rollback, health, role,
  and progression posture.
- `aoa-evals` owns proof, regression, verdict, repair quality, and progression
  quality.
- `aoa-memo` owns memory writeback, recall, failure lessons, and checkpoint to
  memory boundaries.
- `aoa-playbooks` owns recurring cycle choreography and campaign routes.
- `aoa-stats` owns derived visibility from receipts and never raw authority.
- `aoa-routing` owns re-entry and next-route hints without cycle meaning.
- `Dionysus` owns reviewed snapshots and seed lineage when promotion is
  explicit.
- `abyss-stack` owns runtime exports, runtime health receipts, and plumbing
  after runtime gates.

### Inputs

- Checkpoint note, reviewed closeout artifact, donor harvest candidate,
  progression evidence, route fork, automation candidate, diagnosis packet,
  repair packet, quest-shaped repeated unit, or owner-handoff pressure.
- Enough reviewed evidence and owner context to decide which stage is next.

### Outputs

- Stage route, next-skill hint, proof request, repair or diagnosis route, quest
  promotion decision request, owner request packet, memo handoff, or stats
  handoff.
- No proof, memory canon, runtime activation, owner acceptance, hidden
  automation, or final progress claim unless the stronger owner lands it.

### Must not claim

- hook implementation authority
- executable skill truth
- proof verdict
- memory canon
- runtime activation
- owner acceptance
- hidden scheduler or autonomous self-repair
- universal progression score
- quest promotion authority without reviewed evidence
- method-growth final object truth

### Validation

Use the validation lane in [mechanics/growth-cycle/AGENTS.md](AGENTS.md#validation) for executable commands.

### Next route

- For hooks, checkpoint ledgers, local control, and closeout context, route to
  `aoa-sdk`; for executable cycle steps, route to `aoa-skills`; for self-agent
  posture, route to `aoa-agents`.
- For proof, route to `aoa-evals`; for memory, route to `aoa-memo`; for
  choreography, route to `aoa-playbooks`; for derived visibility, route to
  `aoa-stats`; for navigation hints, route to `aoa-routing`; for reviewed
  snapshots and seeds, route to `Dionysus`; for runtime exports and health
  receipts, route to `abyss-stack`; for unclear owner, return to
  `docs/FEDERATION_RULES.md` and `docs/REPO_ROLES.md`.

## Active route

- [DIRECTION](DIRECTION.md)
- [PARTS](PARTS.md)
- [LANDING_LOG](LANDING_LOG.md)
- [ROADMAP](ROADMAP.md)
- [OWNER_MAP](OWNER_MAP.md)
- [OWNER_REQUESTS](OWNER_REQUESTS.md)
- [PROVENANCE](PROVENANCE.md)

## Functioning parts

- [Checkpoint Intake](parts/checkpoint-intake/README.md)
- [Reviewed Closeout Chain](parts/reviewed-closeout-chain/README.md)
- [Donor Harvest](parts/donor-harvest/README.md)
- [Progression Lift](parts/progression-lift/README.md)
- [Route Forks](parts/route-forks/README.md)
- [Automation Opportunity](parts/automation-opportunity/README.md)
- [Diagnosis Gate](parts/diagnosis-gate/README.md)
- [Repair Cycle](parts/repair-cycle/README.md)
- [Quest Promotion](parts/quest-promotion/README.md)
- [Owner Followthrough](parts/owner-followthrough/README.md)

## Owner-request queue

Use [OWNER_REQUESTS](OWNER_REQUESTS.md) when this mechanic produces an
owner-local hook, skill, proof, memory, runtime, role, route, playbook, stats,
seed, or quest request. The central queue source is
[`mechanics/owner-request-queue.json`](../owner-request-queue.json), and the
compact generated companion is
[`generated/owner_request_queue.min.json`](../../generated/owner_request_queue.min.json).
Generated surfaces do not author meaning.

A request packet is not owner acceptance. Keep `growth-cycle` claims
center-bounded until the stronger owner lands the slice and proof routes are
satisfied.

## Historical provenance

Use [PROVENANCE](PROVENANCE.md) only when auditing how checkpoint, closeout,
donor, progression, diagnosis, repair, quest, or owner-followthrough evidence
feeds the active parts. The default route stays on the active route and
functioning parts above.

Canonical doctrine refs: [GROWTH_CYCLE_LAW](docs/GROWTH_CYCLE_LAW.md) and
[GROWTH_CYCLE_OWNER_REPO_REQUESTS](docs/GROWTH_CYCLE_OWNER_REPO_REQUESTS.md).

## Owner boundary

AoA owns the law and route grammar for Growth Cycle. Owner repositories decide
what local hook, skill, proof, memory, runtime, quest, stats, or playbook
behavior means inside their own domains.

Generated surfaces may reflect Growth Cycle cards, queues, or indexes, but they
do not author Growth Cycle meaning.

## Growth posture

When this mechanic changes, preserve a clean active route: update the relevant
functioning part, preserve landing history in `LANDING_LOG.md`, keep historical
accounting behind `PROVENANCE.md`, and route hook, skill, proof, memory,
runtime, role, route, playbook, stats, seed, and quest claims to their stronger
owners.
