/**
 * mailto: が開かない環境向け — Gmail / コピー / ネイティブ mailto の選択肢を表示
 */
(function () {
  function parseMailto(href) {
    var raw = (href || "mailto:123@atono.jp").replace(/^mailto:/i, "");
    var q = raw.indexOf("?");
    var toPart = q === -1 ? raw : raw.slice(0, q);
    var to = decodeURIComponent(toPart).trim() || "123@atono.jp";
    var params = new URLSearchParams(q === -1 ? "" : raw.slice(q + 1));
    return {
      to: to,
      subject: params.get("subject") || "",
      body: params.get("body") || "",
    };
  }

  function gmailComposeUrl(parsed) {
    var u =
      "https://mail.google.com/mail/?view=cm&fs=1&to=" + encodeURIComponent(parsed.to);
    if (parsed.subject) u += "&su=" + encodeURIComponent(parsed.subject);
    if (parsed.body) u += "&body=" + encodeURIComponent(parsed.body);
    return u;
  }

  function showChooser(href) {
    var parsed = parseMailto(href);
    var id = "gmtj-mailto-chooser";
    var old = document.getElementById(id);
    if (old) old.remove();

    var backdrop = document.createElement("div");
    backdrop.id = id;
    backdrop.setAttribute("role", "dialog");
    backdrop.setAttribute("aria-modal", "true");
    backdrop.setAttribute("aria-label", "メールで問い合わせ");
    backdrop.style.cssText =
      "position:fixed;inset:0;z-index:99999;background:rgba(0,0,0,.55);display:flex;align-items:center;justify-content:center;padding:1rem;";

    var box = document.createElement("div");
    box.style.cssText =
      "max-width:22rem;width:100%;background:#1a222d;color:#e8eef5;border-radius:12px;padding:1.1rem 1.2rem;border:1px solid #2a3544;font-family:system-ui,sans-serif;font-size:0.92rem;line-height:1.5;";

    box.innerHTML =
      "<p style=\"margin:0 0 0.75rem;font-weight:600\">メールで問い合わせ</p>" +
      "<p style=\"margin:0 0 1rem;color:#8b98a8;font-size:0.86rem\">メールアプリが開かない場合は、Gmail またはアドレスコピーをお使いください。</p>" +
      "<p style=\"margin:0 0 1rem;word-break:break-all\"><strong>" +
      parsed.to +
      "</strong></p>";

    function btn(label, primary) {
      var b = document.createElement("button");
      b.type = "button";
      b.textContent = label;
      b.style.cssText =
        "display:block;width:100%;margin:0 0 0.5rem;padding:0.55rem 0.75rem;border-radius:8px;font:inherit;font-weight:600;cursor:pointer;border:" +
        (primary ? "none;background:#1d9e75;color:#fff" : "1px solid #2a3544;background:transparent;color:#e8eef5");
      return b;
    }

    var nativeBtn = btn("メールアプリで開く", true);
    nativeBtn.addEventListener("click", function () {
      window.location.href = href;
      backdrop.remove();
    });

    var gmailBtn = btn("Gmail で作成", false);
    gmailBtn.addEventListener("click", function () {
      window.open(gmailComposeUrl(parsed), "_blank", "noopener,noreferrer");
      backdrop.remove();
    });

    var copyBtn = btn("アドレスをコピー", false);
    copyBtn.addEventListener("click", function () {
      var done = function () {
        copyBtn.textContent = "コピーしました";
        setTimeout(function () {
          backdrop.remove();
        }, 600);
      };
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(parsed.to).then(done).catch(function () {
          window.prompt("コピーしてください", parsed.to);
        });
      } else {
        window.prompt("コピーしてください", parsed.to);
        done();
      }
    });

    var closeBtn = document.createElement("button");
    closeBtn.type = "button";
    closeBtn.textContent = "閉じる";
    closeBtn.style.cssText =
      "margin-top:0.35rem;background:none;border:none;color:#8b98a8;font:inherit;cursor:pointer;text-decoration:underline;";
    closeBtn.addEventListener("click", function () {
      backdrop.remove();
    });

    box.appendChild(nativeBtn);
    box.appendChild(gmailBtn);
    box.appendChild(copyBtn);
    box.appendChild(closeBtn);
    backdrop.appendChild(box);
    backdrop.addEventListener("click", function (e) {
      if (e.target === backdrop) backdrop.remove();
    });
    document.body.appendChild(backdrop);
    nativeBtn.focus();
  }

  window.GMTJ_openMail = showChooser;

  function bindMailLinks(root) {
    (root || document).querySelectorAll('a[href^="mailto:"]').forEach(function (a) {
      if (a.dataset.gmtjMailBound === "1") return;
      a.dataset.gmtjMailBound = "1";
      a.addEventListener("click", function (e) {
        e.preventDefault();
        showChooser(a.getAttribute("href") || "mailto:123@atono.jp");
      });
    });
  }

  document.addEventListener("DOMContentLoaded", function () {
    bindMailLinks(document);
  });
})();
