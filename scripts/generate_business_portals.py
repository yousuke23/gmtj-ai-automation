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
        "伊豆山開運ツアー2026｜837段・二社詣+1・6センスボイス。土日祝120日・公式LINE。イベントサービス情報とお得情報で関係人口拡大。Japan Music Tourism #01。",
        "伊豆山開運ツアー2026",
        "伊豆山開運ツアー2026",
        "Global Music Tour",
        "伊豆山開運ツアー2026（詳細は本ページ本文にてご確認ください）。",
        ("Route", "ルートと時間割", "移動負荷と体験密度のバランスを先に決め、雨天・混雑時の代替も一言で示せる型にします。"),
        ("Safety", "安全とマナー", "公式情報を起点に、撮影・会場・移動の注意を短く反復できるチェックリストに落とします。"),
        ("Guide", "多言語ゲスト", "英語を軸に、必要に応じて中国語・韓国語の要点を添えた案内の骨子を用意します。"),
        "",
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
        "不動産・まちづくりのストーリーを、音楽ツーリズムの導線と同じ粒度で設計します。投資家説明・自治体資料・ゲスト向け概要を一枚に揃え、宿泊・ツアー・ファンドへ自然に遷移させます。",
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
        "泊まる時間そのものを、ライブ・食事・景色と同じ価値として設計します。AI TARNAR Voice School のレッスンや録物体験と前後させても破綻しない日程表に落とし込み、移動負荷も先に決めます。",
        ("Stay", "滞在プログラム", "泊数と体験密度を調整し、高齢ゲストにも読みやすい行程表にします。"),
        ("Voice", "声の学び", "AI TARNAR Voice School と接続し、旅前後のレッスン導線を設計できます。"),
        ("Region", "地域と還流", "Izu Music Fund など地域ファンドとも自然につながる案内を整えます。"),
        "",
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
        "店内の音量曲線・撮影可否・子ども同伴の案内を、ピーク時も破綻しない短文セットにします。SNS告知と公式LINE、当日アナウンスの表記を揃え、フェス・ツアー導線とも接続します。",
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
        "動員のピークも、初参加のゲストも置いていかない歓迎の空気をつくることがコンセプトです。チケットから退場後まで、SNS・現場アナウンス・公式LINEを同じ語彙でつなぎ、トラブル時の一言メッセージまでテンプレ化します。",
        ("Crowd", "動員と導線", "混雑ピークと移動ハブを先に定義し、看板とプッシュ通知の文言を揃えます。"),
        ("Safety", "安全コミュニケーション", "熱中症・雨天・緊急時の定型文を短く分かりやすくします。"),
        ("Global", "多言語ゲスト", "英語を軸に、必要に応じて中国語・韓国語の要点を添えます。"),
        "",
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
        "アイデアの熱量を、納品とクレジットまで途切れさせない設計がコンセプトです。デモ評価からセッション、権利表記までを一枚のチェックリストにし、関係者全員が同じゴールを見られるようにします。",
        ("Session", "セッション設計", "楽器編成・録音環境・納品形式を先に固定し、手戻りを抑えます。"),
        ("Rights", "権利と表記", "クレジット・サンプル利用・二次利用の境界を短文で共有します。"),
        ("Studio", "スタジオ連携", "Voice & Music Studio など現場オペとつなぐ導線を用意します。"),
        "",
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
        "ワークショップ・定期演奏・ボランティアの参加導線を、継続率と安全の両立で設計します。世代横断の読みやすさと、地域コンシェルジュ・宿泊プランとの整合を同時に満たします。",
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
        "初回来店から長尺セッションまで、ブッキング・機材説明・アナログ/デジタル取り扱い・制作案件の引き継ぎを短文で揃え、現場とオンラインの案内表記を分岐させます。AI TARNAR Voice School や Music Production First との距離感も一枚で示せます。",
        ("Booking", "予約と窓口", "公開できる料金レンジとキャンセル方針を先に示し、問い合わせメールの件名テンプレまで用意します。"),
        ("Gear", "機材と声学", "マイク特性・モニター配置・レベル設定をゲスト向けに平易化し、自宅録音との差分を一文で説明します。"),
        ("Pipeline", "制作連携", "デモ受け渡し・ステム書き出し・クレジット表記を運用しやすくします。"),
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
        "プレゼン・客服・対外説明の型を整え、部門横断で使える短いスクリプトに落とします。録画レビューとOK/NG例をセットにし、コンプライアンス境界と人間エスカレーションの分岐もテンプレ化します。",
        ("Training", "研修設計", "職種別に演習・ロールプレイ・フィードバック時間を固定し、週次で反復できるカリキュラムにします。"),
        ("Script", "スクリプト", "FAQ・謝罪・クレーム初動・エスカレーションの境界を一文ずつ明文化し、多言語要点を添えます。"),
        ("Scale", "展開", "多拠点・ハイブリッド開催・録画配信の運用ルールと品質チェックリストを用意します。"),
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
        "カリキュラム公開範囲、試験申込、修了後の称号・ロゴ利用権を一枚に整理し、運営負荷と問い合わせ件数を同時に下げます。再受験・更新講習の導線も先に決めておきます。",
        ("Curriculum", "カリキュラム", "モジュール単位で公開・非公開を切り分け、前提知識と到達目標を各章に明記します。"),
        ("Exam", "試験運営", "不正防止・アクセシビリティ・多言語配慮を両立する運営手順のたたき台を用意します。"),
        ("Brand", "ブランド統一", "ロゴ・称号・名刺表記・SNS自己紹介文まで揃えたガイドラインを短くまとめます。"),
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
        "リターン履行可能範囲を先に定義し、更新頻度とトーンを統一したコミュニケーションにします。リスク表記・遅延時の定型文・サポーターFAQ まで含め、炎上しにくい骨子を用意します。",
        ("Plan", "企画構成", "ストーリー・目標金額・マイルストーン・スケジュールの骨子を一枚に整えます。"),
        ("Return", "リターン", "配送・デジタル特典・イベント招待・クレジットの境界と税・個人情報の注意を明確にします。"),
        ("Update", "更新運用", "週次/達成時/遅延時のサポーター向けメッセージ型とSNS短文化テンプレを揃えます。"),
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
        "初回コンタクトから契約前までのFAQと、社内稟議用の短文サマリを用意します。NDA前に共有できるデモ範囲と、権利クリアのチェック項目を先に固定します。",
        ("Contact", "窓口設計", "タイムゾーン・言語・返信SLAを考慮した一次返信とエスカレーション経路を定義します。"),
        ("Deal", "案件整理", "スコープ・権利・納期・テリトリー・収益配分のたたき台を共有します。"),
        ("Brand", "ブランド整合", "グループ横断の表記ルールと共同クレジットの書式を一枚にまとめます。"),
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
        "意図分類・エスカレーション・多言語テンプレを整備し、公式情報に根ざした応答方針を一枚にまとめます。医療・法律・投資判断は人間へ渡す境界を先に固定し、神社・宗教施設の敬意ある案内もテンプレ化します。",
        ("Intent", "意図分類", "予約・交通・安全・イベント・障害情報などの境界を定義し、曖昧な質問の聞き返し型も用意します。"),
        ("Escalation", "エスカレーション", "人間に渡す条件・連絡先・所要時間の目安をゲスト向けに平易に示します。"),
        ("KB", "ナレッジ", "公開してよい案内の骨子と更新の流れを、運用チームと共有できる形にします。"),
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
        "要件整理・締切・必要書類のチェックリストを短くまとめ、法務確認ポイントを添えます。採択後の実績報告スケジュールまで含め、途中で破綻しない運用表にします。",
        ("Scan", "要件整理", "対象事業・上限・重複申請・間接経費の注意を一覧化し、落とし穴を短文で示します。"),
        ("Doc", "書類たたき台", "計画書の章立てとKPIの書き方を固定し、稟議用サマリを自動生成しやすくします。"),
        ("Review", "レビュー", "最終判断は専門家（税理士・助成金コンサル等）への委任と、AIが断定しない領域を明示します。"),
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
        "NDA前に共有できる範囲のサマリと、機密区分のたたき台を用意します。楽曲カタログ・ライブ事業・サブスク収益の切り分けを先に行い、買い手の質問リストを想定したFAQも添えます。",
        ("Teaser", "ティーザー", "売却側の強み・差別化・成長ストーリーを一文ずつ整理し、数字の出し方を統一します。"),
        ("Data", "データルーム", "楽曲権利・契約・KPI・人事情報の棚卸し項目とアクセス権限の型を列挙します。"),
        ("Process", "プロセス", "デューデリジェンスの段取りと、クロージング後のブランド統合コミュニケーションを共有します。"),
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
        "進捗・自動化・重点事業の可視化を GMTJ OS でまとめ、各ポータルへ戻る導線を一本化します。日次チェック項目とアラート閾値のたたき台を用意し、現場の問い合わせを減らす運用設計にします。",
        ("Dash", "ダッシュボード", "今日の実行結果・失敗ジョブ・重点カードを上段に固定し、深掘りは事業別ビューへ遷移させます。"),
        ("Workflow", "ワークフロー", "事業別の登録・承認・公開フローを追跡し、ボトルネックを短文で可視化します。"),
        ("Link", "各事業ポータル", "現場の窓口へすぐ戻れるリンク集と、関連外部サイトの相互導線を維持します。"),
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
        "コンテンツ柱・カレンダー・キーワードを整理し、キャンペーン単位で表記ゆれを抑えます。ブログや記事を公開したあと、各SNSと公式LINEでどう届けるかの役割分担も決めておきます。",
        ("Pillar", "コンテンツ柱", "エリア・季節・事業の軸を固定し、再利用できる短尺・長文の型を揃えます。"),
        ("Channel", "チャネル", "TikTok/Instagram/YouTube/X/Facebook のトーン差と投稿頻度のたたき台を用意します。"),
        ("Measure", "振り返り", "問い合わせや予約につながるリンクの付け方と名称をそろえ、定例レビュー会の型を添えます。"),
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
        "海外から日本の音楽旅へ踏み出す瞬間に、案内の温度差が出ないよう整えます。到着前後の安全・マナー・撮影の注意を多言語で揃え、ツアー・フェス・滞在・AI TARNAR Voice School まで同じ歓迎のトーンでつなぎます。",
        ("Story", "ストーリー", "地域と音楽の魅力を一続きの物語にし、季節・フェス・滞在プランを同じ語彙で語ります。"),
        ("Safety", "安全", "移動・会場・撮影・熱中症の注意を反復しやすい短文にし、緊急時の連絡先表記を統一します。"),
        ("Stay", "滞在接続", "宿泊・リゾート・ファンド・AI TARNAR Voice School まで、同じ歓迎のトーンでつなぐクロスセルを設計します。"),
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
        "カリキュラム公開範囲、言語別導線、修了証明の表記を整理し、現場運用に耐える型にします。オンライン/対面ハイブリッドの時間割と、保護者向けFAQ も同時に整えます。",
        ("Course", "コース設計", "入門から専門までの段階と前提スキルを定義し、評価ルーブリックを短文化します。"),
        ("Lang", "多言語", "教材・サポート窓口・問い合わせ自動返信の言語方針を揃えます。"),
        ("Hub", "ハブ機能", "パートナー教育機関・認定プログラム・スタジオ実習への接続導線を用意します。"),
        "",
    ),
]


DEFAULT_SERVICES_LEAD = "企画・導線・運用を短い型に落とし、現場でそのまま使えるコミュニケーションに整えます。"

SERVICES_SECTION_LEAD: dict[str, str] = {
    "01": "伊豆山開運ツアー2026では、3プログラムを土日祝に年間120日体制で設計し、アンケートと公式LINEで関係人口を積み上げます。",
    "02": "土地と建物のストーリーを、宿泊・ツアー・ファンドへ自然に渡せる導線にします。",
    "03": "泊数と体験の濃さのバランスを先に決め、どの日も同じ歓迎のトーンで案内できるようにします。",
    "04": "ピーク時も安心感が崩れないよう、店内案内とSNS・公式LINEの表記を揃えます。",
    "05": "大人数でも「初めての方が迷わない」動線とアナウンスを優先します。",
    "06": "手戻りを減らすため、セッション前に決めるべき項目を短いチェックリストにします。",
    "07": "初参加からリピーターまで、継続しやすい難易度と案内の温度感を設計します。",
    "09": "初回来店から長時間セッションまで、案内と機材説明を同じ粒度で揃えます。",
    "10": "対外説明と社内共有で、同じ声のトーンが使えるよう短文セットにします。",
    "11": "学びの信頼を、称号・ロゴ・修了後の案内まで一続きにします。",
    "12": "支援者との約束が履行しやすい形で、更新メッセージのトーンも固定します。",
    "13": "海外パートナーとの初回やり取りから、社内稟議用の短文までを用意します。",
    "14": "公式情報を起点に、人間へ渡す境界もゲストに分かりやすく示します。",
    "15": "制度の要点を短く整理し、社内で判断しやすいチェックリストにします。",
    "16": "共有できる範囲の魅力と、機密の切り分けを最初に明確にします。",
    "17": "21事業の窓口へすぐ戻れる導線と、運用の見える化を同時に満たします。",
    "18": "発信の役割分担を決め、問い合わせや予約へ自然につながる導線にします。",
    "19": "到着前から滞在先まで、多言語でも歓迎の空気が変わらない案内にします。",
    "20": "学びの入口を広げつつ、修了や次の一歩も迷わない案内にします。",
}

FOURTH_SERVICE_CARD: dict[str, tuple[str, str, str]] = {
    "01": ("Memory", "思い出の時間配分", "移動だけが主役にならないよう、演奏・食事・景色の余白まで行程に組み込みます。"),
    "02": ("Deck", "一枚の概要", "投資家・自治体・一般ゲストで語りを変えすぎず、宿泊・ツアーへ同じ歓迎でつなげます。"),
    "03": ("Comfort", "からだへの配慮", "歩行距離・段差・湿度まで踏まえた案内文案で、滞在全体の満足度を高めます。"),
    "04": ("Season", "季節とイベント", "季節のメニューと音楽の組み合わせを短文カレンダー化し、告知と店内案内を揃えます。"),
    "05": ("Welcome", "初参加の歓迎", "初めての方にも読みやすいアナウンスと、混雑ピーク時の一言案内をそろえます。"),
    "06": ("Delivery", "納品イメージの共有", "マスター形式・クレジット・修正の期待値を最初にそろえ、認識のズレを防ぎます。"),
    "07": ("Volunteer", "ボランティア導線", "初日オリエンと役割を短文で示し、続けたくなる歓迎の温度感にします。"),
    "09": ("Lesson", "レッスン体験の流れ", "初回からの歓迎と AI TARNAR Voice School とのつながりを一枚で示します。"),
    "10": ("CX", "お客様応答の型", "クレーム初動とお詫びの温度感を統一し、再発防止のメモまで用意します。"),
    "11": ("Alumni", "修了後の歩み", "修了者コミュニティと次の学びへの導線を明るく示します。"),
    "12": ("Trust", "支援者との信頼", "更新の頻度と文面のトーンを先に約束し、安心して待てる関係をつくります。"),
    "13": ("Timezone", "時差と窓口", "返信にかかる時間の目安を示し、海外相手にも誠実さが伝わる導線にします。"),
    "14": ("Guest", "ゲストの安心", "分からないときに送る一言の例を添え、人間へつなぐ流れを平易にします。"),
    "15": ("Deadline", "締切前の運び", "提出物のチェック順を固定し、最終週の取りこぼしを減らします。"),
    "16": ("Narrative", "物語の芯", "数字だけに偏らないよう、差別化の一文を先に据えます。"),
    "17": ("Pulse", "今日の気配", "重点事業の変化が一目でわかる見出し案を添えます。"),
    "18": ("Rhythm", "発信のリズム", "週次・イベント単位で何を出すかを見える化し、続けやすい運用表にします。"),
    "19": ("Arrival", "到着直後の安心", "空港・駅から会場までを同じトーンで案内し、英語を軸に要点を添えます。"),
    "20": ("Family", "保護者・同伴者", "保護者向けの安心文と、同伴者が楽しめる案内を短く添えます。"),
}

RELATED_PORTALS: dict[str, list[tuple[str, str, str]]] = {
    "01": [
        ("Japan Inbound Music Tourism #19", "../19-japan-inbound-music-tourism/", "インバウンド全体の入口とあわせてご案内できます。"),
        ("Global Music Festival #05", "../05-global-music-festival/", "フェス来場と周遊をつなぎます。"),
    ],
    "02": [
        ("123 MUSIC & RESORTS #03", "../03-123-music-resorts/", "滞在と音楽体験を組み合わせた提案ができます。"),
        ("Global Music Tour #01", "../01-global-music-tour/", "来街後のツアー動線へつなげます。"),
    ],
    "03": [
        ("Global Music Tour #01", "../01-global-music-tour/", "周遊と滞在をセットで設計できます。"),
        ("Japan Inbound Music Tourism #19", "../19-japan-inbound-music-tourism/", "海外ゲスト向けの統合案内と整合します。"),
    ],
    "04": [
        ("Global Music Festival #05", "../05-global-music-festival/", "フェス前後の立ち寄り導線を整えられます。"),
        ("Global Music Tour #01", "../01-global-music-tour/", "ツアー客の二次来店につなげられます。"),
    ],
    "05": [
        ("Global Music Tour #01", "../01-global-music-tour/", "周遊ツアーとフェス日程を組み合わせられます。"),
        ("Japan Inbound Music Tourism #19", "../19-japan-inbound-music-tourism/", "海外からの来場者案内と揃えられます。"),
    ],
    "06": [
        ("Voice & Music Studio #09", "../09-voice-music-studio/", "収録・レッスン現場とスムーズにつなぎます。"),
        ("123 MUSIC & RESORTS #03", "../03-123-music-resorts/", "滞在型の制作合宿プランにも展開できます。"),
    ],
    "07": [
        ("Regional Music Alliance #14", "../14-regional-music-alliance/", "地域案内・コンシェルジュと声を揃えられます。"),
        ("Japan Inbound Music Tourism #19", "../19-japan-inbound-music-tourism/", "海外参加者の案内とも整合できます。"),
    ],
    "09": [
        ("Music Production First #06", "../06-music-production-first/", "制作案件の受け渡しと揃えられます。"),
        ("123 MUSIC & RESORTS #03", "../03-123-music-resorts/", "滞在中のレッスン・収録プランに展開できます。"),
    ],
    "10": [
        ("Global Digital Marketing #18", "../18-global-digital-marketing/", "対外公開と社内向けトーンの役割分担に使えます。"),
        ("Music Cafe & Bar #04", "../04-music-cafe-bar/", "接客現場の短文事例ともつなげられます。"),
    ],
    "11": [
        ("Global Music Education Hub #20", "../20-global-music-education-hub/", "教育ハブ・国際連携の導線と揃えられます。"),
        ("Voice & Music Studio #09", "../09-voice-music-studio/", "実技・認定試験の現場導線に展開できます。"),
    ],
    "12": [
        ("Music Production First #06", "../06-music-production-first/", "リリース・制作ストーリーと一続きにできます。"),
        ("Global Digital Marketing #18", "../18-global-digital-marketing/", "更新告知とキャンペーン運用に接続できます。"),
    ],
    "13": [
        ("Music Production First #06", "../06-music-production-first/", "共同制作・ライセンス案件とつなげられます。"),
        ("Japan Inbound Music Tourism #19", "../19-japan-inbound-music-tourism/", "海外向けプロモと整合できます。"),
    ],
    "14": [
        ("Global Music Tour #01", "../01-global-music-tour/", "ツアー現場のFAQとも揃えられます。"),
        ("Japan Inbound Music Tourism #19", "../19-japan-inbound-music-tourism/", "インバウンド案内の中心軸と接続できます。"),
    ],
    "15": [
        ("Real Estate & Revitalization #02", "../02-real-estate-revitalization/", "地域プロジェクトの説明資料とも連動できます。"),
        ("Global Digital Marketing #18", "../18-global-digital-marketing/", "公募・締切の告知運用に使えます。"),
    ],
    "16": [
        ("Crowdfunding AI Producer #12", "../12-crowdfunding-ai-producer/", "資金調達ストーリーと案件整理を接続できます。"),
        ("Real Estate & Revitalization #02", "../02-real-estate-revitalization/", "不動産・事業売却の文脈にも展開できます。"),
    ],
    "17": [
        ("Global Digital Marketing #18", "../18-global-digital-marketing/", "発信と計測のダッシュボード化に使えます。"),
        ("Global Music Tour #01", "../01-global-music-tour/", "現場ツアー窓口へすぐ戻れます。"),
    ],
    "18": [
        ("Japan Inbound Music Tourism #19", "../19-japan-inbound-music-tourism/", "多言語プロモと導線を揃えられます。"),
        ("Music Cafe & Bar #04", "../04-music-cafe-bar/", "店舗・イベント告知の実例にもつなげられます。"),
    ],
    "19": [
        ("Global Music Tour #01", "../01-global-music-tour/", "周遊ツアーと滞在をセットで提案できます。"),
        ("123 MUSIC & RESORTS #03", "../03-123-music-resorts/", "宿泊・リゾート体験と自然につなげられます。"),
    ],
    "20": [
        ("Tana Method Certification #11", "../11-tana-method-certification/", "認定・修了導線と組み合わせられます。"),
        ("Voice & Music Studio #09", "../09-voice-music-studio/", "実習・収録の現場につなげられます。"),
    ],
}

BLOG_PORTAL_LEAD = (
    "次の一覧は、AI TARNAR Voice School の記事ライブラリから、このポータル向けに並べた500本です。"
    "日本語・英語・韓国語・中国語のリンクからそのまま記事を開けます。"
)

LINE_SECTION_LEAD = (
    "公式LINEで最新情報のほか、ご予約・ご相談・キャンペーン案内の窓口もまとめてご案内します。"
)


def _fix_tarnar_article_urls(article: dict) -> None:
    urls = article.get("urls") or {}
    fixed: dict[str, str] = {}
    for lang, path in urls.items():
        if not path:
            continue
        fixed[lang] = path if path.startswith("../") else f"../tarnar/{path}"
    article["urls"] = fixed


def syndicated_tarnar_blog_json() -> str:
    src = SITE / "tarnar" / "data" / "blog-manifest.json"
    if not src.exists():
        return json.dumps({"articles": []}, ensure_ascii=False, indent=2) + "\n"
    data = json.loads(src.read_text(encoding="utf-8"))
    for article in data.get("articles", []):
        _fix_tarnar_article_urls(article)
    return json.dumps(data, ensure_ascii=False, indent=2) + "\n"


def syndicated_tarnar_blog_json_for_portal(bid: str, take: int = 500) -> str:
    """各事業ポータル用: 全ライブラリから take 件を安定スライス（URL は ../tarnar/ に補正）。"""
    src = SITE / "tarnar" / "data" / "blog-manifest.json"
    if not src.exists():
        return json.dumps({"articles": []}, ensure_ascii=False, indent=2) + "\n"
    raw = json.loads(src.read_text(encoding="utf-8"))
    articles = list(raw.get("articles", []))
    n = len(articles)
    if n == 0:
        return json.dumps({"articles": []}, ensure_ascii=False, indent=2) + "\n"
    if n <= take:
        picked = articles
    else:
        idx = int(bid) if bid.isdigit() else 1
        start = (idx * 11 + (idx % 7) * 17) % (n - take + 1)
        picked = articles[start : start + take]
    out: list[dict] = []
    for article in picked:
        row = dict(article)
        _fix_tarnar_article_urls(row)
        out.append(row)
    return json.dumps({"articles": out}, ensure_ascii=False, indent=2) + "\n"


def related_portal_cards_html(bid: str) -> str:
    rows = RELATED_PORTALS.get(bid, [])
    parts: list[str] = []
    for title, url, desc in rows:
        parts.append(
            f"""        <article class="cross-card">
          <h3>{html.escape(title)}</h3>
          <p>{html.escape(desc)}</p>
          <a class="btn btn-ghost" href="{html.escape(url)}">ポータルを開く</a>
        </article>"""
        )
    return "\n".join(parts)


# #01 専用：連動グリッドに追加するクロスセル（TARNAR / Izu Fund への自然な導線）
CROSS_EXTRA_01_IZUSAN = """
        <article class="cross-card cross-card--accent" style="grid-column:1/-1">
          <h3>旅の前後は「声」、地域の続きは「ファンド」で</h3>
          <p>参拝と歩行が中心でも、呼吸と音の意識が変わると旅の体感も変わります。<a href="../tarnar/">AI TARNAR Voice School</a> で旅前後の短いルーティンから。伊豆の音楽とまちづくりのレポートは <a href="../izu-fund/">Izu Music Fund</a> のポータルで。</p>
          <p style="margin:0.75rem 0 0">
            <a class="btn btn-ghost" href="../tarnar/">AI TARNAR Voice School を見る</a>
            <a class="btn btn-ghost" href="../izu-fund/">Izu Music Fund を見る</a>
          </p>
        </article>"""


def _compose_cross_block(bid: str, cross_extra: str) -> str:
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
    partner_cross = """        <article class="cross-card" style="grid-column:1/-1">
          <h3>パートナー・関連サイト（相互導線）</h3>
          <p>グループ各ブランド・音楽レーベル・カラオケ・教育窓口へ、そのまま遷移できます。TARNAR ブログライブラリは<strong>1600本規模</strong>まで拡張済みです。</p>
          <ul style="margin:0.5rem 0 0 1.1rem;padding:0;font-size:0.88rem;line-height:1.75;max-width:52rem;color:var(--muted)">
            <li><a href="https://atono.co.jp/" rel="noopener noreferrer" target="_blank">atono co., ltd.</a> — コーポレート（<a href="mailto:123@atono.jp">123@atono.jp</a> · <a href="../01-global-music-tour/">#01 ツアー</a> 相談導線と接続可）</li>
            <li><a href="https://atono.jp/" rel="noopener noreferrer" target="_blank">atono.jp</a> — アーティスト・音楽コンテンツ（<a href="../18-global-digital-marketing/">#18 マーケ</a> · <a href="../13-global-music-partnership/">#13 パートナー</a> と整合可）</li>
            <li><a href="https://123-music.com/" rel="noopener noreferrer" target="_blank">123-music.com</a> — レーベル・リリース（<a href="../03-123-music-resorts/">#03 リゾート</a> · <a href="../06-music-production-first/">#06 制作</a> と接続可）</li>
            <li><a href="https://atamikaraoke.com/" rel="noopener noreferrer" target="_blank">atamikaraoke.com</a> — 熱海カラオケ（<a href="../19-japan-inbound-music-tourism/">#19 インバウンド</a> · <a href="../04-music-cafe-bar/">#04 カフェ</a> 案内と併記可）</li>
            <li><a href="https://karaoke.ac/" rel="noopener noreferrer" target="_blank">karaoke.ac</a> — カラオケ教育（<a href="../tarnar/">TARNAR</a> · <a href="../05-global-music-festival/">#05 フェス</a> 声量設計と併記可）</li>
            <li><a href="../index.html#partner-network">Japan Music Tourism サイト内「グループ・パートナー」一覧</a> — 5サイトを俯瞰</li>
          </ul>
          <p style="margin:0.75rem 0 0;font-size:0.88rem;line-height:1.65;max-width:52rem;color:var(--muted)">窓口の一本化: <a href="mailto:123@atono.jp">123@atono.jp</a> · 地域ファンドは <a href="../izu-fund/">Izu Music Fund</a> · AIコンシェルジュ枠は <a href="../14-regional-music-alliance/">#14 地域連携</a> · 各サイトは上記リンクからトップに入り、本ポータルへ戻るときは <a href="../index.html#business-portals">事業ポータル一覧</a> または <a href="../tarnar/">AI TARNAR Voice School</a> をご利用ください。</p>
        </article>"""
    hub_cross = """        <article class="cross-card">
          <h3>Japan Music Tourism 全事業</h3>
          <p>21事業のポータルから、隣接する体験へ自然に遷移できます。</p>
          <a class="btn btn-ghost" href="../index.html#business-portals">事業ポータルを見る</a>
        </article>"""
    cross_parts = [cross_standard.rstrip()]
    rel = related_portal_cards_html(bid)
    if rel.strip():
        cross_parts.append(rel.rstrip())
    if cross_extra.strip():
        cross_parts.append(cross_extra.strip())
    cross_parts.append(hub_cross.rstrip())
    cross_parts.append(partner_cross.rstrip())
    return "\n".join(cross_parts)


def _program_card(
    ribbon: str,
    title: str,
    subtitle: str,
    price: str,
    capacity: str,
    schedule: list[tuple[str, str]],
) -> str:
    """伊豆山開運ツアー2026：1プログラム分のカード HTML。"""
    rows = "\n".join(
        f'            <li><strong>{html.escape(t)}</strong>　{html.escape(body)}</li>'
        for t, body in schedule
    )
    return f"""        <article class="cross-card program-tier program-card">
          <p class="tier-ribbon">{html.escape(ribbon)}</p>
          <h3 class="program-star-title">{html.escape(title)}</h3>
          <p class="program-tagline">{html.escape(subtitle)}</p>
          <p class="price-line">{html.escape(price)}<span class="price-capacity">（{html.escape(capacity)}）</span></p>
          <ol class="timetable" aria-label="{html.escape(title)}の時間割">
{rows}
          </ol>
        </article>"""


def build_01_global_music_tour_html(b: Biz) -> str:
    """#01 ポータル専用：伊豆山開運ツアー2026 全面最適化レイアウト。"""
    (
        bid,
        _slug,
        brand,
        _priority,
        meta_desc,
        kicker,
        _h1a,
        _h1b,
        _lead,
        _c1,
        _c2,
        _c3,
        _cross_tuple,
    ) = b
    be = html.escape(brand)
    de = html.escape(meta_desc)
    ke = html.escape(kicker)
    blog_lead_e = html.escape(
        BLOG_PORTAL_LEAD + " 伊豆山・熱海エリアの歩き方・マナー・安全の記事もライブラリ内でご覧いただけます。"
    )
    line_lead_e = html.escape(
        "参加者にはアンケートを取り、伊豆山ファンの公式LINEに登録してもらう。"
        "今後のお祭りやイベントサービス情報、お得情報を配信し伊豆山の関係人口を増やしていくことにより、伊豆山の経済が潤う。"
    )
    cross_block = _compose_cross_block("01", CROSS_EXTRA_01_IZUSAN)

    p1 = html.escape("目的：伊豆山ファンをたくさん作り、伊豆山の経済が潤う")
    p2 = html.escape("参加者にはアンケートを取り、伊豆山ファンの公式LINEに登録してもらう。")
    p3 = html.escape(
        "今後のお祭りやイベントサービス情報、お得情報を配信し伊豆山の関係人口を増やしていくことにより、伊豆山の経済が潤う。"
    )
    p4 = html.escape(
        "３プログラムを土日祝日（年間120日間）実施　1日最大60名×120日　最大7,200名の参拝者数増加を目指す"
    )

    prog_a = _program_card(
        "Program 01",
        "★837 steps of destiny",
        "心も身体も整う",
        "参加費 ￥5,500",
        "最小遂行人数10名・最大20名",
        [
            ("8時", "熱海駅発　バスの中で白装束に着替える・ホラ吹き習う"),
            (
                "8時半",
                "伊豆山港、走り湯神社参拝から837段の階段を登りながら歴史や文化の話と123ヨガリトリート",
            ),
            ("10時", "伊豆山神社　正式参拝　登り切った記念品贈呈"),
            ("11時", "熱海駅着（現地解散もOK）"),
        ],
    )
    prog_b = _program_card(
        "Program 02",
        "★二社詣+1",
        "伊豆山と箱根、二つの神社参拝と御膳",
        "参加費 ¥11,000",
        "最小遂行人数10名・最大20名",
        [
            ("11時", "熱海駅発"),
            ("11時半", "伊豆山神社　正式参拝"),
            ("12時", "参集殿にて宮司講話を聴きながら頼朝政子御膳ランチ"),
            ("13時", "箱根神社へ"),
            ("14時", "箱根神社+九頭竜神社　正式参拝"),
            ("14時半", "宮司講話"),
            ("15時", "熱海駅へ"),
            ("16時", "熱海駅（現地解散もOK）"),
        ],
    )
    prog_c = _program_card(
        "Program 03",
        "★6センスボイスリトリート",
        "あなたの本当の声に出会う",
        "参加費 ¥5,500（19時から宮司＆たーなー先生と祝杯+¥5,500）",
        "最小遂行人数10名・最大20名",
        [
            ("16時", "熱海駅発"),
            ("16時半", "伊豆山神社　正式参拝"),
            ("17時", "6センス123ボイスリトリート"),
            ("19時", "熱海駅（現地解散もOK）"),
        ],
    )

    programs_html = f"""
    <section class="block block-highlight" id="mission">
      <h2>伊豆山開運ツアー2026 — 目的と関係人口の拡大</h2>
      <div class="mission-panel">
        <p class="mission-lead">{p1}</p>
        <p>{p2}</p>
        <p>{p3}</p>
        <p class="mission-scale">{p4}</p>
      </div>
      <div class="stats-row" aria-label="開催規模の目安">
        <article class="stat-card">
          <strong>3</strong>
          <span>プログラム</span>
        </article>
        <article class="stat-card">
          <strong>120</strong>
          <span>土日祝・年間開催日</span>
        </article>
        <article class="stat-card">
          <strong>7,200</strong>
          <span>参拝者数の目標</span>
        </article>
      </div>
    </section>

    <section class="block" id="programs">
      <h2>3つのプログラム</h2>
      <p class="section-lead">
        熱海駅発着。参拝・歩行・声と文化の体験を、土日祝の定番コースとしてご用意しています。下記は各プログラムの<strong>標準的な時間割</strong>です。
      </p>
      <div class="program-grid">
{prog_a}
{prog_b}
{prog_c}
      </div>
    </section>

    <section class="block" id="notes">
      <h2>注意事項</h2>
      <div class="notice-board">
        <ul>
          <li>※時間は前後する場合がございます。</li>
          <li>※宮司さんのスケジュールにより他の神職の方が対応される場合がございます。</li>
          <li>※たーなー先生のスケジュールにより他のトレーナーの方が対応される場合がございます。</li>
        </ul>
      </div>
    </section>

    <section class="block" id="cta-survey">
      <div class="cta-izusan">
        <p class="cta-eyebrow">伊豆山ファン公式LINE</p>
        <h2 style="margin-top:0">アンケートのあと、公式LINEにご登録ください</h2>
        <p class="section-lead" style="max-width:42rem">{p2}</p>
        <p class="section-lead" style="max-width:42rem">{p3}</p>
        <div class="hero-cta" style="justify-content: center; margin-top: 1.35rem">
          <a class="btn btn-line js-line-cta" href="#line">伊豆山ファンの公式LINEに登録する</a>
          <a class="btn btn-ghost" href="#programs">3つのプログラムを見る</a>
        </div>
      </div>
    </section>

    <section class="block" id="cross-sell">
      <h2>旅の前後にも、伊豆の音楽ストーリーにも</h2>
      <p class="section-lead">参拝と歩行のあと、声のケアや地域ファンドの活動にも自然につながる導線です。</p>
      <div class="cross-grid cross-grid--pair">
        <article class="cross-card cross-card--accent">
          <h3>AI TARNAR Voice School</h3>
          <p>6センスボイスリトリートと同じ「声」の軸で、旅前後の呼吸・発声ルーティンをオンラインでも続けられます。</p>
          <a class="btn btn-primary" href="../tarnar/#pricing">声の学校を見る</a>
        </article>
        <article class="cross-card cross-card--accent">
          <h3>Izu Music Fund</h3>
          <p>伊豆の音楽とまちづくり。地域の記事・ファンド活動はこちらのポータルから。</p>
          <a class="btn btn-ghost" href="../izu-fund/">Izu Music Fund を開く</a>
        </article>
      </div>
    </section>
"""

    return f"""<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <meta name="robots" content="index, follow" />
  <title>{be}｜伊豆山開運ツアー2026 | Japan Music Tourism #01</title>
  <meta name="description" content="{de}" />
  <link rel="stylesheet" href="../tarnar/portal.css" />
</head>
<body class="page-izusan-tour">
  <header class="nav">
    <a class="nav-brand" href="index.html">{be}</a>
    <nav class="nav-links" aria-label="ナビ">
      <a href="#mission">目的</a>
      <a href="#programs">3つのプログラム</a>
      <a href="#notes">注意事項</a>
      <a href="#cta-survey">LINE登録</a>
      <a href="#cross-sell">連動体験</a>
      <a href="#blog">ブログ</a>
      <a href="#line">公式LINE</a>
      <a href="../index.html">Japan Music Tourism</a>
    </nav>
  </header>

  <section class="hero hero--izusan" id="top">
    <div class="wrap hero-grid">
      <div class="hero-copy">
        <span class="brand-pill">{be}</span>
        <p class="hero-kicker">GMTJ #01 · {ke}</p>
        <h1>伊豆山開運ツアー2026</h1>
        <p class="hero-lead hero-lead--wide hero-lead--hero">
          伊豆山ファンを増やし、お祭り・イベント・お得情報を公式LINEで届ける。<strong>関係人口の拡大</strong>で、伊豆山の経済が潤う旅を、土日祝に。
        </p>
        <div class="hero-cta hero-cta--izusan">
          <a class="btn btn-line js-line-cta" href="#line">公式LINEに登録する</a>
          <a class="btn btn-primary" href="#programs">3つのプログラムを見る</a>
        </div>
      </div>
      <div class="hero-visual hero-visual--izusan" aria-hidden="true">
        <div class="hero-visual-label">熱海 · 伊豆山 · 箱根</div>
      </div>
    </div>
  </section>

  <main class="wrap">
{programs_html}
    <section class="block" id="blog">
      <h2>ブログ記事一覧</h2>
      <p class="section-lead">
        {blog_lead_e}
      </p>
      <ul class="blog-list" id="blog-list"></ul>
      <p class="section-lead" style="margin-top:1rem;font-size:0.9rem">
        <a class="btn btn-ghost" href="../tarnar/#blog">AI TARNAR Voice School ブログへ</a>
        <a class="btn btn-ghost" href="../izu-fund/#blog">Izu Music Fund ブログへ</a>
        <a class="btn btn-ghost" href="../index.html#partner-network">グループ・パートナー</a>
      </p>
    </section>

    <section class="block" id="line">
      <h2>公式LINE</h2>
      <p class="section-lead">
        {line_lead_e}
      </p>
      <div class="hero-cta" style="justify-content: flex-start">
        <a class="btn btn-line js-line-cta" id="line-cta" href="#">LINEで受け取る</a>
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


def build_index_html(b: Biz) -> str:
    if b[0] == "01":
        return build_01_global_music_tour_html(b)
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

    card_tuples: list[tuple[str, str, str]] = [c1, c2, c3]
    fc = FOURTH_SERVICE_CARD.get(bid)
    if fc:
        card_tuples.append(fc)
    cards_html = "\n".join(card(t[0], t[1], t[2]) for t in card_tuples)
    grid_class = "grid-3 cols-4" if fc else "grid-3"

    services_lead_e = html.escape(SERVICES_SECTION_LEAD.get(bid, DEFAULT_SERVICES_LEAD))
    blog_lead_e = html.escape(BLOG_PORTAL_LEAD)
    line_lead_e = html.escape(LINE_SECTION_LEAD)

    cross_block = _compose_cross_block(bid, cross_extra)

    return f"""<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <meta name="robots" content="index, follow" />
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
      <a href="../index.html">Japan Music Tourism</a>
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
          <a class="btn btn-ghost" href="../tarnar/">AI TARNAR Voice School</a>
          <a class="btn btn-ghost" href="../izu-fund/">Izu Music Fund</a>
          <a class="btn btn-ghost" href="https://atono.co.jp/" rel="noopener noreferrer" target="_blank">atono co., ltd.</a>
          <a class="btn btn-ghost" href="https://atono.jp/" rel="noopener noreferrer" target="_blank">atono.jp</a>
          <a class="btn btn-ghost" href="https://123-music.com/" rel="noopener noreferrer" target="_blank">123-music</a>
          <a class="btn btn-ghost" href="https://atamikaraoke.com/" rel="noopener noreferrer" target="_blank">熱海カラオケ</a>
          <a class="btn btn-ghost" href="https://karaoke.ac/" rel="noopener noreferrer" target="_blank">karaoke.ac</a>
        </div>
      </div>
      <div class="hero-visual" aria-hidden="true"></div>
    </div>
  </section>

  <main class="wrap">
    <section class="block" id="services">
      <h2>サービス</h2>
      <p class="section-lead">
        {services_lead_e}
      </p>
      <div class="{grid_class}">
{cards_html}
      </div>
    </section>

    <section class="block" id="blog">
      <h2>ブログ記事一覧</h2>
      <p class="section-lead">
        {blog_lead_e}
      </p>
      <ul class="blog-list" id="blog-list"></ul>
      <p class="section-lead" style="margin-top:1rem;font-size:0.9rem">
        <a class="btn btn-ghost" href="../tarnar/#blog">AI TARNAR Voice School ブログへ</a>
        <a class="btn btn-ghost" href="../izu-fund/#blog">Izu Music Fund ブログへ</a>
        <a class="btn btn-ghost" href="../index.html#partner-network">グループ・パートナー</a>
      </p>
    </section>

    <section class="block" id="line">
      <h2>公式LINE</h2>
      <p class="section-lead">
        {line_lead_e}
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
    sites.extend(
        [
            {"label": "atono.jp", "url": "https://atono.jp/"},
            {"label": "123-music.com", "url": "https://123-music.com/"},
            {"label": "atamikaraoke.com", "url": "https://atamikaraoke.com/"},
            {"label": "karaoke.ac", "url": "https://karaoke.ac/"},
            {"label": "atono co., ltd.", "url": "https://atono.co.jp/"},
            {"label": "グループ・パートナー一覧", "url": "../index.html#partner-network"},
        ]
    )
    cfg = {
        "lineAddFriendUrl": "",
        "contactEmail": "123@atono.jp",
        "mailtoSubject": (
            f"伊豆山開運ツアー2026 · {brand} · LINE登録・アンケートのご希望"
            if bid == "01"
            else f"GMTJ #{bid} {brand} ポータル（公式LINE）"
        ),
        "relatedSites": sites,
    }
    return json.dumps(cfg, ensure_ascii=False, indent=2) + "\n"


def main() -> None:
    portal_js = PORTAL_JS_SRC.read_text(encoding="utf-8")
    for b in BUSINESSES:
        bid, slug, brand, _p, *_rest = b
        blog_json = syndicated_tarnar_blog_json_for_portal(bid, 500)
        d = SITE / slug
        (d / "data").mkdir(parents=True, exist_ok=True)
        (d / "index.html").write_text(build_index_html(b), encoding="utf-8")
        (d / "portal-config.json").write_text(portal_config_json(bid, brand, slug), encoding="utf-8")
        (d / "portal.js").write_text(portal_js, encoding="utf-8")
        (d / "data" / "blog-manifest.json").write_text(blog_json, encoding="utf-8")

    print("Wrote", len(BUSINESSES), "portals under site/. (Redirects: edit netlify.toml manually.)")


if __name__ == "__main__":
    main()
