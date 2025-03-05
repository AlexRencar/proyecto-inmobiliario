from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app import crud, schemas, models
from app.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter(
    prefix="/projects",
    tags=["projects"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Endpoint para listar los proyectos existentes
@router.get("/", response_model=list[schemas.ProjectResponse])
def read_projects(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    projects = crud.get_projects(db, skip=skip, limit=limit)
    return projects

# Endpoint crear proyectos
@router.post("/", response_model=schemas.ProjectResponse)
def create_project(project: schemas.ProjectCreate, db: Session = Depends(get_db)):
    return crud.create_project(db, project)

# Endpoint para buscar un proyecto o proyectos
@router.get("/search", response_model=list[schemas.ProjectResponse])
def search_projects(
    category: str = Query(None, description="Filtrar por categoría"),
    min_price: float = Query(None, description="Precio mínimo"),
    max_price: float = Query(None, description="Precio máximo"),
    db: Session = Depends(get_db)
):
    results = crud.search_projects(db, category=category, min_price=min_price, max_price=max_price)
    if not results:
        raise HTTPException(status_code=404, detail="No se encontraron proyectos")
    return results

# Endpoint para actualizar un proyecto
@router.put("/{project_id}", response_model=schemas.ProjectResponse)
def update_project_endpoint(project_id: int, project: schemas.ProjectCreate, db: Session = Depends(get_db)):
    updated_project = crud.update_project(db, project_id, project)
    if not updated_project:
        raise HTTPException(status_code=404, detail="Proyecto no encontrado")
    return updated_project

# Endpoint para eliminar un proyecto
@router.delete("/{project_id}", response_model=schemas.ProjectResponse)
def delete_project_endpoint(project_id: int, db: Session = Depends(get_db)):
    deleted_project = crud.delete_project(db, project_id)
    if not deleted_project:
        raise HTTPException(status_code=404, detail="Proyecto no encontrado")
    return deleted_project