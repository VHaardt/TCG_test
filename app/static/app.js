"use strict";
// Client dell'app online di CICATRICI: tavolo grafico senza dipendenze.
// Lo stato vero sta sul server; il client disegna, anima le differenze fra due stati
// e trasforma i clic sulle carte in una delle azioni legali che il server elenca.

const $ = (s, el = document) => el.querySelector(s);
const $$ = (s, el = document) => [...el.querySelectorAll(s)];
const esc = (t) => String(t ?? "").replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
const mdish = (t) => esc(t).replace(/\*([^*]+)\*/g, "<em>$1</em>");
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

let CAT = null, CARTA = {}, LEAD = {};
let sess = null, stato = null;
let chiavePrep = "", chiaveGioco = "";
let mazzo = { leader: null, carte: {} };
let filtro = { testo: "", tipo: "", solo_legali: true };
let prec = null;            // vista precedente della partita, per le animazioni
let mira = null;            // modalità bersaglio: {titolo, opts: [azione con bersaglio]}

const ICONA = { "Unità": "⚔", "Tattica": "✦", "Reazione": "⛨", "Reliquia": "◈" };
const KW = { scudo: "🛡", assalto: "⚡", impeto: "🔥", furia: "💢", caccia: "🎯", bracconiere: "🏹", rinnovo: "♻" };
const ICONA_LEADER = ["♛", "♜", "☠", "❖", "⚜", "✠", "♞", "☬"];

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
  try { stato = await call(path, { ...sess, ...(extra || {}) }); render(); } catch (e) { errore(e.message); }
}

// ------------------------------------------------------------------ disegno di carte e Leader
function colVars(cs) {
  const c = cs && cs.length ? cs : ["N"];
  return `--c1:var(--${c[0]});--c2:var(--${c[1] || c[0]})`;
}

function cartaHTML(id, { classi = "", attr = "", stile = "" } = {}) {
  const c = CARTA[id];
  if (!c) return `<div class="carta ${classi}" ${attr}><div class="c-dentro">${esc(id)}</div></div>`;
  const num = (id.match(/\d+/) || [""])[0];
  return `<div class="carta ${classi}" style="${colVars(c.colori)};${stile}" data-card="${id}" ${attr}>
    <div class="c-costo">${c.costo}</div>
    <div class="c-dentro">
      <div class="c-arte"><span class="icona">${ICONA[c.tipo] || "✧"}</span><span class="num">${num}</span></div>
      <div class="c-nome">${esc(c.nome)}</div>
      <div class="c-tipo">${esc(c.tipo)} · ${c.colori.length ? c.colori.map((x) => CAT.colori[x]).join("/") : "Neutrale"}</div>
      <div class="c-testo">${mdish(c.testo) || "<em>Nessun effetto.</em>"}</div>
    </div>
    ${c.rarita ? `<span class="c-rar ${c.rarita}" title="rarità ${c.rarita}"></span>` : ""}
    ${c.forza != null ? `<div class="c-forza"><b>${c.forza}</b></div>` : ""}</div>`;
}

function retroHTML(classi = "") {
  return `<div class="carta retro ${classi}"><div class="c-dentro">✦</div></div>`;
}

function iconaLeader(id) {
  const n = parseInt((id.match(/\d+/) || ["0"])[0], 10);
  return ICONA_LEADER[n % ICONA_LEADER.length];
}

function eroeHTML(id, L, ent) {
  const l = LEAD[id];
  const v = CAT.valori_leader;
  const forza = L ? L.forza : v.forza, tempra = L ? L.tempra : v.tempra;
  const cl = L ? `${L.risvegliato ? "risv" : ""} ${L.pronto ? "" : "ruotato"}` : "";
  return `<div class="eroe ${cl}" style="${colVars(l.colori)}" ${ent ? `data-ent="${ent}"` : ""} data-leader="${id}">
    ${L && (!L.pronto || L.risvegliato) ? `<span class="stato">${[L.risvegliato ? "🔥 Risvegliato" : "", L.pronto ? "" : "⟳ Ruotato"].filter(Boolean).join(" · ")}</span>` : ""}
    <div class="e-ritratto"><span class="icona">${iconaLeader(id)}</span><span class="nome">${esc(l.nome)}</span></div>
    <div class="e-forza" title="Forza">${forza}</div><div class="e-tempra" title="Tempra">${tempra}</div></div>`;
}

function leaderTesti(id, risv = null) {
  const l = LEAD[id];
  return `<div class="testi"><div style="${risv === true ? "opacity:.45" : ""}"><b>Base.</b> ${l.base.map(mdish).join(" ")}</div>
    <div style="${risv === false ? "opacity:.45" : ""}"><b>Risvegliato.</b> ${l.risvegliato.map(mdish).join(" ")}</div></div>`;
}

// modificatori dal vivo di un'Unità in campo, sotto l'anteprima
function modHTML(el) {
  if (!el.dataset.mod) return "";
  const mod = JSON.parse(el.dataset.mod), c = CARTA[el.dataset.card];
  return `<div class="pannello mod-box"><b>Forza ${c.forza}</b> stampata${mod.map((m) =>
    `<div class="${m.scontro ? "cond" : m.v > 0 ? "su" : "giu"}">${m.v > 0 ? "+" : ""}${m.v} ${m.fonte === "altro" ? "altri effetti" : m.fonte === el.dataset.card ? "propria abilità" : `da ${esc(m.fonte)}`}${m.scontro ? " (solo negli scontri, già attivo)" : ""}</div>`).join("")}</div>`;
}

// anteprima ingrandita al passaggio del mouse
function anteprima(e) {
  const el = e.target.closest("[data-card],[data-leader]");
  const box = $("#anteprima");
  if (!el || el.closest("#anteprima") || el.closest(".offerta")) { box.style.opacity = 0; return; }
  if (el.dataset.card) box.innerHTML = cartaHTML(el.dataset.card, { classi: "grande" }) + modHTML(el);
  else box.innerHTML = `<div class="pannello" style="width:280px">${eroeHTML(el.dataset.leader)}<h3>${esc(el.dataset.leader)}</h3>${leaderTesti(el.dataset.leader)}</div>`;
  const r = el.getBoundingClientRect();
  const w = 240, h = 340;
  let x = r.right + 14; if (x + w > innerWidth) x = r.left - w - 14;
  let y = Math.min(Math.max(8, r.top + r.height / 2 - h / 2), innerHeight - h - 8);
  box.style.left = Math.max(8, x) + "px"; box.style.top = y + "px"; box.style.opacity = 1;
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
  document.addEventListener("mouseover", anteprima);
  document.addEventListener("keydown", (e) => { if (e.key === "Escape") { chiudiMenu(); annullaMira(); } });
  document.addEventListener("click", (e) => { if (!e.target.closest("#menu") && !e.target.closest("[data-ent],[data-mano],[data-scar]")) chiudiMenu(); });
  addEventListener("resize", disegnaFreccia);
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
  const modalita = $('input[name="modalita"]:checked').value;
  const ia = $('input[name="avv"]:checked').value === "ia";
  try { entraIn(await call("/api/stanza", { nome: n, modalita, contro_ia: ia })); } catch (e) { errore(e.message); }
}

async function entra() {
  const n = nome(); if (!n) return;
  try { entraIn(await call("/api/entra", { nome: n, codice: $("#codice").value.trim().toUpperCase() })); }
  catch (e) { errore(e.message); }
}

function esci() {
  sess = null; stato = null; prec = null; chiavePrep = chiaveGioco = "";
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
  if (!inStanza) { $("#info-stanza").innerHTML = ""; $("#gioco").innerHTML = ""; return; }
  const link = `${location.origin}${location.pathname}?stanza=${stato.codice}`;
  const gioc = stato.giocatori.map((g, i) => `${esc(g.nome)}${i === stato.io ? " (tu)" : ""}${g.pronto ? " ✓" : ""}`).join(" · ");
  $("#info-stanza").innerHTML = `Stanza <b>${stato.codice}</b> · ${{ draft: "Draft", pronti: "Mazzi pronti" }[stato.modalita] || "Costruito"} · ${gioc}
    ${stato.giocatori.length < 2 ? ` · invita: <input readonly value="${esc(link)}" onclick="this.select()" size="30">` : ""}
    <button class="piccolo" id="esci">Esci</button>`;
  $("#esci").onclick = esci;
  if (stato.fase === "partita") {
    $("#prep").innerHTML = ""; chiavePrep = "";
    if (stato.partita.mulligan) renderMulligan(); else renderGioco();
  } else {
    $("#gioco").innerHTML = ""; chiaveGioco = ""; prec = null;
    $("#strato svg").innerHTML = "";
    const fp = $("#fine-partita"); if (fp) fp.remove();
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
    $("#prep").innerHTML = `<div class="pannello" style="text-align:center"><h2>Pronto!</h2><p>${altro} La partita inizia da sola quando siete pronti entrambi.</p>
      ${stato.modalita !== "draft" ? `<button class="piccolo" id="annulla">${stato.modalita === "pronti" ? "Cambia mazzo" : "Modifica il mazzo"}</button>` : ""}</div>`;
    if ($("#annulla")) $("#annulla").onclick = () => act("/api/mazzo/annulla");
    return;
  }
  if (stato.modalita === "draft") renderDraft(d);
  else if (stato.modalita === "pronti") renderPronti();
  else renderCostruttore();
}

// ------------------------------------------------------------------ mazzi pronti
function renderPronti() {
  $("#prep").innerHTML = `<h2 style="text-align:center">Scegli un mazzo pronto</h2>
    <p class="nota" style="text-align:center">Sono i mazzi di riferimento del set, già legali. Apri «Carte» per vedere la lista.</p>
    <div class="mazzi-pronti">${CAT.mazzi.map((m, i) => {
      const L = LEAD[m.leader], n = Object.values(m.carte).reduce((a, b) => a + b, 0);
      return `<div class="pannello pronto-mazzo" style="${colVars(L.colori)}">
        <div class="riga">${eroeHTML(m.leader)}<div><h3>${esc(m.nome.replace(/^(rif|mix)_/, "").replace(/_/g, " "))}</h3>
          <p class="nota">${esc(m.leader)} · ${L.colori.map((c) => CAT.colori[c]).join("/")} · ${n} carte</p></div></div>
        <p>${esc(m.note || "")}</p>
        <details><summary>Carte</summary>${listaMazzo(m.carte)}</details>
        <button class="oro" data-pm="${i}">Gioca con questo mazzo</button></div>`;
    }).join("")}</div>`;
  $$("[data-pm]", $("#prep")).forEach((b) => (b.onclick = () => act("/api/mazzo/pronto", { nome: CAT.mazzi[+b.dataset.pm].nome })));
}

// ------------------------------------------------------------------ draft
function renderDraft(d) {
  if (!d.leader) {
    $("#prep").innerHTML = `<h2 style="text-align:center">Draft: scegli il tuo Leader</h2>
      <p class="nota" style="text-align:center">Il Leader decide i colori: dopo ti verranno offerte solo carte dei suoi colori o Neutrali.</p>
      <div class="offerta">${d.leader_offerta.map((id) => `<div class="slot leader-scelta pannello">
        ${eroeHTML(id)}<h3>${esc(id)} · ${LEAD[id].colori.map((c) => CAT.colori[c]).join("/")}</h3>${leaderTesti(id)}
        <button class="oro" data-l="${id}">Scegli</button></div>`).join("")}</div>`;
    $$("[data-l]", $("#prep")).forEach((b) => (b.onclick = () => act("/api/draft/leader", { leader: b.dataset.l })));
    return;
  }
  $("#prep").innerHTML = `<div class="colonne"><div>
      <h2 style="text-align:center">Scelta ${d.scelte + 1} di ${d.totale}: prendi una carta</h2>
      <div class="barra-draft"><div style="width:${(100 * d.scelte) / d.totale}%"></div></div>
      <div class="offerta">${d.offerta.map((id) => `<div class="slot">
        ${cartaHTML(id, { classi: "grande", attr: `data-c="${id}"` })}<span class="nota">ne hai ${d.carte[id] || 0}</span></div>`).join("")}</div>
    </div>
    <div class="pannello laterale"><div style="display:flex;gap:10px;align-items:center">${eroeHTML(d.leader)}<div><h3>${esc(d.leader)}</h3></div></div>
      <h3>Il tuo mazzo (${d.scelte}/${d.totale})</h3>${listaMazzo(d.carte)}</div></div>`;
  $$("[data-c]", $("#prep")).forEach((b) => (b.onclick = () => {
    b.style.transition = "transform .3s, opacity .3s"; b.style.transform = "translateY(-60px) scale(.6)"; b.style.opacity = 0;
    act("/api/draft/scelta", { carta: b.dataset.c });
  }));
}

function listaMazzo(carte, conBottoni = false) {
  const ids = Object.keys(carte).filter((id) => carte[id] > 0)
    .sort((a, b) => (CARTA[a].costo - CARTA[b].costo) || a.localeCompare(b));
  if (!ids.length) return '<p class="nota">vuoto</p>';
  return `<table class="lista">${ids.map((id) => {
    const c = CARTA[id];
    return `<tr data-card="${id}"><td><span class="pallino" style="${colVars(c.colori)}"></span></td><td>${carte[id]}×</td><td><b>${esc(id)}</b></td>
      <td>${c.costo}◆</td><td>${ICONA[c.tipo] || ""} ${c.forza != null ? c.forza : ""}</td>
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
    if (!CARTA[id]) { out.push(`${id}: carta sconosciuta`); continue; }
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
        ${mazzo.leader ? `<div class="pannello riga">${eroeHTML(mazzo.leader)}<div style="flex:1;min-width:220px"><h3>${esc(mazzo.leader)}</h3>${leaderTesti(mazzo.leader)}</div></div>` : ""}
        <div class="pannello riga">
          <input id="f-testo" placeholder="cerca ID, testo o parola chiave" value="${esc(filtro.testo)}">
          <select id="f-tipo"><option value="">tutti i tipi</option>${tipi.map((t) => `<option ${t === filtro.tipo ? "selected" : ""}>${esc(t)}</option>`).join("")}</select>
          <label><input type="checkbox" id="f-legali" ${filtro.solo_legali ? "checked" : ""}> solo carte giocabili col Leader</label>
        </div>
        <div id="pool" class="griglia"></div>
      </div>
      <div class="pannello laterale">
        <h3>Mazzo <span id="conta"></span></h3>
        <div id="problemi"></div>
        <button class="oro" id="pronto">Pronto con questo mazzo</button>
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
  const el = $(`[data-copie="${id}"]`); if (el) el.textContent = k;
}

function renderPool() {
  const t = filtro.testo.toLowerCase();
  const ids = CAT.carte.filter((c) => (!filtro.tipo || c.tipo === filtro.tipo)
    && (!t || c.id.toLowerCase().includes(t) || c.testo.toLowerCase().includes(t) || c.parole.join(" ").includes(t))
    && (!filtro.solo_legali || legale(c.id))).map((c) => c.id);
  $("#pool").innerHTML = ids.map((id) => `<div class="slot">${cartaHTML(id, { classi: legale(id) ? "" : "illegale" })}
    <div class="contatore"><button class="piccolo" data-d="-1" data-id="${id}">−</button><b data-copie="${id}">${mazzo.carte[id] || 0}</b>
    <button class="piccolo" data-d="1" data-id="${id}">+</button></div></div>`).join("");
  $$("[data-d]", $("#pool")).forEach((b) => (b.onclick = () => cambia(b.dataset.id, +b.dataset.d)));
}

function renderLista() {
  const n = Object.values(mazzo.carte).reduce((a, b) => a + b, 0);
  $("#conta").textContent = `${n}/${CAT.costruzione.carte}`;
  const pr = problemi();
  $("#problemi").innerHTML = pr.length ? `<ul class="problemi">${pr.map((p) => `<li>${esc(p)}</li>`).join("")}</ul>` : '<p class="ok">Mazzo legale</p>';
  $("#pronto").disabled = pr.length > 0;
  $("#lista").innerHTML = listaMazzo(mazzo.carte, true);
  $$("[data-meno]", $("#lista")).forEach((b) => (b.onclick = () => cambia(b.dataset.meno, -1)));
}

// ------------------------------------------------------------------ partita: intenzioni
// Ogni elemento cliccabile del tavolo (carta in mano, Unità, Leader, Cicatrice) raccoglie
// le azioni legali che lo riguardano; un'azione con bersaglio apre la modalità bersaglio.
function chiaveAzione(a) {
  if (a.gruppo === "gioca") return `mano:${a.carta}`;
  if (a.gruppo === "rimargina") return `scar:${a.carta}`;
  if (a.sorgente != null) return `io:${a.sorgente}`;
  return null;
}

function intenzioni(azioni) {
  const out = {};
  for (const a of azioni) {
    const k = chiaveAzione(a);
    if (!k) continue;
    const sub = a.gruppo === "abilita" ? `abilita:${a.testo.split("→")[0]}` : a.gruppo;
    out[k] = out[k] || {};
    const titolo = { gioca: "Gioca", attacca: "Attacca", rimargina: "Rimargina (torna in mano)", opposizione: "Opponi questa Unità" }[a.gruppo]
      || a.testo.split("→")[0].trim();
    (out[k][sub] = out[k][sub] || { titolo, opts: [] }).opts.push(a);
  }
  return out;
}

function eseguiSub(sub) {
  chiudiMenu();
  if (sub.opts.length === 1 && !sub.opts[0].bersaglio) return manda(sub.opts[0]);
  if (sub.opts.length === 1 && sub.opts[0].bersaglio && sub.opts[0].bersaglio.uid === "L" && sub.titolo === "Attacca")
    return manda(sub.opts[0]);
  mira = sub;
  disegnaMira();
}

function disegnaMira() {
  $$(".bersagliabile").forEach((x) => x.classList.remove("bersagliabile"));
  const b = $("#mira-info");
  if (!mira) { if (b) b.classList.add("nascosto"); return; }
  for (const o of mira.opts) {
    if (!o.bersaglio) continue;
    const el = $(`[data-ent="${o.bersaglio.lato}:${o.bersaglio.uid}"]`);
    if (el) el.classList.add("bersagliabile");
  }
  if (b) { b.classList.remove("nascosto"); $("span", b).textContent = `${mira.titolo}: scegli il bersaglio`; }
}

function annullaMira() { if (mira && mira.obbligo) return; mira = null; disegnaMira(); }

function manda(a) {
  mira = null;
  chiudiMenu();
  $$(".giocabile").forEach((x) => x.classList.remove("giocabile"));
  act("/api/azione", { versione: stato.partita.versione, indice: a.i });
}

function chiudiMenu() { const m = $("#menu"); if (m) m.remove(); }

function apriMenu(el, voci) {
  chiudiMenu();
  const m = document.createElement("div");
  m.id = "menu";
  voci.forEach((v) => {
    const b = document.createElement("button");
    b.textContent = v.titolo + (v.opts.length > 1 && v.opts.some((o) => o.bersaglio) ? " …" : "");
    b.onclick = (e) => { e.stopPropagation(); eseguiSub(v); };
    m.appendChild(b);
  });
  document.body.appendChild(m);
  const r = el.getBoundingClientRect();
  m.style.left = Math.min(innerWidth - m.offsetWidth - 8, r.left) + "px";
  m.style.top = Math.max(8, r.top - m.offsetHeight - 6) + "px";
}

function clicEntita(e) {
  const el = e.currentTarget;
  e.stopPropagation();
  const key = el.dataset.ent || (el.dataset.mano ? `mano:${el.dataset.mano}` : `scar:${el.dataset.scar}`);
  if (mira) {
    const o = mira.opts.find((x) => x.bersaglio && `${x.bersaglio.lato}:${x.bersaglio.uid}` === key);
    if (o && o.trigger) return act("/api/bersaglio", { versione: stato.partita.versione, uid: o.bersaglio.uid });
    if (o) return manda(o);
    if (mira.obbligo) return;
    return annullaMira();
  }
  const subs = Object.values(intenzioni(stato.partita.azioni)[key] || {});
  if (!subs.length) return;
  if (subs.length === 1) return eseguiSub(subs[0]);
  apriMenu(el, subs);
}

// ------------------------------------------------------------------ partita: disegno
function unitaHTML(u, lato, extraCl = "") {
  const c = CARTA[u.id];
  const kw = c.parole.map((k) => KW[k] || "").join("");
  const delta = u.forza > u.forza_stampata ? "su" : u.forza < u.forza_stampata ? "giu" : "";
  const mod = u.mod || [], inScontro = mod.filter((m) => m.scontro).reduce((a, m) => a + m.v, 0);
  return `<div class="unita ${u.pronta ? "" : "ruotata"} ${c.parole.includes("scudo") ? "scudo" : ""} ${extraCl}" style="${colVars(c.colori)}"
      data-ent="${lato}:${u.uid}" data-card="${u.id}" data-uid="${lato}:${u.uid}" ${mod.length ? `data-mod="${esc(JSON.stringify(mod))}"` : ""}>
    <div class="u-dentro"><span class="u-kw">${kw}</span><span class="icona">${ICONA[c.tipo]}</span><span class="u-nome">${esc(u.id)}</span></div>
    ${mod.length ? `<div class="u-mod">${mod.map((m) => `<span class="${m.scontro ? "cond" : m.v > 0 ? "su" : "giu"}">${m.v > 0 ? "+" : ""}${m.v}</span>`).join("")}</div>` : ""}
    <div class="u-forza ${delta}"><b>${u.forza}</b>${inScontro ? `<small>+${inScontro}⚔</small>` : ""}</div></div>`;
}

function reliquiaHTML(id, k) {
  const c = CARTA[id];
  return `<div class="unita reliquia" style="${colVars(c.colori)}" data-card="${id}" data-rel="${k}">
    <div class="u-dentro"><span class="icona">${ICONA[c.tipo]}</span><span class="u-nome">${esc(id)}</span></div></div>`;
}

function gemmeHTML(n, max, cl) {
  let s = "";
  for (let i = 0; i < Math.max(n, max); i++) s += `<span class="gemma ${i < n ? cl : "vuota"}"></span>`;
  return s;
}

function plancia(g, nome, lato) {
  const L = g.leader;
  const vmax = Math.max(CAT.valori_leader.vite, g.vite);
  let cuori = "";
  for (let i = 0; i < vmax; i++) cuori += `<span class="${i < g.vite ? "" : "perso"}">♥</span>`;
  const cic = g.cicatrici.map((s) => `<span class="cic ${s.fresca ? "fresca" : ""}" style="${colVars(CARTA[s.id]?.colori)}"
      data-card="${s.id}" ${lato === "io" ? `data-scar="${s.id}"` : ""}>${esc(s.id)}</span>`).join("");
  return `<div class="lato-info">
    ${eroeHTML(L.id, L, `${lato}:L`).replace('class="eroe', `class="eroe ${g.alle_corde ? "corde" : ""}`)}
    <div class="risorse">
      <div class="nome-g">${esc(nome)} ${g.alle_corde ? '<span style="color:var(--life)">· Alle Corde</span>' : ""}</div>
      <div class="cuori" title="Vite" data-vite="${lato}">${cuori}</div>
      ${statoVita(g)}
      <div class="gemme" title="Brace: gemme da spendere in questo turno">${gemmeHTML(g.brace, 0, "brace")} <span>Brace ${g.brace}</span></div>
      <div class="gemme" title="Guardia: gemme per difendersi">${gemmeHTML(g.guardia, g.guardia_max, "guardia")} <span>Guardia ${g.guardia}/${g.guardia_max}</span></div>
    </div>
    <div class="risorse">
      <div class="pile"><span class="pila" title="Mazzo">🂠 ${g.mazzo}</span><span class="pila" title="Carte in mano">✋ ${g.mano_n}</span>
        <span class="pila" title="${esc(g.scarti.join(", "))}">🗑 ${g.scarti.length}</span></div>
      <div class="cicatrici"><span class="nota">Cicatrici:</span> ${cic || '<span class="nota">nessuna</span>'}</div>
    </div></div>`;
}

// Perché un colpo a segno può non togliere Vite (§9.2–9.5): lo si dice sotto i cuori
function statoVita(g) {
  const R = stato.partita.regole, fresche = g.cicatrici.filter((c) => c.fresca).length;
  let t = "";
  if (g.alle_corde && fresche) t = "Alle Corde, ma la Cicatrice fresca lo protegge fino a fine turno";
  else if (g.alle_corde) t = "Alle Corde: il prossimo colpo a segno vince la partita";
  else if (fresche >= R.saldo) t = `Saldo pieno (${fresche}/${R.saldo}): altri colpi in questo turno non tolgono Vite`;
  else if (fresche) t = `Cicatrici fresche ${fresche}/${R.saldo}: oltre il Saldo i colpi non tolgono Vite`;
  else if (g.vite === 1 && stato.partita.round < R.corde_a_1) t = `1 Vita: dal round ${R.corde_a_1} basta per essere Alle Corde`;
  return t ? `<div class="stato-vita ${g.alle_corde && !fresche ? "pericolo" : ""}">${t}</div>` : "";
}

function campo(g, lato) {
  const u = g.unita.map((x) => unitaHTML(x, lato)).join("");
  const r = g.reliquie.map((id, k) => reliquiaHTML(id, k)).join("");
  return `<div class="campo ${lato === "io" ? "mio" : ""}">${u || (r ? "" : '<span class="vuoto">nessuna Unità in campo</span>')}${r ? `<span class="sep"></span>${r}` : ""}</div>`;
}

function manoHTML(mano) {
  const n = mano.length;
  return mano.map((id, k) => {
    const off = k - (n - 1) / 2;
    const ang = off * Math.min(7, 40 / Math.max(n, 1));
    const x = off * Math.min(112, 640 / Math.max(n, 1));
    const y = Math.abs(off) * 6;
    const t = `translateX(calc(-50% + ${x}px)) translateY(${y}px) rotate(${ang}deg)`;
    return cartaHTML(id, { attr: `data-mano="${id}" data-t="${t}"`, stile: `transform:${t};z-index:${k + 1}` });
  }).join("");
}

function centroHTML(p) {
  const n = p.nomi;
  let s = `<span class="round">Round ${p.round}</span><span class="fase">${p.attivo_sei_tu ? "Il tuo turno" : `Turno di ${esc(n.avversario)}`} · ${esc(p.fase_testo)}</span>`;
  const cb = p.combattimento;
  if (cb) s += `<span class="fase">⚔ <b>${esc(cb.attaccante)}</b> → <b>${esc(cb.bersaglio)}</b>${cb.opposta_da ? ` (si oppone ${esc(cb.opposta_da)})` : ""}${cb.gemme_attacco != null ? ` · gemme d'attacco ${cb.gemme_attacco}` : ""}</span>${contoHTML(cb.conto)}`;
  if (p.fine) return `${s}<span class="fase"><b>${p.fine.hai_vinto ? "Hai vinto" : "Hai perso"}</b> (${esc(p.fine.motivo)})</span>
    <button class="oro" id="rivincita-c">Nuova partita</button>`;
  if (p.bersaglio) {
    const b = p.bersaglio;
    return `${s}<span class="fase"><b>Effetto di ${esc(b.fonte || "una carta")}</b>: ${b.tuo ? "scegli il bersaglio fra quelli illuminati di rosso" : `${esc(p.decide)} sceglie il bersaglio…`}</span>`;
  }
  if (!p.tocca_a_te) return `${s}<span class="fase" style="opacity:.7">… decide ${esc(p.decide)}</span>`;
  const az = p.azioni;
  if (p.fase === "pugno_att" || p.fase === "impeto") {
    s += `<div class="scelte"><span class="titolo">Quante gemme di Brace impegni nell'attacco?</span>${az.map((a) =>
      `<button class="scelta-gemme" data-i="${a.i}"><span class="gg">${gemmeHTML(a.n, 0, "brace") || "—"}</span>${a.n} gemme
       ${a.fa != null ? `<small>Forza ${a.fa} contro ${a.db}</small>` : ""}</button>`).join("")}</div>`;
  } else if (p.fase === "pugno_def" || p.fase === "risposta") {
    const parate = az.filter((a) => a.gruppo === "parata");
    s += `<div class="scelte"><span class="titolo">Difenditi: gemme di Guardia (+2 l'una) ed eventuale Reazione</span>${parate.map((a) =>
      `<button class="scelta-gemme" data-i="${a.i}" ${a.carta ? `data-card="${a.carta}"` : ""}><span class="gg">${gemmeHTML(a.n, 0, "guardia") || "—"}</span>
        ${a.carta ? `⛨ ${esc(a.carta)}${a.da === "scar" ? " (Cicatrice)" : ""}` : `${a.n} gemme`}
        ${a.fa != null ? `<small>attacco ${a.fa} contro difesa ${a.db}</small>` : ""}</button>`).join("")}</div>`;
    if (az.some((a) => a.gruppo === "opposizione")) s += `<span class="fase">oppure clicca una tua Unità Pronta per opporla</span>`;
  } else if (p.fase === "oppose" || p.fase === "oppose_after") {
    s += `<div class="scelte"><span class="titolo">Vuoi opporre una tua Unità Pronta? Cliccala, oppure:</span>
      ${az.filter((a) => a.gruppo === "opposizione" && a.sorgente == null).map((a) => `<button data-i="${a.i}">${esc(a.testo)}</button>`).join("")}</div>`;
  }
  return s;
}

// Fa e Db dello scontro in corso, con le parti che li compongono
function contoHTML(c) {
  if (!c) return "";
  const parti = (xs) => xs.map((x, k) => `${k ? (x.v != null && x.v < 0 ? " − " : " + ") : ""}${x.v != null ? Math.abs(x.v) : ""} <small>${esc(x.t)}</small>`).join("");
  return `<span class="conto"><span class="att">Attacco <b>${c.fa}</b> = ${parti(c.att)}</span>
    <span class="dif">Difesa <b>${c.db}</b> = ${parti(c.dif)}</span></span>`;
}

function registroHTML(p) {
  const ev = {}; p.eventi.forEach((e) => (ev[e.n] = e));
  const start = p.log_n - p.log.length;
  return p.log.map((l, k) => {
    const e = ev[start + k];
    const cl = !e ? "" : e.t === "turno" ? "r-turno" : e.chi ? `r-${e.chi}` : "";
    return `<div class="${cl}">${esc(l.trim())}</div>`;
  }).join("");
}

// ------------------------------------------------------------------ mulligan (§4.4)
let scartoMull = new Set();
function renderMulligan() {
  const p = stato.partita, m = p.mulligan;
  const chiave = `mull:${p.versione}`;
  if (chiave === chiaveGioco) return;
  chiaveGioco = chiave;
  prec = null;
  if (m.fatto) {
    $("#gioco").innerHTML = `<div class="pannello" style="text-align:center"><h2>Mulligan fatto</h2>
      <p>${m.avversario_fatto ? "Si parte!" : `Aspetto il mulligan di ${esc(p.nomi.avversario)}…`}</p></div>`;
    return;
  }
  const n = scartoMull.size;
  $("#gioco").innerHTML = `<div class="pannello" style="text-align:center">
      <div class="riga" style="justify-content:center;gap:30px">${eroeHTML(m.leader)}<span style="font:800 30px Georgia,serif;color:var(--gold)">VS</span>${eroeHTML(m.leader_avv)}</div>
      <h2>La tua mano iniziale · sei ${p.sei === "G1" ? "il primo giocatore" : "il secondo giocatore"}</h2>
      <p class="nota">Clicca fino a ${m.max} carte da rimettere in fondo al mazzo: ne peschi altrettante dalla cima. Il mazzo non si rimescola.</p>
      <div class="offerta">${m.mano.map((id, k) => `<div class="slot">${cartaHTML(id, { classi: "grande" + (scartoMull.has(k) ? " illegale" : ""), attr: `data-k="${k}"` })}
        <span class="nota">${scartoMull.has(k) ? "⤓ in fondo al mazzo" : "tieni"}</span></div>`).join("")}</div>
      <button class="oro" id="conferma-mull">${n ? `Rimetti ${n} ${n === 1 ? "carta" : "carte"} in fondo e pesca` : "Tieni questa mano"}</button></div>`;
  $$("[data-k]", $("#gioco")).forEach((el) => (el.onclick = () => {
    const k = +el.dataset.k;
    if (scartoMull.has(k)) scartoMull.delete(k);
    else if (scartoMull.size < m.max) scartoMull.add(k);
    else return errore(`Al massimo ${m.max} carte`);
    const via = scartoMull.has(k), n = scartoMull.size;
    el.classList.toggle("illegale", via);
    el.nextElementSibling.textContent = via ? "⤓ in fondo al mazzo" : "tieni";
    $("#conferma-mull").textContent = n ? `Rimetti ${n} ${n === 1 ? "carta" : "carte"} in fondo e pesca` : "Tieni questa mano";
  }));
  $("#conferma-mull").onclick = () => {
    const carte = [...scartoMull].map((k) => m.mano[k]);
    scartoMull = new Set();
    act("/api/mulligan", { carte });
  };
}

function renderGioco() {
  const p = stato.partita;
  const chiave = String(p.versione) + (p.fine ? "f" : "");
  if (chiave === chiaveGioco) return;
  chiaveGioco = chiave;
  const vecchio = prec;
  const rects = fotografa();
  mira = null;
  chiudiMenu();
  $("#gioco").innerHTML = `<div class="tavolo">
    <div class="plancia" id="plancia">
      <div class="mano-avv">${Array.from({ length: p.avversario.mano_n }, () => retroHTML()).join("")}</div>
      ${plancia(p.avversario, p.nomi.avversario, "avv")}
      ${campo(p.avversario, "avv")}
      <div class="centro">${centroHTML(p)}</div>
      ${campo(p.io, "io")}
      ${plancia(p.io, p.nomi.io + " (tu)", "io")}
      <div class="mano" id="mano">${manoHTML(p.io.mano)}</div>
    </div>
    <div class="colonna">
      <button id="fine-turno" class="${p.tocca_a_te && p.fase === "main" ? "attivo" : "attesa"}">${p.fine ? "Partita finita" : p.tocca_a_te && p.fase === "main" ? "FINE TURNO" : p.tocca_a_te ? "Scegli…" : `Turno di ${esc(p.attivo_sei_tu ? p.nomi.io : p.nomi.avversario)}`}</button>
      ${p.puoi_annullare ? '<button id="indietro" title="Annulla la tua ultima scelta: si può finché l\'avversario non ha scelto nulla e non si è scoperta nessuna carta">↶ Torna indietro</button>' : ""}
      <div id="mira-info" class="pannello nascosto"><span></span> <button class="piccolo" id="annulla-mira">Annulla</button></div>
      <div class="pannello"><h3>Registro</h3><div class="registro" id="registro">${registroHTML(p)}</div></div>
      <div class="pannello"><details><summary>Tutte le azioni (${p.azioni.length})</summary>
        ${p.azioni.map((a) => `<button class="piccolo" style="display:block;text-align:left;width:100%" data-i="${a.i}">${esc(a.testo)}</button>`).join("")}</details>
        ${p.fine ? "" : '<button class="piccolo" id="resa">Arrenditi</button>'}
        <p class="nota">Tu sei ${p.sei} · Saldo ${p.regole.saldo} · Crepuscolo al round ${p.regole.crepuscolo}. Clicca le carte illuminate di verde; passa sopra una carta per ingrandirla.</p></div>
    </div></div>`;
  collega(p);
  if (p.bersaglio && p.bersaglio.tuo) {
    mira = { titolo: `Effetto di ${p.bersaglio.fonte || "una carta"}`, obbligo: true,
      opts: p.bersaglio.cands.map((c) => ({ bersaglio: c, trigger: true })) };
    disegnaMira();
    $("#annulla-mira").classList.add("nascosto");
  }
  const reg = $("#registro"); reg.scrollTop = reg.scrollHeight;
  disegnaFreccia();
  anima(vecchio, p, rects);
  prec = p;
}

function collega(p) {
  const tutte = p.azioni;
  const fine = tutte.find((a) => a.gruppo === "turno");
  $("#fine-turno").onclick = () => { if (fine) manda(fine); };
  $$("[data-i]").forEach((b) => (b.onclick = (e) => { e.stopPropagation(); manda(tutte.find((a) => a.i === +b.dataset.i)); }));
  if ($("#indietro")) $("#indietro").onclick = () => act("/api/annulla");
  if ($("#resa")) $("#resa").onclick = () => { if (confirm("Vuoi davvero arrenderti?")) act("/api/resa"); };
  $("#annulla-mira").onclick = annullaMira;
  if ($("#rivincita-c")) $("#rivincita-c").onclick = () => { const f = $("#fine-partita"); if (f) f.remove(); act("/api/rivincita"); };
  const int = intenzioni(tutte);
  for (const el of $$("[data-ent],[data-mano],[data-scar]")) {
    const key = el.dataset.ent || (el.dataset.mano ? `mano:${el.dataset.mano}` : `scar:${el.dataset.scar}`);
    if (int[key]) el.classList.add("giocabile");
    el.addEventListener("click", clicEntita);
  }
  // le carte in mano si sollevano al passaggio del mouse
  for (const c of $$("#mano .carta")) {
    c.addEventListener("mouseenter", () => (c.style.transform = c.dataset.t.replace(/rotate\([^)]*\)/, "rotate(0deg)") + " translateY(-60px) scale(1.12)"));
    c.addEventListener("mouseleave", () => (c.style.transform = c.dataset.t));
  }
  // bersagli della partita in corso
  const cb = p.combattimento;
  if (cb) {
    const latoAtt = cb.attacca_tu ? "io" : "avv", latoDif = cb.attacca_tu ? "avv" : "io";
    const a = $(`[data-ent="${latoAtt}:${cb.att_ref}"]`);
    const d = $(`[data-ent="${latoDif}:${cb.bersaglio_ref == null ? "L" : cb.bersaglio_ref}"]`);
    if (a) a.classList.add("coinvolto");
    if (d) d.classList.add("coinvolto");
  }
}

// ------------------------------------------------------------------ animazioni
function fotografa() {
  const out = {};
  for (const el of $$("[data-uid]")) out[el.dataset.uid] = { r: el.getBoundingClientRect(), html: el.outerHTML };
  for (const el of $$(".eroe[data-ent]")) out[el.dataset.ent] = { r: el.getBoundingClientRect() };
  return out;
}

function centroDi(el) {
  const r = el.getBoundingClientRect();
  return [r.left + r.width / 2, r.top + r.height / 2];
}

function disegnaFreccia() {
  const svg = $("#strato svg");
  svg.innerHTML = "";
  const p = stato && stato.partita;
  if (!p || !p.combattimento || p.fine) return;
  const cb = p.combattimento;
  const latoAtt = cb.attacca_tu ? "io" : "avv", latoDif = cb.attacca_tu ? "avv" : "io";
  const a = $(`[data-ent="${latoAtt}:${cb.att_ref}"]`);
  const d = $(`[data-ent="${latoDif}:${cb.bersaglio_ref == null ? "L" : cb.bersaglio_ref}"]`);
  if (!a || !d) return;
  const [x1, y1] = centroDi(a), [x2, y2] = centroDi(d);
  const mx = (x1 + x2) / 2 + (y2 - y1) * 0.15, my = (y1 + y2) / 2 - Math.abs(x2 - x1) * 0.1;
  svg.innerHTML = `<defs><marker id="punta" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="4" markerHeight="4" orient="auto-start-reverse">
    <path d="M0,0 L10,5 L0,10 z" fill="#ff5a3a"/></marker></defs>
    <path class="freccia" d="M${x1},${y1} Q${mx},${my} ${x2},${y2}" marker-end="url(#punta)"/>`;
}

function effimero(html, cl, ms, pos) {
  const el = document.createElement("div");
  el.className = cl;
  el.innerHTML = html;
  if (pos) { el.style.left = pos[0] + "px"; el.style.top = pos[1] + "px"; }
  document.body.appendChild(el);
  setTimeout(() => el.remove(), ms);
  return el;
}

function ripeti(el, cl) {
  if (!el) return;
  el.classList.remove(cl); void el.offsetWidth; el.classList.add(cl);
}

let coda = Promise.resolve();
function anima(v, p, rects) {
  if (!v) return;                      // primo disegno: niente animazioni
  const nuove = new Set(p.io.unita.map((u) => `io:${u.uid}`).concat(p.avversario.unita.map((u) => `avv:${u.uid}`)));
  const vecchie = new Set(v.io.unita.map((u) => `io:${u.uid}`).concat(v.avversario.unita.map((u) => `avv:${u.uid}`)));
  for (const k of nuove) if (!vecchie.has(k)) $(`[data-uid="${k}"]`)?.classList.add("entra");
  for (const k of vecchie) {
    if (nuove.has(k) || !rects[k]) continue;          // Unità sconfitta: il suo fantasma svanisce
    const g = effimero(rects[k].html, "fantasma", 950);
    g.style.left = rects[k].r.left + "px"; g.style.top = rects[k].r.top + "px";
  }
  const vecchiaMano = new Set(v.io.mano);
  $$("#mano .carta").forEach((c) => { if (!vecchiaMano.has(c.dataset.mano)) c.classList.add("nuova"); });
  for (const lato of ["io", "avv"]) {
    const a = lato === "io" ? v.io : v.avversario, b = lato === "io" ? p.io : p.avversario;
    const eroe = $(`.eroe[data-ent="${lato}:L"]`);
    if (b.vite < a.vite && eroe) {
      effimero(`−${a.vite - b.vite} ♥`, "danno", 1300, centroDi(eroe));
      ripeti(eroe, "trema");
      ripeti($(`[data-vite="${lato}"]`), "trema");
    }
    if (b.leader.risvegliato && !a.leader.risvegliato) ripeti(eroe, "lampo");
  }
  // eventi del registro arrivati da allora, in ordine
  const ev = p.eventi.filter((e) => e.n >= v.log_n);
  const passi = [];
  for (const e of ev) {
    if (e.t === "gioca" || (e.t === "rimargina" && e.chi === "avv")) passi.push(() => volaCarta(e, p));
    else if (e.t === "attacco") passi.push(() => affondo(e, p));
    else if (e.t === "scontro") {
      const dopo = ev.slice(ev.indexOf(e) + 1);
      const fine = dopo.findIndex((x) => x.t === "scontro" || x.t === "attacco" || x.t === "turno");
      const ign = (fine < 0 ? dopo : dopo.slice(0, fine)).find((x) => x.t === "ignorata");
      passi.push(() => scoppioScontro(e, ign));
    }
  }
  const turni = ev.filter((e) => e.t === "turno");
  if (turni.length && !p.fine) {
    const t = turni[turni.length - 1];
    passi.push(() => { if ((t.chi === "io") !== !!stato?.partita?.attivo_sei_tu) return; effimero(t.chi === "io" ? "IL TUO TURNO" : `TURNO DI ${esc(p.nomi.avversario).toUpperCase()}`, "banner", 1600); return sleep(t.chi === "io" ? 900 : 500); });
  }
  if (p.fine && !v.fine) passi.push(() => fineAnim(p));
  // le animazioni restano in coda solo pochi secondi: se l'avversario è veloce non si accumulano
  const nato = Date.now();
  for (const f of passi.slice(-8)) coda = coda.then(() => (Date.now() - nato < 4000 || f === passi[passi.length - 1] ? f() : null)).catch(() => {});
}

function volaCarta(e, p) {
  const chi = e.chi === "io" ? "Giochi" : `${esc(p.nomi.avversario)} gioca`;
  effimero(`<div class="chi">${e.t === "rimargina" ? `${esc(p.nomi.avversario)} Rimargina` : chi}</div>${cartaHTML(e.carta, { classi: "grande" })}`,
    "volante", 1500);
  return sleep(e.chi === "io" ? 500 : 1100);
}

function affondo(e) {
  const cb = stato.partita.combattimento;
  if (cb) {
    const el = $(`[data-ent="${cb.attacca_tu ? "io" : "avv"}:${cb.att_ref}"]`);
    ripeti(el, cb.attacca_tu ? "affondo-su" : "affondo-giu");
  }
  return sleep(350);
}

function scoppioScontro(e, ign) {
  const colpo = +e.fa >= +e.db;
  effimero(`<span class="vs"><span class="att">${e.fa}</span> ⚔ <span class="dif">${e.db}</span></span>
    <span class="esito ${colpo ? "colpo" : "parato"}">${colpo ? "A SEGNO!" : "RESPINTO"}</span>
    ${ign ? `<span class="esito perche">Nessuna Vita persa: ${esc(ign.perche)}</span>` : ""}
    ${e.carta ? `<span class="esito" style="font-size:16px">Reazione ${esc(e.carta)}</span>` : ""}`,
    ign ? "scontro-pop lungo" : "scontro-pop", ign ? 2600 : 1400);
  return sleep(ign ? 1500 : 900);
}

function fineAnim(p) {
  const old = $("#fine-partita"); if (old) old.remove();
  const el = document.createElement("div");
  el.id = "fine-partita";
  el.className = p.fine.hai_vinto ? "vinto" : "perso";
  el.innerHTML = `<h2>${p.fine.hai_vinto ? "VITTORIA" : "SCONFITTA"}</h2>
    <p>${esc(p.fine.motivo)}${p.fine.vincitore ? ` · vince ${esc(p.fine.vincitore)}` : ""}</p>
    <div><button class="oro" id="rivincita">Nuova partita nella stessa stanza</button> <button class="piccolo" id="guarda">Guarda il tavolo</button></div>`;
  document.body.appendChild(el);
  $("#rivincita").onclick = () => { el.remove(); act("/api/rivincita"); };
  $("#guarda").onclick = () => el.remove();
  return sleep(100);
}

avvio().catch((e) => errore("Impossibile caricare il catalogo: " + e.message));
