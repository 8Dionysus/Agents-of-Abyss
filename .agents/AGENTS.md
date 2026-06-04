# AGENTS.md

## Applies to

This card applies to `.agents/` and all descendants unless a nearer `AGENTS.md` narrows the path.

## Role

`.agents/` holds agent-lane skills, prompts, Codex Spark lanes, and local agent
assets that help models operate inside this repository.

## Read before editing

Read root `AGENTS.md`, then inspect any local skill README, lane README, or
manifest before changing prompt-like material.

For Codex Spark work, read `.agents/spark/AGENTS.md` and
`.agents/spark/registry.json`.

Use the nearest README for local file purpose. Use source docs, schemas, generated builders, validators, and owner repos as stronger authority when they apply.

## Boundaries

- Do not encode private memory, hidden authority, or unreviewable autonomy here.
- Do not make this lane the source of constitutional law, owner truth, or runtime state.
- Do not add prompt material that bypasses center route modes, validation, or owner boundaries.

## Validation

Run the narrowest relevant checks first. Usual checks for this district:

```bash
python scripts/agents_mesh/validate_agents_md_shape.py
python scripts/agents_mesh/validate_agents_mesh.py
python .agents/spark/scripts/validate_spark_lane.py
```

If a listed validator is not present in the checkout yet, report that explicitly and run the closest available guardrail.

## Closeout

Report changed files, source surfaces consulted, generated files rebuilt or not rebuilt, checks run, checks skipped, and any owner boundary that may need follow-up.
