from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from core.database import get_db
from features.projects.schemas import ProjectCreate, ProjectResponse
from features.projects.services import get_all_projects_db, get_project_by_id_db, create_project_db

router = APIRouter(prefix="/projects", tags=["Projects"])

@router.get("/", response_model=List[ProjectResponse], status_code=status.HTTP_200_OK)
def get_projects(db: Session = Depends(get_db)):
    return get_all_projects_db(db)

@router.get("/{project_id}", response_model=ProjectResponse, status_code=status.HTTP_200_OK)
def get_project(project_id: int, db: Session = Depends(get_db)):
    project = get_project_by_id_db(db, project_id)
    if not project:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Project not found"
        )
    return project

@router.post("/", response_model=ProjectResponse, status_code=status.HTTP_201_CREATED)
def create_project(payload: ProjectCreate, db: Session = Depends(get_db)):
    return create_project_db(db, payload)