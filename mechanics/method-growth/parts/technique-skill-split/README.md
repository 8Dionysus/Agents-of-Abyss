# Technique Skill Split

Technique Skill Split separates reusable practice from bounded execution before
growth objects are promoted.

## Use When

- A repeated move could be either a technique, a skill, or both.
- Reusable practice is being mixed with execution procedure.
- A future owner pass needs a clean packet for `aoa-techniques` or `aoa-skills`.

## Do Not Use When

- The owner repository already cleanly owns the object.
- The route is scenario-level and belongs first in `aoa-playbooks`.
- The route only needs proof or memory.

## Route Check

Ask whether the object teaches reusable practice, performs bounded execution,
or composes a scenario. Split the request before promotion.

## Active Outputs

- Technique request.
- Skill request.
- Split rationale.
- Shared evidence route.

## Next Route

Route reusable practice to `aoa-techniques`, bounded execution to `aoa-skills`,
scenario method to `aoa-playbooks`, and claim proof to `aoa-evals`.
