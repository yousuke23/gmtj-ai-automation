# 運用 Runbook（社内MVP・短版）

**Open WebUI を使わない運用:** 下の「日常」1〜2はスキップし、**`make ci`** と **`kb/`** の更新フローだけ追う（[CLAUDE.md](../CLAUDE.md)）。

Open WebUI / nginx / Caddy を触る担当者向け。**秘密はこのリポに書かない。**

## 日常

1. バックエンドが **`127.0.0.1:8080`** で応答するか確認（素の compose か auth-stack かを把握）。ファイル対応は **`deploy/README.md`** の Compose 一覧表。  
2. `kb/` を更新したら、運用方針に従い **Knowledge の再取り込み**（`deploy/openwebui-knowledge.md`）。  
3. 変更後は `make ci`（テンプレ整合＋ゴールデン件数）を通す。  
4. ルートや施設の**バリアフリー可否**に関わる説明を変えた場合は、同日中の運用で公式案内・現地制約の確認方法を共有する。

## リリース前チェック

- `docs/kb-review-checklist.md` のチェック  
- `deploy/SECURITY.md` の原則（認証・TLS・ログ）  
- 公開 URL を広げる場合は **必ず人間承認**

## 障害時（ざっくり）

| 症状 | 確認 |
|------|------|
| 502 / 接続拒否 | `docker compose ps`、該当 compose のログ |
| `docker: command not found` | [QUICKSTART の「つまずいたとき」](../deploy/QUICKSTART-サービス開始.md#つまずいたとき)、Docker Desktop の起動 |
| 認証が通らない | `deploy/nginx/.htpasswd` の存在・権限、nginx ログ |
| TLS 警告が消えない | Caddy の `tls internal` は社内検証用。本番は別設計 |

## 連絡

エスカレーション先・本番 URL は **社内の別ドキュメント**に記載する（このリポには書かない）。
