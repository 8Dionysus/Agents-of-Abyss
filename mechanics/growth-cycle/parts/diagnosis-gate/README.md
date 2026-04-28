# Diagnosis Gate

Diagnosis Gate requires cause-reading before repair.

## Use When

- A process failed, drifted, repeated friction, or produced confusing output.
- Repair is tempting but the cause is not yet known.
- The next move needs evidence before mutation.

## Do Not Use When

- The cause is already proven and the owner has a repair route.
- The change is a simple local fix with no lifecycle meaning.
- The route needs eval-owned verdict rather than center diagnosis.

## Route Check

Separate symptom, probable cause, evidence, affected owner, and what would
disprove the diagnosis.

## Active Outputs

- diagnosis route
- symptom and cause split
- evidence refs
- repair eligibility
- proof or owner handoff request

## Next Route

Route diagnosis skills to `aoa-skills`, proof and regression reading to
`aoa-evals`, actor health posture to `aoa-agents`, and local repair ownership
to the repository that owns the failing surface.
