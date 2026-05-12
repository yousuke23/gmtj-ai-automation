# Shin VPS 向けデプロイ（社内MVP想定）

## 原則

- 公開前は **Basic 認証 or VPN 内のみ**
- 秘密は `.env`（**git に含めない**）。テンプレは `.env.example`

## docker-compose（社内MVP）

`docker-compose.yml` では **Open WebUI** を `127.0.0.1:8080` のみに公開し、リポジトリ直下の `kb/` をコンテナ内 `/kb-ro` に読み取り専用マウントします。

```bash
cd deploy
cp .env.example .env
# .env に WEBUI_SECRET_KEY および利用する API キー等を記入
docker compose up -d
```

ナレッジ（RAG）の具体的な手順は **[openwebui-knowledge.md](./openwebui-knowledge.md)** を参照。要点だけ: コンテナ内では `kb` が **`/kb-ro`** に見える。Open WebUI のバージョン差を避けるため、社内運用の正は **Knowledge への UI アップロード（または `deploy/package-kb-for-knowledge.sh` で作った ZIP）** とする。

公開前は **Basic 認証・VPN・IP 制限**のいずれかで必ず囲むこと。

## Basic 認証つきスタック（任意）

Open WebUI の前に **nginx** を置く例は **`docker-compose.auth-stack.yml`** と **`nginx/README.md`**。パスワードファイル `nginx/.htpasswd` は各自が作成し、**コミットしない**。

## TLS 終端（Caddy・任意）

ホストの **`127.0.0.1:8080`** に既にバックエンドがある状態で、その手前に **HTTPS** をかける例は **`docker-compose.caddy-tls.yml`** と **`caddy/README.md`**。

## 運用メモ

1. ログに個人情報を残さない（`kb/policy.md` と整合）
2. 本番 URL・認証方式は社内ドキュメントで管理し、このリポジトリには秘密を置かない

## 環境変数テンプレ

`deploy/.env.example` を `.env` にコピーしてから値を埋める。
