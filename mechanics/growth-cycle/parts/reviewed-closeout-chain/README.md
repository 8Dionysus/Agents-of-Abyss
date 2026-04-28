# Reviewed Closeout Chain

Reviewed Closeout Chain keeps harvest, progression, memory, repair, quest, and
owner claims downstream of reviewed closeout.

## Use When

- A session or process wants to promote residue into a stronger object.
- A checkpoint note exists but has not been reviewed.
- Closeout evidence should determine the next stage.

## Do Not Use When

- The stage is only a live checkpoint with no review posture.
- The requested output is purely owner-local implementation.
- The claim can be validated only by `aoa-evals` or another owner.

## Route Check

Ask whether the reviewed closeout names evidence, boundaries, owner pressure,
and remaining risk. If not, return to checkpoint intake or stop.

## Active Outputs

- reviewed closeout route
- harvest eligibility
- progression eligibility
- diagnosis or repair route
- owner followthrough requirement

## Next Route

Route executable closeout bridge behavior to `aoa-skills`, closeout context
builders to `aoa-sdk`, proof questions to `aoa-evals`, and owner acceptance to
the target owner repository.
