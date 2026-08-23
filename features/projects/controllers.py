from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from features.projects.services import create_project_logic
from shared.utils import format_response

router = APIRouter(prefix="/projects", tags=["TeFa Projects"])

class ProjectRequest(BaseModel):
    name: str
    client_name: str
    total_budget: float

@router.post("/")
def create_project(payload: ProjectRequest):
    result = create_project_logic(payload.name, payload.client_name, payload.total_budget)
    if result["status"] == "success":
        return format_response(success=True, message="Proyek TeFa berhasil dibuat!", data=result)
    raise HTTPException(status_code=400, detail=result["message"])