# 21事業マップ（1行サマリ）

| ID | 事業 | 入力（例） | 出力（例） | KPI（例） |
|----|------|------------|------------|-----------|
| 01 | Global Music Tour | 旅行者ニーズ・日程 | ツアー枠・案内文 | 予約数・満足度 |
| 02 | Real Estate & Revitalization | 物件・地域条件 | 提案・契約支援 | 成約・紹介 |
| 03 | 123 MUSIC & RESORTS | 宿泊需要 | 体験パッケージ | 稼働率・ADR |
| 04 | Music Cafe & Bar | 来店・イベント | メニュー・POS連携 | 客単価・回転 |
| 05 | Global Music Festival | 企画・出演 | イベント制作 | 動員・スポンサー |
| 06 | Music Production First | ブランド要件 | 楽曲・音源 | 納品数・再利用 |
| 07 | Music × Community Japan | コミュニティ活動 | 企画・発信 | 参加率 |
| 08 | AI TARNAR Voice School | 学習者 | レッスン・評価 | 完走率・継続 |
| 09 | Voice & Music Studio | 体験予約 | セッション設計 | 予約・再訪 |
| 10 | B2B Voice & Communication | 企業課題 | 研修設計 | 受注・NPS |
| 11 | Tana Method Certification | 受講履歴 | 認定・LMS | 認定者数 |
| 12 | Crowdfunding AI Producer | アイデア | 企画書・リターン | 達成率 |
| 13 | Global Music Partnership | 海外パートナー | 契約・配信 | 案件数 |
| 14 | Regional Music Alliance | 問い合わせ | AI案内・人間接続 | 一次解決率 |
| 15 | Subsidy Intelligence | 要項・事業計画 | 申請パッケージ | 採択率 |
| 16 | M&A Music Business | 案件情報 | DDサマリ | パイプライン |
| 17 | AI GMTJ OS | 各事業データ | 一元KPI | データ鮮度 |
| 18 | Global Digital Marketing | テーマ・カレンダー | 投稿・LP | リード・CV |
| 19 | Japan Inbound Music Tourism | 旅行者FAQ | 目的地コンテンツ | 滞在・導線 |
| 20 | Global Music Education Hub | 学習者属性 | 教材・LMS | 登録・修了 |
| 21 | Izu Music Fund | 投資家条件 | 案件パイプライン | 組入・利回り |

※ KPI は後で `os/` の定義と揃える。

## 21事業すべてを扱う最適な方法（このリポジトリ）

**結論: 21 本分の独立コンテナや API をこのリポだけで立てるのではなく、次の3層に分けるのが最適です。**

1. **体験・社内試用の「サービス面」は 1 系統に集約する**  
   [Open WebUI + Docker](../deploy/README.md) を **1 つ**起動し、[Knowledge](../deploy/openwebui-knowledge.md) に `kb`（ZIP またはディレクトリ）を載せる。チャット上で事業名・ID（01–21）を明示して聞く運用にすると、**21 領域を横断して試せる**一方、インフラは増やさない。

2. **正と品質ゲートはリポのファイルに置く（全事業共通のガードレール）**  
   [`kb/policy.md`](../kb/policy.md)・[`kb/sources.md`](../kb/sources.md)・[`kb/intents.yaml`](../kb/intents.yaml)・テンプレは **どの事業の話題でも前提**にする。更新後はルートで **`make ci`**。高リスク領域（例: **15** 補助金、**16** M&A、**21** ファンド）は **断定・投資判断をしない**方針を `policy` に沿って運用する。

3. **ナレッジの厚みは「合意済み優先 → 必要な ID から順に」**  
   いまリポで厚くするのは下表の **14 → 01 → 18**。その他の ID は、**専用の本番システム**（予約・決済・LMS 等）は別プロダクト前提とし、このリポでは **`kb/` のメモ・`marketing/`・将来の `os/`** などに **段階的に**足していくのが現実的です。**17（Tana OS）**は「全事業データ一元」の設計枠で、**単一チャットの起動だけでは完結しません**。

**いちばん短い作業順（推奨）:** `make ci` → `make kb-zip` → [QUICKSTART](../deploy/QUICKSTART-サービス開始.md) または `deploy/fast-up.sh` → [SERVICE-LAUNCH](../deploy/SERVICE-LAUNCH.md)（管理者・モデル・Knowledge・スモーク・招待前ゲート）。

## このリポとの対応（スプリント優先 14 → 01 → 18）

21事業全体の一覧は上表。当面このリポで厚くするのは次の3つ（作業順は [docs/README.md](./README.md) の「作業の優先順」節）。

| ID | フォルダ入口 |
|----|----------------|
| **14** | [`kb/README.md`](../kb/README.md)、[`eval/golden-questions.md`](../eval/golden-questions.md)、ルートで `make ci` |
| **01** | [`tour/README.md`](../tour/README.md)、[`kb/tours/README.md`](../kb/tours/README.md) |
| **18** | [`marketing/content-pillars.md`](../marketing/content-pillars.md)、[`kb/brand/README.md`](../kb/brand/README.md)、[`marketing/90day-ideas.md`](../marketing/90day-ideas.md) |
