# 用語集（超ざっくり）

このリポジトリのドキュメントでよく出る言葉。**厳密なIT定義ではなく**、初心者が読むためのメモです。

| 用語 | ざっくり意味 |
|------|----------------|
| **GMTJ** | Global Music Tourism Japan。本プロジェクトの母体。 |
| **14（コンシェルジュ）** | 観光・音楽ツーリズム系の問い合わせに答える AI ナビ／一次対応の想定プロダクト。 |
| **01（ツアー）** | 英語インバウンド向けミュージックツアー商品。`tour/` にゲスト文・Runbook。 |
| **18（マーケ）** | 横断マーケ。`marketing/` にカレンダー案・KW 種など。 |
| **`kb/`** | AI が読む **ナレッジとルール**（policy・テンプレ・地域メモ等）。 |
| **意図（intent）** | ユーザーの質問の種類分け。`kb/intents.yaml` に一覧。 |
| **テンプレ** | 意図ごとの「答え方の型」。`kb/templates/` の `.ja` `.en` `.ko`。 |
| **ゴールデン質問** | 品質テスト用の決まった質問セット。`eval/golden-questions.md`。 |
| **ルーブリック** | 採点の基準。`eval/scoring-rubric.md`。 |
| **RAG / Knowledge** | チャット前にドキュメントを検索して回答に足す仕組み。**運用方針で Open WebUI を使わない場合は概念としてのみ**（実装は別システムでも可）。 |
| **Open WebUI** | ブラウザで使うチャット UI の OSS。**当面は使わない**運用なら無視してよい（`deploy/` は任意参照）。 |
| **Basic 認証** | ブラウザのユーザー名・パスワード入力で入口をふさぐ簡易ガード。 |
| **TLS / HTTPS** | 通信の暗号化。`deploy/docker-compose.caddy-tls.yml` は社内検証用の例。 |
| **コンテンツ柱** | マーケの3つの方向性（音楽×土地・安全・公式ファースト）。`marketing/content-pillars.md`。 |
| **完了の定義（スプリント）** | `CLAUDE.md` に書いた「当面スプリント完了」の条件（14・01・18 + `make ci` 等）。 |
| **作業の優先順** | このリポでは **14 → 01 → 18** でナレッジを厚くする合意。`docs/README.md`。 |

詳しい事業一覧は [business-map.md](./business-map.md)、作業ルールと完了定義はルートの **`CLAUDE.md`**。**`docs/` の目次**は [README.md](./README.md)。マーケの柱は [../marketing/content-pillars.md](../marketing/content-pillars.md)、ツアー参加前チェックは [../tour/checklist-packing-izu-san.md](../tour/checklist-packing-izu-san.md)。
