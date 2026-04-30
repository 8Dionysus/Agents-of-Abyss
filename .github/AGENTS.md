# AGENTS.md

## Applies to

This card applies to `.github/` and all descendants unless a nearer `AGENTS.md` narrows the path.

## Role

`.github/` holds GitHub-native automation, issue/PR templates, workflow files, and repository platform configuration.

## Read before editing

Read root `AGENTS.md`, `CONTRIBUTING.md`, and any workflow-local comments before changing automation.

Use the nearest README for local file purpose. Use source docs, schemas, generated builders, validators, and owner repos as stronger authority when they apply.

## Boundaries

- Do not encode doctrine in workflows that is absent from source docs.
- Do not make CI green by weakening the guardrail being checked.
- Do not add mutation or release behavior without an explicit human-visible path.

## Platform sync

Keep `.github/CODEOWNERS`, `.github/PULL_REQUEST_TEMPLATE.md`, and workflow
expectations aligned with current root districts and guardrail paths. When a
durable root lane is added or removed, update CODEOWNERS and the PR template in
the same review when they are affected.

The branch, PR, CI, and merge route is owned by the root `AGENTS.md` GitHub
landing workflow. This district keeps the GitHub-native files aligned with that
route.

## Validation

Run the narrowest relevant checks first. Usual checks for this district:

```bash
python scripts/validate_agents_mesh.py
python -m pytest -q
```

If a listed validator is not present in the checkout yet, report that explicitly and run the closest available guardrail.

## Closeout

Report changed files, source surfaces consulted, generated files rebuilt or not rebuilt, checks run, checks skipped, and any owner boundary that may need follow-up.
