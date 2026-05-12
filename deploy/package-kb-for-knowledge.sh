#!/usr/bin/env bash
set -euo pipefail
# リポジトリルート（deploy の一つ上）から kb を ZIP 化し、Open WebUI Knowledge へ
# 手動アップロードしやすいファイル名を標準出力に表示する。
# 含まれるもの: policy / templates（.ja .en .ko）/ regions / tours など kb 配下すべて
#
# 補足: チャット UI 自体を Basic 認証で囲む例は docker-compose.auth-stack.yml + nginx/README.md

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
OUT="${1:-${ROOT}/deploy/gmtj-kb-for-knowledge.zip}"

cd "$ROOT"
rm -f "$OUT"
zip -rq "$OUT" kb \
  -x "kb/**/.DS_Store"

echo "Created: $OUT"
echo "Upload this zip in Open WebUI → Knowledge (see deploy/openwebui-knowledge.md)."
echo "Note: UI protection is separate — see deploy/docker-compose.auth-stack.yml if needed."
