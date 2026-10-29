"""Genera il regolamento illustrato di CICATRICI (HTML, versione per artifact, PDF).

Sorgente: docs/manuale/ (manuale.md, figure/*.svg, stile.css, modello.html).
I numeri delle regole non sono scritti a mano: {{nome}} nel testo e nelle figure
si legge dal preset del simulatore indicato nel front matter di manuale.md
(sim/v02/config.py), più poche costanti del mazzo (sim/v02/decks.py).

Uso (dalla radice del repo):
    python3 tools/manuale/build.py                 # HTML + versione artifact
    python3 tools/manuale/build.py --pdf           # anche il PDF (Chromium headless)
    python3 tools/manuale/build.py --copia /mnt/project-files/tcg/regolamento_illustrato
    python3 tools/manuale/build.py --parametri     # elenca i {{nomi}} disponibili
Procedura completa: docs/manuale/LEGGIMI.md."""
import argparse
import datetime
import glob
import html
import os
import re
import shutil
import subprocess
import sys

import markdown

RADICE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, RADICE)

from sim.v02.config import rules_from  # noqa: E402
from sim.v02.decks import DECK_SIZE, MAX_COPIES  # noqa: E402

SORGENTE = os.path.join(RADICE, "docs", "manuale")
USCITA = os.path.join(SORGENTE, "build")
REGOLAMENTO = os.path.join(RADICE, "docs", "regolamento_v0.2.md")
NOME = "regolamento_illustrato"
CHROMIUM = ["/opt/pw-browsers/chromium", "chromium", "chromium-browser", "google-chrome"]


# --- parametri -----------------------------------------------------------------

def elenco(numeri, cong="e"):
    numeri = [str(n) for n in numeri]
    return numeri[0] if len(numeri) == 1 else ", ".join(numeri[:-1]) + f" {cong} " + numeri[-1]


def fine_garantita(r):
    """Round in cui un Leader con v Vite perde al più tardi (Ripristino di G1), simulando il Crepuscolo."""
    righe = {}
    for vite in range(r.life + 1):
        v, rnd = vite, r.crepuscolo_round
        while True:
            corde = v == 0 or (v == 1 and rnd >= r.corde_one_life_round)
            if corde:
                break
            v, rnd = max(0, v - r.crepuscolo_loss), rnd + 1
        righe.setdefault(rnd, []).append(vite)
    return righe


def parametri(preset):
    r = rules_from(preset)
    p = {k: v for k, v in r.as_dict().items() if not isinstance(v, (tuple, list))}
    p["preset"] = preset
    p["mazzo"] = DECK_SIZE
    p["copie"] = MAX_COPIES
    p["tempra_risv"] = r.tempra_awakened or r.tempra
    p["gemme_leader_base"] = max(0, -(-(r.tempra - r.leader_power) // r.forza_per_gemma))
    p["gemme_leader_risv"] = max(0, -(-(p["tempra_risv"] - r.leader_power_awakened) // r.forza_per_gemma))
    extra = set(r.scintilla_extra_rounds)
    if r.scintilla_g2_gems:
        extra.add(1)
    if r.scintilla_extra_gems:
        extra.add(r.scintilla_extra_round)
    p["round_g2"] = elenco(sorted(extra)) if extra else "nessun round"
    p["round_g2_lista"] = sorted(extra)
    p["guard_max_corde"] = r.guard_max + r.guard_alle_corde_bonus
    p["guard_max_risv_corde"] = r.guard_max_awakened + r.guard_alle_corde_bonus
    p["vite_risveglio"] = r.life - r.awaken_at_life
    p["primo_attacco"] = r.no_attack_round + 1
    p["gemme_scorta"] = 12
    p["gemme_totali"] = 24
    fg = fine_garantita(r)
    p["fine_garantita"] = fg
    p["fine_garantita_righe"] = "\n".join(
        f"| Ripristino di G1 del round {rnd} | {elenco(vite, 'o')} |"
        for rnd, vite in sorted(fg.items()))
    return p


# --- figure e blocchi ----------------------------------------------------------

def sostituisci(testo, p, dove):
    def f(m):
        nome = m.group(1).strip()
        if nome not in p:
            raise SystemExit(f"{dove}: parametro sconosciuto {{{{{nome}}}}} (vedi --parametri)")
        return str(p[nome])
    return re.sub(r"\{\{\s*([a-z0-9_]+)\s*\}\}", f, testo)


def figura_tracciato(p):
    """Il tracciato del round, disegnato dai parametri (Brace, compensazione, soglie)."""
    n, w, h0 = 15, 52, 44
    larg = n * w + 20
    eventi = {p["saldo_late_round"]: f"Saldo {p['saldo_late']}",
              p["corde_one_life_round"]: "Alle Corde a 1 Vita",
              p["crepuscolo_round"]: "Crepuscolo"}
    out = [f'<svg viewBox="0 0 {larg} 176" role="img" aria-label="Tracciato del round" class="fig-svg">']
    for i in range(1, n + 1):
        x = 10 + (i - 1) * w
        brace = min(i, p["brace_max"])
        cls = "trk-cella trk-ev" if i in eventi else "trk-cella"
        out.append(f'<rect x="{x}" y="{h0}" width="{w - 4}" height="56" rx="6" class="{cls}"/>')
        out.append(f'<text x="{x + (w - 4) / 2}" y="{h0 + 24}" class="trk-num">{i}</text>')
        out.append(f'<circle cx="{x + 14}" cy="{h0 + 41}" r="6" class="gemma"/>'
                   f'<text x="{x + 24}" y="{h0 + 46}" class="trk-brace">{brace}</text>')
        if i == p["no_attack_round"]:
            out.append(f'<text x="{x}" y="{h0 + 120}" class="trk-nota" style="text-anchor:start">niente attacchi</text>')
        if i in p["round_g2_lista"]:
            out.append(f'<rect x="{x + 2}" y="{h0 + 64}" width="{w - 8}" height="22" rx="11" class="trk-g2"/>'
                       f'<text x="{x + (w - 4) / 2}" y="{h0 + 79}" class="trk-g2t">G2 +1</text>')
        if i in eventi:
            out.append(f'<line x1="{x + (w - 4) / 2}" y1="{h0 + 90}" x2="{x + (w - 4) / 2}" y2="{h0 + 104}" class="trk-linea"/>'
                       f'<text x="{x + w - 4}" y="{h0 + 120}" class="trk-ev-t" text-anchor="end">{eventi[i]}</text>')
    out.append(f'<text x="10" y="20" class="trk-leg">Il segnalino avanza all\'inizio di ogni turno di G1. '
               f'<tspan class="trk-leg-b">Numero</tspan> = round · gemma = Brace del round</text>')
    out.append("</svg>")
    return "\n".join(out)


FIGURE_PY = {"tracciato": figura_tracciato}

ICONE = {
    ":gemma:": '<span class="ic-gemma" aria-label="gemma"></span>',
    ":ruota:": '<span class="ic-ruota" aria-label="ruota">⟳</span>',
}

BLOCCO = re.compile(r"^::: *([a-z]+) *(.*)$")


def blocchi(testo):
    """::: tipo Titolo ... ::: diventa un riquadro (esempio, ricorda, attenzione, prova, riepilogo)."""
    righe, aperti = [], 0
    for riga in testo.split("\n"):
        m = BLOCCO.match(riga.strip())
        if m:
            tipo, titolo = m.group(1), m.group(2).strip()
            righe.append(f'\n<div class="box box-{tipo}" markdown="1">\n')
            if titolo:
                righe.append(f'<p class="box-tit">{html.escape(titolo)}</p>\n')
            aperti += 1
        elif riga.strip() == ":::":
            if not aperti:
                raise SystemExit("manuale.md: ':::' di chiusura senza apertura")
            righe.append("\n</div>\n")
            aperti -= 1
        else:
            righe.append(riga)
    if aperti:
        raise SystemExit("manuale.md: un blocco ':::' non è chiuso")
    return "\n".join(righe)


def figure(testo, p):
    def f(m):
        nome, didascalia = m.group(1), (m.group(2) or "").strip()
        if nome in FIGURE_PY:
            svg = FIGURE_PY[nome](p)
        else:
            percorso = os.path.join(SORGENTE, "figure", nome + ".svg")
            if not os.path.exists(percorso):
                raise SystemExit(f"manuale.md: figura mancante figure/{nome}.svg")
            with open(percorso, encoding="utf-8") as fh:
                svg = sostituisci(fh.read(), p, f"figure/{nome}.svg")
            svg = re.sub(r"<\?xml[^>]*\?>", "", svg).strip()
        cap = f"<figcaption>{html.escape(didascalia)}</figcaption>" if didascalia else ""
        return f'\n<figure class="fig fig-{nome}"><div class="fig-scroll">{svg}</div>{cap}</figure>\n'
    return re.sub(r"^\[\[figura:([a-z0-9_]+)(?:\|([^\]]*))?\]\]$", f, testo, flags=re.M)


# --- composizione --------------------------------------------------------------

def front_matter(testo):
    m = re.match(r"^---\n(.*?)\n---\n", testo, re.S)
    if not m:
        raise SystemExit("manuale.md: manca il front matter (--- ... ---)")
    meta = dict(re.findall(r"^([a-z_]+):\s*(.*)$", m.group(1), re.M))
    return meta, testo[m.end():]


def versione_regolamento():
    with open(REGOLAMENTO, encoding="utf-8") as fh:
        m = re.search(r"^\| Versione \| (v[0-9.]+)", fh.read(), re.M)
    return m.group(1) if m else "?"


def indice(corpo_html):
    voci = re.findall(r'<h2 id="([^"]+)">(.*?)</h2>', corpo_html)
    return "\n".join(f'<li><a href="#{i}">{re.sub(r"<[^>]+>", "", t)}</a></li>' for i, t in voci)


def slug(valore, separatore):
    import unicodedata
    v = unicodedata.normalize("NFKD", valore).encode("ascii", "ignore").decode()
    v = re.sub(r"[^\w\s-]", "", v).strip().lower()
    return re.sub(r"[\s_-]+", separatore, v)


def costruisci(args):
    with open(os.path.join(SORGENTE, "manuale.md"), encoding="utf-8") as fh:
        meta, testo = front_matter(fh.read())
    p = parametri(meta.get("preset", "V026"))
    reg = versione_regolamento()
    if meta.get("basato_su") != reg:
        msg = (f"ATTENZIONE: manuale.md dice basato_su {meta.get('basato_su')}, "
               f"ma docs/regolamento_v0.2.md è {reg}. Rileggi il registro modifiche del regolamento "
               f"e aggiorna il testo (LEGGIMI.md, passo 2).")
        if args.rigido:
            raise SystemExit(msg)
        print(msg, file=sys.stderr)

    testo = sostituisci(testo, p, "manuale.md")
    testo = figure(testo, p)
    testo = blocchi(testo)
    for k, v in ICONE.items():
        testo = testo.replace(k, v)
    md = markdown.Markdown(extensions=["extra", "toc", "sane_lists"],
                           extension_configs={"toc": {"slugify": slug}})
    corpo = md.convert(testo)
    corpo = corpo.replace("<table>", '<div class="tab-scroll"><table>').replace("</table>", "</table></div>")

    with open(os.path.join(SORGENTE, "stile.css"), encoding="utf-8") as fh:
        css = fh.read()
    with open(os.path.join(SORGENTE, "modello.html"), encoding="utf-8") as fh:
        modello = fh.read()
    oggi = datetime.date.today().isoformat()
    sost = {"CSS": css, "CORPO": corpo, "INDICE": indice(corpo), "VERSIONE": meta.get("versione", "?"),
            "REGOLAMENTO": reg, "PRESET": p["preset"], "DATA": oggi}
    pagina = re.sub(r"%%([A-Z]+)%%", lambda m: sost[m.group(1)], modello)

    os.makedirs(USCITA, exist_ok=True)
    completo = os.path.join(USCITA, NOME + ".html")
    with open(completo, "w", encoding="utf-8") as fh:
        fh.write("<!doctype html>\n<html lang=\"it\">\n<head>\n<meta charset=\"utf-8\">\n"
                 "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1, viewport-fit=cover\">\n"
                 + pagina.replace("<!--CORPO-->", "</head>\n<body>", 1) + "\n</body>\n</html>\n")
    # L'artifact riceve dal servizio il proprio scheletro (doctype, head, body): solo il contenuto.
    artifact = os.path.join(USCITA, NOME + ".artifact.html")
    with open(artifact, "w", encoding="utf-8") as fh:
        fh.write(pagina.replace("<!--CORPO-->", "", 1))
    print(f"scritto {os.path.relpath(completo, RADICE)} e {os.path.relpath(artifact, RADICE)} "
          f"(regolamento {reg}, preset {p['preset']})")

    uscite = [completo, artifact]
    if args.pdf:
        uscite.append(pdf(completo))
    if args.copia:
        os.makedirs(args.copia, exist_ok=True)
        for f in uscite:
            shutil.copy2(f, args.copia)
        print(f"copiato in {args.copia}")


def pdf(completo):
    exe = next((c for c in CHROMIUM if shutil.which(c) or os.path.exists(c)), None)
    if exe is None:
        raise SystemExit("PDF: Chromium non trovato")
    dest = completo[:-5] + ".pdf"
    subprocess.run([exe, "--headless", "--no-sandbox", "--disable-gpu", "--no-pdf-header-footer",
                    "--virtual-time-budget=8000", f"--print-to-pdf={dest}", "file://" + completo],
                   check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f"scritto {os.path.relpath(dest, RADICE)}")
    return dest


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--pdf", action="store_true", help="genera anche il PDF stampabile")
    ap.add_argument("--copia", metavar="CARTELLA", help="copia le uscite in questa cartella")
    ap.add_argument("--rigido", action="store_true", help="errore se manuale e regolamento hanno versioni diverse")
    ap.add_argument("--parametri", action="store_true", help="elenca i parametri {{nome}} e i loro valori")
    args = ap.parse_args()
    if args.parametri:
        with open(os.path.join(SORGENTE, "manuale.md"), encoding="utf-8") as fh:
            meta, _ = front_matter(fh.read())
        for k, v in sorted(parametri(meta.get("preset", "V026")).items()):
            if not isinstance(v, (dict, list)) and k != "fine_garantita_righe":
                print(f"{{{{{k}}}}} = {v}")
        return
    costruisci(args)


if __name__ == "__main__":
    main()
