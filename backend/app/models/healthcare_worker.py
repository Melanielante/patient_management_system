
from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.dialects.mysql import CHAR
from datetime import datetime
import uuid
from app.db.database import Base

class HealthcareWorker(Base):
    __tablename__ = "healthcare_workers"

    worker_id = Column(CHAR(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(CHAR(36), ForeignKey("users.id"), nullable=False)
    facility_id = Column(CHAR(36), ForeignKey("healthcare_facilities.facility_id"), nullable=False)
    license_number = Column(String(100), nullable=False)
    job_title = Column(String(100), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
