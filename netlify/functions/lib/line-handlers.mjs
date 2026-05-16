import crypto from "crypto";

function siteBaseUrl() {
  const u = (process.env.SITE_CANONICAL_URL || "").trim().replace(/\/$/, "");
  return u || "https://gmtj-japan-music-tourism.netlify.app";
}

function json(status, body, extraHeaders = {}) {
  return {
    statusCode: status,
    headers: {
      "Content-Type": "application/json; charset=utf-8",
      ...extraHeaders,
    },
    body: JSON.stringify(body),
  };
}

export function verifyLineSignature(rawBody, signature, channelSecret) {
  if (!channelSecret || !signature) return false;
  const h = crypto.createHmac("sha256", channelSecret).update(rawBody, "utf8").digest("base64");
  return h === signature;
}

export function textMessage(text) {
  return { type: "text", text };
}

/**
 * Keyword / intent routing for official LINE (AI TARNAR Voice School + Izu Music Fund).
 */
export function pickReplyMessages(brand, textRaw) {
  const t = (textRaw || "").trim().toLowerCase();

  const blogKeywords = ["ブログ", "blog", "記事", "article", "블로그", "博客"];
  const couponKeywords = ["クーポン", "coupon", "쿠폰", "优惠券", "割引"];
  const bookKeywords = ["予約", "booking", "예약", "预约", "相談", "コンサル"];
  const friendKeywords = ["友だち", "友達", "line", "라인", "加好友"];
  const fundKeywords = ["ファンド", "fund", "投資", "パイプライン"];
  const izuCross = ["伊豆", "izu", "イズ", "ファンド"];
  const tarnarCross = [
    "ターナー",
    "tarnar",
    "aitarnar",
    "ai tarnar",
    "ボイトレ",
    "声の学校",
    "voice school",
  ];
  const menuKeywords = ["メニュー", "menu", "ヘルプ", "help", "메뉴", "菜单"];
  const base = siteBaseUrl();

  if (blogKeywords.some((k) => t.includes(k))) {
    const tarnarBlog = `${base}/tarnar/#blog`;
    const izuBlog = `${base}/izu-fund/#blog`;
    return [
      textMessage(
        brand === "izu_music_fund"
          ? `【ブログ】Izu Music Fund の記事一覧\n${izuBlog}\n声の学びは AI TARNAR Voice School もどうぞ\n${tarnarBlog}`
          : `【ブログ】AI TARNAR Voice School の記事一覧\n${tarnarBlog}\n地域ファンドはこちら\n${izuBlog}`
      ),
    ];
  }

  if (menuKeywords.some((k) => t.includes(k))) {
    return [
      textMessage(
        brand === "izu_music_fund"
          ? `【メニュー】キーワードで案内します：ブログ / ファンド / クーポン / 予約 / 友だち\nポータル: ${base}/izu-fund/`
          : `【メニュー】キーワードで案内します：ブログ / クーポン / 予約 / 友だち\nポータル: ${base}/tarnar/\n伊豆: ${base}/izu-fund/`
      ),
    ];
  }

  if (brand === "tarnar" && izuCross.some((k) => t.includes(k))) {
    return [
      textMessage(
        `【クロス案内】地域と音楽のファンド情報は Izu Music Fund ポータルで公開しています。\n${base}/izu-fund/`
      ),
    ];
  }

  if (brand === "izu_music_fund" && tarnarCross.some((k) => t.includes(k))) {
    return [
      textMessage(
        `【クロス案内】発声・録音・ライブの学びは AI TARNAR Voice School で。\n${base}/tarnar/`
      ),
    ];
  }

  if (couponKeywords.some((k) => t.includes(k))) {
    return [
      textMessage(
        brand === "izu_music_fund"
          ? "【Izu Music Fund】投資家条件を満たす方向けに、別途窓口からクーポンコードをお送りします。まずは「投資家」と送信してください。"
          : "【AI TARNAR Voice School】レッスン関連クーポンはキャンペーン期間中に配信します。コード入力欄に「TARNAR2026」（例）をお試しの場合は案内メールをご確認ください。"
      ),
    ];
  }

  if (bookKeywords.some((k) => t.includes(k))) {
    return [
      textMessage(
        brand === "izu_music_fund"
          ? `【Izu Music Fund】面談・資料請求は 123@atono.jp へ「IMF面談希望」と件名を付けてご連絡ください。\nポータル: ${base}/izu-fund/`
          : `【AI TARNAR Voice School】レッスン・体験のご予約は 123@atono.jp へ「レッスン希望」とお送りください。\nブログ: ${base}/tarnar/#blog\n伊豆ファンド: ${base}/izu-fund/`
      ),
    ];
  }

  if (friendKeywords.some((k) => t.includes(k))) {
    if (brand === "izu_music_fund") {
      return [
        textMessage("友だち追加ありがとうございます。地域と音楽の最新情報をお届けします。"),
        textMessage(
          `【予約・相談】123@atono.jp へ「IMF面談希望」と件名でご連絡ください。\nポータル: ${base}/izu-fund/`
        ),
        textMessage(`【クロス】声の学び・ブログは AI TARNAR Voice School\n${base}/tarnar/#blog`),
      ];
    }
    return [
      textMessage("友だち追加ありがとうございます。レッスン案内やキャンペーンをお届けします。"),
      textMessage(`【予約】123@atono.jp へ「レッスン希望」とお送りください。\nブログ一覧: ${base}/tarnar/#blog`),
      textMessage(`【クロス】地域ファンドは Izu Music Fund\n${base}/izu-fund/`),
    ];
  }

  if (brand === "izu_music_fund" && fundKeywords.some((k) => t.includes(k))) {
    return [
      textMessage(
        "【Izu Music Fund】案件パイプライン・月次レポートは投資家条件確認後にご案内します。関心がある方は「投資家」と送信してください。"
      ),
    ];
  }

  if (t === "こんにちは" || t === "hello" || t === "hi" || t === "안녕" || t === "你好") {
    return [
      textMessage(
        brand === "izu_music_fund"
          ? "Izu Music Fund 公式LINEです。地域と音楽の共創プログラムについてご案内します。「ブログ」「ファンド」「クーポン」「予約」などキーワードで返信します。"
          : "AI TARNAR Voice School 公式LINEです。レッスン案内やキャンペーンをお届けします。「ブログ」「クーポン」「予約」「友だち」などキーワードでもご利用ください。"
      ),
    ];
  }

  return [
    textMessage(
      "ご利用ありがとうございます。次のキーワードで自動案内します：ブログ / クーポン / 予約 / 友だち" +
        (brand === "izu_music_fund" ? " / ファンド" : "")
    ),
  ];
}

async function replyToLine(replyToken, channelAccessToken, messages) {
  const res = await fetch("https://api.line.me/v2/bot/message/reply", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${channelAccessToken}`,
    },
    body: JSON.stringify({ replyToken, messages }),
  });
  if (!res.ok) {
    const errText = await res.text().catch(() => "");
    console.error("LINE reply failed", res.status, errText);
  }
}

export async function pushLineMessage(channelAccessToken, toUserId, messages) {
  if (!channelAccessToken || !toUserId) return false;
  const res = await fetch("https://api.line.me/v2/bot/message/push", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${channelAccessToken}`,
    },
    body: JSON.stringify({ to: toUserId, messages }),
  });
  if (!res.ok) {
    const errText = await res.text().catch(() => "");
    console.error("LINE push failed", res.status, errText);
    return false;
  }
  return true;
}

export async function handleLineWebhook(event, { secret, token, brand }) {
  if (event.httpMethod === "OPTIONS") {
    return { statusCode: 204, headers: { "Access-Control-Allow-Origin": "*" }, body: "" };
  }

  if (event.httpMethod !== "POST") {
    return json(405, { error: "Method not allowed" });
  }

  let rawBody =
    typeof event.body === "string" ? event.body : JSON.stringify(event.body || {});
  if (event.isBase64Encoded && typeof event.body === "string") {
    rawBody = Buffer.from(event.body, "base64").toString("utf8");
  }
  const signature = event.headers["x-line-signature"] || event.headers["X-Line-Signature"];

  if (!secret || !token) {
    console.error("LINE channel not configured for", brand);
    return json(200, {}); // avoid LINE retry storm
  }

  if (!verifyLineSignature(rawBody, signature, secret)) {
    return json(403, { error: "Invalid signature" });
  }

  let body;
  try {
    body = JSON.parse(rawBody);
  } catch {
    return json(400, { error: "Invalid JSON" });
  }

  const events = body.events || [];
  for (const ev of events) {
    if (ev.type === "postback" && ev.replyToken) {
      const data = (ev.postback && ev.postback.data) || "";
      if (data.includes("coupon")) {
        await replyToLine(ev.replyToken, token, pickReplyMessages(brand, "クーポン"));
      } else if (data.includes("book")) {
        await replyToLine(ev.replyToken, token, pickReplyMessages(brand, "予約"));
      }
    } else if (ev.type === "message" && ev.message?.type === "text" && ev.replyToken) {
      const msgs = pickReplyMessages(brand, ev.message.text);
      await replyToLine(ev.replyToken, token, msgs);
    } else if (ev.type === "follow" && ev.replyToken) {
      const base = siteBaseUrl();
      const mail = "123@atono.jp";
      if (brand === "izu_music_fund") {
        await replyToLine(ev.replyToken, token, [
          textMessage(
            "Izu Music Fund 公式LINEの友だち追加ありがとうございます。地域と音楽のプログラム案内をお届けします。"
          ),
          textMessage(
            `【次の一歩】面談・資料はメールへ「IMF面談希望」でご連絡ください: ${mail}\nポータル: ${base}/izu-fund/`
          ),
          textMessage(
            `【クロス】声の学び・ブログは AI TARNAR Voice School\n${base}/tarnar/#blog`
          ),
        ]);
      } else {
        await replyToLine(ev.replyToken, token, [
          textMessage(
            "AI TARNAR Voice School 公式LINEの友だち追加ありがとうございます。レッスン案内・キャンペーンをお届けします。"
          ),
          textMessage(
            `【予約】レッスン・体験はメールへ「レッスン希望」でご連絡ください: ${mail}`
          ),
          textMessage(
            `【ブログ】最新記事一覧\n${base}/tarnar/#blog\n【伊豆】Izu Music Fund\n${base}/izu-fund/`
          ),
        ]);
      }
    }
  }

  return json(200, {});
}
