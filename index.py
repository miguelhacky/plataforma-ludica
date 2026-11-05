from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def inicio() -> dict[str, str]:
    return {"estado": "ok", "proyecto": "Geografia de Colombia"}
