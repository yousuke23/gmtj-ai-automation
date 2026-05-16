/**
 * ブログ公開 → SNS用ペイロード生成 → 外部オーケストレーション（Make/Zapier等）→ 任意でLINE通知
 * Authorization: Bearer OPS_PUBLISH_SECRET
 */
import { buildSocialPack, BRANDS } from "./lib/social-templates.mjs";
import { pushLineMessage, textMessage as lineText } from "./lib/line-handlers.mjs";

const cors = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Headers": "Content-Type, Authorization",
  "Access-Control-Allow-Methods": "POST, OPTIONS",
};

async function postJson(url, payload) {
  const res = await fetch(url, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload),
  });
  const text = await res.text();
  let data;
  try {
    data = JSON.parse(text);
  } catch {
    data = { raw: text };
  }
  return { ok: res.ok, status: res.status, data };
}

export const handler = async (event) => {
  if (event.httpMethod === "OPTIONS") {
    return { statusCode: 204, headers: cors, body: "" };
  }
  if (event.httpMethod !== "POST") {
    return { statusCode: 405, headers: cors, body: JSON.stringify({ error: "Method not allowed" }) };
  }

  const secret = (process.env.OPS_PUBLISH_SECRET || "").trim();
  const auth = event.headers.authorization || event.headers.Authorization || "";
  const token = auth.startsWith("Bearer ") ? auth.slice(7).trim() : "";
  if (!secret || token !== secret) {
    return { statusCode: 401, headers: cors, body: JSON.stringify({ error: "Unauthorized" }) };
  }

  let body;
  try {
    body = JSON.parse(event.body || "{}");
  } catch {
    return { statusCode: 400, headers: cors, body: JSON.stringify({ error: "Invalid JSON" }) };
  }

  const brand = body.brand === "izu_music_fund" ? "izu_music_fund" : "tarnar";
  const article = body.article || {};
  if (!article.title || !article.url) {
    return {
      statusCode: 400,
      headers: cors,
      body: JSON.stringify({ error: "article.title and article.url are required" }),
    };
  }

  const socialPack = buildSocialPack(brand, article);
  const brandLabel = (BRANDS[brand] && BRANDS[brand].displayName) || (brand === "izu_music_fund" ? "Izu Music Fund" : "AI TARNAR Voice School");

  const bridgeUrl = (process.env.AUTOMATION_BRIDGE_URL || "").trim();
  let bridgeResult = null;
  if (bridgeUrl) {
    bridgeResult = await postJson(bridgeUrl, {
      event: "blog_published",
      brand,
      article,
      socialPack,
      lineBroadcast: { text: `【${brandLabel}】${article.title}\n${article.url}` },
      source: "gmtj-netlify",
    });
  }

  let lineNotify = null;
  const lineToken =
    brand === "izu_music_fund"
      ? (process.env.LINE_IMF_CHANNEL_TOKEN || "").trim()
      : (process.env.LINE_TARNAR_CHANNEL_TOKEN || "").trim();
  const lineUser =
    brand === "izu_music_fund"
      ? (process.env.LINE_IMF_NOTIFY_USER_ID || "").trim()
      : (process.env.LINE_TARNAR_NOTIFY_USER_ID || "").trim();

  if (lineToken && lineUser) {
    const ok = await pushLineMessage(lineToken, lineUser, [
      lineText(`【${brandLabel}】新着記事\n${article.title}\n${article.url}`),
    ]);
    lineNotify = { sent: ok };
  }

  const snsPlatformOrder = ["tiktok", "instagram", "youtube", "x", "facebook"];

  return {
    statusCode: 200,
    headers: { "Content-Type": "application/json; charset=utf-8", ...cors },
    body: JSON.stringify({
      ok: true,
      socialPack,
      snsPlatformOrder,
      bridge: bridgeResult,
      lineNotify,
    }),
  };
};
