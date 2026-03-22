# AoA Glossary

## Technique

A minimal reproducible unit of engineering practice.
A technique describes a reusable pattern with explicit boundaries, contracts, risks, and validation.

## Skill

A bounded agent-facing workflow that composes one or more techniques into an operational execution surface.

## Method / Playbook

A recurring scenario-level route that composes techniques, skills, decision points, handoffs, fallback posture, and expected evidence.
Scenario-level method belongs to `aoa-playbooks`, not to `aoa-techniques` or `aoa-skills`.

## Eval

A bounded proof surface that checks a specific claim about behavior, quality, safety, regression, comparison, or growth.

## Routing

A lightweight navigation and dispatch layer that helps humans and models choose the right surface next.
Routing does not own the primary meaning of techniques, skills, evals, or memory objects.

## Memory

The memory and recall layer.
It should own memory objects, provenance-oriented recall, temporal relevance, and retrieval surfaces rather than practice or proof truth.

## Role

A bounded operational identity that states who acts, what posture it carries, and where it should hand off.
Roles are owned by `aoa-agents`.

## Agent

A role-bearing actor in the AoA ecosystem.
An agent should have explicit boundaries, responsibilities, preferred skills, handoff posture, memory posture, and expected evaluation surfaces.
If a self-agent can change important system surfaces, it should be governed through explicit checkpoints rather than autonomy folklore.

## Source of truth

The canonical home of meaning for a given object class.
Example: technique meaning belongs to `aoa-techniques`, not to `aoa-routing`.

## Capsule

A compact agent-friendly summary surface derived from a larger canonical bundle.
A capsule should accelerate routing and decision-making without replacing the full source bundle.

## Bounded claim

A claim that states what is supported, under what conditions, and with what limits.
AoA prefers bounded claims over vague global assertions.

## Provenance

A readable account of where an object, memory, or claim came from and how it was shaped.

## Donor refinery

A source-first AoA intake rule for external donors:
`donor -> repeated pattern -> sanitized technique or skill -> playbook -> eval`.

The refinery exists to extract reusable form without importing foreign doctrine wholesale.

## Shared maturity ladder

The ecosystem-level ladder used when AoA makes cross-repo maturity claims:
`seed -> proven -> promoted -> canonical -> deprecated`.

Individual repositories may keep narrower local ladders, but ecosystem claims should map back to this shared ladder explicitly.

## Federation

The AoA ecosystem understood as a set of distinct but coordinated repositories, each with explicit ownership boundaries.
