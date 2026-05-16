#!/usr/bin/env python3
"""Regenerate #02–#07, #09–#20 business portal index.html to TARNAR-level layout."""
from __future__ import annotations

import html as html_lib
import re
import sys
import textwrap
from pathlib import Path


SITE = Path(__file__).resolve().parents[1] / "site"

PORTAL_DIRS = [
    "02-real-estate-revitalization",
    "03-123-music-resorts",
    "04-music-cafe-bar",
    "05-global-music-festival",
    "06-music-production-first",
    "07-music-community-japan",
    "09-voice-music-studio",
    "10-b2b-voice-communication",
    "11-tana-method-certification",
    "12-crowdfunding-ai-producer",
    "13-global-music-partnership",
    "14-regional-music-alliance",
    "15-subsidy-intelligence",
    "16-ma-music-business",
    "17-ai-gmtj-os",
    "18-global-digital-marketing",
    "19-japan-inbound-music-tourism",
    "20-global-music-education-hub",
]


def section_inner(page: str, sec_id: str) -> str:
    m = re.search(
        rf'(?s)<section class="block" id="{re.escape(sec_id)}">(.*?)</section>\s*(?=<section|<footer)',
        page,
    )
    return m.group(1).strip() if m else ""


def first_match(page: str, pat: str, group: int = 1) -> str:
    m = re.search(pat, page, re.S)
    return m.group(group).strip() if m else ""


def strip_tags(s: str) -> str:
    return re.sub(r"<[^>]+>", "", s).replace("&nbsp;", " ").strip()


def split_first_sentence(text: str) -> tuple[str, str]:
    t = strip_tags(text)
    for sep in ("。", ". ", "．"):
        if sep in t:
            i = t.index(sep) + len(sep)
            return t[:i].strip(), t[i:].strip()
    if len(t) > 100:
        return t[:100] + "…", t[100:]
    return t, ""


def cross_articles_filtered(cross_section_html: str) -> str:
    m2 = re.search(r'(?s)<div class="cross-grid">(.*?)</div>\s*</section>', cross_section_html)
    grid = m2.group(1) if m2 else ""
    arts = re.findall(r'<article class="cross-card"[^>]*>[\s\S]*?</article>', grid)
    out: list[str] = []
    for a in arts:
        if "<h3>AI TARNAR Voice School</h3>" in a and 'href="../tarnar/"' in a:
            continue
        if "<h3>Izu Music Fund</h3>" in a and 'href="../izu-fund/"' in a:
            continue
        a = a.replace(">TARNAR</a>", ">AI TARNAR Voice School</a>")
        a = a.replace("TARNAR ブログライブラリは", "AI TARNAR Voice School ブログライブラリは")
        out.append(a)
    return "\n        ".join(out)


def fix_line_section(line_inner: str) -> str:
    line_inner = line_inner.replace('class="btn btn-line"', 'class="btn btn-line js-line-cta"')
    if 'id="line-cta"' not in line_inner:
        line_inner = line_inner.replace(
            'class="btn btn-line js-line-cta"',
            'class="btn btn-line js-line-cta" id="line-cta"',
            1,
        )
    return line_inner


def build_page(src: str, folder: str) -> str:
    title = first_match(src, r"<title>(.*?)</title>")
    desc = first_match(src, r'<meta name="description" content="(.*?)"\s*/>')
    brand = first_match(src, r'<a class="nav-brand"[^>]*href="index\.html">(.*?)</a>')
    pill = first_match(src, r'<span class="brand-pill">(.*?)</span>')
    kicker = first_match(src, r'<p class="hero-kicker">(.*?)</p>')
    h1 = first_match(src, r"<h1>(.*?)</h1>")
    hero_m = re.search(r'<p class="hero-lead[^"]*"[^>]*>(.*?)</p>', src, re.S)
    hero_lead = hero_m.group(1).strip() if hero_m else ""

    services_block = section_inner(src, "services")
    blog_block = section_inner(src, "blog")
    line_block = fix_line_section(section_inner(src, "line"))
    cross_full = re.search(r'(?s)(<section class="block" id="cross">.*?</section>)', src)
    cross_html = cross_full.group(1) if cross_full else ""

    services_block = textwrap.indent(services_block, "      ").strip("\n")
    blog_block = textwrap.indent(blog_block, "      ").strip("\n")
    line_block = textwrap.indent(line_block, "      ").strip("\n")

    mission_lead = strip_tags(hero_lead)
    first_sent, _rest = split_first_sentence(hero_lead)
    mission_tagline = first_sent if first_sent else mission_lead[:120]
    brand_plain = strip_tags(html_lib.unescape(brand))
    cross_lead = f"「{brand_plain}」の体験設計に、声の学びと地域ファンドを自然に重ねられます。"

    cross_arts = cross_articles_filtered(cross_html)
    cross_arts_indented = textwrap.indent(cross_arts, "        ").strip("\n")

    desc_esc = html_lib.escape(html_lib.unescape(desc), quote=True)

    return f"""<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <meta name="robots" content="index, follow" />
  <title>{title}</title>
  <meta name="description" content="{desc_esc}" />
  <link rel="stylesheet" href="../tarnar/portal.css" />
</head>
<body>
  <header class="nav">
    <a class="nav-brand" href="index.html">{brand}</a>
    <nav class="nav-links" aria-label="ナビ">
      <a href="#mission">価値・目的</a>
      <a href="#services">サービス</a>
      <a href="#cross-highlight">声・地域</a>
      <a href="#blog">ブログ</a>
      <a href="#line">LINE</a>
      <a href="#cross">連動</a>
      <a href="../automation/">SNS・LINE運用</a>
      <a href="../gmtj-os/">GMTJ OS</a>
      <a href="../index.html">Japan Music Tourism</a>
    </nav>
  </header>

  <section class="hero" id="top">
    <div class="wrap hero-grid">
      <div class="hero-copy">
        <span class="brand-pill">{pill}</span>
        <p class="hero-kicker">{kicker}</p>
        <h1>{h1}</h1>
        <p class="hero-lead hero-lead--wide">{hero_lead}</p>
        <div class="hero-cta" style="justify-content: center; flex-wrap: wrap; gap: 0.65rem">
          <a class="btn btn-line js-line-cta" id="line-cta-hero" href="#line">公式LINEに登録する</a>
          <a class="btn btn-primary" href="#services">サービス・特徴を見る</a>
          <a class="btn btn-ghost" href="#blog">ブログ一覧</a>
          <a class="btn btn-ghost" href="../index.html#business-portals">全事業ポータル</a>
        </div>
      </div>
      <div class="hero-visual" aria-hidden="true"></div>
    </div>
  </section>

  <main class="wrap">
    <section class="block block-highlight" id="mission">
      <h2>価値提供と目的</h2>
      <p class="section-lead">{mission_lead}</p>
      <div class="mission-panel">
        <p class="mission-lead">{mission_tagline}</p>
        <p>Japan Music Tourism の導線設計に沿い、ゲスト・投資家・パートナーが同じ前提を共有できる情報設計を優先します。</p>
        <p>公式LINEでは先行案内・相談窓口・キャンペーンを一箇所に集約し、現場で迷子にならない運用につなげます。</p>
      </div>
    </section>

    <section class="block" id="services">
{services_block}
    </section>

    <section class="block" id="cross-highlight">
      <h2>声の学校 × 地域ファンド（クロス）</h2>
      <p class="section-lead">{html_lib.escape(cross_lead)}</p>
      <div class="cross-grid cross-grid--pair">
        <article class="cross-card cross-card--accent">
          <h3>AI TARNAR Voice School</h3>
          <p>発声・録音・ライブ・多言語の基礎から、イベント前後や店舗オペレーションにもそのまま使える声のケアまで一枚で。</p>
          <a class="btn btn-primary" href="../tarnar/">ポータルを開く</a>
        </article>
        <article class="cross-card cross-card--accent">
          <h3>Izu Music Fund</h3>
          <p>伊豆の音楽と地域をつなぐファンド。レポート・パートナー・共創プログラムの入口です。</p>
          <a class="btn btn-ghost" href="../izu-fund/">Izu Music Fund を開く</a>
        </article>
      </div>
    </section>

    <section class="block" id="blog">
{blog_block}
    </section>

    <section class="block" id="line">
{line_block}
    </section>

    <section class="block" id="cross">
      <h2>連動プログラム</h2>
      <p class="section-lead">Japan Music Tourism の事業群と自然につながる導線です。</p>
      <div class="cross-grid">
        {cross_arts_indented}
      </div>
    </section>
  </main>

  <footer class="site-footer">
    <div class="links" id="footer-related"></div>
    <p>© Japan Music Tourism · {brand}</p>
  </footer>

  <script src="portal.js" defer></script>
</body>
</html>
"""


def main() -> int:
    root = Path(SITE)
    if not root.is_dir():
        print("site/ not found", file=sys.stderr)
        return 1
    for d in PORTAL_DIRS:
        p = root / d / "index.html"
        if not p.is_file():
            print("skip missing", p, file=sys.stderr)
            continue
        src = p.read_text(encoding="utf-8")
        out = build_page(src, d)
        p.write_text(out, encoding="utf-8")
        print("wrote", p.relative_to(root))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
