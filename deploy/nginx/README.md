# nginx + Basic 認証（Open WebUI の前段）

`docker-compose.auth-stack.yml` は **Open WebUI をホストに直接公開せず**、nginx が `127.0.0.1:8080` で受け、Basic 認証後に中継します。

## 1. パスワードファイルを作る（初回のみ）

**`deploy/nginx/.htpasswd` は git に含めない**（`.gitignore` 済み）。次のいずれかで作成する。

### A. `htpasswd` コマンドがある場合（Homebrew の `httpd` など）

```bash
cd /Users/tarnar/Desktop/GMTJ-AI-Automation/deploy/nginx
htpasswd -c .htpasswd admin
# パスワードを2回入力
```

### B. Docker で作る（Mac で htpasswd が無いとき）

```bash
cd /Users/tarnar/Desktop/GMTJ-AI-Automation/deploy/nginx
docker run --rm -it httpd:2.4-alpine htpasswd -nbB admin 'ここに強いパスワード' > .htpasswd
```

ファイルができたら権限を絞るとよい: `chmod 600 .htpasswd`

## 2. 起動

```bash
cd /Users/tarnar/Desktop/GMTJ-AI-Automation/deploy
cp .env.example .env   # 未作成なら。WEBUI_SECRET_KEY を設定
docker compose -p gmtj-auth -f docker-compose.auth-stack.yml up -d
```

ブラウザ: `http://127.0.0.1:8080` → Basic 認証 → Open WebUI。

## 3. 注意

- Basic 認証は **HTTPS なしではパスワードが平文に近い形で流れる**ため、社内LAN・VPN前提とし、可能なら TLS 終端を別途置く。
- 素の `docker-compose.yml` と **同時に 8080 を取り合わない**こと。片方を止めてから切り替える。
