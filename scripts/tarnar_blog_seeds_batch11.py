# -*- coding: utf-8 -*-
"""TARNAR blog seeds voice-guide-801 … 900 (100 articles). SEO title variety (batch11)."""

P_JA = [
    "量子会議リモート週の",
    "ゼロカーボン会場見学の",
    "初XRスタジオ収録の",
    "AI同時通訳リハの",
    "サステナブルツアー移動日の",
    "地域共創ワークショップの",
    "多言語字幕ライブ配信の",
    "初バイノーラル試聴会の",
    "耳鳴りケア相談後の",
    "喉スキャン3D共有週の",
    "フェス炭素排出見える化の",
    "ボランティア誘導アナウンスの",
    "夜間搬入明け早声の",
    "海上フェリー移動週の",
    "山小屋無電源リハの",
    "盆帰省高速SA練の",
    "初AI作曲セッションの",
    "著作権ワークショップ明けの",
    "インバウンド礼節講習週の",
    "年末大掃除声帯休めの",
]
S_JA = [
    "3行だけの自己紹介テンプレ声出し",
    "数字読み上げノイズ耐性ミニ練",
    "仮想客席360の視線配分メモ",
    "低酸素モード想定の浅呼吸セット",
    "静音ハミングで喉だけ起こす",
]

P_EN = [
    "Quantum-meeting remote week: ",
    "Zero-carbon venue tour: ",
    "First XR studio session: ",
    "AI simultaneous-interpret rehearsal: ",
    "Sustainable tour travel day: ",
    "Co-creation workshop: ",
    "Multilingual captioned stream: ",
    "First binaural listening session: ",
    "After tinnitus-care consult: ",
    "3D larynx scan share week: ",
    "Fest carbon footprint visible week: ",
    "Volunteer routing announcements: ",
    "Early voice after overnight load-in: ",
    "Ferry week between ports: ",
    "Off-grid mountain hut rehearsal: ",
    "Bon trip highway SA practice: ",
    "First AI co-writing session: ",
    "After copyright workshop: ",
    "Inbound etiquette drill week: ",
    "Year-end deep-clean vocal rest: ",
]
S_EN = [
    "three-line intro template out loud",
    "number-read noise mini-drill",
    "360 audience gaze map memo",
    "shallow-breath low-O2 prep set",
    "silent hum to wake the folds",
]

P_KO = [
    "퀀텀 미팅 원격 주 ",
    "제로카본 공장 견학 ",
    "첫 XR 스튜디오 세션 ",
    "AI 동시통역 리허 ",
    "지속가능 투어 이동일 ",
    "지역 공동창작 워크숍 ",
    "다국어 자막 라이브 ",
    "첫 바이노럴 청취회 ",
    "이명 케어 상담 후 ",
    "3D 후두 스캔 공유 주 ",
    "페스트 탄소 가시화 주 ",
    "자원봉사 안내 아나운스 ",
    "야간 반입 후 이른 발성 ",
    "페리 이동 주 ",
    "산장 오프그리드 리허 ",
    "귀성 고속 SA 연습 ",
    "첫 AI 공동작곡 세션 ",
    "저작권 워크숍 다음 날 ",
    "인바운드 예절 훈련 주 ",
    "연말 대청소 성대 휴식 ",
]
S_KO = [
    "3줄 자기소개 템플릿 발성",
    "숫자 읽기 노이즈 미니 연습",
    "360 관객 시선 배분 메모",
    "저산소 모드 얕은 호흡 세트",
    "무성 허밍으로 성대 깨우기",
]

P_ZH = [
    "量子会议远程周：",
    "零碳场馆参观：",
    "首次XR棚录制：",
    "AI同传排练：",
    "可持续巡演移动日：",
    "地域共创工作坊：",
    "多语字幕直播：",
    "首次双耳试听会：",
    "耳鸣护理咨询后：",
    "喉部3D扫描共享周：",
    "音乐节碳足迹可视化周：",
    "志愿者疏导播报：",
    "夜间进场后晨声：",
    "渡轮周转周：",
    "山间小屋离网排练：",
    "返乡高速SA练习：",
    "首次AI共创曲会话：",
    "版权工作坊次日：",
    "入境礼仪集训周：",
    "年末大扫除声带休息：",
]
S_ZH = [
    "三行自我介绍模板出声",
    "数字朗读抗噪小练",
    "360观众视线分配备忘",
    "低氧模式浅呼吸组",
    "静音哼鸣唤醒声带",
]

BATCH11_JA_SEEDS: list[tuple[str, str, str]] = []
BATCH11_EN_TITLES: list[str] = []
BATCH11_KO_TITLES: list[str] = []
BATCH11_ZH_TITLES: list[str] = []

for pi, pja in enumerate(P_JA):
    for si, sja in enumerate(S_JA):
        idx = pi * len(S_JA) + si
        n = 801 + idx
        slug = f"voice-guide-{n:02d}"
        ja_t = pja + sja
        ja_b = (
            f"{ja_t}。"
            "AI TARNAR Voice School（Japan Music Tourism）の実践メモです。"
            "検索されやすいキーワードをタイトルに織り込み、旅・現場・配信のどれでも短時間で続けられる形にしています。"
        )
        BATCH11_JA_SEEDS.append((slug, ja_t, ja_b))
        BATCH11_EN_TITLES.append(P_EN[pi] + S_EN[si])
        BATCH11_KO_TITLES.append(P_KO[pi] + S_KO[si])
        BATCH11_ZH_TITLES.append(P_ZH[pi] + S_ZH[si])
