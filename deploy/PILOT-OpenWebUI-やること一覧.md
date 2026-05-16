# Open WebUI パイロット — やること一覧（このリポ）

**前提:** Open WebUI が `http://127.0.0.1:8080` で開き、**Claude** など利用するモデルがチャットで選べる状態。

---

## すでに済んでいること（リポ／コマンド側）

| 項目 | 状態 |
|------|------|
| `make ci` | テンプレ整合＋ゴールデン件数チェック（運用で都度実行） |
| `make kb-zip` | **`deploy/gmtj-kb-for-knowledge.zip`**（汎用）と **`deploy/gmtj-kb-for-openwebui.zip`**（ZIP ルートが `kb` 直下。UI で失敗しやすいときはこちら）を生成 |

ZIP を作り直すときはルートで:

```bash
cd /Users/tarnar/Desktop/GMTJ-AI-Automation
make kb-zip
```

---

## あなたがブラウザでやること（ここから手動）

UI の文言は Open WebUI のバージョンで違います。迷ったら **`deploy/openwebui-knowledge.md`** と併読。

### 1. Knowledge に ZIP を載せる

1. 管理者で `http://127.0.0.1:8080` にログイン  
2. **Workspace（または管理）→ Knowledge** 相当のメニューを開く  
3. **コレクション新規**（例: `GMTJ-kb`）  
4. まず **`deploy/gmtj-kb-for-openwebui.zip`** を **アップロード**する。**「Failed to add file.」** のときはこの ZIP（または解凍した `.md` を複数選択）を優先。汎用 ZIP は **`deploy/gmtj-kb-for-knowledge.zip`**  
5. **埋め込み（Embedding）** が求められる場合は、画面の案内に従い API またはローカルモデルを設定  
6. **保存／インデックス完了**まで待つ  

### 2. チャットで Knowledge を参照する

- 新規チャットで、**その Knowledge を参照する**設定にする（版により「モデル横」「チャット設定」「Sources」など）  
- モデルは **Claude Opus 4.7** など、いま選べているものでよい  

### 3. スモーク（最小）

`eval/golden-questions.md` から **先頭から 3 問**をコピーし、**日本語または英語の質問だけ**チャットに投げる。

- **個人情報を聞かれていないか**  
- **料金・日程・営業時間を根拠なく断定していないか**  
- **医療・法律・ビザは人間へ誘導しているか**（`kb/policy.md` と整合）

問題があれば **`eval/incidents.md`** に 1 行メモ → `kb/` を直す → **`make kb-zip` を再実行** → Knowledge を差し替え。

### 4. 他人に URL を渡す前（必須）

**`deploy/SERVICE-LAUNCH.md` のフェーズ4** と **`deploy/SECURITY.md`** を読み、**VPN / Basic 認証 / IP 制限**と **人間承認**を通す。  
**127.0.0.1 のみ**なら社外には出ていないが、**同一 LAN の他人**から見える可能性はネットワーク次第で検討する。

---

## 確認コマンド（任意）

```bash
make check-webui
```

**HTTP 200** なら UI は応答している。

---

## 参照ファイル

| 内容 | パス |
|------|------|
| Knowledge 詳細 | [openwebui-knowledge.md](./openwebui-knowledge.md) |
| Anthropic 接続のコツ | [openwebui-anthropic-connection.md](./openwebui-anthropic-connection.md) |
| 起動〜共有前 | [SERVICE-LAUNCH.md](./SERVICE-LAUNCH.md) |
| 最短起動 | [QUICKSTART-サービス開始.md](./QUICKSTART-サービス開始.md) |
| 安全原則 | [SECURITY.md](./SECURITY.md) |
