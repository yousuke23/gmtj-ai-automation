# -*- coding: utf-8 -*-
"""TARNAR blog seeds voice-guide-401 … 500 (100 articles). SEO title variety (batch7)."""

P_JA = [
    "初Symphony録音週の",
    "多言語リリース週の",
    "ゲストコーラス本番の",
    "ピッチ補正後の生歌慣れの",
    "DTMからライブ初日の",
    "ワイヤレスマイク試走の",
    "二次会カラオケ明けの",
    "ボーカルREC温度差週の",
    "早朝テレビ収録の",
    "海外遠征帰国直後の",
    "座席近めホールの",
    "観客合唱パートの",
    "仮声と地声の切替週の",
    "ハードパン楽曲のみ週の",
    "リハーサル室エア乾燥の",
    "配信コラボ当日の",
    "子ども向けワークショップの",
    "ミュージカルオーディション前の",
    "ダンス連動ステージの",
    "春アレルギー多発週の",
]
S_JA = [
    "会場キーを基準にした短イントロ合わせ",
    "息残しで決めるサビ前無音",
    "耳栓装着時の音量感チェック",
    "仮声域の安全半音ラダー",
    "舌根を抜く「れ」行リセット",
]

P_EN = [
    "First symphony recording week: ",
    "Multilingual release week: ",
    "Guest choir show: ",
    "After pitch-correction live prep: ",
    "From DTM to first live: ",
    "Wireless mic dry run: ",
    "After late-night karaoke: ",
    "Vocal booth temp swing week: ",
    "Early TV taping: ",
    "Right after an overseas tour: ",
    "Close-seating hall: ",
    "Audience singalong part: ",
    "Head/chest switch week: ",
    "Hard-panned tracks week: ",
    "Dry rehearsal-room air: ",
    "Collab stream day: ",
    "Kids workshop: ",
    "Before musical audition: ",
    "Dance-heavy stage: ",
    "High-pollen spring week: ",
]
S_EN = [
    "short intro tuning to room key",
    "silence before chorus on leftover breath",
    "volume check with earplugs in",
    "safe half-step ladder in falsetto",
    "reset tongue root with “re” row drills",
]

P_KO = [
    "첫 심포니 녹음 주 ",
    "다국어 릴리즈 주 ",
    "게스트 합창 본공연 ",
    "피치 보정 후 라이브 적응 ",
    "DTM에서 라이브 첫날 ",
    "무선 마이크 리허설 ",
    "2차 노래방 다음 날 ",
    "보컬 부스 온도차 주 ",
    "새벽 TV 녹화 ",
    "해외 투어 직후 ",
    "좌석 가까운 홀 ",
    "관객 합창 파트 ",
    "가성·진성 전환 주 ",
    "하드 팬 트랙만 주 ",
    "리허설실 건조 공기 ",
    "콜라보 방송 당일 ",
    "아동 워크숍 ",
    "뮤지컬 오디션 전 ",
    "댄스 연동 무대 ",
    "꽃가루 많은 봄 주 ",
]
S_KO = [
    "무대 키 기준 짧은 인트로 맞추기",
    "남은 호흡으로 후렴 전 무음",
    "귀마개 착용 시 볼륨 감각",
    "가성역 안전 반음 사다리",
    "혀뿌리 풀기 ‘레’ 행 리셋",
]

P_ZH = [
    "首次交响录音周：",
    "多语种发行周：",
    "嘉宾合唱正式场：",
    "修音后回归真唱：",
    "从编曲到首场演出：",
    "无线麦试跑：",
    "二次聚会唱K次日：",
    "人声录音棚温差周：",
    "清晨电视录制：",
    "海外巡演刚回国：",
    "座位较近的大厅：",
    "观众合唱段落：",
    "真假声切换周：",
    "硬声像曲目周：",
    "排练室干燥空气：",
    "联机直播当天：",
    "儿童工作坊：",
    "音乐剧试镜前：",
    "舞蹈联动舞台：",
    "花粉季高发周：",
]
S_ZH = [
    "以现场调性对齐短前奏",
    "用余气稳住副歌前静音",
    "戴耳塞时的音量自测",
    "假声区安全半音阶",
    "用「れ」行放松舌根",
]

BATCH7_JA_SEEDS: list[tuple[str, str, str]] = []
BATCH7_EN_TITLES: list[str] = []
BATCH7_KO_TITLES: list[str] = []
BATCH7_ZH_TITLES: list[str] = []

for pi, pja in enumerate(P_JA):
    for si, sja in enumerate(S_JA):
        idx = pi * len(S_JA) + si
        n = 401 + idx
        slug = f"voice-guide-{n:02d}"
        ja_t = pja + sja
        ja_b = (
            f"{ja_t}。"
            "AI TARNAR Voice School（Japan Music Tourism）の実践メモです。"
            "検索されやすいキーワードをタイトルに織り込み、旅・現場・配信のどれでも短時間で続けられる形にしています。"
        )
        BATCH7_JA_SEEDS.append((slug, ja_t, ja_b))
        BATCH7_EN_TITLES.append(P_EN[pi] + S_EN[si])
        BATCH7_KO_TITLES.append(P_KO[pi] + S_KO[si])
        BATCH7_ZH_TITLES.append(P_ZH[pi] + S_ZH[si])
