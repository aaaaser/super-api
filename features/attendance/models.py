from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from core.database import Base

class Attendance(Base):
    __tablename__ = "attendances"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(String, nullable=False, index=True)
    project_id = Column(Integer, ForeignKey("projects.id"), nullable=False)
    status = Column(String, default="PRESENT")  # PRESENT, LATE, ABSENT
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relasi ke tabel projects (opsional)
    project = relationship("Project", back_populates="attendances")