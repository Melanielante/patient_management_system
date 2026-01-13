
from sqlalchemy import Column, String, DateTime, ForeignKey, Date
from sqlalchemy.dialects.mysql import CHAR
from datetime import datetime
import uuid
from app.db.database import Base

class Patient(Base):
    __tablename__ = "patients"

    patient_id = Column(CHAR(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(CHAR(36), ForeignKey("users.id"), nullable=False)
    national_id_encrypted = Column(String(255), nullable=False)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    date_of_birth = Column(Date, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
