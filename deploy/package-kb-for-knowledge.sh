#!/usr/bin/env bash
set -euo pipefail
# リポジトリルート（deploy の一つ上）から kb を ZIP 化する。
# 任意の RAG／ナレッジ取り込み先へ手動アップロードしやすいファイル名を標準出力に表示する。
# 含まれるもの: policy / templates（.ja .en .ko）/ regions / tours など kb 配下すべて
#
# 補足: Open WebUI を使う場合の手順は deploy/openwebui-knowledge.md。チャット UI を Basic 認証で囲む例は docker-compose.auth-stack.yml + nginx/README.md

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
OUT="${1:-${ROOT}/deploy/gmtj-kb-for-knowledge.zip}"
# Open WebUI などで「先頭が kb/ の ZIP」を拒否する場合があるため、kb 直下をルートとした ZIP も併せて出す。
OUT_OPENWEBUI="${ROOT}/deploy/gmtj-kb-for-openwebui.zip"

cd "$ROOT"
rm -f "$OUT" "$OUT_OPENWEBUI"
zip -rq "$OUT" kb \
  -x "kb/**/.DS_Store"

cd "$ROOT/kb"
zip -rq "$OUT_OPENWEBUI" . \
  -x ".DS_Store" \
  -x "*/.DS_Store" \
  -x "*/*/.DS_Store"

echo "Created: $OUT"
echo "Created: $OUT_OPENWEBUI  (paths without top-level kb/ — try this if Open WebUI shows \"Failed to add file\")"
echo "Use these zips for RAG / knowledge pipelines (optional: deploy/openwebui-knowledge.md for Open WebUI)."
echo "Note: UI protection is separate — see deploy/docker-compose.auth-stack.yml if needed."
