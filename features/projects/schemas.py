from datetime import datetime
from pydantic import BaseModel

class ProjectCreate(BaseModel):
    name: str
    client_name: str
    total_budget: float

class ProjectResponse(BaseModel):
    id: int
    name: str
    client_name: str
    total_budget: float
    created_at: datetime

    class Config:
        from_attributes = True