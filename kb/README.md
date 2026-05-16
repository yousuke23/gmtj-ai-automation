# kb — 14 AIコンシェルジュ用ナレッジ（入口）

一次情報と `kb/` の範囲で事実を述べる。推測で料金・法令を断定しない。リポジトリ内の **`docs/` 目次**は [docs/README.md](../docs/README.md)。

## 合意済みの作業順（スプリント）

**14（当フォルダ中心）→ 01（`tour/`・`kb/tours/`）→ 18（`marketing/`・`kb/brand/`）。** 一覧表は [docs/README.md](../docs/README.md) の「作業の優先順」節を正とする。

## まず読む

| ファイル | 内容 |
|----------|------|
| [policy.md](./policy.md) | 応答ポリシー・エスカレーション・禁止 |
| [sources.md](./sources.md) | 情報源の優先順位 |
| [intents.yaml](./intents.yaml) | 意図分類（テンプレ名と対応） |

## サブフォルダ

| パス | 内容 |
|------|------|
| [templates/](./templates/) | 意図別返答テンプレ（`.ja` `.en` `.ko`）一覧は [templates/README.md](./templates/README.md) |
| [tours/](./tours/) | 01ツアー連携 FAQ・スタッフ安全メモ |
| [brand/](./brand/) | ブランド文案ドラフト（入口: [brand/README.md](./brand/README.md)） |
| [area-atami-izu/](./area-atami-izu/) | 熱海・伊豆山周辺（入口: [area-atami-izu/README.md](./area-atami-izu/README.md)） |
| [regions/](./regions/) | 国内エリア骨子（[regions/README.md](./regions/README.md) 一覧）。熱海・伊豆山は [regions/atami-izu.md](./regions/atami-izu.md)、箱根・三島・真鶴は同フォルダ内の各ファイル |

## 品質・運用

- 評価用質問: `../eval/golden-questions.md`
- 評価フォルダ入口: `../eval/README.md`
- 採点ルーブリック: `../eval/scoring-rubric.md`（ゴールデンセットの版に追従）
- テンプレファイルの欠落チェック: `make ci`（`verify-templates` + `eval` のゴールデン件数）または個別に `bash scripts/verify-kb-templates.sh` / `bash scripts/verify-golden-questions.sh`
- **GitHub:** `main` / `master` への push と PR で **`.github/workflows/ci.yml`** が `make ci` を実行します（スプリント本線のゲート）。
