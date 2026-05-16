#!/usr/bin/env python3
"""site/tarnar/index.html の月額決済リンク href を、環境変数または既定 mailto に毎回設定する（冪等）。

  SITE_STRIPE_TARNAR_MONTHLY — Stripe Payment Link 等（任意）
  SITE_PAYJP_TARNAR_MONTHLY  — PAY.JP 決済 URL（任意）

未設定時は mailto（123@atono.jp）へ誘導します。HTML 側に data-tarnar-stripe-monthly /
data-tarnar-payjp-monthly を付けた <a> が1つずつ必要です。
"""
from __future__ import annotations

import os
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HTML = ROOT / "site" / "tarnar" / "index.html"

DEFAULT_STRIPE = (
    "mailto:123@atono.jp?"
    "subject=AI%20TARNAR%20Voice%20School%20%E6%9C%88%E9%A1%8D%E7%94%B3%E8%BE%BC%EF%BC%88Stripe%EF%BC%89&"
    "body=%E3%81%8A%E5%90%8D%E5%89%8D%E3%81%A8%E9%80%A3%E7%B5%A1%E5%85%88%E3%82%92%E8%A8%98%E8%BC%89%E3%81%97%E3%81%A6%E3%81%8A%E9%80%81%E3%82%8A%E3%81%8F%E3%81%A0%E3%81%95%E3%81%84%E3%80%82"
)
DEFAULT_PAYJP = (
    "mailto:123@atono.jp?"
    "subject=AI%20TARNAR%20Voice%20School%20%E6%9C%88%E9%A1%8D%E7%94%B3%E8%BE%BC%EF%BC%88PAY.JP%EF%BC%89&"
    "body=%E3%81%8A%E5%90%8D%E5%89%8D%E3%81%A8%E9%80%A3%E7%B5%A1%E5%85%88%E3%82%92%E8%A8%98%E8%BC%89%E3%81%97%E3%81%A6%E3%81%8A%E9%80%81%E3%82%8A%E3%81%8F%E3%81%A0%E3%81%95%E3%81%84%E3%80%82"
)


def _href_escape(url: str) -> str:
    return url.replace("&", "&amp;").replace('"', "&quot;")


def _patch_by_data_attr(text: str, data_attr: str, new_href: str) -> str:
    esc = _href_escape(new_href)
    pat = re.compile(
        rf'(<a\b[^>]*\bdata-{re.escape(data_attr)}\b[^>]*\bhref=")([^"]*)(")',
        re.IGNORECASE,
    )

    def repl(m: re.Match[str]) -> str:
        return m.group(1) + esc + m.group(3)

    new_text, n = pat.subn(repl, text, count=1)
    if n != 1:
        raise SystemExit(f"inject_tarnar_payment_urls: missing or duplicate data-{data_attr} anchor")
    return new_text


def main() -> None:
    text = HTML.read_text(encoding="utf-8")
    stripe = (os.environ.get("SITE_STRIPE_TARNAR_MONTHLY") or "").strip() or DEFAULT_STRIPE
    payjp = (os.environ.get("SITE_PAYJP_TARNAR_MONTHLY") or "").strip() or DEFAULT_PAYJP
    text = _patch_by_data_attr(text, "tarnar-stripe-monthly", stripe)
    text = _patch_by_data_attr(text, "tarnar-payjp-monthly", payjp)
    HTML.write_text(text, encoding="utf-8")
    print(
        "inject_tarnar_payment_urls: ok (stripe="
        + ("env" if (os.environ.get("SITE_STRIPE_TARNAR_MONTHLY") or "").strip() else "mailto")
        + ", payjp="
        + ("env" if (os.environ.get("SITE_PAYJP_TARNAR_MONTHLY") or "").strip() else "mailto")
        + ")",
    )


if __name__ == "__main__":
    main()
