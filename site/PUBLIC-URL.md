# 公開用 URL（`site/` をインターネットに出す）

Grok などに URL を貼るには、**HTTPS で誰でも開ける場所**に `site/` の静的ファイルを置きます。  
**API キーや `config.js` の秘密はリポジトリにコミットしない**こと（公開リポの場合は特に）。

## チャット試用について

- 公開 URL 上のページは **`config.js` の `chatProxyUrl`** が指す先にのみ POST します。
- **デフォルトは `http://127.0.0.1:8766`** のため、**インターネット上の訪問者のブラウザからはローカルには届きません**。結果として **公開サイトではチャットは動かない**のが普通です（意図どおりで安全）。
- チャットまで公開したい場合は **別途バックエンド**（認証・レート制限・課金）が必要です。本リポの `chat-proxy.py` は **ローカル試用**向けです。

---

## 1. Netlify（手早い）

1. [Netlify](https://www.netlify.com/) にサインアップ。
2. **Add new site** → **Import an existing project** → GitHub のこのリポジトリを選択。
3. ビルド設定:
   - **Base directory**: 空（リポジトリルート）
   - **Build command**: 空
   - **Publish directory**: `site`
4. デプロイ後、**`https://ランダム名.netlify.app`** のような URL が付きます。これを Grok に貼れます。

リポジトリルートの **`netlify.toml`** があれば、上記の Publish は自動です。

### Netlify のサイト名を変える（例: `gmtj-japan-music-tourism`）

1. Netlify ダッシュボード → 対象サイト → **Site configuration** → **General** → **Site details**。
2. **Change site name** で **`gmtj-japan-music-tourism`** など未使用の名前に変更（URL は `https://gmtj-japan-music-tourism.netlify.app/` 形式）。
3. 旧 URL からのリダイレクトが必要なら **Domain management** でドメイン／リダイレクトを設定。

---

## 2. Vercel

1. [Vercel](https://vercel.com/) にサインアップ → **Add New Project** → このリポジトリを import。
2. **重要:** プロジェクト設定の **Root Directory** を **`site`** にする（リポジトリルートのままだと静的ファイルがトップに来ず失敗しやすいです）。
3. **Framework Preset**: Other（または自動検出で「静的」に近いもの）。**Build Command** は空でよいことが多いです。
4. デプロイ後の **`https://プロジェクト名.vercel.app`** を共有。

ルートに **`vercel.json` は置いていません**（Root = `site` の方が確実なため）。

---

## 3. GitHub Pages（Actions）

1. GitHub リポジトリ → **Settings** → **Pages**。
2. **Source**: **GitHub Actions** を選ぶ。
3. リポジトリに **`.github/workflows/deploy-site-pages.yml`** がある場合、`main` への push で `site/` が Pages に上がります。
4. URL は **`https://＜ユーザー名＞.github.io/＜リポジトリ名＞/`** 形式（ユーザー／組織の Pages 設定による）。

初回は Actions の **Permissions** で Pages 書き込みが通るまで数分かかることがあります。

---

## 4. Cloudflare Pages

1. [Cloudflare Dashboard](https://dash.cloudflare.com/) → **Workers & Pages** → **Create** → **Pages** → Connect to Git。
2. **Build command**: 空（または `exit 0`）
3. **Build output directory**: `site`
4. 付与された **`https://xxx.pages.dev`** を利用。

---

## 公開後のチェックリスト

- [ ] `site/config.js` に **本番用の秘密を書いていない**
- [ ] 利用規約・プライバシー（本サイトフッターにもあるとおり、**別ページで整備**が前提）
- [ ] 誤った公式表記や、未確認の数値・営業情報を載せていない（`kb/policy.md` の精神に沿う）
