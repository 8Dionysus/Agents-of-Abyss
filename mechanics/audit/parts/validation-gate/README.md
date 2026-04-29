# Validation Gate

## Use When

Use this part when an audit needs to report checks run, checks skipped, blind spots, stale generated surfaces, or residual risk.

## Do Not Use When

Use `aoa-evals` when the validation result must become a proof verdict or comparison result.

## Route Check

Name the check, source, result, skipped check, reason, and residual risk.

## Active Outputs

- validation report
- skipped-check note
- stale-generated note
- residual-risk note
- proof route hint

## Next Route

Route proof-quality claims to `aoa-evals`; route generated freshness issues to the generator owner.
