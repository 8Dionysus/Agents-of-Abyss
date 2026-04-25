# Link and Shape Hygiene Protocol

This protocol is the Wave E guardrail for local links, Markdown shape, status vocabulary, generated freshness, and known link-drift repair inside `Agents-of-Abyss`.

It does not author constitutional meaning. It keeps surfaces reachable, readable, and mechanically checkable so source-owned meaning can keep moving without losing its signs.

## Scope

Wave E owns hygiene checks for these failure modes:

- local Markdown links that point to files which no longer exist;
- old flat links that should now point into a mechanic package or thematic district;
- entry documents that collapse into one or two giant lines;
- docs that silently lose a top-level heading or second-level sections;
- status strings that drift outside their agreed vocabulary;
- generated capsules that are hand-edited or stale;
- known link repairs that remain tribal knowledge instead of becoming a checkable rule.

Wave E does not decide whether a doctrine is true. It only checks whether the map, shape, and generated mirrors still let an agent reach the stronger source.

## Ownership boundary

`Agents-of-Abyss` may own this protocol as center hygiene because it protects legibility of the constitutional polis.

The protocol must not become:

- technique truth owned by `aoa-techniques`;
- executable workflow truth owned by `aoa-skills`;
- proof or verdict truth owned by `aoa-evals`;
- memory truth owned by `aoa-memo`;
- role or persona truth owned by `aoa-agents`;
- scenario choreography owned by `aoa-playbooks`;
- KAG semantic authority owned by `aoa-kag` or `Tree-of-Sophia`;
- runtime implementation owned by `abyss-stack`.

If a hygiene finding touches one of those domains, this repository may route and label the finding, but the owner repository must land the fix or proof when owner-local truth is involved.

## Local link law

Local links should point to the nearest stable owner surface.

Use relative links when the target is inside the repository. Avoid flat convenience links when the target lives in a mechanic package or thematic district.

A local link is valid when:

1. the target file or directory exists;
2. the target does not escape the repository root;
3. generated files link back to source surfaces rather than pretending to author meaning;
4. optional anchor checks pass when the stricter anchor mode is enabled.

External links are not fetched by the validator. They are treated as outside this hygiene layer unless a future release adds a deliberate external-link checker.

## Known repair law

Known link drift must be captured in `config/link_shape_hygiene.json` under `link_validation.known_rewrites`.

A repair entry needs:

- `id` for stable reference;
- `file` for the surface to patch;
- `old` for the exact stale text;
- `new` for the replacement;
- `reason` for future agents.

The repair script can run in check mode or apply mode. Check mode fails when the stale text still exists. Apply mode rewrites only the exact known stale fragment.

## Markdown shape law

Markdown shape is not prose style. It is entry survivability.

A protected Markdown file should:

- end with a final newline;
- keep line lengths within the configured cap;
- keep a top-level heading where required;
- keep second-level headings where required;
- keep fenced code blocks balanced;
- avoid collapsing a public entry surface into a few enormous lines.

The shape target list lives in `config/link_shape_hygiene.json`. Future files should be added there when they become entry surfaces, district gates, generated gates, or mechanic gates.

## Status vocabulary law

Status words are small laws. They should not mutate casually.

Wave E validates status strings from configured JSON files against named vocabularies. This keeps `planted`, `landed`, `requested`, `operational`, and related words from becoming ornamental fog.

Adding a new status requires updating the vocabulary config and explaining why the existing ladder could not express the state.

## Generated freshness law

Generated capsules may accelerate agent entry. They must not author meaning.

A generated surface is fresh only when its builder can reproduce it in `--check` mode. If a builder is absent and the surface is optional, the freshness check skips it. If the surface is required, absence fails.

The Wave E generated capsule is:

```text
generated/link_shape_hygiene.min.json
```

It reflects the protocol and config. It does not replace them.
Other generated surfaces, including `generated/agents_mesh.min.json`, may be
registered as freshness targets when their builders are part of the release
gate.

## Agent route

When an agent touches links, shape, status, generated capsules, or known repairs, use this route:

1. Read this protocol.
2. Read `docs/HYGIENE_GUARDRAIL_INDEX.md`.
3. Inspect `config/link_shape_hygiene.json`.
4. Run the hygiene validators.
5. If a finding crosses owner boundaries, route the semantic fix to the stronger owner.
6. Keep any repair trace reviewable.

## Validation

Run:

```bash
python scripts/repair_known_link_drifts.py --check
python scripts/validate_links.py
python scripts/validate_markdown_shape.py
python scripts/validate_status_vocabulary.py
python scripts/build_link_shape_hygiene_index.py --check
python scripts/validate_link_shape_hygiene_index.py
python scripts/build_agents_mesh_index.py --check
python scripts/validate_generated_freshness.py
python scripts/validate_hygiene_suite.py
python -m pytest -q tests
```

The broader repository suite may add ecosystem, mechanic, owner-request, or thematic-district checks around these commands.

## Future change rule

When a new district, generated surface, or status ladder is added, update the config first, then the generated index, then tests.

Do not let the future become a room full of handwritten signs pointing at moved doors. The map must learn to regenerate its own labels.
