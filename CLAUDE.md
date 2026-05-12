# GMTJ — Claude Code プロジェクト指示書

## このリポジトリの目的

Global Music Tourism Japan（GMTJ）の **21事業のAI自動化** を進めるための、仕様・ナレッジ・評価・デプロイ手順の単一の源（Single Source of Truth）とする。

当面の最優先スプリント（合意済み）:

1. **18 Global Digital Marketing** — 全事業横断の集客・コンテンツ・提案型マーケの基盤  
2. **01 Global Music Tour** — 英語インバウンド向けの「第一のツアー」商品（ルート・体験・安全・マナー）  
3. **14 Regional Music Alliance** — 全国＋インバウンドの **AI観光コンシェルジュ／ナビ**（問い合わせ一次対応・案内）

Claude Code は **実装・スクリプト・設定・リポ内ドキュメント整備・デプロイ可能な形への落とし込み**を主担当とする。  
長文の推敲・法務リスクの深読み・多言語ニュアンスの最終監査は **Claude（Max）チャット**や人間レビューと併用する。

---

## 21事業一覧（PDFベース・識別子）

作業で触れるときは **ID（01–21）** を使う。

| ID | 事業名（短名） |
|----|----------------|
| 01 | Global Music Tour |
| 02 | Real Estate & Revitalization |
| 03 | 123 MUSIC & RESORTS |
| 04 | Music Cafe & Bar |
| 05 | Global Music Festival |
| 06 | Music Production First |
| 07 | Music × Community Japan |
| 08 | AI Tana Voice School |
| 09 | Voice & Music Studio |
| 10 | B2B Voice & Communication |
| 11 | Tana Method Certification |
| 12 | Crowdfunding AI Producer |
| 13 | Global Music Partnership |
| 14 | Regional Music Alliance（AIコンシェルジュ） |
| 15 | Subsidy Intelligence |
| 16 | M&A Music Business |
| 17 | AI GMTJ OS（Tana OS） |
| 18 | Global Digital Marketing |
| 19 | Japan Inbound Music Tourism |
| 20 | Global Music Education Hub |
| 21 | Izu Music Fund |

---

## ディレクトリ規約（kb 中心）

推奨レイアウト。無ければ Claude Code が段階的に作成してよい。

```text
docs/                 # ビジョン・事業マップ・方針
kb/                   # 14コンシェルジュ／ナビ用ナレッジ（一次情報優先）
  policy.md           # 応答ポリシー・禁止・エスカレーション
  sources.md          # 参照してよい情報源のルール
  intents.yaml        # 意図分類（予約・交通・安全・イベント等）
  templates/          # 意図別の返答テンプレ（ja / en）
  regions/            # 国内エリア概要（沖縄・鹿児島・北海道・新潟・広島 等）
  area-atami-izu/     # 熱海・伊豆山・周辺（箱根・三島・小田原・真鶴・湯河原 等の統合プロモ用）
  brand/              # #JapanMusicTourism 等の固定メッセージ
  tours/              # 01ツアー連携FAQ・安全・マナー（英語ゲスト向け／スタッフ向けを分離）
marketing/            # 18用：カレンダー案・投稿案・KW
tour/                 # 01用：タイムライン・Runbook（ゲスト/スタッフ）
eval/                 # 14品質：ゴールデン質問・インシデントログ
os/                   # 17用：共通エンティティ案（将来）
deploy/               # VPS：compose、手順、環境変数テンプレ（秘密はコミットしない）
```

---

## 14 AIコンシェルジュ（最重要ルール）

### 守ること

- **事実は `kb/` と公式一次情報に限定**。推測で営業時間・料金・法令を断定しない。  
- **医療・法律・投資判断・ビザ条件**は案内せず、**人間または専門家へエスカレーション**のテンプレに誘導。  
- **神社・宗教施設**は敬意と安全（服装・行動・撮影）を最優先。不確実な慣習をでっち上げない。  
- **多言語**: 原則 **日本語＋英語** をセットで整備。韓国語が必要な箇所は `templates/` に `ko` を増やす。

### してはいけないこと

- 個人情報の収集・保存をナレッジ化しない（必要なら別途設計し、**このリポに書かない**）。  
- スクレイピングや利用規約違反のデータ取得をしない。  
- 「公式」と嘘の肩書で返答しない。

### エスカレーション

`kb/policy.md` に **「人間に渡す条件」** を必ず書く。Claude Code はテンプレ作成・不足検知まで。最終文言は人間承認。

---

## 01 ツアー（英語インバウンド）

- `tour/` に **ゲスト向け**（物語・時間割・期待値）と **スタッフRunbook**（連絡・安全・代替ルート）を分ける。  
- `kb/tours/` には **FAQ・マナー・体力・装備** を短く反復可能な形で抽出し、14に供給する。

---

## 18 マーケ

- `marketing/` は **90日カレンダー案**、エリア統合メッセージ、チャネル別短文を置く。  
- ブランド表記ゆれ（地名・施設名）は **一覧表**を `kb/area-atami-izu/` または `kb/brand/` に固定する。

---

## Git / 秘密情報

- **APIキー・トークン・個人情報はコミット禁止**。`deploy/.env.example` のみコミットし、実体は `.env`（gitignore）。  
- 変更は **小さなコミット**（例: `kb: add en templates for intent X`）を推奨。

---

## Claude Code に依頼するときの優先タスク例

1. `kb/policy.md` / `kb/sources.md` の初稿とレビュー用チェックリスト（`docs/kb-review-checklist.md`）  
2. `kb/intents.yaml` と `kb/templates/{intent}.{ja,en}.md` の最小セット（韓国語は `ko` を `scripts/verify-kb-templates.sh` で検証。`make ci` でゴールデン件数も確認）  
3. `eval/golden-questions.md`（英日韓混在のゴールデン質問セット。v0.6 は26問・韓国語2問含む）  
4. `deploy/README.md` + `docker-compose.yml` + **[QUICKSTART-サービス開始.md](deploy/QUICKSTART-サービス開始.md)**（**社内限定**のRAG/チャットMVP用。公開前に人間承認）  
5. `docs/business-map.md` の21事業1行サマリ（入力→出力→KPI）

---

## 用語

- **GMTJ**: Global Music Tourism Japan  
- **Tana OS**: 17番の全事業データ一元管理ビジョン（このリポはその「入口」とスキーマ草案を置く）

---

## 完了の定義（スプリント単位）

- 14: `eval/golden-questions.md` のゴールデン質問に対し、`kb/` 範囲で一貫した返答方針が定義されている（問数は運用で拡張可）
- 01: 英語ゲスト向け v0.1 + スタッフRunbook v0.1 が `tour/` に存在し、**参加前チェックリスト**（`tour/checklist-packing-izu-san.md`）があり、`kb/tours/` にFAQが取り込まれている  
- 18: `marketing/90day-ideas.md` が存在し、**`marketing/content-pillars.md`** で柱が整理され、`kb/brand/` と表記が整合している
