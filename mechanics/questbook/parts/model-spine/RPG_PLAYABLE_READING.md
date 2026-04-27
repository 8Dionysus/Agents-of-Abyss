# RPG Playable Reading Route

This surface defines the Questbook side of RPG playable obligation readings.

Questbook owns the source quest object, lifecycle state, lane placement,
public index posture, generated read models, and source contract. RPG may
derive a playable reading only after the quest source is already legible on
plain Questbook terms.

## Source First

Before using RPG language, a quest must still answer:

- what durable obligation survives the current diff
- which lane and lifecycle state own the route
- what the next action is
- what evidence can move or close it
- what must not be claimed from the quest alone

If those answers are unclear, fix the Questbook source route before adding RPG
language.

## RPG Reading Is Derived

An RPG reading may name campaign, party, stake, proof route, unlock question,
or consequence when that helps a future agent act. It must keep the source
quest ID and owner route visible.

Do not add RPG readings to every quest file as boilerplate. Use the reading in
handoffs, owner requests, reviews, or mechanic docs when it clarifies action.

## Stop-lines

- RPG language does not change lifecycle state.
- RPG language does not close, promote, or reanchor quests.
- RPG language does not prove owner acceptance.
- RPG language does not replace `source_contract`, lane README defaults, or generated Questbook read models.
- RPG language does not turn `sidequest` into dependency, owner transfer, or closure proof.

## Next Route

For the RPG-side reading shape, use
`mechanics/rpg/parts/quest-campaign/PLAYABLE_OBLIGATION.md`.
For whether RPG language belongs at all, use `mechanics/rpg/USAGE.md`.
