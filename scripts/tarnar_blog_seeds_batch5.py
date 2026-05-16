# -*- coding: utf-8 -*-
"""TARNAR blog seeds voice-guide-231 … 300 (70 articles). SEO title variety (batch5)."""

P_JA = [
    "サマーフェス明けの",
    "深夜移動日の",
    "海外メンバー参加週の",
    "ミキサー整備日の",
    "テイク整理デーの",
    "外ロケ早朝の",
    "声のコンディション週間の",
    "ライブハウス周年月の",
    "合唱本番前の",
    "アニメタイアップ週の",
    "乾燥する冬の",
    "新年一発目の公演週の",
    "春休みファミリーデーの",
    "帰省ライブ前の",
]
S_JA = [
    "三呼吸で整える開幕",
    "舌の左右差を均す母音セット",
    "袖でできる静音発声",
    "歩きながらの軽ハミング",
    "観客を見ずに音量だけ合わせるミニ練",
]

P_EN = [
    "After summer fest: ",
    "Late-night travel day: ",
    "International guests week: ",
    "Mixer maintenance day: ",
    "Take cleanup day: ",
    "Early outdoor shoot: ",
    "Weekly voice condition: ",
    "Live house anniversary month: ",
    "Before choir finals: ",
    "Anime tie-in week: ",
    "Dry winter air: ",
    "First show of the year: ",
    "Spring break family gig: ",
    "Before hometown show: ",
]
S_EN = [
    "open with three calm breaths",
    "vowel set to balance left/right tongue bias",
    "silent phonation you can do backstage",
    "light humming while walking",
    "mini level match without staring at the crowd",
]

P_KO = [
    "여름 페스 직후 ",
    "심야 이동일 ",
    "해외 멤버 참여 주 ",
    "믹서 점검일 ",
    "테이크 정리 데이 ",
    "야외 로케이션 이른 아침 ",
    "보이스 컨디션 주간 ",
    "라이브하우스 기념 달 ",
    "합창 본선 전 ",
    "애니 타이업 주 ",
    "건조한 겨울 ",
    "신년 첫 공연 주 ",
    "봄방학 패밀리 데이 ",
    "귀향 라이브 전 ",
]
S_KO = [
    "세 번 호흡으로 오프닝 정리",
    "모음으로 좌우 혀 밸런스",
    "무대 옆 무성 발성",
    "걸으며 가벼운 허밍",
    "관객 없이 볼륨만 맞추는 미니 연습",
]

P_ZH = [
    "夏季音乐节次日：",
    "深夜转场日：",
    "海外成员排练周：",
    "调音台维护日：",
    "分轨整理日：",
    "外景清晨：",
    "嗓音状态周：",
    "Live House周年月：",
    "合唱决赛前：",
    "动画联动周：",
    "干燥冬季：",
    "新年首场演出周：",
    "春假家庭场：",
    "返乡演出前：",
]
S_ZH = [
    "三口气稳住开场",
    "用母音平衡左右舌",
    "侧台静音发声",
    "边走边轻哼",
    "不看观众只做音量对齐的小练习",
]

BATCH5_JA_SEEDS: list[tuple[str, str, str]] = []
BATCH5_EN_TITLES: list[str] = []
BATCH5_KO_TITLES: list[str] = []
BATCH5_ZH_TITLES: list[str] = []

for pi, pja in enumerate(P_JA):
    for si, sja in enumerate(S_JA):
        idx = pi * len(S_JA) + si
        n = 231 + idx
        slug = f"voice-guide-{n:02d}"
        ja_t = pja + sja
        ja_b = (
            f"{ja_t}。"
            "AI TARNAR Voice School（Japan Music Tourism）の実践メモです。"
            "検索されやすいキーワードをタイトルに織り込み、旅・現場・配信のどれでも短時間で続けられる形にしています。"
        )
        BATCH5_JA_SEEDS.append((slug, ja_t, ja_b))
        BATCH5_EN_TITLES.append(P_EN[pi] + S_EN[si])
        BATCH5_KO_TITLES.append(P_KO[pi] + S_KO[si])
        BATCH5_ZH_TITLES.append(P_ZH[pi] + S_ZH[si])
