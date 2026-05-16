/**
 * GMTJ site chrome: share strip, footer CTA, JSON-LD (Phase 1).
 * Loaded from /js/gmtj-chrome.js — portals use ../js/gmtj-chrome.js
 */
(function () {
  if (document.body && document.body.getAttribute("data-gmtj-chrome") === "off") return;

  var base = "https://gmtj-japan-music-tourism.netlify.app";
  try {
    if (location.origin && location.origin.indexOf("http") === 0) base = location.origin;
  } catch (e) {}

  function pageUrl() {
    return location.href.split("#")[0];
  }

  function pageTitle() {
    return document.title || "Japan Music Tourism";
  }

  function chatHref() {
    if (location.pathname === "/" || location.pathname === "/index.html") return "#chat";
    return base.replace(/\/$/, "") + "/index.html#chat";
  }

  function schemaType() {
    var p = location.pathname || "";
    if (p.indexOf("/tarnar") !== -1) return "EducationalOrganization";
    if (p.indexOf("/03-123-music-resorts") !== -1) return "LodgingBusiness";
    if (p.indexOf("/05-global-music-festival") !== -1) return "EventSeries";
    if (p.indexOf("/izu-fund") !== -1) return "Organization";
    return "LocalBusiness";
  }

  function injectJsonLd() {
    if (document.getElementById("gmtj-jsonld-org")) return;
    var s = document.createElement("script");
    s.type = "application/ld+json";
    s.id = "gmtj-jsonld-org";
    s.textContent = JSON.stringify({
      "@context": "https://schema.org",
      "@type": schemaType(),
      name: "Global Music Tourism Japan",
      url: base,
      description: pageTitle(),
      address: {
        "@type": "PostalAddress",
        streetAddress: "伊豆山",
        addressLocality: "熱海市",
        addressRegion: "静岡県",
        addressCountry: "JP",
      },
      contactPoint: {
        "@type": "ContactPoint",
        email: "123@atono.jp",
        availableLanguage: ["Japanese", "English", "Korean", "Chinese"],
      },
    });
    document.head.appendChild(s);
  }

  function shareStripHtml() {
    var u = encodeURIComponent(pageUrl());
    var t = encodeURIComponent(pageTitle() + " #JapanMusicTourism #伊豆山");
    return (
      '<div class="share-strip" role="navigation" aria-label="シェア">' +
      '<span>シェア:</span>' +
      '<a class="share-x" href="https://twitter.com/intent/tweet?url=' +
      u +
      "&text=" +
      t +
      '" target="_blank" rel="noopener">X</a>' +
      '<a href="https://www.facebook.com/sharer/sharer.php?u=' +
      u +
      '" target="_blank" rel="noopener">Facebook</a>' +
      '<a href="https://social-plugins.line.me/lineit/share?url=' +
      u +
      '" target="_blank" rel="noopener">LINE</a>' +
      '<button type="button" class="share-copy">リンクをコピー</button>' +
      "</div>"
    );
  }

  function mountShare() {
    var mount = document.querySelector("main.wrap") || document.querySelector("main");
    if (!mount || mount.querySelector(".share-strip-wrap")) return;
    var wrap = document.createElement("div");
    wrap.className = "share-strip-wrap";
    wrap.innerHTML = shareStripHtml();
    mount.insertBefore(wrap, mount.firstChild);

    var btn = wrap.querySelector(".share-copy");
    if (btn) {
      btn.addEventListener("click", function () {
        var url = pageUrl();
        if (navigator.clipboard && navigator.clipboard.writeText) {
          navigator.clipboard.writeText(url).catch(function () {
            window.prompt("URLをコピー", url);
          });
        } else {
          window.prompt("URLをコピー", url);
        }
      });
    }
  }

  function mountFooterCta() {
    var foot = document.querySelector("footer.site-footer") || document.querySelector("body > footer");
    if (!foot || document.getElementById("gmtj-cta-footer")) return;
    var sec = document.createElement("section");
    sec.id = "gmtj-cta-footer";
    sec.className = "cta-footer";
    sec.innerHTML =
      '<p class="cta-footer__lead">このサービスについて詳しく知りたい方は</p>' +
      '<div class="cta-footer__actions">' +
      '<a class="btn btn-cta-primary btn-mail js-gmtj-mailto" href="mailto:123@atono.jp">メールで問い合わせる</a>' +
      '<a class="btn btn-cta-secondary" href="' +
      chatHref() +
      '">AIに質問する</a>' +
      "</div>" +
      shareStripHtml();
    foot.parentNode.insertBefore(sec, foot);

    var mail = sec.querySelector(".js-gmtj-mailto");
    if (mail) {
      var subj = encodeURIComponent("[" + pageTitle() + "] についてのお問い合わせ");
      mail.href = "mailto:123@atono.jp?subject=" + subj;
    }

    var copy = sec.querySelector(".share-copy");
    if (copy) {
      copy.addEventListener("click", function () {
        var url = pageUrl();
        if (navigator.clipboard && navigator.clipboard.writeText) navigator.clipboard.writeText(url);
        else window.prompt("URL", url);
      });
    }
  }

  document.addEventListener("DOMContentLoaded", function () {
    injectJsonLd();
    mountShare();
    mountFooterCta();
  });
})();
