# 最速でサービスを始める（社内 Open WebUI）

**使わない場合:** 運用方針で **Open WebUI／Docker を使わない**ときは **このファイルを読む必要はありません**（`kb/`・`eval/`・`make ci` を正とする）。

**注意:** AI チャット（Cursor 上の会話など）からは、**あなたの Mac の Docker を直接操作してコンテナを起動することはできません。** 起動は **ご自身のターミナル**で次のコマンドを実行してください。

**前提**: Mac に [Docker Desktop](https://www.docker.com/products/docker-desktop/) を入れ、**起動しておく**（メニューバーにクジラのアイコン）。

## いちばん速い（この3行）

```bash
cd /Users/tarnar/Desktop/GMTJ-AI-Automation/deploy
bash fast-up.sh
```

ブラウザで **http://127.0.0.1:8080** を開く。初回は **管理者アカウント作成**の案内が出ます（既にデータがある PC ではログイン画面）。

- `WEBUI_SECRET_KEY` が初期値のときだけ、`fast-up.sh` がランダム値を自動セットします。
- 起動後のチェックリスト: **[SERVICE-LAUNCH.md](./SERVICE-LAUNCH.md)**

手動で `.env` を編集したい場合やエラー時は、下の **手順 1〜3** を使ってください。

## 1. 秘密の設定（初回だけ・手動）

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
| `command not found: docker` | **Docker Desktop を起動**し、ターミナルを開き直す |
| 初回の `docker compose up -d` が長い | **`ghcr.io/open-webui/open-webui` のイメージ取得**で数分〜かかることがある。終われば次回からは短くなりやすい |
| `docker compose up` が失敗する | `deploy` にいるか、`WEBUI_SECRET_KEY` が `.env` に入っているか確認 |
| 8080 が開かない | `docker compose ps` で `open-webui` が Up か。別アプリが 8080 を占有していないか |

起動後の **管理者・Knowledge・検証・公開前チェック** は **[SERVICE-LAUNCH.md](./SERVICE-LAUNCH.md)** のフェーズに進んでください。
