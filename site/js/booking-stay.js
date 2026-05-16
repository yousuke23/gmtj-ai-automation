(function () {
  "use strict";
  var PROPERTY_ID = "PROPERTY_ID";

  var I18N = {
    ja: {
      stayTitle: "宿泊予約",
      stayLead: "Booking.com のプレースホルダー物件へ日付付きで遷移します。直接予約は下のフォームから。",
      ci: "チェックイン",
      co: "チェックアウト",
      checkBtn: "空室を確認する",
      note: "※ PROPERTY_ID は運用で差し替えてください。",
      p1t: "スタンダードルーム",
      p1p: "¥15,000〜/泊",
      p1d: "朝食付き",
      p2t: "音楽体験パッケージ",
      p2p: "¥25,000〜/泊",
      p2d: "声楽レッスン + 温泉込み",
      p3t: "プレミアムリトリート",
      p3p: "¥45,000〜/泊",
      p3d: "3泊〜・プライベートレッスン付き",
      airbnb: "Airbnb で見る",
      formTitle: "直接予約（手数料なし）",
      fn: "お名前",
      fe: "メール",
      fci: "チェックイン",
      fco: "チェックアウト",
      fg: "人数",
      fr: "ご要望",
      fsend: "送信",
      fdone: "48時間以内にご確認のメールをお送りします。",
    },
    en: {
      stayTitle: "Stay & booking",
      stayLead: "Open Booking.com with dates (replace PROPERTY_ID). Prefer no OTA fee? Use the direct form.",
      ci: "Check-in",
      co: "Check-out",
      checkBtn: "Check availability",
      note: "Replace PROPERTY_ID with your Booking.com hotel slug.",
      p1t: "Standard room",
      p1p: "From ¥15,000/night",
      p1d: "Breakfast included",
      p2t: "Music experience package",
      p2p: "From ¥25,000/night",
      p2d: "Vocal lesson + onsen",
      p3t: "Premium retreat",
      p3p: "From ¥45,000/night",
      p3d: "3+ nights · private lesson",
      airbnb: "View on Airbnb",
      formTitle: "Direct booking (no OTA fee)",
      fn: "Name",
      fe: "Email",
      fci: "Check-in",
      fco: "Check-out",
      fg: "Guests",
      fr: "Requests",
      fsend: "Submit",
      fdone: "We will confirm by email within 48 hours.",
    },
  };

  function apply(lang) {
    var d = I18N[lang] || I18N.ja;
    document.querySelectorAll("[data-stay-i18n]").forEach(function (el) {
      var k = el.getAttribute("data-stay-i18n");
      if (k && d[k]) el.textContent = d[k];
    });
    document.querySelectorAll("[data-stay-lang]").forEach(function (b) {
      b.classList.toggle("lang-switch__btn--active", b.getAttribute("data-stay-lang") === lang);
    });
  }

  document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll("[data-stay-lang]").forEach(function (b) {
      b.addEventListener("click", function () {
        apply(b.getAttribute("data-stay-lang") || "ja");
      });
    });
    var btn = document.getElementById("stay-booking-search");
    if (btn) {
      btn.addEventListener("click", function () {
        var ci = document.getElementById("stay-ci");
        var co = document.getElementById("stay-co");
        var a = ci && ci.value;
        var b = co && co.value;
        if (!a || !b) {
          window.alert("日付を選択してください。");
          return;
        }
        var url =
          "https://www.booking.com/hotel/jp/" +
          PROPERTY_ID +
          ".html?checkin=" +
          encodeURIComponent(a) +
          "&checkout=" +
          encodeURIComponent(b);
        window.open(url, "_blank", "noopener,noreferrer");
      });
    }
    var form = document.querySelector(".stay-direct-form");
    if (form) {
      form.addEventListener("submit", function () {
        setTimeout(function () {
          var done = document.getElementById("stay-direct-done");
          if (done) done.hidden = false;
        }, 500);
      });
    }
  });
})();
