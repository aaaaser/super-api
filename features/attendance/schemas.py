from datetime import datetime
from pydantic import BaseModel

class AttendanceCheckIn(BaseModel):
    student_id: str
    project_id: int

class AttendanceResponse(BaseModel):
    id: int
    student_id: str
    project_id: int
    status: str
    created_at: datetime

    class Config:
        from_attributes = True