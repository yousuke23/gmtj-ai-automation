(function () {
  const apiBase = ""; // same origin
  const el = (id) => document.getElementById(id);

  const CANONICAL = "https://gmtj-japan-music-tourism.netlify.app";
  const SAMPLE_TARNAR = {
    title: "初深海熱水噴出孔採音の16分音符だけの舌位置トラッキング",
    url: CANONICAL + "/tarnar/blog/ja/voice-guide-1501.html",
    summary:
      "AI TARNAR Voice School の実践メモ（batch18）。深海噴出孔×舌位置トラッキング。ブログ公開→SNSパッケージ→bridge/LINE の本番テスト用サンプルです。",
  };

  const SAMPLE_IZU = {
    title: "伊豆の音楽と旅をつなぐ考え方",
    url: CANONICAL + "/izu-fund/blog/ja/izu-01.html",
    summary:
      "Izu Music Fund の記事サンプル。地域の音楽資源と観光導線を一つのストーリーにまとめる視点。izu_music_fund ブランドでパイプライン・LINE通知をテストする際に使用します。",
  };

  function hidePipelineDebug() {
    const dbg = el("pipeline-debug");
    if (dbg) {
      dbg.hidden = true;
      dbg.style.display = "none";
      dbg.textContent = "";
    }
  }

  function fillIzuSample() {
    el("brand").value = "izu_music_fund";
    el("title").value = SAMPLE_IZU.title;
    el("url").value = SAMPLE_IZU.url;
    el("summary").value = SAMPLE_IZU.summary;
    el("image").value = "";
    el("status").textContent =
      "Izu Music Fund サンプルを投入しました。OPSシークレットを入力し、プレビューまたは公開パイプラインを実行してください。";
    hidePipelineDebug();
  }

  function fillTarnarSample() {
    el("brand").value = "tarnar";
    el("title").value = SAMPLE_TARNAR.title;
    el("url").value = SAMPLE_TARNAR.url;
    el("summary").value = SAMPLE_TARNAR.summary;
    el("image").value = "";
    el("status").textContent =
      "TARNAR（voice-guide-1501）サンプルを投入しました。OPSシークレットを入力し、プレビューまたは公開パイプラインを実行してください。";
    hidePipelineDebug();
  }

  function clearForm() {
    el("title").value = "";
    el("url").value = "";
    el("summary").value = "";
    el("image").value = "";
    el("status").textContent = "";
    hidePipelineDebug();
    const out = el("preview");
    if (out) out.innerHTML = "";
  }

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
    let dbg = el("pipeline-debug");
    if (!dbg) {
      dbg = document.createElement("pre");
      dbg.id = "pipeline-debug";
      dbg.className = "auto-pre";
      dbg.setAttribute("aria-label", "パイプライン結果メタ");
      el("status").insertAdjacentElement("afterend", dbg);
    }
    dbg.hidden = false;
    dbg.style.display = "block";
    dbg.textContent = JSON.stringify(
      {
        snsPlatformOrder: data.snsPlatformOrder,
        bridge: data.bridge,
        lineNotify: data.lineNotify,
      },
      null,
      2
    );
  }

  el("btn-preview").addEventListener("click", preview);
  el("btn-publish").addEventListener("click", publishPipeline);
  const fillSample = el("btn-fill-tarnar-sample");
  if (fillSample) fillSample.addEventListener("click", fillTarnarSample);
  const fillIzuBtn = el("btn-fill-izu-sample");
  if (fillIzuBtn) fillIzuBtn.addEventListener("click", fillIzuSample);
  const clearBtn = el("btn-clear-form");
  if (clearBtn) clearBtn.addEventListener("click", clearForm);
})();
