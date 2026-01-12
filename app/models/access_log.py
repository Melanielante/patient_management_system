
from sqlalchemy import Column, String, DateTime, Enum, ForeignKey
from sqlalchemy.dialects.mysql import CHAR
from datetime import datetime
import uuid
from app.db.database import Base

class AccessLog(Base):
    __tablename__ = "access_logs"

    log_id = Column(CHAR(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    patient_id = Column(CHAR(36), ForeignKey("patients.patient_id"), nullable=False)
    accessed_by = Column(CHAR(36), ForeignKey("healthcare_workers.worker_id"), nullable=False)
    facility_id = Column(CHAR(36), ForeignKey("healthcare_facilities.facility_id"), nullable=False)
    action = Column(Enum("view", "edit", "share"), nullable=False)
    result = Column(Enum("allowed", "denied"), nullable=False)
    reason = Column(String(255), nullable=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    ip_address = Column(String(50), nullable=False)
