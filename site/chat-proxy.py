#!/usr/bin/env python3
"""
ローカル開発用: サービスサイトのチャットを Anthropic API または Ollama に中継する。

【Anthropic】
  ANTHROPIC_API_KEY=sk-ant-... python3 site/chat-proxy.py

【Ollama（課金なし・ローカル）】
  USE_OLLAMA=1 python3 site/chat-proxy.py
  # 事前に: ollama serve ＋ ollama pull llama3.2 など

- 既定で http://127.0.0.1:8765 のみにバインド（インターネットに晒さないこと）。
- CORS は開発向けに緩い。**本番公開前に必ず認証・TLS・レート制限を別途設けること。**

環境変数:
  USE_OLLAMA         1 / true / yes のとき Ollama を使用（Anthropic キー不要）
  OLLAMA_BASE_URL    省略時 http://127.0.0.1:11434
  OLLAMA_MODEL       省略時 llama3.2

  ANTHROPIC_API_KEY  USE_OLLAMA が無効なとき必須
  ANTHROPIC_MODEL    省略時 claude-3-5-haiku-20241022
  CHAT_PROXY_HOST    省略時 127.0.0.1
  CHAT_PROXY_PORT    省略時 8765
"""

from __future__ import annotations

import json
import os
import ssl
import sys
import urllib.error
import urllib.request
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse

ANTHROPIC_URL = "https://api.anthropic.com/v1/messages"
ANTHROPIC_VERSION = "2023-06-01"

SYSTEM = """あなたは「Japan Music Tourism / GMTJ」関連の公式サイト上の案内アシスタントです。
音楽と旅行・地域体験に関する一般的な案内を、日本語で丁寧に行ってください。
個人情報の収集は求めないでください。確定的な医療・法律・投資判断は避け、必要なら専門家への相談を促してください。
具体的な予約・決済・キャンセルはメール窓口（123@atono.jp）へ案内してください。
"""


def _ascii_only(s: str) -> str:
    """HTTP ヘッダーは latin-1 のみ。API キーに全角・特殊引用符が混ざると urllib が失敗する。"""
    return "".join(c for c in (s or "") if ord(c) < 128).strip()


def _truthy(v: str | None) -> bool:
    if not v:
        return False
    return v.strip().lower() in ("1", "true", "yes", "on")


def _cors_headers(handler: BaseHTTPRequestHandler) -> None:
    handler.send_header("Access-Control-Allow-Origin", "*")
    handler.send_header("Access-Control-Allow-Methods", "POST, OPTIONS")
    handler.send_header("Access-Control-Allow-Headers", "Content-Type")
    handler.send_header("Access-Control-Max-Age", "86400")


def _ollama_reply(messages: list[dict]) -> tuple[str | None, str | None]:
    """Ollama /api/chat を呼ぶ。(reply, error_message) error 時 reply は None"""
    base = (os.environ.get("OLLAMA_BASE_URL") or "http://127.0.0.1:11434").rstrip("/")
    model = _ascii_only(os.environ.get("OLLAMA_MODEL", "llama3.2")) or "llama3.2"
    ollama_messages = [{"role": "system", "content": SYSTEM}] + messages
    body = {
        "model": model,
        "messages": ollama_messages,
        "stream": False,
    }
    data = json.dumps(body, ensure_ascii=True).encode("utf-8")
    url = base + "/api/chat"
    parsed = urlparse(url)
    ctx = None
    if parsed.scheme == "https":
        ctx = ssl.create_default_context()
    req = urllib.request.Request(
        url,
        data=data,
        method="POST",
        headers={"Content-Type": "application/json; charset=utf-8"},
    )
    try:
        if ctx is not None:
            opener = urllib.request.urlopen(req, timeout=300, context=ctx)
        else:
            opener = urllib.request.urlopen(req, timeout=300)
        with opener as resp:
            res_json = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        err = e.read().decode("utf-8", errors="replace")
        return None, f"Ollama HTTP {e.code}: {err[:800]}"
    except urllib.error.URLError as e:
        return None, f"Ollama に接続できません（`ollama serve` とモデル pull を確認）: {e}"
    except Exception as e:
        return None, f"Ollama 接続エラー: {e}"

    if res_json.get("error"):
        return None, f"Ollama: {res_json.get('error')}"
    msg = res_json.get("message") or {}
    content = msg.get("content")
    if isinstance(content, str):
        return content.strip() or "（空の応答でした）", None
    return None, "Ollama の応答形式が想定外です。"


def _anthropic_reply(key: str, messages: list[dict]) -> tuple[str | None, str | None]:
    model = _ascii_only(os.environ.get("ANTHROPIC_MODEL", "claude-3-5-haiku-20241022"))
    if not model:
        model = "claude-3-5-haiku-20241022"
    body_out = {
        "model": model,
        "max_tokens": 1024,
        "system": SYSTEM,
        "messages": messages,
    }
    data = json.dumps(body_out, ensure_ascii=True).encode("utf-8")
    req = urllib.request.Request(
        ANTHROPIC_URL,
        data=data,
        method="POST",
        headers={
            "Content-Type": "application/json; charset=utf-8",
            "x-api-key": key,
            "anthropic-version": ANTHROPIC_VERSION,
        },
    )
    ctx = ssl.create_default_context()
    try:
        with urllib.request.urlopen(req, timeout=120, context=ctx) as resp:
            res_json = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        err = e.read().decode("utf-8", errors="replace")
        hint = ""
        if "credit balance is too low" in err.lower():
            hint = (
                " 【対処】課金なしで試す: プロキシを Ctrl+C で止め、"
                "`unset ANTHROPIC_API_KEY` のあと "
                "`USE_OLLAMA=1 python3 site/chat-proxy.py`（事前に `ollama serve` と `ollama pull llama3.2`）"
            )
        return None, f"Anthropic API エラー: {e.code} {err[:600]}{hint}"
    except Exception as e:
        return None, f"接続エラー: {e}"

    blocks = res_json.get("content") or []
    text_parts: list[str] = []
    for b in blocks:
        if isinstance(b, dict) and b.get("type") == "text":
            t = b.get("text")
            if isinstance(t, str):
                text_parts.append(t)
    reply = "\n".join(text_parts).strip() or "（空の応答でした）"
    return reply, None


class Handler(BaseHTTPRequestHandler):
    def log_message(self, fmt: str, *args) -> None:
        sys.stderr.write("%s - %s\n" % (self.address_string(), fmt % args))

    def do_GET(self) -> None:
        if self.path in ("/health", "/api/health"):
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            _cors_headers(self)
            self.end_headers()
            self.wfile.write(b'{"ok":true}')
            return
        self.send_error(404)

    def do_OPTIONS(self) -> None:
        if self.path != "/api/site-chat":
            self.send_error(404)
            return
        self.send_response(204)
        _cors_headers(self)
        self.end_headers()

    def do_POST(self) -> None:
        if self.path != "/api/site-chat":
            self.send_error(404)
            return

        use_ollama = _truthy(os.environ.get("USE_OLLAMA"))
        key = _ascii_only(os.environ.get("ANTHROPIC_API_KEY", ""))

        if not use_ollama and not key:
            body = json.dumps(
                {
                    "error": "Anthropic を使う場合は ANTHROPIC_API_KEY を設定するか、Ollama を使う場合は USE_OLLAMA=1 を付けて起動してください。",
                },
                ensure_ascii=False,
            ).encode("utf-8")
            self.send_response(503)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            _cors_headers(self)
            self.end_headers()
            self.wfile.write(body)
            return

        length = int(self.headers.get("Content-Length", "0") or 0)
        raw = self.rfile.read(length) if length > 0 else b"{}"
        try:
            payload = json.loads(raw.decode("utf-8"))
        except json.JSONDecodeError:
            self._json_error(400, "JSON が不正です。")
            return

        messages_in = payload.get("messages")
        if not isinstance(messages_in, list) or not messages_in:
            self._json_error(400, "messages が必要です。")
            return

        messages: list[dict] = []
        for m in messages_in[-12:]:
            if not isinstance(m, dict):
                continue
            role = m.get("role")
            content = m.get("content")
            if role not in ("user", "assistant") or not isinstance(content, str):
                continue
            content = content.strip()
            if not content:
                continue
            messages.append({"role": role, "content": content[:12000]})

        if not messages or messages[-1]["role"] != "user":
            self._json_error(400, "最後のメッセージは user である必要があります。")
            return

        if use_ollama:
            reply, err = _ollama_reply(messages)
        else:
            reply, err = _anthropic_reply(key, messages)

        if err:
            self._json_error(502, err)
            return
        assert reply is not None

        out = json.dumps({"reply": reply}, ensure_ascii=False).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        _cors_headers(self)
        self.end_headers()
        self.wfile.write(out)

    def _json_error(self, code: int, msg: str) -> None:
        body = json.dumps({"error": msg}, ensure_ascii=False).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        _cors_headers(self)
        self.end_headers()
        self.wfile.write(body)


def main() -> None:
    host = os.environ.get("CHAT_PROXY_HOST", "127.0.0.1")
    port = int(os.environ.get("CHAT_PROXY_PORT", "8765"))
    use_ollama = _truthy(os.environ.get("USE_OLLAMA"))
    mode = "Ollama" if use_ollama else "Anthropic"
    if use_ollama:
        print(
            f"バックエンド: Ollama  model={os.environ.get('OLLAMA_MODEL', 'llama3.2')}  base={os.environ.get('OLLAMA_BASE_URL', 'http://127.0.0.1:11434')}"
        )
    else:
        print("バックエンド: Anthropic（残高エラーが出る場合は `unset ANTHROPIC_API_KEY` して `USE_OLLAMA=1` で再起動）")
    httpd = HTTPServer((host, port), Handler)
    print(f"site chat proxy ({mode}): http://{host}:{port}/api/site-chat (Ctrl+C で停止)")
    httpd.serve_forever()


if __name__ == "__main__":
    main()
