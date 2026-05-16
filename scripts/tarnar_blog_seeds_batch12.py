# -*- coding: utf-8 -*-
"""TARNAR blog seeds voice-guide-901 … 1000 (100 articles). SEO title variety (batch12)."""

P_JA = [
    "初グローバルキャスト読合せ週の",
    "カーボンニュートラル宣言ステージの",
    "メタバース会場リハの",
    "福祉施設ボラ演奏の",
    "学校安全啓発ラジオ週の",
    "災害訓練アナ併走日の",
    "国境越え子ども合唱の",
    "図書館サイレントライブの",
    "AI声優デュエット収録の",
    "地域観光英語案内週の",
    "初クルーズ船パフォーマンスの",
    "盆リモート礼拝配信の",
    "夜間工事騒音下リハの",
    "著作権説明会明け初声の",
    "多言語FAQ収録ラッシュの",
    "感音性難聴適応練初週の",
    "喉リハビリ科同行初週の",
    "ボイス相談ウィーク初日の",
    "字幕なし即興配信初回の",
    "年末スピーチ原稿締切週の",
]
S_JA = [
    "90秒エレベーターピッチ声出し",
    "呼称統一リーダー読み上げ練",
    "仮想客と会話体リズム枠",
    "小声クエスチョン応答だけの枠",
    "無音カウント8の沈黙保持",
]

P_EN = [
    "First global cast read-through week: ",
    "Carbon-neutral pledge stage: ",
    "Metaverse venue rehearsal: ",
    "Welfare facility volunteer gig: ",
    "School safety radio week: ",
    "Disaster-drill announcer shadow day: ",
    "Cross-border kids choir: ",
    "Library silent live: ",
    "AI voice-actor duet session: ",
    "Regional tourism English week: ",
    "First cruise-ship performance: ",
    "Remote Bon memorial stream: ",
    "Rehearsal under night construction noise: ",
    "First voice after rights briefing: ",
    "Multilingual FAQ recording rush: ",
    "First week adapting to sensorineural loss: ",
    "First week with voice rehab escort: ",
    "Voice consult week day one: ",
    "First no-caption improv stream: ",
    "Year-end speech draft deadline week: ",
]
S_EN = [
    "90s elevator pitch out loud",
    "honorifics-unified leader read drill",
    "conversational rhythm grid with virtual guests",
    "whisper Q&A response frame only",
    "silent count-of-eight hold",
]

P_KO = [
    "첫 글로벌 캐스트 리드스루 주 ",
    "탄소중립 선언 스테이지 ",
    "메타버스 공연장 리허 ",
    "복지시설 봉사 연주 ",
    "학교 안전 홍보 라디오 주 ",
    "재난 훈련 아나 따라하기 날 ",
    "국경 넘는 아동 합창 ",
    "도서관 사일런트 라이브 ",
    "AI 성우 듀엣 녹음 ",
    "지역 관광 영어 안내 주 ",
    "첫 크루즈 선상 공연 ",
    "원격 봉 제사 방송 ",
    "야간 공사 소음 아래 리허 ",
    "저작권 설명회 후 첫 발성 ",
    "다국어 FAQ 녹음 러시 ",
    "난청 적응 첫 주 ",
    "성대 재활 동행 첫 주 ",
    "보이스 상담 위크 첫날 ",
    "자막 없는 즉흥 방송 첫회 ",
    "연말 스피치 원고 마감 주 ",
]
S_KO = [
    "90초 엘리베이터 피치 발성",
    "호칭 통일 리더 낭독 연습",
    "가상 청중과 대화체 리듬 틀",
    "속삭임 Q&A 응답만 틀",
    "무음 카운트 8 유지",
]

P_ZH = [
    "首次全球卡司读本周：",
    "碳中和宣言舞台：",
    "元宇宙场馆排练：",
    "福利设施志愿演出：",
    "校园安全广播周：",
    "防灾演练播报跟练日：",
    "跨国儿童合唱：",
    "图书馆静音现场：",
    "AI声优对录：",
    "地域观光英语讲解周：",
    "首次邮轮表演：",
    "远程盂兰法会直播：",
    "夜间施工噪音下排练：",
    "版权说明会后首次开嗓：",
    "多语FAQ录制高峰：",
    "感音神经性听损适应首周：",
    "嗓音康复陪同首周：",
    "声音咨询周首日：",
    "无字幕即兴直播首回：",
    "年终演讲稿截稿周：",
]
S_ZH = [
    "90秒电梯演讲出声",
    "称谓统一领读练习",
    "与虚拟观众对话节奏框",
    "仅小声问答回应框",
    "无声数8保持",
]

BATCH12_JA_SEEDS: list[tuple[str, str, str]] = []
BATCH12_EN_TITLES: list[str] = []
BATCH12_KO_TITLES: list[str] = []
BATCH12_ZH_TITLES: list[str] = []

for pi, pja in enumerate(P_JA):
    for si, sja in enumerate(S_JA):
        idx = pi * len(S_JA) + si
        n = 901 + idx
        slug = f"voice-guide-{n:02d}"
        ja_t = pja + sja
        ja_b = (
            f"{ja_t}。"
            "AI TARNAR Voice School（Japan Music Tourism）の実践メモです。"
            "検索されやすいキーワードをタイトルに織り込み、旅・現場・配信のどれでも短時間で続けられる形にしています。"
        )
        BATCH12_JA_SEEDS.append((slug, ja_t, ja_b))
        BATCH12_EN_TITLES.append(P_EN[pi] + S_EN[si])
        BATCH12_KO_TITLES.append(P_KO[pi] + S_KO[si])
        BATCH12_ZH_TITLES.append(P_ZH[pi] + S_ZH[si])
