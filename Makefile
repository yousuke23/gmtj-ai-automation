.PHONY: help verify-templates verify-golden kb-zip ci

help:
	@echo "Targets:"
	@echo "  make verify-templates  - kb/intents と kb/templates のファイル対応を検証"
	@echo "  make verify-golden     - eval/golden-questions.md の番号付き質問が下限以上か"
	@echo "  make kb-zip            - kb を deploy/gmtj-kb-for-knowledge.zip にまとめる"
	@echo "  make ci                - verify-templates + verify-golden"
	@echo "  Open WebUI 起動手順: deploy/QUICKSTART-サービス開始.md（Docker 必須）"

verify-templates:
	@bash scripts/verify-kb-templates.sh

verify-golden:
	@bash scripts/verify-golden-questions.sh

kb-zip:
	@bash deploy/package-kb-for-knowledge.sh

ci: verify-templates verify-golden
