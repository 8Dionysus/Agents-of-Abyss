# Agon Move Registry Model

## Source and generated surfaces

Wave III uses one source file and one generated capsule:

```text
config/agon_lawful_moves.seed.json
generated/agon_lawful_move_registry.min.json
```

The source file is the reviewable owner-authored list.

The generated file is the compact machine-facing registry.

Do not edit the generated file by hand.

## Individual move shape

Each move must include:

```text
move_id
name
move_class
intent
allowed_actor_forms
allowed_seats
preconditions
must_not
produces
center_owns
not_owned_here
future_owner_handoffs
live_protocol
runtime_effect
status
wave
```

A move is valid only when:

```text
live_protocol = false
runtime_effect = none
wave = III
status = seeded_pre_protocol
```

## Move id law

Move ids use:

```text
agon.move.<class>.<slug>
```

Examples:

```text
agon.move.trace.probe_trace
agon.move.closure.deny_closure
agon.move.revision.defer_with_cost
```

The `<class>` segment must match `move_class`.

## Generated registry

The generated registry records:

- source path;
- schema version;
- wave;
- global status;
- count by class;
- count by seat;
- count by actor form;
- the compact move list;
- explicit non-goals.

This registry is not a protocol runtime. It is a law-language surface.

## Required invariants

The builder and validator enforce:

- stable sorted move order;
- unique move ids;
- valid id/class agreement;
- valid actor forms;
- valid seats;
- all moves are pre-protocol;
- all moves deny runtime side effects;
- all moves carry owner handoff information;
- assistant-compatible moves do not grant contestant or judge authority.

## Future widening

A later wave may add:

- move envelopes;
- sealed commits;
- challenge packets;
- contradiction ledger law;
- terminal outcome law;
- verdict bridge;
- scar bridge;
- retention bridge.

That later widening must not be smuggled into this registry.

This registry names legal words, not live blows.
