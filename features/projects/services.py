from sqlalchemy.orm import Session
from features.projects.models import Project
from features.projects.schemas import ProjectCreate

def get_all_projects_db(db: Session):
    return db.query(Project).all()

def get_project_by_id_db(db: Session, project_id: int):
    return db.query(Project).filter(Project.id == project_id).first()

def create_project_db(db: Session, payload: ProjectCreate):
    new_project = Project(
        name=payload.name,
        client_name=payload.client_name,
        total_budget=payload.total_budget
    )
    db.add(new_project)
    db.commit()
    db.refresh(new_project)
    return new_project