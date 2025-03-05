from fastapi import FastAPI
from app.routers import projects

app = FastAPI(title="API de Proyectos Inmobiliarios")

# Incluir el router para los proyectos
app.include_router(projects.router)

@app.get("/")
def read_root():
    return {"message": "Bienvenido al Sistema de Proyectos Inmobiliarios"}
