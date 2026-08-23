# core/models.py
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from core.database import Base

class ProjectModel(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_order=True, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    client_name = Column(String(255), nullable=False)
    total_budget = Column(Float, nullable=False)
    status = Column(String(50), default="ON_PROGRESS")
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relasi ke tabel Absensi
    attendances = relationship("AttendanceModel", back_populates="project")


class AttendanceModel(Base):
    __tablename__ = "attendances"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, nullable=False, index=True)
    project_id = Column(Integer, ForeignKey("projects.id"), nullable=False)
    attendance_type = Column(String(20), default="CHECK_IN")
    timestamp = Column(DateTime, default=datetime.utcnow)

    # Relasi ke tabel Proyek
    project = relationship("ProjectModel", back_populates="attendances")