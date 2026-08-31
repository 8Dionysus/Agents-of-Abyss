# AGENTS.md

## Applies to

This card applies to `.agents/spark/` and every nested path under that scope until a
nearer `AGENTS.md` narrows the lane.

## Role

`.agents/spark/` is the fast session lane for GPT-5.3-Codex-Spark style work. It
stores session-contained scenarios, launch prompts, result contracts, handoff
contracts, and validation for small bounded loops.

Spark is an agent lane, not a new source of constitutional authority.
Its core execution rule is done-or-handoff.

## Read before editing

Select only the source, contract, or owner route that can change the interpretation of the named task.
A nearby human README is on-demand: use it when its explanation, package map, provenance, compatibility, or usage contract is material to the task.
Exact executable checks belong to the applicable `VALIDATION.md`, validated manifest, runner, or stronger owner procedure surface.
## Boundaries

- One Spark session uses one scenario and one bounded scope.
- A Spark session must end as `done` or `handoff`; do not depend on an
  in-session switch to a larger model.
- If the task needs deeper architecture, owner-local judgment, or broad
  synthesis, leave a portable handoff in `.agents/spark/handoffs/open/`.
- Store reusable completed evidence in `.agents/spark/results/` only when it will help a
  later session; ordinary closeout stays in the conversation or PR.
- Do not use Spark to override owner-local truth, generated-source boundaries,
  sibling-repo authority, release validation contracts, or mechanic law.
- Do not turn `.agents/spark/` into a mechanic package. It is a launch and handoff lane
  for work that belongs to existing owners.

## Scenario Law

Every scenario must be registered in `.agents/spark/registry.json` and must provide:

- `README.md` with scope, done signal, stop-line, and handoff route
- `PROMPT.md` that can launch a standalone Spark session
- `templates/result.md`
- `templates/handoff.md`
- `examples/result.example.md`

## Validation

Run the narrowest relevant checks first. Usual checks for this lane:

For release-facing Spark lane changes, also run:

## Closeout

Report scenario registry entries changed, scenario files touched, handoffs or
results added, validation run, validation skipped, remaining risk, and the next
owner route when Spark was only a waypoint.

## Local note

Spark should act as a fast center-layer gardener: prune, align, clarify, test,
or route. It stops when the scoped lane is done, and it hands off when the work
needs a slower session.
