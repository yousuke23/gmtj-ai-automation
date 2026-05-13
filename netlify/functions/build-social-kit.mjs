import { buildSocialPack } from "./lib/social-templates.mjs";

const cors = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Headers": "Content-Type, Authorization",
  "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
};

export const handler = async (event) => {
  if (event.httpMethod === "OPTIONS") {
    return { statusCode: 204, headers: cors, body: "" };
  }

  if (event.httpMethod === "GET") {
    return {
      statusCode: 200,
      headers: { "Content-Type": "application/json; charset=utf-8", ...cors },
      body: JSON.stringify({
        ok: true,
        usage: "POST JSON { brand: tarnar|izu_music_fund, article: { title, url, summary?, imageUrl?, slug?, extraHashtags?[] } }",
      }),
    };
  }

  if (event.httpMethod !== "POST") {
    return { statusCode: 405, headers: cors, body: JSON.stringify({ error: "Method not allowed" }) };
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

  const pack = buildSocialPack(brand, article);
  return {
    statusCode: 200,
    headers: { "Content-Type": "application/json; charset=utf-8", ...cors },
    body: JSON.stringify(pack),
  };
};
