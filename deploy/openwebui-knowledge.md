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

**一括ZIP**: リポジトリルートで `bash deploy/package-kb-for-knowledge.sh` を実行すると、既定で `deploy/gmtj-kb-for-knowledge.zip` が生成される（パスを変えたい場合は第1引数で出力先を指定）。生成物を Knowledge にアップロードする。

### B. コンテナ内 `/kb-ro` を参照して手動コピー（上級者・検証用）

1. `docker compose exec open-webui sh` などでシェルに入る。
2. `/kb-ro` に `policy.md` 等が見えることを確認する。
3. Open WebUI がドキュメント取り込みに使うディレクトリ（通常はデータボリューム配下。詳細は [環境変数 DATA_DIR](https://docs.openwebui.com/reference/env-configuration)）へ、**運用ポリシーに沿って**必要ファイルだけをコピーするか、公式機能で「フォルダ取り込み」できる場合はその手順に従う。

読み取り専用マウント上のファイルを **直接** ベクタDBの入力パスとして指せるかは実装依存のため、**勤務手順書では A を正**とするのが安全。

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
