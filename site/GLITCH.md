# Glitch（グリッチ）でメインサイトを見る

**「グロック」＝ [Glitch](https://glitch.com/)** の前提で書いています。別サービス名の場合は教えてください。

## できること

- **`site/` 以下の静的 HTML**（`index.html`、多言語、`landing-tailwind*.html` など）を、Glitch の URL で閲覧できる形にできます。
- このリポジトリ用に、ルートの **`package.json`** の `npm start` が **`site/` を配信**するようになっています（[serve](https://github.com/vercel/serve)）。

## できない／注意（Glitch 上）

- **AI チャット**（`chat-proxy.py`）は Glitch のこの構成では動かしません。試用チャットはローカル（`python3 -m http.server` ＋ プロキシ）向けです。
- **機密**（API キー等）は Glitch に置かないでください。

## 手順（GitHub 連携が簡単）

1. このリポジトリを **GitHub に push** する（まだなら）。
2. [Glitch](https://glitch.com/) にログイン → **New project** → **Import from GitHub**（または GitHub の「Remix on Glitch」相当の導線）。
3. このリポジトリを選ぶ。Glitch が **`npm install` → `npm start`** を実行する。
4. 表示された **`https://（プロジェクト名）.glitch.me/`** を開く → 自動で `site/index.html` がトップ相当で表示されます（`serve` の既定動作）。

### 表示確認

- 日本語トップ: `/` または `/index.html`
- 英語: `/index-en.html`
- 韓国語: `/index-ko.html`
- 中国語: `/index-zh.html`

## 手順（`site/` だけを Glitch に置く場合）

1. Glitch で新規プロジェクトを作る。
2. エディタで **`site/` の中身だけ**をプロジェクト直下にコピー（`index.html`、`style.css`、`app.js` など）。
3. そのプロジェクトの `package.json` を次のようにする:

```json
{
  "scripts": { "start": "serve . --listen tcp://0.0.0.0:${PORT:-3000}" },
  "dependencies": { "serve": "^14.2.4" }
}
```

4. Glitch が再起動したらプロジェクト URL を開く。

## ローカルで Glitch と同じプレビュー

リポジトリルートで:

```bash
npm install
npm run site:preview
```

ブラウザで `http://127.0.0.1:4173/` を開く（ポートは `package.json` の `site:preview` で変更可）。

Glitch 本番と同じく **`npm start`** で試す場合は、環境変数 `PORT` を付けてください（例: `PORT=4173 npm start`）。
