# kb — 14 AIコンシェルジュ用ナレッジ（入口）

一次情報と `kb/` の範囲で事実を述べる。推測で料金・法令を断定しない。

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
| [regions/](./regions/) | 国内エリア骨子（数値は公式出典＋確認日で追記） |

## 品質・運用

- 評価用質問: `../eval/golden-questions.md`
- 採点ルーブリック: `../eval/scoring-rubric.md`
- テンプレファイルの欠落チェック: リポジトリルートで `bash scripts/verify-kb-templates.sh`（または `make verify-templates`）
