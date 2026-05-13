(function () {
  "use strict";

  var SESSION_KEY = "gmtj_os_session";
  var MEMO_KEY = "gmtj_os_memo";
  var THEME_KEY = "gmtj_os_theme";

  /** OS3 相当の運用モジュール（PDF の代わりにそのまま操作できる骨子） */
  var MODULES = [
    {
      vol: 1,
      title: "ビジョンと価値",
      blurb: "音楽ツーリズムの提供価値と、地域・ゲスト双方に対する約束事を言語化する。",
      body: [
        "旅行者が「音楽」を理由に選ぶ動機と、地域側が得たい経済・文化効果を一枚岩のストーリーにまとめます。",
        "AI は一次案内に留め、予約変更・トラブル・決済は人の窓口へ必ずエスカレーションする方針を明文化します。",
      ],
      tasks: [
        { id: "a", text: "提供価値（ゲスト向け）を3行で書いた" },
        { id: "b", text: "地域側のKPI（来訪・滞在・満足）を1つ選んだ" },
      ],
    },
    {
      vol: 2,
      title: "ブランドとトーン",
      blurb: "案内文・SNS・現場アナウンスでブレない声のトーンを固定する。",
      body: [
        "敬語レベル、絵文字の有無、緊急時の文体をテンプレに落とし込み、多言語版の「温度差」だけを調整します。",
      ],
      tasks: [
        { id: "a", text: "日本語ベースのトーンガイドを1ページにした" },
        { id: "b", text: "英語版で直訳せず自然な言い回しにした箇所をメモした" },
      ],
    },
    {
      vol: 3,
      title: "体験設計（ジャーニー）",
      blurb: "検索〜帰宅までのタッチポイントと、音楽コンテンツの見せ方を整理する。",
      body: [
        "フェス前後の宿泊・移動・周辺散策まで含めた「一日の物語」を設計し、混雑・天候・安全の注意喚起を差し込みます。",
      ],
      tasks: [
        { id: "a", text: "主要タッチポイントを時系列で10個以内にした" },
        { id: "b", text: "オフピーク誘導の案内文を用意した" },
      ],
    },
    {
      vol: 4,
      title: "多言語コミュニケーション",
      blurb: "日・英・他言語でのFAQ・案内の優先度と更新フローを決める。",
      body: [
        "翻訳は「正しさ」より「現場で伝わるか」を優先し、固有名詞・交通手段・チケット種別は用語集で統一します。",
      ],
      tasks: [
        { id: "a", text: "用語集（固有名詞10件）を作成した" },
        { id: "b", text: "更新オーナー（誰が最終承認か）を決めた" },
      ],
    },
    {
      vol: 5,
      title: "デジタル導線",
      blurb: "検索・SNS・公式サイトから予約・問い合わせへの導線を点検する。",
      body: [
        "UTM・ランディングの一貫性、モバイル表示、ページ速度の最低ラインをチェックリスト化します。",
      ],
      tasks: [
        { id: "a", text: "主要3導線の到達URLを記録した" },
        { id: "b", text: "モバイルでCTAが折りたたみ下に埋もれていないか確認した" },
      ],
    },
    {
      vol: 6,
      title: "スタッフ運用",
      blurb: "問い合わせ分類・返信SLA・引き継ぎテンプレを現場サイズに合わせる。",
      body: [
        "ピーク時のシフト想定と、AI下書き＋人間校正の二段構えを手順書にします。",
      ],
      tasks: [
        { id: "a", text: "優先度タグ（緊急/予約/一般）を3つ以内にした" },
        { id: "b", text: "引き継ぎメッセージのテンプレを1つ書いた" },
      ],
    },
    {
      vol: 7,
      title: "パートナー・地域連携",
      blurb: "宿・交通・観光協会との役割分担と情報の出どころを一本化する。",
      body: [
        "情報の正本（single source of truth）を決め、パートナー向けの更新通知チャネルを一本にします。",
      ],
      tasks: [
        { id: "a", text: "正本データの保管場所（URLまたはフォルダ）を決めた" },
        { id: "b", text: "連絡窓口一覧を作った" },
      ],
    },
    {
      vol: 8,
      title: "安全・法務・クレーム",
      blurb: "免責・撮影・未成年・キャンセル政策をゲスト向けに平易に説明する。",
      body: [
        "注意事項は箇条書きの羅列ではなく、シナリオ別（悪天候・開演遅延等）に短く分割します。",
      ],
      tasks: [
        { id: "a", text: "悪天候時の案内フローを1枚にした" },
        { id: "b", text: "問い合わせ窓口と返信SLAを記載した" },
      ],
    },
    {
      vol: 9,
      title: "計測と改善",
      blurb: "アンケート・ログ・売上のどれを週次で見るかを決める。",
      body: [
        "イベント単位でレビューを行い、次回に持ち越す「改善バックログ」を1リストに集約します。",
      ],
      tasks: [
        { id: "a", text: "週次で見る指標を3つに絞った" },
        { id: "b", text: "振り返りミーティングの議事テンプレを置いた" },
      ],
    },
    {
      vol: 10,
      title: "拡張とロードマップ",
      blurb: "パイロットから本番へ進むゲートと、次の機能投資の優先順位。",
      body: [
        "セキュリティ・個人情報・決済の有無で必要工程が変わるため、ゲートを明文化し、関係者で合意します。",
      ],
      tasks: [
        { id: "a", text: "パイロット完了の定義を書いた" },
        { id: "b", text: "次の3ヶ月でやらないことも1行で書いた" },
      ],
    },
  ];

  var THEMES = {
    sunset: { accent: "#e8b86a", accentSoft: "rgba(232, 184, 106, 0.15)" },
    ocean: { accent: "#6ec9ff", accentSoft: "rgba(110, 201, 255, 0.15)" },
    moss: { accent: "#8fd99f", accentSoft: "rgba(143, 217, 159, 0.15)" },
  };

  var loginEl = document.getElementById("login");
  var desktopEl = document.getElementById("desktop");
  var loginForm = document.getElementById("login-form");
  var loginErrorEl = document.getElementById("login-error");
  var windowsEl = document.getElementById("windows");
  var toastEl = document.getElementById("toast");
  var clockEl = document.getElementById("clock");

  function storageGet(key) {
    try {
      return localStorage.getItem(key);
    } catch (e) {
      return null;
    }
  }

  function storageSet(key, value) {
    try {
      localStorage.setItem(key, value);
      return true;
    } catch (e) {
      return false;
    }
  }

  function storageRemove(key) {
    try {
      localStorage.removeItem(key);
      return true;
    } catch (e) {
      return false;
    }
  }

  function sessionGet(key) {
    try {
      return sessionStorage.getItem(key);
    } catch (e) {
      return null;
    }
  }

  function sessionSet(key, value) {
    try {
      sessionStorage.setItem(key, value);
      return true;
    } catch (e) {
      return false;
    }
  }

  function sessionRemove(key) {
    try {
      sessionStorage.removeItem(key);
      return true;
    } catch (e) {
      return false;
    }
  }

  /** localStorage / sessionStorage がともに不可なときのみ（同一タブ内） */
  var volatileSession = null;

  function setLoginErr(msg) {
    if (!loginErrorEl) return;
    if (msg) {
      loginErrorEl.textContent = msg;
      loginErrorEl.hidden = false;
    } else {
      loginErrorEl.textContent = "";
      loginErrorEl.hidden = true;
    }
  }

  var windows = [];
  var nextWinId = 1;
  var zTop = 100;
  var dragState = null;

  function onDragMove(e) {
    if (!dragState) return;
    var win = windows.find(function (x) {
      return x.id === dragState.id;
    });
    if (!win || !dragState.el) return;
    var dx = e.clientX - dragState.px;
    var dy = e.clientY - dragState.py;
    win.x = Math.max(0, dragState.x + dx);
    win.y = Math.max(0, dragState.y + dy);
    var wrap = dragState.el;
    wrap.style.left = win.x + "px";
    wrap.style.top = win.y + "px";
    wrap.style.right = "";
    wrap.style.bottom = "";
    wrap.style.width = win.w + "px";
    wrap.style.height = win.h + "px";
    win.maxed = false;
  }

  function onDragEnd() {
    dragState = null;
    document.removeEventListener("pointermove", onDragMove);
    document.removeEventListener("pointerup", onDragEnd);
    document.removeEventListener("pointercancel", onDragEnd);
  }

  function showToast(msg, ms) {
    if (!toastEl) return;
    toastEl.textContent = msg;
    toastEl.hidden = false;
    clearTimeout(showToast._t);
    showToast._t = setTimeout(function () {
      toastEl.hidden = true;
    }, ms || 3200);
  }

  function normalizeSessionObject(o) {
    if (!o || typeof o !== "object" || Array.isArray(o)) return null;
    var nm =
      typeof o.name === "string" ? (o.name.trim() ? o.name.trim() : "ゲスト") : "ゲスト";
    var sn = typeof o.since === "number" && !isNaN(o.since) ? o.since : Date.now();
    return { name: nm, since: sn };
  }

  function parseSessionRaw(raw) {
    if (!raw || typeof raw !== "string") return null;
    try {
      return normalizeSessionObject(JSON.parse(raw));
    } catch (e) {
      return null;
    }
  }

  function loadSession() {
    var raw = storageGet(SESSION_KEY);
    var parsed = parseSessionRaw(raw);
    if (parsed) return parsed;
    if (raw) storageRemove(SESSION_KEY);

    raw = sessionGet(SESSION_KEY);
    parsed = parseSessionRaw(raw);
    if (parsed) return parsed;
    if (raw) sessionRemove(SESSION_KEY);

    if (volatileSession) return normalizeSessionObject(volatileSession);
    return null;
  }

  function saveSession(name) {
    var rec = { name: name || "ゲスト", since: Date.now() };
    volatileSession = rec;
    var data = JSON.stringify(rec);
    storageSet(SESSION_KEY, data);
    sessionSet(SESSION_KEY, data);
    return true;
  }

  function clearSession() {
    volatileSession = null;
    storageRemove(SESSION_KEY);
    sessionRemove(SESSION_KEY);
  }

  function applyTheme(id) {
    var t = THEMES[id] || THEMES.sunset;
    document.documentElement.style.setProperty("--accent", t.accent);
    document.documentElement.style.setProperty("--accent-soft", t.accentSoft);
    storageSet(THEME_KEY, id);
  }

  function loadTheme() {
    var id = storageGet(THEME_KEY) || "sunset";
    applyTheme(id);
    return id;
  }

  function tickClock() {
    if (!clockEl) return;
    var d = new Date();
    var w = ["日", "月", "火", "水", "木", "金", "土"][d.getDay()];
    clockEl.textContent =
      d.getFullYear() +
      "/" +
      (d.getMonth() + 1) +
      "/" +
      d.getDate() +
      "（" +
      w +
      "） " +
      d.toLocaleTimeString("ja-JP", { hour: "2-digit", minute: "2-digit" });
  }

  function closeAllMenus() {
    document.querySelectorAll(".menu-trigger[aria-expanded='true']").forEach(function (b) {
      b.setAttribute("aria-expanded", "false");
    });
    document.querySelectorAll(".menu-dropdown").forEach(function (ul) {
      ul.hidden = true;
    });
  }

  function setLoginVisible(showLogin) {
    if (!loginEl || !desktopEl) return;
    if (showLogin) {
      loginEl.hidden = false;
      loginEl.style.display = "flex";
      loginEl.style.visibility = "visible";
      loginEl.style.pointerEvents = "auto";
      desktopEl.hidden = true;
      desktopEl.style.display = "none";
      desktopEl.style.visibility = "hidden";
      desktopEl.style.pointerEvents = "none";
    } else {
      loginEl.hidden = true;
      loginEl.style.display = "none";
      loginEl.style.visibility = "hidden";
      loginEl.style.pointerEvents = "none";
      desktopEl.hidden = false;
      desktopEl.style.display = "flex";
      desktopEl.style.visibility = "visible";
      desktopEl.style.pointerEvents = "auto";
    }
    loginEl.setAttribute("aria-hidden", showLogin ? "false" : "true");
    desktopEl.setAttribute("aria-hidden", showLogin ? "true" : "false");
  }

  function chkKey(vol, taskId) {
    return "gmtj_chk_" + vol + "_" + taskId;
  }

  function isChecked(vol, taskId) {
    return storageGet(chkKey(vol, taskId)) === "1";
  }

  function setChecked(vol, taskId, on) {
    storageSet(chkKey(vol, taskId), on ? "1" : "0");
  }

  function cascadePosition(index) {
    var base = 24 + index * 28;
    return { x: base, y: 36 + index * 22 };
  }

  function findWin(kind, payload) {
    return windows.find(function (w) {
      if (w.kind !== kind) return false;
      if (payload === undefined) return true;
      return w.payload === payload;
    });
  }

  function bringToFront(id) {
    var w = windows.find(function (x) {
      return x.id === id;
    });
    if (!w || w.minimized) return;
    zTop += 1;
    w.z = zTop;
    var el = document.getElementById("win-" + id);
    if (el) el.style.zIndex = String(w.z);
    windows.forEach(function (x) {
      var node = document.getElementById("win-" + x.id);
      if (node) node.classList.toggle("focused", x.id === id);
    });
  }

  function removeWindow(id) {
    windows = windows.filter(function (w) {
      return w.id !== id;
    });
    var el = document.getElementById("win-" + id);
    if (el) el.remove();
  }

  function minimizeWindow(id) {
    var w = windows.find(function (x) {
      return x.id === id;
    });
    if (!w) return;
    w.minimized = true;
    var el = document.getElementById("win-" + id);
    if (el) el.hidden = true;
    showToast("ウィンドウを最小化しました（ドックから再オープンで復帰）", 2400);
  }

  function renderHub(container) {
    var grid = document.createElement("div");
    grid.className = "hub-grid";
    var tiles = [
      { t: "OS3 モジュール", d: "全10巻のチェックリスト", k: "modules" },
      { t: "メモ", d: "自動保存ノート", k: "memo" },
      { t: "ターミナル", d: "open コマンド", k: "terminal" },
      { t: "設定", d: "テーマ・データ消去", k: "settings" },
    ];
    tiles.forEach(function (tile) {
      var b = document.createElement("button");
      b.type = "button";
      b.className = "hub-tile";
      b.innerHTML = "<strong>" + tile.t + "</strong><span>" + tile.d + "</span>";
      b.addEventListener("click", function () {
        openOrFocus(tile.k);
      });
      grid.appendChild(b);
    });
    container.appendChild(grid);
  }

  function renderModulesLauncher(container) {
    var list = document.createElement("div");
    list.className = "mod-list";
    MODULES.forEach(function (m) {
      var b = document.createElement("button");
      b.type = "button";
      b.className = "mod-row";
      b.innerHTML =
        '<span class="mod-vol">' +
        m.vol +
        "</span><div><strong>" +
        escapeHtml(m.title) +
        "</strong><span>" +
        escapeHtml(m.blurb) +
        "</span></div>";
      b.addEventListener("click", function () {
        openOrFocus("module", m.vol);
      });
      list.appendChild(b);
    });
    container.appendChild(list);
  }

  function renderModuleDetail(container, vol) {
    var m = MODULES.find(function (x) {
      return x.vol === vol;
    });
    if (!m) return;
    var h2 = document.createElement("h2");
    h2.textContent = "OS3_" + m.vol + " — " + m.title;
    container.appendChild(h2);
    m.body.forEach(function (para) {
      var p = document.createElement("p");
      p.textContent = para;
      container.appendChild(p);
    });
    var ul = document.createElement("ul");
    ul.className = "checklist";
    m.tasks.forEach(function (task) {
      var li = document.createElement("li");
      var cb = document.createElement("input");
      cb.type = "checkbox";
      cb.checked = isChecked(m.vol, task.id);
      cb.addEventListener("change", function () {
        setChecked(m.vol, task.id, cb.checked);
      });
      var span = document.createElement("span");
      span.textContent = task.text;
      li.appendChild(cb);
      li.appendChild(span);
      ul.appendChild(li);
    });
    container.appendChild(ul);
  }

  function renderMemo(container) {
    var ta = document.createElement("textarea");
    ta.className = "memo-area";
    ta.value = storageGet(MEMO_KEY) || "";
    ta.placeholder = "現場メモ、次回イベントのTODO、用語のメモなど…";
    var t;
    ta.addEventListener("input", function () {
      clearTimeout(t);
      t = setTimeout(function () {
        storageSet(MEMO_KEY, ta.value);
      }, 400);
    });
    container.appendChild(ta);
  }

  function renderTerminal(container, win) {
    var out = document.createElement("pre");
    out.className = "term-out";
    out.textContent = win.termLog || "GMTJ OS ターミナル — help と入力してください。\n";
    var line = document.createElement("div");
    line.className = "term-line";
    line.innerHTML = "<span>$</span>";
    var input = document.createElement("input");
    input.type = "text";
    input.autocomplete = "off";
    input.setAttribute("aria-label", "コマンド");
    line.appendChild(input);
    container.appendChild(out);
    container.appendChild(line);

    function appendLog(s) {
      win.termLog = (win.termLog || "") + s + "\n";
      out.textContent = win.termLog;
      out.scrollTop = out.scrollHeight;
    }

    function run(cmd) {
      var parts = cmd.trim().split(/\s+/);
      var c = (parts[0] || "").toLowerCase();
      if (!c) return;
      if (c === "help") {
        appendLog(
          "コマンド: help | clear | date | whoami | open <hub|memo|settings|modules|module N>"
        );
        return;
      }
      if (c === "clear") {
        win.termLog = "";
        out.textContent = "";
        return;
      }
      if (c === "date") {
        appendLog(new Date().toString());
        return;
      }
      if (c === "whoami") {
        var s = loadSession();
        appendLog(s && s.name ? s.name : "guest");
        return;
      }
      if (c === "open" && parts[1]) {
        var target = parts[1].toLowerCase();
        if (target === "hub") {
          openOrFocus("hub");
          appendLog("opened hub");
          return;
        }
        if (target === "memo") {
          openOrFocus("memo");
          appendLog("opened memo");
          return;
        }
        if (target === "settings") {
          openOrFocus("settings");
          appendLog("opened settings");
          return;
        }
        if (target === "modules") {
          openOrFocus("modules");
          appendLog("opened modules");
          return;
        }
        if (target === "module" && parts[2]) {
          var n = parseInt(parts[2], 10);
          if (n >= 1 && n <= 10) {
            openOrFocus("module", n);
            appendLog("opened module " + n);
            return;
          }
        }
        appendLog("不明な open 先です");
        return;
      }
      appendLog("コマンドが見つかりません: " + cmd);
    }

    input.addEventListener("keydown", function (e) {
      if (e.key === "Enter") {
        var v = input.value;
        appendLog("$ " + v);
        run(v);
        input.value = "";
      }
    });
    setTimeout(function () {
      input.focus();
    }, 50);
  }

  function renderSettings(container) {
    var cur = loadTheme();
    var block = document.createElement("div");
    block.className = "settings-block";
    block.innerHTML = "<label>アクセントテーマ</label>";
    var sel = document.createElement("select");
    sel.innerHTML =
      '<option value="sunset"' +
      (cur === "sunset" ? " selected" : "") +
      ">サンセット</option>" +
      '<option value="ocean"' +
      (cur === "ocean" ? " selected" : "") +
      ">オーシャン</option>" +
      '<option value="moss"' +
      (cur === "moss" ? " selected" : "") +
      ">モス</option>";
    sel.addEventListener("change", function () {
      applyTheme(sel.value);
      showToast("テーマを更新しました");
    });
    block.appendChild(sel);
    container.appendChild(block);

    var block2 = document.createElement("div");
    block2.className = "settings-block";
    block2.innerHTML =
      "<label>データ</label><p style=\"margin:0 0 0.5rem;font-size:0.8rem;color:var(--muted)\">チェック・メモ・セッションを消去します。</p>";
    var reset = document.createElement("button");
    reset.type = "button";
    reset.className = "ghost";
    reset.textContent = "ローカルデータを消去";
    reset.addEventListener("click", function () {
      if (!confirm("チェック・メモ・ログイン状態を消去します。よろしいですか？")) return;
      try {
        Object.keys(localStorage).forEach(function (k) {
          if (
            k.indexOf("gmtj_") === 0 ||
            k === MEMO_KEY ||
            k === SESSION_KEY ||
            k === THEME_KEY
          ) {
            try {
              localStorage.removeItem(k);
            } catch (e2) {}
          }
        });
      } catch (e) {}
      clearSession();
      location.reload();
    });
    block2.appendChild(reset);
    container.appendChild(block2);
  }

  function renderShortcuts(container) {
    container.innerHTML =
      "<h2>ショートカット</h2>" +
      "<p>メニューバーの「表示」からウィンドウ操作。</p>" +
      "<ul class=\"checklist\"><li><span>ドラッグ — タイトルバーでウィンドウ移動</span></li>" +
      "<li><span>赤ボタン — 閉じる / 黄 — 最小化 / 緑 — 画面いっぱいに切替</span></li>" +
      "<li><span>ターミナルで <code>open module 3</code> のように起動可能</span></li></ul>";
  }

  function escapeHtml(s) {
    return String(s)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");
  }

  function fillWindowBody(win, bodyEl) {
    bodyEl.innerHTML = "";
    if (win.kind === "hub") renderHub(bodyEl);
    else if (win.kind === "modules") renderModulesLauncher(bodyEl);
    else if (win.kind === "module") renderModuleDetail(bodyEl, win.payload);
    else if (win.kind === "memo") renderMemo(bodyEl);
    else if (win.kind === "terminal") renderTerminal(bodyEl, win);
    else if (win.kind === "settings") renderSettings(bodyEl);
    else if (win.kind === "shortcuts") renderShortcuts(bodyEl);
  }

  function mountWindow(win) {
    if (!windowsEl) {
      console.error("GMTJ OS: #windows が見つかりません");
      return false;
    }
    var wrap = document.createElement("div");
    wrap.id = "win-" + win.id;
    wrap.className = "win focused";
    wrap.style.zIndex = String(win.z);
    wrap.style.left = win.x + "px";
    wrap.style.top = win.y + "px";
    wrap.style.width = win.w + "px";
    wrap.style.height = win.h + "px";

    var tb = document.createElement("div");
    tb.className = "win-titlebar";

    var dots = document.createElement("div");
    dots.className = "win-dots";
    ["close", "min", "max"].forEach(function (kind) {
      var dot = document.createElement("button");
      dot.type = "button";
      dot.className = "win-dot " + kind;
      dot.setAttribute("aria-label", kind === "close" ? "閉じる" : kind === "min" ? "最小化" : "拡大");
      dot.addEventListener("click", function (e) {
        e.stopPropagation();
        if (kind === "close") removeWindow(win.id);
        else if (kind === "min") minimizeWindow(win.id);
        else {
          win.maxed = !win.maxed;
          var stage = document.getElementById("stage").getBoundingClientRect();
          if (win.maxed) {
            win._restore = { x: win.x, y: win.y, w: win.w, h: win.h };
            var pad = 8;
            win.x = pad;
            win.y = pad;
            win.w = Math.max(240, stage.width - pad * 2);
            win.h = Math.max(160, stage.height - pad * 2);
            wrap.style.left = win.x + "px";
            wrap.style.top = win.y + "px";
            wrap.style.width = win.w + "px";
            wrap.style.height = win.h + "px";
            wrap.style.right = "";
            wrap.style.bottom = "";
          } else if (win._restore) {
            win.x = win._restore.x;
            win.y = win._restore.y;
            win.w = win._restore.w;
            win.h = win._restore.h;
            wrap.style.left = win.x + "px";
            wrap.style.top = win.y + "px";
            wrap.style.width = win.w + "px";
            wrap.style.height = win.h + "px";
          }
        }
      });
      dots.appendChild(dot);
    });

    var title = document.createElement("div");
    title.className = "win-title";
    title.textContent = win.title;

    tb.appendChild(dots);
    tb.appendChild(title);

    var body = document.createElement("div");
    body.className = "win-body";
    fillWindowBody(win, body);

    tb.addEventListener("pointerdown", function (e) {
      if (e.target.closest(".win-dot")) return;
      dragState = {
        id: win.id,
        px: e.clientX,
        py: e.clientY,
        x: win.x,
        y: win.y,
        el: wrap,
      };
      document.addEventListener("pointermove", onDragMove);
      document.addEventListener("pointerup", onDragEnd);
      document.addEventListener("pointercancel", onDragEnd);
      bringToFront(win.id);
    });

    wrap.addEventListener("pointerdown", function () {
      bringToFront(win.id);
    });

    wrap.appendChild(tb);
    wrap.appendChild(body);
    windowsEl.appendChild(wrap);
    return true;
  }

  function titleForKind(kind, payload) {
    if (kind === "hub") return "ハブ";
    if (kind === "modules") return "OS3 モジュール";
    if (kind === "memo") return "メモ";
    if (kind === "terminal") return "ターミナル";
    if (kind === "settings") return "設定";
    if (kind === "shortcuts") return "ショートカット";
    if (kind === "module") {
      var m = MODULES.find(function (x) {
        return x.vol === payload;
      });
      return m ? "OS3_" + payload + " " + m.title : "モジュール";
    }
    return "ウィンドウ";
  }

  function openOrFocus(kind, payload) {
    var exist = findWin(kind, payload);
    if (exist) {
      if (exist.minimized) {
        exist.minimized = false;
        var el = document.getElementById("win-" + exist.id);
        if (el) el.hidden = false;
      }
      bringToFront(exist.id);
      return;
    }
    var idx = windows.length;
    var pos = cascadePosition(idx);
    var w = 420;
    var h = 360;
    if (kind === "module") {
      w = 440;
      h = 400;
    }
    if (kind === "memo") {
      w = 480;
      h = 420;
    }
    if (kind === "terminal") {
      w = 460;
      h = 380;
    }
    var win = {
      id: nextWinId++,
      kind: kind,
      payload: payload,
      title: titleForKind(kind, payload),
      x: pos.x,
      y: pos.y,
      w: w,
      h: h,
      z: ++zTop,
      minimized: false,
      maxed: false,
      termLog: "",
    };
    windows.push(win);
    if (!mountWindow(win)) {
      windows.pop();
      showToast("ウィンドウを開けませんでした。", 4000);
      return;
    }
    bringToFront(win.id);
  }

  function tileWindows() {
    var openW = windows.filter(function (w) {
      return !w.minimized;
    });
    if (!openW.length) return;
    var n = openW.length;
    var stage = document.getElementById("stage").getBoundingClientRect();
    var cols = n <= 2 ? n : 2;
    var rows = Math.ceil(n / cols);
    var cw = Math.floor((stage.width - 16) / cols);
    var ch = Math.floor((stage.height - 16) / rows);
    openW.forEach(function (w, i) {
      var col = i % cols;
      var row = Math.floor(i / cols);
      w.x = 8 + col * cw;
      w.y = 8 + row * ch;
      w.w = cw - 8;
      w.h = ch - 8;
      w.maxed = false;
      var el = document.getElementById("win-" + w.id);
      if (el) {
        el.style.left = w.x + "px";
        el.style.top = w.y + "px";
        el.style.width = w.w + "px";
        el.style.height = w.h + "px";
        el.style.right = "";
        el.style.bottom = "";
      }
    });
    showToast("ウィンドウを並べました");
  }

  function closeAllWindows() {
    windows.slice().forEach(function (w) {
      removeWindow(w.id);
    });
    showToast("すべて閉じました");
  }

  document.addEventListener("pointerdown", function (e) {
    if (!e.target.closest(".menu-root")) closeAllMenus();
  });

  document.querySelectorAll(".menu-trigger").forEach(function (btn) {
    btn.addEventListener("click", function (e) {
      e.stopPropagation();
      var mid = btn.getAttribute("data-menu");
      var open = btn.getAttribute("aria-expanded") === "true";
      closeAllMenus();
      if (!open) {
        btn.setAttribute("aria-expanded", "true");
        var ul = document.getElementById("menu-" + mid);
        if (ul) ul.hidden = false;
      }
    });
  });

  document.querySelectorAll(".menu-dropdown button").forEach(function (b) {
    b.addEventListener("click", function () {
      var act = b.getAttribute("data-action");
      closeAllMenus();
      if (act === "logout") {
        clearSession();
        location.reload();
      } else if (act === "about") {
        showToast("GMTJ OS — ブラウザ上の運用デスクトップ（静的フロントのみ）", 4000);
      } else if (act === "automation-show") {
        refreshAutomationStrip();
        showToast("今日の自動実行パネルを表示しました", 2500);
      } else if (act === "tile") tileWindows();
      else if (act === "close-all") closeAllWindows();
      else if (act === "help-shortcuts") openOrFocus("shortcuts");
    });
  });

  document.querySelectorAll(".dock-item[data-open]").forEach(function (btn) {
    btn.addEventListener("click", function () {
      var k = btn.getAttribute("data-open");
      openOrFocus(k);
    });
  });

  function tryEnterDesktop() {
    setLoginErr("");
    try {
      enterDesktop();
    } catch (err) {
      console.error(err);
      clearSession();
      setLoginVisible(true);
      setLoginErr(
        "画面の起動に失敗しました。ページを再読み込みするか、「ストレージを使わず入室」を試してください。"
      );
    }
  }

  if (loginForm) {
    loginForm.addEventListener("submit", function (e) {
      e.preventDefault();
      var name = document.getElementById("login-name");
      var nameVal = name ? name.value.trim() : "";
      saveSession(nameVal);
      tryEnterDesktop();
    });
  }

  var skipBtn = document.getElementById("login-skip");
  if (skipBtn) {
    skipBtn.addEventListener("click", function () {
      var name = document.getElementById("login-name");
      var nameVal = name ? name.value.trim() : "";
      clearSession();
      volatileSession = {
        name: nameVal || "ゲスト",
        since: Date.now(),
      };
      tryEnterDesktop();
    });
  }

  var AUTOMATION_DATA_URL = "data/automation-summary.json";

  function escapeHtml(s) {
    return String(s)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");
  }

  function jstNowLabel() {
    try {
      return new Intl.DateTimeFormat("ja-JP", {
        timeZone: "Asia/Tokyo",
        dateStyle: "medium",
        timeStyle: "short",
      }).format(new Date());
    } catch (e) {
      return String(new Date());
    }
  }

  function renderAutomationFromJson(data) {
    var body = document.getElementById("automation-strip-body");
    var todayEl = document.getElementById("automation-today");
    if (!body || !todayEl) return;
    todayEl.textContent = jstNowLabel();
    var parts = [];
    if (data.note) {
      parts.push(
        '<p class="automation-block" style="color:var(--muted);margin:0 0 0.35rem;">' +
          escapeHtml(data.note) +
          "</p>"
      );
    }
    if (data.grokReview) {
      parts.push(
        '<p class="automation-block" style="color:var(--muted);margin:0 0 0.35rem;font-size:0.68rem;">Grok: ' +
          escapeHtml(data.grokReview) +
          "</p>"
      );
    }
    var p1 = data.phase1 || {};
    if (p1["08_tana_voice_school"]) {
      var b = p1["08_tana_voice_school"];
      parts.push('<div class="automation-block"><h3>' + escapeHtml(b.title) + "</h3><ul>");
      (b.automations || []).forEach(function (a) {
        parts.push(
          "<li>" +
            escapeHtml(a.label) +
            " — <span style=\"color:var(--muted)\">" +
            escapeHtml(a.status) +
            "</span></li>"
        );
      });
      parts.push("</ul></div>");
    }
    if (p1["21_izu_music_fund"]) {
      var f = p1["21_izu_music_fund"];
      parts.push('<div class="automation-block"><h3>' + escapeHtml(f.title) + "</h3><ul>");
      (f.automations || []).forEach(function (a) {
        parts.push(
          "<li>" +
            escapeHtml(a.label) +
            " — <span style=\"color:var(--muted)\">" +
            escapeHtml(a.status) +
            "</span></li>"
        );
      });
      parts.push("</ul></div>");
    }
    var slots = data.workflowSlots42 || [];
    parts.push(
      '<div class="automation-block"><h3>42レーン（日次／レビュー）</h3><div class="automation-slot-grid">'
    );
    slots.forEach(function (s) {
      parts.push(
        '<div class="automation-slot" title="' +
          escapeHtml(s.businessName || "") +
          '">' +
          escapeHtml(String(s.businessId || "")) +
          " · " +
          escapeHtml(String(s.lane || "")) +
          "</div>"
      );
    });
    parts.push("</div></div>");
    body.innerHTML = parts.join("");
  }

  function showAutomationFallback(msg) {
    var body = document.getElementById("automation-strip-body");
    var todayEl = document.getElementById("automation-today");
    if (todayEl) todayEl.textContent = jstNowLabel();
    if (body) {
      body.innerHTML =
        '<p class="automation-block">' +
        escapeHtml(msg || "サマリーの読み込みに失敗しました。") +
        "</p>";
    }
  }

  function refreshAutomationStrip() {
    var strip = document.getElementById("automation-strip");
    var desk = document.getElementById("desktop");
    if (!strip || !desk) return;
    strip.hidden = false;
    desk.classList.add("has-automation-strip");
    fetch(AUTOMATION_DATA_URL + "?t=" + Date.now(), { cache: "no-store" })
      .then(function (r) {
        if (!r.ok) throw new Error("HTTP " + r.status);
        return r.json();
      })
      .then(renderAutomationFromJson)
      .catch(function () {
        showAutomationFallback(
          "data/automation-summary.json を取得できませんでした（file:// またはオフライン）。http(s) で開き直してください。"
        );
      });
  }

  function hideAutomationStrip() {
    var strip = document.getElementById("automation-strip");
    var desk = document.getElementById("desktop");
    if (strip) strip.hidden = true;
    if (desk) desk.classList.remove("has-automation-strip");
  }

  var arBtn = document.getElementById("automation-refresh");
  if (arBtn) {
    arBtn.addEventListener("click", function () {
      refreshAutomationStrip();
    });
  }
  var acBtn = document.getElementById("automation-collapse");
  if (acBtn) {
    acBtn.addEventListener("click", function () {
      hideAutomationStrip();
    });
  }

  var clockTimerStarted = false;

  function enterDesktop() {
    loadTheme();
    setLoginVisible(false);
    tickClock();
    if (!clockTimerStarted) {
      clockTimerStarted = true;
      setInterval(tickClock, 1000);
    }
    openOrFocus("hub");
    refreshAutomationStrip();
  }

  var existing = loadSession();
  if (existing) {
    var nameInput = document.getElementById("login-name");
    if (nameInput) nameInput.value = existing.name || "";
    tryEnterDesktop();
  } else {
    setLoginVisible(true);
  }
})();
