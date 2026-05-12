# 最速でサービスを始める（社内 Open WebUI）

**注意:** AI チャット（Cursor 上の会話など）からは、**あなたの Mac の Docker を直接操作してコンテナを起動することはできません。** 起動は **ご自身のターミナル**で次のコマンドを実行してください。

**前提**: Mac に [Docker Desktop](https://www.docker.com/products/docker-desktop/) を入れ、**起動しておく**（メニューバーにクジラのアイコン）。

## 1. 秘密の設定（初回だけ）

```bash
cd /Users/tarnar/Desktop/GMTJ-AI-Automation/deploy
cp .env.example .env
```

`.env` を開き、`WEBUI_SECRET_KEY=` の右に **長いランダム文字列**を入れる。  
チャットで OpenAI 等を使うなら `OPENAI_API_KEY=` も（空のままだとローカル LLM 設定が必要）。

## 2. 起動

```bash
cd /Users/tarnar/Desktop/GMTJ-AI-Automation/deploy
docker compose up -d
```

## 3. ブラウザ

**http://127.0.0.1:8080** を開く（この URL だけが compose で公開されています）。

## 4. ナレッジ（任意・すぐ試すなら）

別ターミナルで:

```bash
cd /Users/tarnar/Desktop/GMTJ-AI-Automation
bash deploy/package-kb-for-knowledge.sh
```

できた `deploy/gmtj-kb-for-knowledge.zip` を Open WebUI の **Knowledge** にアップロード（手順の詳細は [openwebui-knowledge.md](./openwebui-knowledge.md)）。

## 5. 止める

```bash
cd /Users/tarnar/Desktop/GMTJ-AI-Automation/deploy
docker compose down
```

## もっと早く「社外に近い形」で囲む

- 入口にパスワード: [nginx/README.md](./nginx/README.md) → `docker-compose.auth-stack.yml`  
- HTTPS の検証: [caddy/README.md](./caddy/README.md)

公開インターネットに出す前は **[SECURITY.md](./SECURITY.md)** と人間承認を必ず通すこと。

---

## つまずいたとき

| 症状 | 試すこと |
|------|----------|
| **まだアカウント登録していないのにパスワード**を求められる | 下の「パスワードが出る典型例」を読む（ブラウザの種類・URL で切り分け） |
| `command not found: docker` | **Docker Desktop を起動**し、ターミナルを開き直す |
| `docker compose up` が失敗する | `deploy` にいるか、`WEBUI_SECRET_KEY` が `.env` に入っているか確認 |
| 8080 が開かない | `docker compose ps` で `open-webui` が Up か。別アプリが 8080 を占有していないか |

起動後の **管理者・Knowledge・検証・公開前チェック** は **[SERVICE-LAUNCH.md](./SERVICE-LAUNCH.md)** のフェーズに進んでください。

### パスワードが出る典型例（初期登録の前かどうか）

1. **macOS のダイアログで「パスワードを入力」**（鍵マーク・システム風）  
   → **Docker Desktop のインストール／推奨設定**などが、管理者権限の変更をしようとしているだけです。**Open WebUI の登録とは別**です。

2. **ブラウザが出す「ユーザー名とパスワードを入力」**（グレーの小さなダイアログ・サイトの外観ではない）  
   → **nginx の Basic 認証**の可能性が高いです。`docker-compose.auth-stack.yml` を使っている場合や、**別のポート／プロキシ**の前段で認証がかかっていることがあります。  
   → まずは **単体の Open WebUI** 用 compose で起動しているか確認し、URL は **`http://127.0.0.1:8080`**（このリポの `docker-compose.yml` の前提）に合わせる。Basic 認証の ID/パスは [nginx/README.md](./nginx/README.md) で設定した値。

3. **Open WebUI の「ログイン」画面**（メール／パスワードの入力フォーム）で、**新規登録に進めない**  
   → **以前に同じ PC で起動したデータ**が Docker のボリュームに残っていると、**初回の「管理者作成」ではなくログイン**になることがあります。  
   → 本当に捨ててよいデータだけなら、`deploy` で `docker compose down` のあと **ボリューム削除**（例: `docker volume rm` で `open-webui-data` に相当する名前）を検討。運用データがある場合は削除せず、既存アカウントでログインするか別途バックアップのうえ相談。
