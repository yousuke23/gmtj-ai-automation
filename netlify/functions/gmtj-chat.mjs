/**
 * Netlify Function: Anthropic Messages API for public site chat.
 * Set ANTHROPIC_API_KEY in Netlify Site settings → Environment variables.
 * Optional: ANTHROPIC_MODEL (default claude-3-5-haiku-20241022)
 */

const ANTHROPIC_URL = "https://api.anthropic.com/v1/messages";
const ANTHROPIC_VERSION = "2023-06-01";

const SYSTEM = `You are the concierge assistant for Japan Music Tourism (GMTJ), a music-and-travel experience brand.
Answer helpfully about music tourism, regional travel in Japan, etiquette, planning tips, and related topics.
Do not ask users for sensitive personal data. Do not give definitive legal, medical, or investment advice; suggest consulting professionals when needed.
For specific bookings, payments, or cancellations, direct users to email 123@atono.jp unless they already have another official channel.
Keep answers concise unless the user asks for detail.`;

const cors = {
  "Content-Type": "application/json; charset=utf-8",
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Headers": "Content-Type",
  "Access-Control-Allow-Methods": "POST, OPTIONS",
};

function json(statusCode, bodyObj) {
  return {
    statusCode,
    headers: cors,
    body: JSON.stringify(bodyObj),
  };
}

export const handler = async (event) => {
  if (event.httpMethod === "OPTIONS") {
    return { statusCode: 204, headers: cors, body: "" };
  }
  if (event.httpMethod !== "POST") {
    return json(405, { error: "Method not allowed" });
  }

  const key = (process.env.ANTHROPIC_API_KEY || "").trim();
  if (!key) {
    return json(503, { error: "Assistant is not configured." });
  }

  let payload;
  try {
    payload = JSON.parse(event.body || "{}");
  } catch {
    return json(400, { error: "Invalid request body." });
  }

  const messagesIn = payload.messages;
  if (!Array.isArray(messagesIn) || messagesIn.length === 0) {
    return json(400, { error: "Missing messages." });
  }

  const messages = [];
  for (const m of messagesIn.slice(-12)) {
    if (!m || typeof m !== "object") continue;
    const role = m.role;
    const content = typeof m.content === "string" ? m.content.trim() : "";
    if (!content || (role !== "user" && role !== "assistant")) continue;
    messages.push({ role, content: content.slice(0, 12000) });
  }
  if (messages.length === 0) {
    return json(400, { error: "No valid messages." });
  }

  const model =
    (process.env.ANTHROPIC_MODEL || "claude-3-5-haiku-20241022").trim() ||
    "claude-3-5-haiku-20241022";

  const body = JSON.stringify({
    model,
    max_tokens: 1024,
    system: SYSTEM,
    messages,
  });

  let res;
  try {
    res = await fetch(ANTHROPIC_URL, {
      method: "POST",
      headers: {
        "content-type": "application/json; charset=utf-8",
        "x-api-key": key,
        "anthropic-version": ANTHROPIC_VERSION,
      },
      body,
    });
  } catch {
    return json(502, { error: "Could not reach assistant service." });
  }

  const raw = await res.text();
  if (!res.ok) {
    return json(502, { error: "Assistant temporarily unavailable." });
  }

  let data;
  try {
    data = JSON.parse(raw);
  } catch {
    return json(502, { error: "Assistant temporarily unavailable." });
  }

  const blocks = data.content || [];
  const parts = [];
  for (const b of blocks) {
    if (b && b.type === "text" && typeof b.text === "string") {
      parts.push(b.text);
    }
  }
  const reply = parts.join("\n").trim() || " ";
  return json(200, { reply });
};
