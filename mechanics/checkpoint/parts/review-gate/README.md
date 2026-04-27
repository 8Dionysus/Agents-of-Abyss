# Review Gate

Review Gate names when checkpoint evidence must stop and be reviewed before it
can shape promotion, mutation, return, or closeout.

## Use When

- A checkpoint note carries pending review.
- Self-agent or owner-sensitive work may continue only after approval.
- A route risks treating checkpoint hints as final truth.

## Do Not Use When

- The work is a tiny local edit with no checkpoint pressure.
- The owner repository already has a stronger explicit gate.
- The route is trying to use review wording to bypass proof.

## Route Check

Ask what would become unsafe if work continued without review. Name that
boundary and route it to the owner that can approve or reject it.

## Active Outputs

- review-needed state
- approval route
- rollback or safe-stop hint
- proof-needed hint
- owner escalation

## Next Route

Route actor posture to `aoa-agents`, bridge protocol to `aoa-skills`, and proof
questions to `aoa-evals`.
