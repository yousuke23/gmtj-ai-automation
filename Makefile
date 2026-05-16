.PHONY: help verify-templates verify-golden verify-gmtj-os-pdfs kb-zip ci open-webui check-webui openwebui-kb-prune-help site-dev generate-business-portals

help:
	@echo "Targets:"
	@echo "  make verify-templates  - kb/intents と kb/templates のファイル対応を検証"
	@echo "  make verify-gmtj-os-pdfs - デスクトップ GMTJ OS の OS3 PDF 10件の存在確認（パス固定）"
	@echo "  make kb-zip            - kb を ZIP 化（汎用 + Open WebUI 向けフラットの2種）"
	@echo "  make ci                - verify-templates + verify-golden"
	@echo "  make open-webui        - （任意）deploy/fast-up.sh で Open WebUI を起動（Docker 必須）"
	@echo "  make check-webui       - （任意）localhost:8080 が応答するか確認（Docker 必須）"
	@echo "  make openwebui-kb-prune-help - Knowledge がリポ全体のときの API 整理スクリプトの使い方表示"
	@echo "  make site-dev          - サービスサイト + AIチャット試用の起動コマンド表示"
	@echo "  手順の説明（Docker 使う場合のみ）: deploy/QUICKSTART-サービス開始.md"

check-webui:
	@bash deploy/check-service.sh

open-webui:
	@bash deploy/fast-up.sh

verify-templates:
	@bash scripts/verify-kb-templates.sh

verify-golden:
	@bash scripts/verify-golden-questions.sh

verify-gmtj-os-pdfs:
	@bash scripts/verify-gmtj-os-pdfs.sh

kb-zip:
	@bash deploy/package-kb-for-knowledge.sh

openwebui-kb-prune-help:
	@echo "Knowledge にリポ全体が入ったとき: deploy/openwebui-knowledge.md の「C. リポジトリ全体が…」"
	@echo "例: export OPENWEBUI_API_KEY=\"...\" && python3 deploy/scripts/prune_openwebui_knowledge_kb_only.py --list"
	@echo "ドライラン: ... --match-name \"コンシェルジュ\" --dry-run   実行: ... --apply"

site-dev:
	@echo "【本番チャット】Netlify デプロイ後、トップの AIコンシェルジュは /.netlify/functions/gmtj-chat を利用します（ANTHROPIC_API_KEY を Netlify に設定）。"
	@echo "【ローカル開発（任意）】Anthropic: ANTHROPIC_API_KEY=sk-ant-... python3 site/chat-proxy.py"
	@echo "【ローカル開発（任意）】Ollama: ollama serve → ollama pull llama3.2 → USE_OLLAMA=1 python3 site/chat-proxy.py"
	@echo "【静的確認】python3 -m http.server 8888 → http://127.0.0.1:8888/site/"

ci: verify-templates verify-golden

generate-business-portals:
	@python3 scripts/build_tarnar_izu_blog_pages.py
	@python3 scripts/generate_business_portals.py
