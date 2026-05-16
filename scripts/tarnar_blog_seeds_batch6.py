# -*- coding: utf-8 -*-
"""TARNAR blog seeds voice-guide-301 … 400 (100 articles). SEO title variety (batch6)."""

P_JA = [
    "ラジオ収録当日の",
    "アイドル握手会前週の",
    "ストリングスセッション週の",
    "夏キャンプライブ明けの",
    "スピーカーチェック直前の",
    "ピアノ伴奏リハ初日の",
    "ストリートライブ雨上がりの",
    "オーディション最終日の",
    "メタル系セトリ週の",
    "アカペラ本番前の",
    "スタジオ追加人件日の",
    "声優収録ラッシュ週の",
    "教会ステージ本番の",
    "河川敷フェス朝の",
    "バンド加入1ヶ月の",
    "ヴィンテージマイク試用日の",
    "語学学校発表会週の",
    "バスキング指導日の",
    "エコー少なめ箱スタジオの",
    "年末カウントダウン前の",
]
S_JA = [
    "息量だけで決めるイントロ音量",
    "母音ラダーで喉の高さを固定",
    "モニター外し1曲だけの確認反復",
    "弱唱から強唱へ1フレーズの往復練",
    "口先の明瞭さを取り戻す短母音セット",
]

P_EN = [
    "Radio session day: ",
    "Pre handshake-event week: ",
    "Strings session week: ",
    "After summer camp show: ",
    "Before speaker check: ",
    "First piano rehearsal day: ",
    "After rain street gig: ",
    "Final audition day: ",
    "Metal setlist week: ",
    "Before a cappella finals: ",
    "Extra studio personnel day: ",
    "Voice-actor recording rush: ",
    "Church stage show: ",
    "Riverside fest morning: ",
    "One month in the band: ",
    "Vintage mic trial day: ",
    "Language school recital week: ",
    "Busking coaching day: ",
    "Dry room low echo: ",
    "Before NYE countdown: ",
]
S_EN = [
    "set intro level with breath only",
    "vowel ladder to lock larynx height",
    "one song without monitors, repeat",
    "one phrase soft-to-loud round trip",
    "short vowels for front clarity",
]

P_KO = [
    "라디오 녹음 당일 ",
    "핸드셰이크 이벤트 전 주 ",
    "스트링 세션 주 ",
    "캠프 라이브 다음 날 ",
    "스피커 체크 직전 ",
    "피아노 리허 첫날 ",
    "비 온 뒤 버스킹 ",
    "오디션 최종일 ",
    "메탈 셋리스트 주 ",
    "아카펠라 본선 전 ",
    "스튜디오 추가 인원일 ",
    "성우 녹음 러시 주 ",
    "교회 무대 본공연 ",
    "강변 페스 아침 ",
    "밴드 합류 한 달 ",
    "빈티지 마이크 시험일 ",
    "어학원 발표회 주 ",
    "버스킹 코칭일 ",
    "에코 적은 박스룸 ",
    "연말 카운트다운 전 ",
]
S_KO = [
    "호흡만으로 인트로 볼륨",
    "모음 사다리로 후두 높이 고정",
    "모니터 없이 한 곡 반복 확인",
    "약→강 한 구절 왕복",
    "짧은 모음으로 전방 명료성",
]

P_ZH = [
    "广播录音当天：",
    "握手会前一周：",
    "弦乐排练周：",
    "夏令营演出后：",
    "音响检查前：",
    "钢琴合排首日：",
    "雨后街头演出：",
    "终审面试日：",
    "金属曲目排练周：",
    "阿卡贝拉决赛前：",
    "录音棚加人日：",
    "声优连录周：",
    "教堂舞台正式场：",
    "河畔音乐节清晨：",
    "加入乐队满一月：",
    "复古麦克风试用日：",
    "语言学校发表会周：",
    "街演指导日：",
    "少混响小录音室：",
    "跨年倒数前：",
]
S_ZH = [
    "只用气息定前奏音量",
    "母音阶梯稳住喉位",
    "无监听单曲反复确认",
    "弱到强一句往返",
    "短母音找回唇齿清晰度",
]

BATCH6_JA_SEEDS: list[tuple[str, str, str]] = []
BATCH6_EN_TITLES: list[str] = []
BATCH6_KO_TITLES: list[str] = []
BATCH6_ZH_TITLES: list[str] = []

for pi, pja in enumerate(P_JA):
    for si, sja in enumerate(S_JA):
        idx = pi * len(S_JA) + si
        n = 301 + idx
        slug = f"voice-guide-{n:02d}"
        ja_t = pja + sja
        ja_b = (
            f"{ja_t}。"
            "AI TARNAR Voice School（Japan Music Tourism）の実践メモです。"
            "検索されやすいキーワードをタイトルに織り込み、旅・現場・配信のどれでも短時間で続けられる形にしています。"
        )
        BATCH6_JA_SEEDS.append((slug, ja_t, ja_b))
        BATCH6_EN_TITLES.append(P_EN[pi] + S_EN[si])
        BATCH6_KO_TITLES.append(P_KO[pi] + S_KO[si])
        BATCH6_ZH_TITLES.append(P_ZH[pi] + S_ZH[si])
