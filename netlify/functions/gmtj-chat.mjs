/**
 * Netlify Function: Anthropic Messages API — lead-focused concierge (JSON envelope).
 * ANTHROPIC_API_KEY required. Optional ANTHROPIC_MODEL.
 */

const ANTHROPIC_URL = "https://api.anthropic.com/v1/messages";
const ANTHROPIC_VERSION = "2023-06-01";

const SYSTEM = `あなたは Global Music Tourism Japan（GMTJ）のAIコンシェルジュです。
たーなー先生（田中直人）が代表を務める音楽×温泉×神社ツーリズムの専門家として、訪問者の質問に答えてください。

回答のルール:
1. 簡潔に答えた後、必ず「次のステップ」を提案する。
2. 宿泊に関する質問 → #03 123 MUSIC & RESORTS へ誘導。
3. 声楽・レッスン・発声に関する質問 → #08 AI TARNAR Voice School へ誘導。
4. イベント・フェスに関する質問 → #05 Global Music Festival へ誘導。
5. 投資・ファンドに関する質問 → #21 Izu Music Fund へ誘導。
6. 上記に当てはまらない場合は Japan Music Tourism トップの案内を type=info で返す。

出力は次のJSONオブジェクト1つのみ（説明文・Markdown・コードフェンス禁止）:
{"message":"回答テキスト（ユーザーの言語に合わせる）","cta":{"label":"ボタンラベル","url":"完全なパスまたはhttps URL","type":"booking|info|purchase"}}

cta は必ず付与する。url はサイト上の実在パスを優先:
- #03: /03-123-music-resorts/
- #08: /tarnar/
- #05: /05-global-music-festival/
- #21: /izu-fund/
- 一般: / （トップ）

type の目安: 体験・予約導線=booking, 読み物・一覧=info, 課金・購入=purchase（レッスン月額等）。

機微な個人情報の収集を促さない。予約・決済の確定は人間窓口 123@atono.jp へ。`;

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

function extractJsonObject(text) {
  const t = (text || "").trim();
  const start = t.indexOf("{");
  const end = t.lastIndexOf("}");
  if (start === -1 || end <= start) return null;
  const slice = t.slice(start, end + 1);
  try {
    return JSON.parse(slice);
  } catch {
    return null;
  }
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
    (process.env.ANTHROPIC_MODEL || "claude-haiku-4-5-20251001").trim() ||
    "claude-haiku-4-5-20251001";

  const body = JSON.stringify({
    model,
    max_tokens: 1200,
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
    console.error("gmtj-chat anthropic", res.status, raw.slice(0, 800));
    let hint = "Assistant temporarily unavailable.";
    if (res.status === 401) hint = "Invalid API key.";
    else if (res.status === 404 || res.status === 400) hint = "Model or request error. Set ANTHROPIC_MODEL.";
    else if (res.status === 429) hint = "Rate limit or billing. Check Anthropic console.";
    return json(502, { error: hint });
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
  const rawText = parts.join("\n").trim() || "{}";
  const parsed = extractJsonObject(rawText);
  if (parsed && typeof parsed.message === "string") {
    const cta =
      parsed.cta && typeof parsed.cta === "object"
        ? {
            label: String(parsed.cta.label || "").slice(0, 120),
            url: String(parsed.cta.url || "").slice(0, 2000),
            type: ["booking", "info", "purchase"].includes(parsed.cta.type) ? parsed.cta.type : "info",
          }
        : null;
    return json(200, {
      message: parsed.message.trim(),
      cta: cta && cta.label && cta.url ? cta : null,
    });
  }

  return json(200, {
    message: rawText.replace(/^\{[\s\S]*\}$/, "").trim() || rawText,
    cta: null,
  });
};
