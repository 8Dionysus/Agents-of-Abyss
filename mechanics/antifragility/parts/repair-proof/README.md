# Repair Proof

Repair proof prevents cleanup stories from hardening before evidence exists.

## Use When

- A repair, subtraction, anti-authority change, or degraded-mode adjustment is
  claimed to improve the system.
- A public release or roadmap note wants to say a fragility was fixed.
- Regression risk needs bounded proof before promotion.

## Do Not Use When

- The claim is only a route suggestion.
- Owner receipts do not exist yet.
- The work is a memory lesson rather than a proof verdict.

## Route Check

Name the claim, the evidence needed, the regression risk, the owner receipt, and
what `aoa-evals` must decide.

## Active Outputs

- Proof request.
- Regression question.
- Public-claim stop-line.
- Owner evidence gap.

## Next Route

Route proof to `aoa-evals`. Do not publish repair success until proof or an
explicitly bounded receipt supports the claim.
