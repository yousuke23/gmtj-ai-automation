# Open WebUI — `kb` を Knowledge（RAG）に載せる手順（社内MVP）

対象: `deploy/docker-compose.yml` で起動する Open WebUI。UI はバージョンで文言が変わるため、**画面は公式ドキュメントと併読**すること。

**Anthropic をつないでも「モデル 0」になる場合:** **[openwebui-anthropic-connection.md](./openwebui-anthropic-connection.md)**（空の OpenAI 接続の削除・**Model IDs 手動追加**・Prefix ID）。

**パイロットの全体チェックリスト（ZIP 済み・ブラウザ手動含む）:** **[PILOT-OpenWebUI-やること一覧.md](./PILOT-OpenWebUI-やること一覧.md)**

## 1. マウントの確認

ホストの `kb/` はコンテナ内 **`/kb-ro`**（読み取り専用）にマウントされている。

```bash
cd deploy
docker compose exec open-webui ls -la /kb-ro
```

ファイルが見えない場合は `docker-compose.yml` の相対パス（`../kb`）と、compose を実行したカレントディレクトリが `deploy/` であることを確認する。

## 2. Knowledge への取り込み方（現実的な2経路）

Open WebUI はバージョンにより「サーバー上のパスをそのまま Knowledge 化」する UI が **ある／ない** の差がある。社内MVPでは次のどちらか（または併用）を推奨する。

### A. UI からアップロード（最も互換性が高い）

1. 管理ユーザーでログインする。
2. **Workspace → Knowledge**（または同等メニュー）でナレッジコレクションを新規作成する（例: `GMTJ-kb`）。
3. `kb` 配下の `.md` / `.yaml` 等を、**ファイル選択または ZIP** でアップロードする。
4. 埋め込みモデル（Embedding）が未設定の場合は、公式手順に従い API またはローカルモデルを設定する（`OFFLINE_MODE` 時は注意）。

**一括ZIP**: リポジトリルートで `make kb-zip`（または `bash deploy/package-kb-for-knowledge.sh`）を実行すると次の2つが生成される。

| ファイル | 内容 |
|----------|------|
| `deploy/gmtj-kb-for-knowledge.zip` | アーカイブ先頭が `kb/`（汎用パイプライン向け） |
| `deploy/gmtj-kb-for-openwebui.zip` | **`kb` の直下を ZIP ルート**（`regions/foo.md` など。Open WebUI で失敗しやすい場合はこちらを試す） |

第1引数で出力先を変えられるのは **汎用 ZIP のみ**（Open WebUI 用は常に `deploy/gmtj-kb-for-openwebui.zip`）。

**ZIP が必ずエラーになる版:** Knowledge の **「+」メニュー → アップロードディレクトリ（Upload Directory）」** を使い、Finder でリポジトリの **`kb` フォルダそのもの**（例: `GMTJ-AI-Automation/kb`）を指定する。ZIP にせず **ディレクトリ単位**だと通ることが多い。別の場所に置きたい場合は `gmtj-kb-for-openwebui.zip` を解凍したフォルダを指定してもよい。

**「Failed to add file.」のとき:** まず上記の **ディレクトリアップロード**、または **アップロードファイル**で `.md` を複数選択。ZIP は諦めてよい。原因切り分けは `cd deploy && docker compose logs open-webui --tail 80` でサーバー側エラーを確認する。**埋め込み（Embedding）未設定**の場合も取り込みに失敗することがある（管理画面の RAG／埋め込み設定を確認）。

### B. コンテナ内 `/kb-ro` を参照して手動コピー（上級者・検証用）

1. `docker compose exec open-webui sh` などでシェルに入る。
2. `/kb-ro` に `policy.md` 等が見えることを確認する。
3. Open WebUI がドキュメント取り込みに使うディレクトリ（通常はデータボリューム配下。詳細は [環境変数 DATA_DIR](https://docs.openwebui.com/reference/env-configuration)）へ、**運用ポリシーに沿って**必要ファイルだけをコピーするか、公式機能で「フォルダ取り込み」できる場合はその手順に従う。

読み取り専用マウント上のファイルを **直接** ベクタDBの入力パスとして指せるかは実装依存のため、**勤務手順書では A を正**とするのが安全。

### C. リポジトリ全体が Knowledge に入ってしまったとき（API で `kb` 以外を一括削除）

ブラウザで1件ずつ消す代わりに、**ローカルで API を叩いて**「ファイルの `path` に `/kb/` が含まれないもの」だけをコレクションから外すスクリプトがある（`deploy/docker-compose.yml` の **Open WebUI v0.5.10** と同じ API 前提）。

1. Open WebUI に **管理者相当**でログインできるユーザーから **API キー**を発行する（画面: **設定 → アカウント** 付近。版により文言が異なる）。
2. リポジトリルートで次を実行する。

```bash
export OPENWEBUI_API_KEY="（発行したキー）"
export OPENWEBUI_URL="http://127.0.0.1:8080"   # 省略可

python3 deploy/scripts/prune_openwebui_knowledge_kb_only.py --list
python3 deploy/scripts/prune_openwebui_knowledge_kb_only.py --match-name "コンシェルジュ" --dry-run
python3 deploy/scripts/prune_openwebui_knowledge_kb_only.py --match-name "コンシェルジュ" --apply
```

`--match-name` で複数コレクションに当たる場合はエラーにするので、そのときは **`--knowledge-id`**（`--list` の1列目）で明示する。

**注意（重要）:** この Open WebUI 版の **`file/remove` はファイル本体も削除する**実装になっている。スクリプトは **`path` に `/kb/` を含むものだけ保持**し、**`path` が空のファイルは誤削除防止のため触らない**（一覧に SKIP として出る）。取り込み時のメタデータによっては手動整理が必要。

## 3. `kb` を更新したあと

- UI 取り込み方式の場合: 差分ファイルを **再アップロード**し、該当ナレッジの **再インデックス／再処理**（UI にあれば実行）を行う。
- 回答に **古い前提** が残る場合は、チャット側の「Knowledge を参照する」設定と、モデルキャッシュを含めて切り分ける。
- 社内で **HTTPS** まで揃えたい場合は `deploy/caddy/README.md`（Caddy 例）を参照。ナレッジ ZIP とは別レイヤー。
- `eval/golden-questions.md` の**番号付き質問を増減**したら、リポジトリルートで `make verify-golden`（または `MIN_GOLDEN=…`）が通るよう **`scripts/verify-golden-questions.sh` の既定下限**と CI を揃える。

## 4. セキュリティ・ポリシー

- 公開前は `deploy/README.md` のとおり **VPN / Basic 認証 / IP 制限**で囲む。
- `kb/policy.md` に反する個人情報や秘密は Knowledge に **載せない**。
- ログにパスポート番号・決済情報を残さない。

## 5. 参考リンク

- [Open WebUI — Environment variables](https://docs.openwebui.com/reference/env-configuration)（`DATA_DIR`、`RAG_*`、`VECTOR_DB` 等）
