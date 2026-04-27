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

## Closeout

Closeout must name changed active parts, owner requests affected, whether
`PROVENANCE.md` was actually consulted, checks run, checks skipped, remaining
risk, and the next owner route if this lane was only a waypoint.
