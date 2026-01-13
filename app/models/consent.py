# app/models/consent.py
from sqlalchemy import Column, String, DateTime, Enum, ForeignKey
from sqlalchemy.dialects.mysql import CHAR
from datetime import datetime
import uuid
from app.db.database import Base

class Consent(Base):
    __tablename__ = "consents"

    consent_id = Column(CHAR(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    patient_id = Column(CHAR(36), ForeignKey("patients.patient_id"), nullable=False)
    facility_id = Column(CHAR(36), ForeignKey("healthcare_facilities.facility_id"), nullable=False)
    consent_type = Column(Enum("view", "edit", "share"), nullable=False)
    granted_at = Column(DateTime, default=datetime.utcnow)
    expires_at = Column(DateTime, nullable=True)
    revoked_at = Column(DateTime, nullable=True)
    granted_by = Column(CHAR(36), nullable=False)  # patient user_id
    purpose = Column(String(255), nullable=False)
    status = Column(Enum("active", "expired", "revoked"), nullable=False, default="active")
