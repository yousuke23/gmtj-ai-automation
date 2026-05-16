# -*- coding: utf-8 -*-
"""TARNAR blog seeds voice-guide-1301 … 1400 (100 articles). SEO title variety (batch16)."""

P_JA = [
    "初超音速客室噪度測定週の",
    "深海潜水艇艦橋通話の",
    "初ARグラス字幕読上げ配信の",
    "台風眼壁通過静音ホストの",
    "初低温液化ガス搬送説明の",
    "砂漠夜間冷却合金マイクの",
    "初衛星ISL中継MCの",
    "谷間集音逆位相補正の",
    "初脳内BCI無声発話デモの",
    "停波海岸潮汐サイレン併走の",
    "初量子認証会員登録盆の",
    "雪崩警報避難所アナウンスの",
    "初ナノファイバー吸音壁収録の",
    "市民科学夜空声ログの",
    "初自己組織マルチキャスト合唱の",
    "古寺院鐘前無拡声案内の",
    "初音楽NFT二次市場告知の",
    "極低温半導体工場見学の",
    "初分散レッスン5拠点同期の",
    "初音波ガイドレール収録の",
]
S_JA = [
    "8小節だけの声帯コンディション通報",
    "鼻腔閉鎖ONOFF切替比較枠",
    "横隔膜フラッターの拍子検証",
    "会議室混響RT60一言校正",
    "唾液pHと声の滑りメモ同期",
]

P_EN = [
    "First supersonic-cabin noise survey week: ",
    "Deep-sub bridge comms: ",
    "First AR-glass subtitle read-aloud stream: ",
    "Typhoon eyewall silent host pass: ",
    "First cryogenic LNG transfer brief: ",
    "Desert night cooled-alloy mic: ",
    "First satellite ISL relay MC: ",
    "Valley pickup inverse-phase fix: ",
    "First intracranial BCI silent-speech demo: ",
    "Still-sea coast with tidal sirens: ",
    "First quantum-auth member desk: ",
    "Avalanche-alert shelter PA: ",
    "First nanofiber absorber-wall capture: ",
    "Citizen-science night-sky voice log: ",
    "First self-organizing multicast choir: ",
    "Ancient-temple bell unamplified guide: ",
    "First music-NFT secondary-market pitch: ",
    "Ultra-cold fab tour VO: ",
    "First split-lesson five-site sync: ",
    "First sonic-guided rail capture: ",
]
S_EN = [
    "8-bar vocal-fold status callout",
    "nasal occlusion on/off compare frame",
    "diaphragm flutter tempo check",
    "one-line RT60 tweak in a meeting room",
    "saliva pH vs glide memo sync",
]

P_KO = [
    "첫 초음속 객실 소음 측정 주 ",
    "심해 잠수함 함교 통화 ",
    "첫 AR 글라스 자막 낭독 방송 ",
    "태풍 안벽 통과 사일런트 호스트 ",
    "초저온 액화가스 운송 설명 ",
    "사막 야간 냉각 합금 마이크 ",
    "첫 위성 ISL 중계 MC ",
    "골짜기 집음 역위상 보정 ",
    "첫 뇌내 BCI 무성 발화 데모 ",
    "정파 해안 조석 사이렌 동반 ",
    "첫 양자 인증 회원 등록 데스크 ",
    "눈사태 경보 대피소 안내 ",
    "첫 나노파이버 흡음벽 캡처 ",
    "시민과학 야하늘 보이스 로그 ",
    "첫 자기조직 멀티캐스트 합창 ",
    "고사찰 종 앞 무확성 안내 ",
    "첫 음악 NFT 2차 시장 공지 ",
    "초저온 반도체 공장 견학 ",
    "첫 분산 레슨 5거점 동기 ",
    "첫 음파 가이드 레일 캡처 ",
]
S_KO = [
    "8마디만 성대 컨디션 통보",
    "비강 폐쇄 ON/OFF 비교 틀",
    "횡격막 플러터 박자 검증",
    "회의실 잔향 RT60 한 줄 보정",
    "타액 pH와 보이스 미끄럼 메모 동기",
]

P_ZH = [
    "首次超音速客舱噪声测量周：",
    "深海潜艇舰桥通话：",
    "首次AR眼镜字幕朗读直播：",
    "台风眼壁穿越静音主持：",
    "首次低温液化气体搬运说明：",
    "沙漠夜间冷却合金麦克风：",
    "首次卫星ISL中继主持：",
    "山谷拾音反相校正：",
    "首次颅内BCI无声发音演示：",
    "静海海岸与潮汐警报并行：",
    "首次量子认证会员登记台：",
    "雪崩预警避难所广播：",
    "首次纳米纤维吸声墙采集：",
    "市民科学夜空声音日志：",
    "首次自组织多播合唱：",
    "古寺钟前无扩声导览：",
    "首次音乐NFT二级市场宣讲：",
    "极低温半导体工厂参观口播：",
    "首次分散授课五地同步：",
    "首次声波导轨采集：",
]
S_ZH = [
    "仅8小节的声带状态通报",
    "鼻腔闭合开闭对比框",
    "横膈 flutter 节拍验证",
    "会议室混响RT60一句校正",
    "唾液pH与嗓音滑移备忘同步",
]

BATCH16_JA_SEEDS: list[tuple[str, str, str]] = []
BATCH16_EN_TITLES: list[str] = []
BATCH16_KO_TITLES: list[str] = []
BATCH16_ZH_TITLES: list[str] = []

for pi, pja in enumerate(P_JA):
    for si, sja in enumerate(S_JA):
        idx = pi * len(S_JA) + si
        n = 1301 + idx
        slug = f"voice-guide-{n:02d}"
        ja_t = pja + sja
        ja_b = (
            f"{ja_t}。"
            "AI TARNAR Voice School（Japan Music Tourism）の実践メモです。"
            "検索されやすいキーワードをタイトルに織り込み、旅・現場・配信のどれでも短時間で続けられる形にしています。"
        )
        BATCH16_JA_SEEDS.append((slug, ja_t, ja_b))
        BATCH16_EN_TITLES.append(P_EN[pi] + S_EN[si])
        BATCH16_KO_TITLES.append(P_KO[pi] + S_KO[si])
        BATCH16_ZH_TITLES.append(P_ZH[pi] + S_ZH[si])
