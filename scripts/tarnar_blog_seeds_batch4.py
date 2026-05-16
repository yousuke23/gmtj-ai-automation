# -*- coding: utf-8 -*-
"""TARNAR blog seeds voice-guide-181 … 230 (50 articles). SEO-friendly title variety (batch4)."""

P_JA = [
    "ワンマン前週の",
    "配信アーカイブ週の",
    "新曲レコーディング週の",
    "ライブハウス常連週の",
    "オーディション本番前の",
    "アコースティックセット週の",
    "ストリートライブ週の",
    "セッション本番前の",
    "ウィンター遠征中の",
    "春キャンプツアー中の",
]
S_JA = [
    "声を冷やさない朝イチの順番",
    "舌打ちレスの母音ドリル",
    "客席距離ごとの音量イメトレ",
    "眠気と声の抜けを防ぐ水分タイミング",
    "イヤモニ外し後の耳休めルーチン",
]

P_EN = [
    "One-man show week: ",
    "Streaming archive week: ",
    "New track recording week: ",
    "Live house regulars week: ",
    "Audition week: ",
    "Acoustic set week: ",
    "Street live week: ",
    "Session rehearsal week: ",
    "Winter tour: ",
    "Spring camp tour: ",
]
S_EN = [
    "a gentle morning order that keeps cords warm",
    "vowel drills without tongue clicks",
    "volume imagery by crowd distance",
    "hydration timing to beat sleepy tone",
    "ear-rest routine after in-ears",
]

P_KO = [
    "원맨 직전 주 ",
    "방송 아카이브 주 ",
    "신곡 녹음 주 ",
    "라이브하우스 단골 주 ",
    "오디션 본전 ",
    "어쿠스틱 세트 주 ",
    "스트리트 라이브 주 ",
    "세션 본공 전 ",
    "윈터 투어 중 ",
    "봄 캠프 투어 중 ",
]
S_KO = [
    "성대를 식히지 않는 아침 순서",
    "혀 클릭 없는 모음 드릴",
    "객석 거리별 볼륨 이미지",
    "졸림·탈성 방지 수분 타이밍",
    "인이어 후 귀 휴식 루틴",
]

P_ZH = [
    "个唱前一周：",
    "直播回放整理周：",
    "新曲录音周：",
    "Live House常客周：",
    "选拔本番前：",
    "原声现场周：",
    "街头演出周：",
    "合奏彩排前：",
    "冬季巡演途中：",
    "春季露营巡演：",
]
S_ZH = [
    "不凉嗓的早晨顺序",
    "无舌打音的母音练习",
    "按观众距离的音量想象",
    "防困与声音发虚的补水节奏",
    "摘下耳返后的耳朵休息流程",
]

BATCH4_JA_SEEDS: list[tuple[str, str, str]] = []
BATCH4_EN_TITLES: list[str] = []
BATCH4_KO_TITLES: list[str] = []
BATCH4_ZH_TITLES: list[str] = []

for pi, pja in enumerate(P_JA):
    for si, sja in enumerate(S_JA):
        idx = pi * len(S_JA) + si
        n = 181 + idx
        slug = f"voice-guide-{n:02d}"
        ja_t = pja + sja
        ja_b = (
            f"{ja_t}。"
            "AI TARNAR Voice School（Japan Music Tourism）向けの実践メモです。"
            "検索されやすい語をタイトルに入れつつ、旅・現場・配信のどれでも続けられる短時間設計にしています。"
        )
        BATCH4_JA_SEEDS.append((slug, ja_t, ja_b))
        BATCH4_EN_TITLES.append(P_EN[pi] + S_EN[si])
        BATCH4_KO_TITLES.append(P_KO[pi] + S_KO[si])
        BATCH4_ZH_TITLES.append(P_ZH[pi] + S_ZH[si])
