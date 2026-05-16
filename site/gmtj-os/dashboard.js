(function () {
  "use strict";

  var DATA_URL = "data/operations-dashboard.json";

  function esc(s) {
    return String(s)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");
  }

  function pillClass(status) {
    if (status === "running") return "pill pill--running";
    if (status === "warning") return "pill pill--warning";
    return "pill pill--ok";
  }

  function pillLabel(status) {
    if (status === "running") return "実行中";
    if (status === "warning") return "要確認";
    return "順調";
  }

  function bizById(list, id) {
    for (var i = 0; i < (list || []).length; i++) {
      if (list[i].id === id) return list[i];
    }
    return null;
  }

  function renderBar(bar) {
    var ok = bar.success || 0;
    var w = bar.warning || 0;
    var r = bar.running || 0;
    var track = document.getElementById("status-track");
    if (!track) return;
    var sum = ok + w + r;
    if (sum === 0) {
      track.innerHTML =
        '<div class="status-seg status-seg--empty" style="width:100%" title="記録なし"></div>';
    } else {
      var total = sum;
      track.innerHTML =
        '<div class="status-seg status-seg--ok" style="width:' +
        (100 * ok) / total +
        '%"></div>' +
        '<div class="status-seg status-seg--warn" style="width:' +
        (100 * w) / total +
        '%"></div>' +
        '<div class="status-seg status-seg--run" style="width:' +
        (100 * r) / total +
        '%"></div>';
    }
    var leg = document.getElementById("status-legend");
    if (leg) {
      leg.innerHTML =
        '<span><strong>' +
        ok +
        "</strong> 成功</span>" +
        '<span><strong>' +
        w +
        "</strong> 要確認</span>" +
        '<span><strong>' +
        r +
        "</strong> 実行中</span>";
    }
  }

  function renderHeadline(text) {
    var el = document.getElementById("today-headline");
    if (!el) return;
    if (text) {
      el.textContent = text;
      el.hidden = false;
    } else {
      el.textContent = "";
      el.hidden = true;
    }
  }

  function renderActions(items) {
    var ul = document.getElementById("today-actions");
    if (!ul) return;
    var list = items && items.length ? items : [];
    if (!list.length) {
      ul.innerHTML =
        '<li class="today-actions__empty">今日の優先タスクは未入力です。</li>';
      return;
    }
    ul.innerHTML = list
      .map(function (line) {
        return "<li>" + esc(line) + "</li>";
      })
      .join("");
  }

  function renderSalesRanking(rows) {
    var host = document.getElementById("sales-ranking");
    if (!host) return;
    if (!rows || !rows.length) {
      host.innerHTML =
        '<p class="sales-ranking__empty">売上データはこのダッシュボードに未登録です。</p>';
      return;
    }
    host.innerHTML =
      "<ol>" +
      rows
        .map(function (row) {
          return (
            "<li><span>" +
            esc(row.label || "") +
            "</span><span>" +
            esc(String(row.amount ?? "")) +
            "</span></li>"
          );
        })
        .join("") +
      "</ol>";
  }

  function renderBusinesses(list) {
    var grid = document.getElementById("biz-grid");
    if (!grid) return;
    grid.innerHTML = (list || [])
      .map(function (b) {
        var focus = b.id === "08" || b.id === "21" ? " biz-card--focus" : "";
        return (
          '<article class="biz-card' +
          focus +
          '">' +
          '<span class="' +
          pillClass(b.todayStatus) +
          '">' +
          esc(pillLabel(b.todayStatus)) +
          "</span>" +
          '<div class="biz-card__id">#' +
          esc(b.id) +
          "</div>" +
          '<div class="biz-card__name">' +
          esc(b.name) +
          "</div>" +
          '<div class="biz-card__kpi">' +
          esc(b.kpiLine || "") +
          "</div></article>"
        );
      })
      .join("");
  }

  function renderFocusHero(articleId, business, wf) {
    var root = document.getElementById(articleId);
    if (!root || !business || !wf || !wf.steps) return;
    var n = wf.steps.length;
    var steps = wf.steps
      .map(function (s) {
        return (
          "<li><span>" +
          esc(s.name) +
          '</span><span class="focus-card__state">' +
          esc(s.state) +
          "</span></li>"
        );
      })
      .join("");
    var portalHref =
      articleId === "tarnar" ? "../tarnar/" : "../izu-fund/";
    var portalLabel =
      articleId === "tarnar"
        ? "AI TARNAR Voice School を開く"
        : "Izu Music Fund を開く";
    root.innerHTML =
      '<span class="' +
      pillClass(business.todayStatus) +
      ' focus-card__pill">' +
      esc(pillLabel(business.todayStatus)) +
      "</span>" +
      '<h3 class="focus-card__title">' +
      esc(wf.title || business.name) +
      "</h3>" +
      '<p class="focus-card__kpi">' +
      esc(business.kpiLine || "") +
      "</p>" +
      '<p class="focus-card__metric">登録フロー <b>' +
      n +
      "</b> 件</p>" +
      '<ol class="focus-card__steps">' +
      steps +
      "</ol>" +
      '<p class="focus-card__cta"><a class="focus-card__link" href="' +
      esc(portalHref) +
      '">' +
      esc(portalLabel) +
      "</a></p>";
  }

  function load() {
    fetch(DATA_URL + "?t=" + Date.now(), { cache: "no-store" })
      .then(function (r) {
        if (!r.ok) throw new Error();
        return r.json();
      })
      .then(function (data) {
        renderBar(data.todayBar || {});
        renderHeadline(data.todayHeadline || "");
        renderActions(data.todayActions);
        renderSalesRanking(data.salesRanking);
        var biz = data.businesses || [];
        renderFocusHero("tarnar", bizById(biz, "08"), data.tarnar08);
        renderFocusHero("izu", bizById(biz, "21"), data.izu21);
        renderBusinesses(biz);
      })
      .catch(function () {
        renderHeadline("");
        renderActions(["ページを再読み込みしてください。"]);
        renderSalesRanking([]);
      });
  }

  load();
})();
