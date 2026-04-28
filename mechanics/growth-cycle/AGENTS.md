# AGENTS.md

## Applies to

This card applies to `mechanics/growth-cycle/` and every nested path under that
scope until a nearer `AGENTS.md` narrows the lane.

## Role

Growth Cycle owns AoA center law for the reviewed lifecycle of agent-process
growth: checkpoint intake, reviewed closeout, donor harvest, progression lift,
route forks, automation opportunity, diagnosis, repair, quest promotion, and
owner followthrough.

It does not own hook implementation, executable skill truth, proof verdicts,
memory canon, runtime activation, hidden scheduling, autonomous self-repair, or
owner-local acceptance.

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

## Post-change Route Review

After Growth Cycle changes, check whether the next agent can start from
`README.md`, `DIRECTION.md`, `PARTS.md`, and the relevant active part without
reading sibling logs or implementation histories.

Update `OWNER_MAP.md` when ownership changes, `OWNER_REQUESTS.md` when an owner
handoff changes, `ROADMAP.md` when future route pressure changes, and
`LANDING_LOG.md` when a checked landing changes.

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

## Closeout

Closeout must name changed Growth Cycle surfaces, source surfaces consulted
through `PROVENANCE.md`, owner requests affected, checks run, checks skipped,
remaining risk, and the next owner route if Growth Cycle was only a waypoint.
