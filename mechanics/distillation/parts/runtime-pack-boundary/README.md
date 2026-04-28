# Runtime Pack Boundary

Use this part to keep runtime distillation packs below memory, proof, and
runtime authority.

## Use When

- A runtime or agent layer emits a `distillation_pack`.
- The pack may produce claim, pattern, bridge, or memory candidates.

## Do Not Use When

- The task is runtime storage or execution plumbing; route to `abyss-stack`.
- The task is memory writeback; route to `aoa-memo`.

## Route Check

Treat runtime packs as candidate output only. Confirm the pack does not settle
truth, write memory canon, or prove the route.

## Active Outputs

- Runtime-pack boundary note.
- Candidate route.
- Memo/eval/runtime stop-line.

## Next Route

Route artifact contracts to `aoa-agents`, memory candidates to `aoa-memo`,
proof to `aoa-evals`, and storage or export behavior to `abyss-stack`.
