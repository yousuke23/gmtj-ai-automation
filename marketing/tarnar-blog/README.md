# TARNAR ブログ量産テンプレート

1テーマ（柱）から **30〜50本** の見出しを出し、4言語（日・英・中・韓）で本文を埋める想定です。**200本規模**は `batch_id` と連番でフォルダを分けて管理します。

## フォルダの使い方

| パス | 役割 |
|------|------|
| `batch/theme-one-pillar.example.yaml` | 1テーマのメタと角度スロットの例 |
| `csv/batch-rows.template.csv` | 一括生成用の行テンプレ（スプレッドシートにコピー可） |
| `skeleton/article.*.md` | 言語別の本文スケルトン（見出しだけ） |
| `posts/` | 生成物を置く（`posts/{ja,en,ko,zh}/{batch}-{nnn}-{slug}.md` を推奨） |

## 30〜50本の出し方

1. `batch/theme-one-pillar.example.yaml` を複製し、`theme_id` と `pillar` を書く。  
2. `angles` に短文の切り口を **30〜50行** 並べる（同じ柱でも検索意図がぶれないよう変える）。  
3. `csv/batch-rows.template.csv` にエクスポートするか、CSV をそのまま増やす。列 `angle_ja` をマスタにし、`angle_en` `angle_ko` `angle_zh` を翻訳で埋める。  
4. 各行について `skeleton/article.{ja,en,ko,zh}.md` を複製し、フロントマターの `slug` `title` `angle` を埋める。  
5. 公開用ポータル `site/tarnar/data/blog-manifest.json` に一覧行を追加する（またはビルドスクリプトで JSON を生成）。

## 200本規模

- `batch_id` を `tarnar-2026q2-a` のように分割し、**1バッチ最大50本**でファイルを分ける。  
- ファイル名例: `posts/ja/tarnar-2026q2-a-001-voice-warmup-basics.md`  
- 重複 `slug` を避けるため `slug` は `{pillar_short}-{topic_hash}-{index}` 推奨。

## 品質ゲート

医療・法律・投資勧誘は書かない。固有名詞・料金・実績は一次情報に合わせる。公開前に人間レビューを通す。
