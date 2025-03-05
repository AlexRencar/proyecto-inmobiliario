from sqlalchemy.orm import Session
from . import models, schemas

def get_projects(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Project).offset(skip).limit(limit).all()

def create_project(db: Session, project: schemas.ProjectCreate):
    db_project = models.Project(**project.model_dump())
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project

def search_projects(db: Session, category: str = None, min_price: float = None, max_price: float = None):
    query = db.query(models.Project)
    if category:
        query = query.filter(models.Project.category.ilike(f"%{category}%"))
    if min_price is not None:
        query = query.filter(models.Project.price >= min_price)
    if max_price is not None:
        query = query.filter(models.Project.price <= max_price)
    return query.all()

def update_project(db: Session, project_id: int, project_update: schemas.ProjectCreate):
    db_project = db.query(models.Project).filter(models.Project.id == project_id).first()
    if not db_project:
        return None
    # Actualizamos cada campo con los datos del proyecto recibido
    for key, value in project_update.model_dump().items():
        setattr(db_project, key, value)
    db.commit()
    db.refresh(db_project)
    return db_project

def delete_project(db: Session, project_id: int):
    db_project = db.query(models.Project).filter(models.Project.id == project_id).first()
    if not db_project:
        return None
    db.delete(db_project)
    db.commit()
    return db_project
