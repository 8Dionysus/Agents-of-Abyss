# Repair Cycle

Repair Cycle routes the smallest honest repair packet after diagnosis.

## Use When

- Diagnosis found a bounded failure that can be repaired.
- The repair needs rollback, proof, checkpoint, or owner handoff boundaries.
- The same failure may teach the process something durable.

## Do Not Use When

- Diagnosis is missing.
- Repair would hide a failed proof, broken owner boundary, or runtime risk.
- The center would need to claim implementation ownership.

## Route Check

Ask what is the smallest repair, how it rolls back, who proves it, and what
lesson should survive after the repair.

## Active Outputs

- repair route
- rollback hint
- proof request
- owner handoff
- memory lesson candidate

## Next Route

Route executable repair workflows to `aoa-skills`, proof and regression to
`aoa-evals`, runtime repair to `abyss-stack`, memory lessons to `aoa-memo`, and
owner acceptance to the target owner repository.
