# GMTJ AI Automation

## 超初心者の方へ（最初に読む）

**[docs/START_HERE-超初心者.md](docs/START_HERE-超初心者.md)** を開いて、上から順にやってください。  

### メインの進め方（Open WebUI / Docker 不要）

運用方針は **[CLAUDE.md](CLAUDE.md)**（**Open WebUI / Docker は当面使わず**）。作業の正は **`kb/`**・**`tour/`**・**`marketing/`**・**`eval/`** とルートの **`make ci`**。事業マップ・入口は **[docs/business-map.md](docs/business-map.md)**。

**「サービス開始」（Docker なし）の最小:** ルートで **`make ci`** が通ること＋必要なら **`make kb-zip`** で `deploy/gmtj-kb-for-knowledge.zip` を更新（別チャネルの RAG 用素材）。

チェック用: **[docs/チェックリスト-初日.md](docs/チェックリスト-初日.md)**（末尾に任意の「2日目」もあり）  
用語: **[docs/glossary.md](docs/glossary.md)** · 運用短版: **[docs/operations-runbook.md](docs/operations-runbook.md)** · **ドキュメント目次: [docs/README.md](docs/README.md)**

### 任意: Open WebUI（Docker を使う場合だけ）

社内でチャット UI を試す人向け。**使わないなら読まなくてよい。** 手順は **[deploy/README.md](deploy/README.md)**（`make open-webui` / `fast-up.sh` はここに従う）。

### 主要フォルダ（迷ったらここ）

| フォルダ | 役割の一言 |
|----------|------------|
| `kb/` | コンシェルジュAIのルール・テンプレ（日英韓）・地域メモ |
| `tour/` | ゲスト向け日英シート・スタッフRunbook・**参加前チェック**（`checklist-packing-izu-san.md`） |
| `marketing/` | マーケ案・短文例・キーワード種（`keywords-seed.md`）・**コンテンツ柱**（`content-pillars.md`） |
| `eval/` | ゴールデン質問・**採点ルーブリック**・インシデント記録 |
| `scripts/` | `kb` テンプレ検証などの小さなスクリプト |
| `deploy/` | **任意**（Docker 利用時）: compose・nginx・Caddy・ZIP・**[SECURITY.md](deploy/SECURITY.md)**。使わない場合は **[CLAUDE.md](CLAUDE.md)** どおりスキップ可 |

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

### Cursor から起動（「ここで出す」）

1. このリポを **フォルダーとして開いている**ことを確認する（左に `GMTJ-AI-Automation` のルート）  
2. **`Cmd + Shift + P`** → **「Tasks: Run Task」**（**タスクの実行**）  
3. **「Claude Code: 起動 (このフォルダで)」** を選ぶ  

統合ターミナルが開き、**`${workspaceFolder}`**（＝いま開いているこのフォルダ）で **`claude`** が起動します。

手で打つ場合（統合ターミナル）:

```bash
cd /Users/tarnar/Desktop/GMTJ-AI-Automation
make ci
claude
```

`make ci` で **テンプレ整合**と **ゴールデン質問の件数**を確認できます（`make help` で他ターゲット表示）。

## 当面スプリント完了の確認（14・01・18）

条件の詳細は **[CLAUDE.md](CLAUDE.md) の「完了の定義」**。一覧・フォルダ入口は **[docs/business-map.md](docs/business-map.md)** と **[docs/README.md](docs/README.md)**（作業の優先順）。

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
