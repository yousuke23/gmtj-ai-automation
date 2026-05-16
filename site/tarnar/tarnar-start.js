(function () {
  "use strict";

  var LANG = "ja";
  var calLoaded = false;
  var calShown = false;

  var I18N = {
    ja: {
      startTitle: "今すぐ始める",
      startLead:
        "体験は Calendly で予約、月額は Stripe の Payment Link（差し替え可）からお申し込みいただけます。",
      trialTitle: "体験レッスン",
      trialPrice: "¥3,000（1回・30分）",
      trialDesc: "まずは短時間で声の使い方と目標をすり合わせます。",
      trialBook: "体験レッスンを予約する",
      basicTitle: "ベーシック",
      basicPrice: "¥9,800/月（税込）",
      basicDesc: "月4回レッスン＋教材セット。",
      basicCta: "ベーシックを購入",
      proTitle: "プロ",
      proPrice: "¥19,800/月（税込）",
      proDesc: "月8回＋個別フィードバック＋教材。",
      proCta: "プロを購入",
      langJa: "日本語",
      langEn: "English",
      calTitle: "体験レッスン — 日程選択",
    },
    en: {
      startTitle: "Get started",
      startLead:
        "Book a trial on Calendly; subscribe to monthly plans via Stripe Payment Links (replaceable).",
      trialTitle: "Trial Lesson",
      trialPrice: "¥3,000 (30 min, one-time)",
      trialDesc: "Short session to align goals and vocal approach.",
      trialBook: "Book trial lesson",
      basicTitle: "Basic Plan",
      basicPrice: "¥9,800/month (tax incl.)",
      basicDesc: "4 lessons per month + materials.",
      basicCta: "Purchase Basic",
      proTitle: "Pro Plan",
      proPrice: "¥19,800/month (tax incl.)",
      proDesc: "8 lessons + premium feedback + materials.",
      proCta: "Purchase Pro",
      langJa: "日本語",
      langEn: "English",
      calTitle: "Trial lesson — pick a time",
    },
  };

  function t(key) {
    return (I18N[LANG] && I18N[LANG][key]) || I18N.ja[key] || key;
  }

  function applyLang() {
    document.querySelectorAll("[data-i18n]").forEach(function (el) {
      var k = el.getAttribute("data-i18n");
      if (k && t(k)) el.textContent = t(k);
    });
    var cal = document.getElementById("calendly-inline");
    if (cal) {
      var url =
        LANG === "en"
          ? cal.getAttribute("data-url-en") || cal.getAttribute("data-url")
          : cal.getAttribute("data-url");
      cal.setAttribute("data-url", url);
    }
  }

  function loadCalendlyScript(cb) {
    if (window.Calendly) {
      cb();
      return;
    }
    if (calLoaded) return;
    calLoaded = true;
    var s = document.createElement("script");
    s.src = "https://assets.calendly.com/assets/external/widget.js";
    s.async = true;
    s.onload = function () {
      cb();
    };
    document.body.appendChild(s);
  }

  function showCalendly() {
    var wrap = document.getElementById("calendly-wrap");
    var host = document.getElementById("calendly-inline");
    if (!wrap || !host) return;
    wrap.hidden = false;
    calShown = true;
    loadCalendlyScript(function () {
      host.innerHTML = "";
      var url = host.getAttribute("data-url") || "https://calendly.com/TANA_PLACEHOLDER/trial-lesson";
      if (window.Calendly && typeof window.Calendly.initInlineWidget === "function") {
        window.Calendly.initInlineWidget({ url: url, parentElement: host });
      }
      wrap.scrollIntoView({ behavior: "smooth", block: "start" });
    });
  }

  function wireStripePlaceholders() {
    document.querySelectorAll("[data-stripe-link]").forEach(function (btn) {
      btn.addEventListener("click", function (e) {
        e.preventDefault();
        var href = (btn.getAttribute("data-stripe-link") || "").trim();
        if (href && href !== "PLACEHOLDER") {
          window.open(href, "_blank", "noopener,noreferrer");
          return;
        }
        window.location.href =
          "mailto:123@atono.jp?subject=" +
          encodeURIComponent("AI TARNAR Voice School 月額プラン") +
          "&body=" +
          encodeURIComponent("ご希望プラン: " + (btn.getAttribute("data-plan") || "") + "\nお名前・連絡先をご記載ください。");
      });
    });
  }

  document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll("[data-lang-switch]").forEach(function (b) {
      b.addEventListener("click", function () {
        LANG = b.getAttribute("data-lang-switch") === "en" ? "en" : "ja";
        document.documentElement.setAttribute("lang", LANG === "en" ? "en" : "ja");
        document.querySelectorAll("[data-lang-switch]").forEach(function (x) {
          x.classList.toggle("lang-switch__btn--active", x.getAttribute("data-lang-switch") === LANG);
        });
        applyLang();
      });
    });
    var bookBtn = document.getElementById("btn-calendly-trial");
    if (bookBtn) bookBtn.addEventListener("click", showCalendly);
    var bookBtn2 = document.getElementById("btn-calendly-trial-card");
    if (bookBtn2) bookBtn2.addEventListener("click", showCalendly);
    applyLang();
    wireStripePlaceholders();
  });
})();
