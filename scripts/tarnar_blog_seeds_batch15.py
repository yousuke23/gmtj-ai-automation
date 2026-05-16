# -*- coding: utf-8 -*-
"""TARNAR blog seeds voice-guide-1201 … 1300 (100 articles). SEO title variety (batch15)."""

P_JA = [
    "初地下防潮スタジオ週の",
    "高湿度塩害海岸収録の",
    "初真空チャンバー無響の",
    "砂嵐フェス眼鏡装着MCの",
    "極寒氷点下声帯ウォームの",
    "初二酸化炭素高濃度ホールの",
    "雷雲30キロ退避配信の",
    "初パーソナル立体音響劇場の",
    "高速道路SA夜間アナウンスの",
    "初脳波同期リハーサルの",
    "ラグビー場収録防護週の",
    "初市民天文台サイレント演出の",
    "停電自家発バックアップ録音の",
    "盆地逆温層蒸気声の",
    "初触覚フィードバックスーツ収録の",
    "明治古建木造反響補正の",
    "初音声DNAウォーターマーク収録の",
    "夜間空港滑走路ライトの",
    "初分散型タグライン同期週の",
    "初収音権ウォレット署名日の",
]
S_JA = [
    "20秒囁き声域だけの通話テスト",
    "吸気2拍子の子音連打安定枠",
    "舌根沈下と喉頭安定モノローグ",
    "耳道圧バランス確認用母音スイープ",
    "心拍変動に合わせた語尾長調整",
]

P_EN = [
    "First sub-basement damp-proof studio week: ",
    "High-humidity salt-spray coast recording: ",
    "First vacuum-chamber anechoic day: ",
    "Sandstorm fest goggle-on MC: ",
    "Sub-zero vocal-fold warm-up: ",
    "First high-CO2 hall rehearsal: ",
    "Thundercell 30 km evac stream: ",
    "First personal spatial-audio theatre: ",
    "Highway SA night-announce booth: ",
    "First EEG-sync rehearsal: ",
    "Rugby pitch recording PPE week: ",
    "First public-observatory silent show: ",
    "Blackout genset backup recording: ",
    "Basin inversion-layer steam voice: ",
    "First haptic-feedback suit capture: ",
    "Meiji-era timber echo correction: ",
    "First audio-DNA watermark session: ",
    "Night-airport runway-light VO: ",
    "First distributed tagline sync week: ",
    "First listening-rights wallet-sign day: ",
]
S_EN = [
    "20s whisper-range-only call test",
    "two-beat inhale consonant burst frame",
    "root-down larynx-steady monologue",
    "ear-canal pressure vowel sweep check",
    "phrase tails to HRV pacing",
]

P_KO = [
    "첫 지하 방습 스튜디오 주 ",
    "고습도 염해 해안 녹화 ",
    "첫 진공 챔버 무향 ",
    "모래 폭풍 페스트 고글 MC ",
    "혹한 결빙 성대 워밍 ",
    "첫 이산화탄소 고농도 홀 ",
    "뇌운 30km 대피 방송 ",
    "첫 개인 입체음향 극장 ",
    "고속도로 SA 야간 안내 ",
    "첫 뇌파 동기 리허설 ",
    "럭비장 녹화 방호 주 ",
    "첫 시민천문대 사일런트 쇼 ",
    "정전 자가발전 백업 녹음 ",
    "분지 역온층 수증기 보이스 ",
    "첫 촉각 피드백 슈트 캡처 ",
    "메이지 고목 반향 보정 ",
    "첫 오디오 DNA 워터마크 세션 ",
    "야간 공항 활주로 라이트 VO ",
    "첫 분산형 태그라인 동기 주 ",
    "첫 청음권 월렛 서명일 ",
]
S_KO = [
    "20초 속삭임 음역만 통화 테스트",
    "흡기 2박자 자음 연타 안정 틀",
    "혀뿌리 침강 후두 안정 모노로그",
    "이도압 밸런스 모음 스윕 점검",
    "심박 변동에 맞춘 어미 길이",
]

P_ZH = [
    "首次地下防潮录音棚周：",
    "高湿盐雾海岸录制：",
    "首次真空舱消声日：",
    "沙尘暴音乐节护目镜主持：",
    "极寒冰点声带热身：",
    "首次高二氧化碳大厅排练：",
    "雷暴云30公里撤离直播：",
    "首次个人空间音频剧场：",
    "高速公路服务区夜间播报：",
    "首次脑电同步排练：",
    "橄榄球场录制防护周：",
    "首次市民天文台静音演出：",
    "停电自发电备份录音：",
    "盆地逆温层蒸汽声：",
    "首次触觉反馈服采集：",
    "明治古木混响校正：",
    "首次声纹DNA水印场次：",
    "夜间机场跑道灯口播：",
    "首次分布式标语同步周：",
    "首次收听权钱包签名日：",
]
S_ZH = [
    "20秒耳语音域纯通话测试",
    "吸气两拍的辅音连打稳定框",
    "舌根下沉喉位稳定独白",
    "耳道压力平衡母音扫频",
    "按心率变异调整句尾长度",
]

BATCH15_JA_SEEDS: list[tuple[str, str, str]] = []
BATCH15_EN_TITLES: list[str] = []
BATCH15_KO_TITLES: list[str] = []
BATCH15_ZH_TITLES: list[str] = []

for pi, pja in enumerate(P_JA):
    for si, sja in enumerate(S_JA):
        idx = pi * len(S_JA) + si
        n = 1201 + idx
        slug = f"voice-guide-{n:02d}"
        ja_t = pja + sja
        ja_b = (
            f"{ja_t}。"
            "AI TARNAR Voice School（Japan Music Tourism）の実践メモです。"
            "検索されやすいキーワードをタイトルに織り込み、旅・現場・配信のどれでも短時間で続けられる形にしています。"
        )
        BATCH15_JA_SEEDS.append((slug, ja_t, ja_b))
        BATCH15_EN_TITLES.append(P_EN[pi] + S_EN[si])
        BATCH15_KO_TITLES.append(P_KO[pi] + S_KO[si])
        BATCH15_ZH_TITLES.append(P_ZH[pi] + S_ZH[si])
