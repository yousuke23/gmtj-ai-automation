# サービス開始まで（社内パイロット用チェックリスト）

**使わない場合:** **Open WebUI／Docker を使わない**運用なら **このファイルは不要**です。ナレッジ品質はルートの **`make ci`** と **`eval/`**・**`kb/`**（[CLAUDE.md](../CLAUDE.md)）。

## この文書の位置づけ（最初に読む）

**あなたの環境（手元の Mac など）で「サービス開始まで」進める手順**は次のとおりです。

1. **[QUICKSTART-サービス開始.md](./QUICKSTART-サービス開始.md)** で **Open WebUI を起動**する（**Docker Desktop 必須**）。  
2. 起動できたら、**このファイル（`SERVICE-LAUNCH.md`）のフェーズ**に沿って進める。  
   - **管理者設定**（フェーズ2）  
   - **Knowledge**（フェーズ2・[openwebui-knowledge.md](./openwebui-knowledge.md)）  
   - **スモーク**（フェーズ3）  
   - **招待前ゲート**（フェーズ4・[SECURITY.md](./SECURITY.md)）  
3. **Cursor などの AI チャット環境には Docker がない**ため、**実際のコンテナ起動はご自身の Mac のターミナル**での実行が必要です（このリポの手順書は「何を打つか」の正本です）。

**対象:** 手元または社内ネットワークで **Open WebUI を「チームが触れる状態」**にするとき。  
**前提:** コンテナの起動手順は **[QUICKSTART-サービス開始.md](./QUICKSTART-サービス開始.md)**（または **`deploy/fast-up.sh`**）。本書はその**先**（初回設定・品質・公開範囲）です。

### すでに Open WebUI が動いている場合

`deploy` で `docker compose ps` し、`gmtj-open-webui` が **Up**（**healthy** ならなお良い）なら **フェーズ1は完了扱い**で **[フェーズ2](#フェーズ2--初回セットアップopen-webui-画面)** へ進んでください。

---

## フェーズ0 — リポジトリが整っているか（Docker 不要）

- [ ] ルートで `make ci` が通る（テンプレ整合＋ゴールデン件数）
- [ ] `kb/` の更新方針を把握している（`kb/policy.md`、`docs/kb-review-checklist.md`）

---

## フェーズ1 — プロセス起動（Docker 必須）

- [ ] Docker Desktop が起動している
- [ ] `deploy/.env` に `WEBUI_SECRET_KEY` を設定済み（`.env.example` からコピー）
- [ ] `deploy` で `docker compose up -d` が成功し、`docker compose ps` で `open-webui` が Up
- [ ] ブラウザで **http://127.0.0.1:8080** が開く（迷ったら [QUICKSTART の「つまずいたとき」](./QUICKSTART-サービス開始.md#つまずいたとき)）

**自動確認（任意）:** `deploy` で `bash check-service.sh` → **`HTTP 200`** なら **インフラとしてのサービス到達**（UI はブラウザで開く）。

---

## フェーズ2 — 初回セットアップ（Open WebUI 画面）

※ 文言は Open WebUI のバージョンで変わる。迷ったら公式ドキュメントと併読。

- [ ] **管理者アカウント**を作成（初回アクセス時の案内に従う）
- [ ] 利用する **モデル（API キーまたはローカル LLM）** を設定し、単純な「こんにちは」で応答があることを確認
- [ ] （推奨）**Knowledge** に `kb` を取り込む（[openwebui-knowledge.md](./openwebui-knowledge.md)／ZIP は `bash deploy/package-kb-for-knowledge.sh`）

**ここまでできれば「社内MVPとしてのサービス開始」**（個人～少人数で試用可能）。他者公開はフェーズ4。

---

## フェーズ3 — 品質スモーク（最小）

- [ ] `eval/golden-questions.md` から **2〜3問**を選び、**断定・個人情報要求・禁止領域**に入っていないか目視
- [ ] 問題があれば `eval/incidents.md` に1行メモし、`kb/` 側の修正方針を決める（社内プロセス）

---

## フェーズ4 — 「他者を呼ぶ」前のゲート（必須）

- [ ] **[SECURITY.md](./SECURITY.md)** を読み、**VPN / Basic 認証 / IP 制限**のいずれかで入口を囲む計画がある（`docker-compose.auth-stack.yml` 等）
- [ ] **インターネット全体に URL を晒す**前に、**人間承認**を得る
- [ ] ログに **パスポート・カード・住所**が残らない運用であることを確認

---

## フェーズ5 — パイロット開始の宣言（運用）

- [ ] 利用時間・問い合わせ窓口・障害時連絡を **社内の別ドキュメント**に記載（このリポには秘密を書かない）
- [ ] 関係者へ「試用 URL・認証情報・注意事項」を共有（チャットに API キーを貼らない）

---

## ロールバック（いつでも）

```bash
cd /Users/tarnar/Desktop/GMTJ-AI-Automation/deploy
docker compose down
```

データを消して最初からやり直す場合は、ボリューム削除が必要になることがある。運用方針に従い、**本番相当のデータは別途バックアップ**すること。

---

## 参照

| 内容 | ファイル |
|------|------------|
| 最速起動 | [QUICKSTART-サービス開始.md](./QUICKSTART-サービス開始.md) |
| ナレッジ取り込み | [openwebui-knowledge.md](./openwebui-knowledge.md) |
| 全体・Compose | [README.md](./README.md) |
| 日々の運用メモ | [../docs/operations-runbook.md](../docs/operations-runbook.md) |
