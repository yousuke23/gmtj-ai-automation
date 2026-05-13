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
    },
  };

  const T = STR[langKey] || STR.ja;

  const panel = document.getElementById("chat-panel");
  const logEl = document.getElementById("chat-log");
  const input = document.getElementById("chat-input");
  const sendBtn = document.getElementById("chat-send");
  const statusEl = document.getElementById("chat-status");

  if (!panel || !logEl || !input || !sendBtn) return;

  const state = { messages: [] };

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
        throw new Error(data.error || "HTTP " + res.status);
      }
      const reply = (data.reply || "").trim() || T.empty;
      state.messages.push({ role: "assistant", content: reply });
      appendLine("assistant", reply);
      setStatus(T.continue, false);
    } catch (e) {
      state.messages.pop();
      if (logEl.lastChild) logEl.removeChild(logEl.lastChild);
      setStatus(T.sendFail, true);
    } finally {
      sendBtn.disabled = false;
      input.focus();
    }
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
