# Boundary Contract

Use this part before any bridge is treated as valid.

## Function

Name the two sides of a crossing, what each owner owns, what bridge mode is
being used, and what must not transfer.

## Inputs

- source owner
- receiving or derived owner
- bridge mode
- source surfaces
- no-transfer rule

## Outputs

- one sentence naming the bridge
- owner split
- stop-lines
- next owner route

## Stop-lines

- no unnamed owner
- no bridge without a no-transfer rule
- no convenience transfer of source truth

## Validation

Use the validation lane in [../../AGENTS.md](../../AGENTS.md#validation).
