from __future__ import annotations

import argparse
from pathlib import Path

from agents_mesh_common import DEFAULT_GENERATED, load_json, read_config, repo_root_from


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate generated AGENTS mesh index shape.")
    parser.add_argument("--repo-root", default=None)
    args = parser.parse_args()
    repo_root = Path(args.repo_root).resolve() if args.repo_root else repo_root_from()
    config = read_config(repo_root)
    path = repo_root / DEFAULT_GENERATED
    if not path.exists():
        raise SystemExit(f"missing generated AGENTS mesh index: {path}")
    data = load_json(path)
    errors: list[str] = []
    if data.get("schema_version") != "aoa_agents_mesh_index_v1":
        errors.append("wrong schema_version")
    if data.get("source_ref") != "config/agents_mesh.json":
        errors.append("wrong source_ref")
    if data.get("authority_ref") != config.get("authority_ref"):
        errors.append("authority_ref does not match config")
    if data.get("validation_commands") != config.get("validation_commands", []):
        errors.append("validation_commands does not match config")
    if data.get("missing_cards"):
        errors.append(f"missing_cards is not empty: {data.get('missing_cards')}")
    cards = data.get("cards", [])
    if data.get("card_count") != len(cards):
        errors.append("card_count does not match cards length")
    paths = [card.get("path") for card in cards]
    if len(paths) != len(set(paths)):
        errors.append("duplicate card paths in generated index")
    for card in cards:
        if not card.get("sha256") or len(card.get("sha256", "")) != 64:
            errors.append(f"bad sha256 for {card.get('path')}")
        if card.get("line_count", 0) < 8:
            errors.append(f"card too short in generated index: {card.get('path')}")
    if errors:
        raise SystemExit("AGENTS mesh index validation failed:\n" + "\n".join(f"- {e}" for e in errors))
    print("generated AGENTS mesh index validated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
