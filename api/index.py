"""Adaptador FastAPI para el despliegue serverless en Vercel."""

from fastapi import FastAPI
from fastapi.responses import HTMLResponse, Response

app = FastAPI(
    title="Plataforma lúdica de Geografía de Colombia",
    description="Juego educativo con mecánica de Estrellas.",
    version="0.1.0",
)


@app.get("/", response_class=HTMLResponse, include_in_schema=False)
def inicio() -> str:
    return """<!doctype html>
<html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Geografía de Colombia | Estrellas</title>
<style>body{font-family:system-ui,sans-serif;background:#f5f3ff;color:#24134f;margin:0;display:grid;place-items:center;min-height:100vh}.card{max-width:680px;margin:24px;padding:36px;border-radius:24px;background:white;box-shadow:0 12px 40px #27105b22}h1{color:#5b21b6}li{margin:12px 0}.estrella{font-size:2rem}</style></head>
<body><main class="card"><div class="estrella">⭐ ⭐ ⭐</div><h1>Geografía de Colombia</h1>
<p>Plataforma lúdica de aprendizaje basada en retos y recompensas.</p>
<ul><li>Responde preguntas sobre regiones, departamentos y paisajes de Colombia.</li>
<li>Obtén Estrellas por cada respuesta correcta.</li><li>Consulta el progreso y supera nuevos retos.</li></ul>
<p><strong>Aprendiz:</strong> Miguel Fajardo<br><strong>Mecánica:</strong> Estrellas</p>
<p><a href="/docs">Abrir documentación de la API</a></p></main></body></html>"""


@app.get("/salud", tags=["Sistema"])
def salud() -> dict[str, str]:
    return {"estado": "ok"}


@app.get("/api/proyecto", tags=["Proyecto"])
def proyecto() -> dict[str, str]:
    return {
        "aprendiz": "Miguel Fajardo",
        "curso": "Geografía de Colombia",
        "mecanica": "Estrellas",
        "version": "0.1.0",
    }


@app.get("/sw.js", include_in_schema=False)
def service_worker() -> Response:
    script = "self.addEventListener('install',()=>self.skipWaiting());"
    return Response(script, media_type="application/javascript")
