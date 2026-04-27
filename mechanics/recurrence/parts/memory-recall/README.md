# Memory Recall

Memory Recall keeps anchors, checkpoints, recall contracts, state capsules, and
provenance explicit without turning memory into route authority.

## Use When

- A return needs bounded relaunch support.
- Checkpoint continuity needs recall, state capsule, decision, episode,
  audit-event, anchor, or provenance-thread support.
- A continuity route needs writeback without a new memory family.

## Do Not Use When

- Memo is asked to decide return legitimacy, dispatch, role rights, or retry budgets.
- The route wants a new return-only memory taxonomy.
- Raw runtime scratchpad is being promoted into canon.

## Route Check

Ask whether memo is preserving an anchor or trace, not deciding the route. If
memo would become policy, router, proof, or runtime body, stop and reroute.

## Active Outputs

- memo support request
- recall route
- state capsule route
- provenance thread route
- checkpoint-to-memory writeback route

## Next Route

Route memory objects and writeback meaning to `aoa-memo`, proof to `aoa-evals`,
navigation to `aoa-routing`, runtime export to `abyss-stack`, and actor posture
to `aoa-agents`.
