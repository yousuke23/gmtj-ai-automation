#!/usr/bin/env bash
set -euo pipefail
# kb/intents.yaml の各 id に対し kb/templates/{id}.ja.md .en.md .ko.md が存在するか検証する。
# 使い方: リポジトリルートで bash scripts/verify-kb-templates.sh
# 韓国語を必須にしない場合: REQUIRE_KO=0 bash scripts/verify-kb-templates.sh

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

REQUIRE_KO="${REQUIRE_KO:-1}"

TMP="$(mktemp)"
grep -E '^[[:space:]]+-[[:space:]]+id:' kb/intents.yaml | sed -E 's/^[[:space:]]+-[[:space:]]+id:[[:space:]]+//; s/[[:space:]]+$//' >"$TMP"

if [[ ! -s "$TMP" ]]; then
  rm -f "$TMP"
  echo "error: no intent ids found in kb/intents.yaml" >&2
  exit 1
fi

ERR=0
COUNT=0
while IFS= read -r id; do
  COUNT=$((COUNT + 1))
  for lang in ja en; do
    f="kb/templates/${id}.${lang}.md"
    if [[ ! -f "$f" ]]; then
      echo "MISSING $f" >&2
      ERR=1
    fi
  done
  if [[ "$REQUIRE_KO" == "1" ]]; then
    fk="kb/templates/${id}.ko.md"
    if [[ ! -f "$fk" ]]; then
      echo "MISSING $fk (set REQUIRE_KO=0 to allow omit)" >&2
      ERR=1
    fi
  fi
done <"$TMP"
rm -f "$TMP"

if [[ "$ERR" -ne 0 ]]; then
  echo "verify-kb-templates: failed" >&2
  exit 1
fi

echo "verify-kb-templates: OK (${COUNT} intents, REQUIRE_KO=${REQUIRE_KO})"
