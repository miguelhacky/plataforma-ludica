"""Punto de entrada de la aplicación FastAPI para Vercel (serverless compatible)."""

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, PlainTextResponse

app = FastAPI(
    title="Plataforma lúdica de cursos para niños",
    description="Proyecto de Miguel Fajardo: Geografía de Colombia con Estrellas.",
    version="0.1.0",
)


# Datos del proyecto incrustados (compatibles con serverless)
PROYECTO = {
    "aprendiz": "Miguel Fajardo",
    "curso": "Geografía de Colombia",
    "mecanica": "Estrellas",
    "version": "0.1.0",
}


@app.get("/", response_class=HTMLResponse)
def inicio() -> str:
    """Página de inicio HTML."""
    return """<!doctype html><html lang="es"><head><meta charset="utf-8">
    <title>Geografía de Colombia</title></head><body><h1>Geografía de Colombia</h1>
    <p>Plataforma lúdica con mecánica de <strong>Estrellas</strong>.</p>
    <ul><li>Aprendiz: Miguel Fajardo</li><li>Curso: Geografía de Colombia</li>
    <li>Estrellas: recompensa por cada reto superado</li></ul>
    <a href="/docs">API</a>
    </body></html>"""


@app.get("/salud")
def salud() -> dict[str, str]:
    """Indica si la aplicación está en funcionamiento."""
    return {"estado": "ok", "servicio": "plataforma-ludica"}


@app.get("/api/proyecto")
def proyecto() -> dict[str, str]:
    """Devuelve los datos de identificación del proyecto."""
    return PROYECTO


@app.get("/sw.js", response_class=PlainTextResponse)
def service_worker() -> str:
    """El service worker se sirve desde la raíz."""
    return "self.addEventListener('fetch', () => {});"