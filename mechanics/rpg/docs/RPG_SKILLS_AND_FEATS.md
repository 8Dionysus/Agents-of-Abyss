# RPG Skills And Feats

## Purpose

This note defines the second adjunct RPG reflection contour for AoA.

It extends the first-wave progression and campaign spine into the execution and reusable-practice layers without mutating the underlying source-owned meanings of skills, techniques, proofs, playbooks, routing, or runtime.

## Core rule

Skills and techniques gain an RPG reading as derived reader surfaces, not as a hidden replacement ontology.

It may:
- map bounded skill bundles into active ability cards
- map reusable techniques into feat / perk cards
- connect first-wave progression axes to ability and feat unlock posture
- make long-horizon mastery easier to read without changing source ownership

It must not:
- replace `SKILL.md` as the owner of skill meaning
- replace `TECHNIQUE.md` as the owner of technique meaning
- turn pack profiles into runtime inventory
- turn playbooks into a combo engine by accident
- invent runtime state inside repos that do not own runtime

## Reflection map

- skill bundle -> active ability
- invocation mode -> activation posture
- pack profile -> loadout hint
- technique dependency -> feat adjacency
- reusable technique -> feat / perk candidate
- canonical readiness and evidence -> feat eligibility gate
- project overlay -> local adaptation hint
- local adapter seam -> portability / equip constraint

## Ability rules

Abilities belong in `aoa-skills` only as reflections of already-owned skill bundles.

Good second-wave ability posture:
- active, bounded, executable
- reviewable through existing skill, evaluation, and portable-layer surfaces
- unlock hints tied to first-wave progression axes
- pack-profile-aware rather than runtime-inventory-shaped
- overlay-aware without letting overlays redefine the core ability

## Feat rules

Feats belong in `aoa-techniques` only as reflections of already-owned technique canon.

Good second-wave feat posture:
- reusable and portable enough to survive beyond one local diff
- derived from technique canon, readiness, donor-refinery, or evidence surfaces
- mastery-shaped rather than score-shaped
- allowed to express transfer scope and caution posture
- never used to bypass canonical review or source-owned technique meaning

## Boundary rules

### Skills stay bounded

`aoa-skills` still owns bounded execution packages, portable export posture, pack profiles, overlays, and local adapter seams. It does not become the owner of scenario method.

### Techniques stay source-first

`aoa-techniques` still owns reusable practice canon, validation, adaptation notes, and promotion posture. It does not become a second skill catalog.

### Playbooks stay scenario-shaped

If later "build", "combo", or "rotation" language becomes necessary, it should live in `aoa-playbooks` only when it is truly scenario method rather than an ability reader surface.

### Runtime stays later

Durable equipped state, UI, services, or persistent progression remain runtime concerns for `abyss-stack`, not for this second wave.

## Exclusions

This wave excludes:
- ability cooldown or resource systems
- inventory or slot accounting
- live combo planners
- public profile mirrors
- routing expansion
- runtime persistence

## Final rule

The second honest RPG win in AoA is that skills feel like abilities and techniques feel like feats while every repo keeps owning the same meaning it already owned before.
