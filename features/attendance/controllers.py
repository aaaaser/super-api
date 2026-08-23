# features/attendance/controllers.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from features.attendance.services import checkin_attendance_logic
from shared.utils import format_response

router = APIRouter(prefix="/attendance", tags=["TeFa Attendance"])

class AttendanceRequest(BaseModel):
    student_id: int
    project_id: int

@router.post("/check-in")
def check_in(payload: AttendanceRequest):
    result = checkin_attendance_logic(payload.student_id, payload.project_id)
    if result["status"] == "success":
        return format_response(success=True, message="Absensi masuk berhasil diisi!", data=result)
    raise HTTPException(status_code=400, detail=result["message"])