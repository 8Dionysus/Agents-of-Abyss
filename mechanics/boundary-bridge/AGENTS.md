# AGENTS.md

## Applies to

This card applies to `mechanics/boundary-bridge/` and every nested path under
that scope until a nearer `AGENTS.md` narrows the lane.

## Read before editing

Read root `AGENTS.md`, `mechanics/AGENTS.md`, this card, and
`mechanics/boundary-bridge/README.md` before changing files in this lane.

## Role

Boundary bridge owns AoA center doctrine for crossing owner boundaries without
identity collapse, authority transfer, or hidden implementation claim.

It may describe support, counterpart edges, ToS support, witness/compost
routes, derived projections, owner handoffs, proof routes, and compatibility
routes.

It does not author ToS meaning, owner-local implementation truth, KAG source
authority, routing meaning, memory truth, proof verdicts, runtime behavior, or
public projection authority.

## Boundaries

- Name both sides of a bridge before changing the bridge.
- Keep the owner that authors truth stronger than the bridge that points to it.
- Do not treat `support`, `analogy`, `projection`, or `compatibility` as proof
  of identity.
- Keep ToS-authored meaning in `Tree-of-Sophia`.
- Keep derived projection in `aoa-kag`, route behavior in `aoa-routing`,
  memory and witness objects in `aoa-memo`, proof in `aoa-evals`, and
  choreography in `aoa-playbooks`.
- If the bridge creates an owner-local request, update
  `OWNER_REQUESTS.md`, `mechanics/owner-request-queue.json`, and generated
  owner-request companions.
- If a new recurring bridge shape appears, update `PARTS.md`, `OWNER_MAP.md`,
  `PROVENANCE.md`, `LANDING_LOG.md`, and `ROADMAP.md` only when their future
  meaning actually changes.

## Validation

Run the narrow package lane after boundary-bridge changes:

```bash
python mechanics/boundary-bridge/scripts/validate_boundary_bridge_distillation.py
python scripts/validate_mechanics_topology.py --mechanic boundary-bridge
python scripts/validate_mechanic_readme_cards.py --mechanic boundary-bridge
python scripts/validate_mechanic_landing_logs.py --mechanic boundary-bridge
python scripts/validate_owner_request_queue.py --mechanic boundary-bridge
python scripts/build_owner_request_queue.py --check
python scripts/validate_generated_owner_request_queue.py
python scripts/validate_owner_request_docs.py --mechanic boundary-bridge
python scripts/build_mechanic_card_index.py --check
python scripts/validate_mechanic_card_index.py
```

For release-facing changes, also run `python scripts/release_check.py`.

<!-- centralized-child-validation:start -->

### Centralized Child Validation

Executable validation commands from child docs live here. Child docs should
route to this section instead of carrying command blocks.

#### `mechanics/boundary-bridge/README.md`

```bash
python mechanics/boundary-bridge/scripts/validate_boundary_bridge_distillation.py
python scripts/validate_mechanics_topology.py --mechanic boundary-bridge
python scripts/validate_mechanic_readme_cards.py --mechanic boundary-bridge
python scripts/build_mechanic_card_index.py --check
python scripts/validate_mechanic_card_index.py
python scripts/validate_owner_request_queue.py --mechanic boundary-bridge
python scripts/build_owner_request_queue.py --check
python scripts/validate_generated_owner_request_queue.py
python scripts/validate_owner_request_docs.py --mechanic boundary-bridge
python scripts/validate_mechanic_landing_logs.py --mechanic boundary-bridge
```

<!-- centralized-child-validation:end -->

## Closeout

Closeout must name changed active parts, source doctrine consulted through
`PROVENANCE.md`, owner requests affected, checks run, checks skipped,
remaining risk, and the next owner route if this lane was only a waypoint.
