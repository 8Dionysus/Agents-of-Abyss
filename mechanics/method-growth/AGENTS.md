# AGENTS.md

## Applies to

This card applies to `mechanics/method-growth/` and every nested path under that scope until a nearer `AGENTS.md` narrows the lane.

## Read before editing

Read the repository root `AGENTS.md`, this card, and the nearest `README.md` or protocol surface before changing files in this lane.

## Boundaries

Do not use this lane to override owner-local truth, generated-source boundaries, sibling-repo authority, or release validation contracts.


## Closeout

Closeout must name changed surfaces, checks run, checks skipped, remaining risk, and the next owner route if this lane was only a waypoint.

This file applies to `mechanics/method-growth/`.

## Role

Method-growth owns the center route from repeated work into candidates, seeds,
owner landings, methods, proofs, memory, and derived summaries.

It does not own final object truth for specialized repositories.

## Validation

Run `python scripts/validate_mechanics_topology.py --mechanic method-growth`
after package changes.
Run candidate-lineage validators when the moved docs name them.

<!-- centralized-child-validation:start -->

### Centralized Child Validation

Executable validation commands from child docs live here. Child docs should
route to this section instead of carrying command blocks.

#### `mechanics/method-growth/README.md`

```bash
python scripts/validate_mechanics_topology.py --mechanic method-growth
python scripts/validate_mechanic_readme_cards.py --mechanic method-growth
python scripts/build_mechanic_card_index.py --check
python scripts/validate_mechanic_card_index.py
python scripts/validate_owner_request_queue.py --mechanic method-growth
python scripts/build_owner_request_queue.py --check
python scripts/validate_generated_owner_request_queue.py
python scripts/validate_owner_request_docs.py --mechanic method-growth
```

<!-- centralized-child-validation:end -->
