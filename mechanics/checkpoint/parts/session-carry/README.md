# Session Carry

Session Carry keeps mid-session checkpoint evidence reviewable without turning
it into candidate truth.

## Use When

- A commit, verify, PR, merge, pause, or owner-followthrough boundary should
  preserve evidence.
- A route has `cluster_ref`-level pressure but no reviewed `candidate_ref`.
- Closeout will need to know what survived the work slice.

## Do Not Use When

- The owner repository already accepted the object.
- The route needs proof, memory canon, or runtime activation.
- The evidence is only raw append history with no review posture.

## Route Check

Ask whether the checkpoint is still provisional. If yes, keep it in session
carry and name the next owner. If no, route to the stronger owner.

## Active Outputs

- checkpoint signal
- provisional owner hint
- evidence refs
- review-needed note
- closeout bridge candidate

## Next Route

Route controls and ledgers to `aoa-sdk`. Route checkpoint-note protocol to
`aoa-skills`. Route owner acceptance to the target owner repository.
