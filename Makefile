.PHONY: help verify-templates kb-zip ci

help:
	@echo "Targets:"
	@echo "  make verify-templates  - kb/intents と kb/templates のファイル対応を検証"
	@echo "  make kb-zip            - kb を deploy/gmtj-kb-for-knowledge.zip にまとめる"
	@echo "  make ci                - ローカルで最低限の検証（いまは verify-templates のみ）"

verify-templates:
	@bash scripts/verify-kb-templates.sh

kb-zip:
	@bash deploy/package-kb-for-knowledge.sh

ci: verify-templates
