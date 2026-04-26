# agon Quest Lane

Agon obligations and owner follow-through.

## Lane route

Use this lane for Agon quest families whose source ID and owner route already
belong to the Agon mechanic. The large triaged pool is a receipt-backed frontier,
not a priority queue.

Current source split:

- `done`: center-owned Agon contour quests whose active part artifacts,
  generated capsules, or stop-line surfaces are already landed in
  `mechanics/agon/`.
- `ready`: owner-followthrough quests where the next action is receipt review,
  owner-acceptance confirmation, or owner-request update.
- `triaged`: only for newly captured Agon quest pressure whose owner route is
  known but whose next action is not yet clear.

## Promotion rule

Promote an Agon quest only during an Agon mechanic pass or when an owner-request
route makes the next action clear. If the work belongs to a stronger sibling
owner, keep the quest as a handoff until that owner accepts it.

Move center-landed contour quests to `done` only when the active Agon part,
generated capsule, validator, or landing ledger proves the surface. Move
owner-followthrough quests to `ready` when sibling or center request surfaces
exist and the remaining work is receipt review rather than doctrine invention.

## Stop-lines

- Do not use Agon quests to rewrite trial, proof, memory, KAG, routing, or role
  truth owned elsewhere.
- Do not promote a wave-era receipt only because it is old.
- Do not collapse Agon quest follow-through into root roadmap history.

Quest source files in this lane use lifecycle subdirectories only when items exist. The lifecycle states are `captured`, `triaged`, `ready`, `active`, `blocked`, `reanchor`, `done`, and `dropped`.

Do not create top-level `AOA-Q-*` aliases in this lane. Keep each quest under `<lane>/<state>/AOA-Q-*` and keep root `QUESTBOOK.md` as the public index, not a second roadmap.
