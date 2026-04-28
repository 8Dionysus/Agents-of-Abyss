# Growth Cycle Parts

This file is the active map of functioning Growth Cycle parts. Each part owns
one bounded stage route. Sibling repositories own the local implementation and
meaning.

## Part Map

| Part | Center function | Stronger owner route |
|---|---|---|
| [Checkpoint Intake](parts/checkpoint-intake/README.md) | read checkpoint carry as provisional evidence and choose the next reviewed stage | `aoa-sdk`, `aoa-skills`, `aoa-agents` |
| [Reviewed Closeout Chain](parts/reviewed-closeout-chain/README.md) | require reviewed closeout before harvest, progression, repair, quest, or memory claims | `aoa-skills`, `aoa-sdk`, `aoa-evals` |
| [Donor Harvest](parts/donor-harvest/README.md) | route reusable residue into candidate owner shapes without minting final object truth | `aoa-skills`, `aoa-techniques`, `Dionysus`, final owner repos |
| [Progression Lift](parts/progression-lift/README.md) | lift evidence-backed movement without reducing growth to a universal score | `aoa-agents`, `aoa-evals`, `aoa-stats` |
| [Route Forks](parts/route-forks/README.md) | name material next choices, costs, risks, and stop conditions | `aoa-skills`, `aoa-playbooks`, `aoa-routing` |
| [Automation Opportunity](parts/automation-opportunity/README.md) | detect automation seeds without activating hidden schedulers | `aoa-skills`, `aoa-sdk`, `abyss-stack` |
| [Diagnosis Gate](parts/diagnosis-gate/README.md) | diagnose before repair and separate symptoms from causes | `aoa-skills`, `aoa-evals`, `aoa-agents` |
| [Repair Cycle](parts/repair-cycle/README.md) | route the smallest repair packet with rollback and proof boundaries | `aoa-skills`, `aoa-evals`, `abyss-stack` |
| [Quest Promotion](parts/quest-promotion/README.md) | decide whether repeated work becomes a public quest obligation | `aoa-playbooks`, `aoa-evals`, `mechanics/questbook` |
| [Owner Followthrough](parts/owner-followthrough/README.md) | carry unresolved pressure to owner requests, memo, stats, and next owner routes | target owner repositories |

## Active Part Contract

Every part keeps the same active-route shape:

- `## Use When`
- `## Do Not Use When`
- `## Route Check`
- `## Active Outputs`
- `## Next Route`

## Provenance Bridge

Use [PROVENANCE](PROVENANCE.md) when a Growth Cycle source must be audited.
Active part docs should not carry hook logs, generated summaries, or sibling
implementation histories.

## Validation

Use the validation lane in [mechanics/growth-cycle/AGENTS.md](AGENTS.md#validation) for executable commands.
