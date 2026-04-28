# AGENTS.md

## Applies to

This card applies to `mechanics/recurrence/` and every nested path under that
scope until a nearer `AGENTS.md` narrows the lane.

## Read before editing

Read the repository root `AGENTS.md`, `mechanics/AGENTS.md`, this card,
`README.md`, `DIRECTION.md`, `PARTS.md`, and the nearest nested route surface
before changing files in this lane.

Read `PROVENANCE.md` only when you need source lineage, sibling evidence, or a
receipt trail. Do not pull provenance inventories into active part docs.

## Role

Recurrence owns bounded return, anchor recovery, re-entry, continuity windows,
component refresh law, control-plane carry boundaries, runtime-return
stop-lines, and recursor-readiness stop-lines.

It names the route and the law. It does not become the owner-local
implementation, proof verdict, memory canon, runtime behavior, or self-spawn
authority.

## Boundaries

- Do not override owner-local truth, generated-source boundaries, sibling-repo
  authority, runtime policy, memory canon, proof verdicts, release validation,
  or ToS-authored meaning.
- Do not claim ambient continuity, hidden memory sovereignty, runtime
  self-healing, or automatic recursor spawn.
- Keep active parts short and routed. Deep source trails belong in
  `PROVENANCE.md`; owner-local asks belong in `OWNER_REQUESTS.md`.
- Agon-specific recurrence files remain under `mechanics/agon/`.

## Closeout

Closeout must name changed active parts, whether `PROVENANCE.md` was consulted,
owner requests affected, checks run, checks skipped, remaining risk, and the
next owner route if this lane was only a waypoint.

If `PROVENANCE.md` was consulted, name only the relevant return, continuity,
or receipt section. Do not enumerate sibling histories unless the task
specifically audited that evidence in depth.

## Source Surfaces

- `README.md`: package entry and route.
- `DIRECTION.md`: current active mechanic direction.
- `PARTS.md`: active functioning-part map.
- `parts/`: concise active recurrence contracts.
- `OWNER_MAP.md`: recurrence owner boundary and stronger-owner split.
- `OWNER_REQUESTS.md`: center-side owner request packet.
- `ROADMAP.md`: current and next recurrence contour.
- `LANDING_LOG.md`: checked recurrence landing ledger.
- `PROVENANCE.md`: controlled bridge to source evidence.
- `docs/`: detailed doctrine and support notes.

## Post-change route review

After any recurrence change, check whether the next agent can start from
`README.md`, `DIRECTION.md`, `PARTS.md`, and the relevant active part without
opening sibling history or raw evidence.

Check whether the move changed:

- `DIRECTION.md`: current return, continuity, or re-entry posture.
- `PARTS.md`: active part boundaries or functioning-part map.
- `OWNER_MAP.md`: owner boundary, stop-line, or handoff target.
- `OWNER_REQUESTS.md` and `mechanics/owner-request-queue.json`: runtime,
  memory, proof, role, route, SDK, or owner-local asks.
- `ROADMAP.md`: future route pressure or unresolved recurrence contour.
- `LANDING_LOG.md`: a checked landing or planted contract.
- `PROVENANCE.md`: source bridge, receipt route, or archive map.
- `mechanics/registry.json` and generated indexes: card-facing route, owner
  boundary, validation refs, or public summaries.

Only update a surface when its meaning moved. Leave it untouched when the
change does not affect its job.

## Validation

Run the recurrence package validator after package changes:

```bash
python mechanics/recurrence/scripts/validate_recurrence_mechanic.py
python -m pytest -q mechanics/recurrence/tests/test_recurrence_mechanic.py
```

For registry, card, queue, or release-facing changes, also use the relevant
commands below.

<!-- centralized-child-validation:start -->

### Centralized Child Validation

Executable validation commands from child docs live here. Child docs should
route to this section instead of carrying command blocks.

#### `mechanics/recurrence/README.md`

```bash
python mechanics/recurrence/scripts/validate_recurrence_mechanic.py
python -m pytest -q mechanics/recurrence/tests/test_recurrence_mechanic.py
python scripts/validate_mechanics_topology.py --mechanic recurrence
python scripts/validate_mechanic_readme_cards.py --mechanic recurrence
python scripts/build_mechanic_card_index.py --check
python scripts/validate_mechanic_card_index.py
python scripts/validate_owner_request_queue.py --mechanic recurrence
python scripts/build_owner_request_queue.py --check
python scripts/validate_generated_owner_request_queue.py
python scripts/validate_owner_request_docs.py --mechanic recurrence
```

#### `mechanics/recurrence/PARTS.md`

```bash
python mechanics/recurrence/scripts/validate_recurrence_mechanic.py
python -m pytest -q mechanics/recurrence/tests/test_recurrence_mechanic.py
```

<!-- centralized-child-validation:end -->
