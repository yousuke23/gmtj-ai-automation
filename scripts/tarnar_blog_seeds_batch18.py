# -*- coding: utf-8 -*-
"""TARNAR blog seeds voice-guide-1501 … 1600 (100 articles). SEO title variety (batch18)."""

P_JA = [
    "初深海熱水噴出孔採音の",
    "夜行列車寝台密閉放送の",
    "初プラズマドーム放電MCの",
    "盆地大気光化学スモッグの",
    "初音響地雷探知訓練の",
    "熱帯低気圧のここ通過アナの",
    "初金属積層造形ハウリング抑制の",
    "古墳石室反響歩行の",
    "初低軌道衛星ノイズ週の",
    "停戦中立地帯拡声案内の",
    "初芳香剤高濃度下のCMの",
    "雪山滑落救助笛パターンの",
    "初流体ダイナミクス風洞収録の",
    "夜市露天キッチン油煙の",
    "初水中音叉共鳴デモの",
    "干潟干上り亀裂足音収録の",
    "初強磁性MRI近傍声量の",
    "台風避難所断水告知の",
    "初宇宙デブリ接近警報アナの",
    "初音楽著作隣接権セミナーの",
]
S_JA = [
    "16分音符だけの舌位置トラッキング",
    "語頭無声摩擦音三連打クールダウン",
    "横隔膜ロックイン10秒白熱枠",
    "会話中ビートボックス切替二拍猶予",
    "唾液粘度と発話遅延ログ照合",
]

P_EN = [
    "First deep-sea vent hydrophone week: ",
    "Sleeper-train sealed-cabin PA: ",
    "First plasma-dome discharge MC: ",
    "Basin photochemical smog day: ",
    "First acoustic landmine-drill VO: ",
    "Tropical cyclone center-pass announcer: ",
    "First metal-AM howl-suppression set: ",
    "Kofun stone-chamber echo walk: ",
    "First LEO satellite noise week: ",
    "Ceasefire neutral-zone loud hailer: ",
    "First high-scent-load ad read: ",
    "Avalanche-rescue whistle patterns: ",
    "First CFD wind-tunnel capture: ",
    "Night-market open-kitchen grease haze: ",
    "First underwater tuning-fork demo: ",
    "Tidal-flat crackle footstep capture: ",
    "First strong-MRI-adjacent SPL cap: ",
    "Typhoon-shelter water-cut notice: ",
    "First space-debris proximity alert announcer: ",
    "First neighboring-rights seminar host: ",
]
S_EN = [
    "16th-note-only tongue tracking",
    "triple voiceless-fricative cool-down",
    "10s diaphragm lock-in sprint frame",
    "two-beat grace talk-to-beatbox switch",
    "saliva viscosity vs speech-latency log match",
]

P_KO = [
    "첫 심해열수 분출공 채음 ",
    "야행 열차 침대 밀폐 방송 ",
    "첫 플라즈마 돔 방전 MC ",
    "분지 대기 광화학 스모그 ",
    "첫 음향 지뢰 탐지 훈련 ",
    "열대 저기압 중심 통과 아나 ",
    "첫 금속 적층조형 하울링 억제 ",
    "고분 석실 반향 도보 ",
    "첫 저궤도 위성 노이즈 주 ",
    "휴전 중립지대 확성 안내 ",
    "첫 방향제 고농도 하 CM ",
    "설산 미끄럼 구조 호루라기 패턴 ",
    "첫 유체역학 풍동 캡처 ",
    "야시 노점 키친 기름 연기 ",
    "첫 수중 음차 공명 데모 ",
    "갯벌 바싹 갈라짐 발소리 녹음 ",
    "첫 강자성 MRI 인접 음량 ",
    "태풍 대피소 단수 공지 ",
    "첫 우주 잔해물 접근 경보 아나 ",
    "첫 음악 저작 인접권 세미나 ",
]
S_KO = [
    "16분음표만 혀 위치 트래킹",
    "어두 무성 마찰음 삼연타 쿨다운",
    "횡격막 락인 10초 스프린트 틀",
    "대화 중 비트박스 전환 2박 유예",
    "타액 점도와 발화 지연 로그 대조",
]

P_ZH = [
    "首次深海热液喷口采声：",
    "夜行列车卧铺密闭广播：",
    "首次等离子穹顶放电主持：",
    "盆地大气光化学烟雾日：",
    "首次音响探雷训练口播：",
    "热带低压中心通过播报：",
    "首次金属增材啸叫抑制：",
    "古坟石室回声步行：",
    "首次低轨卫星噪声周：",
    "停战中立地带扩声指引：",
    "首次高浓度香氛下广告朗读：",
    "雪山滑落救援哨音型：",
    "首次计算流体力学风洞采集：",
    "夜市露天厨房油烟：",
    "首次水下音叉共振演示：",
    "干滩龟裂足音采集：",
    "首次强磁场MRI邻近声压：",
    "台风避难所断水通知：",
    "首次空间碎片接近警报播报：",
    "首次音乐著作邻接权研讨会主持：",
]
S_ZH = [
    "仅十六分音符的舌位跟踪",
    "词头清擦音三连击放松",
    "横膈10秒锁定冲刺框",
    "对话中节奏口技切换两拍缓冲",
    "唾液黏度与发音延迟日志对照",
]

BATCH18_JA_SEEDS: list[tuple[str, str, str]] = []
BATCH18_EN_TITLES: list[str] = []
BATCH18_KO_TITLES: list[str] = []
BATCH18_ZH_TITLES: list[str] = []

for pi, pja in enumerate(P_JA):
    for si, sja in enumerate(S_JA):
        idx = pi * len(S_JA) + si
        n = 1501 + idx
        slug = f"voice-guide-{n:02d}"
        ja_t = pja + sja
        ja_b = (
            f"{ja_t}。"
            "AI TARNAR Voice School（Japan Music Tourism）の実践メモです。"
            "検索されやすいキーワードをタイトルに織り込み、旅・現場・配信のどれでも短時間で続けられる形にしています。"
        )
        BATCH18_JA_SEEDS.append((slug, ja_t, ja_b))
        BATCH18_EN_TITLES.append(P_EN[pi] + S_EN[si])
        BATCH18_KO_TITLES.append(P_KO[pi] + S_KO[si])
        BATCH18_ZH_TITLES.append(P_ZH[pi] + S_ZH[si])
