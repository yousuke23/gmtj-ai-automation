/**
 * SNS payload builders for TARNAR and Izu Music Fund.
 * Image binary is not generated here — pass imageUrl through to your bridge (Make/Zapier/Meta).
 */

const BRANDS = {
  tarnar: {
    displayName: "AI TARNAR Voice School",
    defaultHashtags: [
      "#AITARNAR",
      "#TARNAR",
      "#ボイトレ",
      "#JapanMusicTourism",
      "#音楽ツーリズム",
      "#声の学校",
    ],
    lineAddCopy: "公式LINEでレッスン案内・クーポンを受け取る",
  },
  izu_music_fund: {
    displayName: "Izu Music Fund",
    defaultHashtags: [
      "#IzuMusicFund",
      "#伊豆",
      "#音楽ファンド",
      "#JapanMusicTourism",
      "#地域共創",
      "#音楽ツーリズム",
    ],
    lineAddCopy: "公式LINEで月次レポートと投資家向け案内（条件あり）",
  },
};

function clip(s, n) {
  const t = (s || "").replace(/\s+/g, " ").trim();
  if (t.length <= n) return t;
  return t.slice(0, n - 1) + "…";
}

function joinHashtags(brandKey, extra = []) {
  const base = BRANDS[brandKey]?.defaultHashtags || [];
  const seen = new Set(base.map((h) => h.toLowerCase()));
  const out = [...base];
  for (const h of extra) {
    const x = h.startsWith("#") ? h : `#${h}`;
    if (!seen.has(x.toLowerCase())) {
      seen.add(x.toLowerCase());
      out.push(x);
    }
  }
  return out.join(" ");
}

/**
 * @param {"tarnar"|"izu_music_fund"} brandKey
 * @param {{ title: string, url: string, summary?: string, imageUrl?: string, slug?: string, extraHashtags?: string[] }} article
 */
export function buildSocialPack(brandKey, article) {
  const brand = BRANDS[brandKey] || BRANDS.tarnar;
  const title = article.title || "New post";
  const url = article.url || "";
  const summary = article.summary || "";
  const imageUrl = article.imageUrl || "";
  const tags = joinHashtags(brandKey, article.extraHashtags || []);

  const tiktok = {
    platform: "tiktok",
    caption: clip(`${title}\n${brand.displayName}\n${summary || "詳細はリンクへ"}\n${url}\n${tags}`, 2200),
    hashtags: tags,
    imageUrl,
    notes: "縦動画9:16推奨。冒頭1秒にフック文言を載せるテンプレ。",
  };

  const instagram = {
    platform: "instagram",
    caption: clip(
      `${title}\n\n${summary}\n\n${brand.lineAddCopy}\n${url}\n\n${tags}`,
      2200
    ),
    hashtags: tags,
    imageUrl,
    notes: "フィード1:1または4:5。ストーリーズは同キャプション短縮版＋リンクスタンプ。",
  };

  const youtube = {
    platform: "youtube",
    title: clip(title, 100),
    description: clip(
      `${summary}\n\n${url}\n\n${tags}\n\n—\n${brand.displayName} / Japan Music Tourism`,
      5000
    ),
    communityPost: clip(`${title}\n${summary}\n${url}`, 500),
    hashtags: tags,
    imageUrl,
    notes: "ショートは縦60秒以内。説明欄にURLとハッシュタグを固定ブロックで配置。",
  };

  const x = {
    platform: "x",
    text: clip(`${title}\n${url}\n${tags}`, 260),
    thread: [
      clip(`${title}\n${url}`, 260),
      clip(summary, 260),
      clip(tags, 260),
    ].filter(Boolean),
    hashtags: tags,
    imageUrl,
    notes: "画像4枚まで。長文はスレッド2〜3投稿に分割。",
  };

  const facebook = {
    platform: "facebook",
    message: clip(`${title}\n\n${summary}\n\n${url}\n\n${tags}`, 5000),
    hashtags: tags,
    imageUrl,
    notes: "リンクプレビューが効くようURLは本文冒頭付近に。",
  };

  return {
    brand: brandKey,
    article: { title, url, summary, imageUrl, slug: article.slug || "" },
    generatedAt: new Date().toISOString(),
    platforms: { tiktok, instagram, youtube, x, facebook },
  };
}

export { BRANDS };
