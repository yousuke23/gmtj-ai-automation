#!/usr/bin/env python3
"""Append ../js/gmtj-chrome.js before </body> on business portals (one-level under site/)."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "site"
SNIPPET = (
    '  <script src="../js/netlify-form.js" defer></script>\n'
    '  <script src="../js/gmtj-mailto.js" defer></script>\n'
    '  <script src="../js/gmtj-chrome.js" defer></script>\n'
)

SKIP = {"js", "legal", "gmtj-os", "automation", "social-templates"}


def main() -> None:
    for d in sorted(ROOT.iterdir()):
        if not d.is_dir() or d.name.startswith(".") or d.name in SKIP:
            continue
        idx = d / "index.html"
        if not idx.is_file():
            continue
        text = idx.read_text(encoding="utf-8")
        if "gmtj-chrome.js" in text and "gmtj-mailto.js" in text and "netlify-form.js" in text:
            continue
        if "gmtj-chrome.js" in text and "netlify-form.js" not in text:
            old = '  <script src="../js/gmtj-chrome.js" defer></script>\n'
            if "gmtj-mailto.js" in text and "netlify-form.js" not in text:
                old = (
                    '  <script src="../js/gmtj-mailto.js" defer></script>\n'
                    '  <script src="../js/gmtj-chrome.js" defer></script>\n'
                )
            text = text.replace(old, SNIPPET, 1)
            idx.write_text(text, encoding="utf-8")
            print("patched mailto+chrome", idx.relative_to(ROOT))
            continue
        if "</body>" not in text:
            continue
        text = text.replace("</body>", SNIPPET + "</body>", 1)
        idx.write_text(text, encoding="utf-8")
        print("patched", idx.relative_to(ROOT))


if __name__ == "__main__":
    main()
