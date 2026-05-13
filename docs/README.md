# `docs/` — ドキュメント目次

| ファイル | 誰向け | 内容 |
|----------|--------|------|
| [START_HERE-超初心者.md](./START_HERE-超初心者.md) | 初参加者 | 環境構築から日常までの順路 |
| [チェックリスト-初日.md](./チェックリスト-初日.md) | 初参加者 | 初日・任意2日目のチェック |
| [glossary.md](./glossary.md) | 全員 | 用語の短い説明 |
| [kb-review-checklist.md](./kb-review-checklist.md) | ナレッジ編集者 | `kb/` 更新時の人間レビュー |
| [operations-runbook.md](./operations-runbook.md) | 社内運用 | Open WebUI 周りの短い Runbook |
| [business-map.md](./business-map.md) | 全員 | 21事業1行サマリ・**14/01/18 のリポ入口** |
| [../eval/README.md](../eval/README.md) | 品質・14担当 | ゴールデン質問・ルーブリック・インシデントログ入口 |

リポジトリ全体のルールとフォルダ規約はルートの **`CLAUDE.md`**。**完了の定義（スプリント）**も `CLAUDE.md` に記載。

## 作業の優先順（合意済み・14 → 01 → 18）

Open WebUI / Docker は任意。**ナレッジとファイル編集だけでこの順で進められる。**

| 順 | 事業（短名） | 主なフォルダ・検証 |
|----|----------------|---------------------|
| 1 | **14** Regional Music Alliance（AIコンシェルジュ） | [`kb/`](../kb/README.md)、[`eval/golden-questions.md`](../eval/golden-questions.md)、ルートで `make ci` |
| 2 | **01** Global Music Tour（英語インバウンド第一ツアー） | [`tour/`](../tour/README.md)、[`kb/tours/`](../kb/tours/README.md) |
| 3 | **18** Global Digital Marketing | [`marketing/content-pillars.md`](../marketing/content-pillars.md)、[`kb/brand/`](../kb/brand/README.md)、[`marketing/90day-ideas.md`](../marketing/90day-ideas.md) |

## 関連（`docs/` 外）

| パス | 内容 |
|------|------|
| [../deploy/QUICKSTART-サービス開始.md](../deploy/QUICKSTART-サービス開始.md) | **Docker を使う場合のみ**最短起動（使わないならスキップ可） |
| [../deploy/SERVICE-LAUNCH.md](../deploy/SERVICE-LAUNCH.md) | **Docker を使う場合のみ**起動後チェックリスト |
| [../marketing/content-pillars.md](../marketing/content-pillars.md) | マーケ3本柱（ドラフト） |
| [../tour/checklist-packing-izu-san.md](../tour/checklist-packing-izu-san.md) | ツアー参加前チェック |
| [../kb/regions/atami-izu.md](../kb/regions/atami-izu.md) | 熱海・伊豆山リージョン入口 |
