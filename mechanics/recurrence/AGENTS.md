# AGENTS.md

## Applies to

This card applies to `mechanics/recurrence/` and every nested path under that scope until a nearer `AGENTS.md` narrows the lane.

## Read before editing

Read the repository root `AGENTS.md`, this card, and the nearest `README.md` or protocol surface before changing files in this lane.

## Boundaries

Do not use this lane to override owner-local truth, generated-source boundaries, sibling-repo authority, or release validation contracts.


## Closeout

Closeout must name changed surfaces, checks run, checks skipped, remaining risk, and the next owner route if this lane was only a waypoint.

This file applies to `mechanics/recurrence/`.

## Role

Recurrence owns bounded return, re-entry, continuity, and component refresh law.

Agon-specific recurrence files remain under `mechanics/agon/`.

## Validation

Run `python scripts/validate_mechanics_topology.py --mechanic recurrence` after
package changes.

<!-- centralized-child-validation:start -->

### Centralized Child Validation

Executable validation commands from child docs live here. Child docs should
route to this section instead of carrying command blocks.

#### `mechanics/recurrence/README.md`

```bash
python scripts/validate_mechanics_topology.py --mechanic recurrence
python scripts/validate_mechanic_readme_cards.py --mechanic recurrence
python scripts/build_mechanic_card_index.py --check
python scripts/validate_mechanic_card_index.py
python scripts/validate_owner_request_queue.py --mechanic recurrence
python scripts/build_owner_request_queue.py --check
python scripts/validate_generated_owner_request_queue.py
python scripts/validate_owner_request_docs.py --mechanic recurrence
```

<!-- centralized-child-validation:end -->
