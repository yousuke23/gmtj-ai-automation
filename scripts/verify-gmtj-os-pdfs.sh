#!/usr/bin/env bash
# GMTJ OS3 系 PDF（デスクトップの GMTJ OS フォルダ）が揃っているか確認する。
set -euo pipefail
ROOT="${GMTJ_OS_ROOT:-/Users/tarnar/Desktop/GMTJ OS}"
MISS=0
for i in $(seq 1 10); do
  f="$ROOT/GMTJ OS3_${i}.pdf"
  if [[ -f "$f" ]]; then
    echo "OK  $f"
  else
    echo "MISSING  $f"
    MISS=1
  fi
done
if [[ "$MISS" -ne 0 ]]; then
  echo "一部ファイルがありません。フォルダ名・ファイル名を確認してください。" >&2
  exit 1
fi
echo "verify-gmtj-os-pdfs: OK (10 files)"
