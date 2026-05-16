# -*- coding: utf-8 -*-
"""TARNAR blog seeds voice-guide-1101 … 1200 (100 articles). SEO title variety (batch14)."""

P_JA = [
    "アキバ深夜24時間配信週の",
    "氷湖ロケーション収録の",
    "盆地フェス熱帯夜湿度の",
    "初メタバース教会ユニゾンの",
    "屋上風15メートル収録日の",
    "初マグレブ車内ポッドキャストの",
    "洞窟残響96ミリ秒補正の",
    "熱帯雨林夜行性フェスの",
    "サイレントディスコ耳元MCの",
    "初ホログラムゲスト同席週の",
    "砂丘遮音ボックス野外の",
    "初思い出補完AI声合成週の",
    "初水中ヘッドセットMCの",
    "高層ガラス張り反響補正の",
    "初ISO whisper評価週の",
    "劇場廻り廊下ステージの",
    "初電磁パルス対策リハの",
    "島嶼部衛星リンク遅延の",
    "初収束型AI同時通訳の",
    "初リジェネラティブフィル席案内の",
]
S_JA = [
    "45秒テレプロンプター心拍同期読み上げ",
    "片耳モニタ定位のみの母音短尺",
    "子音前置時間を吐息で刻む練習",
    "360度カメラ正面と声の焦点合わせ",
    "乾燥指数と嘶り予兆の記録同期",
]

P_EN = [
    "Akiba overnight 24h stream week: ",
    "Frozen-lake location recording: ",
    "Basin fest tropical-night humidity: ",
    "First metaverse church unison: ",
    "Rooftop 15 m/s wind recording day: ",
    "First maglev in-car podcast: ",
    "Cave reverb 96 ms correction: ",
    "Rainforest nocturnal fest: ",
    "Silent-disco whisper MC: ",
    "First hologram guest co-presence week: ",
    "Dune wind-shielded outdoor booth: ",
    "First memory-fill AI voice synth week: ",
    "First underwater headset MC: ",
    "High-rise glass echo correction: ",
    "First ISO whisper eval week: ",
    "Theatre wraparound corridor stage: ",
    "First EMP-hardened rehearsal: ",
    "Island satellite-link latency: ",
    "First convergent AI simultaneous interp: ",
    "First regenerative-fil seat briefing: ",
]
S_EN = [
    "45s teleprompter read synced to heart rate",
    "one-ear-monitor vowel snaps for imaging",
    "consonant lead-in timed with breath puffs",
    "align voice focus with 360-cam front",
    "log dryness index with rasp precursors",
]

P_KO = [
    "아키바 심야 24시간 방송 주 ",
    "빙호 로케이션 녹화 ",
    "분지 페스트 열대야 습도 ",
    "첫 메타버스 교회 유니즌 ",
    "옥상 풍속 15m 녹화일 ",
    "첫 마그레브 차내 팟캐스트 ",
    "동굴 잔향 96ms 보정 ",
    "열대우림 야행성 페스트 ",
    "사일런트 디스코 귓속 MC ",
    "첫 홀로그램 게스트 동석 주 ",
    "사구 방풍 부스 야외 ",
    "첫 기억 보완 AI 보이스 합성 주 ",
    "첫 수중 헤드셋 MC ",
    "고층 유리 반향 보정 ",
    "첫 ISO 위스퍼 평가 주 ",
    "극장 회랑 무대 ",
    "첫 EMP 대비 리허 ",
    "도서 위성 링크 지연 ",
    "첫 수렴형 AI 동시통역 ",
    "첫 재생 필 좌석 안내 ",
]
S_KO = [
    "45초 텔레프롬프터 심박 동기 낭독",
    "한쪽 이어만으로 이미징 모음 짧은 구간",
    "숨김으로 자음 선행 타이밍",
    "360 카메라 정면과 보컬 포커스 맞추기",
    "건조 지수와 쉰 예감 메모 동기",
]

P_ZH = [
    "秋叶原深夜24小时直播周：",
    "冰湖外景录制：",
    "盆地音乐节热带夜湿度：",
    "首次元宇宙教堂齐唱：",
    "屋顶15米风速录制日：",
    "首次磁浮车内播客：",
    "洞穴混响96毫秒校正：",
    "热带雨林夜行音乐节：",
    "无声迪斯科耳边主持：",
    "首次全息嘉宾同席周：",
    "沙丘防风棚户外：",
    "首次记忆补全AI人声合成周：",
    "首次水下头戴主持：",
    "高层玻璃反射声校正：",
    "首次ISO耳语评估周：",
    "剧场回廊舞台：",
    "首次电磁脉冲对策排练：",
    "离岛卫星链路延迟：",
    "首次收敛型AI同传：",
    "首次再生胶片座位导览：",
]
S_ZH = [
    "45秒提词器与心率同步朗读",
    "单耳监听定位的短母音",
    "用气息刻出辅音前置时间",
    "360相机正面与发声焦点对齐",
    "干燥指数与嘶哑前兆同步记录",
]

BATCH14_JA_SEEDS: list[tuple[str, str, str]] = []
BATCH14_EN_TITLES: list[str] = []
BATCH14_KO_TITLES: list[str] = []
BATCH14_ZH_TITLES: list[str] = []

for pi, pja in enumerate(P_JA):
    for si, sja in enumerate(S_JA):
        idx = pi * len(S_JA) + si
        n = 1101 + idx
        slug = f"voice-guide-{n:02d}"
        ja_t = pja + sja
        ja_b = (
            f"{ja_t}。"
            "AI TARNAR Voice School（Japan Music Tourism）の実践メモです。"
            "検索されやすいキーワードをタイトルに織り込み、旅・現場・配信のどれでも短時間で続けられる形にしています。"
        )
        BATCH14_JA_SEEDS.append((slug, ja_t, ja_b))
        BATCH14_EN_TITLES.append(P_EN[pi] + S_EN[si])
        BATCH14_KO_TITLES.append(P_KO[pi] + S_KO[si])
        BATCH14_ZH_TITLES.append(P_ZH[pi] + S_ZH[si])
