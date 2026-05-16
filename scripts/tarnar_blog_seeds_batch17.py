# -*- coding: utf-8 -*-
"""TARNAR blog seeds voice-guide-1401 … 1500 (100 articles). SEO title variety (batch17)."""

P_JA = [
    "初月面低重力ボイトレ模擬の",
    "海底油田プラットフォーム夜勤の",
    "初脳波夢遊ステージ司会の",
    "砂漠オアシス蜃気楼フェスの",
    "極地ブリザード中継アナの",
    "初細菌培養室声量制限の",
    "火山ガス警報下避難放送の",
    "初AI司書朗読対決週の",
    "地下鉄全線停電自足放送の",
    "初音響ホログラム合唱指揮の",
    "熱帯雷雨ピークCM収録の",
    "初火星VOICEBANK試聴会の",
    "古都石畳反響歩行ツアーの",
    "初量子鍵配送ライブ告知の",
    "雪原犬ぞり橇鈴同期規律の",
    "初非同期的和声リモート収録の",
    "潮干狩り干潟風マイクの",
    "初ゼロトラスト音声IAMの",
    "都市農園蜂羽音共生の",
    "初光通信深海ケーブル開通式の",
]
S_JA = [
    "12小節だけの母音三角測量",
    "一拍子ハミング定位グラデーション",
    "顎二重関節緩め読みリセット",
    "イヤーチップ交換後の音色校正",
    "血中酸素と声の通り一本化",
]

P_EN = [
    "First lunar low-g vocal sim week: ",
    "Offshore rig night-shift VO: ",
    "First sleepwalking-stage host EEG: ",
    "Desert-oasis mirage fest: ",
    "Polar blizzard relay announcer: ",
    "First culture-lab SPL cap: ",
    "Volcanic-gas alert evacuation PA: ",
    "First AI-librarian read-aloud duel week: ",
    "Metro-wide blackout self-powered PA: ",
    "First acoustic-hologram choir conduct: ",
    "Tropical thunderstorm peak ad capture: ",
    "First Mars voice-bank listening party: ",
    "Ancient-cobble echo walking tour: ",
    "First quantum-key courier live pitch: ",
    "Sled-dog bell sync discipline: ",
    "First async-harmony remote capture: ",
    "Tidal-flat wind-mic clamming day: ",
    "First zero-trust voice IAM: ",
    "Urban-farm bee-wing coexistence: ",
    "First fiber deep-sea cable launch VO: ",
]
S_EN = [
    "12-bar vowel triangulation only",
    "one-beat hum imaging gradient",
    "TMJ-softened read-aloud reset",
    "timbre check after ear-tip swap",
    "SpO2 aligned with vocal throughput",
]

P_KO = [
    "첫 달 표면 저중력 보이트레 시뮬 주 ",
    "해저 유전 플랫폼 야근 ",
    "첫 뇌파 몽유 무대 사회 ",
    "사막 오아시스 신기루 페스트 ",
    "극지 블리자드 중계 아나 ",
    "첫 세균 배양실 음량 제한 ",
    "화산 가스 경보 하 대피 방송 ",
    "첫 AI 사서 낭독 대결 주 ",
    "지하철 전선 정전 자급 방송 ",
    "첫 음향 홀로그램 합창 지휘 ",
    "열대 뇌우 피크 CM 녹화 ",
    "첫 화성 보이스뱅크 시청회 ",
    "고도 돌포장 반향 도보 투어 ",
    "첫 양자 키 배송 라이브 공지 ",
    "설원 썰매 개 징 동기 규율 ",
    "첫 비동기 화성 원격 녹음 ",
    "갯벌 바람 마이크 조개잡이 ",
    "첫 제로트러스트 보이스 IAM ",
    "도시 농원 벌 날개 공존 ",
    "첫 광통신 심해 케이블 개통식 ",
]
S_KO = [
    "12마디만 모음 삼각 측량",
    "한박자 허밍 이미징 그라데이션",
    "턱 이중관절 풀어 읽기 리셋",
    "이어팁 교체 후 음색 보정",
    "혈중 산소와 보이스 통로 일원화",
]

P_ZH = [
    "首次月球低重力练声模拟周：",
    "海底油田平台夜班口播：",
    "首次脑波梦游舞台主持：",
    "沙漠绿洲海市蜃楼音乐节：",
    "极地暴风雪中继播报：",
    "首次细菌培养室声压限制：",
    "火山气体警报下疏散广播：",
    "首次AI馆员朗读对决周：",
    "地铁全线停电自供电广播：",
    "首次声学全息合唱指挥：",
    "热带雷雨高峰广告采集：",
    "首次火星语音库试听会：",
    "古都石板回声步行导览：",
    "首次量子密钥配送现场宣讲：",
    "雪原狗拉雪橇铃声同步纪律：",
    "首次非同步和声远程采集：",
    "赶海滩涂防风麦克风：",
    "首次零信任语音IAM：",
    "都市农园蜂翅声共存：",
    "首次光通信深海电缆开通式：",
]
S_ZH = [
    "仅12小节的母音三角测量",
    "一拍哼鸣定位渐变",
    "颞颌放松朗读复位",
    "换耳塞后的音色校正",
    "血氧与发声通量对齐",
]

BATCH17_JA_SEEDS: list[tuple[str, str, str]] = []
BATCH17_EN_TITLES: list[str] = []
BATCH17_KO_TITLES: list[str] = []
BATCH17_ZH_TITLES: list[str] = []

for pi, pja in enumerate(P_JA):
    for si, sja in enumerate(S_JA):
        idx = pi * len(S_JA) + si
        n = 1401 + idx
        slug = f"voice-guide-{n:02d}"
        ja_t = pja + sja
        ja_b = (
            f"{ja_t}。"
            "AI TARNAR Voice School（Japan Music Tourism）の実践メモです。"
            "検索されやすいキーワードをタイトルに織り込み、旅・現場・配信のどれでも短時間で続けられる形にしています。"
        )
        BATCH17_JA_SEEDS.append((slug, ja_t, ja_b))
        BATCH17_EN_TITLES.append(P_EN[pi] + S_EN[si])
        BATCH17_KO_TITLES.append(P_KO[pi] + S_KO[si])
        BATCH17_ZH_TITLES.append(P_ZH[pi] + S_ZH[si])
