# Open WebUI × Anthropic（接続が「モデル 0」のとき）

対象: **`deploy/docker-compose.yml`** の Open WebUI v0.5.10 付近。**Anthropic は「OpenAI API」枠**で `https://api.anthropic.com/v1` を登録する構成。

## いま進める（チェックリスト）

1. **管理者パネル → 設定 → 接続 → OpenAI API**
2. **`https://api.openai.com/v1` でキーが空の行は削除**（残すと一覧取得が壊れやすい）
3. **`https://api.anthropic.com/v1` の行 → 歯車（Edit Connection）**
4. 次を埋めて **保存**:
   - **Key**: Anthropic の API キー（`.env` と同じで可）
   - **Prefix ID**: 任意。**空**でよい。複数プロバイダを並べるなら `anthropic` など
   - **Model IDs**: 下記を **1つずつ「＋」で追加**（手動指定しないと `GET /models` に依存し、`モデル 0` のままになりやすい）

### Model IDs のコピペ例（2026年時点・公式 ID は変わることがある）

まずは **1つだけ** でも動作確認できます。

| 用途の目安 | Model ID（例） |
|------------|----------------|
| まず試す（バランス） | `claude-sonnet-4-6` |
| 速さ重視 | Haiku 系は Anthropic の一覧で **現在の ID** を確認して追加 |
| 最高品質（コスト高め） | `claude-opus-4-7`（利用可否はプラン・地域による） |

※ 最新の正式な一覧は Anthropic の **[Models](https://platform.claude.com/docs/en/api/models)** または Console で確認してください。

5. **接続**画面で **Ollama API がオン**なら、Mac に Ollama が無いときは **オフ**推奨
6. **設定 → モデル** を開き、右上の **更新／取得** があれば実行 → **`モデル 0` が増えるか確認**
7. **チャット**で上記モデルを選び、「こんにちは」と送れるか確認

## うまくいかないとき

- **`deploy/SERVICE-LAUNCH.md`** のフェーズ2〜3
- ログ: `docker compose logs open-webui --tail 80`（キーを貼らない）

## 関連

- [openwebui-knowledge.md](./openwebui-knowledge.md)（Knowledge）
- [QUICKSTART-サービス開始.md](./QUICKSTART-サービス開始.md)
