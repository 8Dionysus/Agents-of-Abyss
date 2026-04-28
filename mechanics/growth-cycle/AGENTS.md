# AGENTS.md

## Applies to

This card applies to `mechanics/growth-cycle/` and every nested path under that
scope until a nearer `AGENTS.md` narrows the lane.

## Read before editing

Read root `AGENTS.md`, `mechanics/AGENTS.md`, this card,
`mechanics/growth-cycle/README.md`, `mechanics/growth-cycle/DIRECTION.md`,
`mechanics/growth-cycle/PARTS.md`, and the relevant active part before changing
this package.

For owner boundaries, start from `mechanics/growth-cycle/OWNER_MAP.md`.
For source lineage, use `mechanics/growth-cycle/PROVENANCE.md`; do not start
from hook logs, generated summaries, or sibling implementation surfaces.

## Boundaries

- Do not turn Growth Cycle into an always-on scheduler or hidden automation
  loop.
- Do not treat checkpoint notes, closeout notes, donor packets, progression
  hints, or quest candidates as proof, memory canon, or owner acceptance.
- Do not make AoA the implementation owner for hooks, skills, evals, memo,
  runtime exports, playbooks, stats, or route dispatch.
- If a cycle stage needs owner-local implementation, proof, memory, runtime,
  role, route, playbook, stats, seed, or quest behavior, update the owner-request
  surfaces instead of claiming it in the center.

## Closeout

Closeout must name changed Growth Cycle surfaces, whether `PROVENANCE.md` was
consulted, owner requests affected, checks run, checks skipped, remaining risk,
and the next owner route if Growth Cycle was only a waypoint.

If `PROVENANCE.md` was consulted, name only the relevant source bridge or
receipt section. Do not enumerate hook logs, generated summaries, or sibling
implementation histories unless the task specifically audited that evidence in
depth.

## Role

Growth Cycle owns AoA center law for the reviewed lifecycle of agent-process
growth: checkpoint intake, reviewed closeout, donor harvest, progression lift,
route forks, automation opportunity, diagnosis, repair, quest promotion, and
owner followthrough.

It does not own hook implementation, executable skill truth, proof verdicts,
memory canon, runtime activation, hidden scheduling, autonomous self-repair, or
owner-local acceptance.

## Source Surfaces

- `README.md`: package entry and route.
- `DIRECTION.md`: current active mechanic direction.
- `PARTS.md`: active functioning-part map.
- `parts/`: concise active Growth Cycle contracts.
- `OWNER_MAP.md`: Growth Cycle owner boundary and stronger-owner split.
- `OWNER_REQUESTS.md`: center-side owner request packet.
- `ROADMAP.md`: current and next Growth Cycle contour.
- `LANDING_LOG.md`: checked Growth Cycle landing ledger.
- `PROVENANCE.md`: controlled bridge to source evidence.
- `docs/`: detailed doctrine and support notes.

## Post-change route review

After Growth Cycle changes, check whether the next agent can start from
`README.md`, `DIRECTION.md`, `PARTS.md`, and the relevant active part without
reading sibling logs or implementation histories.

Check whether the move changed:

- `DIRECTION.md`: current cycle posture or reviewed lifecycle emphasis.
- `PARTS.md`: active stage boundary or functioning-part map.
- `OWNER_MAP.md`: owner boundary, stop-line, or handoff target.
- `OWNER_REQUESTS.md` and `mechanics/owner-request-queue.json`: hook, skill,
  proof, memory, runtime, role, route, playbook, stats, seed, or quest asks.
- `ROADMAP.md`: future route pressure or unresolved growth-cycle contour.
- `LANDING_LOG.md`: a checked landing or planted contract.
- `PROVENANCE.md`: source bridge, receipt route, or archive map.
- `mechanics/registry.json` and generated indexes: card-facing route, owner
  boundary, validation refs, or public summaries.

Only update a surface when its meaning moved. Leave it untouched when the
change does not affect its job.

## Validation

Run the narrow Growth Cycle lane after package changes:

```bash
python scripts/validate_mechanics_topology.py --mechanic growth-cycle
python scripts/validate_mechanic_readme_cards.py --mechanic growth-cycle
python scripts/build_mechanic_card_index.py --check
python scripts/validate_mechanic_card_index.py
python scripts/validate_mechanic_landing_logs.py --mechanic growth-cycle
python scripts/validate_mechanic_artifact_topology.py --mechanic growth-cycle
python mechanics/growth-cycle/scripts/validate_growth_cycle_mechanic.py
python -m pytest -q mechanics/growth-cycle/tests
```

If owner requests changed, also run:

```bash
python scripts/validate_owner_request_queue.py --mechanic growth-cycle
python scripts/build_owner_request_queue.py --check
python scripts/validate_generated_owner_request_queue.py
python scripts/validate_owner_request_docs.py --mechanic growth-cycle
```

For release-readiness or cross-mechanic edits, finish with:

```bash
python scripts/release_check.py
```
