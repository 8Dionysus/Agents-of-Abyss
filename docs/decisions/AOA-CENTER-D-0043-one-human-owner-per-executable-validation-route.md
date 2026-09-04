# One Human Owner Per Executable Validation Route

- Decision ID: AOA-CENTER-D-0043

## Status

Accepted.

## Index Metadata

- Original date: 2026-09-04
- Surface classes: agent guidance, validation guard, procedure route, decision record
- Center facets: agent guidance, federation contour
- Mechanic parents: cross-mechanic
- Guard families: AGENTS/mesh, docs hygiene, validation ownership, generated freshness
- Posture: accepted portable route law; sibling adoption and exceptions remain owner-local

## Context

`AOA-CENTER-D-0042` separates inherited agent routes, human README surfaces,
owner procedure, and generated views. During the federation-wide migration of
executable blocks out of `AGENTS.md`, many commands reached `VALIDATION.md`, but
some were copied into both a parent validation map and a local validation file.
The prompt became lighter while command ownership became less clear.

A working-tree census found exact executable duplication in several owner
repositories, including large concentrations in `aoa-sdk`, `aoa-evals`,
`abyss-stack`, and `aoa-stats`. Some parent files had become concatenated
catalogs of child commands. That creates two editable human sources for one
invocation and makes later fixes likely to update only one copy. It also hides
whether a broad gate owns orchestration or merely repeats its leaves.

Exact textual duplication is not the whole semantic problem, but it is a
deterministic lower bound. Future agents need to know why moving commands out
of inherited context is incomplete until their procedure ownership is singular
and the surviving route remains discoverable.

## Options considered

1. Permit copied commands in every local `VALIDATION.md` so each directory is
   fully self-contained.
2. Keep all commands only in each repository root `VALIDATION.md` and remove
   local validation routes.
3. Give each exact executable invocation one human-authored procedure owner
   per repository; make other validation surfaces route to that owner, manifest
   key, runner, or named lane without copying the invocation.
4. Centralize every repository's commands in one federation-wide manifest.

## Decision

Choose option 3.

Within one repository, an exact executable validation invocation has one
human-authored procedure owner. That owner may be a `VALIDATION.md`, a validated
command manifest and runner, or another explicitly named owner procedure.
Sibling `VALIDATION.md` files retain local discoverability but refer to the
owner by repository-relative link, heading, lane, or manifest key instead of
copying the command.

A broad validation or release surface owns its orchestration contract. It may
invoke a named composite runner or validated lane, but it must not reproduce
leaf command text already owned by a child route. Conversely, a child route
must not copy a root command merely to appear self-contained. When a reusable
machine sequence already exists in a canonical manifest or script, the human
validation surface explains selection and invokes that authority rather than
becoming a second command catalog.

The uniqueness boundary is repository-local. Identical commands in different
owner repositories do not share authority merely because their argv matches.
Commands in README usage examples are not automatically violations, but an
identical block presented as required validation must be routed to the owner
procedure. Executable procedure remains outside inherited `AGENTS.md`.

Validators should reject unexplained exact duplicates across active authored
validation surfaces. A real need for repeated presentation requires an
owner-local, reviewable exception that names the distinct audience or execution
contract; convenience is not sufficient. Exact-command checks remain a lower
bound: owner review must also catch semantically duplicated wrappers or command
variants that text normalization cannot prove equivalent.

Fence labelling does not change procedure ownership. An executable-looking
invocation in a `text`, unlabelled, console, or shell fence remains part of the
validation corpus; a presentation-only language tag cannot be used to evade
the uniqueness check.

Command migration must preserve the set of unique executable procedures.
Deletion of a duplicate is safe only after the surviving owner, incoming
routes, relevant manifest or runner, and focused verification are accounted
for. A green command proves only its declared check, not CI, release readiness,
runtime state, proof strength, or owner acceptance.

## Rationale

Option 1 preserves local convenience at the cost of silent drift and makes file
count look like ownership. Option 2 removes local discoverability and turns the
root into another monolith. Option 4 crosses repository authority and makes one
integration surface responsible for sibling procedure truth.

Option 3 keeps on-demand navigation close to the affected path while making the
editable executable source unambiguous. It also lets repositories with mature
validated manifests retain them, lets smaller repositories use a direct local
`VALIDATION.md`, and gives the federation audit one conservative signal without
granting it sibling write authority.

## Consequences

- Local validation files may be short routing documents rather than command
  copies.
- Root validation maps remain useful as navigation and orchestration surfaces,
  not recursive command archives.
- Exact duplicate count becomes a guarded review signal; zero exact duplicates
  does not replace semantic review.
- README verification duplication must be classified separately from genuine
  public usage examples.
- Each sibling repository owns adoption, exceptions, command conservation,
  validators, and generated updates for its own procedure corpus.
- The cross-repository audit may measure and compare results, but cannot choose
  a sibling command owner.

## Source surfaces

- `DESIGN.AGENTS.md`
- `docs/guardrails/AGENTS_MESH_PROTOCOL.md`
- `docs/guardrails/README_AGENTS_CORPUS_PROTOCOL.md`
- `mechanics/validation-routes.json`
- `scripts/agents_mesh/`
- `scripts/mechanics_topology/`
- `8Dionysus:scripts/readme_agents_corpus.py`

## Follow-up route

Apply the invariant owner by owner. Preserve unique-command conservation,
replace duplicate leaf text with exact owner routes, add focused regression
guards where each repository has an active agent/validation validator, and
rebuild only declared generated consumers. The federation merge barrier stays
closed until the final corpus census accounts for every duplicate, exception,
route, and owner-local check.
