from sqlalchemy.orm import Session
from features.attendance.models import Attendance
from features.projects.models import Project

def create_attendance_db(db: Session, student_id: str, project_id: int):
    # Cek apakah project_id valid/tersedia
    project = db.query(Project).filter(Project.id == project_id).first()
    if not project:
        return None

    new_attendance = Attendance(
        student_id=student_id,
        project_id=project_id,
        status="PRESENT"
    )
    db.add(new_attendance)
    db.commit()
    db.refresh(new_attendance)
    return new_attendance