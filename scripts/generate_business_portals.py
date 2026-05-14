#!/usr/bin/env python3
"""Generate static mini-portals for GMTJ businesses (01–20 except 08 tarnar, 21 izu-fund)."""
from __future__ import annotations

import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "site"
PORTAL_JS_SRC = SITE / "tarnar" / "portal.js"

# id, slug, brand_pill, priority, meta_desc, kicker, h1_line1, h1_line2, lead,
# (pill1, h3_1, p1), (pill2, h3_2, p2), (pill3, h3_3, p3), cross_extra (HTML fragment or "")
Biz = tuple[str, str, str, bool, str, str, str, str, str, tuple, tuple, tuple, str]

BUSINESSES: list[Biz] = [
    (
        "01",
        "01-global-music-tour",
        "Global Music Tour",
        True,
        "英語インバウンド向けの音楽ツアー設計・安全・マナー・導線。Japan Music Tourism #01。",
        "Tour × Inbound",
        "音楽と移動を、",
        "安心の一本道に。",
        "ルート設計、参加前チェック、多言語案内までを一枚にまとめます。フェスや滞在プランとも自然につなぎ、現場で迷わない導線をつくります。",
        ("Route", "ルートと時間割", "移動負荷と体験密度のバランスを先に決め、雨天・混雑時の代替も一言で示せる型にします。"),
        ("Safety", "安全とマナー", "公式情報を起点に、撮影・会場・移動の注意を短く反復できるチェックリストに落とします。"),
        ("Guide", "多言語ゲスト", "英語を軸に、必要に応じて中国語・韓国語の要点を添えた案内の骨子を用意します。"),
        """<article class="cross-card">
          <h3>SNS・LINE運用</h3>
          <p>告知・FAQ・当日連絡の型を自動化ラインとつなぎます。</p>
          <a class="btn btn-ghost" href="../automation/">運用ポータル</a>
        </article>""",
    ),
    (
        "02",
        "02-real-estate-revitalization",
        "Real Estate & Revitalization",
        False,
        "音楽と地域を軸にした不動産・まちづくりの企画導線。Japan Music Tourism #02。",
        "Place × Revitalization",
        "場所の価値を、",
        "音楽で再点火。",
        "滞在・体験・ブランドストーリーを束ね、投資家・自治体・ゲスト双方に伝わる一枚絵をつくります。",
        ("Story", "ストーリー設計", "地域の音楽資源と建物・土地の強みを短い物語にまとめます。"),
        ("Ops", "運用と導線", "内覧・イベント・パートナー連携まで、問い合わせの受け皿を一本化します。"),
        ("Partner", "パートナー連携", "宿泊・ツアー・ファンド案件へクロスする導線を用意します。"),
        "",
    ),
    (
        "03",
        "03-123-music-resorts",
        "123 MUSIC & RESORTS",
        True,
        "宿泊・リゾートと音楽体験の統合。レッスン前後の滞在も含めた設計。Japan Music Tourism #03。",
        "Stay × Music",
        "泊まるほどに、",
        "音が深まる。",
        "リゾート滞在とライブ・レッスン・録音体験を組み合わせ、日程と移動負荷を先に決めたプランに落とし込みます。",
        ("Stay", "滞在プログラム", "泊数と体験密度を調整し、高齢ゲストにも読みやすい行程表にします。"),
        ("Voice", "声の学び", "AI TARNAR Voice School と接続し、旅前後のレッスン導線を設計できます。"),
        ("Region", "地域と還流", "Izu Music Fund など地域ファンドとも自然につながる案内を整えます。"),
        """<article class="cross-card">
          <h3>AI TARNAR Voice School</h3>
          <p>滞在中のレッスンやオンライン併用の導線です。</p>
          <a class="btn btn-ghost" href="../tarnar/">ポータルを開く</a>
        </article>""",
    ),
    (
        "04",
        "04-music-cafe-bar",
        "Music Cafe & Bar",
        False,
        "カフェ・バーでの音楽体験と運営コミュニケーション。Japan Music Tourism #04。",
        "Hospitality × Live",
        "一杯のあいだに、",
        "ライブの温度。",
        "セットリスト・音量・撮影ルールをゲストに伝わる短い文面にまとめ、スタッフシフト間でもブレない運用にします。",
        ("Guest", "ゲスト案内", "入店から退店まで、安全と楽しさのバランスを一文ずつ整えます。"),
        ("Ops", "店内オペレーション", "ピーク時の案内・混雑・エスカレーションの型を用意します。"),
        ("Cross", "地域連携", "フェス・ツアー・インバウンド導線とつなぐメッセージを統一します。"),
        "",
    ),
    (
        "05",
        "05-global-music-festival",
        "Global Music Festival",
        True,
        "国際的な音楽フェスの動員・安全・多言語コミュニケーション。Japan Music Tourism #05。",
        "Festival × Scale",
        "動員の波を、",
        "安全と歓迎で受ける。",
        "チケット導線、現地案内、トラブル時の一言メッセージまでをテンプレ化し、SNS・LINE・現場アナウンスの表記ゆれを抑えます。",
        ("Crowd", "動員と導線", "混雑ピークと移動ハブを先に定義し、看板とプッシュ通知の文言を揃えます。"),
        ("Safety", "安全コミュニケーション", "熱中症・雨天・緊急時の定型文を短く分かりやすくします。"),
        ("Global", "多言語ゲスト", "英語を軸に、必要に応じて中国語・韓国語の要点を添えます。"),
        """<article class="cross-card">
          <h3>SNS・LINE運用</h3>
          <p>開催前後の告知と当日連絡を一元化します。</p>
          <a class="btn btn-ghost" href="../automation/">運用ポータル</a>
        </article>""",
    ),
    (
        "06",
        "06-music-production-first",
        "Music Production First",
        True,
        "楽曲制作・収録・クレジット表記までの制作導線。Japan Music Tourism #06。",
        "Production × Quality",
        "アイデアから、",
        "マスターまで一直線。",
        "デモ評価、セッション設計、権利表記のたたき台までを一枚のチェックリストにし、クライアントとクリエイターの認識差を減らします。",
        ("Session", "セッション設計", "楽器編成・録音環境・納品形式を先に固定し、手戻りを抑えます。"),
        ("Rights", "権利と表記", "クレジット・サンプル利用・二次利用の境界を短文で共有します。"),
        ("Studio", "スタジオ連携", "Voice & Music Studio など現場オペとつなぐ導線を用意します。"),
        """<article class="cross-card">
          <h3>SNS・LINE運用</h3>
          <p>リリース告知・制作裏側の発信テンプレを揃えます。</p>
          <a class="btn btn-ghost" href="../automation/">運用ポータル</a>
        </article>""",
    ),
    (
        "07",
        "07-music-community-japan",
        "Music × Community Japan",
        False,
        "地域コミュニティと音楽活動の継続設計。Japan Music Tourism #07。",
        "Community × Sustain",
        "つながりを、",
        "音で育てる。",
        "ワークショップ・定期演奏・ボランティア導線を設計し、継続率と安全性のバランスを取ります。",
        ("Program", "プログラム", "初参加からリピーターまで段階的な難易度設計を行います。"),
        ("Care", "ケアと安全", "子ども・高齢者参加時の配慮事項をテンプレ化します。"),
        ("Region", "地域横断", "コンシェルジュ・ツアー導線と整合するメッセージにします。"),
        "",
    ),
    (
        "09",
        "09-voice-music-studio",
        "Voice & Music Studio",
        False,
        "レコーディング・レッスン・機材を扱うスタジオ運営の案内。Japan Music Tourism #09。",
        "Studio × Session",
        "音を閉じ込め、",
        "可能性を開く。",
        "ブッキング・機材説明・初回来店の案内を短く揃え、制作案件ともスムーズに接続します。",
        ("Booking", "予約と料金", "公開できる範囲の情報を整理し、問い合わせ窓口を明確にします。"),
        ("Gear", "機材と環境", "マイク・モニター・取り扱いをゲスト向けに平易に説明します。"),
        ("School", "レッスン連携", "AI TARNAR Voice School とのクロス案内を用意します。"),
        "",
    ),
    (
        "10",
        "10-b2b-voice-communication",
        "B2B Voice & Communication",
        False,
        "企業向けボイス・コミュニケーション研修と導入支援。Japan Music Tourism #10。",
        "B2B × Voice",
        "組織の声を、",
        "ブランドに変える。",
        "プレゼン・客服・対外説明の型を整え、部門横断で使える短いスクリプトに落とします。",
        ("Training", "研修設計", "職種別に演習とフィードバックの型を用意します。"),
        ("Script", "スクリプト", "FAQ・謝罪・エスカレーションの境界を明文化します。"),
        ("Scale", "展開", "多拠点・多言語展開のたたき台を作成します。"),
        "",
    ),
    (
        "11",
        "11-tana-method-certification",
        "Tana Method Certification",
        False,
        "認定プログラム・試験運営・修了導線の設計。Japan Music Tourism #11。",
        "Certification × Trust",
        "学びを、",
        "認定で形に。",
        "カリキュラム公開範囲、試験申込、修了後の権利表記を整理し、運営負荷を下げます。",
        ("Curriculum", "カリキュラム", "モジュール単位で公開・非公開を切り分けます。"),
        ("Exam", "試験運営", "不正防止とアクセシビリティの両立を考慮します。"),
        ("Brand", "ブランド統一", "ロゴ・称号の使い方を一枚にまとめます。"),
        "",
    ),
    (
        "12",
        "12-crowdfunding-ai-producer",
        "Crowdfunding AI Producer",
        False,
        "クラウドファンディング企画とリターン設計の支援。Japan Music Tourism #12。",
        "Funding × Story",
        "想いを、",
        "数字に耐える形へ。",
        "リターン履行可能範囲を先に定義し、更新頻度とトーンを統一したコミュニケーションにします。",
        ("Plan", "企画構成", "ストーリー・目標金額・スケジュールの骨子を整えます。"),
        ("Return", "リターン", "配送・デジタル特典・イベント招待の境界を明確にします。"),
        ("Update", "更新運用", "サポーター向けメッセージの型を用意します。"),
        "",
    ),
    (
        "13",
        "13-global-music-partnership",
        "Global Music Partnership",
        False,
        "海外パートナー・共同制作・ライセンスの窓口設計。Japan Music Tourism #13。",
        "Partnership × Global",
        "国境をまたぐ、",
        "音の共同事業。",
        "初回コンタクトから契約前までのFAQと、社内稟議用の短文サマリを用意します。",
        ("Contact", "窓口設計", "タイムゾーンと言語を考慮した一次返信の型をつくります。"),
        ("Deal", "案件整理", "スコープ・権利・納期のたたき台を共有します。"),
        ("Brand", "ブランド整合", "グループ横断の表記ルールに合わせます。"),
        "",
    ),
    (
        "14",
        "14-regional-music-alliance",
        "Regional Music Alliance",
        False,
        "AI観光コンシェルジュ・地域案内の設計。Japan Music Tourism #14。",
        "Concierge × Region",
        "旅の途中で、",
        "すぐ聞ける案内。",
        "意図分類・エスカレーション・多言語テンプレを整備し、公式情報に根ざした応答方針を一枚にまとめます。",
        ("Intent", "意図分類", "予約・交通・安全・イベントなどの境界を定義します。"),
        ("Escalation", "エスカレーション", "人間に渡す条件を明文化します。"),
        ("KB", "ナレッジ", "kb/ 方針と整合する公開文面の骨子を用意します。"),
        "",
    ),
    (
        "15",
        "15-subsidy-intelligence",
        "Subsidy Intelligence",
        False,
        "補助金・助成の探索と社内稟議用サマリ。Japan Music Tourism #15。",
        "Grant × Clarity",
        "制度を、",
        "使える形に翻訳。",
        "要件整理・締切・必要書類のチェックリストを短くまとめ、法務確認ポイントを添えます。",
        ("Scan", "要件整理", "対象事業・上限・重複申請の注意を一覧化します。"),
        ("Doc", "書類たたき台", "計画書の章立てを固定します。"),
        ("Review", "レビュー", "最終判断は専門家・社内法務へ委ねる導線を明示します。"),
        "",
    ),
    (
        "16",
        "16-ma-music-business",
        "M&A Music Business",
        False,
        "音楽事業のM&A初期整理とデータルーム準備。Japan Music Tourism #16。",
        "M&A × Music",
        "価値を、",
        "数字と物語で示す。",
        "NDA前に共有できる範囲のサマリと、機密区分のたたき台を用意します。",
        ("Teaser", "ティーザー", "売却側の強みを一文で整理します。"),
        ("Data", "データルーム", "楽曲権利・契約・KPIの棚卸し項目を列挙します。"),
        ("Process", "プロセス", "デューデリジェンスの段取りを共有します。"),
        "",
    ),
    (
        "17",
        "17-ai-gmtj-os",
        "AI GMTJ OS（Tana OS）",
        False,
        "全事業横断のデータ基盤・運用ダッシュボードへの導線。Japan Music Tourism #17。",
        "OS × Operations",
        "21事業を、",
        "ひとつの画面で。",
        "進捗・自動化・重点事業の可視化を GMTJ OS でまとめ、各ポータルへ戻る導線を一本化します。",
        ("Dash", "ダッシュボード", "今日の実行結果と重点カードを中心に据えます。"),
        ("Workflow", "ワークフロー", "事業別の登録フローを追跡します。"),
        ("Link", "各事業ポータル", "現場の窓口へすぐ戻れるリンク集を維持します。"),
        "",
    ),
    (
        "18",
        "18-global-digital-marketing",
        "Global Digital Marketing",
        False,
        "横断マーケ・コンテンツ柱・チャネル運用。Japan Music Tourism #18。",
        "Marketing × Reach",
        "発信を、",
        "導線に変える。",
        "コンテンツ柱・カレンダー・KW を整理し、キャンペーン単位で表記ゆれを抑えます。",
        ("Pillar", "コンテンツ柱", "エリア・季節・事業の軸を固定します。"),
        ("Channel", "チャネル", "SNS・LINE・検索の役割分担を定義します。"),
        ("Measure", "計測", "ランディングと問い合わせまでの導線を短くします。"),
        "",
    ),
    (
        "19",
        "19-japan-inbound-music-tourism",
        "Japan Inbound Music Tourism",
        False,
        "インバウンド向け音楽観光の統合プロモーション。Japan Music Tourism #19。",
        "Inbound × Music",
        "海外から、",
        "日本の音旅へ。",
        "到着前後の案内・安全・マナーを多言語で揃え、ツアー・フェス・滞在へ接続します。",
        ("Story", "ストーリー", "地域と音楽の魅力を一続きの物語にします。"),
        ("Safety", "安全", "移動・会場・撮影の注意を反復しやすくします。"),
        ("Stay", "滞在接続", "宿泊・リゾート・ファンド導線と整合します。"),
        "",
    ),
    (
        "20",
        "20-global-music-education-hub",
        "Global Music Education Hub",
        False,
        "音楽教育ハブ・教材・国際連携の設計。Japan Music Tourism #20。",
        "Education × Hub",
        "学びの入口を、",
        "世界へ開く。",
        "カリキュラム公開範囲、言語別導線、修了証明の表記を整理し、現場運用に耐える型にします。",
        ("Course", "コース設計", "入門から専門までの段階を定義します。"),
        ("Lang", "多言語", "教材とサポート窓口の言語方針を揃えます。"),
        ("Hub", "ハブ機能", "パートナー教育機関との接続導線を用意します。"),
        "",
    ),
]


def build_index_html(b: Biz) -> str:
    (
        bid,
        slug,
        brand,
        _priority,
        meta_desc,
        kicker,
        h1a,
        h1b,
        lead,
        c1,
        c2,
        c3,
        cross_extra,
    ) = b
    be = html.escape(brand)
    de = html.escape(meta_desc)
    ke = html.escape(kicker)
    h1ae = html.escape(h1a)
    h1be = html.escape(h1b)
    le = html.escape(lead)

    def card(pill: str, h3: str, p: str) -> str:
        return f"""        <article class="card">
          <span class="pill">{html.escape(pill)}</span>
          <h3>{html.escape(h3)}</h3>
          <p>{html.escape(p)}</p>
        </article>"""

    cards_html = "\n".join(
        [
            card(c1[0], c1[1], c1[2]),
            card(c2[0], c2[1], c2[2]),
            card(c3[0], c3[1], c3[2]),
        ]
    )

    cross_standard = """        <article class="cross-card">
          <h3>AI TARNAR Voice School</h3>
          <p>声の学びと旅を組み合わせた体験導線です。</p>
          <a class="btn btn-ghost" href="../tarnar/">ポータルを開く</a>
        </article>
        <article class="cross-card">
          <h3>Izu Music Fund</h3>
          <p>地域と音楽をつなぐファンドの記事と案内です。</p>
          <a class="btn btn-ghost" href="../izu-fund/">ポータルを開く</a>
        </article>"""
    gmtj_os_card = """        <article class="cross-card">
          <h3>GMTJ OS</h3>
          <p>運用ダッシュボードで進捗と自動実行を確認します。</p>
          <a class="btn btn-ghost" href="../gmtj-os/">ダッシュボードを開く</a>
        </article>"""
    cross_parts = [cross_standard.rstrip()]
    if bid == "17":
        cross_parts.append(gmtj_os_card.rstrip())
    if cross_extra.strip():
        cross_parts.append(cross_extra.strip())
    cross_block = "\n".join(cross_parts)

    return f"""<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{be} | ポータル</title>
  <meta name="description" content="{de}" />
  <link rel="stylesheet" href="../tarnar/portal.css" />
</head>
<body>
  <header class="nav">
    <a class="nav-brand" href="index.html">{be}</a>
    <nav class="nav-links" aria-label="ナビ">
      <a href="#services">サービス</a>
      <a href="#blog">ブログ</a>
      <a href="#line">LINE</a>
      <a href="#cross">連動</a>
      <a href="../automation/">SNS・LINE運用</a>
      <a href="../index.html">Japan Music Tourism</a>
      <a href="../gmtj-os/">GMTJ OS</a>
    </nav>
  </header>

  <section class="hero" id="top">
    <div class="wrap hero-grid">
      <div class="hero-copy">
        <span class="brand-pill">{be}</span>
        <p class="hero-kicker">GMTJ #{bid} · {ke}</p>
        <h1>{h1ae}<br />{h1be}</h1>
        <p class="hero-lead">
          {le}
        </p>
        <div class="hero-cta" style="justify-content: center">
          <a class="btn btn-primary" href="#line">公式LINEはこちら</a>
          <a class="btn btn-ghost" href="#blog">ブログ一覧</a>
          <a class="btn btn-ghost" href="../automation/">SNS・LINE運用</a>
          <a class="btn btn-ghost" href="https://atono.co.jp/" rel="noopener noreferrer" target="_blank">atono co., ltd.</a>
        </div>
      </div>
      <div class="hero-visual" aria-hidden="true"></div>
    </div>
  </section>

  <main class="wrap">
    <section class="block" id="services">
      <h2>サービス</h2>
      <p class="section-lead">
        企画・導線・運用を短い型に落とし、現場でそのまま使えるコミュニケーションに整えます。
      </p>
      <div class="grid-3">
{cards_html}
      </div>
    </section>

    <section class="block" id="blog">
      <h2>ブログ記事一覧</h2>
      <p class="section-lead">
        事例・運用メモ・チェックリストを順次掲載します。
      </p>
      <ul class="blog-list" id="blog-list"></ul>
    </section>

    <section class="block" id="line">
      <h2>公式LINE</h2>
      <p class="section-lead">
        最新情報やキャンペーンをお届けします。
      </p>
      <div class="hero-cta" style="justify-content: flex-start">
        <a class="btn btn-line" id="line-cta" href="#">LINEで受け取る</a>
      </div>
    </section>

    <section class="block" id="cross">
      <h2>連動プログラム</h2>
      <p class="section-lead">Japan Music Tourism の事業群と自然につながる導線です。</p>
      <div class="cross-grid">
{cross_block}
      </div>
    </section>
  </main>

  <footer class="site-footer">
    <div class="links" id="footer-related"></div>
    <p>© Japan Music Tourism · {be}</p>
  </footer>

  <script src="portal.js" defer></script>
</body>
</html>
"""


def portal_config_json(bid: str, brand: str, slug: str) -> str:
    sites: list[dict[str, str]] = [
        {"label": "Japan Music Tourism", "url": "../index.html"},
        {"label": "AI TARNAR Voice School", "url": "../tarnar/"},
        {"label": "Izu Music Fund", "url": "../izu-fund/"},
    ]
    if bid == "17":
        sites.insert(1, {"label": "GMTJ OS", "url": "../gmtj-os/"})
    sites.extend(
        [
            {"label": "atono co., ltd.", "url": "https://atono.co.jp/"},
            {"label": "karaoke.ac", "url": "https://karaoke.ac/"},
        ]
    )
    cfg = {
        "lineAddFriendUrl": "",
        "contactEmail": "123@atono.jp",
        "mailtoSubject": f"GMTJ #{bid} {brand} ポータル（公式LINE）",
        "relatedSites": sites,
    }
    return json.dumps(cfg, ensure_ascii=False, indent=2) + "\n"


def main() -> None:
    portal_js = PORTAL_JS_SRC.read_text(encoding="utf-8")
    for b in BUSINESSES:
        bid, slug, brand, _p, *_rest = b
        d = SITE / slug
        (d / "data").mkdir(parents=True, exist_ok=True)
        (d / "index.html").write_text(build_index_html(b), encoding="utf-8")
        (d / "portal-config.json").write_text(portal_config_json(bid, brand, slug), encoding="utf-8")
        (d / "portal.js").write_text(portal_js, encoding="utf-8")
        (d / "data" / "blog-manifest.json").write_text(
            json.dumps({"articles": []}, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )

    print("Wrote", len(BUSINESSES), "portals under site/. (Redirects: edit netlify.toml manually.)")


if __name__ == "__main__":
    main()
