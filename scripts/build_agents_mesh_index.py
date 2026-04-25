from __future__ import annotations

import argparse
from pathlib import Path

from agents_mesh_common import DEFAULT_GENERATED, build_index, dump_min_json, repo_root_from


def main() -> int:
    parser = argparse.ArgumentParser(description="Build generated AGENTS mesh index.")
    parser.add_argument("--check", action="store_true", help="fail if generated index is stale")
    parser.add_argument("--repo-root", default=None)
    args = parser.parse_args()

    repo_root = Path(args.repo_root).resolve() if args.repo_root else repo_root_from()
    out = repo_root / DEFAULT_GENERATED
    data = dump_min_json(build_index(repo_root))

    if args.check:
        if not out.exists():
            raise SystemExit(f"missing generated AGENTS mesh index: {out}")
        current = out.read_text(encoding="utf-8")
        if current != data:
            raise SystemExit("generated AGENTS mesh index is stale; run python scripts/build_agents_mesh_index.py")
        print("generated AGENTS mesh index is current")
        return 0

    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(data, encoding="utf-8")
    print(f"wrote {out.relative_to(repo_root)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
