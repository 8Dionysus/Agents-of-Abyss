#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path

from docs_thematic_common import (
    CLASSIFIER_REL,
    DISTRICT_README_HEADINGS,
    REPO_ROOT,
    build_plan,
    current_root_allowlist,
    load_classifier,
    validate_classifier_shape,
)


EXEMPT_GUARDRAIL_FILES = {"AGENTS.md", "README.md"}


def rel(path: Path) -> str:
    return path.relative_to(REPO_ROOT).as_posix()


def require_docs_root_surfaces(repo_root: Path, classifier: dict) -> list[str]:
    docs = repo_root / "docs"
    errors: list[str] = []
    for name in current_root_allowlist(classifier):
        if not (docs / name).exists():
            errors.append(f"missing docs/{name}")
    return errors


def require_district_readmes(repo_root: Path, classifier: dict) -> list[str]:
    errors: list[str] = []
    for district in classifier.get("districts", {}).values():
        path = repo_root / district["path"]
        readme = repo_root / district["readme"]
        if not path.exists():
            errors.append(f"missing district {district['path']}")
            continue
        if not readme.exists():
            errors.append(f"missing district readme: {district['readme']}")
            continue

        text = readme.read_text(encoding="utf-8")
        for heading in DISTRICT_README_HEADINGS:
            if heading not in text:
                errors.append(f"{district['readme']} missing heading {heading!r}")
    return errors


def require_guardrail_index_coverage(repo_root: Path) -> list[str]:
    guardrails = repo_root / "docs" / "guardrails"
    readme = guardrails / "README.md"
    if not readme.exists():
        return ["missing docs/guardrails/README.md"]

    text = readme.read_text(encoding="utf-8")
    errors: list[str] = []
    for path in sorted(guardrails.iterdir()):
        if not path.is_file() or path.name in EXEMPT_GUARDRAIL_FILES:
            continue
        if path.name not in text:
            errors.append(f"docs/guardrails/README.md does not index {rel(path)}")
    return errors


def require_docs_readme_routes(repo_root: Path, classifier: dict) -> list[str]:
    docs_readme = repo_root / "docs" / "README.md"
    if not docs_readme.exists():
        return ["missing docs/README.md"]

    text = docs_readme.read_text(encoding="utf-8")
    errors: list[str] = []
    for district in classifier.get("districts", {}).values():
        short = district["path"].replace("docs/", "") + "/"
        if short not in text and district["path"] not in text:
            errors.append(f"docs/README.md does not mention {district['path']}")
    return errors


def require_validation_refs(repo_root: Path, classifier: dict) -> list[str]:
    docs_agents = repo_root / "docs" / "AGENTS.md"
    guardrails_agents = repo_root / "docs" / "guardrails" / "AGENTS.md"
    release_check = repo_root / "scripts" / "release_check.py"
    surfaces = [
        docs_agents.read_text(encoding="utf-8") if docs_agents.exists() else "",
        guardrails_agents.read_text(encoding="utf-8") if guardrails_agents.exists() else "",
    ]
    release_text = release_check.read_text(encoding="utf-8") if release_check.exists() else ""

    errors: list[str] = []
    for command in classifier.get("validation_refs", []):
        if not any(command in surface for surface in surfaces):
            errors.append(f"docs AGENTS cards missing validation command: {command}")
        script_name = command.split()[1] if command.startswith("python ") and len(command.split()) > 1 else None
        if script_name and script_name not in release_text:
            errors.append(f"release_check.py missing docs guardrail command: {command}")
    return errors


def require_root_law_mentions(repo_root: Path) -> list[str]:
    root_law = repo_root / "docs" / "ROOT_SURFACE_LAW.md"
    if not root_law.exists():
        return ["missing docs/ROOT_SURFACE_LAW.md"]

    text = root_law.read_text(encoding="utf-8")
    errors: list[str] = []
    for required in ["docs thematic cleanup", "guardrails", "docs root"]:
        if required not in text:
            errors.append(f"ROOT_SURFACE_LAW.md missing {required!r}")
    return errors


def require_classifier_route(repo_root: Path) -> list[str]:
    docs_readme = repo_root / "docs" / "README.md"
    guardrails_agents = repo_root / "docs" / "guardrails" / "AGENTS.md"
    text = ""
    if docs_readme.exists():
        text += docs_readme.read_text(encoding="utf-8")
    if guardrails_agents.exists():
        text += "\n" + guardrails_agents.read_text(encoding="utf-8")
    if str(CLASSIFIER_REL) not in text:
        return [f"docs surfaces do not mention classifier {CLASSIFIER_REL}"]
    return []


def main() -> int:
    repo_root = REPO_ROOT
    docs = repo_root / "docs"
    errors: list[str] = []

    if not docs.exists():
        raise SystemExit("missing docs directory")

    classifier = load_classifier(repo_root)
    errors.extend(validate_classifier_shape(classifier))
    errors.extend(require_docs_root_surfaces(repo_root, classifier))
    errors.extend(require_district_readmes(repo_root, classifier))
    errors.extend(require_guardrail_index_coverage(repo_root))
    errors.extend(require_docs_readme_routes(repo_root, classifier))
    errors.extend(require_validation_refs(repo_root, classifier))
    errors.extend(require_root_law_mentions(repo_root))
    errors.extend(require_classifier_route(repo_root))

    leftovers = build_plan(repo_root, classifier)
    if leftovers:
        sources = ", ".join(item["source"] for item in leftovers)
        errors.append(f"flat docs still classify into districts: {sources}")

    if errors:
        raise SystemExit("docs thematic district validation failed:\n- " + "\n- ".join(errors))
    print("docs thematic districts validated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
