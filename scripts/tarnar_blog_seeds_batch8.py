# -*- coding: utf-8 -*-
"""TARNAR blog seeds voice-guide-501 … 600 (100 articles). SEO title variety (batch8)."""

P_JA = [
    "サマタイム声枯れ予防週の",
    "秋祭り演台初日の",
    "オンライン宿題添削日の",
    "耳鳴りを感じた週の",
    "アナログテープ走行週の",
    "子連れリハーサル日の",
    "深夜オンライン合奏の",
    "仮装ライブ本番の",
    "卒業ライブ最終週の",
    "デュエット初披露の",
    "喉風邪明け初声の",
    "アイス飲みすぎ乾燥日の",
    "屋外夕涼みライブの",
    "耳コピ押し込み週の",
    "CDサイン会前の",
    "防音室初使用日の",
    "喉スプレー変更週の",
    "メトロノーム外し練の",
    "チア曲メドレー週の",
    "吹奏アンコン直前の",
]
S_JA = [
    "唇閉じ45秒ホールド",
    "有声子音だけのリズム枠",
    "ノートPCファン音下での小声合わせ",
    "背筋から胸骨の一直線イメージ呼吸",
    "フレーズ頭の子音だけ抜き打ち",
]

P_EN = [
    "Summer vocal fatigue prevention: ",
    "First day autumn festival stage: ",
    "Online homework feedback day: ",
    "Week you noticed ear ringing: ",
    "Analog tape run week: ",
    "Kids-at-rehearsal day: ",
    "Late-night online ensemble: ",
    "Costume live show: ",
    "Final grad live week: ",
    "First duet reveal: ",
    "First phonation after sore throat: ",
    "Too much ice drink dry day: ",
    "Outdoor evening breeze gig: ",
    "Ear-copy cram week: ",
    "Before CD signing: ",
    "First day in the booth: ",
    "Throat spray switch week: ",
    "Practice without metronome: ",
    "Cheer medley week: ",
    "Before wind ensemble concert: ",
]
S_EN = [
    "45s closed-lip hold",
    "rhythm grid voiced consonants only",
    "quiet blend under laptop fan noise",
    "stack spine-to-sternum breath line",
    "spot-drill phrase-initial consonants",
]

P_KO = [
    "여름 성대 피로 예방 주 ",
    "가을 축제 무대 첫날 ",
    "온라인 과제 피드백일 ",
    "이명 느낀 주 ",
    "아날로그 테이프 런 주 ",
    "아이 동반 리허설일 ",
    "심야 온라인 합주 ",
    "분장 라이브 본공연 ",
    "졸업 라이브 마지막 주 ",
    "첫 듀엣 공개 ",
    "목감기 후 첫 발성 ",
    "아이스 과다 건조일 ",
    "야외 저녁 바람 공연 ",
    "귀복사 암기 주 ",
    "CD 사인회 전 ",
    "방음실 첫 사용일 ",
    "목 스프레이 교체 주 ",
    "메트로놈 없이 연습 ",
    "치어 메들리 주 ",
    "관악 정기연주 직전 ",
]
S_KO = [
    "입술 닫고 45초 홀드",
    "유성 자음만 리듬 틀",
    "노트북 팬 소음 아래 작은 소리 맞추기",
    "등→흉골 일직선 호흡 이미지",
    "구절 머리 자음만 스팟",
]

P_ZH = [
    "夏季护嗓预防周：",
    "秋日祭舞台首日：",
    "在线作业点评日：",
    "出现耳鸣的一周：",
    "模拟磁带跑带周：",
    "带娃排练日：",
    "深夜在线合奏：",
    "变装live正式场：",
    "毕业演出最后一周：",
    "首次双人公开：",
    "感冒后首次开嗓：",
    "冰饮过量干燥日：",
    "户外纳凉演出：",
    "扒谱突击周：",
    "签售会前：",
    "隔音室首日：",
    "换用喉喷周：",
    "脱离节拍器练习：",
    "啦啦队串烧周：",
    "管乐定期演奏会前：",
]
S_ZH = [
    "抿唇45秒保持",
    "只用浊辅音打节奏框",
    "在笔记本风扇声下小声对齐",
    "脊背到胸骨一条线呼吸意象",
    "只抠乐句开头的辅音",
]

BATCH8_JA_SEEDS: list[tuple[str, str, str]] = []
BATCH8_EN_TITLES: list[str] = []
BATCH8_KO_TITLES: list[str] = []
BATCH8_ZH_TITLES: list[str] = []

for pi, pja in enumerate(P_JA):
    for si, sja in enumerate(S_JA):
        idx = pi * len(S_JA) + si
        n = 501 + idx
        slug = f"voice-guide-{n:02d}"
        ja_t = pja + sja
        ja_b = (
            f"{ja_t}。"
            "AI TARNAR Voice School（Japan Music Tourism）の実践メモです。"
            "検索されやすいキーワードをタイトルに織り込み、旅・現場・配信のどれでも短時間で続けられる形にしています。"
        )
        BATCH8_JA_SEEDS.append((slug, ja_t, ja_b))
        BATCH8_EN_TITLES.append(P_EN[pi] + S_EN[si])
        BATCH8_KO_TITLES.append(P_KO[pi] + S_KO[si])
        BATCH8_ZH_TITLES.append(P_ZH[pi] + S_ZH[si])
