# Witness and Compost

This document records the current fourth-wave doctrine for AoA after the trunk-first, method-centered, and counterpart-bridge waves.

It does not open runtime instrumentation yet.
It names the public contracts that let AoA leave a reviewable witness and let ToS compost that witness into layered knowledge without collapsing memory, proof, and runtime into one object.

## Core law

The current fourth-wave witness and compost pilot is:

1. **AoA leaves a reviewable witness**
2. **ToS composts that witness into layered knowledge**
3. **memory and proof stay explicit**
4. **runtime implementation remains later and belongs in `abyss-stack`**

## Ownership chain

The ownership boundary for this pilot is explicit:

- `aoa-playbooks` owns the scenario route
- `aoa-memo` owns witness-facing memory contracts
- `aoa-evals` owns proof of trace integrity and compost provenance
- `Tree-of-Sophia` owns compost-cycle doctrine and canon-facing digestion
- `abyss-stack` is deferred for later runtime instrumentation

## Pilot posture

This wave is intentionally contract-first.

It should produce:

- a readable witness contract
- a readable compost-cycle doctrine
- one real playbook-owned route from witness artifact to note or principle candidate
- bounded proof surfaces for trace integrity and provenance preservation

It should not produce:

- a full runtime trace platform
- hidden logging doctrine in the infrastructure layer
- a new memory-object family that replaces the current memo taxonomy
- a KAG-first bridge that outruns authored source surfaces

## Practical rule

If a witness/compost surface cannot answer these questions clearly, it is not ready:

- what artifact counts as the witness?
- what memory writeback survives the route?
- what proof surface checks the witness or compost result?
- what ToS layer receives the composted output?
- what runtime work is still explicitly deferred?

The point of this wave is to make the pair public and reviewable before any deeper execution machinery is claimed.
