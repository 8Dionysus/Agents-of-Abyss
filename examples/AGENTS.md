# AGENTS.md

## Applies to

This card applies to `examples/` and all descendants unless a nearer `AGENTS.md` narrows the path.

## Role

`examples/` holds illustrative examples for humans and agents. Examples help readers understand patterns without becoming canonical source truth.

## Read before editing

Read root `AGENTS.md`, local README, and the source document the example illustrates.

Use the nearest README for local file purpose. Use source docs, schemas, generated builders, validators, and owner repos as stronger authority when they apply.

## Boundaries

- Do not let examples become the only statement of a rule.
- Do not cite examples as stronger than docs, schemas, mechanics cards, or owner repos.
- Keep examples small, clear, and linked to their source contract.

## Validation

Run the narrowest relevant checks first. Usual checks for this district:

```bash
python scripts/validate_links.py
python scripts/validate_markdown_shape.py
python -m pytest -q tests
```

If a listed validator is not present in the checkout yet, report that explicitly and run the closest available guardrail.

## Closeout

Report changed files, source surfaces consulted, generated files rebuilt or not rebuilt, checks run, checks skipped, and any owner boundary that may need follow-up.
