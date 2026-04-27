# RPG Usage Contract

This is the active decision surface for using RPG language in AoA work.
Use it before attaching game-shaped terms to a task, quest, route, proof claim, or runtime idea.

RPG language is allowed when it makes the work more legible, consequential, and owner-routable.
Plain repository language wins when it is clearer.

## Use RPG When

- it clarifies who acts, from which role or origin, and under which owner boundary
- it makes a quest, campaign, party, stake, proof route, consequence, reputation, or unlock easier to judge
- it helps a future agent remember what changed and what should follow
- it preserves canonical keys, source refs, and proof routes while adding a readable reflection

## Use Plain Repo Language When

- the work is a direct code, docs, config, validation, or release task with no added routing value from RPG terms
- a label would decorate the task without changing the owner route, proof route, memory route, or consequence
- the RPG term would imply runtime state, role canon, proof verdict, quest closure, or owner acceptance
- the source owner already has a clearer local vocabulary for the task

## Decision Table

| Pressure | RPG reading allowed | First route | Must not claim |
|---|---|---|---|
| ordinary repo work | no, unless it changes route judgment | nearest owner README or AGENTS | quest, rank, reward, or campaign |
| durable obligation | quest reading | `mechanics/questbook/` and `quests/` | quest ownership or closure |
| long-horizon composition | campaign or party reading | `aoa-playbooks` | choreography truth |
| role or actor posture | class, origin, or party role reading | `aoa-agents` | role canon |
| executable workflow | ability reading | `aoa-skills` | skill object truth |
| reusable practice | feat reading | `aoa-techniques` | technique canon |
| advancement or unlock | rank, mastery, reputation, or unlock question | `aoa-agents`, `aoa-evals`, `aoa-stats` | proof verdict or universal score |
| proof or claim validation | trial, gate, or evidence reading | `aoa-evals` | proof authority from RPG |
| memory or consequence | chronicle or scar reading | `aoa-memo` | memory object ownership |
| runtime or frontend projection | resource, loadout, state hint, or display reading | `abyss-stack` | runtime ledger or UI authority |
| public display | themed label with canonical key visible | `mechanics/rpg/parts/vocabulary-overlay/` | presentation replacing keys |
| unclear owner | no RPG expansion yet | `docs/FEDERATION_RULES.md` and `docs/REPO_ROLES.md` | hidden transfer of ownership |

## Application Sequence

1. Name the source object and its owner before naming the RPG reflection.
2. Ask whether the RPG term improves routing, judgment, memory, proof, or consequence.
3. Choose the active part in `PARTS.md` that owns the reflection.
4. Keep the RPG reading visibly derived from source refs, proof refs, owner routes, or runtime contracts.
5. If owner-local work is needed, create or update an owner request instead of claiming acceptance.
6. Update `ROADMAP.md` only when the future route changes, and `LANDING_LOG.md` only when the landing is checked.

## Stop-lines

- Do not turn every task into a quest.
- Do not turn every label into a stat.
- Do not create a universal power score.
- Do not treat RPG labels as source truth.
- Do not hide owner uncertainty behind game language.
- Do not route runtime state, proof verdicts, role canon, skill canon, quest closure, or memory ownership through RPG center docs.

## Post-change Route Review

After changing RPG language, confirm that a future agent can still answer:

- What is the source object?
- Who owns the source truth?
- Which RPG part owns the reflection?
- Which owner route handles proof, runtime, memory, quest, role, skill, or campaign work?
- Did the change add useful consequence, or only decorative vocabulary?

## Next Route

For quest-shaped obligations, go to Questbook first, then use
`mechanics/rpg/parts/quest-campaign/PLAYABLE_OBLIGATION.md` only when a derived
reading improves action.
For role, skill, technique, playbook, proof, memory, stats, or runtime truth, route to the stronger owner.
For pure language-shape decisions, return to `DIRECTION.md`, `PARTS.md`, and the relevant active part.
