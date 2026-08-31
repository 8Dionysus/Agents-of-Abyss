# AGENTS.md

## Applies to

This card applies to `mechanics/` and every nested path under that scope until a nearer `AGENTS.md` narrows the lane.

## Read before editing

Select only the source, contract, or owner route that can change the interpretation of the named task.
A nearby human README is on-demand: use it when its explanation, package map, provenance, compatibility, or usage contract is material to the task.
Exact executable checks belong to the applicable `VALIDATION.md`, validated manifest, runner, or stronger owner procedure surface.
## Closeout

Closeout must name changed surfaces, checks run, checks skipped, remaining risk, and the next owner route if this lane was only a waypoint.

## Role

`mechanics/` is the canonical home for center-level AoA mechanics that cross
layers, repositories, or future implementation surfaces.

It is not the home for constitutional law, repository ownership law, generated
truth, or owner-local implementation.

Mechanics packages explain how a kind of move grows, repeats, returns, gets
tested, becomes visible, or stays bounded. They must keep the owning repository
boundary explicit.

## Root Markdown Split

Root `mechanics/*.md` files are route surfaces for the mechanics tree. Keep
their ownership narrow:

- `mechanics/AGENTS.md` owns mechanics-tree law, editing posture, closeout, and
  the compact validation entry route.
- `mechanics/README.md` owns the atlas, compass, route contract, and mechanic
  card contract.
- `mechanics/ARTIFACT_TOPOLOGY.md` owns artifact placement law for root
  technical districts versus mechanic homes.
- `mechanics/OWNER_REQUEST_PROTOCOL.md` owns owner-request fields, status and
  priority vocabulary, advancement rules, and queue stop-lines.
- `mechanics/OWNER_REQUEST_QUEUE.md` owns the human request index and package
  request routes.
- `mechanics/validation-routes.json` owns exact child-surface command argv;
  its runner and validator own lookup, execution, and route integrity.

Do not let these root files duplicate package doctrine. If a detail belongs to
one mechanic, route to that package's `README.md`, `DIRECTION.md`, `PARTS.md`,
`OWNER_MAP.md`, `OWNER_REQUESTS.md`, `PROVENANCE.md`, `LANDING_LOG.md`,
`ROADMAP.md`, `docs/`, or part-local surface.

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

The package `DIRECTION.md` owns current operating direction and should name the
source-of-truth split before giving route guidance. The package `PARTS.md`
owns the active part map and should describe active part contracts without
turning into a source-file inventory. The package `PROVENANCE.md` is the
active-first bridge back to historical accounting; it should tell agents to
start from current surfaces and use provenance only when source lineage must be
audited. The package `ROADMAP.md` is the forward contour, including a
condition-based "When Time Comes" block when future work is likely but not
ready. The package `LANDING_LOG.md` is the checked landing ledger and should
begin with a route index plus update contract when it grows beyond one entry.
The package `docs/` directory holds detailed mechanic-owned doctrine, models,
waves, handoffs, or support notes.

The package `AGENTS.md` is the local route law. It must name the active source
surfaces, the post-change route review, the closeout contract, and the local
validation route. It should follow the Experience-style shape without copying
Experience-specific meaning into other mechanics.

The package `README.md` should stay entry-card shaped: start with the mechanic
card, then route to active surfaces, functioning parts, owner-request queue,
historical provenance, owner boundary, and growth posture. It should not become
the deep doctrine store once `DIRECTION.md`, `PARTS.md`, `docs/`,
`PROVENANCE.md`, and `LANDING_LOG.md` already own those concerns.

Experience is the reference shape for `DIRECTION.md`, `PARTS.md`,
`PROVENANCE.md`, `ROADMAP.md`, and `LANDING_LOG.md` only when the Experience
surface is good for that document type. Check the reference first; copy the
role discipline, not Experience-specific meaning. If Experience lacks the
surface, as with `OWNER_MAP.md`, do not invent a forced parallel.

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
- `quests/` remains the quest item store; lane-first lifecycle directories own source placement, and top-level `AOA-Q-*` aliases are intentionally absent.
- Mechanic receipts remain in the owning `mechanics/<slug>/legacy/raw/` route and provenance bridge, not in empty docs districts.
- Generic repo movement traces may live in `docs/traces/`; mechanic-specific
  source traces stay in the owning mechanic's legacy/provenance route.
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
10. Use the mechanic artifact-topology validation route when schemas,
    examples, config, generated artifacts, scripts, tests, or quest routing move
    between root districts and mechanic homes.
11. Run a decision review when a mechanic change alters topology, owner split,
    workflow expectation, route law, validator authority, public contract, or a
    durable placement rule. Use `docs/decisions/AGENTS.md` when future agents
    need the rationale.

Do not touch these surfaces mechanically. The post-change review is a route check:
change only the files whose future-facing meaning actually moved.

## Validation

Run the narrow mechanic validators:

For release-bound mechanics changes, also run:

### Routed child validation

Child-specific commands are source-owned by `mechanics/validation-routes.json`.
Run the applicable validation route;
add `--show` to inspect the route without executing it.
