/**
 * Netlify Forms: submission-created → Resend auto-reply + ops notify.
 * Env: RESEND_API_KEY, RESEND_FROM (verified domain or onboarding@resend.dev)
 */
export const handler = async (event) => {
  let body = {};
  if (event && typeof event.body === "string" && event.body) {
    try {
      body = JSON.parse(event.body);
    } catch {
      console.error("submission-created: invalid JSON body");
      return { statusCode: 400, body: "Invalid JSON" };
    }
  } else if (event && event.payload) {
    body = { payload: event.payload };
  }

  const payload = body.payload || body;
  const data = payload.data || payload.human_fields || payload.fields || {};

  if (Array.isArray(payload.ordered_human_fields)) {
    for (const row of payload.ordered_human_fields) {
      if (row && row.name && row.value != null && data[row.name] == null) {
        data[row.name] = row.value;
      }
    }
  }

  const email = String(
    data.email || data.Email || data["メール"] || data["メールアドレス"] || "",
  ).trim();
  const name = String(data.name || data.Name || data["お名前"] || data["名前"] || "").trim();
  const formName = String(
    payload.form_name || body.form_name || data["form-name"] || data.form_name || "contact",
  ).trim();

  console.log("submission-created", { formName, email: email ? "(set)" : "(missing)" });

  if (!email) {
    return { statusCode: 200, body: "OK (no email)" };
  }

  const key = (process.env.RESEND_API_KEY || "").trim();
  if (!key) {
    console.warn("submission-created: RESEND_API_KEY missing");
    return { statusCode: 200, body: "OK (no resend)" };
  }

  const from = (process.env.RESEND_FROM || "onboarding@resend.dev").trim();

  const templates = {
    contact: {
      subject: "【GMTJ】お問い合わせを受け付けました",
      text: `${name || "お客様"}様\n\nお問い合わせいただきありがとうございます。\n担当者より48時間以内にご連絡いたします。\n\nGlobal Music Tourism Japan\n123@atono.jp`,
    },
    "chat-lead": {
      subject: "【GMTJ】資料請求・個別案内の受付",
      text: `${name || "お客様"}様\n\nお問い合わせありがとうございます。\n担当よりご連絡いたします。\n\nGlobal Music Tourism Japan`,
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
    const { Resend } = await import("resend");
    const resend = new Resend(key);
    const toUser = await resend.emails.send({
      from,
      to: email,
      subject: template.subject,
      text: template.text,
    });
    if (toUser.error) {
      console.error("submission-created user mail error", toUser.error);
      return { statusCode: 500, body: "Resend user error" };
    }
    const toOps = await resend.emails.send({
      from,
      to: "123@atono.jp",
      subject: `[${formName}] 新規フォーム送信: ${email}`,
      text: JSON.stringify({ formName, email, name, data }, null, 2),
    });
    if (toOps.error) {
      console.error("submission-created ops mail error", toOps.error);
    }
  } catch (e) {
    console.error("submission-created resend error", e);
    return { statusCode: 500, body: "Resend error" };
  }

  return { statusCode: 200, body: "OK" };
};
