const STORAGE_KEY = "lemmikos_state_v1";
const STAGES = ["Sourced", "Screened", "Client Review", "Interview", "Offer"];

const automationRules = [
  "If score >= 85, advance one stage per automation cycle.",
  "If score < 70 and still in Sourced, flag for manual review.",
  "When moved to Interview, create follow-up task in 24h.",
  "When moved to Offer, alert account lead and client contact."
];

const seedState = {
  clients: [
    { id: "c1", company: "Apex Infrastructure", contact: "Dana West", email: "dana@apexinfra.com", priority: "High", createdAt: "2026-03-01" },
    { id: "c2", company: "North Ridge Builders", contact: "Kieran Cole", email: "kieran@northridge.com", priority: "Medium", createdAt: "2026-03-02" }
  ],
  searches: [
    { id: "s1", clientId: "c1", role: "VP Operations", location: "Dallas, TX", fee: 5000, targetStart: "2026-04-15", status: "Active" },
    { id: "s2", clientId: "c2", role: "Chief Estimator", location: "Denver, CO", fee: 5000, targetStart: "2026-04-22", status: "Active" }
  ],
  candidates: [
    { id: "p1", name: "Morgan Hale", roleTrack: "VP Operations", source: "LinkedIn", searchId: "s1", score: 91, stage: "Screened", updatedAt: new Date().toISOString() },
    { id: "p2", name: "Riley Chen", roleTrack: "Chief Estimator", source: "Referral", searchId: "s2", score: 88, stage: "Client Review", updatedAt: new Date().toISOString() },
    { id: "p3", name: "Jordan Pike", roleTrack: "VP Operations", source: "Database", searchId: "s1", score: 69, stage: "Sourced", updatedAt: new Date().toISOString() }
  ],
  log: [
    `${new Date().toLocaleString()}: System initialized with seed data.`
  ]
};

let state = loadState();

document.addEventListener("DOMContentLoaded", () => {
  bindViewSwitching();
  bindForms();
  bindAutomation();
  renderAutomationRules();
  renderAll();
});

function loadState() {
  try {
    const raw = localStorage.getItem(STORAGE_KEY);
    if (!raw) return structuredClone(seedState);
    const parsed = JSON.parse(raw);
    if (!parsed.clients || !parsed.searches || !parsed.candidates || !parsed.log) {
      return structuredClone(seedState);
    }
    return parsed;
  } catch {
    return structuredClone(seedState);
  }
}

function persist() {
  localStorage.setItem(STORAGE_KEY, JSON.stringify(state));
}

function renderAll() {
  renderSiteMetrics();
  renderCrmKpis();
  renderRecruitKpis();
  renderClientSelects();
  renderClientsTable();
  renderSearchesTable();
  renderPipeline();
  renderLog();
  persist();
}

function bindViewSwitching() {
  document.querySelectorAll("[data-view-target]").forEach((button) => {
    button.addEventListener("click", () => setActiveView(button.dataset.viewTarget));
  });
}

function setActiveView(viewId) {
  document.querySelectorAll(".app-view").forEach((view) => {
    view.classList.toggle("active", view.id === viewId);
  });

  document.querySelectorAll(".view-btn").forEach((btn) => {
    btn.classList.toggle("active", btn.dataset.viewTarget === viewId);
  });
}

function bindForms() {
  const clientForm = document.getElementById("clientForm");
  const searchForm = document.getElementById("searchForm");
  const candidateForm = document.getElementById("candidateForm");

  clientForm.addEventListener("submit", (event) => {
    event.preventDefault();
    const formData = new FormData(clientForm);
    const client = {
      id: createId("c"),
      company: formData.get("company").toString().trim(),
      contact: formData.get("contact").toString().trim(),
      email: formData.get("email").toString().trim(),
      priority: formData.get("priority").toString(),
      createdAt: new Date().toISOString().slice(0, 10)
    };

    state.clients.unshift(client);
    pushLog(`Client added: ${client.company} (${client.priority} priority)`);
    clientForm.reset();
    renderAll();
  });

  searchForm.addEventListener("submit", (event) => {
    event.preventDefault();
    const formData = new FormData(searchForm);
    const search = {
      id: createId("s"),
      clientId: formData.get("clientId").toString(),
      role: formData.get("role").toString().trim(),
      location: formData.get("location").toString().trim(),
      fee: Number(formData.get("fee")),
      targetStart: formData.get("targetStart").toString(),
      status: "Active"
    };

    state.searches.unshift(search);
    pushLog(`Search created: ${search.role} in ${search.location}`);
    searchForm.reset();
    renderAll();
  });

  candidateForm.addEventListener("submit", (event) => {
    event.preventDefault();
    const formData = new FormData(candidateForm);
    const candidate = {
      id: createId("p"),
      name: formData.get("name").toString().trim(),
      roleTrack: formData.get("roleTrack").toString().trim(),
      source: formData.get("source").toString(),
      searchId: formData.get("searchId").toString(),
      score: Number(formData.get("score")),
      stage: STAGES[0],
      updatedAt: new Date().toISOString()
    };

    state.candidates.unshift(candidate);
    pushLog(`Candidate added: ${candidate.name} (${candidate.score})`);
    candidateForm.reset();
    renderAll();
  });
}

function bindAutomation() {
  const button = document.getElementById("runAutomationBtn");
  button.addEventListener("click", runAutomationCycle);
}

function runAutomationCycle() {
  let updates = 0;

  state.candidates = state.candidates.map((candidate) => {
    const stageIndex = STAGES.indexOf(candidate.stage);
    if (candidate.score >= 85 && stageIndex < STAGES.length - 1) {
      updates += 1;
      const nextStage = STAGES[stageIndex + 1];
      pushLog(`Auto advanced ${candidate.name}: ${candidate.stage} -> ${nextStage}`);
      return { ...candidate, stage: nextStage, updatedAt: new Date().toISOString() };
    }

    if (candidate.score < 70 && candidate.stage === "Sourced") {
      pushLog(`Flagged ${candidate.name} for manual review (score ${candidate.score})`);
    }

    return candidate;
  });

  if (updates === 0) {
    pushLog("Automation cycle complete: no stage changes.");
  } else {
    pushLog(`Automation cycle complete: ${updates} candidate(s) advanced.`);
  }

  renderAll();
}

function renderSiteMetrics() {
  const filled = state.candidates.filter((candidate) => candidate.stage === "Offer").length;
  const totalFee = state.searches.reduce((sum, search) => sum + Number(search.fee || 0), 0);

  const metrics = [
    { label: "Active Clients", value: state.clients.length.toString() },
    { label: "Active Searches", value: state.searches.filter((s) => s.status === "Active").length.toString() },
    { label: "Candidates In Play", value: state.candidates.length.toString() },
    { label: "Projected Fees", value: `$${totalFee.toLocaleString()}` },
    { label: "Offers Ready", value: filled.toString() },
    { label: "Automation Rules", value: automationRules.length.toString() }
  ];

  renderMetrics("siteMetrics", metrics);
}

function renderCrmKpis() {
  const highPriority = state.clients.filter((client) => client.priority === "High").length;
  const avgFee = state.searches.length
    ? Math.round(state.searches.reduce((sum, search) => sum + Number(search.fee || 0), 0) / state.searches.length)
    : 0;

  const kpis = [
    { label: "Total Clients", value: state.clients.length.toString() },
    { label: "High Priority", value: highPriority.toString() },
    { label: "Open Searches", value: state.searches.filter((s) => s.status === "Active").length.toString() },
    { label: "Average Fee", value: `$${avgFee.toLocaleString()}` }
  ];

  renderMetrics("crmKpis", kpis);
}

function renderRecruitKpis() {
  const interviewCount = state.candidates.filter((candidate) => candidate.stage === "Interview").length;
  const offerCount = state.candidates.filter((candidate) => candidate.stage === "Offer").length;
  const avgScore = state.candidates.length
    ? Math.round(state.candidates.reduce((sum, c) => sum + c.score, 0) / state.candidates.length)
    : 0;

  const kpis = [
    { label: "Pipeline Size", value: state.candidates.length.toString() },
    { label: "In Interview", value: interviewCount.toString() },
    { label: "Offer Stage", value: offerCount.toString() },
    { label: "Average Score", value: `${avgScore}` }
  ];

  renderMetrics("recruitKpis", kpis);
}

function renderMetrics(targetId, items) {
  const target = document.getElementById(targetId);
  const template = document.getElementById("metricTemplate");
  target.innerHTML = "";

  items.forEach((item) => {
    const clone = template.content.cloneNode(true);
    clone.querySelector("h4").textContent = item.label;
    clone.querySelector("p").textContent = item.value;
    target.appendChild(clone);
  });
}

function renderClientSelects() {
  const clientSelect = document.getElementById("clientSelect");
  const searchSelect = document.getElementById("searchSelect");

  clientSelect.innerHTML = state.clients
    .map((client) => `<option value="${client.id}">${escapeHtml(client.company)}</option>`)
    .join("");

  searchSelect.innerHTML = state.searches
    .map((search) => {
      const client = state.clients.find((c) => c.id === search.clientId);
      const label = `${search.role} | ${client ? client.company : "Unknown"}`;
      return `<option value="${search.id}">${escapeHtml(label)}</option>`;
    })
    .join("");
}

function renderClientsTable() {
  const table = document.getElementById("clientsTable");
  table.innerHTML = state.clients
    .map((client) => `
      <tr>
        <td>${escapeHtml(client.company)}</td>
        <td>${escapeHtml(client.contact)}<br><span class="muted">${escapeHtml(client.email)}</span></td>
        <td><span class="status-chip">${escapeHtml(client.priority)}</span></td>
      </tr>
    `)
    .join("");
}

function renderSearchesTable() {
  const table = document.getElementById("searchesTable");
  table.innerHTML = state.searches
    .map((search) => {
      const client = state.clients.find((entry) => entry.id === search.clientId);
      return `
      <tr>
        <td>${escapeHtml(search.role)}</td>
        <td>${escapeHtml(client ? client.company : "Unknown")}</td>
        <td>${escapeHtml(search.location)}</td>
        <td>${escapeHtml(search.targetStart)}</td>
        <td><span class="status-chip">${escapeHtml(search.status)}</span></td>
      </tr>
    `;
    })
    .join("");
}

function renderPipeline() {
  const board = document.getElementById("pipelineBoard");
  board.innerHTML = "";

  STAGES.forEach((stage) => {
    const column = document.createElement("div");
    column.className = "pipeline-column";
    const candidates = state.candidates.filter((candidate) => candidate.stage === stage);

    column.innerHTML = `<h4>${stage} (${candidates.length})</h4>`;

    candidates.forEach((candidate) => {
      const card = document.createElement("article");
      card.className = "candidate-card";
      const currentIndex = STAGES.indexOf(candidate.stage);
      const canAdvance = currentIndex < STAGES.length - 1;
      const search = state.searches.find((entry) => entry.id === candidate.searchId);
      const client = search ? state.clients.find((entry) => entry.id === search.clientId) : null;

      card.innerHTML = `
        <strong>${escapeHtml(candidate.name)}</strong>
        <span>${escapeHtml(candidate.roleTrack)}</span><br>
        <span class="muted">${escapeHtml(candidate.source)} | Score ${candidate.score}</span><br>
        <span class="muted">${escapeHtml(client ? client.company : "Unknown Client")}</span>
      `;

      if (canAdvance) {
        const button = document.createElement("button");
        button.className = "secondary";
        button.textContent = `Move to ${STAGES[currentIndex + 1]}`;
        button.addEventListener("click", () => advanceCandidate(candidate.id));
        card.appendChild(button);
      }

      column.appendChild(card);
    });

    board.appendChild(column);
  });
}

function advanceCandidate(candidateId) {
  state.candidates = state.candidates.map((candidate) => {
    if (candidate.id !== candidateId) return candidate;

    const currentIndex = STAGES.indexOf(candidate.stage);
    if (currentIndex >= STAGES.length - 1) return candidate;

    const nextStage = STAGES[currentIndex + 1];
    pushLog(`Manual move: ${candidate.name} -> ${nextStage}`);
    return {
      ...candidate,
      stage: nextStage,
      updatedAt: new Date().toISOString()
    };
  });

  renderAll();
}

function renderAutomationRules() {
  const list = document.getElementById("automationRules");
  list.innerHTML = automationRules.map((rule) => `<li>${escapeHtml(rule)}</li>`).join("");
}

function renderLog() {
  const list = document.getElementById("automationLog");
  list.innerHTML = state.log.slice(0, 14).map((entry) => `<li>${escapeHtml(entry)}</li>`).join("");
}

function pushLog(message) {
  state.log.unshift(`${new Date().toLocaleString()}: ${message}`);
  state.log = state.log.slice(0, 120);
}

function createId(prefix) {
  const stamp = Date.now().toString(36);
  const rand = Math.random().toString(36).slice(2, 6);
  return `${prefix}_${stamp}_${rand}`;
}

function escapeHtml(value) {
  return String(value)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#39;");
}
