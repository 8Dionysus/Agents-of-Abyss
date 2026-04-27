# Candidate Lineage

Candidate Lineage keeps the growth chain readable across owners without making
the center the minting authority.

## Use When

- A growth object crosses checkpoint carry, reviewed candidate identity, seed
  staging, and final owner landing.
- Stage identity or owner responsibility is unclear.
- A validator or closeout needs the same biography across repositories.

## Do Not Use When

- The work is already final owner truth.
- A local repo only needs its own status vocabulary.
- The question is proof quality rather than stage ownership.

## Route Check

Restore the chain `cluster_ref -> candidate_ref -> seed_ref -> object_ref` and
ask which owner can honestly mint or resolve the current stage.

## Active Outputs

- Stage name.
- Owner route.
- Lineage continuity hint.
- Missing-stage or drift note.

## Next Route

Route provisional carry to `aoa-sdk`, reviewed candidate identity to
`aoa-skills`, seed staging to `Dionysus`, final object truth to the owner repo,
and proof questions to `aoa-evals`.
