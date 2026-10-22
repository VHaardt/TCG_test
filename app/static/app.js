"use strict";
// Client dell'app online di CICATRICI: solo testo, nessuna dipendenza.
// Lo stato vero sta sul server; qui si tiene solo il mazzo in costruzione.

const $ = (s) => document.querySelector(s);
const esc = (t) => String(t ?? "").replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
const mdish = (t) => esc(t).replace(/\*([^*]+)\*/g, "<em>$1</em>");

let CAT = null;            // catalogo: carte, leader, regole di costruzione
let CARTA = {};            // id -> carta
let LEAD = {};             // id -> leader
let sess = null;           // {codice, token}
let stato = null;          // ultima vista del server
let chiavePrep = "", chiaveGioco = "";
let mazzo = { leader: null, carte: {} };   // mazzo in costruzione (modalità costruito)
let filtro = { testo: "", tipo: "", solo_legali: true };

async function call(path, body) {
  const opt = body ? { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify(body) } : {};
  const r = await fetch(path, opt);
  const j = await r.json().catch(() => ({ errore: "risposta non valida" }));
  if (!r.ok) throw new Error(j.errore || r.statusText);
  return j;
}

function errore(msg) {
  $("#errore").textContent = msg || "";
  if (msg) setTimeout(() => { if ($("#errore").textContent === msg) $("#errore").textContent = ""; }, 6000);
}

async function act(path, extra) {
  try {
    stato = await call(path, { ...sess, ...(extra || {}) });
    render();
  } catch (e) { errore(e.message); }
}

// ------------------------------------------------------------------ carte
function colori(cs) {
  if (!cs || !cs.length) return '<span class="col col-N">Neutrale</span>';
  return cs.map((c) => `<span class="col col-${c}">${esc(CAT.colori[c] || c)}</span>`).join(" ");
}

function cartaHTML(id, extra = "", classi = "") {
  const c = CARTA[id];
  if (!c) return `<div class="carta">${esc(id)}</div>`;
  const forza = c.forza !== null && c.forza !== undefined ? ` · Forza <b>${c.forza}</b>` : "";
  return `<div class="carta ${classi}">
    <div class="testa"><b>${esc(c.nome)}</b> <span class="costo">${c.costo}</span></div>
    <div class="attr">${esc(c.tipo)}${forza} · ${colori(c.colori)}${c.rarita ? ` · <span class="rar">${esc(c.rarita)}</span>` : ""}</div>
    <div class="testo">${mdish(c.testo)}</div>${extra}</div>`;
}

function leaderHTML(id, extra = "", stato_l = null) {
  const l = LEAD[id];
  const v = CAT.valori_leader;
  const risv = stato_l && stato_l.risvegliato;
  return `<div class="carta leader ${risv ? "risv" : ""}">
    <div class="testa"><b>${esc(l.nome)}</b> <span class="attr">${colori(l.colori)}</span></div>
    <div class="attr">Base: Forza ${v.forza}, Tempra ${v.tempra}, Vite ${v.vite}, Guardia max ${v.guardia_max} ·
      Risvegliato (a ${v.risveglio_a_vite} Vite): Forza ${v.forza_risvegliato}, Guardia max ${v.guardia_max_risvegliato}</div>
    <div class="testo ${risv ? "spento" : ""}"><b>Base.</b> ${l.base.map(mdish).join(" ")}</div>
    <div class="testo ${stato_l && !risv ? "spento" : ""}"><b>Risvegliato.</b> ${l.risvegliato.map(mdish).join(" ")}</div>${extra}</div>`;
}

// ------------------------------------------------------------------ avvio
async function avvio() {
  CAT = await call("/api/catalogo");
  CAT.carte.forEach((c) => (CARTA[c.id] = c));
  CAT.leader.forEach((l) => (LEAD[l.id] = l));
  $("#info-set").textContent = `Set ${CAT.set.version || ""} (${CAT.set.data || ""}), regole ${CAT.regole}. ` +
    `Mazzo: ${CAT.costruzione.carte} carte, max ${CAT.costruzione.copie} copie per ID, solo colori del Leader o Neutrali.`;
  $("#nome").value = localStorage.getItem("cic_nome") || "";
  const qs = new URLSearchParams(location.search);
  if (qs.get("stanza")) $("#codice").value = qs.get("stanza").toUpperCase();
  const salvata = JSON.parse(localStorage.getItem("cic_sess") || "null");
  if (salvata && (!qs.get("stanza") || qs.get("stanza").toUpperCase() === salvata.codice)) {
    try { sess = salvata; stato = await call(`/api/stato?codice=${sess.codice}&token=${sess.token}`); }
    catch { sess = null; localStorage.removeItem("cic_sess"); }
  }
  try { mazzo = JSON.parse(localStorage.getItem("cic_mazzo")) || mazzo; } catch {}
  $("#crea").onclick = crea;
  $("#entra").onclick = entra;
  render();
  setInterval(poll, 1000);
}

function nome() {
  const n = $("#nome").value.trim();
  if (!n) { errore("Scrivi il tuo nome"); return null; }
  localStorage.setItem("cic_nome", n);
  return n;
}

function entraIn(r) {
  sess = { codice: r.codice, token: r.token };
  localStorage.setItem("cic_sess", JSON.stringify(sess));
  history.replaceState(null, "", `?stanza=${r.codice}`);
  poll();
}

async function crea() {
  const n = nome(); if (!n) return;
  const modalita = document.querySelector('input[name="modalita"]:checked').value;
  const ia = document.querySelector('input[name="avv"]:checked').value === "ia";
  try { entraIn(await call("/api/stanza", { nome: n, modalita, contro_ia: ia })); } catch (e) { errore(e.message); }
}

async function entra() {
  const n = nome(); if (!n) return;
  try { entraIn(await call("/api/entra", { nome: n, codice: $("#codice").value.trim().toUpperCase() })); }
  catch (e) { errore(e.message); }
}

function esci() {
  sess = null; stato = null; chiavePrep = chiaveGioco = "";
  localStorage.removeItem("cic_sess");
  history.replaceState(null, "", location.pathname);
  render();
}

let inVolo = false;
async function poll() {
  if (!sess || inVolo || document.hidden) return;
  inVolo = true;
  try { stato = await call(`/api/stato?codice=${sess.codice}&token=${sess.token}`); render(); }
  catch (e) { if (/inesistente|sconosciuto/.test(e.message)) { errore(e.message); esci(); } }
  finally { inVolo = false; }
}

// ------------------------------------------------------------------ render
function render() {
  const inStanza = !!(sess && stato);
  $("#home").classList.toggle("nascosto", inStanza);
  $("#stanza").classList.toggle("nascosto", !inStanza);
  if (!inStanza) { $("#info-stanza").innerHTML = ""; return; }
  const link = `${location.origin}${location.pathname}?stanza=${stato.codice}`;
  const gioc = stato.giocatori.map((g, i) => `${esc(g.nome)}${i === stato.io ? " (tu)" : ""}${g.pronto ? " ✓" : ""}`).join(" · ");
  $("#info-stanza").innerHTML = `Stanza <b>${stato.codice}</b> · ${stato.modalita === "draft" ? "Draft" : "Costruito"} · ${gioc}
    ${stato.giocatori.length < 2 ? ` · invita: <input readonly value="${esc(link)}" onclick="this.select()" size="30">` : ""}
    <button class="piccolo" id="esci">Esci</button>`;
  $("#esci").onclick = esci;

  if (stato.fase === "partita") {
    $("#prep").innerHTML = ""; chiavePrep = "";
    renderGioco();
  } else {
    $("#gioco").innerHTML = ""; chiaveGioco = "";
    renderPrep();
  }
}

function renderPrep() {
  const io = stato.giocatori[stato.io];
  const d = stato.draft;
  const chiave = JSON.stringify([stato.modalita, io.pronto, d && [d.leader, d.scelte], stato.n_partita, stato.giocatori.length]);
  if (chiave === chiavePrep) return;
  chiavePrep = chiave;
  if (io.pronto) {
    const altro = stato.giocatori.length < 2 ? "Aspetto che entri il secondo giocatore." : "Aspetto l'avversario.";
    $("#prep").innerHTML = `<div class="pannello"><h2>Pronto</h2><p>${altro} La partita inizia da sola quando siete pronti entrambi.</p>
      ${stato.modalita === "costruito" ? '<button id="annulla">Modifica il mazzo</button>' : ""}</div>`;
    if ($("#annulla")) $("#annulla").onclick = () => act("/api/mazzo/annulla");
    return;
  }
  if (stato.modalita === "draft") renderDraft(d); else renderCostruttore();
}

// ------------------------------------------------------------------ draft
function renderDraft(d) {
  if (!d.leader) {
    $("#prep").innerHTML = `<h2>Draft: scegli il tuo Leader</h2>
      <p class="nota">Il Leader decide i colori: le carte offerte dopo saranno solo dei suoi colori o Neutrali.</p>
      <div class="griglia">${d.leader_offerta.map((id) =>
        leaderHTML(id, `<button data-l="${id}">Scegli ${esc(id)}</button>`)).join("")}</div>`;
    $("#prep").querySelectorAll("[data-l]").forEach((b) => (b.onclick = () => act("/api/draft/leader", { leader: b.dataset.l })));
    return;
  }
  $("#prep").innerHTML = `<h2>Draft: scelta ${d.scelte + 1} di ${d.totale}</h2>
    <div class="griglia">${d.offerta.map((id) =>
      cartaHTML(id, `<div class="copie">ne hai ${d.carte[id] || 0}</div><button data-c="${id}">Prendi ${esc(id)}</button>`)).join("")}</div>
    <div class="colonne">
      <div>${leaderHTML(d.leader)}</div>
      <div class="pannello"><h3>Il tuo mazzo (${d.scelte}/${d.totale})</h3>${listaMazzo(d.carte)}</div>
    </div>`;
  $("#prep").querySelectorAll("[data-c]").forEach((b) => (b.onclick = () => act("/api/draft/scelta", { carta: b.dataset.c })));
}

function listaMazzo(carte, conBottoni = false) {
  const ids = Object.keys(carte).filter((id) => carte[id] > 0)
    .sort((a, b) => (CARTA[a].costo - CARTA[b].costo) || a.localeCompare(b));
  if (!ids.length) return '<p class="nota">vuoto</p>';
  return `<table class="lista">${ids.map((id) => {
    const c = CARTA[id];
    return `<tr><td>${carte[id]}×</td><td><b>${esc(id)}</b></td><td>${c.costo}</td><td>${esc(c.tipo)}${c.forza != null ? " " + c.forza : ""}</td>
      ${conBottoni ? `<td><button class="piccolo" data-meno="${id}">−</button></td>` : ""}</tr>`;
  }).join("")}</table>`;
}

// ------------------------------------------------------------------ costruito
function legale(id) {
  const c = CARTA[id];
  if (!mazzo.leader) return true;
  return !c.colori.length || c.colori.some((x) => LEAD[mazzo.leader].colori.includes(x));
}

function problemi() {
  const out = [];
  if (!mazzo.leader) out.push("scegli un Leader");
  const n = Object.values(mazzo.carte).reduce((a, b) => a + b, 0);
  if (n !== CAT.costruzione.carte) out.push(`${n} carte su ${CAT.costruzione.carte}`);
  for (const [id, k] of Object.entries(mazzo.carte)) {
    if (k > CAT.costruzione.copie) out.push(`${id}: ${k} copie`);
    if (mazzo.leader && k > 0 && !legale(id)) out.push(`${id}: colore fuori dal Leader`);
  }
  return out;
}

function salvaMazzo() { localStorage.setItem("cic_mazzo", JSON.stringify(mazzo)); }

function renderCostruttore() {
  const tipi = [...new Set(CAT.carte.map((c) => c.tipo))];
  $("#prep").innerHTML = `<h2>Costruisci il mazzo</h2>
    <div class="colonne">
      <div>
        <div class="pannello riga">
          <label>Leader <select id="leader"><option value="">—</option>${CAT.leader.map((l) =>
            `<option value="${l.id}" ${l.id === mazzo.leader ? "selected" : ""}>${esc(l.id)} (${l.colori.map((c) => CAT.colori[c]).join("/")})</option>`).join("")}</select></label>
          <label>Parti da un mazzo di riferimento <select id="rif"><option value="">—</option>${CAT.mazzi.map((m, i) =>
            `<option value="${i}">${esc(m.nome)}</option>`).join("")}</select></label>
        </div>
        <div id="leader-box">${mazzo.leader ? leaderHTML(mazzo.leader) : ""}</div>
        <div class="pannello riga">
          <input id="f-testo" placeholder="cerca ID o testo" value="${esc(filtro.testo)}">
          <select id="f-tipo"><option value="">tutti i tipi</option>${tipi.map((t) => `<option ${t === filtro.tipo ? "selected" : ""}>${esc(t)}</option>`).join("")}</select>
          <label><input type="checkbox" id="f-legali" ${filtro.solo_legali ? "checked" : ""}> solo carte giocabili col Leader</label>
        </div>
        <div id="pool" class="griglia"></div>
      </div>
      <div class="pannello laterale">
        <h3>Mazzo <span id="conta"></span></h3>
        <div id="problemi"></div>
        <button id="pronto">Pronto con questo mazzo</button>
        <div id="lista"></div>
        <details><summary>Esporta / importa</summary>
          <textarea id="codice-mazzo" rows="4" placeholder='{"leader": "LDR-01", "carte": {"ROS-001": 3}}'></textarea>
          <button class="piccolo" id="esporta">Esporta</button> <button class="piccolo" id="importa">Importa</button>
          <button class="piccolo" id="svuota">Svuota</button>
        </details>
      </div>
    </div>`;
  $("#leader").onchange = (e) => { mazzo.leader = e.target.value || null; salvaMazzo(); chiavePrep = ""; renderPrep(); };
  $("#rif").onchange = (e) => {
    const m = CAT.mazzi[+e.target.value]; if (!m) return;
    mazzo = { leader: m.leader, carte: { ...m.carte } }; salvaMazzo(); chiavePrep = ""; renderPrep();
  };
  $("#f-testo").oninput = (e) => { filtro.testo = e.target.value; renderPool(); };
  $("#f-tipo").onchange = (e) => { filtro.tipo = e.target.value; renderPool(); };
  $("#f-legali").onchange = (e) => { filtro.solo_legali = e.target.checked; renderPool(); };
  $("#pronto").onclick = () => act("/api/mazzo", { leader: mazzo.leader, carte: mazzo.carte });
  $("#esporta").onclick = () => ($("#codice-mazzo").value = JSON.stringify(mazzo));
  $("#importa").onclick = () => {
    try {
      const m = JSON.parse($("#codice-mazzo").value);
      if (!m.leader || !m.carte) throw new Error();
      mazzo = { leader: m.leader, carte: m.carte }; salvaMazzo(); chiavePrep = ""; renderPrep();
    } catch { errore("Codice del mazzo non valido"); }
  };
  $("#svuota").onclick = () => { mazzo.carte = {}; salvaMazzo(); renderPool(); renderLista(); };
  renderPool(); renderLista();
}

function cambia(id, d) {
  const k = Math.max(0, (mazzo.carte[id] || 0) + d);
  if (k > CAT.costruzione.copie) return;
  if (k) mazzo.carte[id] = k; else delete mazzo.carte[id];
  salvaMazzo(); renderLista();
  const el = document.querySelector(`[data-copie="${id}"]`); if (el) el.textContent = k;
}

function renderPool() {
  const t = filtro.testo.toLowerCase();
  const ids = CAT.carte.filter((c) => (!filtro.tipo || c.tipo === filtro.tipo)
    && (!t || c.id.toLowerCase().includes(t) || c.testo.toLowerCase().includes(t) || c.parole.join(" ").includes(t))
    && (!filtro.solo_legali || legale(c.id))).map((c) => c.id);
  $("#pool").innerHTML = ids.map((id) => cartaHTML(id,
    `<div class="riga"><button class="piccolo" data-d="-1" data-id="${id}">−</button>
     <b data-copie="${id}">${mazzo.carte[id] || 0}</b>
     <button class="piccolo" data-d="1" data-id="${id}">+</button></div>`, legale(id) ? "" : "illegale")).join("");
  $("#pool").querySelectorAll("[data-d]").forEach((b) => (b.onclick = () => cambia(b.dataset.id, +b.dataset.d)));
}

function renderLista() {
  const n = Object.values(mazzo.carte).reduce((a, b) => a + b, 0);
  $("#conta").textContent = `${n}/${CAT.costruzione.carte}`;
  const pr = problemi();
  $("#problemi").innerHTML = pr.length ? `<ul class="problemi">${pr.map((p) => `<li>${esc(p)}</li>`).join("")}</ul>` : '<p class="ok">Mazzo legale</p>';
  $("#pronto").disabled = pr.length > 0;
  $("#lista").innerHTML = listaMazzo(mazzo.carte, true);
  $("#lista").querySelectorAll("[data-meno]").forEach((b) => (b.onclick = () => { cambia(b.dataset.meno, -1); }));
}

// ------------------------------------------------------------------ partita
function renderGioco() {
  const p = stato.partita;
  const chiave = String(p.versione) + (p.fine ? "f" : "");
  if (chiave === chiaveGioco) return;
  chiaveGioco = chiave;
  const n = p.nomi;
  let cent = `<div class="pannello centro">
    <div><b>Round ${p.round}</b> · turno di <b>${p.attivo_sei_tu ? esc(n.io) : esc(n.avversario)}</b> · ${esc(p.fase_testo)}
      · tu sei ${p.sei} · Saldo ${p.regole.saldo} · Crepuscolo al round ${p.regole.crepuscolo}</div>`;
  if (p.combattimento) {
    const c = p.combattimento;
    cent += `<div class="scontro">Scontro: <b>${esc(c.attaccante)}</b> attacca → bersaglio <b>${esc(c.bersaglio)}</b>
      ${c.opposta_da ? ` · si oppone <b>${esc(c.opposta_da)}</b>` : ""}
      ${c.gemme_attacco != null ? ` · gemme d'attacco <b>${c.gemme_attacco}</b>` : ""}</div>`;
  }
  if (p.fine) {
    cent += `<div class="fine ${p.fine.hai_vinto ? "vinto" : "perso"}">${p.fine.hai_vinto ? "Hai vinto" : "Hai perso"}
      (${esc(p.fine.motivo)}${p.fine.vincitore ? ", vince " + esc(p.fine.vincitore) : ""}).
      <button id="rivincita">Nuova partita nella stessa stanza</button></div>`;
  } else if (p.tocca_a_te) {
    const gruppi = {};
    p.azioni.forEach((a) => (gruppi[a.gruppo] = gruppi[a.gruppo] || []).push(a));
    const nomiG = { turno: "Turno", gioca: "Gioca una carta", attacca: "Attacca", abilita: "Abilità ⟳", rimargina: "Rimargina",
      gemme: "Gemme d'attacco", opposizione: "Opposizione", parata: "Guardia", altro: "Altro" };
    cent += `<div class="azioni"><b>Tocca a te.</b>${Object.entries(gruppi).map(([g, as]) =>
      `<div class="gruppo"><span>${nomiG[g] || g}</span>${as.map((a) =>
        `<button data-i="${a.i}" ${a.carta ? `title="${esc(CARTA[a.carta]?.testo || "")}"` : ""}>${esc(a.testo)}</button>`).join("")}</div>`).join("")}</div>`;
  } else {
    cent += `<div class="attesa">Decide ${esc(p.decide)}…</div>`;
  }
  if (!p.fine) cent += `<button class="piccolo" id="resa">Arrenditi</button>`;
  cent += "</div>";

  $("#gioco").innerHTML = `<div class="tavolo">
    <div class="campo">${lato(p.avversario, n.avversario, false)}${cent}${lato(p.io, n.io, true)}</div>
    <div class="pannello registro"><h3>Registro</h3><pre>${p.log.map(esc).join("\n")}</pre></div></div>`;
  $("#gioco").querySelectorAll("[data-i]").forEach((b) => (b.onclick = () => {
    $("#gioco").querySelectorAll("[data-i]").forEach((x) => (x.disabled = true));
    act("/api/azione", { versione: p.versione, indice: +b.dataset.i });
  }));
  if ($("#rivincita")) $("#rivincita").onclick = () => act("/api/rivincita");
  if ($("#resa")) $("#resa").onclick = () => { if (confirm("Vuoi davvero arrenderti?")) act("/api/resa"); };
  const pre = $("#gioco pre"); if (pre) pre.scrollTop = pre.scrollHeight;
}

function lato(g, nome, mio) {
  const L = g.leader;
  const stato_l = `${L.pronto ? "Pronto" : "Ruotato"}${L.risvegliato ? " · Risvegliato" : ""} · Forza ${L.forza} · Tempra ${L.tempra}`;
  const cic = g.cicatrici.length ? g.cicatrici.map((s) => `<span class="cic ${s.fresca ? "fresca" : ""}" title="${esc(CARTA[s.id]?.testo || "")}">${esc(s.id)}${s.fresca ? " (fresca)" : ""}</span>`).join(" ") : "nessuna";
  const unita = g.unita.length ? g.unita.map((u) => cartaHTML(u.id,
    `<div class="stato-u">#${u.uid} · ${u.pronta ? "Pronta" : "Ruotata"} · Forza ora ${u.forza}</div>`, u.pronta ? "" : "ruotata")).join("") : '<p class="nota">nessuna Unità</p>';
  const rel = g.reliquie.map((id) => cartaHTML(id)).join("");
  return `<div class="lato ${mio ? "mio" : "suo"}">
    <h3>${esc(nome)}${mio ? " (tu)" : ""} ${g.alle_corde ? '<span class="corde">Alle Corde</span>' : ""}</h3>
    <div class="numeri">Vite <b>${g.vite}</b> · Brace <b>${g.brace}</b> · Guardia <b>${g.guardia}</b>/${g.guardia_max}
      · Mano ${g.mano_n} · Mazzo ${g.mazzo} · Scarti ${g.scarti.length}</div>
    <div class="riga-campo">
      <div class="leader-col">${leaderHTML(L.id, `<div class="stato-u">${stato_l}</div>`, L)}</div>
      <div><div class="griglia">${unita}${rel}</div>
        <div class="nota">Cicatrici: ${cic}</div>
        ${g.scarti.length ? `<details class="nota"><summary>Scarti</summary>${g.scarti.map(esc).join(", ")}</details>` : ""}</div>
    </div>
    ${mio ? `<h4>La tua mano</h4><div class="griglia mano">${g.mano.map((id) => cartaHTML(id)).join("") || '<p class="nota">vuota</p>'}</div>` : ""}
  </div>`;
}

avvio().catch((e) => errore("Impossibile caricare il catalogo: " + e.message));
