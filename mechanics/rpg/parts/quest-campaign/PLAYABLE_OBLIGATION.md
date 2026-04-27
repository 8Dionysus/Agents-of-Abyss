# Playable Obligation Reading

This surface defines how RPG may read a Questbook obligation without becoming
the quest source, lifecycle owner, or closure authority.

Questbook owns source quest object truth. RPG may add a derived reading only
when it makes the obligation easier to play, hand off, prove, remember, or
route.

## Reading Shape

| Field | Meaning | Owner route |
|---|---|---|
| `quest_ref` | source quest object or public Questbook entry | Questbook and `quests/` |
| `owner_route` | repository or mechanic that owns the next real move | source owner |
| `campaign_ref` | optional long-horizon composition route | `aoa-playbooks` |
| `party` | optional collaboration reading for one bounded run | `aoa-agents` and runtime owner |
| `stake` | what becomes better or worse if the quest moves | source owner plus proof route |
| `proof_route` | what evidence can move or close the obligation | `aoa-evals` or owner-local proof |
| `unlock_question` | whether completion should change rank, access, or capability | `aoa-agents`, `aoa-skills`, `aoa-techniques`, `aoa-evals` |
| `consequence_route` | what should be remembered after the move | `aoa-memo` |

The reading may be written in a handoff, review note, owner request, or active
mechanic document. It should not be added to every quest source by default.

## Use When

- a quest has enough ambiguity that campaign, party, stake, proof, or consequence language improves the next move
- a quest is readable as a side route, encounter, trial, unlock, or campaign step without changing ownership
- the next agent needs to know why the obligation matters, not only what file to edit

## Do Not Use When

- the quest only needs a lifecycle state move
- plain Questbook fields already answer the next action
- the reading would imply owner acceptance, proof completion, quest closure, runtime state, or reward authority
- the reading would be copied into many quest sources as repeated boilerplate

## Application Sequence

1. Read the source quest object and Questbook lane README first.
2. Confirm the owner route and lifecycle state without RPG language.
3. Add the RPG reading only if it improves the next move.
4. Keep `quest_ref` and `owner_route` visible.
5. Route proof, campaign, party, unlock, runtime, and memory claims to their owners.
6. Update the quest source only when the durable obligation changes, not when the reading is merely explanatory.

## Stop-lines

- RPG does not own quest lifecycle.
- RPG does not close quests.
- RPG does not prove completion.
- RPG does not turn sidequest relation into dependency or owner transfer.
- RPG does not create rewards, ranks, unlocks, or runtime state from center docs.

## Next Route

Use `mechanics/questbook/parts/model-spine/RPG_PLAYABLE_READING.md` for the Questbook-side reciprocal route.
Use `mechanics/rpg/USAGE.md` when deciding whether RPG language belongs at all.
