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

## Start Here

- Direction: [DIRECTION](DIRECTION.md)
- Parts atlas: [PARTS](PARTS.md) and [parts](parts/)
- Center law: [GROWTH_CYCLE_LAW](docs/GROWTH_CYCLE_LAW.md)
- Owner boundaries: [OWNER_MAP](OWNER_MAP.md)
- Owner requests: [OWNER_REQUESTS](OWNER_REQUESTS.md) and [GROWTH_CYCLE_OWNER_REPO_REQUESTS](docs/GROWTH_CYCLE_OWNER_REPO_REQUESTS.md)
- Provenance: [PROVENANCE](PROVENANCE.md)
- Status: [LANDING_LOG](LANDING_LOG.md) and [ROADMAP](ROADMAP.md)

## Working Law

Growth Cycle is the route law for reviewed process movement. It says which
stage should happen next, which owner owns the stronger truth, and what must
remain provisional until review, proof, memory, runtime, or owner-local landing
exists.

Generated surfaces may reflect Growth Cycle cards, queues, or indexes, but they
do not author Growth Cycle meaning.

## Active Parts

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

## Owner Boundary

AoA owns the law and route grammar for Growth Cycle. Owner repositories decide
what local hook, skill, proof, memory, runtime, quest, stats, or playbook
behavior means inside their own domains.
