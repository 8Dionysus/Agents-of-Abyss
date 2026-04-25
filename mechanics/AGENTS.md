# AGENTS.md

## Applies to

This card applies to `mechanics/` and every nested path under that scope until a nearer `AGENTS.md` narrows the lane.

## Read before editing

Read the repository root `AGENTS.md`, this card, and the nearest `README.md` or protocol surface before changing files in this lane.

## Closeout

Closeout must name changed surfaces, checks run, checks skipped, remaining risk, and the next owner route if this lane was only a waypoint.

This file applies to the root `mechanics/` tree.

## Role

`mechanics/` is the canonical home for center-level AoA mechanics that cross
layers, repositories, or future implementation surfaces.

It is not the home for constitutional law, repository ownership law, generated
truth, or owner-local implementation.

Mechanics packages explain how a kind of move grows, repeats, returns, gets
tested, becomes visible, or stays bounded. They must keep the owning repository
boundary explicit.

## Package law

Every `mechanics/<slug>/` package must contain:

- `AGENTS.md`
- `README.md`
- `ROADMAP.md`
- `LANDING_LOG.md`
- `docs/`

The package `README.md` is the mechanic entry card. It must contain the
mechanic card contract headings defined in `mechanics/README.md` and reflected
in `mechanics/registry.json`:

- `## Mechanic card`
- `### Trigger`
- `### Center owns`
- `### Stronger owner split`
- `### Inputs`
- `### Outputs`
- `### Must not claim`
- `### Validation`
- `### Next route`

The package `ROADMAP.md` is the forward contour. The package `LANDING_LOG.md`
is the checked landing ledger. The package `docs/` directory holds detailed
mechanic-owned doctrine, models, waves, handoffs, or support notes.

Mechanic packages may also own artifact homes:

- `schemas/`
- `examples/`
- `config/`
- `generated/`
- `scripts/`
- `tests/`

Use these homes when an artifact only makes sense inside the mechanic's owner
boundary. Keep root technical districts for repository-wide contracts only, as
defined by `mechanics/ARTIFACT_TOPOLOGY.md`.


## Owner-request law

Owner-request queue surfaces are center-side handoff contracts. They may name requests, stop-lines, source refs, proof routes, and next actions. They must not claim owner acceptance or owner-local landing without an owner-local receipt.

Required queue surfaces:

- `mechanics/OWNER_REQUEST_PROTOCOL.md`
- `mechanics/OWNER_REQUEST_QUEUE.md`
- `mechanics/owner-request-queue.json`
- `mechanics/<slug>/docs/*OWNER_REPO_REQUESTS.md`
- `generated/owner_request_queue.min.json`

When a mechanic output would become runtime, proof, memory, role, playbook, KAG, SDK, public projection, or ToS-authored meaning, route through the queue before changing owner-local surfaces.

## Boundaries

- `CHARTER.md`, `ECOSYSTEM_MAP.md`, `docs/FEDERATION_RULES.md`, `docs/LAYERS.md`, and `docs/REPO_ROLES.md` remain governance surfaces.
- `QUESTBOOK.md` remains a root public obligation index; `mechanics/questbook/` owns questbook mechanics.
- `quests/` remains the quest item store; lifecycle directories own source placement, and top-level `AOA-Q-*` aliases are intentionally absent.
- `docs/landings/` remains an archive and receipt district, not a canonical mechanic log.
- Generated card indexes reflect package entries; they do not author mechanic truth.

## Editing posture

When editing a mechanic:

1. Read this file, then the nearest `mechanics/<slug>/AGENTS.md`.
2. Keep the package `README.md` card synchronized with `mechanics/registry.json`.
3. Keep owner-local implementation claims out of center mechanics.
4. After the content change, review whether `DIRECTION.md`, `PARTS.md`, `ROADMAP.md`, `LANDING_LOG.md`, owner-request docs, validators, or generated indexes also changed in meaning.
5. Update `ROADMAP.md` when the change alters future work, route shape, unresolved owner pressure, or a mechanic's current contour.
6. Update the mechanic `LANDING_LOG.md` when a checked landing changes.
7. Update `mechanics/registry.json` when a package, owner boundary, card field, required surface, or validation route changes.
8. Rebuild the generated card index when card-facing registry fields change.
9. Rebuild the owner-request queue when request-facing registry or queue fields change.
10. Run `scripts/validate_mechanic_artifact_topology.py` when schemas,
    examples, config, generated artifacts, scripts, tests, or quest routing move
    between root districts and mechanic homes.

Do not touch these surfaces mechanically. The post-change review is a route check:
change only the files whose future-facing meaning actually moved.

## Validation

Run the narrow mechanic validators:

```bash
python scripts/validate_mechanic_readme_cards.py
python scripts/build_mechanic_card_index.py --check
python scripts/validate_mechanic_card_index.py
python scripts/validate_mechanics_topology.py
python scripts/validate_mechanic_artifact_topology.py
python scripts/validate_owner_request_queue.py
python scripts/build_owner_request_queue.py --check
python scripts/validate_generated_owner_request_queue.py
python scripts/validate_owner_request_docs.py
```

For release-bound mechanics changes, also run:

```bash
python scripts/validate_markdown_shape.py
python scripts/validate_mechanic_landing_logs.py
python scripts/validate_ecosystem.py
python -m pytest -q
```
