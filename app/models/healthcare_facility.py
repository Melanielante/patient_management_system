
from sqlalchemy import Column, String, DateTime, Enum
from sqlalchemy.dialects.mysql import CHAR
from datetime import datetime
import uuid
from app.db.database import Base

class HealthcareFacility(Base):
    __tablename__ = "healthcare_facilities"

    facility_id = Column(CHAR(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String(255), nullable=False)
    facility_type = Column(Enum("hospital", "clinic", "pharmacy"), nullable=False)
    license_number = Column(String(100), unique=True, nullable=False)
    location = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
