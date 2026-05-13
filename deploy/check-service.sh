#!/usr/bin/env bash
# Open WebUI（localhost:8080）が応答するか確認する
set -euo pipefail
cd "$(dirname "$0")"

echo "=== docker compose ps ==="
docker compose ps

echo ""
echo "=== GET http://127.0.0.1:8080/ ==="
code="$(curl -s -o /dev/null -w "%{http_code}" --connect-timeout 5 http://127.0.0.1:8080/)" || code="000"
echo "HTTP ${code}"

if [[ "${code}" == "200" ]]; then
  echo ""
  echo "OK — Web UI は応答しています（インフラの「サービス到達」）。"
  echo "次: ブラウザで http://127.0.0.1:8080 → SERVICE-LAUNCH.md のフェーズ2（管理者・モデル・Knowledge）。"
else
  echo ""
  echo "NG — 期待は 200。Docker Desktop とコンテナを確認してください（QUICKSTART / fast-up.sh）。"
  exit 1
fi
