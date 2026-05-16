# -*- coding: utf-8 -*-
"""TARNAR blog seeds voice-guide-131 … 180 (50 articles). Composed titles for SEO variety."""

# 10 × 5 = 50 unique Japanese titles
P_JA = [
    "ツアー初日の",
    "遠征二日目の",
    "レッスン週の",
    "収録月の",
    "配信シリーズの",
    "合唱練習週の",
    "バンド合宿の",
    "カフェ演奏週の",
    "フェス直前週の",
    "リゾート滞在中の",
]
S_JA = [
    "声メンテ予定を紙に落とすワーク",
    "3分スケール練習を固定する方法",
    "リスニング音量を見直すチェック",
    "睡眠ログと声のメモを並べる習慣",
    "水分ログで喉の声を相関させる記録",
]

P_EN = [
    "Tour day 1: ",
    "Tour day 2: ",
    "Lesson week: ",
    "Recording month: ",
    "Streaming series: ",
    "Choir week: ",
    "Band retreat: ",
    "Cafe gig week: ",
    "Festival week: ",
    "Resort stay: ",
]
S_EN = [
    "map a simple voice maintenance plan",
    "lock a 3-minute scale routine",
    "review safe listening levels",
    "pair sleep notes with vocal notes",
    "track hydration alongside tone changes",
]

P_KO = [
    "투어 첫날 ",
    "투어 이틀차 ",
    "레슨 주간 ",
    "녹음 월간 ",
    "방송 시리즈 ",
    "합창 연습 주 ",
    "밴드 합숙 ",
    "카페 공연 주 ",
    "페스 직전 주 ",
    "리조트 체류 중 ",
]
S_KO = [
    "보이스 메모를 종이에 정리",
    "3분 스케일 루틴 고정",
    "리스닝 볼륨 점검",
    "수면·목소리 메모 병행",
    "수분과 톤 변화 기록",
]

P_ZH = [
    "巡演首日：",
    "巡演次日：",
    "上课周：",
    "录音月：",
    "直播系列：",
    "合唱排练周：",
    "乐队集训：",
    "咖啡馆演出周：",
    "音乐节前一周：",
    "度假村停留：",
]
S_ZH = [
    "把嗓音养护计划写下来",
    "固定三分钟音阶练习",
    "复查聆听音量",
    "睡眠与嗓音笔记对照",
    "记录饮水与音色变化",
]

BATCH3_JA_SEEDS: list[tuple[str, str, str]] = []
BATCH3_EN_TITLES: list[str] = []
BATCH3_KO_TITLES: list[str] = []
BATCH3_ZH_TITLES: list[str] = []

for pi, pja in enumerate(P_JA):
    for si, sja in enumerate(S_JA):
        idx = pi * len(S_JA) + si
        n = 131 + idx
        slug = f"voice-guide-{n:02d}"
        ja_t = pja + sja
        ja_b = (
            f"{ja_t}。"
            "AI TARNAR Voice School の実践ログとして、短いセッションで再現性を上げる手順に整理しています。"
            "検索流入で見つけやすいよう、旅・収録・配信の文脈語をタイトルに織り込みました。"
        )
        BATCH3_JA_SEEDS.append((slug, ja_t, ja_b))
        BATCH3_EN_TITLES.append(P_EN[pi] + S_EN[si])
        BATCH3_KO_TITLES.append(P_KO[pi] + S_KO[si])
        BATCH3_ZH_TITLES.append(P_ZH[pi] + S_ZH[si])
