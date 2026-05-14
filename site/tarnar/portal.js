(function () {
  "use strict";

  function esc(s) {
    return String(s)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");
  }

  function loadConfig() {
    return fetch("portal-config.json?t=" + Date.now(), { cache: "no-store" })
      .then(function (r) {
        return r.ok ? r.json() : {};
      })
      .catch(function () {
        return {};
      });
  }

  function loadBlog() {
    return fetch("data/blog-manifest.json?t=" + Date.now(), { cache: "no-store" })
      .then(function (r) {
        return r.ok ? r.json() : { articles: [] };
      })
      .catch(function () {
        return { articles: [] };
      });
  }

  function applyConfig(cfg) {
    var lineBtn = document.getElementById("line-cta");
    var mail = (cfg && cfg.contactEmail) || "123@atono.jp";
    if (lineBtn) {
      var url = (cfg && cfg.lineAddFriendUrl) || "";
      if (url) {
        lineBtn.href = url;
        lineBtn.rel = "noopener noreferrer";
        lineBtn.target = "_blank";
      } else {
        lineBtn.href = "mailto:" + mail + "?subject=LINE%E7%99%BB%E9%8C%B2%E3%81%AE%E3%81%8A%E5%95%8F%E3%81%84%E5%90%88%E3%82%8F%E3%81%9B";
      }
    }
    var foot = document.getElementById("footer-related");
    if (foot && cfg && cfg.relatedSites && cfg.relatedSites.length) {
      foot.innerHTML = cfg.relatedSites
        .map(function (s, i) {
          return (
            (i ? " · " : "") +
            '<a href="' +
            esc(s.url) +
            '" rel="noopener noreferrer" target="_blank">' +
            esc(s.label) +
            "</a>"
          );
        })
        .join("");
    }
  }

  function renderBlog(data) {
    var ul = document.getElementById("blog-list");
    if (!ul) return;
    var items = (data && data.articles) || [];
    if (!items.length) {
      ul.innerHTML =
        '<li class="blog-meta">記事一覧は準備中です。</li>';
      return;
    }
    ul.innerHTML = items
      .map(function (a) {
        var t = a.titles || {};
        var u = a.urls || {};
        function chip(lang, label) {
          var href = u[lang] || "";
          if (!href) {
            return '<span class="lang-chip">' + label + "</span>";
          }
          return (
            '<a class="lang-chip" href="' +
            esc(href) +
            '">' +
            label +
            "</a>"
          );
        }
        var title = t.ja || t.en || a.slug || "（無題）";
        var mainHref = u.ja || u.en || u.ko || u.zh || "#";
        return (
          '<li><a href="' +
          esc(mainHref) +
          '">' +
          esc(title) +
          '</a><div class="blog-meta">' +
          chip("ja", "JA") +
          " " +
          chip("en", "EN") +
          " " +
          chip("ko", "KO") +
          " " +
          chip("zh", "ZH") +
          "</div></li>"
        );
      })
      .join("");
  }

  Promise.all([loadConfig(), loadBlog()]).then(function (pair) {
    applyConfig(pair[0]);
    renderBlog(pair[1]);
  });
})();
