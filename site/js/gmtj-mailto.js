/**
 * メールボタン → お問い合わせフォーム（モーダル）を表示
 */
(function () {
  function contactFormHtml() {
    return (
      '<form name="contact" method="POST" data-netlify="true" data-netlify-honeypot="bot-field" class="gmtj-form-ajax gmtj-modal-form">' +
      '<input type="hidden" name="form-name" value="contact" />' +
      '<p class="bot-field" style="position:absolute;left:-9999px"><label>Do not fill<input name="bot-field" /></label></p>' +
      '<label class="gmtj-form-label">お名前<input type="text" name="name" autocomplete="name" required /></label>' +
      '<label class="gmtj-form-label">メールアドレス<input type="email" name="email" autocomplete="email" required /></label>' +
      '<label class="gmtj-form-label">お問い合わせ内容<textarea name="message" rows="4" required placeholder="ご質問・ご相談内容"></textarea></label>' +
      '<p class="gmtj-form-error" hidden></p>' +
      '<button type="submit" class="btn btn-primary">送信する</button>' +
      "</form>"
    );
  }

  function showContactModal() {
    var id = "gmtj-contact-modal";
    var old = document.getElementById(id);
    if (old) old.remove();

    var backdrop = document.createElement("div");
    backdrop.id = id;
    backdrop.setAttribute("role", "dialog");
    backdrop.setAttribute("aria-modal", "true");
    backdrop.setAttribute("aria-label", "お問い合わせフォーム");
    backdrop.className = "gmtj-modal-backdrop";

    var box = document.createElement("div");
    box.className = "gmtj-modal-box";
    box.innerHTML =
      "<h3 class=\"gmtj-modal-title\">お問い合わせ</h3>" +
      "<p class=\"gmtj-modal-lead\">内容を入力して送信してください。担当より48時間以内にご連絡します。</p>" +
      contactFormHtml() +
      '<button type="button" class="gmtj-modal-close">閉じる</button>';

    backdrop.appendChild(box);
    backdrop.addEventListener("click", function (e) {
      if (e.target === backdrop) backdrop.remove();
    });
    box.querySelector(".gmtj-modal-close").addEventListener("click", function () {
      backdrop.remove();
    });
    document.body.appendChild(backdrop);
    var first = box.querySelector("input:not([type=hidden])");
    if (first) first.focus();
  }

  window.GMTJ_openContactForm = showContactModal;

  function bindMailTriggers(root) {
    (root || document).querySelectorAll("[data-open-contact-form], .js-gmtj-mailto").forEach(function (el) {
      if (el.dataset.gmtjFormBound === "1") return;
      el.dataset.gmtjFormBound = "1";
      el.addEventListener("click", function (e) {
        e.preventDefault();
        showContactModal();
      });
    });
    (root || document).querySelectorAll('a[href^="mailto:123@atono.jp"]').forEach(function (a) {
      if (a.dataset.gmtjFormBound === "1" || a.closest(".gmtj-modal-form")) return;
      if (a.classList.contains("js-gmtj-mailto")) return;
      a.dataset.gmtjFormBound = "1";
      a.addEventListener("click", function (e) {
        e.preventDefault();
        showContactModal();
      });
    });
  }

  document.addEventListener("DOMContentLoaded", function () {
    bindMailTriggers(document);
  });
})();
