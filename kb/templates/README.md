# 返答テンプレ一覧（`kb/intents.yaml` と対応）

| intent id | JA | EN | KO（任意） |
|-----------|----|----|----|
| `itinerary_music_tourism` | [itinerary_music_tourism.ja.md](./itinerary_music_tourism.ja.md) | [itinerary_music_tourism.en.md](./itinerary_music_tourism.en.md) | [itinerary_music_tourism.ko.md](./itinerary_music_tourism.ko.md) |
| `transport_access` | [transport_access.ja.md](./transport_access.ja.md) | [transport_access.en.md](./transport_access.en.md) | [transport_access.ko.md](./transport_access.ko.md) |
| `lodging_booking` | [lodging_booking.ja.md](./lodging_booking.ja.md) | [lodging_booking.en.md](./lodging_booking.en.md) | [lodging_booking.ko.md](./lodging_booking.ko.md) |
| `shrine_etiquette_safety` | [shrine_etiquette_safety.ja.md](./shrine_etiquette_safety.ja.md) | [shrine_etiquette_safety.en.md](./shrine_etiquette_safety.en.md) | [shrine_etiquette_safety.ko.md](./shrine_etiquette_safety.ko.md) |
| `events_festivals` | [events_festivals.ja.md](./events_festivals.ja.md) | [events_festivals.en.md](./events_festivals.en.md) | [events_festivals.ko.md](./events_festivals.ko.md) |
| `escalation_human` | [escalation_human.ja.md](./escalation_human.ja.md) | [escalation_human.en.md](./escalation_human.en.md) | [escalation_human.ko.md](./escalation_human.ko.md) |
| `official_tourism_info` | [official_tourism_info.ja.md](./official_tourism_info.ja.md) | [official_tourism_info.en.md](./official_tourism_info.en.md) | [official_tourism_info.ko.md](./official_tourism_info.ko.md) |
| `gmtj_contact_booking` | [gmtj_contact_booking.ja.md](./gmtj_contact_booking.ja.md) | [gmtj_contact_booking.en.md](./gmtj_contact_booking.en.md) | [gmtj_contact_booking.ko.md](./gmtj_contact_booking.ko.md) |
| `accessibility_mobility` | [accessibility_mobility.ja.md](./accessibility_mobility.ja.md) | [accessibility_mobility.en.md](./accessibility_mobility.en.md) | [accessibility_mobility.ko.md](./accessibility_mobility.ko.md) |

意図を増やすときは `kb/intents.yaml` 冒頭の運用コメントに従う。

## 品質・優先順

- 応答の前提: [`policy.md`](../policy.md)
- 評価用質問: [`eval/golden-questions.md`](../../eval/golden-questions.md) · 採点ルーブリック: [`eval/scoring-rubric.md`](../../eval/scoring-rubric.md) · インシデント記録: [`eval/incidents.md`](../../eval/incidents.md)
- 変更後はリポジトリルートで **`make ci`**（テンプレ整合＋ゴールデン件数）
- スプリント上の作業順（14→01→18）の一覧は [`docs/README.md`](../../docs/README.md) の「作業の優先順」節
