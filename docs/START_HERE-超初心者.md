# GMTJ AI 自動化 — 超初心者向けスタートガイド

このファイルは **ゼロから順番に** 読んでください。  
用語は初めて出るときに短く説明します。

---

## 0. 用語ミニ辞典（先にざっくり）

| 用語 | 意味 |
|------|------|
| **フォルダ** | ファイルを入れる箱。Finder で見えるもの。 |
| **リポジトリ（リポ）** | プロジェクトの「公式フォルダ」。履歴（Git）を付けられる。 |
| **リポジトリのルート** | そのプロジェクトの **いちばん上のフォルダ**。`CLAUDE.md` がある場所。 |
| **ターミナル** | 文字でパソコンに命令する黒い（または白い）画面。 |
| **Cursor** | プログラムを書いたり、AIと一緒に作業するためのアプリ（VS Code 系）。 |
| **Claude Code** | ターミナルから動く AI 作業アシスタント（Anthropic）。 |
| **Git** | 変更履歴を残すための仕組み。`git` コマンドで使う。 |

---

## 1. いまのプロジェクトはどこ？

**リポジトリのルート（＝いちばん上）**は次のフォルダです。

```text
/Users/tarnar/Desktop/GMTJ-AI-Automation
```

**Finder で開く手順**

1. 画面下の **Finder** をクリック  
2. 左の一覧から **デスクトップ** をクリック  
3. **`GMTJ-AI-Automation`** というフォルダを探してダブルクリック  

中に `CLAUDE.md` や `README.md` が見えれば OK です。

> メモ: デスクトップに **`GMTJ OS`** という別フォルダがあっても大丈夫です。あちらは PDF などの資料用で、**作業用は `GMTJ-AI-Automation`** です。

---

## 2. Mac に「コマンドラインデベロッパツール」を入れる（初回だけ）

`git` を使うと、Mac が次のようなダイアログを出すことがあります。

> 「git を実行するにはコマンドラインデベロッパツールが必要です。インストールしますか？」

**おすすめ: 「インストール」を押す**

1. **インストール** をクリック  
2. 規約に同意  
3. **ダウンロードとインストールが終わるまで待つ**（Wi‑Fi 次第で数分〜）  
4. 終わったら **Mac を一度再起動**してもしなくてもよいですが、**ターミナルは一度閉じて開き直す**と確実です。

**終わったか確認（ターミナルで）**

1. **Spotlight**（`Command + スペース`）→ `ターミナル` と入力 → Enter  
2. 次をコピーして貼り付け → Enter:

```bash
git --version
```

`git version 2.x` のように表示されれば成功です。

---

## 3. Cursor を入れる（まだの場合）

1. ブラウザで Cursor の公式サイトを開き、アプリをダウンロードしてインストールします。  
2. 初回起動でアカウント作成やログインを求められたら、案内に従ってください。

---

## 4. Cursor でこのフォルダを「開く」（重要）

1. **Cursor** を起動  
2. メニュー **File（ファイル）** → **Open Folder…（フォルダーを開く）**  
3. 左のサイドバーで **Desktop（デスクトップ）** → **`GMTJ-AI-Automation`** を選ぶ  
4. **Open（開く）** をクリック  

**成功のサイン**

- 左にファイル一覧（`CLAUDE.md`, `kb`, `docs` など）が見える  
- 上のタイトルバーに `GMTJ-AI-Automation` と出る  

---

## 5. ターミナルを「このフォルダの中」で開く

### 方法A（おすすめ）: Cursor 内のターミナル

1. Cursor で **表示（View）** → **ターミナル（Terminal）**  
   - またはキーボード **Ctrl + `**（バッククォート。`@` の左のキー）  
2. 下にパネルが出たら、次を **そのままコピー**して Enter:

```bash
cd /Users/tarnar/Desktop/GMTJ-AI-Automation
pwd
```

`pwd` の結果が次であれば **正しい場所**です。

```text
/Users/tarnar/Desktop/GMTJ-AI-Automation
```

### 方法B: Finder から

1. Finder で `GMTJ-AI-Automation` を開く  
2. フォルダの中の **何もない空白** を右クリック  
3. メニューに **「ターミナルで開く」** があればそれを選ぶ（macOS の設定によっては出ません。そのときは方法A）

---

## 6. Git を始める（履歴を残す／GitHub に繋ぐ前の準備）

ターミナルで、まだ `GMTJ-AI-Automation` にいることを確認してから:

### 6-1. 初回だけ（あなたの名前を Git に登録）

**メールは公開されやすいので、GitHub 用のニックネームメールでも構いません。**

```bash
git config --global user.name "あなたの名前"
git config --global user.email "あなたのメール@example.com"
```

### 6-2. このフォルダで Git を有効化

```bash
cd /Users/tarnar/Desktop/GMTJ-AI-Automation
git init
```

### 6-3. 最初の保存（コミット）

```bash
git add .
git status
git commit -m "最初の保存: GMTJ用の土台ファイル"
```

- `git status` で **緑や追加予定のファイル**が見えれば OK  
- `commit` で **「何をしたか」** のメモが1つ付きます  

---

## 7. Claude Code を起動する

### 7-1. インストール済みか確認

```bash
claude --version
```

バージョンが表示されれば OK です。

### 7-2. 起動

```bash
cd /Users/tarnar/Desktop/GMTJ-AI-Automation
claude
```

初回はログインやブラウザ認証を求められることがあります。画面の指示に従ってください。

### 7-3. 最初に頼むと良いこと（例）

Claude Code が動いたら、次のような文章を **日本語で**打ってみてください。

```text
CLAUDE.md と kb/README.md と kb/policy.md を読んでください。
deploy/README.md を読み、社内PCで Docker が使える場合は
docker compose を試す準備ができているか確認してください。
```

（すでに `kb/templates/` が揃っているので、「新しい意図を1つ追加してテンプレも作って」など、**次の一歩**を依頼しても大丈夫です。）

---

## 8. 毎日のルーティン（慣れたら）

1. Cursor で `GMTJ-AI-Automation` を開く  
2. ターミナルで `cd /Users/tarnar/Desktop/GMTJ-AI-Automation`  
3. `claude` を起動  
4. やりたいことを日本語で依頼  
5. 終わったら `git add .` → `git commit -m "今日やったこと"`  

---

## 9. つまずいたとき

| 症状 | 試すこと |
|------|----------|
| `git: command not found` | セクション2の開発者ツールをインストール |
| `pwd` が違うフォルダ | `cd /Users/tarnar/Desktop/GMTJ-AI-Automation` をもう一度 |
| `claude: command not found` | Claude Code の公式手順で再インストール |
| 何をしていいか分からない | このファイルの **7-3** をコピペする |

---

## 10. このリポジトリに最初から入っているもの（2026-05 時点の目安）

- **`CLAUDE.md`** … Claude Code へのプロジェクト説明（21事業・14コンシェルジュ・フォルダの意味）  
- **`kb/README.md`** … `kb/` フォルダの入口（どのファイルを先に読むか）  
- **`docs/README.md`** … `docs/` フォルダの目次  
- **`docs/operations-runbook.md`** … 社内MVP運用の短い Runbook  
- **`kb/intents.yaml`** … 質問の「意図」分類（一覧）  
- **`kb/templates/`** … 意図ごとの返答の型（日本語・英語の `.md`、韓国語は `.ko.md`）  
- **`kb/tours/`** … ツアー連携FAQなど（コンシェルジュ14へ供給）  
- **`kb/regions/`** … 国内エリア骨子（数値断定なし）  
- **`kb/brand/`** … ブランド文案ドラフト（`#JapanMusicTourism` 等）  
- **`tour/`** … 01ツアー：ゲスト向け英語・**日本語**シート・スタッフRunbook  
- **`marketing/90day-ideas.md`** … マーケのたたき台＋短文例  
- **`marketing/keywords-seed.md`** … SEO用キーワード種（検索数は未計測のドラフト）  
- **`eval/golden-questions.md`** … 品質確認用の質問セット（v0.5 は25問・韓国語2問含む）  
- **`eval/scoring-rubric.md`** … ゴールデン質問の採点ルーブリック  
- **`eval/incidents.md`** … インシデント記録テンプレ  
- **`deploy/SECURITY.md`** … 認証・秘密・ログの原則  
- **`docs/business-map.md`** … 21事業の1行マップ  

---

## 11. 社内チャット（Open WebUI）— 利用する場合

**Open WebUI を使う**場合の手順です（Docker Desktop が必要なときがあります）。

### 11-A. いちばん短い手順（まずここ）

**[deploy/QUICKSTART-サービス開始.md](../deploy/QUICKSTART-サービス開始.md)**（Docker Desktop 起動 → `deploy` で `cp` / `docker compose` → ブラウザ8080）。

起動できたら、**[deploy/SERVICE-LAUNCH.md](../deploy/SERVICE-LAUNCH.md)** のフェーズに沿って、管理者設定・モデル・Knowledge・スモーク・招待前ゲートまで進めてください。

動作確認だけならルートで **`make check-webui`**（HTTP 200 を確認）。

補足: **Cursor のこのチャットからは、あなたの Mac 上の Docker を操作できません**（コンテナの実起動は、あなたのターミナルでの実行が必要です）。

### 11-B. 全体像とナレッジ

1. 手順の全体像・オプション: **`deploy/README.md`**（先頭に QUICKSTART / SERVICE-LAUNCH へのリンクあり）  
2. `kb` をチャットのナレッジに載せる詳細: **`deploy/openwebui-knowledge.md`**  
3. **Anthropic / モデル ID が出ないとき:** **`deploy/openwebui-anthropic-connection.md`**  
4. **本番に近い「サービス公開」**は **`deploy/SECURITY.md`**（VPN・認証・人間承認）を前提にすること  

### 11-C. ZIP を作る（Open WebUI の Knowledge 用）

ターミナルで:

```bash
cd /Users/tarnar/Desktop/GMTJ-AI-Automation
make kb-zip
```

（`make kb-zip` は `deploy/package-kb-for-knowledge.sh` と同じです。**Open WebUI に載せる ZIP は `deploy/gmtj-kb-for-openwebui.zip` を優先**し、エラーになる場合は `deploy/openwebui-knowledge.md` を参照してください。）

---

## 次に進む

セクション **2 → 4 → 5 → 6 → 7** を上から順にやれば、一通り「始めて」から立ち上がれます。  
どこかで止まったら、**止まったセクション番号**と、ターミナルに出た **赤いエラーの全文** を控えて質問してください。
