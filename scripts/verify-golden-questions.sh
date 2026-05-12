#!/usr/bin/env bash
set -euo pipefail
# eval/golden-questions.md 内の「番号付き質問」行数が下限以上か確認する。
# 使い方: リポジトリルートで bash scripts/verify-golden-questions.sh
# 下限を変える: MIN_GOLDEN=30 bash scripts/verify-golden-questions.sh

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

FILE="eval/golden-questions.md"
MIN="${MIN_GOLDEN:-26}"

if [[ ! -f "$FILE" ]]; then
  echo "error: missing $FILE" >&2
  exit 1
fi

# 行頭（空白可）の「数字. 」で始まる質問行を数える（採点メモ見出しは "## " のため除外されやすい）
count=$(grep -E '^[[:space:]]*[0-9]+\.[[:space:]]' "$FILE" | wc -l | tr -d '[:space:]')

if [[ -z "$count" || ! "$count" =~ ^[0-9]+$ ]]; then
  echo "error: could not count golden questions" >&2
  exit 1
fi

if [[ "$count" -lt "$MIN" ]]; then
  echo "error: golden question lines=$count (expected >= $MIN). Update eval/golden-questions.md or MIN_GOLDEN." >&2
  exit 1
fi

echo "verify-golden-questions: OK ($count numbered questions, MIN_GOLDEN=$MIN)"
