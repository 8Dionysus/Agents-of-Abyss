# AoA Agent Surface Design

## Role

`DESIGN.AGENTS.md` describes the desired form of agent-facing guidance within
Agents of Abyss. Adjacent agentic projects may adopt its portable shape when it
fits their own owner truth.

It is not an `AGENTS.md` card, prompt library, policy bundle, charter, roadmap,
schema, validator, or generated index.

It answers one question:

What shape should agent-facing surfaces take so agents can act locally without
losing owner truth, evidence, reviewability, or return routes?

## Design Thesis

An agentic project should not give agents one giant instruction wall.

It should give them a navigable mesh:

- a root card that names identity, owner boundaries, and route choice;
- local cards that narrow the lane for districts, packages, parts, and high-risk
  surfaces;
- source surfaces that keep meaning stronger than summaries;
- validation surfaces that turn claims into checkable work;
- closeout contracts that let the next agent resume without archaeology.

Agent guidance is not authority by volume. It is authority by placement,
proximity, ownership, validation, and explicit return.

The root names the road system.
The nearest card narrows the lane.
The owner surface keeps truth.
The validator tests the claim.
The closeout returns the work to memory.

Human documentation is a neighboring layer, not inherited agent law.
README surfaces may explain purpose, use, navigation, provenance, and public
posture on demand. An agent card points to one only when that human surface is
material to the work.

## Design as Appearance

Agent guidance should appear as a readable road network, not a buried control
panel.

A healthy agent-facing layer has:

- a clear root `AGENTS.md`;
- local `AGENTS.md` cards in durable districts;
- a consistent card shape;
- visible owner boundaries;
- named validation routes;
- negative boundaries that say what must not be claimed;
- closeout expectations for changed surfaces, skipped checks, remaining risk,
  and next owner route;
- generated companions that summarize the mesh without becoming the mesh.

The layer should be friendly to low-context agents. A newcomer should be able to
ask: where am I, what owns this, what must I read, what must I not claim, how do
I verify, and how do I return?

Ritual, mythic, civic, or game language is allowed when it makes motion more
memorable and bounded. It fails when it hides responsibility, source truth,
validation, or human review.

## Design as Anatomy

The agent-facing layer is composed of several different organs.

### Root card

The root `AGENTS.md` owns repository identity, global route modes, owner
boundaries, cross-repository routing, broad validation posture, and closeout
expectations.

It should not contain every local rule. A swollen root card is a map that ate
the city.

### District cards

Top-level and thematic district cards own local risks, local source surfaces,
local validation, and local closeout requirements.

They narrow the root card. They do not overturn it.

### Package cards

Package cards describe the operating lane for a mechanic, module, subsystem, or
similar owned body of work.

A package card should name its source surfaces, post-change route review, local
validators, owner requests, generated mirrors, and stop-lines.

### Deep cards

Deep cards protect high-friction or high-risk surfaces: decisions, guardrails,
parts, legacy archives, manifests, generated read models, release claims, or
other surfaces where a wrong move can silently change meaning.

A deep card exists because proximity matters. The safest instruction is often
nearest to the file that can be harmed.

### Source surfaces

Source docs, schemas, builders, validators, tests, registries, owner repos, and
human-authored maps own meaning.

`AGENTS.md` cards route agents to source truth. They do not become source truth
by repetition.

### Human and public surfaces

README files introduce, explain, and connect a surface for humans and public
callers. They may be valuable without being mandatory agent context. A README
does not become an owner contract merely because it is conventional, and an
AGENTS card does not need to repeat it merely because both files share a
directory.

Keep a README when it carries a real public entrypoint, usage path, package map,
example route, provenance bridge, or compatibility function. Merge, move,
generate, or remove it only through the evidence law in
`docs/guardrails/README_AGENTS_CORPUS_PROTOCOL.md`.

### Validation surfaces

Validators, tests, builders, and freshness checks make agency inspectable.

A card that asks an agent to change something should also say how that change is
checked, or where to find the check.

### Generated companions

Generated indexes and compact capsules may help low-context agents navigate the
mesh.

They are mirrors and companions. They must point back to source surfaces, remain
reproducible, and avoid authoring new meaning.

## Design as Operation

A safe agent move follows a route before it touches content.

1. Receive the applicable root card.
2. Read the nearest local card for every touched path.
3. Follow only the task-relevant owner source routes named by those cards.
4. Make the smallest change that preserves the owner boundary.
5. Run the narrowest relevant validation first.
6. Run broader gates when the change is release-facing, route-facing, generated,
   structural, or cross-owner.
7. Close out with changed surfaces, checks run, checks skipped, remaining risk,
   and next owner route.

Agency becomes stronger when it can stop, explain itself, and hand off cleanly.

## Design as Authority

Agent guidance has limited authority.

It may:

- route work;
- name local risks;
- name owner surfaces;
- require task-relevant owner routes;
- require validation;
- set closeout shape;
- prevent common unsafe claims.

It must not:

- override source-owned truth;
- claim hidden autonomy;
- claim live runtime state unless the runtime owner proves it;
- claim memory sovereignty;
- claim proof sovereignty;
- claim owner-local acceptance without owner-local receipt;
- turn generated surfaces into authority;
- convert mythic language into permission;
- bury semantic changes under "docs-only" wording.

The agent layer is a road law. It is not the king, the archive, the oracle, or
the runtime body.

## Canonical Card Shape

Every durable `AGENTS.md` card under Agents of Abyss, or in a project that
explicitly adopts this design, should begin from this shape:

```markdown
# AGENTS.md

## Applies to

## Role

## Read before editing

## Boundaries

## Validation

## Closeout
```

This shape is intentionally plain.

`Applies to` tells the agent where the card rules.
`Role` tells the agent what this lane is for.
`Read before editing` selects the minimum owner surfaces that can change the
interpretation of work in this lane. It is not permission to require the
nearest README or repeat a generic repository reading list.
`Boundaries` prevents authority drift.
`Validation` turns action into checkable work.
`Closeout` preserves handoff memory.

Optional sections may be added when the lane needs them: `Purpose`, `Owner
lane`, `Route modes`, `Source Surfaces`, `Post-change route review`, `Editing
posture`, `Part evolution`, `Decision review`, `Routed child validation`,
or local equivalents.

Optional sections should sharpen the route. They should not decorate it into
fog.

## Design Principles

### 1. Locality before abstraction

The nearest relevant card should carry the local rule. Root guidance should stay
wide enough to route and narrow enough to remain readable.

### 2. Routes before commands

A good card does not merely say "do X". It says which surface owns the claim,
which route to follow, which check to run, and where to hand off.

### 3. Source before instruction

Instructions are guidance. Source surfaces own meaning. When an instruction and
a source surface conflict, the agent should stop, report the conflict, and route
to the owner rather than inventing reconciliation.

### 4. Negative boundaries are design

A clear "do not" is not pessimism. It is a guardrail against silent authority
transfer.

### 5. Validation is the handshake with reality

Every substantial card should name the smallest useful validation path. Broad
gates are valuable, but local checks keep work from becoming theatrical.

### 6. Closeout is memory

A closeout is not ceremony. It is the next agent's doorway: what changed, what
was checked, what was skipped, what remains risky, and where work resumes.

### 7. Generated companions are companions

Machine-readable summaries are useful when they compress and route. They become
dangerous when they start to author meaning or hide their source.

### 8. Proximity narrows, it does not usurp

Nested cards narrow the lane for their scope. They do not steal root identity,
sibling authority, owner-local truth, or source meaning.

### 9. Portability comes from repeated shape

A portable agent layer is not copied text. It is copied discipline: same card
shape, same owner logic, same validation posture, same closeout memory, adapted
to local truth.

### 10. Agency must remain returnable

An agent may act, propose, validate, route, summarize, and hand off. Durable
action should always preserve review, rollback, evidence, and a way back to the
owner surface.

### 11. Inherited context is a budgeted route surface

Every descendant receives the applicable AGENTS chain, so repeated command
catalogs and source prose become a recurring context cost. Keep owner
boundaries, stop-lines, task-relevant source routes, and the smallest executable entrypoint
in the card. Put large child-specific command matrices in a validated owner
manifest and retrieve only the exact route needed for the touched surface.

Shorter is not automatically better. The budget protects locality and signal;
it must not erase a contract that has no stronger source elsewhere.

## Good Agent Design Feels Like

A low-context agent can find the nearest rule.
A maintainer can find the owner.
A claim can find its source.
A generated summary can find its builder.
A risky change can find its validator.
A future agent can find the closeout.
A human can see what authority the agent used.
A repository can grow without turning its root into a labyrinth cupboard.

## Bad Agent Design Smells Like

- one enormous root `AGENTS.md` that tries to control every district;
- local cards that duplicate root doctrine instead of naming local risk;
- instructions that cite no owner surface;
- validation commands copied everywhere and allowed to drift;
- the nearest README required by convention rather than task relevance;
- human overview moved into inherited cards to lower the README count;
- inherited card chains that silently exceed their declared context budget;
- generated indexes treated as source authority;
- autonomous language without stop-lines;
- mythic language replacing evidence;
- hidden memory, runtime, proof, or owner acceptance claims;
- closeouts that say only "done";
- new durable directories without a local card or explicit exemption;
- semantic changes disguised as formatting, metadata, or docs-only cleanup.

## Relationship to Other Surfaces

`README.md` introduces the project.
`CHARTER.md` authorizes the center.
`DESIGN.md` names the system form.
`AGENTS.md` routes agent work in the repository.
Nested `AGENTS.md` cards narrow local work.
`docs/guardrails/AGENTS_MESH_PROTOCOL.md` defines the current mesh contract.
`docs/guardrails/README_AGENTS_CORPUS_PROTOCOL.md` defines the boundary between
inherited agent routes and on-demand human README surfaces.
`config/agents_mesh.json` registers required cards.
`generated/agents_mesh.min.json` mirrors mesh coverage for machines.

`DESIGN.AGENTS.md` holds the design form of the agent-facing layer.

It tells humans and agents what kind of agent guidance they are preserving when
they add, move, split, validate, generate, or port `AGENTS.md` surfaces.

## Portability to Other Agentic Projects

A project may adopt this design without adopting AoA's whole doctrine.

The portable minimum is:

- one root `AGENTS.md`;
- local cards for durable editable districts;
- the canonical six-section card shape;
- explicit owner surfaces;
- explicit negative boundaries;
- validation named close to the work;
- closeout that records changed surfaces, checks, skipped checks, risk, and next
  route;
- generated mesh summaries only when they remain source-linked and reproducible.

Port the shape, then let local truth speak in its own tongue.

## Use by Agents

Agents should consult this file when a change alters:

- the shape of any `AGENTS.md` card;
- the root-to-local precedence model;
- route modes or owner-source selection;
- validation authority;
- generated agent-mesh companions;
- closeout requirements;
- local card placement;
- cross-repository owner routing;
- the portability of agent guidance to another project.

This file does not override local owner truth. It tells agents what kind of
agent-facing form they are preserving.

## Landing Rule

When this design changes, review whether the following surfaces also need to
move:

- root `AGENTS.md`;
- affected nested `AGENTS.md` cards;
- `docs/guardrails/AGENTS_MESH_PROTOCOL.md`;
- `docs/guardrails/README_AGENTS_CORPUS_PROTOCOL.md`;
- `config/agents_mesh.json`;
- generated agent-mesh companions;
- validators for card shape, mesh coverage, generated freshness, and release
  checks;
- `README.md`, `docs/ROOT_SURFACE_LAW.md`, and a decision record when the root
  or route-law meaning changes.

Only update a surface when its meaning actually moved. The design is a compass,
not a broom.
