# 全世界向け — ステージング起動手順（VPS + TLS + Basic）

**目的:** インターネット全体から **HTTPS** で届き、**nginx Basic 認証**の後に Open WebUI が開く最小構成。  
**前提:** パブリック IP の **Linux VPS**（Ubuntu 等）、**Docker** と **Docker Compose v2** が入っていること。

**このリポでは「手順と Compose 例」まで。** ドメイン取得・DNS・請求・法務文書は別途あなたの組織で行う。

---

## 0. やらないこと

- 自宅 Mac で **0.0.0.0:80/443** を全世界に開けない（誤起動・家庭用ルータの制約・リスク大）。
- **Basic 認証だけ＋HTTP** で公開しない（`SECURITY.md` 参照）。

---

## 1. DNS とファイアウォール

1. 使うホスト名を決める（例: `chat.staging.example.com`）。**ステージング用サブドメイン**を推奨。  
2. DNS で **A レコード**（および IPv6 なら AAAA）を **VPS のパブリック IP** に向ける。  
3. VPS のファイアウォールで **TCP 80, 443** を開ける（SSH は別ポートでも可）。  
4. 伝播待ち: `dig +short chat.staging.example.com` が正しい IP を返すまで待つ。

---

## 2. サーバー上の準備

```bash
# リポを置く（例）
git clone <あなたのリポURL> GMTJ-AI-Automation
cd GMTJ-AI-Automation/deploy
cp .env.example .env
```

`.env` に最低限:

- `WEBUI_SECRET_KEY` … 長いランダム文字列  
- モデル用のキー（Anthropic 等）… 全世界向けでも **サーバー側の環境変数のみ**

全世界用に **追記**:

```bash
# ドメイン（DNS が当たっている名前と一致させる）
GMTJ_PUBLIC_DOMAIN=chat.staging.example.com
# Let's Encrypt 用（有効なメール）
ACME_EMAIL=ops@example.com
```

**Basic 認証用の `.htpasswd`:**

```bash
cd nginx
# htpasswd または Docker 例は nginx/README.md 参照
htpasswd -c .htpasswd admin
chmod 600 .htpasswd
cd ..
```

---

## 3. 起動

```bash
cd /path/to/GMTJ-AI-Automation/deploy
docker compose -p gmtj-www -f docker-compose.worldwide-staging.yml up -d
docker compose -p gmtj-www -f docker-compose.worldwide-staging.yml ps
```

初回は Caddy が **Let's Encrypt** で証明書を取りに行く。**DNS がまだ当たっていないと失敗**する。

---

## 4. 確認

1. ブラウザで `https://（GMTJ_PUBLIC_DOMAIN）` を開く。  
2. **証明書エラーがない**こと（正しいドメインで開いているか）。  
3. **Basic 認証** → Open WebUI のログイン画面。  
4. チャットが一通り動く（モデル API の課金・キーも確認）。

---

## 5. Open WebUI をリバースプロキシの背後で使うとき

バージョンにより **URL や信頼プロキシ**の環境変数が必要なことがある。挙動がおかしい場合は [Open WebUI の環境変数ドキュメント](https://docs.openwebui.com/reference/env-configuration) を参照し、`WEBUI_URL` 等を HTTPS の公開 URL に合わせる。

---

## 6. 本番 URL に切り替える前

- `deploy/SECURITY.md` の **「全世界向け」** セクションを満たす（OAuth 検討・レート制限・ナレッジの秘匿など）。  
- `deploy/SERVICE-LAUNCH.md` **フェーズ4**（人間承認）。  
- 利用規約・プライバシー（サイト上の別ページ）は組織側で用意。

---

## 7. 止める・消す

```bash
cd deploy
docker compose -p gmtj-www -f docker-compose.worldwide-staging.yml down
```

データを捨てる場合はボリューム `open-webui-data-www` 等の扱いに注意（バックアップ方針は社内で）。

---

## 参照

| 内容 | ファイル |
|------|----------|
| セキュリティ原則 | [SECURITY.md](./SECURITY.md) |
| Basic 作成 | [nginx/README.md](./nginx/README.md) |
| 社内ローカル用 Caddy 例 | [caddy/README.md](./caddy/README.md) |
