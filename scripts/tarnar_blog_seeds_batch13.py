# -*- coding: utf-8 -*-
"""TARNAR blog seeds voice-guide-1001 … 1100 (100 articles). SEO title variety (batch13)."""

P_JA = [
    "初宇宙ビデオコール収録の",
    "海底ケーブル遅延配信週の",
    "極夜ツアー日照補正週の",
    "砂漠フェス防塵マスクの",
    "ジャングル湿度95パーセントの",
    "高山病リスク声量調整の",
    "初水中パフォーマンスの",
    "火山灰飛散警報下の",
    "オーロラ撮影サイレントMCの",
    "初AI翻訳即席リップの",
    "量子暗号回線試験週の",
    "初5GSA単独配信の",
    "衛星電話バックアップ日の",
    "初ブロックチェーン証明ライブの",
    "初NFTチケット入場案内の",
    "初カーボンクレジット公表ステージの",
    "初バイオメトリクス入場の",
    "初顔認証ゲート通過MCの",
    "初ドローンライトショー併走の",
    "初都市型無音フェスの",
]
S_JA = [
    "30秒無編集ワンカット声出し",
    "遅延200ms想定の語尾伸ばし練",
    "小声域だけの二部ハモリ枠",
    "マスク内結露拭きタイミング声",
    "湿度計と声の粘りメモ同期",
]

P_EN = [
    "First space video-call recording: ",
    "Subsea-cable latency stream week: ",
    "Polar-night tour daylight-correct week: ",
    "Desert fest dust-mask day: ",
    "Jungle 95% humidity day: ",
    "Altitude-risk volume scaling: ",
    "First underwater performance: ",
    "Under volcanic ash advisory: ",
    "Aurora shoot silent MC: ",
    "First AI live-translate lip sync: ",
    "Quantum-secure line test week: ",
    "First 5G SA solo stream: ",
    "Sat-phone backup day: ",
    "First on-chain provenance live: ",
    "First NFT ticket gate script: ",
    "First carbon-credit disclosure stage: ",
    "First biometric entry flow: ",
    "First face-gate pass MC: ",
    "First drone-light-show co-run: ",
    "First urban silent fest: ",
]
S_EN = [
    "30s no-edit one-take out loud",
    "tail stretch for 200ms delay",
    "two-part hum frame whisper-only",
    "voice timing with mask wipe",
    "humidity meter vs vocal stickiness log",
]

P_KO = [
    "첫 우주 화상 녹화 ",
    "해저 케이블 지연 방송 주 ",
    "극야 투어 일조 보정 주 ",
    "사막 페스트 방진 마스크 ",
    "정글 습도 95퍼센트 ",
    "고산병 위험 볼륨 조절 ",
    "첫 수중 퍼포먼스 ",
    "화산재 비행 주의하 ",
    "오로라 촬영 사일런트 MC ",
    "첫 AI 통역 립싱크 ",
    "양자 암호 회선 테스트 주 ",
    "첫 5G SA 단독 방송 ",
    "위성폰 백업 날 ",
    "첫 온체인 증명 라이브 ",
    "첫 NFT 티켓 게이트 안내 ",
    "첫 탄소 크레딧 공개 스테이지 ",
    "첫 바이오메트릭 입장 ",
    "첫 얼굴인식 게이트 MC ",
    "첫 드론 라이트쇼 동반 ",
    "첫 도시형 무음 페스 ",
]
S_KO = [
    "30초 무편집 원테이크 발성",
    "200ms 지연 꼬리 늘리기 연습",
    "속삭임만 이부 화음 틀",
    "마스크 결로 닦기 타이밍 발성",
    "습도계와 목소리 끈적임 메모 동기",
]

P_ZH = [
    "首次太空视频连线录制：",
    "海底光缆延迟直播周：",
    "极夜巡演日照校正周：",
    "沙漠音乐节防尘口罩：",
    "丛林湿度95%日：",
    "高反风险音量调节：",
    "首次水下表演：",
    "火山灰预警下：",
    "极光拍摄静音主持：",
    "首次AI翻译即兴对嘴：",
    "量子加密线路测试周：",
    "首次5G SA独播：",
    "卫星电话备份日：",
    "首次链上存证现场：",
    "首次NFT门票闸机口播：",
    "首次碳积分公开舞台：",
    "首次生物识别入场：",
    "首次人脸闸机主持：",
    "首次无人机灯光秀伴走：",
    "首次城市静音音乐节：",
]
S_ZH = [
    "30秒无剪辑一条过出声",
    "按200ms延迟拉长字尾练习",
    "仅小声区的二部和声框",
    "口罩起雾擦拭与发声节奏",
    "湿度计与嗓音黏滞度同步记录",
]

BATCH13_JA_SEEDS: list[tuple[str, str, str]] = []
BATCH13_EN_TITLES: list[str] = []
BATCH13_KO_TITLES: list[str] = []
BATCH13_ZH_TITLES: list[str] = []

for pi, pja in enumerate(P_JA):
    for si, sja in enumerate(S_JA):
        idx = pi * len(S_JA) + si
        n = 1001 + idx
        slug = f"voice-guide-{n:02d}"
        ja_t = pja + sja
        ja_b = (
            f"{ja_t}。"
            "AI TARNAR Voice School（Japan Music Tourism）の実践メモです。"
            "検索されやすいキーワードをタイトルに織り込み、旅・現場・配信のどれでも短時間で続けられる形にしています。"
        )
        BATCH13_JA_SEEDS.append((slug, ja_t, ja_b))
        BATCH13_EN_TITLES.append(P_EN[pi] + S_EN[si])
        BATCH13_KO_TITLES.append(P_KO[pi] + S_KO[si])
        BATCH13_ZH_TITLES.append(P_ZH[pi] + S_ZH[si])
