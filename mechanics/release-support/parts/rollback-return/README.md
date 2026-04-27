# Rollback Return

Use this part when a transition must keep a visible path back.

## Use When

- A release, landing, owner handoff, public claim, generated update, or
  maturity change would be painful to reverse if wrong.
- A staged change needs rollback wording before it becomes public.

## Do Not Use When

- The change is strictly additive and has no state or public claim impact.
- The rollback is runtime-owned and must be handled by `abyss-stack`.

## Route Check

Name what reverts, what evidence triggers rollback, what remains preserved, and
which owner must execute the return.

## Active Outputs

- Rollback condition.
- Return route.
- Preserved evidence/provenance note.
- Owner stop-line.

## Next Route

Route runtime rollback to `abyss-stack`, proof-triggered rollback to
`aoa-evals`, and public projection rollback to `8Dionysus`.
