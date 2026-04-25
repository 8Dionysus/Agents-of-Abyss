# AGENTS.md

## Applies to

This card applies to `assets/` and all descendants unless a nearer `AGENTS.md` narrows the path.

## Role

`assets/` holds images, static media, and visual assets used by human-facing documentation.

## Read before editing

Read root `AGENTS.md` and check the referencing Markdown before adding, moving, or deleting assets.

Use the nearest README for local file purpose. Use source docs, schemas, generated builders, validators, and owner repos as stronger authority when they apply.

## Boundaries

- Assets support meaning; they do not prove or author meaning.
- Do not break referenced paths in README or docs.
- Do not add large, generated, private, or license-unclear media without clear purpose.

## Validation

Run the narrowest relevant checks first. Usual checks for this district:

```bash
python scripts/validate_links.py
python scripts/validate_markdown_shape.py
```

If a listed validator is not present in the checkout yet, report that explicitly and run the closest available guardrail.

## Closeout

Report changed files, source surfaces consulted, generated files rebuilt or not rebuilt, checks run, checks skipped, and any owner boundary that may need follow-up.
