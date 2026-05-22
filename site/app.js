(function () {
  const cfg = window.GMTJ_SITE || {};
  const apiUrl = (cfg.chatApiUrl || "").trim();

  const rawLang = (document.documentElement.getAttribute("lang") || "ja").toLowerCase();
  const langKey = rawLang.startsWith("zh")
    ? "zh"
    : { ja: 1, en: 1, ko: 1 }[rawLang.slice(0, 2)]
      ? rawLang.slice(0, 2)
      : "ja";

  const STR = {
    ja: {
      user: "あなた",
      assistant: "アシスタント",
      empty: "（応答がありませんでした）",
      wait: "回答を作成しています…",
      continue: "続けてご質問ください。",
      noApi: "チャットを利用できません。",
      sendFail: "送信に失敗しました。時間をおいて再度お試しください。",
      checkInput: "メッセージを入力してください。",
      leadPrompt:
        "ご興味をお持ちいただきありがとうございます。個別のご案内をご希望の方はメールアドレスを入力して送信してください。",
      leadThanks: "ありがとうございます。担当よりご連絡します。",
      leadSending: "送信中…",
      leadSend: "送信",
      leadPlaceholder: "例: name@example.com",
    },
    en: {
      user: "You",
      assistant: "Assistant",
      empty: "(No response received)",
      wait: "Generating a reply…",
      continue: "Feel free to ask another question.",
      noApi: "Chat is not available.",
      sendFail: "Something went wrong. Please try again shortly.",
      checkInput: "Please enter a message.",
      leadPrompt:
        "Thank you for your interest. If you would like a personal follow-up, leave your email below.",
      leadThanks: "Thank you. Our team will reach out shortly.",
      leadSending: "Sending…",
      leadSend: "Send",
      leadPlaceholder: "you@example.com",
    },
    ko: {
      user: "나",
      assistant: "어시스턴트",
      empty: "(응답이 없습니다)",
      wait: "답변을 작성 중입니다…",
      continue: "이어서 질문하실 수 있습니다.",
      noApi: "채팅을 이용할 수 없습니다.",
      sendFail: "전송에 실패했습니다. 잠시 후 다시 시도해 주세요.",
      checkInput: "메시지를 입력해 주세요.",
      leadPrompt: "관심 가져 주셔서 감사합니다. 개별 안내를 원하시면 이메일을 남겨 주세요.",
      leadThanks: "감사합니다. 담당자가 연락드리겠습니다.",
      leadSending: "전송 중…",
      leadSend: "보내기",
      leadPlaceholder: "name@example.com",
    },
    zh: {
      user: "您",
      assistant: "助手",
      empty: "（暂无回复）",
      wait: "正在生成回复…",
      continue: "欢迎继续提问。",
      noApi: "暂时无法使用对话功能。",
      sendFail: "发送失败，请稍后重试。",
      checkInput: "请输入内容。",
      leadPrompt: "感谢您的关注。如需单独说明，请留下邮箱。",
      leadThanks: "谢谢。我们会尽快与您联系。",
      leadSending: "发送中…",
      leadSend: "发送",
      leadPlaceholder: "you@example.com",
    },
  };

  const T = STR[langKey] || STR.ja;

  const panel = document.getElementById("chat-panel");
  const logEl = document.getElementById("chat-log");
  const input = document.getElementById("chat-input");
  const sendBtn = document.getElementById("chat-send");
  const statusEl = document.getElementById("chat-status");

  if (!panel || !logEl || !input || !sendBtn) return;

  const state = { messages: [], userTurns: 0, leadShown: false };

  function appendLine(role, text) {
    const row = document.createElement("div");
    row.className = "chat-row chat-row--" + role;
    const label = document.createElement("span");
    label.className = "chat-label";
    label.textContent = role === "user" ? T.user : T.assistant;
    const bubble = document.createElement("div");
    bubble.className = "chat-bubble";
    bubble.textContent = text;
    row.appendChild(label);
    row.appendChild(bubble);
    logEl.appendChild(row);
    logEl.scrollTop = logEl.scrollHeight;
    return row;
  }

  function appendCtaRow(cta) {
    if (!cta || !cta.label || !cta.url) return;
    const wrap = document.createElement("div");
    wrap.className = "chat-cta-row";
    const a = document.createElement("a");
    a.href = cta.url;
    a.textContent = cta.label;
    a.rel = "noopener noreferrer";
    const ty = cta.type || "info";
    if (ty === "booking") a.className = "btn-cta-booking";
    else if (ty === "purchase") a.className = "btn-cta-purchase";
    else a.className = "btn-cta-info";
    wrap.appendChild(a);
    logEl.appendChild(wrap);
    logEl.scrollTop = logEl.scrollHeight;
  }

  function maybeShowLead() {
    if (state.leadShown || state.userTurns < 3) return;
    const form = document.getElementById("chat-lead-form");
    if (!form || form.dataset.visible === "1") return;
    state.leadShown = true;
    form.hidden = false;
    form.dataset.visible = "1";
    if (!form.querySelector(".chat-lead-prompt")) {
      const p = document.createElement("p");
      p.className = "chat-lead-prompt";
      p.textContent = T.leadPrompt;
      form.insertBefore(p, form.firstChild);
    }
  }

  function setStatus(text, isError) {
    if (!statusEl) return;
    statusEl.textContent = text || "";
    statusEl.classList.toggle("chat-status--error", !!isError);
  }

  async function send() {
    const text = input.value.trim();
    if (!text) {
      setStatus(T.checkInput, true);
      return;
    }
    if (!apiUrl) {
      setStatus(T.noApi, true);
      return;
    }

    input.value = "";
    appendLine("user", text);
    state.messages.push({ role: "user", content: text });
    state.userTurns += 1;
    sendBtn.disabled = true;
    setStatus(T.wait, false);

    try {
      const res = await fetch(apiUrl, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ messages: state.messages }),
      });
      const data = await res.json().catch(() => ({}));
      if (!res.ok) {
        const errMsg = data.error || "HTTP " + res.status;
        throw new Error(errMsg);
      }
      const message = (data.message != null ? String(data.message) : String(data.reply || "")).trim() || T.empty;
      state.messages.push({ role: "assistant", content: message });
      appendLine("assistant", message);
      if (data.cta) appendCtaRow(data.cta);
      setStatus(T.continue, false);
      maybeShowLead();
    } catch (e) {
      state.messages.pop();
      if (logEl.lastChild) logEl.removeChild(logEl.lastChild);
      const detail = e && e.message ? String(e.message) : "";
      setStatus(detail && detail !== "Failed to fetch" ? T.sendFail + " (" + detail + ")" : T.sendFail, true);
    } finally {
      sendBtn.disabled = false;
      input.focus();
    }
  }

  const leadForm = document.getElementById("chat-lead-form");
  if (leadForm) {
    leadForm.addEventListener("submit", async function (ev) {
      ev.preventDefault();
      const em = document.getElementById("chat-lead-email");
      const v = (em && em.value) || "";
      if (!v.trim()) {
        setStatus(T.checkInput, true);
        return;
      }
      const submitBtn = leadForm.querySelector('button[type="submit"]');
      if (submitBtn) submitBtn.disabled = true;
      setStatus(T.leadSending || T.wait, false);
      const body = new URLSearchParams();
      body.append("form-name", "chat-lead");
      body.append("email", v.trim());
      body.append("source", "ai-concierge");
      body.append("page", location.href);
      body.append("bot-field", "");
      try {
        const res = await fetch("/", {
          method: "POST",
          headers: { "Content-Type": "application/x-www-form-urlencoded" },
          body,
        });
        if (!res.ok) throw new Error("HTTP " + res.status);
        leadForm.innerHTML = '<p class="chat-lead-thanks">' + T.leadThanks + "</p>";
        setStatus("", false);
      } catch {
        if (submitBtn) submitBtn.disabled = false;
        setStatus(T.sendFail, true);
      }
    });
  }

  sendBtn.addEventListener("click", send);
  input.addEventListener("keydown", function (ev) {
    if (ev.key === "Enter" && !ev.shiftKey) {
      ev.preventDefault();
      send();
    }
  });

  if (!apiUrl) {
    setStatus(T.noApi, true);
  } else {
    setStatus("", false);
  }
})();
