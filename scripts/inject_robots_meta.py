#!/usr/bin/env python3
"""Add <meta name=\"robots\"> after the first viewport meta when missing (idempotent).

- site/automation/ → noindex, nofollow
- site/gmtj-os/ → noindex, nofollow
- all other HTML under site/ → index, follow
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "site"
VIEWPORT_RE = re.compile(
    r'(<meta\s+name=["\']viewport["\']\s+content=["\'][^"\']+["\']\s*/?>)',
    re.IGNORECASE,
)


def robots_value(rel: Path) -> str:
    if rel.parts and rel.parts[0] in ("automation", "gmtj-os"):
        return "noindex, nofollow"
    return "index, follow"


def main() -> None:
    updated = 0
    skipped_no_viewport: list[Path] = []
    for p in sorted(ROOT.rglob("*.html")):
        text = p.read_text(encoding="utf-8")
        if re.search(r'name=["\']robots["\']', text):
            continue
        m = VIEWPORT_RE.search(text)
        if not m:
            skipped_no_viewport.append(p.relative_to(ROOT))
            continue
        rw = robots_value(p.relative_to(ROOT))
        insert = f'{m.group(1)}\n  <meta name="robots" content="{rw}" />'
        text = VIEWPORT_RE.sub(insert, text, count=1)
        p.write_text(text, encoding="utf-8")
        updated += 1
    print("inject_robots_meta: updated", updated, "files")
    if skipped_no_viewport:
        print("inject_robots_meta: no viewport (skipped)", len(skipped_no_viewport))
        for r in skipped_no_viewport[:30]:
            print(" ", r)
        if len(skipped_no_viewport) > 30:
            print("  ...")


if __name__ == "__main__":
    main()
