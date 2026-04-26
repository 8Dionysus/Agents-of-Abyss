# center Quest Lane

Center federation obligations and cross-mechanic quest routing.

## Lane route

Use this lane for obligations that change AoA center posture, cross more than
one mechanic, or must stay visible from the root `QUESTBOOK.md`.

Legacy center RPG quest IDs remain here until a deliberate reanchor creates a
new RPG-lane source object. Do not silently move `AOA-Q-0004` through
`AOA-Q-0008` only because their topic is RPG-shaped.

Use `sidequest` relations when a center quest needs to point at mechanic-shaped
routes without transferring ownership or lifecycle placement.

## Promotion rule

Promote a center quest only when its anchor can be read without raw session
history and the next center action is clear. Closing a center quest requires
public evidence that the named seam, doctrine, or owner route landed.

## Stop-lines

- Do not turn center quests into a catch-all backlog.
- Do not use center placement for repo-local work.
- Do not treat `sidequest` as dependency, owner acceptance, or closure proof.
- Do not let a generated Questbook view become quest authority.

Quest source files in this lane use lifecycle subdirectories only when items exist. The lifecycle states are `captured`, `triaged`, `ready`, `active`, `blocked`, `reanchor`, `done`, and `dropped`.

Do not create top-level `AOA-Q-*` aliases in this lane. Keep each quest under `<lane>/<state>/AOA-Q-*` and keep root `QUESTBOOK.md` as the public index, not a second roadmap.
