# GMTJ OS — Phase 1（自動化の記録）

## このリポジトリで保持しているもの

1. **`site/gmtj-os/data/automation-summary.json`**  
   #08 / #21 の自動化項目と、21事業×2レーン（計42）の実行結果フィールド。

2. **`site/gmtj-os/data/operations-dashboard.json`**  
   公開用ダッシュボードの表示内容（リポジトリ上の登録数と同期）。

3. **`site/gmtj-os/workflows/`**  
   #08 / #21 のワークフロー仕様（Markdown）。

## 本番の日次実行

ジョブ本体は別システムで動かし、結果だけを上記 JSON に反映する運用を想定しています。

Netlify でサイトを更新するには、このリポジトリを push してください。
