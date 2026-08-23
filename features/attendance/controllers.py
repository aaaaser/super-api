from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from core.database import get_db
from features.attendance.schemas import AttendanceCheckIn, AttendanceResponse
from features.attendance.services import create_attendance_db

router = APIRouter(prefix="/attendance", tags=["Attendance"])

@router.post("/checkin", response_model=AttendanceResponse, status_code=status.HTTP_201_CREATED)
def checkin_attendance(payload: AttendanceCheckIn, db: Session = Depends(get_db)):
    result = create_attendance_db(db, payload.student_id, payload.project_id)
    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Project not found or invalid student"
        )
    return result