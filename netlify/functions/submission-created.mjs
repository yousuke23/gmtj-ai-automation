/**
 * Netlify Forms: submission-created → Resend auto-reply + ops notify.
 * Env: RESEND_API_KEY, optional RESEND_FROM (default onboarding@resend.dev for tests)
 */
export const handler = async (event) => {
  if (event.httpMethod !== "POST") {
    return { statusCode: 405, body: "Method Not Allowed" };
  }

  let body;
  try {
    body = JSON.parse(event.body || "{}");
  } catch {
    return { statusCode: 400, body: "Invalid JSON" };
  }

  const payload = body.payload || body;
  const data = payload.data || payload.human_fields || payload.fields || {};
  const email = String(data.email || data.Email || data["メール"] || "").trim();
  const name = String(data.name || data.Name || data["お名前"] || "").trim();
  const formName = String(
    payload.form_name || body.form_name || data["form-name"] || data.form_name || "contact",
  ).trim();

  if (!email) {
    return { statusCode: 200, body: "OK (no email)" };
  }

  const key = (process.env.RESEND_API_KEY || "").trim();
  if (!key) {
    console.warn("submission-created: RESEND_API_KEY missing");
    return { statusCode: 200, body: "OK (no resend)" };
  }

  const from = (process.env.RESEND_FROM || "GMTJ <onboarding@resend.dev>").trim();

  const templates = {
    contact: {
      subject: "【GMTJ】お問い合わせを受け付けました",
      text: `${name || "お客様"}様\n\nお問い合わせいただきありがとうございます。\n担当者より48時間以内にご連絡いたします。\n\nGlobal Music Tourism Japan\n123@atono.jp`,
    },
    "chat-lead": {
      subject: "【GMTJ】資料請求・個別案内の受付",
      text: `${name || "お客様"}様\n\nお問い合わせありがとうございます。\n担当よりご連絡いたします。\n\nGlobal Music Tourism Japan`,
    },
    "trial-lesson": {
      subject: "【AI TARNAR】体験レッスンのお申し込みを受け付けました",
      text: `${name || "お客様"}様\n\n体験レッスンのお申し込みありがとうございます。\nCalendlyで選択いただいた日時にZoomリンクをお送りします。\n\nたーなー先生 / AI TARNAR Voice School`,
    },
    "festival-artist": {
      subject: "【IZUSAN MUSIC FEST 2026】出演申請を受け付けました",
      text: `ご応募ありがとうございます。\n審査結果は2026年7月末までにメールでご連絡します。\n\nATAMI IZUSAN International Music Festival 事務局`,
    },
    "festival-mail": {
      subject: "【IZUSAN MUSIC FEST 2026】メーリングリスト登録",
      text: `登録ありがとうございます。最新情報をお届けします。\n\nATAMI IZUSAN International Music Festival`,
    },
    "stay-direct": {
      subject: "【123 MUSIC & RESORTS】直接予約の受付",
      text: `${name || "お客様"}様\n\n直接予約のお申し込みを受け付けました。48時間以内にご確認メールをお送りします。\n\n123 MUSIC & RESORTS / GMTJ`,
    },
  };

  const template = templates[formName] || templates.contact;

  try {
    const { Resend } = await import("@resend/node");
    const resend = new Resend(key);
    await resend.emails.send({
      from,
      to: email,
      subject: template.subject,
      text: template.text,
    });
    await resend.emails.send({
      from,
      to: "123@atono.jp",
      subject: `[${formName}] 新規フォーム送信: ${email}`,
      text: JSON.stringify({ formName, email, name, data }, null, 2),
    });
  } catch (e) {
    console.error("submission-created resend error", e);
    return { statusCode: 500, body: "Resend error" };
  }

  return { statusCode: 200, body: "OK" };
};
