# Automation Opportunity

Automation Opportunity detects repeated work that may deserve automation
without activating a hidden scheduler.

## Use When

- Reviewed work repeats enough that a helper, hook, skill, or runtime route may
  reduce friction.
- Manual steps are stable enough to describe.
- The risk of automation can be named before implementation.

## Do Not Use When

- The repeated behavior is not yet understood.
- Automation would bypass review, proof, rollback, or owner approval.
- Runtime activation is needed before the runtime owner accepts it.

## Route Check

Ask what should remain manual, what can be safely suggested, what proof is
needed, and which owner owns the automation surface.

## Active Outputs

- automation opportunity note
- manual boundary
- owner request pressure
- proof request
- rollback or kill-switch hint

## Next Route

Route helper and hook behavior to `aoa-sdk`, executable automation workflows to
`aoa-skills`, runtime activation to `abyss-stack`, proof to `aoa-evals`, and
recurring scenario shape to `aoa-playbooks`.
