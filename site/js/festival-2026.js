(function () {
  "use strict";
  var PROPERTY_ID = "PROPERTY_ID";
  var target = new Date("2026-09-19T10:00:00+09:00").getTime();

  function pad(n) {
    return n < 10 ? "0" + n : String(n);
  }

  function tick() {
    var el = document.getElementById("fest-countdown");
    if (!el) return;
    var now = Date.now();
    var ms = Math.max(0, target - now);
    var s = Math.floor(ms / 1000);
    var days = Math.floor(s / 86400);
    var h = Math.floor((s % 86400) / 3600);
    var m = Math.floor((s % 3600) / 60);
    var sec = s % 60;
    el.textContent =
      "開幕まで " + days + " 日 " + pad(h) + " 時間 " + pad(m) + " 分 " + pad(sec) + " 秒（JST 2026-09-19 10:00）";
  }

  function wireForms() {
    document.querySelectorAll("#fest-forms form").forEach(function (f) {
      f.addEventListener("submit", function () {
        setTimeout(function () {
          var card = f.closest(".card");
          if (card) {
            var done = card.querySelector(".fest-done");
            if (done) done.hidden = false;
          }
        }, 400);
      });
    });
  }

  var F = {
    ja: {
      kicker: "ATAMI IZUSAN International Music Festival 2026",
      sub: "伊豆山神社参道837段 · 5会場",
      lead: "開催: 2026年9月19日（土）〜23日（水） · 入場無料（一部有料プログラムあり）",
    },
    en: {
      kicker: "ATAMI IZUSAN International Music Festival 2026",
      sub: "837 shrine steps, Izusan · 5 stages",
      lead: "Sep 19–23, 2026 · Free entry (some paid programs)",
    },
    ko: {
      kicker: "ATAMI IZUSAN International Music Festival 2026",
      sub: "이즈산 신사 참배길 837단 · 5개 스테이지",
      lead: "2026년 9월 19일(토)–23일(수) · 무료 입장(일부 유료 프로그램)",
    },
  };

  function applyLang(lang) {
    var x = F[lang] || F.ja;
    var k = document.getElementById("fest-kicker");
    var t = document.getElementById("fest-title");
    var l = document.getElementById("fest-lead");
    if (k) k.textContent = x.kicker;
    if (t) t.textContent = x.sub;
    if (l) l.textContent = x.lead;
    document.querySelectorAll("[data-fest-lang]").forEach(function (b) {
      b.classList.toggle("lang-switch__btn--active", b.getAttribute("data-fest-lang") === lang);
    });
  }

  document.addEventListener("DOMContentLoaded", function () {
    tick();
    setInterval(tick, 1000);
    wireForms();
    document.querySelectorAll("[data-fest-lang]").forEach(function (b) {
      b.addEventListener("click", function () {
        applyLang(b.getAttribute("data-fest-lang") || "ja");
      });
    });
  });
})();
