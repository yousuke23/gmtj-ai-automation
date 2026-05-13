(function () {
  const apiBase = ""; // same origin
  const el = (id) => document.getElementById(id);

  function getSecret() {
    return (el("ops-secret").value || "").trim();
  }

  function renderPack(pack) {
    const out = el("preview");
    out.innerHTML = "";
    const plats = pack.platforms || {};
    const order = ["tiktok", "instagram", "youtube", "x", "facebook"];
    for (const key of order) {
      const p = plats[key];
      if (!p) continue;
      const card = document.createElement("article");
      card.className = "auto-card";
      const title = document.createElement("h3");
      title.textContent = p.platform.toUpperCase();
      card.appendChild(title);
      const pre = document.createElement("pre");
      pre.className = "auto-pre";
      const text =
        key === "youtube"
          ? JSON.stringify(
              { title: p.title, description: p.description, communityPost: p.communityPost, notes: p.notes },
              null,
              2
            )
          : JSON.stringify(p, null, 2);
      pre.textContent = text;
      card.appendChild(pre);
      const row = document.createElement("div");
      row.className = "auto-row";
      const copy = document.createElement("button");
      copy.type = "button";
      copy.className = "btn btn-ghost";
      copy.textContent = "キャプションをコピー";
      copy.addEventListener("click", async () => {
        const cap =
          p.caption || p.text || p.message || p.description || "";
        await navigator.clipboard.writeText(cap);
        copy.textContent = "コピー済み";
        setTimeout(() => (copy.textContent = "キャプションをコピー"), 1500);
      });
      row.appendChild(copy);
      card.appendChild(row);
      out.appendChild(card);
    }
  }

  async function preview() {
    const brand = el("brand").value;
    const article = {
      title: el("title").value.trim(),
      url: el("url").value.trim(),
      summary: el("summary").value.trim(),
      imageUrl: el("image").value.trim(),
    };
    if (!article.title || !article.url) {
      el("status").textContent = "タイトルとURLは必須です。";
      return;
    }
    el("status").textContent = "生成中…";
    const res = await fetch(apiBase + "/.netlify/functions/build-social-kit", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ brand, article }),
    });
    const data = await res.json().catch(() => ({}));
    if (!res.ok) {
      el("status").textContent = data.error || "エラー";
      return;
    }
    el("status").textContent = "OK";
    renderPack(data);
    window.__lastPack = data;
  }

  async function publishPipeline() {
    const secret = getSecret();
    if (!secret) {
      el("status").textContent = "OPSシークレットを入力してください。";
      return;
    }
    const brand = el("brand").value;
    const article = {
      title: el("title").value.trim(),
      url: el("url").value.trim(),
      summary: el("summary").value.trim(),
      imageUrl: el("image").value.trim(),
    };
    if (!article.title || !article.url) {
      el("status").textContent = "タイトルとURLは必須です。";
      return;
    }
    el("status").textContent = "パイプライン送信中…";
    const res = await fetch(apiBase + "/.netlify/functions/blog-publish-hook", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: "Bearer " + secret,
      },
      body: JSON.stringify({ brand, article }),
    });
    const data = await res.json().catch(() => ({}));
    if (!res.ok) {
      el("status").textContent = data.error || "送信失敗";
      return;
    }
    el("status").textContent = "パイプライン完了（bridge / LINE は環境変数に依存）";
    if (data.socialPack) renderPack(data.socialPack);
  }

  el("btn-preview").addEventListener("click", preview);
  el("btn-publish").addEventListener("click", publishPipeline);
})();
