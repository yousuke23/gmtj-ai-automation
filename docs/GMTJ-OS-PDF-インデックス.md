# GMTJ OS3 — PDF インデックス（ローカル管理用）

**場所:** デスクトップの **`GMTJ OS`** フォルダ（Git 管理外）。このファイルは **パスの正本**として `GMTJ-AI-Automation` リポ内に置く。

別のパスに PDF を置く場合は、確認スクリプト実行時に  
`GMTJ_OS_ROOT="/path/to/GMTJ OS" bash scripts/verify-gmtj-os-pdfs.sh`  
のように **`GMTJ_OS_ROOT`** を指定する（スクリプト先頭の既定値も編集可）。

Finder でフォルダを開く:

```bash
open "/Users/tarnar/Desktop/GMTJ OS"
```

存在確認だけ（ターミナル）:

```bash
bash scripts/verify-gmtj-os-pdfs.sh
```

**ブラウザで動かす OS シェル（PDF ではなく運用UI）:** リポの `site/gmtj-os/`（サインイン後にデスクトップ・OS3モジュール・メモ等）。`http://127.0.0.1:8888/site/gmtj-os/`。PDF を同梱ビューしたい場合のみ `site/gmtj-os/pdfs/README.md` に従い `pdfs/` へコピー（通常は不要）。

---

## 一覧（GMTJ OS3_1 … 3_10）

| # | ファイル | フルパス | 要約メモ | 最終確認日 | 備考 |
|---|----------|----------|----------|------------|------|
| 1 | GMTJ OS3_1.pdf | `/Users/tarnar/Desktop/GMTJ OS/GMTJ OS3_1.pdf` | | | |
| 2 | GMTJ OS3_2.pdf | `/Users/tarnar/Desktop/GMTJ OS/GMTJ OS3_2.pdf` | | | |
| 3 | GMTJ OS3_3.pdf | `/Users/tarnar/Desktop/GMTJ OS/GMTJ OS3_3.pdf` | | | |
| 4 | GMTJ OS3_4.pdf | `/Users/tarnar/Desktop/GMTJ OS/GMTJ OS3_4.pdf` | | | |
| 5 | GMTJ OS3_5.pdf | `/Users/tarnar/Desktop/GMTJ OS/GMTJ OS3_5.pdf` | | | |
| 6 | GMTJ OS3_6.pdf | `/Users/tarnar/Desktop/GMTJ OS/GMTJ OS3_6.pdf` | | | |
| 7 | GMTJ OS3_7.pdf | `/Users/tarnar/Desktop/GMTJ OS/GMTJ OS3_7.pdf` | | | |
| 8 | GMTJ OS3_8.pdf | `/Users/tarnar/Desktop/GMTJ OS/GMTJ OS3_8.pdf` | | | |
| 9 | GMTJ OS3_9.pdf | `/Users/tarnar/Desktop/GMTJ OS/GMTJ OS3_9.pdf` | | | |
| 10 | GMTJ OS3_10.pdf | `/Users/tarnar/Desktop/GMTJ OS/GMTJ OS3_10.pdf` | | | |

---

## 運用メモ

- **更新版が出たら** 行を追加するか、ファイル名規則（`OS3_11` など）を決めてこの表を拡張する。  
- **Open WebUI の Knowledge に載せるか**は別判断（PDF のサイズ・秘匿・版管理）。載せる場合は `kb/policy.md` と整合を取る。  
- **バックアップ**は iCloud／社内ストレージの方針に従う（このリポには PDF をコミットしない）。
