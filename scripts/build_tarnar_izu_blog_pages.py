#!/usr/bin/env python3
"""Generate static blog HTML for TARNAR (80×4 langs) and Izu Fund (24×4)."""
from __future__ import annotations

import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARNAR = ROOT / "site" / "tarnar"
IZU = ROOT / "site" / "izu-fund"
_SCRIPTS = Path(__file__).resolve().parent
if str(_SCRIPTS) not in __import__("sys").path:
    __import__("sys").path.insert(0, str(_SCRIPTS))
from tarnar_blog_seeds_extra import (
    EXTRA_EN_TITLES,
    EXTRA_JA_SEEDS,
    EXTRA_KO_TITLES,
    EXTRA_ZH_TITLES,
)

JA_SEEDS = [
    ("voice-guide-01", "朝の声を整える3分ルーティン", "朝は体温が低く声帯も硬めです。鼻から吸って口から吐く呼吸を10回、唇のブルブルを軽く、ハミングで小さな声域を滑らせます。無理に音量を出さず、一日の声の土台を作ることが目的です。"),
    ("voice-guide-02", "録音前にやるべきチェック5項目", "マイクの高さ、ポップガードの距離、部屋の反響、水分補給、そして心拍が落ち着くまでの短い沈黙。録音は演奏と違い、細部が残るので、事前の型を決めると失敗が減ります。"),
    ("voice-guide-03", "腹式呼吸を日常に取り込むコツ", "腹式呼吸は特別な姿勢だけでなく、歩きやデスクワークの合間にも応用できます。肋骨を広げすぎず、下腹部が自然に動くイメージで十分です。"),
    ("voice-guide-04", "高音が苦手な人の段階練習", "いきなり歌わず、唇震えから母音を狭くして半音ずつ上げる。喉の外筋が入らないよう、顎は軽く下げたまま小さな声で輪郭を取ります。"),
    ("voice-guide-05", "低音域のブレを抑えるリズム練習", "メトロノームに合わせ短い母音を刻むと、声帯の閉じ方が安定しやすいです。音量よりも拍の正確さを優先してください。"),
    ("voice-guide-06", "ライブ前日の声の休ませ方", "シャウトは控え、ストレッチと十分な睡眠を優先。アルコールは脱水につながるため控えめにし、温かい飲み物で粘膜を保護します。"),
    ("voice-guide-07", "カラオケ後のクールダウン手順", "高音を多用した後は、低めのハミングで戻し、首肩をほぐします。翌日の声枯れ予防になります。"),
    ("voice-guide-08", "マイクとの距離感を覚える練習", "15cmから30cmの範囲で同じフレーズを録り、波形を比較。自分の音量癖を把握すると現場でブレません。"),
    ("voice-guide-09", "声帯を痛めない話し方の切り替え", "長時間の説明は、間を増やし、語尾を落として息を補給。声量より明瞭さを優先すると負担が減ります。"),
    ("voice-guide-10", "鼻声と抜け声のバランスを整える", "鼻に抜けすぎる場合は口の開きと舌中央を意識。抜けない場合は軟口蓋の解放イメージを試します。"),
    ("voice-guide-11", "英語歌詞を歌うときの発音と母音", "英語の母音は口形が大きく変わります。歌詞を話す速度で読み、子音の位置を確認してからメロディに載せます。"),
    ("voice-guide-12", "韓国語歌詞のリズムに合わせるコツ", "子音連続は息の切れ目を設計。メトロノームより実音源に合わせた叩きが効果的です。"),
    ("voice-guide-13", "中国語の声調をメロディに乗せる練習", "声調と音高がぶつかる箇所は早めにマークし、小さな装飾音で逃がすか、母音を微調整します。"),
    ("voice-guide-14", "アンサンブルで音量を合わせる耳", "自分の音量を一段下げて聴くと他パートが聞こえます。合わせの練習は録音して客観視するのが近道です。"),
    ("voice-guide-15", "自宅練習の音量と近所への配慮", "防音は完璧でなくても、時間帯と窓の開閉、吸音の簡易パネルで配慮できます。夜はヘッドフォン＋マイクが現実的です。"),
    ("voice-guide-16", "声の疲れをセルフチェックする目安", "朝の低音が出にくい、話し始めに違和感、痛みがある場合は安静を優先。痛みは専門家へ相談してください。"),
    ("voice-guide-17", "発声前の首肩ストレッチ", "胸鎖乳突筋を優しくほぐし、肩甲骨を動かすと喉周りの緊張が抜けやすいです。回数より丁寧さを重視します。"),
    ("voice-guide-18", "舌の力みをほぐす母音練習", "「あいうえお」を舌先を下げ気味に。舌骨筋群の過緊張を避けるイメージです。"),
    ("voice-guide-19", "ステージ上の立ち位置と声の届き方", "モニターの角度、客席との距離に合わせて声の焦点を前後に移動。歩きながら歌う場合はマイク位置を先に決めます。"),
    ("voice-guide-20", "緊張をほぐす呼吸パターン4-7-8", "4秒吸い、7秒止め、8秒吐くを数回。過換気にならないよう浅めでも構いません。"),
    ("voice-guide-21", "イヤモニターの音量バランス", "クリックと自分の声の比率を固定。ライブ中に触りすぎないようプリセットを決めておきます。"),
    ("voice-guide-22", "リップトリルができないときの代替", "舌先を軽く上げた「だ」行の震えや、手で頬を支えると振動が伝わりやすいです。"),
    ("voice-guide-23", "歌詞暗記と音取りの順番", "メロディが体に入ってから歌詞を載せると、発声の癖が減ります。逆にやると母音が崩れがちです。"),
    ("voice-guide-24", "録音データのファイル命名規則", "日付_曲名_テイク番号で揃えると後から検索しやすいです。バックアップ先も決めておきます。"),
    ("voice-guide-25", "ボイトレで目標を言語化するワーク", "今月の課題を一文で書き、週末に録音で検証。数値化できる目標ほど継続しやすいです。"),
    ("voice-guide-26", "声域拡張のための半音ステップ練習", "無理な伸ばしではなく、今日はここまで、と上限を決めると安全です。翌日に回す勇気も大切です。"),
    ("voice-guide-27", "ビブラートのかけすぎを直す", "拍に乗せすぎないよう、まずはストレートで音程を安定。装飾は最後の仕上げに回します。"),
    ("voice-guide-28", "合唱でパート音を取りやすくする聴き方", "自分の声を少し抑え、左右のパートを交互に聴く。定位が分かると音取りが速くなります。"),
    ("voice-guide-29", "配信ライブの音圧と話し声の切替", "話すときはマイクを少し離し、歌うときに戻す。コンプ設定は事前に決めておきます。"),
    ("voice-guide-30", "年間の声のメンテナンスカレンダー", "繁忙期の前に軽い休声週間を入れる、年に一度の聴力チェックを入れるなど、予定に組み込むと実行率が上がります。"),
]
JA_SEEDS = JA_SEEDS + EXTRA_JA_SEEDS

EN_TITLES = [
    "A 3-minute morning routine for your voice",
    "Five checks before you hit record",
    "How to practice diaphragmatic breath in daily life",
    "Stepwise exercises if high notes feel tight",
    "Rhythm drills to steady your low register",
    "How to rest your voice the day before a show",
    "Cool-down after a long karaoke session",
    "Training mic distance with simple recordings",
    "Switching between speaking and singing safely",
    "Balancing nasality and openness",
    "Singing English lyrics: vowels and consonants",
    "Korean lyrics: pacing consonant clusters",
    "Mandarin tones and melody: practical tips",
    "Matching volume in small ensembles",
    "Considerate home practice volume",
    "Self-check signs of vocal fatigue",
    "Neck and shoulder stretches before phonation",
    "Vowel drills to relax tongue tension",
    "Stage position and projection basics",
    "A simple breathing pattern to ease nerves",
    "In-ear mix: clicks vs. your voice",
    "Alternatives if lip trills are difficult",
    "Learn melody first, then lyrics",
    "Naming recorded takes for easy search",
    "Writing a one-line monthly vocal goal",
    "Half-step routines for range work",
    "Keeping vibrato tasteful, not constant",
    "Hearing harmony parts faster in choir",
    "Switching tone between talk and song on stream",
    "A yearly maintenance calendar for vocal health",
]
EN_TITLES = EN_TITLES + EXTRA_EN_TITLES

KO_TITLES = [
    "아침 3분 보이스 루틴",
    "녹음 전 체크 5가지",
    "일상에 배압 호흡 넣기",
    "높은 음이 힘들 때 단계 연습",
    "저음 안정을 위한 리듬 연습",
    "공연 전날 목 쉬게 하기",
    "노래방 후 쿨다운",
    "마이크 거리 익히기",
    "말하기와 노래 전환",
    "비음과 개방감 밸런스",
    "영어 가사 발성",
    "한국어 가사 리듬",
    "중국어 성조와 멜로디",
    "소규모 합창 볼륨 맞추기",
    "가정 연습 배려",
    "피로 신호 체크",
    "목 어깨 스트레칭",
    "모음으로 혀 긴장 풀기",
    "무대 위치와 전달",
    "긴장 완화 호흡",
    "인이어 믹스",
    "립트릴 대안",
    "멜로디 후 가사",
    "파일 이름 규칙",
    "월간 목표 한 줄",
    "반음 스텝 연습",
    "비브라토 절제",
    "합창 파트 듣기",
    "방송 토크와 노래",
    "연간 보이스 캘린더",
]
KO_TITLES = KO_TITLES + EXTRA_KO_TITLES

ZH_TITLES = [
    "晨间3分钟开嗓流程",
    "录音前的五项检查",
    "把腹式呼吸带进日常",
    "高音吃力的分步练习",
    "稳住低音的节奏训练",
    "演出前一日如何护嗓",
    "唱K后的放松步骤",
    "练出稳定的麦克风距离",
    "说话与歌唱的安全切换",
    "鼻音与开放的平衡",
    "唱英文歌词的母音与辅音",
    "韩文歌词的节奏处理",
    "中文声调与旋律的配合",
    "小组合唱的音量对齐",
    "居家练习的音量与邻里",
    "嗓音疲劳的自测要点",
    "发声前的颈肩拉伸",
    "用母音放松舌头紧张",
    "站位与声音投射",
    "缓解紧张的呼吸节奏",
    "耳返里节拍与自己的比例",
    "唇颤困难时的替代练习",
    "先旋律后歌词的顺序",
    "录音文件命名习惯",
    "把月度目标写成一句话",
    "半音阶的安全拓展",
    "让颤音更克制自然",
    "合唱里更快找准声部",
    "直播里说话与演唱的切换",
    "年度嗓音维护日历",
]
ZH_TITLES = ZH_TITLES + EXTRA_ZH_TITLES


def paras_to_html(p: str) -> str:
    parts = [x.strip() for x in p.split("。") if x.strip()]
    out = []
    for part in parts:
        if not part.endswith("。"):
            part += "。"
        out.append(f"<p>{html.escape(part)}</p>")
    return "\n".join(out) if out else f"<p>{html.escape(p)}</p>"


def html_article(
    *,
    lang: str,
    slug: str,
    title: str,
    description: str,
    body_html: str,
    css_href: str,
    home_href: str,
    brand: str,
    alt_ja: str,
    alt_en: str,
    alt_ko: str,
    alt_zh: str,
) -> str:
    title_e = html.escape(title)
    brand_e = html.escape(brand)
    desc_e = html.escape(description)
    canon = alt_ja if lang == "ja" else alt_en if lang == "en" else alt_ko if lang == "ko" else alt_zh
    ld = json.dumps(
        {
            "@context": "https://schema.org",
            "@type": "Article",
            "headline": title,
            "description": description[:300],
            "inLanguage": lang,
            "author": {"@type": "Organization", "name": brand},
            "publisher": {"@type": "Organization", "name": "Japan Music Tourism"},
        },
        ensure_ascii=False,
    )
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{title_e} | {brand_e}</title>
  <meta name="description" content="{desc_e}" />
  <meta property="og:title" content="{title_e}" />
  <meta property="og:description" content="{desc_e}" />
  <meta name="twitter:card" content="summary_large_image" />
  <link rel="canonical" href="{html.escape(canon)}" />
  <link rel="stylesheet" href="{html.escape(css_href)}" />
  <link rel="alternate" hreflang="ja" href="{html.escape(alt_ja)}" />
  <link rel="alternate" hreflang="en" href="{html.escape(alt_en)}" />
  <link rel="alternate" hreflang="ko" href="{html.escape(alt_ko)}" />
  <link rel="alternate" hreflang="zh-Hans" href="{html.escape(alt_zh)}" />
  <script type="application/ld+json">{ld}</script>
</head>
<body>
  <header class="nav">
    <a class="nav-brand" href="{html.escape(home_href)}">{brand_e}</a>
    <nav class="nav-links" aria-label="nav">
      <a href="{html.escape(home_href)}#blog">一覧</a>
      <a href="{html.escape(home_href)}">ホーム</a>
    </nav>
  </header>
  <main class="wrap article-page">
    <article class="article-shell">
      <p class="article-kicker">{brand_e}</p>
      <h1 class="article-title">{title_e}</h1>
      <div class="blog-meta article-meta">
        <a class="lang-chip" href="{html.escape(alt_ja)}">JA</a>
        <a class="lang-chip" href="{html.escape(alt_en)}">EN</a>
        <a class="lang-chip" href="{html.escape(alt_ko)}">KO</a>
        <a class="lang-chip" href="{html.escape(alt_zh)}">ZH</a>
      </div>
      <div class="article-body article-prose">{body_html}</div>
    </article>
  </main>
  <footer class="site-footer">
    <p><a href="{html.escape(home_href)}">← {brand_e}</a></p>
  </footer>
</body>
</html>
"""


def build_tarnar() -> list[dict]:
    manifest: list[dict] = []
    css = "../../portal.css"
    home = "../../index.html"
    brand = "AI TARNAR Voice School"
    for i, (slug, ja_title, ja_body) in enumerate(JA_SEEDS):
        en_t = EN_TITLES[i]
        ko_t = KO_TITLES[i]
        zh_t = ZH_TITLES[i]
        if i < 30:
            en_body = ja_body.replace("。", ". ")
            ko_body = ja_body
            zh_body = ja_body
        else:
            en_body = (
                f"This guide is part of AI TARNAR Voice School (Japan Music Tourism). Topic: {en_t}. "
                "Start quietly, build the phrase across several days, and record short takes for self-review. "
                "Stop if you feel pain or strain and seek professional advice."
            )
            ko_body = (
                f"{ko_t} — AI TARNAR Voice School 실습 가이드입니다. "
                "작은 소리로 형태를 확인하고 며칠에 걸쳐 부하를 올리며 짧게 녹음해 점검하세요. "
                "통증이 있으면 중단하고 전문가 상담을 우선합니다."
            )
            zh_body = (
                f"{zh_t}——AI TARNAR Voice School 练习导读。"
                "先用较小音量建立动作，再分几天逐步增加强度，并录音自查。"
                "若出现疼痛或明显不适，请停止并咨询专业人士。"
            )
        ja_html = paras_to_html(ja_body)
        en_html = paras_to_html(en_body)
        ko_html = paras_to_html(ko_body)
        zh_html = paras_to_html(zh_body)
        alt_ja = f"../ja/{slug}.html"
        alt_en = f"../en/{slug}.html"
        alt_ko = f"../ko/{slug}.html"
        alt_zh = f"../zh/{slug}.html"
        desc_ja = (ja_title + "。" + ja_body[:100]).replace('"', "'")[:158]
        desc_en = (en_t + ". " + en_body[:90]).replace('"', "'")[:158]
        desc_ko = (ko_t + ". " + ko_body[:80]).replace('"', "'")[:158]
        desc_zh = (zh_t + "。" + zh_body[:80]).replace('"', "'")[:158]
        for lang, title, body, desc in (
            ("ja", ja_title, ja_html, desc_ja),
            ("en", en_t, en_html, desc_en),
            ("ko", ko_t, ko_html, desc_ko),
            ("zh-Hans", zh_t, zh_html, desc_zh),
        ):
            sub = "ja" if lang == "ja" else "en" if lang == "en" else "ko" if lang == "ko" else "zh"
            out_dir = TARNAR / "blog" / sub
            out_dir.mkdir(parents=True, exist_ok=True)
            fp = out_dir / f"{slug}.html"
            fp.write_text(
                html_article(
                    lang=lang,
                    slug=slug,
                    title=title,
                    description=desc,
                    body_html=body,
                    css_href=css,
                    home_href=home,
                    brand=brand,
                    alt_ja=alt_ja,
                    alt_en=alt_en,
                    alt_ko=alt_ko,
                    alt_zh=alt_zh,
                ),
                encoding="utf-8",
            )
        manifest.append(
            {
                "slug": slug,
                "status": "published",
                "titles": {"ja": ja_title, "en": en_t, "ko": ko_t, "zh": zh_t},
                "urls": {
                    "ja": f"blog/ja/{slug}.html",
                    "en": f"blog/en/{slug}.html",
                    "ko": f"blog/ko/{slug}.html",
                    "zh": f"blog/zh/{slug}.html",
                },
            }
        )
    return manifest


IZU_JA = [
    ("izu-01", "伊豆の音楽と旅をつなぐ考え方", "地域の音楽資源と観光導線を一つのストーリーにまとめると、滞在の動機が明確になります。単発イベントではなく、季節と連動した体験設計が鍵です。"),
    ("izu-02", "アーティスト支援と地域プログラムの両立", "出演料と地域還元のバランスは、事前に透明性のある枠組みを示すと信頼が得られます。スポンサー表記も統一します。"),
    ("izu-03", "音楽ツーリズムの安全とマナー", "移動・会場・撮影について、公式情報を起点に案内を揃えます。不確実な慣習は断定しません。"),
    ("izu-04", "滞在型プログラムの設計メモ", "宿泊日数と移動負荷を先に決め、音楽体験の密度を調整します。高齢ゲストにも読みやすい行程表にします。"),
    ("izu-05", "パートナー募集で伝えるべき3点", "目的、期間、期待する協力内容を短文で。審査基準がある場合は最初に明示します。"),
    ("izu-06", "レポートに載せる指標の選び方", "公開できる範囲の数値と定性の声をセットにします。個人が特定される表現は避けます。"),
    ("izu-07", "多言語ゲストへの案内の型", "日英を基本に、必要に応じて中国語・韓国語の要点を添えます。専門用語は脚注で補足します。"),
    ("izu-08", "クラウドファンディング連携の設計ポイント", "リターン内容は履行可能な範囲で設計し、変更可能性がある場合は規約に明記します。"),
    ("izu-09", "地域の音楽施設との連携チェック", "営業情報は公式サイトを参照し、推測で時刻や料金を書きません。"),
    ("izu-10", "イベント後のフォローアップ", "アンケートは任意・匿名を原則にし、次回案内はオプトインで送ります。"),
    ("izu-11", "伊豆エリアの移動ハブ整理", "主要駅と周辺の接続を地図とセットで示し、天候による代替ルートも一言添えます。"),
    ("izu-12", "音楽と地域ブランドのメッセージ統一", "ハッシュタグとロゴ利用ルールを一枚にまとめ、パートナーと共有します。"),
    ("izu-13", "地域スポンサー表記のガイドライン", "ロゴサイズ、クレジット順、禁止パターンを先に定義します。更新時は版数を上げ、過去資料との差分を残します。"),
    ("izu-14", "音楽体験と宿泊パッケージの組み方", "移動負荷と体験時間のバランスを先に決め、オプションは後付け可能な形にします。キャンセル条件も明文化します。"),
    ("izu-15", "投資家向けレターのトーンと禁則", "確約表現を避け、リスク要因を箇条書きで併記します。個人情報や未公開案件は記載しません。"),
    ("izu-16", "アーティストデイと地域学校の連携", "学校側の規程に沿った写真・SNS掲載ルールを確認し、同意取得のフローを用意します。"),
    ("izu-17", "防災・避難計画とイベント運営", "屋外イベントでは気象情報の参照元と中止基準を事前に共有します。避難経路は図示します。"),
    ("izu-18", "著作権とセットリストの取り扱い", "原盤・著作隣接権の範囲を整理し、配信やアーカイブの可否を契約に反映します。"),
    ("izu-19", "地域交通とラストトレイン案内", "公式の終電・バス時刻を引用し、代替タクシー情報は参考程度に留めます。"),
    ("izu-20", "ボランティア募集と保険の確認", "活動内容に応じた保険範囲を確認し、未成年参加の可否と保護者同意を明記します。"),
    ("izu-21", "地域飲食店とのコラボ条件", "提供メニュー、提供時間、在庫リスクを事前に合意し、トラブル時の連絡先を一本化します。"),
    ("izu-22", "観光協会・DMOとの情報整合", "公式観光サイトの更新日を記録し、引用時はURLと取得日を残します。"),
    ("izu-23", "サステナビリティ観点の音楽イベント", "廃棄物、電力、輸送の各項目で改善余地を洗い出し、次回に反映できる形で記録します。"),
    ("izu-24", "次年度に向けたナレッジの棚卸し", "成功要因と失敗要因を分けて記録し、再現可能な手順だけをテンプレ化します。"),
]

IZU_EN = [
    "Connecting music and travel in Izu",
    "Artist support and local programs",
    "Safety and etiquette for music tourism",
    "Designing stay-based programs",
    "Three points for partner outreach",
    "Choosing metrics for public reports",
    "Templates for multilingual guests",
    "Crowdfunding collaboration design",
    "Checklist for venue partnerships",
    "Post-event follow-up",
    "Mobility hubs around Izu",
    "Unifying regional brand messages",
    "Guidelines for local sponsor credits",
    "Bundling music experiences with stays",
    "Tone and guardrails for investor letters",
    "Artist days and school partnerships",
    "Disaster planning for outdoor events",
    "Setlists and copyright handling",
    "Last-train guidance and mobility",
    "Volunteers and insurance checks",
    "Collaboration terms with local restaurants",
    "Aligning with tourism associations / DMOs",
    "Sustainability notes for music events",
    "Year-end knowledge cleanup for the next season",
]

IZU_KO_TITLES = [
    "이즈의 음악과 여행을 잇는 사고방식",
    "아티스트 지원과 지역 프로그램의 양립",
    "뮤직 투어리즘의 안전과 매너",
    "체류형 프로그램 설계 메모",
    "파트너 모집에서 전할 세 가지",
    "보고서에 실을 지표 고르기",
    "다국어 게스트 안내 템플릿",
    "크라우드펀딩 연계 설계 포인트",
    "지역 음악 시설과의 협업 체크",
    "이벤트 후속 조치",
    "이즈 지역 이동 허브 정리",
    "음악과 지역 브랜드 메시지 통일",
    "지역 스폰서 표기 가이드라인",
    "음악 체험과 숙박 패키지 구성",
    "투자자용 레터 톤과 금지 표현",
    "아티스트 데이와 지역 학교 연계",
    "방재·대피 계획과 이벤트 운영",
    "저작권과 셋리스트 취급",
    "지역 교통과 막차 안내",
    "자원봉사 모집과 보험 확인",
    "지역 음식점과의 콜라보 조건",
    "관광협회·DMO와의 정보 정합",
    "서스테이너빌리티 관점의 음악 이벤트",
    "차기 연도를 위한 지식 정리",
]

IZU_ZH_TITLES = [
    "伊豆连接音乐与旅行的思路",
    "艺人支援与地域项目并行",
    "音乐旅游的安全与礼仪",
    "停留型项目设计备忘",
    "伙伴招募应说明的三点",
    "公开报告指标的选择",
    "多语言客人指引模板",
    "众筹联动设计要点",
    "与地域音乐设施协作清单",
    "活动后跟进",
    "伊豆区域交通节点整理",
    "音乐与地域品牌信息统一",
    "地域赞助露出规范",
    "音乐体验与住宿打包",
    "致投资人信函的语气与禁区",
    "艺人日与学校合作",
    "防灾疏散与活动运营",
    "版权与歌单处理",
    "末班车与交通指引",
    "志愿者招募与保险核对",
    "与本地餐饮合作条件",
    "与观光协会/DMO信息对齐",
    "音乐活动的可持续要点",
    "面向下一年度的知识盘点",
]


def build_izu() -> list[dict]:
    manifest: list[dict] = []
    css = "../../portal.css"
    home = "../../index.html"
    brand = "Izu Music Fund"
    for i, (slug, ja_title, ja_body) in enumerate(IZU_JA):
        en_t = IZU_EN[i]
        ko_t = IZU_KO_TITLES[i]
        zh_t = IZU_ZH_TITLES[i]
        ja_html = paras_to_html(ja_body)
        en_html = paras_to_html(ja_body.replace("。", ". "))
        ko_body = (
            f"{ko_t}。Izu Music Fund 실무 가이드입니다。"
            "공식 정보를 우선하고 수치는 출처를 명시합니다。"
            "Japan Music Tourism의 음악 관광 맥락에서 지역 이벤트와 숙박 동선을 함께 고려합니다。"
        )
        zh_body = (
            f"{zh_t}。Izu Music Fund 实务导读。"
            "请以日本官方渠道核对时间与费用，避免臆测。"
            "在 Japan Music Tourism 的音乐旅游框架下，将演出、移动与住宿一并设计。"
        )
        ko_html = paras_to_html(ko_body)
        zh_html = paras_to_html(zh_body)
        alt_ja = f"../ja/{slug}.html"
        alt_en = f"../en/{slug}.html"
        alt_ko = f"../ko/{slug}.html"
        alt_zh = f"../zh/{slug}.html"
        desc_ja = (ja_title + "。" + ja_body[:100])[:158]
        for lang, title, body, desc in (
            ("ja", ja_title, ja_html, desc_ja),
            ("en", en_t, en_html, (en_t + ".")[:158]),
            ("ko", ko_t, ko_html, (ko_t + ".")[:158]),
            ("zh-Hans", zh_t, zh_html, (zh_t + "。")[:158]),
        ):
            sub = "ja" if lang == "ja" else "en" if lang == "en" else "ko" if lang == "ko" else "zh"
            out_dir = IZU / "blog" / sub
            out_dir.mkdir(parents=True, exist_ok=True)
            fp = out_dir / f"{slug}.html"
            fp.write_text(
                html_article(
                    lang=lang,
                    slug=slug,
                    title=title,
                    description=desc.replace('"', "'"),
                    body_html=body,
                    css_href=css,
                    home_href=home,
                    brand=brand,
                    alt_ja=alt_ja,
                    alt_en=alt_en,
                    alt_ko=alt_ko,
                    alt_zh=alt_zh,
                ),
                encoding="utf-8",
            )
        manifest.append(
            {
                "slug": slug,
                "status": "published",
                "titles": {"ja": ja_title, "en": en_t, "ko": ko_t, "zh": zh_t},
                "urls": {
                    "ja": f"blog/ja/{slug}.html",
                    "en": f"blog/en/{slug}.html",
                    "ko": f"blog/ko/{slug}.html",
                    "zh": f"blog/zh/{slug}.html",
                },
            }
        )
    return manifest


def main() -> None:
    TARNAR.mkdir(parents=True, exist_ok=True)
    (TARNAR / "data").mkdir(parents=True, exist_ok=True)
    IZU.mkdir(parents=True, exist_ok=True)
    (IZU / "data").mkdir(parents=True, exist_ok=True)
    m1 = build_tarnar()
    (TARNAR / "data" / "blog-manifest.json").write_text(
        json.dumps({"articles": m1}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    m2 = build_izu()
    (IZU / "data" / "blog-manifest.json").write_text(
        json.dumps({"articles": m2}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print("Wrote", len(m1), "TARNAR article sets and", len(m2), "Izu sets.")


if __name__ == "__main__":
    main()
