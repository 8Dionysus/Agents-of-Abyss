# AGENTS.md

## Applies to

This card applies to `examples/` and all descendants unless a nearer `AGENTS.md` narrows the path.

## Role

`examples/` holds public-safe worked examples for the AoA center. Examples help readers apply route contracts, placement rules, and owner boundaries without becoming canonical source truth.

## Read before editing

Select only the source, contract, or owner route that can change the interpretation of the named task.
A nearby human README is on-demand: use it when its explanation, package map, provenance, compatibility, or usage contract is material to the task.
Exact executable checks belong to the applicable `VALIDATION.md`, validated manifest, runner, or stronger owner procedure surface.
## Boundaries

- Keep root examples centered on center routes, root placement, owner-routing, and public-entry posture.
- Keep mechanic behavior examples in the owning mechanic package.
- Keep sibling implementation examples in the owning sibling repository.
- Link every root example to the source surfaces that own the rule being demonstrated.
- Keep examples small, public-safe, and free of secrets, private paths, tokens, and live runtime assumptions.
- Treat examples as illustrative surfaces below docs, schemas, generated contracts, validators, tests, and owner repositories.
- Do not let examples override or silently replace the source surface they illustrate.

## Required Shape

Every root example Markdown file outside `README.md` and `AGENTS.md` must include:

- `## Source Surfaces`
- `## Demonstrates`
- `## Boundary`
- `## Checks`
- `## Closeout`

The local README must index every root example file.

## Validation

Run the narrowest relevant checks first. Usual checks for this district:

If a listed validator is not present in the checkout yet, report that explicitly and run the closest available guardrail.

## Closeout

Report changed files, source surfaces consulted, generated files rebuilt or not rebuilt, checks run, checks skipped, and any owner boundary that may need follow-up.
