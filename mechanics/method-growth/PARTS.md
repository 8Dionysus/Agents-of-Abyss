# Method-growth Parts

This file is the active map of functioning Method-growth parts. Each part owns
one bounded center route shape. Sibling repositories own their local
implementation and meaning.

## Part Map

| Part | Center function | Stronger owner route |
|---|---|---|
| [Donor Refinery](parts/donor-refinery/README.md) | extract reusable pattern while keeping provenance and rejecting contamination | source owner, `aoa-techniques`, `aoa-skills`, and `aoa-playbooks` own local objects |
| [Candidate Lineage](parts/candidate-lineage/README.md) | keep `cluster_ref -> candidate_ref -> seed_ref -> object_ref` readable without minting identities in the center | `aoa-sdk`, `aoa-skills`, `Dionysus`, and final owner repos own stage identity |
| [Owner Landing](parts/owner-landing/README.md) | route reviewed candidates into owner-local acceptance, landing, or receipt posture | final owner repos own landed object truth |
| [Pruning](parts/pruning/README.md) | make reanchor, merge, defer, drop, and supersession explicit | owner repos, `aoa-memo`, and `aoa-stats` own local receipts and derived summaries |
| [Proof Route](parts/proof-route/README.md) | keep growth claims weaker than evidence until eval owners land proof | `aoa-evals` owns verdict and regression posture |
| [Method Promotion](parts/method-promotion/README.md) | route stable scenario-level repetition into playbook-owned method | `aoa-playbooks` owns recurring choreography |
| [Technique Skill Split](parts/technique-skill-split/README.md) | separate reusable practice from bounded execution before promotion | `aoa-techniques` owns technique; `aoa-skills` owns skill |
| [Memory Writeback](parts/memory-writeback/README.md) | route lessons and retention reasons without turning center prose into memory | `aoa-memo` owns memory objects and recall contracts |
| [Maturity Ladder](parts/maturity-ladder/README.md) | use shared maturity language for cross-repo legibility without forcing local status names | owner repos keep local status vocabulary; release support governs public claims |
| [Growth Closeout](parts/growth-closeout/README.md) | close a growth lane with changed parts, provenance use, owner requests, checks, risk, and next route | final owner, proof, memory, stats, or playbook owners receive the next packet |

## Active Part Contract

Every part keeps three working surfaces:

- `README.md`: when to use the part.
- `CONTRACT.md`: center boundary, allowed outputs, and stop-lines.
- `VALIDATION.md`: validation route, with executable commands centralized in
  `parts/AGENTS.md`.

Every part should keep the same active-route shape:

- `## Use When`
- `## Do Not Use When`
- `## Route Check`
- `## Active Outputs`
- `## Next Route`

## Provenance Bridge

Use [PROVENANCE](PROVENANCE.md) when a Method-growth source must be audited.
Active part docs should not carry sibling inventories, old receipt inventories,
or raw history.

## Validation

Use the validation lane in [mechanics/method-growth/AGENTS.md](AGENTS.md#validation)
for package commands and [parts/AGENTS.md](parts/AGENTS.md#validation) for part
commands.
