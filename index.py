"""Entry point autodetectable por Vercel para la plataforma ludica."""

from fastapi import FastAPI
from fastapi.responses import HTMLResponse, Response

app = FastAPI(title="Geografia de Colombia - Estrellas", version="0.1.0")


@app.get("/", response_class=HTMLResponse, include_in_schema=False)
def inicio() -> str:
    return """<!doctype html><html lang="es"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>Geografia de Colombia</title>
<style>body{font-family:system-ui;background:#f5f3ff;color:#24134f;margin:0;display:grid;place-items:center;min-height:100vh}.card{max-width:680px;margin:24px;padding:36px;border-radius:24px;background:#fff;box-shadow:0 12px 40px #27105b22}h1{color:#5b21b6}.star{font-size:2rem}</style></head>
<body><main class="card"><div class="star">* * *</div><h1>Geografia de Colombia</h1>
<p>Plataforma ludica basada en retos y recompensas.</p><p>Consigue Estrellas al responder correctamente preguntas sobre las regiones, departamentos y paisajes de Colombia.</p>
<p><strong>Aprendiz:</strong> Miguel Fajardo<br><strong>Mecanica:</strong> Estrellas</p><p><a href="/docs">Documentacion de la API</a></p></main></body></html>"""


@app.get("/salud", tags=["Sistema"])
def salud() -> dict[str, str]:
    return {"estado": "ok"}


@app.get("/api/proyecto", tags=["Proyecto"])
def proyecto() -> dict[str, str]:
    return {"aprendiz": "Miguel Fajardo", "curso": "Geografia de Colombia", "mecanica": "Estrellas", "version": "0.1.0"}


@app.get("/sw.js", include_in_schema=False)
def service_worker() -> Response:
    return Response("self.addEventListener('install',()=>self.skipWaiting());", media_type="application/javascript")
