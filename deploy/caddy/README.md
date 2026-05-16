# Caddy で TLS 終端（ホストの :8080 背後を https で叩く例）

Open WebUI 単体、または **`docker-compose.auth-stack.yml`** で立ち上げた nginx ＋ Open WebUI が、**ホストの `127.0.0.1:8080`** で待っている前提です。その手前に **HTTPS** をかけたいときの参考構成です。

## 手順（概要）

1. まず普段どおり `127.0.0.1:8080` でバックエンドが応答することを確認する。  
2. `deploy` で Caddy 用 compose を起動する:

```bash
cd /Users/tarnar/Desktop/GMTJ-AI-Automation/deploy
docker compose -p gmtj-caddy -f docker-compose.caddy-tls.yml up -d
```

3. ブラウザで **`https://127.0.0.1:8443`** を開く。初回は Caddy の **内部 CA** による証明書のため、ブラウザに警告が出る。社内検証用として警告を通過するか、社内 CA 配布ポリシーに従う。

## ファイル

- **`Caddyfile.example`** … `tls internal` ＋ `host.docker.internal:8080` へのリバースプロキシ  
- **`docker-compose.caddy-tls.yml`** … Caddy を `127.0.0.1:8443`（コンテナ内 443）にだけバインド

## 注意

- **本番ドメイン＋Let's Encrypt** に切り替える場合は、`Caddyfile.example` のブロックを実ドメイン名に変更し、ポート 80/443 の開放と DNS を社内手順で整備する。  
- Linux では `extra_hosts: host.docker.internal:host-gateway` が必要（compose に記載済み）。  
- Basic 認証は **バックエンドの nginx** 側（`auth-stack`）でかけつつ、Caddy で TLS をかける、という二段構成が可能。

## 全世界向け（Let's Encrypt）

ローカル検証用の `Caddyfile.example` とは別に、**実ドメイン＋ACME** で nginx 背後へ中継する例は **[../WORLDWIDE-STAGING.md](../WORLDWIDE-STAGING.md)** と **`Caddyfile.worldwide`**、`docker-compose.worldwide-staging.yml` を参照。
