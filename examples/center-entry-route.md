# Center Entry Route Example

This worked example shows how a reader or agent can enter the AoA center, choose a route mode, and keep the next change inside the owning surface.

## Source Surfaces

- [Start Here Route Contract](../docs/START_HERE_ROUTE_CONTRACT.md)
- [center_entry_map.min.json](../generated/center_entry_map.min.json)
- [root AGENTS](../AGENTS.md)
- [Mechanics Atlas](../mechanics/README.md)
- [Repository Roles](../docs/REPO_ROLES.md)

## Demonstrates

A contributor arrives with this request:

> Add an example for how agents should decide whether a new process belongs in a mechanic package or a root technical district.

The request sounds like a root example, but it also mentions process mechanics. The first task is route choice.

## Route Walk

1. Start with the root route card in [AGENTS.md](../AGENTS.md).
2. Use [START_HERE_ROUTE_CONTRACT](../docs/START_HERE_ROUTE_CONTRACT.md) to choose the route mode.
3. Select `district-work` if the edit is already inside a technical district such as `examples/`.
4. Select `mechanic-change` if the example would teach behavior for Agon, Experience, Questbook, RPG, recurrence, release-support, audit, or another mechanic.
5. Select `ownership-routing` if the owning repository is unclear.
6. Read the selected human path and the local `AGENTS.md` before editing.
7. Keep the example linked to the source surface that owns the rule being demonstrated.

## Boundary

The root `examples/` district carries center-level worked examples. A mechanic-specific example moves to the owning mechanic package. A runtime or sibling-repository example moves to the owning repository.

This file illustrates route behavior. It does not replace the route contract, generated center map, validators, tests, or owner-local source docs.

## Checks

Use [examples/AGENTS.md#validation](AGENTS.md#validation) for the local validation route. When this example changes a route contract, also run the validators named by [START_HERE_ROUTE_CONTRACT](../docs/START_HERE_ROUTE_CONTRACT.md#validation).

## Closeout

A clean closeout for this lane names:

- changed example files
- source surfaces consulted
- whether generated route maps changed
- checks run and checks skipped
- the next owner route if the example revealed mechanic or sibling ownership
