#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path

from docs_thematic_common import REPO_ROOT, load_classifier, validate_classifier_shape


def main() -> int:
    classifier = load_classifier(REPO_ROOT)
    errors = validate_classifier_shape(classifier)
    districts = classifier.get("districts", {})

    for item in classifier.get("exact_migrations", []):
        district = item.get("district")
        target = item.get("target", "")
        if district in districts and not target.startswith(districts[district]["path"] + "/"):
            errors.append(f"exact migration target {target} is not under district {district}")
        if Path(item.get("source", "")).name == "README.md":
            errors.append("migration map must not move README.md surfaces")

    for rule in classifier.get("pattern_migrations", []):
        district = rule.get("district")
        target_dir = rule.get("target_dir", "")
        source_glob = rule.get("source_glob", "")
        external_owner_route = rule.get("external_owner_route")

        if district not in districts:
            errors.append(f"pattern migration has unknown district {district}")
            continue

        district_path = districts[district]["path"]
        if target_dir != district_path:
            if not external_owner_route:
                errors.append(f"pattern migration target_dir {target_dir} does not match district {district}")
            elif external_owner_route != target_dir:
                errors.append(
                    f"pattern migration external_owner_route {external_owner_route} must match target_dir {target_dir}"
                )
            elif not (REPO_ROOT / external_owner_route).is_dir():
                errors.append(f"pattern migration external owner route does not exist: {external_owner_route}")

        if source_glob.startswith("docs/") and "README" in source_glob.upper():
            errors.append(f"pattern migration must not catch README surfaces: {source_glob}")

    if errors:
        raise SystemExit("docs migration map validation failed:\n- " + "\n- ".join(errors))
    print("docs migration map validated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
