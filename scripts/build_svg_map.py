#!/usr/bin/env python3
"""
Scan the `badges/` folder for .svg files and write a JSON mapping
of filename (without extension) -> file contents (as string) to
`badges/svgs.json`.

Run: python3 scripts/build_svg_map.py
"""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
BADGES = ROOT / "badges"
OUT = BADGES / "svgs.json"


def main():
    if not BADGES.exists():
        print(f"Badges folder not found: {BADGES}")
        return

    svgs = {}
    for p in sorted(BADGES.glob("*.svg")):
        key = p.stem
        try:
            text = p.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            text = p.read_text(encoding="latin-1")
        svgs[key] = text

    OUT.write_text(json.dumps(svgs, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Wrote {len(svgs)} svgs to {OUT}")


if __name__ == "__main__":
    main()
