# Examples District

This directory holds public-safe worked examples for the AoA center.

Root examples show how a reader or agent can apply center route contracts in a concrete situation.
They demonstrate route shape, posture, and usage while source docs, schemas, generated surfaces, validators, and owner repositories keep authority.

Mechanic-owned examples live under `mechanics/<slug>/.../examples/`. Root `examples/`
contains only root-owned examples.

## Placement

| Example kind | Home |
|---|---|
| Center route, root placement, owner-routing, or public-entry walkthrough | `examples/` |
| Mechanic behavior, mechanic schema instance, or part-local usage | `mechanics/<slug>/.../examples/` |
| Sibling repository implementation or runtime usage | owning sibling repository |
| Proof, regression, or acceptance fixture | `tests/`, `schemas/`, generated validators, or owner proof surface |

## Current Examples

| Example | Demonstrates | Source surfaces |
|---|---|---|
| [center-entry-route.md](center-entry-route.md) | entering the center, choosing a route mode, finding the owner surface, and closing with bounded verification | [Start Here Route Contract](../docs/START_HERE_ROUTE_CONTRACT.md), [center entry map](../generated/center_entry_map.min.json), [root AGENTS](../AGENTS.md) |

## Example Shape

Each root example names:

- the source surfaces it illustrates
- the route or placement decision it demonstrates
- the boundary that keeps the example illustrative
- the local checks or AGENTS validation path to use after related edits

## Before editing

1. Identify the source surface that the example illustrates.
2. Check whether the example belongs in a sibling repository instead.
3. If the example belongs to a center mechanic, edit the mechanic-owned source path.
4. Use [AGENTS.md#validation](AGENTS.md#validation) for local checks.
