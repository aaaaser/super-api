from datetime import datetime

def checkin_attendance_logic(student_id: int, project_id: int):
    if student_id <= 0 or project_id <= 0:
        return {"status": "failed", "message": "ID Siswa dan ID Proyek tidak valid"}
    
    return {
        "status": "success",
        "attendance_id": 501,
        "student_id": student_id,
        "project_id": project_id,
        "timestamp": datetime.now().isoformat(),
        "attendance_type": "CHECK_IN"
    }