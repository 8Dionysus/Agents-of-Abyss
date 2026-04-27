# Continuity Window

Continuity Window keeps self-agency continuity tied to explicit revision
windows, reanchor decisions, and anchor artifacts.

## Use When

- A route needs duration across more than one pass.
- A revision window must stay reviewable.
- Drift requires a named reanchor event.

## Do Not Use When

- Continuity is being claimed from memory feel or transcript length.
- The route cannot name `continuity_ref`, `revision_window_ref`,
  `reanchor_ref`, and `anchor_artifact_ref`.
- The next owner should be proof, memory, or playbook instead.

## Route Check

Ask whether the continuity chain is explicit:
`continuity_ref -> revision_window_ref -> reanchor_ref -> anchor_artifact_ref`.
If not, return to the last valid anchor or safe-stop.

## Active Outputs

- continuity route
- revision-window boundary
- reanchor request
- anchor-artifact route
- owner handoff

## Next Route

Route role-facing continuity to `aoa-agents`, choreography to `aoa-playbooks`,
writeback support to `aoa-memo`, proof to `aoa-evals`, and hint carry to
`aoa-sdk`.
