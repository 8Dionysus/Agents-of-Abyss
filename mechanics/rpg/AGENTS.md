# AGENTS.md

## Applies to

This card applies to `mechanics/rpg/` and every nested path under that scope
until a nearer `AGENTS.md` narrows the lane.

## Read before editing

Read `DIRECTION.md`, `PARTS.md`, and the relevant owner route only when RPG meaning changes.
## Boundaries

- Do not turn RPG terms into hidden ontology, runtime ledger authority, role canon, proof verdicts, or quest ownership.
- Do not let presentation labels replace canonical machine keys.
- Do not treat generated RPG artifacts as authored meaning; they must mirror the terminology and schema contract.
- Do not cite closed historical sources as active law; distill needed material into a part and record the immutable Git path in provenance.
- If RPG creates a stronger-owner request, update `mechanics/rpg/OWNER_REQUESTS.md` and the owner-request queue surfaces instead of pretending the owner accepted it.

## Closeout


Closeout must name changed RPG active parts, whether `PROVENANCE.md` was
consulted, whether vocabulary or owner requests changed, checks run, checks
skipped, remaining risk, and the next owner route if RPG was only a reflection
waypoint.

If `PROVENANCE.md` was consulted, name only the relevant legacy map,
distillation log, or receipt section. Do not enumerate raw legacy sources
unless the task specifically audited archive evidence in depth.

## Role

RPG owns adjunct reflection for progression, questlines, campaigns, skills,
feats, unlock proof, and readable navigation.

It makes cross-owner work easier to see without changing the owner of roles,
skills, playbooks, proof, quests, runtime state, or source meaning.

## Source Surfaces

- `README.md`: package entry and route.
- `DIRECTION.md`: current active mechanic direction.
- `USAGE.md`: active usage posture.
- `PARTS.md`: active functioning-part map.
- `parts/`: concise active RPG contracts.
- `OWNER_REQUESTS.md`: center-side owner request packet.
- `ROADMAP.md`: current and next RPG contour.
- `LANDING_LOG.md`: checked RPG landing ledger.
- `PROVENANCE.md`: controlled bridge to immutable Git history and current source accounting.
- Optional content-bearing `docs/` may hold detailed doctrine and support notes;
  historical material is reached through `PROVENANCE.md` and immutable Git history.

## Post-change route review

After RPG changes, check whether the next agent can start from the current
inherited `AGENTS.md` card, then `DIRECTION.md`, `USAGE.md`, `PARTS.md`, and the
relevant active part without reading raw legacy.
If an active part needs history, distill the rule into the part and route the evidence through `PROVENANCE.md` and the immutable owner Git path.

Check whether the move changed:

- `DIRECTION.md`: current RPG posture or language boundary.
- `USAGE.md`: usage route, task-reading route, or reflection posture.
- `PARTS.md`: active part boundaries or functioning-part map.
- `OWNER_REQUESTS.md` and `mechanics/owner-request-queue.json`: role, skill,
  playbook, proof, quest, runtime, or owner-local asks.
- `ROADMAP.md`: useful future route or unresolved RPG contour.
- `LANDING_LOG.md`: a reviewable landing or planted contract.
- `PROVENANCE.md`: immutable Git bridge, receipt route, or current source map.
- vocabulary artifacts: terminology, schema, example, generated overlay, or
  validator surfaces.
- `mechanics/registry.json` and generated indexes: card-facing route, owner
  boundary, validation refs, or public summaries.

Only update a surface when its meaning moved. Leave it untouched when the
change does not affect its job.

## Validation

Child routes remain keyed by `mechanics/validation-routes.json`.

The narrow RPG package route is defined in the repository [`VALIDATION.md`](../../VALIDATION.md).

The owner-request route for RPG changes is defined in the repository [`VALIDATION.md`](../../VALIDATION.md).

The release route for release-readiness or cross-mechanic edits is defined in the repository [`VALIDATION.md`](../../VALIDATION.md).
