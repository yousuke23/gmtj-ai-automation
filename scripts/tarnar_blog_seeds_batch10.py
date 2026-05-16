# -*- coding: utf-8 -*-
"""TARNAR blog seeds voice-guide-701 … 800 (100 articles). SEO title variety (batch10)."""

P_JA = [
    "セルフプロデュース週の",
    "AI解析FB初週の",
    "ラストツアー前週の",
    "文化祭メインステージの",
    "コミュニティFM出演日の",
    "ピアノ採点リハの",
    "聴力検査後初練の",
    "初マスタリング同席週の",
    "字幕収録見学日の",
    "メーター持参交渉日の",
    "TAB譜併用週の",
    "喉鏡後初声の",
    "女声パート合わせの",
    "男声パート合わせの",
    "混声四部本番前の",
    "アイドルオーディション最終の",
    "古参ファン前列週の",
    "初海外配信越境の",
    "停電明け残響判定的",
    "新年ライブ初日の",
]
S_JA = [
    "セルフチェック15秒録音ループ",
    "OKワードだけの短返答練",
    "BPM88で刻む語尾減衰",
    "マスク装着小声穿透チェック",
    "モノローグ台本の息配分割り",
]

P_EN = [
    "Self-produce week: ",
    "First week of AI feedback: ",
    "Week before the farewell tour: ",
    "School festival main stage: ",
    "Community FM guest day: ",
    "Piano-scored rehearsal: ",
    "First practice after hearing test: ",
    "First mastering session sit-in week: ",
    "Subtitle session observation: ",
    "SPL meter negotiation day: ",
    "TAB plus notation week: ",
    "First phonation after laryngoscopy: ",
    "Women’s section blend: ",
    "Men’s section blend: ",
    "Before SATB finals: ",
    "Idol audition finals: ",
    "Front-row veteran fans week: ",
    "First cross-border stream: ",
    "Post-outage room-decay check: ",
    "New Year's first live: ",
]
S_EN = [
    "15s self-record loop",
    "OK-only short reply drill",
    "tail decay at BPM 88",
    "mask-on whisper projection check",
    "monologue breath map split",
]

P_KO = [
    "셀프 프로듀스 주 ",
    "AI 피드백 첫 주 ",
    "페어웰 투어 전 주 ",
    "문화제 메인 스테이지 ",
    "지역 FM 게스트 날 ",
    "피아노 채점 리허 ",
    "청력 검사 후 첫 연습 ",
    "첫 마스터링 동석 주 ",
    "자막 녹음 견학일 ",
    "미터 지참 협상일 ",
    "TAB 병행 주 ",
    "후경 후 첫 발성 ",
    "여성 파트 블렌드 ",
    "남성 파트 블렌드 ",
    "혼성 4부 본선 전 ",
    "아이돌 오디션 파이널 ",
    "첫열 베테랑 팬 주 ",
    "첫 해외 스트림 ",
    "정전 후 잔향 판별 ",
    "신년 첫 라이브 ",
]
S_KO = [
    "15초 셀프 녹음 루프",
    "OK 단어만 짧은 답변 연습",
    "BPM88로 말미 감쇠",
    "마스크 착용 속삭임 투사 체크",
    "독백 대본 호흡 맵 분할",
]

P_ZH = [
    "自主制作周：",
    "AI反馈首周：",
    "告别巡演前一周：",
    "校庆主舞台：",
    "社区电台嘉宾日：",
    "钢琴打分排练：",
    "听力检查后首练：",
    "首次母带同席周：",
    "字幕录制观摩日：",
    "自带声压计沟通日：",
    "TAB与五线谱并用周：",
    "喉镜后首次发声：",
    "女声部磨合：",
    "男声部磨合：",
    "混声四部决赛前：",
    "偶像选拔终试：",
    "前排老粉周：",
    "首次跨境直播：",
    "停电后残响判断：",
    "新年首场演出：",
]
S_ZH = [
    "15秒自检录音循环",
    "只用OK词的短答练习",
    "BPM88刻语尾衰减",
    "戴口罩小声穿透检查",
    "独白稿呼吸分段",
]

BATCH10_JA_SEEDS: list[tuple[str, str, str]] = []
BATCH10_EN_TITLES: list[str] = []
BATCH10_KO_TITLES: list[str] = []
BATCH10_ZH_TITLES: list[str] = []

for pi, pja in enumerate(P_JA):
    for si, sja in enumerate(S_JA):
        idx = pi * len(S_JA) + si
        n = 701 + idx
        slug = f"voice-guide-{n:02d}"
        ja_t = pja + sja
        ja_b = (
            f"{ja_t}。"
            "AI TARNAR Voice School（Japan Music Tourism）の実践メモです。"
            "検索されやすいキーワードをタイトルに織り込み、旅・現場・配信のどれでも短時間で続けられる形にしています。"
        )
        BATCH10_JA_SEEDS.append((slug, ja_t, ja_b))
        BATCH10_EN_TITLES.append(P_EN[pi] + S_EN[si])
        BATCH10_KO_TITLES.append(P_KO[pi] + S_KO[si])
        BATCH10_ZH_TITLES.append(P_ZH[pi] + S_ZH[si])
