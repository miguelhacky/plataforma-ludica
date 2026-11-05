"""Punto de entrada de FastAPI para Vercel."""

try:
    from app.main import app
except Exception as exc:  # pragma: no cover - diagnóstico temporal de despliegue
    from fastapi import FastAPI

    app = FastAPI(title="Diagnóstico temporal")
    error = repr(exc)

    @app.get("/")
    def diagnostic():
        return {"error_importacion": error}

__all__ = ["app"]
