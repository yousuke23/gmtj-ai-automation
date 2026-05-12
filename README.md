# GMTJ AI Automation

## 超初心者の方へ（最初に読む）

**[docs/START_HERE-超初心者.md](docs/START_HERE-超初心者.md)** を開いて、上から順にやってください。  

### 今すぐ（Mac で最速起動）

**手順の全文（コピペ用コマンド付き）:** **[deploy/QUICKSTART-サービス開始.md](deploy/QUICKSTART-サービス開始.md)**  
**起動後〜パイロット開始（チェックリスト）:** **[deploy/SERVICE-LAUNCH.md](deploy/SERVICE-LAUNCH.md)**  
**Docker不要ならスキップして問題ありません**（`kb` / `docs` / `make ci` などは Docker なしで進められます）。

チェック用: **[docs/チェックリスト-初日.md](docs/チェックリスト-初日.md)**（末尾に任意の「2日目」もあり）  
用語: **[docs/glossary.md](docs/glossary.md)** · 運用短版: **[docs/operations-runbook.md](docs/operations-runbook.md)** · **ドキュメント目次: [docs/README.md](docs/README.md)**

### 主要フォルダ（迷ったらここ）

| フォルダ | 役割の一言 |
|----------|------------|
| `kb/` | コンシェルジュAIのルール・テンプレ（日英韓）・地域メモ |
| `tour/` | ゲスト向け日英シート・スタッフRunbook・**参加前チェック**（`checklist-packing-izu-san.md`） |
| `marketing/` | マーケ案・短文例・キーワード種（`keywords-seed.md`）・**コンテンツ柱**（`content-pillars.md`） |
| `eval/` | ゴールデン質問・**採点ルーブリック**・インシデント記録 |
| `scripts/` | `kb` テンプレ検証などの小さなスクリプト |
| `deploy/` | 社内 Open WebUI・nginx・Caddy・ZIP・**[SECURITY.md](deploy/SECURITY.md)** · **起動: [QUICKSTART](deploy/QUICKSTART-サービス開始.md)** · **開始まで: [SERVICE-LAUNCH](deploy/SERVICE-LAUNCH.md)** |

## リポジトリルート（これが答え）

このフォルダ **`GMTJ-AI-Automation`** が **リポジトリルート** です。  
ルートの目印は、**この `README.md` と `CLAUDE.md` が同じ階層にあること**。

### フルパス（コピー用）

```text
/Users/tarnar/Desktop/GMTJ-AI-Automation
```

## Cursor で開く手順

1. Cursor メニュー **File → Open Folder…**（日本語: **ファイル → フォルダーを開く**）
2. 上記パスを選ぶ（Finder なら **デスクトップ → GMTJ-AI-Automation**）

## Claude Code（CLI）

統合ターミナルで:

```bash
cd /Users/tarnar/Desktop/GMTJ-AI-Automation
make ci
claude
```

`make ci` で **テンプレ整合**と **ゴールデン質問の件数**を確認できます（`make help` で他ターゲット表示）。

## Git をまだ初期化していない場合

この環境では Xcode コマンドラインツール未設定だと `git` が動かないことがあります。お使いの Mac のターミナルで:

```bash
xcode-select --install
cd /Users/tarnar/Desktop/GMTJ-AI-Automation
git init
git add .
git commit -m "chore: bootstrap GMTJ AI repo with CLAUDE.md and kb layout"
```

## 既存フォルダとの関係

デスクトップの **`GMTJ OS`** は PDF 資料用のフォルダです。**コード用のルートは本フォルダ**（`GMTJ-AI-Automation`）を使ってください。
