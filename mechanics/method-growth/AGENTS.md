# AGENTS.md

## Applies to

This card applies to `mechanics/method-growth/` and every nested path under
that scope until a nearer `AGENTS.md` narrows the lane.

## Read before editing

Read the repository root `AGENTS.md`, `mechanics/AGENTS.md`, this card,
`README.md`, `DIRECTION.md`, `PARTS.md`, and the nearest source surface before
changing files in this lane.

## Role

Method-growth owns the center route from repeated work into donor refinement,
candidates, seeds, owner landings, pruning, methods, proofs, memory, derived
summaries, and closeout posture.

It does not own final object truth for specialized repositories.

## Boundaries

- Do not use this lane to override owner-local truth, generated-source
  boundaries, sibling-repo authority, release validation contracts, proof
  verdicts, memory canon, runtime activation, or ToS-authored meaning.
- Do not mint `candidate_ref`, `seed_ref`, or `object_ref` in the center.
  `aoa-skills`, `Dionysus`, and the final owner repository own those stages.
- Keep active parts light and route-shaped. Put deeper doctrine in `docs/`,
  historical lineage in `PROVENANCE.md`, and owner-local requests in
  `OWNER_REQUESTS.md`.
- If a real owner-local landing request changes, update
  `mechanics/owner-request-queue.json`, rebuild its generated companion, and
  keep the package request doc synchronized.

## Validation

Run the narrow package lane after changing Method-growth surfaces:

```bash
python mechanics/method-growth/scripts/validate_method_growth_mechanic.py
python scripts/validate_mechanics_topology.py --mechanic method-growth
python scripts/validate_mechanic_readme_cards.py --mechanic method-growth
python scripts/validate_owner_request_queue.py --mechanic method-growth
python scripts/validate_owner_request_docs.py --mechanic method-growth
python scripts/validate_mechanic_artifact_topology.py --mechanic method-growth
python scripts/validate_mechanic_landing_logs.py --mechanic method-growth
```

Run lineage witnesses when the growth-refinery chain changes:

```bash
python mechanics/method-growth/scripts/validate_candidate_lineage_contract.py --workspace-root /srv
python mechanics/method-growth/scripts/validate_wave4_kernel_automation.py --workspace-root /srv
```

Run generated checks when registry, owner requests, or AGENTS surfaces change:

```bash
python scripts/build_mechanic_card_index.py --check
python scripts/validate_mechanic_card_index.py
python scripts/build_owner_request_queue.py --check
python scripts/validate_generated_owner_request_queue.py
python scripts/build_agents_mesh_index.py --check
python scripts/validate_agents_mesh_index.py
```

<!-- centralized-child-validation:start -->

### Centralized Child Validation

Executable validation commands from child docs live here. Child docs should
route to this section instead of carrying command blocks.

#### `mechanics/method-growth/README.md`

```bash
python mechanics/method-growth/scripts/validate_method_growth_mechanic.py
python scripts/validate_mechanics_topology.py --mechanic method-growth
python scripts/validate_mechanic_readme_cards.py --mechanic method-growth
python scripts/build_mechanic_card_index.py --check
python scripts/validate_mechanic_card_index.py
python scripts/validate_owner_request_queue.py --mechanic method-growth
python scripts/build_owner_request_queue.py --check
python scripts/validate_generated_owner_request_queue.py
python scripts/validate_owner_request_docs.py --mechanic method-growth
python scripts/validate_mechanic_landing_logs.py --mechanic method-growth
```

#### `mechanics/method-growth/OWNER_REQUESTS.md`

```bash
python scripts/validate_owner_request_queue.py --mechanic method-growth
python scripts/build_owner_request_queue.py --check
python scripts/validate_generated_owner_request_queue.py
python scripts/validate_owner_request_docs.py --mechanic method-growth
python mechanics/method-growth/scripts/validate_method_growth_mechanic.py
```

#### `mechanics/method-growth/docs/REVIEWABLE_GROWTH_REFINERY.md`

```bash
python mechanics/method-growth/scripts/validate_candidate_lineage_contract.py --workspace-root /srv
python mechanics/method-growth/scripts/validate_wave4_kernel_automation.py --workspace-root /srv
```

<!-- centralized-child-validation:end -->

## Closeout

Closeout must name changed active parts, whether `PROVENANCE.md` was consulted,
owner requests affected, checks run, checks skipped, remaining risk, and the
next owner route if this lane was only a waypoint.
