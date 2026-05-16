#!/usr/bin/env python3
"""
Open WebUI (v0.5.x 想定) の Knowledge コレクションから、
パス上「kb」フォルダ配下にないファイルだけを API 経由で取り除く。

file/remove は当該ファイルをシステムからも削除する実装のため、
誤って kb 配下を消さないようパス判定を厳密にする。

使い方:
  export OPENWEBUI_API_KEY="..."   # ブラウザ: 設定 → アカウント → API キー 等
  python3 deploy/scripts/prune_openwebui_knowledge_kb_only.py --list
  python3 deploy/scripts/prune_openwebui_knowledge_kb_only.py --match-name "コンシェルジュ" --dry-run
  python3 deploy/scripts/prune_openwebui_knowledge_kb_only.py --knowledge-id "<id>" --apply

環境変数:
  OPENWEBUI_URL   既定 http://127.0.0.1:8080
  OPENWEBUI_API_KEY  必須（--list 以外でも推奨）
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.request
from typing import Any


def _norm(p: str) -> str:
    return p.replace("\\", "/")


def file_is_under_kb(path: str | None, filename: str | None) -> bool:
    """
    アップロード元が .../GMTJ-AI-Automation/kb/... のとき path に /kb/ が含まれる想定。
    path が空のときは誤削除を避け、kb 配下とみなさない（手動確認用に残す）。
    """
    p = _norm((path or "").strip())
    fn = (filename or "").strip()
    if not p and not fn:
        return False
    combined = _norm(f"{p}/{fn}" if p and fn else (p or fn))
    if "/kb/" in combined:
        return True
    # 稀に path が "kb/..." のように先頭から始まる
    if combined.startswith("kb/"):
        return True
    return False


def http_json(
    method: str,
    url: str,
    token: str,
    body: dict[str, Any] | None = None,
    timeout: int = 120,
) -> Any:
    data_bytes = None
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json",
    }
    if body is not None:
        data_bytes = json.dumps(body).encode("utf-8")
        headers["Content-Type"] = "application/json"
    req = urllib.request.Request(url, data=data_bytes, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            raw = resp.read().decode("utf-8", errors="replace")
            if not raw.strip():
                return None
            return json.loads(raw)
    except urllib.error.HTTPError as e:
        err_body = e.read().decode("utf-8", errors="replace")
        raise SystemExit(f"HTTP {e.code} {method} {url}\n{err_body}") from e


def pick_knowledge(
    bases: list[dict[str, Any]], knowledge_id: str | None, match_name: str | None
) -> dict[str, Any]:
    if knowledge_id:
        for kb in bases:
            if kb.get("id") == knowledge_id:
                return kb
        raise SystemExit(f"knowledge id が見つかりません: {knowledge_id}")
    if match_name:
        m = match_name.casefold()
        hits = [kb for kb in bases if m in (kb.get("name") or "").casefold()]
        if not hits:
            raise SystemExit(f"name に '{match_name}' を含むコレクションがありません。")
        if len(hits) > 1:
            names = ", ".join(f"{kb.get('name')}({kb.get('id')})" for kb in hits)
            raise SystemExit(f"複数ヒットしました。--knowledge-id で指定してください: {names}")
        return hits[0]
    raise SystemExit("--knowledge-id または --match-name のどちらかが必要です。")


def main() -> None:
    parser = argparse.ArgumentParser(description="Open WebUI Knowledge を kb 配下だけに整理")
    parser.add_argument(
        "--url",
        default=os.environ.get("OPENWEBUI_URL", "http://127.0.0.1:8080"),
        help="Open WebUI のベース URL",
    )
    parser.add_argument(
        "--token",
        default=os.environ.get("OPENWEBUI_API_KEY", ""),
        help="API キー（未指定時は環境変数 OPENWEBUI_API_KEY）",
    )
    parser.add_argument("--list", action="store_true", help="Knowledge 一覧を表示して終了")
    parser.add_argument("--knowledge-id", default=None, help="対象コレクションの ID")
    parser.add_argument("--match-name", default=None, help="コレクション名の部分一致（先頭1件）")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        default=True,
        help="削除せず一覧のみ（既定）",
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="実際に file/remove を実行する",
    )
    args = parser.parse_args()
    if args.apply:
        args.dry_run = False

    base = args.url.rstrip("/")
    token = (args.token or "").strip()
    if not token:
        raise SystemExit("OPENWEBUI_API_KEY または --token が必要です。")

    list_url = f"{base}/api/v1/knowledge/"
    bases = http_json("GET", list_url, token)
    if not isinstance(bases, list):
        raise SystemExit(f"想定外の応答: {bases!r}")

    if args.list:
        for kb in bases:
            n = len((kb.get("files") or []) if isinstance(kb.get("files"), list) else [])
            print(f"{kb.get('id')}\t{n} files\t{kb.get('name')}")
        return

    kb_summary = pick_knowledge(bases, args.knowledge_id, args.match_name)
    kid = kb_summary["id"]
    detail_url = f"{base}/api/v1/knowledge/{kid}"
    detail = http_json("GET", detail_url, token)
    if not isinstance(detail, dict):
        raise SystemExit(f"想定外の応答: {detail!r}")

    files = detail.get("files") or []
    if not isinstance(files, list):
        raise SystemExit("files フィールドがありません（Open WebUI の版が異なる可能性）。")

    remove: list[dict[str, Any]] = []
    keep: list[dict[str, Any]] = []
    ambiguous: list[dict[str, Any]] = []

    for f in files:
        if not isinstance(f, dict):
            continue
        fid = f.get("id")
        fn = f.get("filename") or ""
        path = f.get("path")
        if file_is_under_kb(path, fn):
            keep.append(f)
        else:
            if not (path or "").strip():
                ambiguous.append(f)
            else:
                remove.append(f)

    print(f"コレクション: {detail.get('name')}  (id={kid})")
    print(f"保持（kb 配下と判定）: {len(keep)} 件")
    print(f"削除候補（kb 外）: {len(remove)} 件")
    if ambiguous:
        print(
            f"注意: path が空で判定不能なためスキップ: {len(ambiguous)} 件（手動で要確認）",
            file=sys.stderr,
        )
        for f in ambiguous:
            print(f"  SKIP id={f.get('id')} filename={f.get('filename')!r}", file=sys.stderr)

    for f in remove:
        p = f.get("path") or ""
        print(f"  REMOVE {f.get('id')}\t{p}\t{f.get('filename')}")

    if args.dry_run:
        print("\nドライランのみ。実行するには同じ引数に --apply を付けて再実行してください。")
        return

    for i, f in enumerate(remove):
        fid = f.get("id")
        if not fid:
            continue
        url = f"{base}/api/v1/knowledge/{kid}/file/remove"
        http_json("POST", url, token, body={"file_id": fid})
        print(f"removed {i + 1}/{len(remove)} file_id={fid}")
        time.sleep(0.15)

    print("完了。")


if __name__ == "__main__":
    main()
