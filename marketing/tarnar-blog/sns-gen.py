#!/usr/bin/env python3
"""
SNS Post Generator — ブログ記事 Markdown → 5プラットフォーム投稿テキスト一括出力

使い方:
  python3 sns-gen.py posts/ja/tarnar-2026q2-a-001-*.md --brand tarnar
  python3 sns-gen.py posts/ja/*.md --brand izu_music_fund --output sns-queue/

出力: 標準出力（プレビュー）または --output 指定ディレクトリへ {slug}-sns.json
"""

import argparse
import glob
import json
import os
import re
import sys
from datetime import date

# ---------------------------------------------------------------------------
# ブランド設定
# ---------------------------------------------------------------------------

BRANDS = {
    "tarnar": {
        "name": "AI TARNAR Voice School",
        "site_url": "https://gmtj-japan-music-tourism.netlify.app/tarnar/",
        "hashtags_ja": ["#AITARNAR", "#TARNAR", "#ボイトレ", "#JapanMusicTourism", "#音楽ツーリズム", "#声の学校"],
        "hashtags_en": ["#AITarnar", "#VoiceTraining", "#JapanMusicTourism", "#MusicTourism"],
        "hashtags_ko": ["#AITARNAR", "#보이스트레이닝", "#JapanMusicTourism", "#음악투어리즘"],
        "hashtags_zh": ["#AITARNAR", "#声乐训练", "#日本音乐旅游", "#音乐旅游"],
        "line_cta": "公式LINEでレッスン案内・クーポンを受け取る → line.me/R/ti/p/@tarnar",
        "image_style": "明るいスタジオ調、声と音楽のビジュアル、16:9またはポートレート9:16",
    },
    "izu_music_fund": {
        "name": "Izu Music Fund",
        "site_url": "https://gmtj-japan-music-tourism.netlify.app/izu-fund/",
        "hashtags_ja": ["#IzuMusicFund", "#伊豆", "#音楽ファンド", "#JapanMusicTourism", "#地域共創"],
        "hashtags_en": ["#IzuMusicFund", "#Izu", "#MusicFund", "#JapanMusicTourism"],
        "hashtags_ko": ["#이즈뮤직펀드", "#이즈", "#음악펀드", "#JapanMusicTourism"],
        "hashtags_zh": ["#伊豆音乐基金", "#伊豆", "#音乐基金", "#日本音乐旅游"],
        "line_cta": "公式LINEで月次レポート・投資家向け案内 → line.me/R/ti/p/@izumusicfund",
        "image_style": "伊豆の自然・温泉・音楽フォント、落ち着いたトーン",
    },
}

PLATFORM_LIMITS = {
    "tiktok":    {"caption": 2200, "hashtag_max": 30},
    "instagram": {"caption": 2200, "hashtag_max": 30},
    "youtube":   {"title": 100,   "description": 5000, "community": 500},
    "x":         {"text": 260},
    "facebook":  {"message": 63000},
}

# ---------------------------------------------------------------------------
# Markdown フロントマター解析
# ---------------------------------------------------------------------------

def parse_frontmatter(path: str) -> dict:
    """YAML フロントマターを簡易パース（pyyaml 任意）"""
    meta = {}
    try:
        with open(path, encoding="utf-8") as f:
            content = f.read()
    except OSError:
        return meta

    m = re.match(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
    if not m:
        return meta
    for line in m.group(1).splitlines():
        if ":" in line:
            k, _, v = line.partition(":")
            meta[k.strip()] = v.strip().strip('"').strip("'")

    # 本文の最初の非コメント段落をサマリーとして取る
    body = content[m.end():]
    paras = [p.strip() for p in body.split("\n\n") if p.strip() and not p.strip().startswith("#") and not p.strip().startswith("<!--")]
    meta["_summary"] = paras[0][:200] if paras else ""
    return meta


# ---------------------------------------------------------------------------
# テキストユーティリティ
# ---------------------------------------------------------------------------

def clip(text: str, n: int) -> str:
    t = re.sub(r"\s+", " ", text or "").strip()
    return t if len(t) <= n else t[: n - 1] + "…"


def tags_str(brand_key: str, lang: str) -> str:
    b = BRANDS.get(brand_key, BRANDS["tarnar"])
    key = f"hashtags_{lang}" if lang in ("ja", "en", "ko", "zh") else "hashtags_ja"
    return " ".join(b.get(key, b["hashtags_ja"]))


# ---------------------------------------------------------------------------
# 画像生成プロンプト
# ---------------------------------------------------------------------------

def image_prompt(brand_key: str, title: str, angle: str) -> dict:
    b = BRANDS.get(brand_key, BRANDS["tarnar"])
    return {
        "style": b["image_style"],
        "prompt_en": (
            f"Professional music education visual. Topic: '{angle}'. "
            f"Text overlay: '{clip(title, 60)}'. "
            f"Style: {b['image_style']}. No humans, no logos, photorealistic."
        ),
        "formats": {
            "square_1x1":    "1080x1080px — Instagram feed / Facebook",
            "portrait_4x5":  "1080x1350px — Instagram portrait / TikTok thumbnail",
            "vertical_9x16": "1080x1920px — TikTok / Reels / Stories",
            "landscape_16x9":"1920x1080px — YouTube thumbnail / Twitter card",
        },
        "note": "Canva / Midjourney / DALL-E 3 等で生成後、URLをブログ記事フロントマターの imageUrl に追記する。",
    }


# ---------------------------------------------------------------------------
# プラットフォーム別ビルダー
# ---------------------------------------------------------------------------

def build_pack(brand_key: str, meta: dict) -> dict:
    b = BRANDS.get(brand_key, BRANDS["tarnar"])
    lang = meta.get("lang", "ja")
    title = meta.get("title", "")
    angle = meta.get("angle", "")
    slug = meta.get("slug", "")
    summary = meta.get("_summary", "")
    url = meta.get("url", b["site_url"])
    tags = tags_str(brand_key, lang)
    lim = PLATFORM_LIMITS

    # TikTok
    tiktok = {
        "caption": clip(f"{title}\n{b['name']}\n{summary or '詳細はリンクへ'}\n{url}\n{tags}", lim["tiktok"]["caption"]),
        "hashtags": tags,
        "image_prompt": image_prompt(brand_key, title, angle),
        "notes": [
            "縦動画 9:16 推奨（15〜60秒）",
            "冒頭1秒にフック文言（タイトルをテキストオーバーレイ）",
            "ナレーションまたはBGMあり推奨",
        ],
    }

    # Instagram
    instagram = {
        "caption": clip(f"{title}\n\n{summary}\n\n{b['line_cta']}\n{url}\n\n{tags}", lim["instagram"]["caption"]),
        "hashtags": tags,
        "image_prompt": image_prompt(brand_key, title, angle),
        "notes": [
            "フィード: 1:1 または 4:5",
            "ストーリーズ: 9:16、リンクスタンプを付ける",
            "カルーセルは同テーマ3〜5枚で深掘り",
        ],
    }

    # YouTube
    yt_title = clip(title, lim["youtube"]["title"])
    youtube = {
        "video_title": yt_title,
        "description": clip(
            f"{summary}\n\n{url}\n\n{tags}\n\n—\n{b['name']} / Japan Music Tourism",
            lim["youtube"]["description"],
        ),
        "community_post": clip(f"{title}\n{summary}\n{url}", lim["youtube"]["community"]),
        "hashtags": tags,
        "image_prompt": image_prompt(brand_key, title, angle),
        "notes": [
            "ショート: 縦 9:16、60秒以内",
            "長尺: 5〜15分、同テーマ深掘り",
            "サムネイル: 1920x1080px、テキスト最小化",
        ],
    }

    # X (Twitter)
    x = {
        "text": clip(f"{title} {url} {tags}", lim["x"]["text"]),
        "thread": [
            clip(f"{title}\n{url}", lim["x"]["text"]),
            clip(summary, lim["x"]["text"]),
            clip(tags, lim["x"]["text"]),
        ],
        "image_prompt": image_prompt(brand_key, title, angle),
        "notes": [
            "画像は最大4枚",
            "長文はスレッド2〜3投稿に分割",
            "URLは最後に置くとリーチが上がる場合あり（テスト推奨）",
        ],
    }

    # Facebook
    facebook = {
        "message": clip(f"{title}\n\n{summary}\n\n{url}\n\n{tags}", lim["facebook"]["message"]),
        "hashtags": tags,
        "image_prompt": image_prompt(brand_key, title, angle),
        "notes": [
            "リンクプレビューを活かすため URL は本文早め",
            "グループ投稿は適切なコミュニティへ",
        ],
    }

    return {
        "brand": brand_key,
        "lang": lang,
        "slug": slug,
        "title": title,
        "angle": angle,
        "generated_date": str(date.today()),
        "platforms": {
            "tiktok": tiktok,
            "instagram": instagram,
            "youtube": youtube,
            "x": x,
            "facebook": facebook,
        },
    }


# ---------------------------------------------------------------------------
# エントリーポイント
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(description="SNS Post Generator")
    parser.add_argument("files", nargs="+", help="Markdown ファイル（glob 可）")
    parser.add_argument("--brand", default="tarnar", choices=list(BRANDS.keys()))
    parser.add_argument("--output", default="", help="出力ディレクトリ（省略時は stdout）")
    args = parser.parse_args()

    paths = []
    for pat in args.files:
        paths.extend(glob.glob(pat))
    paths = sorted(set(paths))

    if not paths:
        print("対象ファイルが見つかりません。", file=sys.stderr)
        sys.exit(1)

    if args.output:
        os.makedirs(args.output, exist_ok=True)

    for path in paths:
        meta = parse_frontmatter(path)
        if not meta.get("title"):
            print(f"  SKIP (フロントマターなし): {path}", file=sys.stderr)
            continue
        pack = build_pack(args.brand, meta)
        if args.output:
            slug = meta.get("slug", os.path.splitext(os.path.basename(path))[0])
            out_path = os.path.join(args.output, f"{slug}-sns.json")
            with open(out_path, "w", encoding="utf-8") as f:
                json.dump(pack, f, ensure_ascii=False, indent=2)
            print(f"  → {out_path}")
        else:
            print(f"\n{'='*60}")
            print(f"  {meta.get('title', path)}")
            print(f"{'='*60}")
            for plat, data in pack["platforms"].items():
                print(f"\n▶ {plat.upper()}")
                cap = data.get("caption") or data.get("text") or data.get("message") or data.get("video_title", "")
                print(cap[:300])
                print(f"  [画像指示] {data['image_prompt']['prompt_en'][:120]}…")

    print(f"\n完了: {len(paths)} 記事 × 5プラットフォーム")


if __name__ == "__main__":
    main()
