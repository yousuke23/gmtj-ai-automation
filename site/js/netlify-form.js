/**
 * Netlify Forms: AJAX submit + 完了メッセージ
 */
(function () {
  function encodeForm(form) {
    const body = new URLSearchParams();
    const name = form.getAttribute("name") || form.querySelector('[name="form-name"]')?.value;
    if (name) body.append("form-name", name);
    form.querySelectorAll("input, textarea, select").forEach(function (el) {
      if (!el.name || el.name === "form-name" || el.type === "submit" || el.disabled) return;
      if ((el.type === "radio" || el.type === "checkbox") && !el.checked) return;
      body.append(el.name, el.value);
    });
    return body;
  }

  function showDone(form, message) {
    const box = form.closest(".gmtj-form-panel") || form.parentElement;
    const done = document.createElement("p");
    done.className = "gmtj-form-done";
    done.textContent = message;
    form.replaceWith(done);
    if (box && box.scrollIntoView) box.scrollIntoView({ behavior: "smooth", block: "nearest" });
  }

  async function submitNetlifyForm(form, doneMessage) {
    const btn = form.querySelector('button[type="submit"]');
    if (btn) btn.disabled = true;
    try {
      const res = await fetch("/", {
        method: "POST",
        headers: { "Content-Type": "application/x-www-form-urlencoded" },
        body: encodeForm(form),
      });
      if (!res.ok) throw new Error("HTTP " + res.status);
      showDone(form, doneMessage);
      return true;
    } catch (e) {
      if (btn) btn.disabled = false;
      const err = form.querySelector(".gmtj-form-error");
      if (err) {
        err.hidden = false;
        err.textContent =
          "送信に失敗しました。しばらくして再試行するか、123@atono.jp へ直接メールしてください。";
      }
      return false;
    }
  }

  window.GMTJ_submitNetlifyForm = submitNetlifyForm;

  document.addEventListener("submit", function (ev) {
    const form = ev.target;
    if (!form || !form.matches || !form.matches("form[data-netlify].gmtj-form-ajax")) return;
    ev.preventDefault();
    const msg =
      form.getAttribute("data-done-message") ||
      "送信を受け付けました。48時間以内にご連絡いたします。確認メールが届かない場合は迷惑メールをご確認ください。";
    submitNetlifyForm(form, msg);
  });
})();
