/**
 * 1日複数回: 公開キューを読み、予定時刻を過ぎた項目を AUTOMATION_BRIDGE_URL へ送る
 * キューは静的 JSON（デプロイで更新）。送信済みフラグは外部（Make等）で管理する想定。
 */
import { buildSocialPack, BRANDS } from "./lib/social-templates.mjs";
export const config = {
  schedule: "5 2,8,14,20 * * *",
};

function siteBaseUrl() {
  return (
    (process.env.SITE_CANONICAL_URL || "").replace(/\/$/, "") ||
    (process.env.URL || "").replace(/\/$/, "") ||
    (process.env.DEPLOY_PRIME_URL || "").replace(/\/$/, "") ||
    "https://gmtj-japan-music-tourism.netlify.app"
  );
}

export const handler = async () => {
  const base = siteBaseUrl();
  const queueUrl = `${base}/automation/queue.json`;
  const bridge = (process.env.AUTOMATION_BRIDGE_URL || "").trim();

  let queue = { items: [] };
  try {
    const res = await fetch(queueUrl, { headers: { Accept: "application/json" } });
    if (res.ok) {
      queue = await res.json();
    }
  } catch (e) {
    console.error("queue fetch failed", e);
  }

  const items = Array.isArray(queue.items) ? queue.items : [];
  const now = Date.now();
  const due = items.filter((it) => {
    if (!it || it.status === "sent") return false;
    const t = Date.parse(it.scheduledAt || "");
    return Number.isFinite(t) && t <= now;
  });

  const results = [];
  if (bridge && due.length) {
    for (const item of due) {
      const brand = item.brand === "izu_music_fund" ? "izu_music_fund" : "tarnar";
      const article = item.article || {};
      const socialPack =
        article.title && article.url ? buildSocialPack(brand, article) : null;
      const brandLabel = (BRANDS[brand] && BRANDS[brand].displayName) || (brand === "izu_music_fund" ? "Izu Music Fund" : "AI TARNAR Voice School");
      const res = await fetch(bridge, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          event: "scheduled_social",
          brand,
          article,
          socialPack,
          lineBroadcast: article.title
            ? { text: `【${brandLabel} · 予定投稿】${article.title}` }
            : null,
          queueId: item.id || null,
          scheduledAt: item.scheduledAt || null,
          source: "gmtj-netlify-cron",
        }),
      });
      results.push({ id: item.id, status: res.status, ok: res.ok });
    }
  } else {
    console.log("social-daily-tick: no bridge or nothing due", { due: due.length, bridge: !!bridge });
  }

  return {
    statusCode: 200,
    headers: { "Content-Type": "application/json; charset=utf-8" },
    body: JSON.stringify({
      ok: true,
      checkedAt: new Date().toISOString(),
      queueUrl,
      dueCount: due.length,
      bridgeConfigured: !!bridge,
      results,
    }),
  };
};
