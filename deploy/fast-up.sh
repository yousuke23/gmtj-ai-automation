#!/usr/bin/env bash
# Open WebUI を最速で起動する（Docker Desktop 起動済みが前提）
set -euo pipefail
DEPLOY_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$DEPLOY_DIR"

if ! command -v docker >/dev/null 2>&1; then
  echo "docker が見つかりません。Docker Desktop をインストールして起動してください。" >&2
  exit 1
fi

if [[ ! -f .env ]]; then
  cp .env.example .env
  echo "Created .env from .env.example"
fi

python3 <<'PY'
import pathlib, re, secrets
p = pathlib.Path(".env")
text = p.read_text(encoding="utf-8")
lines = text.splitlines()
key_ok = False
for line in lines:
    if line.startswith("WEBUI_SECRET_KEY="):
        val = line.split("=", 1)[1].strip()
        if val and val != "change-me-long-random-string":
            key_ok = True
        break
if not key_ok:
    sec = secrets.token_hex(32)
    out = []
    replaced = False
    for line in lines:
        if line.startswith("WEBUI_SECRET_KEY="):
            out.append(f"WEBUI_SECRET_KEY={sec}")
            replaced = True
        else:
            out.append(line)
    if not replaced:
        out.insert(0, f"WEBUI_SECRET_KEY={sec}")
    p.write_text("\n".join(out) + "\n", encoding="utf-8")
    print("Set WEBUI_SECRET_KEY to a new random value (was placeholder or missing).")
PY

echo "Starting containers..."
docker compose up -d

echo ""
echo "OK — Open in browser: http://127.0.0.1:8080"
echo "First visit: create admin account (or sign in if data already exists)."
echo "Next: deploy/SERVICE-LAUNCH.md for Knowledge / smoke checks."
