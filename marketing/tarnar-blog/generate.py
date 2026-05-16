#!/usr/bin/env python3
"""
TARNAR Blog Bulk Generator
1テーマ（YAML or CSV）から 30〜50 本の多言語 Markdown を一括生成する。

使い方:
  python3 generate.py --yaml batch/voice-school-full.yaml
  python3 generate.py --csv  csv/batch-rows.csv --batch-id tarnar-2026q2-a

出力:
  posts/{ja,en,ko,zh}/{batch_id}-{NNN}-{slug}.md

品質ゲート:
  医療・法律・投資勧誘のキーワードが title/angle に含まれる場合はスキップし警告する。
"""

import argparse
import csv
import hashlib
import os
import re
import sys
import unicodedata
from datetime import date

try:
    import yaml
except ImportError:
    yaml = None

# ---------------------------------------------------------------------------
# 定数・テンプレート
# ---------------------------------------------------------------------------

LANGS = ["ja", "en", "ko", "zh"]

BLOCKED_KEYWORDS = [
    "投資勧誘", "元本保証", "確実に儲", "医療", "診断", "治療",
    "guaranteed returns", "medical", "diagnosis", "treatment",
]

SITE_URL = "https://gmtj-japan-music-tourism.netlify.app"

SEO_TEMPLATES: dict[str, dict] = {
    "ja": {
        "meta_desc_tpl": "{angle}について、実践的な視点で解説します。声のプロフェッショナル TARNAR メソッドが基礎から丁寧にサポート。",
        "lead_tpl":     "{angle}は、多くの方が最初に迷うポイントのひとつです。このページでは実践的なアプローチを紹介します。",
        "h2_1":         "なぜこれが大切なのか",
        "h2_2":         "具体的な実践ステップ",
        "h2_3":         "よくある疑問と答え",
        "closing_tpl":  "まずは小さな一歩から。継続が声を育てます。",
        "links": [
            f"- Japan Music Tourism: {SITE_URL}/",
            "- AI TARNAR ポータル: /tarnar/",
            "- Izu Music Fund: /izu-fund/",
        ],
    },
    "en": {
        "meta_desc_tpl": "Learn about {angle} with TARNAR Method—practical, repeatable guidance from voice professionals at Japan Music Tourism.",
        "lead_tpl":     "{angle} is one of the first things many learners wonder about. Here's a practical approach you can start today.",
        "h2_1":         "Why This Matters",
        "h2_2":         "Step-by-Step Practice",
        "h2_3":         "Frequently Asked Questions",
        "closing_tpl":  "Start small, stay consistent. Your voice grows with deliberate practice.",
        "links": [
            f"- Japan Music Tourism: {SITE_URL}/",
            "- AI TARNAR portal: /tarnar/",
            "- Izu Music Fund: /izu-fund/",
        ],
    },
    "ko": {
        "meta_desc_tpl": "{angle}에 대해 TARNAR 메서드로 실천적인 관점에서 설명합니다. Japan Music Tourism의 보이스 전문가가 기초부터 지원합니다.",
        "lead_tpl":     "{angle}은(는) 많은 분들이 처음 헷갈리는 부분 중 하나입니다. 실천적인 접근법을 소개합니다.",
        "h2_1":         "왜 중요한가",
        "h2_2":         "구체적인 실천 단계",
        "h2_3":         "자주 묻는 질문",
        "closing_tpl":  "작은 한 걸음부터 시작하세요. 꾸준함이 목소리를 키웁니다.",
        "links": [
            f"- Japan Music Tourism: {SITE_URL}/",
            "- AI TARNAR 포털: /tarnar/",
        ],
    },
    "zh": {
        "meta_desc_tpl": "关于{angle}，TARNAR工法从实践角度为您详解。Japan Music Tourism的声音专家从基础到进阶全程支持。",
        "lead_tpl":     "{angle}是许多学习者一开始感到困惑的问题之一。本文介绍可以立即付诸实践的方法。",
        "h2_1":         "为什么这很重要",
        "h2_2":         "具体练习步骤",
        "h2_3":         "常见问题解答",
        "closing_tpl":  "从小处开始，坚持练习。您的声音会在积累中成长。",
        "links": [
            f"- Japan Music Tourism: {SITE_URL}/",
            "- AI TARNAR 门户: /tarnar/",
        ],
    },
}

# ---------------------------------------------------------------------------
# ユーティリティ
# ---------------------------------------------------------------------------

def slugify(text: str, max_len: int = 60) -> str:
    text = unicodedata.normalize("NFKD", text)
    text = text.encode("ascii", "ignore").decode("ascii")
    text = re.sub(r"[^\w\s-]", "", text).strip().lower()
    text = re.sub(r"[\s_-]+", "-", text)
    return text[:max_len].rstrip("-")


def short_hash(text: str, n: int = 6) -> str:
    return hashlib.md5(text.encode()).hexdigest()[:n]


def is_blocked(text: str) -> bool:
    lower = text.lower()
    return any(kw.lower() in lower for kw in BLOCKED_KEYWORDS)


def make_slug(pillar_short: str, angle: str, index: int) -> str:
    base = slugify(angle) or short_hash(angle)
    if not base:
        base = f"article-{index:03d}"
    return f"{pillar_short}-{base}" if pillar_short else base


# ---------------------------------------------------------------------------
# Markdown 生成
# ---------------------------------------------------------------------------

def render_article(
    lang: str,
    slug: str,
    title: str,
    pillar: str,
    pillar_short: str,
    angle: str,
    angle_local: str,
    batch_id: str,
    index: int,
    today: str,
) -> str:
    t = SEO_TEMPLATES[lang]
    meta_desc = t["meta_desc_tpl"].format(angle=angle_local)
    lead = t["lead_tpl"].format(angle=angle_local)
    closing = t["closing_tpl"]
    links = "\n".join(t["links"])

    # SEO: keyword in first H2 で自然な配置
    kw_note = f"<!-- SEO keyword: {angle_local} -->"

    lines = [
        "---",
        f"lang: {lang}",
        f"slug: {slug}",
        f"title: {title}",
        f"description: {meta_desc}",
        f"topic_pillar: {pillar}",
        f"pillar_short: {pillar_short}",
        f"angle: {angle_local}",
        f"batch_id: {batch_id}",
        f"batch_index: {index:03d}",
        f"date: {today}",
        "status: draft",
        "---",
        "",
        kw_note,
        "",
        f"## {angle_local}",
        "",
        lead,
        "",
        f"## {t['h2_1']}",
        "",
        f"<!-- TODO: {angle_local} の重要性・背景（2〜4文） -->",
        "",
        f"## {t['h2_2']}",
        "",
        f"<!-- TODO: 実践ステップ（番号リスト 3〜5 項目） -->",
        "",
        f"## {t['h2_3']}",
        "",
        f"<!-- TODO: Q&A 形式 1〜3 問 -->",
        "",
        "---",
        "",
        closing,
        "",
        "## Links",
        "",
        links,
    ]
    return "\n".join(lines) + "\n"


# ---------------------------------------------------------------------------
# YAML モード
# ---------------------------------------------------------------------------

def process_yaml(path: str, out_root: str) -> int:
    if yaml is None:
        print("ERROR: PyYAML が必要です。pip install pyyaml", file=sys.stderr)
        sys.exit(1)
    with open(path, encoding="utf-8") as f:
        cfg = yaml.safe_load(f)

    batch_id     = cfg.get("theme_id", "tarnar-batch")
    pillar       = cfg.get("pillar", "")
    pillar_short = cfg.get("pillar_short", slugify(pillar, 20))
    locale_primary = cfg.get("locale_primary", "ja")
    angles_raw   = cfg.get("angles", [])

    # 多言語マッピング（省略時は全言語同じ angle 文字列）
    # YAML で angles を辞書リストにも対応:
    #   - ja: ウォームアップ
    #     en: Warm-up
    #     ko: 워밍업
    #     zh: 热身
    count = 0
    today = str(date.today())

    for idx, raw in enumerate(angles_raw, start=1):
        if isinstance(raw, dict):
            angle_map = {lang: raw.get(lang, raw.get(locale_primary, "")) for lang in LANGS}
        else:
            angle_map = {lang: str(raw) for lang in LANGS}

        angle_ja = angle_map["ja"]
        if is_blocked(angle_ja) or is_blocked(angle_map["en"]):
            print(f"  SKIP [{idx:03d}] ブロックキーワード検出: {angle_ja}")
            continue

        slug = make_slug(pillar_short, angle_map[locale_primary], idx)

        for lang in LANGS:
            angle_local = angle_map[lang]
            # タイトル: 日本語は「〜の方法」スタイル、英語は How to / Guide
            if lang == "ja":
                title = f"{angle_ja} — {pillar}の実践ガイド"
            elif lang == "en":
                title = f"{angle_map['en']} — {pillar} Practice Guide"
            elif lang == "ko":
                title = f"{angle_map['ko']} — {pillar} 실전 가이드"
            else:
                title = f"{angle_map['zh']} — {pillar}实践指南"

            body = render_article(
                lang=lang, slug=slug, title=title,
                pillar=pillar, pillar_short=pillar_short,
                angle=angle_map[locale_primary], angle_local=angle_local,
                batch_id=batch_id, index=idx, today=today,
            )

            out_dir = os.path.join(out_root, lang)
            os.makedirs(out_dir, exist_ok=True)
            fname = f"{batch_id}-{idx:03d}-{slug}.md"
            fpath = os.path.join(out_dir, fname)
            with open(fpath, "w", encoding="utf-8") as fp:
                fp.write(body)

        count += 1
        print(f"  [{idx:03d}] {slug}")

    return count


# ---------------------------------------------------------------------------
# CSV モード
# ---------------------------------------------------------------------------

def process_csv(path: str, batch_id_override: str, out_root: str) -> int:
    count = 0
    today = str(date.today())

    with open(path, encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for idx, row in enumerate(reader, start=1):
            batch_id     = batch_id_override or row.get("batch_id", "tarnar-batch")
            pillar       = row.get("topic_pillar", "")
            pillar_short = slugify(pillar, 20)
            slug_base    = row.get("slug", "")
            slug         = slug_base or make_slug(pillar_short, row.get("angle_ja", ""), idx)

            angle_map = {
                "ja": row.get("angle_ja", ""),
                "en": row.get("angle_en", row.get("angle_ja", "")),
                "ko": row.get("angle_ko", row.get("angle_ja", "")),
                "zh": row.get("angle_zh", row.get("angle_ja", "")),
            }

            if is_blocked(angle_map["ja"]) or is_blocked(angle_map["en"]):
                print(f"  SKIP [{idx:03d}] ブロックキーワード検出: {angle_map['ja']}")
                continue

            for lang in LANGS:
                angle_local = angle_map[lang]
                if lang == "ja":
                    title = f"{angle_map['ja']} — {pillar}の実践ガイド"
                elif lang == "en":
                    title = f"{angle_map['en']} — {pillar} Practice Guide"
                elif lang == "ko":
                    title = f"{angle_map['ko']} — {pillar} 실전 가이드"
                else:
                    title = f"{angle_map['zh']} — {pillar}实践指南"

                body = render_article(
                    lang=lang, slug=slug, title=title,
                    pillar=pillar, pillar_short=pillar_short,
                    angle=angle_map["ja"], angle_local=angle_local,
                    batch_id=batch_id, index=idx, today=today,
                )

                out_dir = os.path.join(out_root, lang)
                os.makedirs(out_dir, exist_ok=True)
                fname = f"{batch_id}-{idx:03d}-{slug}.md"
                fpath = os.path.join(out_dir, fname)
                with open(fpath, "w", encoding="utf-8") as fp:
                    fp.write(body)

            count += 1
            print(f"  [{idx:03d}] {slug}")

    return count


# ---------------------------------------------------------------------------
# エントリーポイント
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(description="TARNAR Blog Bulk Generator")
    src = parser.add_mutually_exclusive_group(required=True)
    src.add_argument("--yaml", metavar="FILE", help="YAML テーマファイル")
    src.add_argument("--csv",  metavar="FILE", help="CSV バッチファイル")
    parser.add_argument("--batch-id", default="", help="CSV モード時のバッチID上書き")
    parser.add_argument(
        "--out", default=os.path.join(os.path.dirname(__file__), "posts"),
        help="出力ルートディレクトリ（既定: posts/）",
    )
    args = parser.parse_args()

    print(f"出力先: {args.out}")

    if args.yaml:
        print(f"YAMLモード: {args.yaml}")
        n = process_yaml(args.yaml, args.out)
    else:
        print(f"CSVモード: {args.csv}")
        n = process_csv(args.csv, args.batch_id, args.out)

    print(f"\n完了: {n} テーマ × 4言語 = {n * 4} ファイル生成")
    print("次: posts/ を確認し、TODO コメントを埋めて公開前レビューへ。")


if __name__ == "__main__":
    main()
