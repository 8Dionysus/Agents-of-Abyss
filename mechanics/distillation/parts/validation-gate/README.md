# Validation Gate

Use this part to check whether a distillation stayed honest.

## Use When

- A source was converted into active form.
- A distillation may have lost provenance, review state, or owner boundary.
- A public or release-facing claim depends on the conversion.

## Do Not Use When

- The task needs proof of final object quality; route that to `aoa-evals`.
- The output is still raw and has not been extracted.

## Route Check

Check source route, review state, active function, owner boundary, and stop-line
against authority inflation.

## Active Outputs

- Validation note.
- Failed-gate reason.
- Owner proof request when needed.

## Next Route

Use `aoa-evals` for verdict strength and `release-support` for public claim
support.
