# -*- coding: utf-8 -*-
"""TARNAR blog seeds voice-guide-601 … 700 (100 articles). SEO title variety (batch9)."""

P_JA = [
    "冬ツアー喉乾燥週の",
    "盆踊り司会マイク日の",
    "初海外フェス通訳伴走週の",
    "リングライト直視収録の",
    "喉仮説検査後初発声の",
    "早朝ラジオ体操コールの",
    "盆DJセット明けの",
    "雪道移動ライブ前の",
    "除夜鐘カウント合わせの",
    "初詣参道ライブの",
    "成人式祝賀演奏前の",
    "運動会応援曲リハの",
    "花火大会ナレーション日の",
    "七夕短冊朗読会の",
    "運転中ボイトレ禁止週の",
    "空港ラウンジ小声練の",
    "温泉街歩き歌明けの",
    "初任給ライブチケット週の",
    "台風接近屋外中止判断日の",
    "紅白リハ初日の",
]
S_JA = [
    "湿度60メモで保湿目標",
    "司会原稿と息継ぎだけの通し",
    "通訳ワードリスト読み上げウォーム",
    "視線オフ45秒瞼ストレッチ",
    "医師指示どおりの小声スケール",
]

P_EN = [
    "Winter tour dry-throat week: ",
    "Bon dance MC mic day: ",
    "First overseas fest interpreter week: ",
    "Ring-light stare recording: ",
    "First phonation after larynx check: ",
    "Early radio calisthenics call: ",
    "After Bon DJ set: ",
    "Before snowy-road gig: ",
    "New Year’s Eve bell count-in: ",
    "First shrine approach live: ",
    "Before coming-of-age ceremony: ",
    "Sports-day cheer rehearsal: ",
    "Fireworks narration day: ",
    "Tanabata strip reading: ",
    "No in-car vocal drill week: ",
    "Airport lounge whisper practice: ",
    "After onsen-town walk-and-sing: ",
    "First-paycheck ticket week: ",
    "Typhoon outdoor cancel call: ",
    "Kohaku first rehearsal day: ",
]
S_EN = [
    "humidity 60% hydration memo",
    "run script with breath marks only",
    "interpreter word-list warm read",
    "45s eyes-off lid stretch",
    "quiet scale per doctor note",
]

P_KO = [
    "겨울 투어 목 건조 주 ",
    "봉오도리 사회 마이크 날 ",
    "첫 해외 페스 통역 동행 주 ",
    "링라이트 정면 녹음 ",
    "후두 검사 후 첫 발성 ",
    "새벽 라디오체조 콜 ",
    "봉 DJ 세트 다음 날 ",
    "눈길 이동 라이브 전 ",
    "제야의 종 카운트 ",
    "첫 신사参道 라이브 ",
    "성인식 축하 연주 전 ",
    "운동회 응원곡 리허 ",
    "불꽃 나레이션 날 ",
    "칠석 단편 낭독 ",
    "운전 중 보이트레 금지 주 ",
    "공항 라운지 속삭임 연습 ",
    "온천가 산책 노래 다음 날 ",
    "첫 월급 티켓 주 ",
    "태풍 야외 중지 판단일 ",
    "홍백 리허 첫날 ",
]
S_KO = [
    "습도 60% 보습 메모",
    "대본과 호흡만 통돌이",
    "통역 단어장 워밍 리드",
    "시선 오프 45초 눈꺼풀 스트레칭",
    "의사 지시 소음 스케일",
]

P_ZH = [
    "冬季巡演咽干周：",
    "盆舞主持麦日：",
    "首次海外音乐节口译随行周：",
    "环形灯直视录制：",
    "喉部检查后首次发声：",
    "清晨广播体操口令：",
    "盆DJ set次日：",
    "雪路移动演出前：",
    "除夕钟声数拍：",
    "初诣参道演出：",
    "成人式祝贺演奏前：",
    "运动会应援曲排练：",
    "花火大会解说日：",
    "七夕短笺朗读会：",
    "禁止车内练声周：",
    "机场休息室小声练：",
    "温泉街边走边唱后：",
    "初薪买票周：",
    "台风临近户外取消判断日：",
    "红白彩排首日：",
]
S_ZH = [
    "湿度60%保湿备忘",
    "只过主持稿与换气",
    "口译词表热身朗读",
    "闭眼45秒眼睑拉伸",
    "遵医嘱小声音阶",
]

BATCH9_JA_SEEDS: list[tuple[str, str, str]] = []
BATCH9_EN_TITLES: list[str] = []
BATCH9_KO_TITLES: list[str] = []
BATCH9_ZH_TITLES: list[str] = []

for pi, pja in enumerate(P_JA):
    for si, sja in enumerate(S_JA):
        idx = pi * len(S_JA) + si
        n = 601 + idx
        slug = f"voice-guide-{n:02d}"
        ja_t = pja + sja
        ja_b = (
            f"{ja_t}。"
            "AI TARNAR Voice School（Japan Music Tourism）の実践メモです。"
            "検索されやすいキーワードをタイトルに織り込み、旅・現場・配信のどれでも短時間で続けられる形にしています。"
        )
        BATCH9_JA_SEEDS.append((slug, ja_t, ja_b))
        BATCH9_EN_TITLES.append(P_EN[pi] + S_EN[si])
        BATCH9_KO_TITLES.append(P_KO[pi] + S_KO[si])
        BATCH9_ZH_TITLES.append(P_ZH[pi] + S_ZH[si])
