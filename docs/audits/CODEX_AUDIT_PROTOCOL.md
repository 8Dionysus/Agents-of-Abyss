# Codex Audit Protocol

This document defines the default audit posture for the AoA ecosystem.

Use it when:

- auditing a repository without making changes,
- preparing a narrow fix after an audit,
- reviewing a pull request with Codex,
- deciding whether work belongs in the current repository at all.

Read this file together with:

- `AGENTS.md`
- `ECOSYSTEM_AUDIT_INDEX.md`
- the target repository's own source-of-truth docs
- any repo-local `AUDIT.md` if one exists

## Core stance

- Prefer **report-first** over immediate code edits.
- Prefer **one repository at a time** over cross-repo cleanup.
- Prefer **the smallest reviewable change** over broad refactors.
- Prefer **explicit uncertainty** over confident drift.
- Prefer **routing** over rewriting a neighboring repository's meaning.

## Audit sequence

### 1. Establish the active instruction chain

Before doing anything else:

- identify the nearest active `AGENTS.md` chain,
- note any nested `AGENTS.md` files that apply,
- list repo-local audit docs that must also be read,
- name the current repository role in one sentence.

### 2. Re-state ownership

Before proposing a change, answer:

- what this repository owns,
- what it explicitly does not own,
- which neighboring repositories might look relevant but are not the owner.

If ownership is ambiguous, stop broad implementation and turn the ambiguity into the first audit finding.

### 3. Build a source-of-truth set

List the exact files that are authoritative for this task.
Separate:

- entrypoint docs,
- architectural or doctrine docs,
- generated or derived surfaces,
- validation or workflow surfaces.

Never let a generated summary outrank its source.

### 4. Declare the risk class

Name one or more of:

- constitutional
- runtime
- workflow
- meaning
- proof

Then say what the most likely failure mode is in this repository.

### 5. Audit before patching

The first pass should produce an audit memo, not a diff.

The memo should include:

- active instructions,
- source-of-truth docs,
- ownership boundaries,
- mandatory verification,
- likely drift or risk points,
- smallest reviewable next change.

### 6. Patch narrowly only after the audit is grounded

If a change is still needed:

- touch only the owning repository,
- keep the diff narrow,
- preserve current terminology unless semantic change is intentional,
- update validation and docs when contract meaning changes,
- report any residual risk honestly.

## Required output contract

Every Codex audit or fix in AoA should end in this shape:

### PLAN

- state the task in executable form
- list the files likely to change
- state the main boundary or safety risk

### DIFF

- list exactly what changed
- call out semantic change versus metadata/docs-only change

### VERIFY

- list the commands or checks actually run
- say explicitly what was **not** run
- never imply validation that did not happen

### REPORT

- summarize the result in plain language
- state whether the work changed meaning, only routing, or only metadata
- name any neighboring repository follow-up needed

### RESIDUAL RISK

- note remaining ambiguity, unverified surfaces, or follow-up work

## GitHub review severity map for AoA

Codex GitHub review flags only P0 and P1 issues by default.
Use the following interpretation across AoA unless a repo-local `AGENTS.md` narrows it further.

### P0

Reserve for issues that would create immediate severe harm, for example:

- committed secrets or secret-bearing runtime output
- a change that turns safe/default-local behavior into externally exposed behavior
- a default path that can trigger destructive or real-world actions without the intended safeguard

### P1

Use for high-value issues that would materially break trust, boundaries, or operating safety, for example:

- source-of-truth drift
- wrong-owner routing
- silent semantic changes hidden as docs-only or metadata-only
- generated surfaces drifting from their sources
- verification claims that were not actually checked
- bounded claims that overstate what evidence supports
- center claims that absorb owner-local implementation, proof, runtime,
  memory, or ToS meaning
- bootstrap, runtime, or dry-run posture weakened without explicit callout

Do not spend review budget on low-value nits unless the task explicitly requests them.

## Default prompts

### Read-only audit

```text
Goal: Audit this repository without changing files.

Context:
This repository is part of the AoA ecosystem.
Identify the active instruction chain, the exact source-of-truth docs for this task, the ownership boundaries, the mandatory verification, and the smallest reviewable next change.

Constraints:
Read-only.
No speculative claims.
Quote exact evidence when possible.
List what you could not verify.
Do not propose broad refactors before identifying the smallest reviewable change.

Done when:
Return PLAN, REPORT, and RESIDUAL RISK with:
1) active instructions,
2) source-of-truth docs,
3) mandatory verification,
4) drift risks,
5) smallest next change.
```

### Narrow fix after audit

```text
Goal: Make the smallest reviewable change for item X.

Context:
Follow the nearest AGENTS.md chain, repo-local AUDIT.md if present, and owning source-of-truth docs.

Constraints:
One issue only.
One repository only.
Run mandatory verification.
Do not widen permissions, dependencies, services, ports, or semantic scope unless explicitly required.
Do not claim checks you did not run.

Done when:
Return PLAN, DIFF, VERIFY, REPORT, and RESIDUAL RISK.
```

## Special rule for the center repository

When working in `Agents-of-Abyss`:

- fix ecosystem clarity, not layer-owned meaning,
- prefer links and routing over copied detail,
- update center docs coherently or not at all,
- treat contradictions among `README.md`, `CHARTER.md`, `ECOSYSTEM_MAP.md`, `docs/LAYERS.md`, `docs/FEDERATION_RULES.md`, `ROADMAP.md`, and `generated/ecosystem_registry.min.json` as first-class findings.

## Special rule for runtime repositories

When working in `ATM10-Agent` or `abyss-stack`:

- separate harmless documentation drift from changes that alter execution posture,
- treat dry-run, localhost-first, public-safe examples, secrets hygiene, and bootstrap contracts as review-critical,
- prefer read-only audit mode first, then a narrow patch.
