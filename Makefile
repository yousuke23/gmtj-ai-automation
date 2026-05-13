.PHONY: help verify-templates verify-golden kb-zip ci open-webui check-webui

help:
	@echo "Targets:"
	@echo "  make verify-templates  - kb/intents と kb/templates のファイル対応を検証"
	@echo "  make verify-golden     - eval/golden-questions.md の番号付き質問が下限以上か"
	@echo "  make kb-zip            - kb を deploy/gmtj-kb-for-knowledge.zip にまとめる"
	@echo "  make ci                - verify-templates + verify-golden"
	@echo "  make open-webui        - （任意）deploy/fast-up.sh で Open WebUI を起動（Docker 必須）"
	@echo "  make check-webui       - （任意）localhost:8080 が応答するか確認（Docker 必須）"
	@echo "  手順の説明（Docker 使う場合のみ）: deploy/QUICKSTART-サービス開始.md"

check-webui:
	@bash deploy/check-service.sh

open-webui:
	@bash deploy/fast-up.sh

verify-templates:
	@bash scripts/verify-kb-templates.sh

verify-golden:
	@bash scripts/verify-golden-questions.sh

kb-zip:
	@bash deploy/package-kb-for-knowledge.sh

ci: verify-templates verify-golden
