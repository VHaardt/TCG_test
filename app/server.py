"""Server HTTP dell'app online di CICATRICI (solo libreria standard, più numpy per l'IA).

    python -m app.server            # http://localhost:8000
    PORT=9000 python -m app.server

Il client (app/static) interroga /api/stato una volta al secondo; nessun account, le stanze
vivono in memoria finché il server è acceso (scadono dopo 6 ore senza visite)."""
import json
import mimetypes
import os
import sys
import traceback
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs, urlparse

from . import core

STATIC = os.path.join(core.HERE, "static")
REG = core.Registro()


def _nome(body):
    n = str(body.get("nome") or "").strip()[:24]
    if not n:
        raise ValueError("serve un nome")
    return n


def api(method, path, q, body):
    """(stato HTTP, risposta json) per una chiamata all'API; gli errori diventano codici HTTP."""
    try:
        return _api(method, path, q, body)
    except KeyError as e:
        return 404, {"errore": e.args[0] if e.args else "non trovato"}
    except PermissionError as e:
        return 403, {"errore": str(e)}
    except (ValueError, TypeError) as e:
        return 400, {"errore": str(e)}
    except Exception as e:                          # un errore del motore non deve fermare il server
        traceback.print_exc()
        return 500, {"errore": f"errore interno: {e}"}


def _api(method, path, q, body):
    if path == "/api/catalogo":
        return 200, core.dati().catalogo()
    if path == "/api/stanza" and method == "POST":
        st = REG.crea(body.get("modalita", "costruito"), _nome(body), bool(body.get("contro_ia")))
        return 200, {"codice": st.codice, "token": st.posti[0].token}
    if path == "/api/entra" and method == "POST":
        st = REG.get(body.get("codice"))
        with st.lock:
            p = st.entra(_nome(body))
        return 200, {"codice": st.codice, "token": p.token}

    st = REG.get(body.get("codice") or q.get("codice", [""])[0])
    token = body.get("token") or q.get("token", [""])[0]
    with st.lock:
        i, _ = st.posto(token)
        if path == "/api/stato":
            pass
        elif method != "POST":
            return 405, {"errore": "usa POST"}
        elif path == "/api/mazzo":
            st.imposta_mazzo(i, body.get("leader"), body.get("carte"))
        elif path == "/api/mazzo/pronto":
            st.scegli_pronto(i, body.get("nome"))
        elif path == "/api/annulla":
            st.annulla(i)
        elif path == "/api/mazzo/annulla":
            st.annulla_pronto(i)
        elif path == "/api/draft/leader":
            st.draft_leader(i, body.get("leader"))
        elif path == "/api/draft/scelta":
            st.draft_scelta(i, body.get("carta"))
        elif path == "/api/azione":
            st.azione(i, int(body.get("versione", -1)), int(body.get("indice", -1)))
        elif path == "/api/mulligan":
            st.mulligan(i, body.get("carte"))
        elif path == "/api/bersaglio":
            st.bersaglio(i, int(body.get("versione", -1)), body.get("uid"))
        elif path == "/api/resa":
            st.resa(i)
        elif path == "/api/rivincita":
            st.rivincita()
        else:
            return 404, {"errore": "chiamata sconosciuta"}
        return 200, st.vista(i)


class Handler(BaseHTTPRequestHandler):
    server_version = "Cicatrici/0.1"

    def log_message(self, fmt, *args):
        if os.environ.get("CICATRICI_LOG"):
            super().log_message(fmt, *args)

    def _send(self, code, payload, ctype="application/json; charset=utf-8"):
        data = payload if isinstance(payload, bytes) else json.dumps(payload, ensure_ascii=False).encode()
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(data)

    def _handle(self, method):
        url = urlparse(self.path)
        if not url.path.startswith("/api/"):
            return self._static(url.path)
        body = {}
        if method == "POST":
            n = int(self.headers.get("Content-Length") or 0)
            if n > 100_000:
                return self._send(413, {"errore": "richiesta troppo grande"})
            try:
                body = json.loads(self.rfile.read(n) or b"{}")
            except json.JSONDecodeError:
                return self._send(400, {"errore": "json non valido"})
        self._send(*api(method, url.path, parse_qs(url.query), body))

    def _static(self, path):
        rel = "index.html" if path in ("", "/") else path.lstrip("/")
        full = os.path.normpath(os.path.join(STATIC, rel))
        if not full.startswith(STATIC + os.sep) or not os.path.isfile(full):
            return self._send(404, b"non trovato", "text/plain; charset=utf-8")
        with open(full, "rb") as f:
            data = f.read()
        ctype = mimetypes.guess_type(full)[0] or "application/octet-stream"
        if ctype.startswith("text/") or ctype.endswith("javascript"):
            ctype += "; charset=utf-8"
        self._send(200, data, ctype)

    def do_GET(self):
        self._handle("GET")

    def do_POST(self):
        self._handle("POST")


def main():
    port = int(os.environ.get("PORT", "8000"))
    host = os.environ.get("HOST", "0.0.0.0")
    d = core.dati()
    srv = ThreadingHTTPServer((host, port), Handler)
    print(f"CICATRICI online su http://{host}:{port}  set: {d.set_path}  regole: {d.regole_spec}", file=sys.stderr)
    srv.serve_forever()


if __name__ == "__main__":
    main()
